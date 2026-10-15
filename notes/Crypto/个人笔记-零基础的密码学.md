# [个人] 零基础的密码学笔记



# 进制转换

## 公式

### 定义法

```python
def changeNumBase(num: any, toBase: any = 10) -> str:
    chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    if num == 0:
        return "0"
    is_negative = False
    if num < 0:
        is_negative = True
        num = abs(num)
    res = ""
    while num > 0:
        remainder = num % toBase
        res = chars[remainder] + res
        num = num // toBase
    return "-" + res if is_negative else res
```



# 取模 mod

## 定义

```python
a % b = c
```

## 公式

### 定义法

```python
a = b * i + c
b = (a - c) // i
```



# 最大公因数 gcd

## 公式

### 定义法

```python
from gmpy2 import gmpy2

g = gmpy2.gcd(a1, a2)
```



# 逆元 inv_n

## 公式

### 定义法

```python
inv_s = pow(s, -1, n)
```

## 应用

### 逆元等价

```python
c = (m * s) % n
m = (c / s) % n = (c * inv_s) % n
```



# 同余 ≡

## 定义

```python
a ≡ b (mod n)
(a - b) % n == 0
```

## 公式

### 定义法

```python
a = n * i + b
n = (a - b) // i
```



# 欧拉函数 Φ(n) | phi_n

## 定义

```python
# 若
n = p * q

# 则
phi_n = (p - 1) * (q - 1)
```

```python
# 若
n = pow(p, 3) * pow(q, 2)

# 则
phi_n = (pow(p, 2) * (p - 1)) * (q * (q - 1))
```



## 公式

### 工具库法

```python
from sympy import factorint

p, q = list(factorint(n).keys())
phi_n = (p - 1) * (q - 1)
```

```python
from galois import euler_phi

phi_n = euler_phi(n)
```



## 应用

### 欧拉降级

```python
d = inverse(e, phi_n) # 私钥
m = pow(c, d, n) # 明文
```

```python
# 超大指数
l = pow(2, pow(2,t), n)

# 欧拉降级
l = pow(2, pow(2,t,phi_n), n)
```



# 欧拉定理

## 公式

### 定义法

```python
gcd(m, n) = 1
m ** phi_n ≡ 1 (mod n)
```



# pow中pow

## 公式

### 定义法

```python
# 若
a = pow(b, a1, n)
b = pow(c, a2, n)

# 则
a = pow(c, a1*a2, n)
```

## 应用

### 代入消元

```python
# 已知
s = pow(y, k, p)
y = pow(g, x, p)
c = pow(g, k, p)

# 得到
s = pow(y, k, p) = pow(g, x*k, p) = pow(c, x, p)
```



# 分解大素数积 n

## 定义

```python
p = getPrime(512)
q = getPrime(512)
n = p * q
```

## 公式

### 工具库法

```python
from sympy import factorint

p, q = list(factorint(n).keys())
```

### 网站法

```html
https://tools.qsnctf.com/crypto/rsa_factordb
```



# 小公钥e漏洞攻击

## 定义

```python
e = 3 # 小公钥
c = pow(m, e, n)
```

## 公式

### 定义法

```python
from Crypto.Util.number import *
from gmpy2 import iroot

m = iroot(c, e)[0]
flag = long_to_bytes(m).decode()
```



# p、q、n、phi_n、d、e、m、c、flag的基本运算关系

## 定义

```python
n = p * q
phi_n = (p - 1) * (q - 1)

e * d ≡ 1 (mod phi_n)
phi_n = (e * d - 1) // k # k <= e

d = inverse(e, phi_n)

c = pow(m, e, n)
m = pow(c, d, n)

m = bytes_to_long(flag.encode())
flag = long_to_bytes(m).decode()

p < iroot(n, 2)[0] < q
```

## 公式

### 定义法

```python
p < iroot(n, 2)[0] < q
```

## 例题

### 例题一

#### 题目

