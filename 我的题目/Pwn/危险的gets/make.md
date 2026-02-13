# 危险的gets

## 编写题目

```c
/* pwn.c */

#include <stdio.h>
#include <stdlib.h>

int backdoor() {
    puts("congratulation!");
    system("/bin/sh");
    return 0;
}

int main() {
    char buf[64];
    gets(buf);
    return 0;
}
```

## 编译题目

```shell
probie@Probie:/mnt/d/Work/ctf/challenges/mine/Pwn/危险的gets$ gcc -g -std=c90 -fno-stack-protector -no-pie pwn.c -o pwn
```

## 下载docker

```shell
probie@Probie:/mnt/d/Work/ctf/challenges/mine/Pwn/危险的gets$ sudo apt-get update
```

```shell
probie@Probie:/mnt/d/Work/ctf/challenges/mine/Pwn/危险的gets$ sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
```

```shell
probie@Probie:/mnt/d/Work/ctf/challenges/mine/Pwn/危险的gets$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

```shell
probie@Probie:/mnt/d/Work/ctf/challenges/mine/Pwn/危险的gets$ echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

```shell
probie@Probie:/mnt/d/Work/ctf/challenges/mine/Pwn/危险的gets$ sudo apt-get update
```

```shell
probie@Probie:/mnt/d/Work/ctf/challenges/mine/Pwn/危险的gets$ sudo apt-get install docker-ce docker-ce-cli containerd.io
```

```shell
probie@Probie:/mnt/d/Work/ctf/challenges/mine/Pwn/危险的gets$ cat /etc/os-release 
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

```shell
probie@Probie:/mnt/d/Work/ctf/challenges/mine/Pwn/危险的gets$ sudo docker run -it --name ubuntu-linux-pwn-ctf ubuntu:latest /bin/bash
```

```shell
probie@Probie:/mnt/d/Work/ctf/challenges/mine/Pwn/危险的gets$ sudo docker ps -a
```

```shell
CONTAINER ID   IMAGE           COMMAND       CREATED        STATUS          PORTS     NAMES
1e771be0d529   ubuntu:latest   "/bin/bash"   26 hours ago   Up 35 minutes             ubuntu-linux-pwn-ctf
```

```shell
probie@Probie:/mnt/d/Work/ctf/challenges/mine/Pwn/危险的gets$ sudo docker start ubuntu-linux-pwn-ctf
```

```shell
probie@Probie:/mnt/d/Work/ctf/challenges/mine/Pwn/危险的gets$ sudo docker exec -it ubuntu-linux-pwn-ctf /bin/bash
```

## 下载wget

```shell
root@1e771be0d529:/ngrok# apt update
```

```shell
root@1e771be0d529:/ngrok# apt install -y wget unzip
```

## 下载ngrok

```shell
root@1e771be0d529:/ngrok# mkdir -p /ngrok && cd /ngrok
```

```shell
root@1e771be0d529:/ngrok# wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
```

```shell
root@1e771be0d529:/ngrok# tar -zxvf ngrok-v3-stable-linux-amd64.tgz
```

## 拷贝题目

```shell
root@1e771be0d529:/ngrok# mkdir /pwn
```

```shell
probie@Probie:/mnt/d/Work/ctf/challenges/mine/Pwn/危险的gets$ sudo docker cp pwn ubuntu-linux-pwn-ctf:/pwn
```

```shell
root@1e771be0d529:/ngrok# chmod +x /pwn/pwn
```

## 添加Flag

```shell
root@1e771be0d529:/ngrok# cat > /pwn/flag << EOF
flag{probie}
EOF
```

## 开放端口

```shell
root@1e771be0d529:/ngrok# nohup socat TCP-LISTEN:9999,fork,reuseaddr EXEC:/pwn/pwn > pwn/pwn.log 2>&1 &
```

```shell
root@1e771be0d529:/ngrok# ./ngrok tcp 9999
```

```shell
ngrok                                                                                                   (Ctrl+C to quit)

🧠 Call internal services from your gateway: https://ngrok.com/r/http-request

Session Status                online
Account                       BProbie (Plan: Free)
Version                       3.34.0
Region                        Japan (jp)
Web Interface                 http://127.0.0.1:4042
Forwarding                    tcp://0.tcp.jp.ngrok.io:11402 -> localhost:9999

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```

## 下载netcat

```shell
root@1e771be0d529:/ngrok# apt install -y socat netcat-traditional net-tools
```

## 测试连接

```shell
nc localhost 9999
```

```shell
nc 0.tcp.jp.ngrok.io 11402
```
