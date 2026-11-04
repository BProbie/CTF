# 证书



## PFX



### 解密

```shell
# 提取证书（公钥）
openssl pkcs12 -in DESKTOP-KG7H8ET.pfx -clcerts -nokeys -out cert.pem -passin pass:ChangeMe

# 提取无加密私钥
openssl pkcs12 -in DESKTOP-KG7H8ET.pfx -nocerts -noenc -out privkey.pem -passin pass:ChangeMe

# 一次性导出证书+私钥到同一个PEM
openssl pkcs12 -in DESKTOP-KG7H8ET.pfx -noenc -out full.pem -passin pass:ChangeMe

# 查看pfx内部信息（校验密码是否正确）
openssl pkcs12 -in DESKTOP-KG7H8ET.pfx -info -noout -passin pass:ChangeMe
```

