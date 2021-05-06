+ hyperplatform 成熟的VT框架

+ ![image-20210503124028626](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master/image-20210503124028626.png)

  驱动开发包编译汇编文件

+ ![image-20210503125702031](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master/image-20210503125702031.png)

+ 32位下返回一个64位的返回值一般把 **高32位** 放在 `ebx` 里，**低32位**放在 `eax` 里

+ ![image-20210503184334666](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master/image-20210503184334666.png)

+ 驱动卸载之后泄露的内存并不会清除，会一直留在内存中。

+ 在 `30.4` 可以查错误代码。

  ![image-20210503181128472](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master/image-20210503181128472.png)

+ `dbgprint` 就能占用差不多2k的栈空间。

+ 裸函数

  1. 里面不要使用任何的局部变量。因为局部变量放的位置都是 `ebp-8` 这样的位置。而裸函数没有提升堆栈，这样的操作会导致前一个栈里面的东西被覆盖。
  2. 裸函数不要写得太长，如果想在裸函数里面实现什么功能建议再写一个新的函数来调用。

### EPT

+ 并不是说开启了 `EPTP` 之后CR3就不用了，还是要用。在虚拟机中通过 `CR3` 转换为物理地址，然后物理机中再通过 `EPTP` 转换为真实的物理地址。
+ 虚拟机中的地址是 `guest physical address` ， `GPA` ，转换为物理机中的地址 `HPA` 。 `host` 。
+ 并不是说在虚拟机中先通过页表找到GPA之后再回到物理机然后进行GPA到HPA的转换。而是说在每一级页表中的转换得到的物理地址都要走一遍EPTP得到实际的物理地址。这样每一层都要经过一次转换，最终才能得到真实的物理地址。每一次找地址的时候都要经过如下的循环。
+ ![image-20210503181128472](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master/image-20210504132553314.png)
+ 