# [个人队伍] NSSCTF2026下旬的Writeup

> **2026年00月00日00:00 ~ 2026年00月00日00:00**
>
> **比赛地址：https://www.nssctf.cn/**
>
> **复现地址：https://www.nssctf.cn/**

> 官方简介



# 2026年下旬



## Crtpto



### [强网杯 2024]EasyRSA

#### 题目介绍

> 399分
>
> CRYPTO
>
> 
>
> 
>
> 题目描述
>
> easy的RSA。
>
> 该题目复现环境尚未取得主办方及出题人相关授权，如果侵权，请联系管理员删除。

---

#### 解题过程

##### 1. 查看题目

```python
#encoding:utf-8
from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime
import random, gmpy2

class RSAEncryptor:
	def __init__(self):
		self.g = self.a = self.b = 0
		self.e = 65537
		self.factorGen()
		self.product()

	def factorGen(self):
		while True:
			self.g = getPrime(500)
			while not gmpy2.is_prime(2*self.g*self.a+1):
				self.a = random.randint(2**523, 2**524)
			while not gmpy2.is_prime(2*self.g*self.b+1):
				self.b = random.randint(2**523, 2**524)
			self.h = 2*self.g*self.a*self.b+self.a+self.b
			if gmpy2.is_prime(self.h):
				self.N = 2*self.h*self.g+1
				print(len(bin(self.N)))
				return

	def encrypt(self, msg):
		return gmpy2.powmod(msg, self.e, self.N)


	def product(self):
		with open('/flag', 'rb') as f:
			self.flag = f.read()
		self.enc = self.encrypt(self.flag)
		self.show()
		print(f'enc={self.enc}')

	def show(self):
		print(f"N={self.N}")
		print(f"e={self.e}")
		print(f"g={self.g}")


RSAEncryptor()
```

**分析**

- 共素数RSA (Common Prime RSA) -> https://hasegawaazusa.github.io/common-prime-rsa.html

##### 2. 编写脚本

