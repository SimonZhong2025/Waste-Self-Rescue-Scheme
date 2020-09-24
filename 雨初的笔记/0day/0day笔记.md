+ `rep stosd` 将 `EAX` 中的 `DWORD` 重复 `ECX` 次放入 `EDI` 指向的地方。

+ 堆栈图是基本功。

+ 需要插入shellcode，先将地址改成自己代码的地址，如下

  ![image-20200924201421850](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200924201421850.png)

  运行时这个地方的代码是 `33DB` ，于是可以执行自己的代码弹出 `messagebox` 。