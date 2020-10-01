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

+ 在NT内核系统中fs寄存器指向TEB结构，**TEB+0x30处指向PEB结构**，**PEB+0x0c**处指向PEB_LDR_DATA结构，

  **PEB_LDR_DATA+0x1c**处存放一些动态链接库地址，**第一个指向ntdl.dll,第二个就是kernel32.dll的基地址了**

+ `lodsd` 和 `movsd` 相反，是从对应的地址中加载到 `eax,ax,al` 中

+ 提取shellcode应该可以先OD找到对应要dump的shellcode，然后用ultraedit来打开并复制shellcode。

+ ![image-20200926150841713](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200926150841713.png)

  `SEH` 链，最靠近栈顶的是 `19FFCC` 。进到 `19FFCC` 可以看到其第一个值是指向下一个 `SEH` 的指针，而第二个值既是这个异常处理函数所在的位置。

+ ```cpp
  int main(int argc, char** argv)
  {
      printf(argv[1]);
  }
  ```

  如果输入普通的字符，不会出现问题，但是如果传入的字符串中带有格式控制符时， `printf` 就会暴露栈中的数据。另 `%n` 控制符可以将当前输出的所有数据的长度写回到一个变量中去

+ 获取模块地址和函数地址

  ```cpp
  #include <stdio.h>
  #include <windows.h>
  
  #include <iostream>
  typedef void (*MYPROC)(LPTSTR);
  
  int main()
  {
      HINSTANCE LibAddr;
      MYPROC procAddr;
      LibAddr = LoadLibrary(TEXT("user32"));
      printf("动态库及地址 = 0x%x\n", (int)LibAddr);
      procAddr = (MYPROC)GetProcAddress(LibAddr, "MessageBoxA");
      printf("函数相对地址 = 0x%x\n", (int)procAddr);
      getchar();
      return 0;
  }
  ```

+ VS好像禁用了 `printf` 的 `%n` 形式。

+ `GetFullPathName` 可以获取某个文件的全路径。

+ 通过添加 `#pragma strict_gs_check(on)` 可以对任意类型的函数添加 `security cookie`  。

+ ![image-20200926200404069](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200926200404069.png)

  ​	![image-20200926200943226](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200926200943226.png)

+ `command prompt` 

  ![image-20200926204750505](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200926204750505.png)

+ safeSEH

  + 检查异常处理链是否位于当前程序的栈中，如果不在，终止异常处理函数的调用
  + 检查异常处理函数指针是否指向当前程序的栈中，如果指向当前栈中，终止对异常处理程序的调用。