```python
from Crypto.Util.number import *
from gmpy2 import next_prime
from functools import reduce
from secret import flag

assert len(flag) == 38
assert flag[:7] == b'moectf{'
assert flag[-1:] == b'}'

def main():
    p = getPrime(512)
    q = int(reduce(lambda res, _: next_prime(res), range(114514), p))

    n = p * q
    e = 65537

    m = bytes_to_long(flag)

    c = pow(m, e, n)
	
    print(f'{n = }')
    print(f'{c = }')

if __name__ == '__main__':
    main()

"""
n = 96742777571959902478849172116992100058097986518388851527052638944778038830381328778848540098201307724752598903628039482354215330671373992156290837979842156381411957754907190292238010742130674404082688791216045656050228686469536688900043735264177699512562466087275808541376525564145453954694429605944189276397
c = 17445962474813629559693587749061112782648120738023354591681532173123918523200368390246892643206880043853188835375836941118739796280111891950421612990713883817902247767311707918305107969264361136058458670735307702064189010952773013588328843994478490621886896074511809007736368751211179727573924125553940385967
"""
```

#### 题解

```python
from Crypto.Util.number import *
from gmpy2 import next_prime, iroot

n = 96742777571959902478849172116992100058097986518388851527052638944778038830381328778848540098201307724752598903628039482354215330671373992156290837979842156381411957754907190292238010742130674404082688791216045656050228686469536688900043735264177699512562466087275808541376525564145453954694429605944189276397
c = 17445962474813629559693587749061112782648120738023354591681532173123918523200368390246892643206880043853188835375836941118739796280111891950421612990713883817902247767311707918305107969264361136058458670735307702064189010952773013588328843994478490621886896074511809007736368751211179727573924125553940385967
e = 65537

sqrt_n = iroot(n, 2)[0]
q = next_prime(sqrt_n)

while True:
    if n % q == 0:
        p = n // q
        phi_n = (p - 1) * (q - 1)
        d = inverse(e, phi_n)
        m = pow(c, d, n)
        flag = long_to_bytes(m).decode()
        if flag.startswith("moectf{") and flag.endswith("}"):
            print(flag) # moectf{vv0W_p_m1nu5_q_i5_r34l1y_sm4lI}
            break
    q = next_prime(q)
```



# 共模攻击

## 定义

```python
c1 ≡ m ** e1 (mod n)
c2 ≡ m ** e2 (mod n)

# 等价于
c1 = pow(m, e1, n)
c2 = pow(m, e2, n)
```

## 公式

### 定义法

```python
from Crypto.Util.number import *
from gmpy2 import gmpy2

g, s1, s2 = gmpy2.gcdext(e1, e2)
m = pow(c1, s1, n) * pow(c2, s2, n) % n
flag = long_to_bytes(gmpy2.iroot(m, g)[0]).decode()

print(flag)
```

## 例题

### 例题一

#### 题目

```python
from Crypto.Util.number import *

p = getPrime(1024)

q = getPrime(1024)

N = p*q

e = 65537

msg = bytes_to_long(b"ISCTF{dummy_flag}")

ct1 = pow(msg, e, N)

ct2 = pow(msg, p+q, N)

print(f"{N = }")

print(f"{ct1 = }")

print(f"{ct2 = }")

"""
N = 17630258257080557797062320474423515967705950026415012912087655679315479168903980901728425140787005046038000068414269936806478828260848859753400786557270120330760791255046985114127285672634413513991988895166115794242018674042563788348381567565190146278040811257757119090296478610798393944581870309373529884950663990485525646200034220648901490835962964029936321155200390798215987316069871958913773199197073860062515329879288106446016695204426001393566351524023857332978260894409698596465474214898402707157933326431896629025197964209580991821222557663589475589423032130993456522178540455360695933336455068507071827928617
ct1 = 5961639119243884817956362325106436035547108981120248145301572089585639543543496627985540773185452108709958107818159430835510386993354596106366458898765597405461225798615020342640056386757104855709899089816838805631480329264128349465229327090721088394549641366346516133008681155817222994359616737681983784274513555455340301061302815102944083173679173923728968671113926376296481298323500774419099682647601977970777260084799036306508597807029122276595080580483336115458713338522372181732208078117809553781889555191883178157241590455408910096212697893247529197116309329028589569527960811338838624831855672463438531266455
ct2 = 11792054298654397865983651507912282632831471680334312509918945120797862876661899077559686851237832931501121869814783150387308320349940383857026679141830402807715397332316601439614741315278033853646418275632174160816784618982743834204997402866931295619202826633629690164429512723957241072421663170829944076753483616865208617479794763412611604625495201470161813033934476868949612651276104339747165276204945125001274777134529491152840672010010940034503257315555511274325831684793040209224816879778725612468542758777428888563266233284958660088175139114166433501743740034567850893745466521144371670962121062992082312948789
"""
```

