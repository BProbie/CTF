# [个人] 零基础的MISC笔记



# 已知明文攻击

## 获取Keys

```shell
bkcrack -C flag.zip -c hint.txt -p hint.txt
```

```
bkcrack -C flag.zip -c hint.txt -P hint.zip -p hint.txt
```

## 解压压缩包

```shell
bkcrack -C flag.zip -k a923d145 ecc0362d 296a6ff5 -U 123456.zip 123456
```

## 解压单文件

```shell
bkcrack -C flag.zip -c flag.txt -k a923d145 ecc0362d 296a6ff5 -d flag.txt
```
