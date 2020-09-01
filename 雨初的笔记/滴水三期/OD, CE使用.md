# OD

+ OD中 `ctrl + G` 跳转到某一指定地址。

+ OD中命令 `dd xxxxx` 是 **data DWORD** 的意思，以DWORD为单位查看数据。如果是 `db xxxx` 就是 `data BYTE` 以字节为单位查看数据。

+ `ctrl + f9` 执行完这个函数并断在 `retn` 那里。 `f8` 下一步（返回），这样可以回到调用这个函数的那个  `call` 的下一行。

+ 在内存窗口中转到表达式 `ctrl + g`

  ![image-20200824200509769](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200824200509769.png)

# CE

+ 在CE中，如果是基址，显示为 **绿色** 。重启后也不会改变地址。但是如果显示为 **黑色** ，说明这个变量是在 **堆** 里面（用 `new` 或者 `malloc` ）分配的，重启之后地址会改变。

+ 在CE中找指针要勾上 `pointer`

+ [CE练习](https://www.cnblogs.com/LyShark/p/10799926.html)第七关的时候第二层是 `mov [ESI], ESI` 。由于CE默认采用硬件断点的方式，断点只能停在指令执行之后，而这条指令正好是把 esi 原来指向的地址中的值再赋值给 esi，所以执行之后 esi 的值已经是被覆盖掉的值了，而我们想知道的恰恰是执行这条指令之前的 esi 值， esi 就是这个我们监视的地址。

+ x32dbg.ini / x64dbg.ini 可以设置配色

+ ![image-20200820103447643](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200820103447643.png)

  这个可以设置高亮模式
  
+ `pushad` 之后 `popad` ，**标志寄存器** 里面的值并不会被改变。

+ `pushfd` 可以保存标志寄存器的值。之后再 `popfd` 恢复。