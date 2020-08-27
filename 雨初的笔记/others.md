![无法加载请爬梯子](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/20200706175612.png)

+ 将vs里面的唤醒代码提示快捷键设置成了 `ALT + /`

+ `Ctrl + alt + L` 打开VS的右侧侧边栏， `shift + Ese` 隐藏

+ VS中连按两下 `CTRL + M` 可以将代码块缩起来

  

+ `CTRL + SHIFT + [` 可以在vscode中折叠代码块

+ 打开内存监控窗口

  ![无法加载请爬梯子](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/20200721115806.png)

+ 若要打开“自动变量”窗口，请在调试时依次选择“调试” > “窗口” > “自动变量”，或按 Ctrl+Alt+V > A 调试 

  若要打开“局部变量”窗口，请在调试时选择“调试” > “窗口” > “局部变量”，或按 Alt+4 。

+ `LOBYTE` 截取4字节的低两位， `HIBYTE` 截取高两位

  ![](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/20200723002011.png)
  
+ 知道自己哪不会你就已经会了 --海哥

+ 在 `cmd` 里面输 `python3` 会弹出ms store...要输入py才能进python3环境。

+ 可以通过添加这个函数来进行调试信息的输出

  ```cpp
  #include <stdarg.h>
  #include <ctype.h>
  void __cdecl OutputDebugStringF(const char *format, ...)  
  {  
      va_list vlArgs;  
      char    *strBuffer = (char*)GlobalAlloc(GPTR, 4096);  
  	
      va_start(vlArgs, format);  
      _vsnprintf(strBuffer, 4096 - 1, format, vlArgs);  
      va_end(vlArgs);  
      strcat(strBuffer, "\n");  
      OutputDebugStringA(strBuffer);  
      GlobalFree(strBuffer);  
      return;  
  }  
  ```

  ```cpp
  // Tools.h: interface for the Tools class.
  //
  //////////////////////////////////////////////////////////////////////
  #if !defined(AFX_TOOLS_H__16F2B0E1_C614_49AE_A5C4_1C58B76F50AC__INCLUDED_)
  #define AFX_TOOLS_H__16F2B0E1_C614_49AE_A5C4_1C58B76F50AC__INCLUDED_
  #if _MSC_VER > 1000
  #pragma once
  #endif // _MSC_VER > 1000
  void __cdecl OutputDebugStringF(const char *format, ...); 
  #ifdef _DEBUG  
  #define DbgPrintf   OutputDebugStringF  
  #else  
  #define DbgPrintf  
  #endif 
  #endif // !defined(AFX_TOOLS_H__16F2B0E1_C614_49AE_A5C4_1C58B76F50AC__INCLUDED_)
  ```

  

+ OD 

  + `F8` 单步

  + `CTRL + G` 查看某个位置的反汇编（如 `00401150` ）

  + `enter` 跳到函数定义， `-` 跳回来

  + 视图中的 `W` 是 `windows窗口` 。点开之后可以看到当前程序有多少个窗口

  + 视图中的 `C` 是 `CPU窗口` ，点开之后可以回到一打开就看到的那个窗口。

    ![](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/20200725195815.png) 

+ `ALT + 0` 和 `ALT + 2` 可以打开空间和输出视图。

+ 要让对话框中的按钮对齐可以调出这个工具栏然后点击相应的按钮，就可以达到左对齐上对齐下对齐的目的。

  ![image-20200725220538272](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200725220538272.png)

+ autohotkey停止脚本

  ![image-20200802235816841](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200802235816841.png)

+ `UltraEdit` 修改布局

  ![image-20200803111907063](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200803111907063.png)

+ 一个 `WCHAR` 大小是2个字节（一个 `WORD` ）![image-20200803123923855](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200803123923855.png)

+ 资源类型

  ![image-20200803185230591](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200803185230591.png)

  ![image-20200803185322604](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200803185322604.png)

![image-20200805110013917](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200805110013917.png)

+ vc6中 `#define` 后 `do` 可以自动补全 `do while(0)`

+ 要想知道某个缩写的全称是什么就google搜 **what does \*\* stand for** 吧，中文搜索是不指望了， `stackoverflow` 上面可能能找到答案。

  > 所以要好好学英语啊！！

  ![image-20200806220713807](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200806220713807.png)

+ `VC6` 好像不支持代码折叠。


