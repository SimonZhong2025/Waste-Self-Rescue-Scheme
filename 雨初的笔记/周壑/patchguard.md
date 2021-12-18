+ 绝大部分PG检测基于 `context` 结构体。

+ ![image-20210411205545730](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master/image-20210411205545730.png)

+ ![image-20210411204859958](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master/image-20210411204859958.png)

+ `ZwQuerySystemInformation` 函数可以得到所有的？？？

+ `www.geoffchappell.com` 这个网站可以搜到一些未文档化的函数的分析

+ `context` 是一块RWX的内存。pg平均两分钟调度一次 `context` 。这一块内存采用接力式的方法，在使用了一次之后就不要了，然后再申请一块，把自己复制到新的那块那里。

+ 定位 `context` 的方法是在驱动中将 `context` 的可执行位关闭，这样再执行的时候就会进入异常。

+ 在windbg里面使用 `!pool 地址` 可以看这个地址的页面属性。

+ ![image-20210502000646584](C:\Users\22112\AppData\Roaming\Typora\typora-user-images\old_images\image-20210502000646584.png)

  `ba` 下硬件断点。



# patchguard

+ bypass方法
  + 直接patch掉pg初始化的地方。好处是比较稳定，坏处是必须重启系统。而且patch掉之后checksum会改变，且数字签名会非法。而在系统启动加载ntoskrnl的时候会校验checksum和数字签名的合法性。需要对这些都进行绕过。
  + 通过VT做到读写分离，有一定的技术门槛
  + 定位所有context源。虽然context是加密的，但是调用的源头不是加密的。比如有十几个源头，那么我把所有的源头全部进行patch，就可以达到bypass PG的效果。这种方法比较鸡肋了，很难做到。
  + 基于加密算法分析，攻击context内容
    + 虽然context是经过加密的，但是其加密的算法并不复杂，主要还是通过异或进行加密。
    + 首先搜索内存，粗筛context
    + 然后基于加密算法的特性，进行context的定位。
    + 解密context，patch检测逻辑，加密写回context
  + 设置context页面不可执行，接管页面异常处理
    + 首先搜索内存，粗筛context
    + 全部virtualprotext设置为不可执行，接管执行异常（hook pagefault(0xe)，不过patch这个不会触发PG吗？）
    + 在异常处理中定位context，阻止检测逻辑
  + 