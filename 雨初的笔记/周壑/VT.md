+ hyperplatform 成熟的VT框架

+ ![image-20210503124028626](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master/image-20210503124028626.png)

  驱动开发包编译汇编文件

+ ![image-20210503125702031](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master/image-20210503125702031.png)

+ 32位下返回一个64位的返回值一般把 **高32位** 放在 `ebx` 里，**低32位**放在 `eax` 里

+ ![image-20210503133254011](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master/image-20210503133254011.png)

+ 驱动卸载之后泄露的内存并不会清除，会一直留在内存中。

+ 在 `30.4` 可以查错误代码。

  ![image-20210503181128472](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master/image-20210503181128472.png)

+ 