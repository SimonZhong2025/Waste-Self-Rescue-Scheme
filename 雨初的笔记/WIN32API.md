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

+ 画一个组框可以将各种东西框在里面，更加美观

  ![image-20200805104246014](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200805104246014.png)

+ 在使用列表控件的时候，因为这些控件都在一个 `dll` 里面，所以要先把这个 `dll` 导入进来

  ```cpp
  #include <commctrl.h>				
  #pragma comment(lib,"comctl32.lib")				
  ```

  且通用控件（列表控件属于通用控件的一种）在使用之前，需要通过 `INITCOMMONCONTROLSEX` 进行初始化，只要在您的程序中的任意地方引用了该函数就会使得WINDOWS的程序加载器PE  Loader加载该库

  可以将这几行代码加在 `WinMain` 的开头

  ```cpp
  INITCOMMONCONTROLSEX icex;				
  icex.dwSize = sizeof(INITCOMMONCONTROLSEX);				
  icex.dwICC = ICC_WIN95_CLASSES;				
  InitCommonControlsEx(&icex);				
  ```

+ 消息处理函数如果处理了一个消息的话要 `return TRUE` ，否则默认 `return FALSE` 的话系统会认为你没有对这个消息进行处理。比如在 `WM_INITDIALOG` 里面写了一大堆窗口总是弹不出来十分烦躁最后发现是漏了 `return TRUE` 本来就弹不出来。。。

+ 消息处理函数最后一定要记得将没有处理的消息 `return FALSE` 放回给系统处理。否则会出现窗口加载不正常的现象。

  ![image-20200805222840820](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200805222840820.png)

+ 如果要让点这里的时候下面自动展示相应的数据，回调函数中拦截的消息不是 `WM_COMMAND` ，而应该是 `WM_NOTIFY`  。（也叫通知消息）

  ![image-20200806214950748](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200806214950748.png)

+ 拦截到 `WM_NOTIFY` 消息的时候其中的 `lParam` 指向一个结构，这个结构根据具体消息的不同可能会有不同。

  ![image-20200806215159768](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200806215159768.png)

+ `WM_NOTIFY` 用法

  ![image-20200806220956941](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200806220956941.png)

+ `WINDOWS` 编程的本质是消息驱动的，任何东西都是消息

  ![image-20200806225549205](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200806225549205.png)

  如果需要获取用户在列表中选取了哪一行，可以通过 `SendMessage` ，最后一个参数写为 `LUNI_SELECTED` 得到选择了哪一行。

+ 需要获取某一个窗口的句柄的时候要使用 `GetDlgItem` 来获取。像这样 `GetDlgItem(hwndDlg, ID_ITEMNAME)); ` 。其中 `hwndDlg` 是程序的 `ImageBase` 。