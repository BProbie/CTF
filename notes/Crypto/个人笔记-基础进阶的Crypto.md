# RSA

## 经典RSA

### 例题1

#### 加密

```python
from Crypto.Util.number import *
from secret import flag

e = 0x10001

p = getPrime(512)
q = getPrime(512)
n = p * q

m = bytes_to_long(flag)

c = pow(m, e, n)
```

#### 解密

```python
from Crypto.Util.number import *

p = 
q = 
n = p * q
phi_n = (p-1) * (q-1)

e = 0x10001

d = inverse(e, phi_n)

m = pow(c, d, n)
raw = long_to_bytes(m)

flag = raw.decode()
```



## 共素数RSA (Common Prime RSA)

### 教程

```html
https://hasegawaazusa.github.io/common-prime-rsa.html
```



### 例题1

#### 加密

```python
from Crypto.Util.number import *
try:
    gcd
except NameError:
    from math import gcd

def gen_prime(nbits: int, gamma: float):
    g = getPrime(int(nbits * gamma))
    alpha = 0.5 - gamma
    while True:
        a = getRandomNBitInteger(int(alpha * nbits))
        p = 2 * g * a + 1
        if isPrime(p):
            b = getRandomNBitInteger(int(alpha * nbits))
            q = 2 * g * b + 1
            h = 2 * g * a * b + a + b
            while not isPrime(q) or isPrime(h) or gcd(a, b) != 1:
                b = getRandomNBitInteger(int(alpha * nbits))
                h = 2 * g * a * b + a + b
                q = 2 * g * b + 1
            return p, q
print(gen_prime(512, 0.48))
```

#### 解密

##### logN(g)≈1/2

```python
import random
try:
    gcd
except NameError:
    from math import gcd

def rho(N):
    f = lambda x: (pow(x, N-1, N) + 3) % N
    while True:
        # 加快入环速度
        t = random.randint(2, N)
        h = f(t)
        step_times = 0
        step_limit = 2
        while True:
            if not step_times < step_limit:
                step_times = 0
                step_limit *= 2
                t = h
                h = f(h)
            p = gcd(abs(int(t) - int(h)), N)
            if p == N:
                break
            elif p > 1:
                return (p, N // p)
            else:
                h = f(h)
                step_times += 1

print(rho(84236796025318186855187782611491334781897277899439717384242559751095347166978304126358295609924321812851255222430530001043539925782811895605398187299748256080526691975084042025794113521587064616352833904856626744098904922117855866813505228134381046907659080078950018430266048447119221001098505107823645953039))
```

##### logN(g)≈1/4

**`sage`**

```sage
from sage.groups.generic import bsgs

g = 28838314918840273611038952856252141148393903858815521699377328440901497
N = 23895816238623712091906549349650291003358466897973970818205381234024572750472476312894286233088847723906345049342176974080465940396626170377635736786780099297743807402105462746828310247313063710700453371777283064626446124365885063073122303271609231832129823571694756234973129694217982548355078107610764879363
nbits = 1024
gamma = 0.23
cbits = ceil(nbits * (0.5 - 2 * gamma))

M = (N - 1) // (2 * g)
u = M // (2 * g)
v = M - 2 * g * u
GF = Zmod(N)
x = GF.random_element()
y = x ^ (2 * g)
# c的范围大概与N^(0.5-2*gamma)很接近
c = bsgs(y, y ^ u, (int(2**(cbits-1)), int(2**(cbits+1))))
ab = u - c
apb = v + 2 * g * c
P.<x> = ZZ[]
f = x ^ 2 - apb * x + ab
a = f.roots()
if a:
    a, b = a[0][0], a[1][0]
    p = 2 * g * a + 1
    q = 2 * g * b + 1
    assert p * q == N
```

##### 已知a,b

**`sage`**

```sage
a = 1185431345934512
b = 1989628969125971
N = 54692260436051338814890781701826055707958209029414126894070449935683071253184867947357262267840171428710181955973010913204514025135188192484651672240708141692701667242130748316666406528479191422804307020656050201187035928715833163999813216597718706449260040885862566373392398826670863398295350419792842640631
P.<g> = ZZ[]
f = 4 * a * b * g ^ 2 + 2 * (a + b) * g - N + 1
g = f.roots()
if g:
    g = g[0][0]
    p = 2 * g * a + 1
    q = 2 * g * b + 1
    assert p * q == N
```

##### 已知g

######   g > a + b

**`sage`**

