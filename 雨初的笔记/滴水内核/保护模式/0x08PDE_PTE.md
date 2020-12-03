+ `windows` 下一个页的大小通常是 `4KB = 4096字节` 	

+ 一个PTE可以指向多个物理页

+ PTE可以没有物理页，比如一个进程的0地址，PTE为0，没有挂载物理页。而如果想要往0地址写数据，很简单，给他挂上一个物理页就可以。

  ![image-20201128203220245](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201128203220245.png)

+ 海哥视频没演示，怎么挂物理页？ `ed` 一下？

  ![image-20201128203553057](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201128203553057.png)

  ![image-20201128203628119](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201128203628119.png)

  就是把0地址挂到这个地址指向的物理页上

+ 注意第一和第二张表存的是地址，大小是4字节，所以要乘4

+ 晚上修复一下环境，试一下给0地址挂物理页。

  ```
  [boot loader]
  timeout=30
  default=multi(0)disk(0)rdisk(0)partition(1)\WINDOWS
  [operating systems]
  multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional [DEBUG]" execute=optin /fastdetect /debug /debugport=com1
  multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional" /noexecute=optin /fastdetect
  
  
  [boot loader]
  timeout=30
  default=multi(0)disk(0)rdisk(0)partition(1)\WINDOWS
  [operating systems]
  multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional [DEBUG]" /DEBUG /DEBUGPORT=bazis /fastdetect /execute=optin
  multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional" /noexecute=optin /fastdetect
  
  ```

  ![image-20201128204320952](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201128204320952.png)

  + 先看PDE与PTE的P位 **P=1** 才是有效的物理页

  + R/W = 0 只读

    R/W = 1 可读可写

  + U/S = 0 特权用户

    U/S = 1 普通用户

  + ![image-20201128210439031](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201128210439031.png)

    PTE里面没有 `P/S` 位，只有 `PAT` ，白皮书里面好像说这个是对于某些特定CPU有用，如果没用的话就置为0

  + ![image-20201128210904693](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201128210904693.png)

  + ![image-20201128210951859](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201128210951859.png)