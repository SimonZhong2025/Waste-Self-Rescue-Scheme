+ `rep stosd` 将 `EAX` 中的 `DWORD` 重复 `ECX` 次放入 `EDI` 指向的地方。

+ 堆栈图是基本功。

+ 需要插入shellcode，先将地址改成自己代码的地址，如下

  ![image-20200924201421850](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200924201421850.png)

  运行时这个地方的代码是 `33DB` ，于是可以执行自己的代码弹出 `messagebox` 。

+ ![image-20200924211014620](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200924211014620.png)

+ 一般 **fs:[0x30]** 即为**PEB**的起始地址。

+ 想要调试shellcode，通常可以使用这样的代码

  ![image-20200924212033560](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200924212033560.png)

  简单hash

  ```cpp
  #include <stdio.h>
  #include <windows.h>
  
  #include <iostream>
  using namespace std;
  
  DWORD GetHash(char *fun_name)
  {
      DWORD digest = 0;
      while (*fun_name)
      {
          digest = ((digest << 25) | (digest >> 7));
          digest += *fun_name;
          fun_name++;
      }
      return digest;
  }
  
  int main()
  {
      DWORD hash = GetHash("abcacc345dws");
      printf("%x", hash);
  }
  ```

  