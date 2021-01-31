+ `!vtop CR3的值 线性地址` 可以得到其物理地址。

+ `!dt` 的时候如果不给出地址如 `dt _DRIVER_OBJECT` 的话其会将这个结构体的结构列出来。如果给出其地址的话 `dt _DRIVER_OBJECT 86624360` ，其不仅会列出结构，还会列出起其对应的值

+ 如果想要看某个进程低2G的地址，要先 `.process 进程ID` 。

  ![image-20210128173531521](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210128173531521.png)

+ 