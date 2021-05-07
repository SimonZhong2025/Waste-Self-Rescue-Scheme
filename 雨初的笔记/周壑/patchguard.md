+ 绝大部分PG检测基于 `context` 结构体。

+ ![image-20210411205545730](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master/image-20210411205545730.png)

+ ![image-20210411204859958](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master/image-20210411204859958.png)

+ `ZwQuerySystemInformation` 函数可以得到所有的？？？

+ `www.geoffchappell.com` 这个网站可以搜到一些未文档化的函数的分析

+ `context` 是一块RWX的内存。pg平均两分钟调度一次 `context` 。这一块内存采用接力式的方法，在使用了一次之后就不要了，然后再申请一块，把自己复制到新的那块那里。

+ 定位 `context` 的方法是在驱动中将 `context` 的可执行位关闭，这样再执行的时候就会进入异常。

+ 在windbg里面使用 `!pool 地址` 可以看这个地址的页面属性。

+ ![image-20210502000646584](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20210502000646584.png)

  `ba` 下硬件断点。