#### 题解

```python
from Crypto.Util.number import *
from gmpy2 import gmpy2

n = 17630258257080557797062320474423515967705950026415012912087655679315479168903980901728425140787005046038000068414269936806478828260848859753400786557270120330760791255046985114127285672634413513991988895166115794242018674042563788348381567565190146278040811257757119090296478610798393944581870309373529884950663990485525646200034220648901490835962964029936321155200390798215987316069871958913773199197073860062515329879288106446016695204426001393566351524023857332978260894409698596465474214898402707157933326431896629025197964209580991821222557663589475589423032130993456522178540455360695933336455068507071827928617
c1 = 5961639119243884817956362325106436035547108981120248145301572089585639543543496627985540773185452108709958107818159430835510386993354596106366458898765597405461225798615020342640056386757104855709899089816838805631480329264128349465229327090721088394549641366346516133008681155817222994359616737681983784274513555455340301061302815102944083173679173923728968671113926376296481298323500774419099682647601977970777260084799036306508597807029122276595080580483336115458713338522372181732208078117809553781889555191883178157241590455408910096212697893247529197116309329028589569527960811338838624831855672463438531266455
c2 = 11792054298654397865983651507912282632831471680334312509918945120797862876661899077559686851237832931501121869814783150387308320349940383857026679141830402807715397332316601439614741315278033853646418275632174160816784618982743834204997402866931295619202826633629690164429512723957241072421663170829944076753483616865208617479794763412611604625495201470161813033934476868949612651276104339747165276204945125001274777134529491152840672010010940034503257315555511274325831684793040209224816879778725612468542758777428888563266233284958660088175139114166433501743740034567850893745466521144371670962121062992082312948789
e1 = 65537
e2 = n + 1

g, s1, s2 = gmpy2.gcdext(e1, e2)
m = pow(c1, s1, n) * pow(c2, s2, n) % n
flag = long_to_bytes(gmpy2.iroot(m, g)[0]).decode()

print(flag)
```



# BSGS大步小步

## 公式

### 定义法

```python
import math
from math import gcd

def BSGS(a: int, b: int, m: int) -> int | None:
    m = abs(m)
    b = b % m
    a = a % m

    if m == 1:
        return 1
    if b == 1:
        return 0
    if a == 0:
        return 1 if b == 0 else None

    d = 0
    g = gcd(a, m)
    while g != 1:
        if b % g != 0:
            return None
        d += 1
        m = m // g
        b = b // g
        a = a // g
        g = gcd(a, m)
        if b == 1:
            return d

    t = math.ceil(math.sqrt(m))
    hash_map = dict()
    aj = 1
    for j in range(t):
        val = (b * aj) % m
        if val not in hash_map:
            hash_map[val] = j
        aj = (aj * a) % m

    at = pow(a, t, m)
    ati = 1
    for i in range(1, t + 1):
        ati = (ati * at) % m
        if ati in hash_map:
            x_prime = i * t - hash_map[ati]
            x = x_prime + d
            if pow(a, x, m * (10 ** d)) == b % (m * (10 ** d)):
                return x
    return None
```

## 应用

### 大步小步

```python
(a ** x) ≡ b (mod m)
x = BSGS(a, b, m)
```

## 例题

### 例题一

#### 题目

```python
(13 ** flag) ≡ 114514 (mod 100000000000099) # 其中flag为最小整数
```

#### 题解

```python
flag = BSGS(13, 114514, 100000000000099)
print(f"moectf{{{flag}}}") # moectf{18272162371285}
```



# RSA

## 公式

### 定义法

#### 加密

```python
from Crypto.Util.number import * # 这里是经典密码学的工具库，应该不会陌生
from secret import m # 这里用import导入明文

m = bytes_to_long(m) # 明文m，这里是字节流表达
p = getPrime(512) # 第512位质数，这里是bit位，即质数p∈(2**511,2**512)，这里存在多解，确解可通过抓包获取
q = getPrime(512) # 第512位质数，这里是bit位，即质数q∈(2**511,2**512)，这里存在多解，确解可通过抓包获取

e = 65537 # 公钥e，一般都是小整数
n = p * q # 模数n
c = pow(m, e, n) # 密文c，这里等价于c=m**e%n
```

