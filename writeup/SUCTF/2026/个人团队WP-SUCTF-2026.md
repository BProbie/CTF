# [个人团队] SUCTF2026的Writeup

> **2026年3月14日9:00 ~ 2026年3月16日9:00**
>
> **比赛地址：[Contest](https://adworld.xctf.org.cn/page/mg/saas/contest/flag/c7b203698e6208554f1c3913d955ed70/ContestPage)**
>
> **复现地址：[Contest](https://adworld.xctf.org.cn/page/mg/saas/contest/flag/c7b203698e6208554f1c3913d955ed70/ContestPage)**

> # SUCTF 2026
>
> 主办方: XCTF联赛
>
> 赛事介绍
>
> SUCTF 2026
>
> ![SUCTF 2026](https://adworld.xctf.org.cn/assets/race_default_cover-DeflcrG9.png)
>
> ## SUCTF 2026
>
> 比赛时间：2026-03-14 09:00:00 ~ 2026-03-16 09:00:00
>
> 夺旗赛
>
> 
>
> ## 赛事简介 / Introduction
>
> 本届 SUCTF 2026 是由 XCTF 联赛的合作单位 SU 战队组织，赛宁网安提供技术支持。作为第十届 XCTF 国际联赛的分站赛，本次比赛采用在线网络安全夺旗挑战赛形式，面向全球开放。
> 此次比赛冠军队伍将直接晋级第十届 XCTF 总决赛（总决赛具体地点时间待定，将在确定后通知获得资格的国际和国内队伍）。其他参赛队伍也将获得积分，竞争 XCTF 总决赛的其他席位。
>
> SUCTF 2026 is a Jeopardy-style Online Capture The Flag Competition presented by SU, with technical support from Cynet Security. As a qualifying round of the 10th XCTF International League, the competition is open to participants worldwide. Teams can compete from any location. No restriction on the number of participants of any team.
> The Champion Team of SUCTF 2026 will be invited to The Finals of the 10th Edition of XCTF (location and date subject to change; qualified teams will be informed once the Finals details are confirmed). Other teams can also earn cumulative points to compete for other slots in The Finals.
>
> ------
>
> ## 比赛详情 / Competition Details
>
> ### 竞赛时间 / Competition Time
>
> - **开始**：2026年3月14日 09:00（北京时间） / March 14, 2026, 01:00 UTC
> - **结束**：2026年3月16日 09:00（北京时间） / March 16, 2026, 01:00 UTC
>   比赛时长为 48 小时 / The competition lasts 48 hours.
>
> ### 奖金设置 / Prizes
>
> | 名次  | 奖金（人民币）            | 备注                       |
> | ----- | ------------------------- | -------------------------- |
> | 第1名 | 8,000 元（20%个人所得税） | 直接晋级第十届 XCTF 总决赛 |
> | 第2名 | 5,000 元（20%个人所得税） |                            |
> | 第3名 | 3,000 元（20%个人所得税） |                            |
>
>  
>
> - 1st place: 8,000 CNY (20% tax included) + Qualified for The Finals of the 10th XCTF.
> - 2nd place: 5,000 CNY (20% tax included).
> - 3rd place: 3,000 CNY (20% tax included).
>
> ### 题目类别 / Challenge Categories
>
> - **Crypto**（密码学）
> - **Reverse**（逆向工程）
> - **Misc**（杂项）
> - **Pwn**（二进制漏洞利用）
> - **Web**（Web 安全）
>
> ### 得分与排名 / Scoring & Ranking
>
> 1. **Flag 格式**：大多数情况下，flag 形式为 `SUCTF{this_is_a_sample_flag}`，请提交包含 `SUCTF{}` 的完整 flag 以获得分数。如 flag 为其他格式，题目中会明确说明。
>    *In most cases, flags are of format `SUCTF{this_is_a_sample_flag}`. Please submit the entire flag, including `SUCTF{}`, for score. If flag is in other formats, it will be clarified in the challenge description.*
> 2. **动态计分**：每道题目的分值将根据解出队伍的数量动态计算。
>    *The score of each challenge will be dynamically calculated according to the number of solved teams.*
> 3. **排名规则**：最终排名根据每个队伍的总分确定。若多个队伍得分相同，则先达到该分数的队伍排名更高。
>    *Final ranking is determined by the total score of each team. In case of multiple teams with equal scores, the team that reached the score earlier ranks higher.*
>
> ### 竞赛规则 / Competition Rules
>
> - 参赛队伍如有任何违规行为，将被取消比赛资格。
>   *Teams breaking rules may be penalized or excluded from the competition.*
> - 禁止不同参赛队伍合作，或者共享 flag、hint 等任何比赛相关信息。
>   *It is not allowed for teams with independent accounts to cooperate, or share any flag/hints.*
> - 禁止攻击比赛平台，如果发现平台漏洞，请务必向我们报告。
>   *It is not allowed to attack the competition infrastructure. If flaws in the infrastructure are found, please report them to us.*
> - 禁止在比赛中妨碍其他队伍解题（例如解完题后破坏环境）。
>   *It is not allowed to sabotage or in any way hinder the progress of other competing teams. This includes attempting to destroy a challenge after you have completed it.*
> - 禁止往比赛平台发送大量流量，没有任何题目需要使用扫描器。
>   *It is not allowed to generate large amounts of traffic. None of the challenges can be solved by running automated scanners.*
> - 禁止对提交的 flag 进行爆破。
>   *It is not allowed to brute-force challenge flags/keys against the scoring site.*
> - 获奖队伍必须提交完整解题报告。
>   *For placing teams to receive prizes, they must submit a full and detailed writeup of each challenge, explaining how it was solved.*
> - 大赛主办方有权修改包括赛题、规则等一切事项。
>   *Organizers may rearrange/modify contest problems, proceedings, and rules.*
>
> ------
>
> ## 竞赛网址 / URL
>
> https://suctf2026.xctf.org.cn/
>
> ------
>
> ## 联系方式 / Contact
>
> - **Discord**：https://discord.gg/UYgPUn7eUH
> - **QQ 群**：935041519



# Day0



# Day1

## Misc

### SU_Signin

#### 题目信息

> SU_Signin
>
> 69PT
>
> Misc
>
> if you want it then you have to take it.
>
> https://ctftime.org/team/29641

#### 解题过程

**浏览网页**

```shell
If you want to join us to be a suer,you can fill in https://forms.office.com/r/YxbUJJ3i78

SSUUCCTTFF{{WW33llcc00mmee__22__SSUUCC77FF22002266!!!!!!!!}}
```

#### 题目答案

**得到：SSUUCCTTFF{{WW33llcc00mmee22SSUUCC77FF22002266!!!!!!!!}}**



# 队伍

## 名称

**F1ux**



## 口号

**F1ux**



## 成员

### 队长

- **F1uxTeam**

### 队员

- **probie等24位队员**



## 留言

### F1uxTeam

- **暂无**

### probie

- **暂无**



## 成果

### 排名

- **1 / n**

### 解题

- **13 / n**

### 分数

- **6673 / n**