```python
from Crypto.Util.number import bytes_to_long, long_to_bytes
from gmpy2 import iroot, mpz, powmod, invert
from multiprocessing import Pool, cpu_count, Value, Manager
import math
import time
from datetime import datetime

N = 54642322838521966106812419124141939188989640814860878861908076164639367595914512196689546261469345514255441116302800139668437203232194709285409075862419734007902906374266399946334745212375047784704524011282117381662325280446704897787659122983658402386409111680527237824015035597005313191262677046034069311159229487077629209355803968123085023774573470039717820771904932963580385259183454286138826580540970458295849974865118842313357636425032600607639797650353675780470249861726402474026943128529940611865467085977350731870140237435132883515585257875892835970695457915025407153187085139372317622088931196367733198938707
e = 65537
g = 3040871967959800581351382295274005388082419270793259228509099272494086612979335548205806725469849481228948811909984262857772287453967175931780503026101
C = 2943043642353328002876864807982430088155660822875620826904788027826791235694668929126605073008611413080545304228241315652914389365950973553948468198195371326905729558415048914150798032186503571933339483143249392641011625692150494418151768085058864814515527963235510367111731516712421523064653073080703922008383628514363876763544334441608554731878181193253138408301552775095820668011549737562728268234635193691457580590888335159170642760998742172559080197161030658057527202339796434963046059298938197535006830683224845729879670756048295724543749759587267935803780444044244976305081493659058863559940653813796735799062

# 预计算一些常量
h = (N - 1) // g
u = h // g
v = h % g


def format_time(seconds):
    """格式化时间显示"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"


def print_progress(progress, elapsed_time):
    """打印进度信息"""
    if progress > 0:
        estimated_total = elapsed_time / (progress / 100)
        remaining = estimated_total - elapsed_time
        print(f"\r进度: {progress:.2f}% | 已用时间: {format_time(elapsed_time)} | 预计剩余: {format_time(remaining)}",
              end="", flush=True)


def check_range(args):
    start, end, D, b, u, N = args
    final = powmod(b, u, N)

    for r in range(start, end):
        base = powmod(b, r * D, N)
        for s in range(D):
            if (base * powmod(b, s, N)) % N == final:
                return r * D + s
    return None


def Solve_c():
    sqrt_N = int(iroot(mpz(N), 2)[0])
    C = int(sqrt_N // (g ** 2))

    a = 2
    b = powmod(a, g, N)

    # 优化搜索范围
    for i in range(2, C):
        D = (int(iroot(C, 2)[0]) + 1) * i
        print(f"\n开始新的搜索轮次 i={i}, D={D}")

        # 并行处理搜索
        num_processes = cpu_count()
        chunk_size = math.ceil(D / num_processes)
        ranges = []

        for j in range(num_processes):
            start = j * chunk_size
            end = min((j + 1) * chunk_size, D)
            ranges.append((start, end, D, b, u, N))

        search_start_time = time.time()
        completed_chunks = 0
        total_chunks = len(ranges)

        with Pool(processes=num_processes) as pool:
            for result in pool.imap_unordered(check_range, ranges):
                completed_chunks += 1
                progress = (completed_chunks / total_chunks) * 100
                elapsed = time.time() - search_start_time
                print_progress(progress, elapsed)

                if result is not None:
                    print("\n找到结果！")
                    return result

    return None


def main():
    start_time = time.time()

    print(f"开始求解... {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"使用 {cpu_count()} 个CPU核心进行并行计算")

    c = Solve_c()
    if c is None:
        print("\n未找到有效的 c 值")
        return

    print(f"\n找到 c: {c}")

    print("计算 x 和 y...")
    # 计算 x 和 y
    A = u - c
    B = v + c * g

    delta = iroot(B * B - 4 * A, 2)[0]
    x = (B + delta) // 2
    y = (B - delta) // 2

    print("计算 p 和 q...")
    # 计算 p 和 q
    a = x // 2
    b = y // 2
    p = int(2 * g * a + 1)
    q = int(2 * g * b + 1)

    print("计算私钥并解密...")
    # 计算私钥并解密
    phi = (p - 1) * (q - 1)
    d = invert(e, phi)
    m = powmod(C, d, N)

    end_time = time.time()
    total_time = end_time - start_time

    print(f"\n总计用时: {format_time(total_time)}")

    try:
        flag = long_to_bytes(m).decode(errors='ignore')
        print(f"解密结果: {flag}")
        if flag.startswith("flag"):
            print(f"找到的 flag: {flag}")
    except:
        print("解密结果转换失败")


if __name__ == "__main__":
    main()
```

```shell
D:\Environment\python\python-3.13.0\python.exe D:\Work\study\python\exp.py 
开始求解... 2026-10-15 23:03:23
使用 32 个CPU核心进行并行计算

开始新的搜索轮次 i=2, D=10056
进度: 3.12% | 已用时间: 00:00:43 | 预计剩余: 00:22:14
找到结果！

找到 c: 51797621
计算 x 和 y...
计算 p 和 q...
计算私钥并解密...

总计用时: 00:00:43
解密结果: NSSCTF{99935876-63d2-4e81-83d8-5e031ca666e6}

进程已结束，退出代码为 0
```

---

#### 题目答案

##### Flag

```flag
NSSCTF{99935876-63d2-4e81-83d8-5e031ca666e6}
```











## Web



### [NCTF 2018]签到题

#### 题目介绍

> 1分
>
> HTTP协议信息收集PHP
>
> 
>
> 
>
> 题目描述
>
> 真的不能再简单了
> 得到的flag使用NSSCTF{}格式提交。

---

#### 解题过程

##### 1. 开发者工具Network

Ctrl+Shift+I -> Network

##### 2. 访问题目

http://node4.anna.nssctf.cn:28788/

```shell
nctf2018	flag{w3lc0m3_t0_nctf2018hhhhhhhhhhhh}
```

---

#### 题目答案

##### Flag

```flag
NSSCTF{w3lc0m3_t0_nctf2018hhhhhhhhhhhh}
```





































# 成果

## 解题

- **0 / ?**