```sage
g = 2056971706333850947354991471886113601423457483931388832864204860321308350537317091564919029078296379733989138742162694786565228112885684303
N = 67324909911911622626246005558967775211455024820506932698435813321567574468019013664789401988015894964099052816176029553245881317276340043887466584645914352982274378611180595397686920214079479901514703963131435008906250160656759300390805929849374653321934393399433471228218819498373221757779799476717494079667
M = (N - 1) // (2 * g)
c = M % g
P.<a> = ZZ[]
f = 2 * g * a ^ 2 - 2 * g * c * a + M - c
a = f.roots()
if a:
    a, b = a[0][0], a[1][0]
    p = 2 * g * a + 1
    q = 2 * g * b + 1
    assert p * q == N
```

###### g = a + b

**`sage`**

```sage
g = 2855372645569408464444580237486670388029956719716115953907612135874419892154982850222965560661211729647325085879529571229774148545656169021
N = 159549169988238873893531105042878385551537587717347282632324748268846735710748763722602882823022008548774298858161130258369850715542192739582830583643642436399008902770027668038725347353393047833875066622910131525247842517372845617227325882916166114361718015983671803859502931814932543107911548450229250776542101141849788751722460468073974316977656001286989710480324512919121409123619799426221232443036698458643438020098037548757403
M = (N - 1) // (2 * g)
P.<a> = ZZ[]
f = 2 * a ^ 2 - 2 * g * a + (N - 1) // (2 * g ^ 2) - 1
a = f.roots()
if a:
    a, b = a[0][0], a[1][0]
    p = 2 * g * a + 1
    q = 2 * g * b + 1
    assert p * q == N
```



### 例题2 (强网杯2024-EasyRSA)

#### 加密

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

#### 解密

##### python

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
C = 3657145329109399421118487507342086209154249658246027816909711331681502841894307019782408594896074985187112151367537397288510083367722326554204893742802338351276672927516452624199068623713531789905014236979561598659634925789470632720772928838077259579613844984493706430796116592518511907671796131164951914532897947597906310544751670523089201643171695263167433884852481543729381168553209305916423519995801936969752610120486972291638827395644070225763602627850659111989991799584577439758777767233806926601773839822484036166907443952389120568889885305356206052019785749511714814218869305185506765531879276774411927901438

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

##### sage

```sage
N=54642322838521966106812419124141939188989640814860878861908076164639367595914512196689546261469345514255441116302800139668437203232194709285409075862419734007902906374266399946334745212375047784704524011282117381662325280446704897787659122983658402386409111680527237824015035597005313191262677046034069311159229487077629209355803968123085023774573470039717820771904932963580385259183454286138826580540970458295849974865118842313357636425032600607639797650353675780470249861726402474026943128529940611865467085977350731870140237435132883515585257875892835970695457915025407153187085139372317622088931196367733198938707
e=65537
g=3040871967959800581351382295274005388082419270793259228509099272494086612979335548205806725469849481228948811909984262857772287453967175931780503026101
enc=3657145329109399421118487507342086209154249658246027816909711331681502841894307019782408594896074985187112151367537397288510083367722326554204893742802338351276672927516452624199068623713531789905014236979561598659634925789470632720772928838077259579613844984493706430796116592518511907671796131164951914532897947597906310544751670523089201643171695263167433884852481543729381168553209305916423519995801936969752610120486972291638827395644070225763602627850659111989991799584577439758777767233806926601773839822484036166907443952389120568889885305356206052019785749511714814218869305185506765531879276774411927901438
nbits = 1024
gamma = 500/(1024*2)
cbits = ceil(nbits * (0.5 - 2 * gamma))

M = (N - 1) // (2 * g)
u = M // (2 * g)
v = M - 2 * g * u
GF = Zmod(N)
x = GF.random_element()
y = x ^ (2 * g)
# c的范围大概与N^(0.5-2*gamma)很接近
c = bsgs(y, y ^ u, (2**(cbits-1), 2**(cbits+1)), operation='*')
#(a, b, bounds, operation='*', identity=None, inverse=None, op=None)
ab = u - c
apb = v + 2 * g * c
P.<x> = ZZ[]
f = x ^ 2 - apb * x + ab
a = f.roots()
if a:
    a, b = a[0][0], a[1][0]
    p = 2 * g * a + 1
    q = 2 * g * b + 1
    assert p * q == N

from Crypto.Util.number import *
print(long_to_bytes(int(pow(enc,inverse(e,(p-1)*(q-1)),N))))
```

