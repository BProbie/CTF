# [个人] 零基础的逆向笔记



# Python逆向

## 1. exe到pyc

```shell
python D:\Environment\pyinstxtractor\pyinstxtractor-2025.2\pyinstxtractor.py exe.exe
```

## 2. pyc到py

### 2.1 查看python版本

```shell
file pyc.pyc
```

### 2.2 获取python版本魔术数

```python
import importlib.util

print(importlib.util.MAGIC_NUMBER.hex())
```

### 2.3 修改pyc魔术数

### 2.4 反编译成py

#### 2.4.1 uncompyle6

```shell
pip install uncompyle6
```

```shell
uncompyle6 pyc.pyc
```

#### 2.4.2 decompyle3

```shell
pip install decompyle3
```

```shell
decompyle3 pyc.pyc
```

#### 2.4.3 pycdc

```shell
git clone https://gitcode.com/GitHub_Trending/py/pycdc
```

```shell
cd pycdc
```

将`MinGW64\bin`的三个`dll`文件扔进`pycdc`静态编译

| **libstdc++-6.dll**     | **C++ 标准库**   |
| ----------------------- | ---------------- |
| **libgcc_s_seh-1.dll**  | **GCC 运行时库** |
| **libwinpthread-1.dll** | **线程库**       |

```shell
cmake -G "MinGW Makefiles" ^
-DCMAKE_BUILD_TYPE=Release ^
-DCMAKE_CXX_FLAGS="-static -static-libgcc -static-libstdc++" ^
-DCMAKE_EXE_LINKER_FLAGS="-static -static-libgcc -static-libstdc++" .
```

```shell
mingw32-make
```

得到`pycdc.exe`和`pycdas.exe`

##### 2.4.3.1 反编译

```shell
pycdc pyc.pyc
```

##### 2.4.3.2 反汇编

```shell
pycdas pyc.pyc
```
