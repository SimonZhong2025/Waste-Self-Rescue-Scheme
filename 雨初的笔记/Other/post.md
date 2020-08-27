# 手动在程序中添加shellcode


## 思路
+ 首先理清思路，添加shellcode的原理是什么。添加shellcode就是在 **节里面没有用到的空白区域** 添加入自己的shellcode，然后将程序入口点 **OEP** 修改到添加的shellcode的起始位置，在执行完shellcode之后再 `JMP` 跳回原来程序的入口点。

+ 在这里我们的目标是添加一个弹出MessageBox的shellcode，其代码为 `MessageBox(0, 0, 0, 0)` ，执行效果为

  ![无法加载请爬梯子](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/20200706112744.png)

## 准备工作

+ 首先我们要进行一些准备工作。在每一台机器上 `MessageBox` 这个函数的地址都是不同的，我们要先找到这个函数的地址。在VC6.0中写如下代码

  ```cpp
  #include <windows.h>
  #include <stdio.h>
  
  int main()
  {
      MessageBox(0, 0, 0, 0);
      return 0;
  }
  ```

  然后在MessageBox处打上断点，进入反汇编，F11跟入，可找到 `MessageBox` 所在的地址为 **77D507EA** 。

  ![无法加载请爬梯子](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/20200706113033.png)

  或者也可以用代码找到MessageBox的地址，代码如下

  ```cpp
  #include <stdio.h>
  #include <iostream>
  #include <windows.h>
  typedef void (*MYPROC)(LPTSTR);
  
  int main()
  {
      HINSTANCE LibAddr;
      MYPROC procAddr;
      LibAddr = LoadLibrary("user32");
      printf("动态库及地址 = 0x%x\n", (int)LibAddr);
      procAddr = (MYPROC)GetProcAddress(LibAddr, "MessageBoxA");
      printf("函数相对地址 = 0x%x\n", (int)procAddr);
      getchar();
      return 0;
  }
  ```

  同样可以得到其相对地址。

  ![无法加载请爬梯子](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/20200706113408.png)

## 开始添加shellcode

+ 得到 `MessageBox` 地址之后开始准备添加shellcode。先用PETOOL查出其ImageBase、文件对齐和文件入口点OEP，如下，则其入口点为 `86E0` , `ImageBase` 为 `40000` ，文件对齐为 `1000`

![无法加载请爬梯子](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/20200706115752.png)

+ 然后在节表信息中找到某个节是否有多余的空间

  ![无法加载请爬梯子](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200706114021998.png)

  这里可以得到307E0-31000这一段区域应该是没有被使用的，于是打开 **WinHex** ，按 `Alt + G`  跳转到31000位置

  ![无法加载请爬梯子](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/20200706114235.png)

  发现一大片空白区。随意选择一处添加入我们的shellcode

+ 我们添加的shellcode首先要 `push 0` 执行4次，将 `MessageBox` 的4个参数压入栈中。其对应硬编码为 `6a 00 6a 00 6a 00 6a 00`  。然后要 `CALL` 调用 `MessageBox` 函数，调用完之后再 `JMP` 跳转到原来函数的入口点OEP使程序能正常运行。这里 `CALL` 的硬编码是 `E8` ，`JMP` 的硬编码是 `E9` ，因此先填入 `E8 00 00 00 00 E9 00 00 00 00` 。

+ 接下来开始算 `CALL` 和 `JMP` 后面跟着的参数。其计算方法为

  ![无法加载请爬梯子](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/20200706114802.png)

  则通过 `(ImageBase + CALL指令后一条指令的地址) + X = 77D507EA` 算出应该填在E8后面的参数。其中 `77D507EA` 是我们之前得到的MessageBox的地址。

  ![无法加载请爬梯子](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/20200706115053.png)

  算出得E8后面应跟 `7791F8FD` ，将其填到E8后面。这里注意要将计算器设置为DWORD（双字）

  而根据公式，E9后面跟的参数为 `X = 程序入口点OEP - E9这条指令后一条指令的地址` 。之前已经查得程序入口点OEP为 `86E0`

  ![无法加载请爬梯子](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/20200706115727.png)

  而E9后一条指令的地址为 `30EF2` ，则用计算器算得

  ![无法加载请爬梯子](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/20200706115944.png)

  E9后面应填 `FFFFD 77EE` 

  将其填入， shellcode编写完成

  ![无法加载请爬梯子](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/20200706120045.png)

## 将程序入口点OEP改到添加的shellcode上

接下来是最后一步，将程序原来的入口点改到添加的shellcode （ `30EE0` ）上面，如下

![无法加载请爬梯子](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/20200706120324.png)

修改完成后添加shellcode的工作结束了，接下来保存到原文件，双击便可执行我们添加的shellcode-弹出 `MessageBox`

![无法加载请爬梯子](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/20200706120452.png)