#### 解密

```python
from Crypto.Util.number import * # 一样的经典密码学的工具库

# 由加密过程和抓包得到的数据
p = getPrime(512) # 质数p，这里替换成确解
q = getPrime(512) # 质数q，这里替换成确解
e = 65537 # 公钥e
n = p * q # 模数n

phi_n = (p-1) * (q-1) # φ(n) = (p-1)*(q-1)
d = inverse(e, phi_n) # 私钥d直接调用逆模函数处理

m = pow(c, d, n) # 解密得到明文m的字节流表达
m = long_to_bytes(m) # 将字节流m转为字符串表示

flag = m.decode() # 解码明文成字符串byte -> str
```



# DES

## 碰撞

### 实战

```python
from Crypto.Cipher import DES
from random import randbytes

flag = b'moectf{???}'
print("Do u know the length of DES'key? That may be the key of DES.")
m = randbytes(8)
print("Here is the message. Please enter two different keys to generate the same ciphertext.")
print(m)
try:
    key1 = bytes.fromhex(input("input the first  key(hex): "))
    key2 = bytes.fromhex(input("input the second key(hex): "))
    des1 = DES.new(key=key1, mode=DES.MODE_ECB)
    c1 = des1.encrypt(m)
    des2 = DES.new(key=key2, mode=DES.MODE_ECB)
    c2 = des2.encrypt(m)
except:
    print("something wrong.")
    exit()

if key1 == key2:
    print("no cheat!")
    exit()

if c1 == c2:
    print("You did it! Here is the flag")
    print(flag)
    exit()
else:
    print("bye!")
    exit()
```

```shell
Key1 = 0000000000000000
Key2 = 0101010101010101
```

```shell
Key1 = c97c9edd4a196af3
Key2 = c97d9fdd4b196bf3
```



# AES



# 流密码

```python
import base64
key = b"0xGame_2026"
ct = base64.b64decode("fTAvKTQybl5VAXRHHA8JCygHfFZTWGYCIydUDQcBX0pVdkB3AwA3OVBnZAZpLxUJCSIZVFJYeAIiHysLPDV8AFFcYk0kUFRQEnpmCw==")
print(base64.b64decode(bytes(c ^ key[i % len(key)] for i, c in enumerate(ct))).decode())
```



# 椭圆曲线离散对数 (ECDLP)

## 1. 定义

```shell
Q = k · G

G：基点 (生成元)
Q：公钥点
k：私钥，bytes_to_long(flag)
```

## 2. 脚本

```sage
# y² = x³ + a x + b mod p

# ======================【这里改题目参数】======================
p = 380025560263444925282186340357451425457046895363401263284043
a = 3
b = 0
Gx = 89416635389252243162818482998273067753365476637225933437342
Gy = 246277781258250668709138589808946483685012465285148814183503
Qx = 329460413071651533403262472631632126805896556373758724864455
Qy = 299273891016902567464505544081763716760408274149519169100436
# ==============================================================

# 构造有限域上椭圆曲线 E: y² = x³ + a x + b mod p
E = EllipticCurve(GF(p), [a, b])

# 构造基点G、公钥点Q
G = E(Gx, Gy)
Q = E(Qx, Qy)

# 计算基点G的阶，并分解素因子（判断是否平滑，能否Pohlig-Hellman破解）
n = G.order()
print("[+] G点阶 n =", n)
print("[+] n素因子分解 factor(n):", factor(n))

# Sage内置discrete_log：自动识别平滑阶，调用Pohlig-Hellman求解ECDLP
# 求解 k * G = Q，得到私钥k
k = G.discrete_log(Q)
print("\n[+] secret k =", k)

# Sage Integer 转 Python原生int，才能调用to_bytes
k_py = int(k)

# 大端转字节串，还原 bytes_to_long(flag) 的逆运算
byte_len = (k_py.bit_length() + 7) // 8
flag_raw = k_py.to_bytes(byte_len, 'big')
print("\n[+] raw bytes =", flag_raw)

# 尝试utf8解码，CTF flag一般是可见字符串
try:
    flag_str = flag_raw.decode('utf-8')
    print("[+] flag(utf8) =", flag_str)
except UnicodeDecodeError:
    print("[!] 无法utf8解码，原始hex =", flag_raw.hex())
```
