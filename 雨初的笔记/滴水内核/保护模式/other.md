[TOC]

+ 一个进程最多能访问的物理地址为 `1024 * 1024 * 4096 = 4GB` （10-10-12分页，1024个PDE，1024个PTE，每个PTE对应一个物理页，一个页的大小是 `4kb` ）。
+ 10-10-12分页使得一个进程能访问的物理内存最大就是4GB。
+ 只要两个地址的PTE相同，那么它们一定指向同一个物理页（PTE相同PDE不可能不同（好像不一定吧？（不太确定）））
+ 在10-10-12分页中，如果想判断两个地址是否在同一个物理页中，很简单，直接看前20位（16进制前5位）。前10位是PDE偏移，10~20位是PTE偏移，后12位是页内偏移。所以如果16进制中前五位一样，则肯定在同一个物理页中。如 `12345000` 和 `12345888` 就在同一个物理页中。

![image-20201129121732497](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201129121732497.png)

+ 一个页的属性是一样的，如果0地址不能读不能写，那么 `0~fff` 地址都是不能读不能写的。
+ 缺页异常走E号中断
+ ![image-20201129124957213](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201129124957213.png)

+ 从CPU角度，只要P位为0，马上就走E号中断

+ 缺页无时无刻不在发生。走E号中断之后CPU会重新帮忙挂上物理页。 `VAD` 是一个二叉树。只有当发现VAD里面也找不到地址的情况下，才会弹出 `c0000005` 。

+ 内核情景分析

+ 内核原理与实现

+ ![image-20201129132136503](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201129132136503.png)

+ CR3其实是给CPU用的。

+ 按10-10-12拆分地址

  ```cpp
  #include <stdio.h>
  #include <stdlib.h>
  
  #include <iostream>
  
  using namespace std;
  
  int main()
  {
      int x;
      while (scanf("%x", &x) != EOF)
      {
          printf("0x%x\n", (x >> 22) * 4);
          printf("0x%x\n", ((x >> 12) & 0x3ff) * 4); 
          printf("0x%x\n", x & 0xfff);
      }
      return 0;
  }
  ```

+ 事实上并不存在这张图里面的PDT

  ![image-20201129135241570](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201129135241570.png)

  PDT本质上就是一个PTT。下面这张图才准确

  ![image-20201129135329696](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201129135329696.png)

+ 练习：修改0地址的PDE和PTE

  + 我的想法是先把PDE里面的值读进来，然后在偏移修改PTE（这个得到的是物理地址，也用不了）

+ ![image-20201129144759848](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201129144759848.png)

+ 第一个PTT和第二个PTT中间相差了一个页，也就是说PTT **在物理页上不是连续的** ，但是**在线性地址上是连续的。** 

  在线性地址上，0XC0000000是第一个PTT，0XC0000000 + 0X1000是第二个PTT。

  ![image-20201129145125465](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201129145125465.png)

+ ![image-20201129145742389](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201129145742389.png)







### 逆向MmIsAddressValid函数

+ ![image-20201129151656334](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201129151656334.png)

+ ![image-20201129152249468](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201129152249468.png)
+ https://blog.csdn.net/Kwansy/article/details/108945068





### 2-9-9-12分页

+ 因为页的大小是确定的（4kb），所以 `12` 是不能改的

+ `2-9-9-12` 分页中PTE的长度是8个字节，比 `10-10-12` 分页大了一倍。

+ 一个`PTT`页还是 `4 * 1024 = 4096` 个字节大小，而此时一个 `PTE` 的大小是 **8个字节** ，所以一个 `PTT` 页里面可以放 **512** 个 `PTE` 。则所需要的寻址比特数为9个比特。

+ 一个 `PDT` 页也是一样的道理， **9个比特** 就可以索引整个表中的数值。

+ ![image-20201129170058878](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201129170058878.png)

  `2-9-9-12` 中的 `2` 就是指这个 `PDPTE(page-directory-point-table)` （页目录指针表）选择哪一个。

+ 在 `10-10-12` 分页中 `cr3` 直接指向 `PDT` 表，但是 `2-9-9-12` 分页中 `CR3` 指向的是 `PDPTE` 表。

+ ![image-20201129172051731](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201129172051731.png)

  + 当 `PS = 1` 的时候（第8位（下标为7 ）），其 `base addr` 的大小是 `35 - 21 = 15` 位， `2^15 / 1024 / 8 = 2` ，因此如果这是一个大页的话是 `2MB` 大小。
  + 当 `PS = 0` 的时候，

+ ![image-20201129171211789](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201129171211789.png)

  + 通过 `2-9-9-12` 找一下物理地址

#### 2-9-9-12分页找基址实验

+ ![image-20201201202636152](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201201202636152.png)

  ```
  0x420024
  00
  00 0000 010
  0 0010 0000
  0000 0010 0100
  
  0x0 * 8 = 0x0
  0x2 * 8 = 0x10
  0x20 * 8 = 0x100
  		   0x24
  ```

  + 首先查看 `CR3` ，然后 `!dq CR3 + 0`

    ![image-20201201203925088](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201201203925088.png)

    得 ```PDPTE = 00000000`167e3001``` 。

    ![image-20201201200944191](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201201200944191.png)

    页目录表低12位是属性，则可得 ```PDT = 1b620000``` 

  + 接下来查看 `PDE` ， ```!dq 167e3000+10```

    ![image-20201201203913826](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201201203913826.png)

  + 接下来查看 `PTE` ，`!dq 167a5000+100`

    ![image-20201201202923224](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201201202923224.png)

  + 得到 `PTE` 的值是 `1b20b000` ，再加上页内偏移 ```!db 15e87000+24``` 找到字符串。

    ![image-20201201203835338](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201201203835338.png)

  + 用 `!vtop` 验证一下

    ![image-20201201204048206](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201201204048206.png)



### 逆向MmIsAddressValid函数

+ `0xC000000`是第一张页表的线性地址，`0xC0600000`是第一张页目录表的线性地址。





### TLB

+ ![image-20201202083643383](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201202083643383.png)
  + 体验TLB存在：给一个线性地址挂一个物理页B，放一个内容，然后再将其改为另外一个物理页C，读这个变量，发现其仍然读取物理页B里面的东西。



### 中断与异常

+ 线程的切换并不是使用 `IRQ0` 时钟中断来进行的，虽然它确实可以用来做线程切换。

  ![image-20201202093303464](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201202093303464.png)

  中断可以通过 `cli` 来将 `IF` 位清空达到屏蔽的效果，但是异常是不能被屏蔽的。

  

### 特殊功能寄存器

+ ![image-20201202101403538](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201202101403538.png)
+ 如何查看缺页异常处理函数的代码？先 `r cr2` 然后 `!vtop cr3 cr2` 然后 `u` 看不到，显示不是代码。
+ ![image-20201202102316449](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201202102316449.png)



### PWT/PCD

![image-20201202103742687](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201202103742687.png)



