![无法加载请爬梯子](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/20200706175612.png)

+ 将vs里面的唤醒代码提示快捷键设置成了 `ALT + /`

+ `Ctrl + alt + L` 打开VS的右侧侧边栏， `shift + Ese` 隐藏

+ VS中连按两下 `CTRL + M` 可以将代码块缩起来

  

+ `CTRL + SHIFT + [` 可以在vscode中折叠代码块

+ 打开内存监控窗口

  ![无法加载请爬梯子](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/20200721115806.png)

+ 若要打开“自动变量”窗口，请在调试时依次选择“调试” > “窗口” > “自动变量”，或按 Ctrl+Alt+V > A 调试 

  若要打开“局部变量”窗口，请在调试时选择“调试” > “窗口” > “局部变量”，或按 Alt+4 。

+ `LOBYTE` 截取4字节的低两位， `HIBYTE` 截取高两位

  ![](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/20200723002011.png)
  
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