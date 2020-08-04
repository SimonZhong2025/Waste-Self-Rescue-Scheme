+ 获取文本框句柄

  ```cpp
  HWND hEditUser = GetDlgItem(hDlg,IDC_EDIT_USER);
  ```

+ 获取文本框内容

  ```cpp
  TCHAR szUserBuff[0x50];	// 缓冲区，用于存储字符串。
  GetWindowText(hEditUser,szUserBuff,0x50);	
  ```

  其中 `hEditUser` 是刚刚获得的文本框的句柄。

+ 在打开的子窗口里面要用 `EndDialog` 来结束当前的窗口。不能用 `PostQuitMessage` 。后者会连父窗口都一起关闭。

  ![image-20200804201855999](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200804201855999.png)

+ 如果需要 **获取或者设置** 某个文本框中的文字

  ```cpp
  HWND hEditUser = GetDlgItem(hwndDlg,IDC_EDIT_OEP);
  TCHAR szUserBuff[0x50];
  GetWindowText(hEditUser,szUserBuff,0x50);
  SetWindowText(hEditUser, TEXT("哈哈哈")); // 设置窗口文字
  ```

+ `WINDEF.H` 中有一个宏 `MAX_PATH` 定义了文件路径最大长度260

  ![image-20200804203749407](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200804203749407.png)

+ 在添加了 `.cpp` 文件之后一定要加上 `#include "StdAfx.h"` ，否则会出现 `.sbr` 文件找不到的问题。

  ![image-20200804204455968](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200804204455968.png)

+ [慎用USES_CONVERSION 使用和注意](https://blog.csdn.net/thanklife/article/details/70208841) 好像说要慎用 `USES_CONVERSION` ，因为它是在堆栈上分配空间的，不小心很容易栈溢出。最好还是自己写 `W2A A2W` 作用的函数。（这个宏在 `atlconv.h` 头文件里面）

  > `MultiByteToWideChar` 函数好像跟这功能有点关系