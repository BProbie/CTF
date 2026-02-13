# [个人队伍] XSWCTF2025热身赛的Writeup

3人赛

# XSWCTF2025热身赛

**59**支队伍已报名

开始时间

2025年11月7日上午9点00分

结束时间

2025年11月14日上午9点00分

本次比赛为**中山大学、华南师范大学、暨南大学**联合举办，由**暨大Xp0int团队、华师Sloth团队、中大W4terDr0p团队**联合命题

旨在培养同学们对网络安全竞赛的兴趣，寻找对网络安全技术感兴趣的小伙伴们

为 Xp0int、Sloth 、W4terDr0p 战队纳新挖掘优秀人才，注入新生力量

先来热个身吧，大家！



# Week1

## Misc

### 猜数字

#### 解题过程

下载解压得到wav直接扔进`Audacity`

对照参数表，查看多图层

| 按键 | 低频（Hz） | 高频（Hz） |
| ---- | ---------- | ---------- |
| 1    | 697        | 1209       |
| 2    | 697        | 1336       |
| 3    | 697        | 1477       |
| A    | 697        | 1633       |
| 4    | 770        | 1209       |
| 5    | 770        | 1336       |
| 6    | 770        | 1477       |
| B    | 770        | 1633       |
| 7    | 852        | 1209       |
| 8    | 852        | 1336       |
| 9    | 852        | 1477       |
| C    | 852        | 1633       |
| *    | 941        | 1209       |
| 0    | 941        | 1336       |
| #    | 941        | 1477       |
| D    | 941        | 1633       |

得到数字：1596#38952#73751#4185856

得到：flag{1596#38952#73751#4185856}



## web

### ez_php

#### 解题过程

创建实例，将代理复制粘贴到`websocket`中得到容器

用浏览器访问，查看源码

```php
<?php
include 'flag.php';
extract($_GET);
if (isset($wsf)) {
    $xmm = trim(file_get_contents($zm));
    if ($xmm == $wsf) {
        if (!empty($xlq)) {
            $xw = trim(file_get_contents($fn));
            if ($xlq === $xw) {

                echo "<p>$flag</p>";
            } else {
                echo '<p>no no no </p>';
            }
        } else 'You cant do that!!';
    } else {
        echo 'hacker!!';
    }
} else {
    highlight_file(__FILE__);
}
?>
```

**解读：**

- 它get了一些变量
- 然后是两个重要的判断`$wsf==trim(file_get_contents($zm))`和`$xlq==trim(file_get_contents($fn))`
- 重点是获得文件的内容，我们可以用data参数伪造一个文件内容，即`data://text/plain;base64,YQ==`

构造并发送payload

```
http://127.0.0.1:7839/?wsf=a&zm=data://a/;base64,YQ==&xlq=b&fn=data://b/;base64,Yg==
```

得到：flag{phP_lS_th9_be5T_l4ngUa9e}



# 后记

## 赠言

### 好好吃饭，认真睡觉。感谢相遇，铭记学习。——我就玩玩