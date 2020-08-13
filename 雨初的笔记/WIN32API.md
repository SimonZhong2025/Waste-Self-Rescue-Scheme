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

+ 需要获取某一个窗口的句柄的时候要使用 `GetDlgItem` 来获取。像这样 `GetDlgItem(hwndDlg, ID_ITEMNAME))`  。其中 `hwndDlg` 是程序的 `ImageBase` 。

+ 在获取用户选择第几行之后再得到这一行里面存储的PID（存储的特定的数据）

  ![image-20200806230327036](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200806230327036.png)
  
+ 这个宏 `MAKEINTRESOURCE` 也可以将一个数字转换为 `char *` 类型，便于传递参数。

  ![image-20200725202941156](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200725202941156.png)

  ![image-20200725203108905](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200725203108905.png)

+ 想要删除所有元素的时候句柄都得实时获取才行，原因不清楚。

  ![image-20200807163121870](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200807163121870.png)

  ![image-20200807163236455](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200807163236455.png)

  ![image-20200807163306486](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200807163306486.png)

  难道是我那三个函数里面的逻辑问题？不小心把这个指针指向 `NULL` 了？先放着懒得追究了（懒得理直气壮），记得每次 `GetDlgItem` 就没事了。

+ ![image-20200807195738904](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200807195738904.png)

+ 进程是静止的，就是指一个4GB的空间里面都放了什么。线程是指里面有几个同时执行的程序

+ WIN10的任务管理器里面跳到详细信息然后右键可以调出选择列选项

  ![image-20200807221027008](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200807221027008.png)

+ 加上 `::` 表示其不属于任何一个类，其是一个全局的函数。最好加上。可以避免和其他一些同名的函数冲突

  ![image-20200807222038945](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200807222038945.png)

+ `::CloseHandle` 之后只是说这个句柄我不用了，并不是说线程就挂了。事实上线程还在跑。句柄只是三环和零环的一个接口（？），关掉这个句柄并不会关掉这个线程。

  ![image-20200807222159616](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200807222159616.png)

+ 这里千万不能传一个 `&x` 地址进去。因为 `MyTest` 这个函数执行完了之后堆栈就销毁了，传到新线程中的那个指针已经指向垃圾数据了。所以在多线程中谨慎传指针，不然容易出错。（另外如果这里的 `x` 是一个 `static int` 的话也不会出现这种问题。）

  ![image-20200807223201071](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200807223201071.png)

+ `sprintf` 和 `sscnaf` 吹爆！！！

+ 做图形界面的时候一定要单独起线程。如果只有一个线程，那么干活的时候就没有人来管消息了。如果在干活的地方卡死了，那这个程序就卡死了，消息没有人可以处理了。

+ `::SuspendThread(hThread)` 挂起线程。 `::ResumeThread(hThread)` 恢复线程，而终止线程有三种方式

  ![image-20200808002327738](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200808002327738.png)

  + 如果是用 `::ExitThread` 方法退出，就是直接退出了， **只是把调用的堆栈空间释放了** 。在堆里面的东西不管。比如你在这个线程里面创建了一个对象，如果是 `ExitThread` 方法来退出的话程序并不会自动帮你调用析构函数，该在哪还是在哪。（内存泄露警告！）
  + 如果是用 `::TerminateThread` 方法结束线程， **异步** 退出线程， 并且 **不会清理堆栈** 。
  + 线程函数返回就是这个函数执行完了就结束这个线程。这是 **推荐的写法** 。这样你在函数的末尾可以从容地做完收尾工作。（问题：会自动调用析构函数吗，还是要手动调用？）

+ `windows` 不是一个实时的操作系统

+  `::ExitThread` 是  **同步调用** ，只有操作系统做完关闭线程这个动作程序才会向下一行代码执行。而 `::TerminateThread` 是 **异步调用** 。它只是发一个消息给操作系统告诉他要关闭这个线程，在执行这一行后面的代码的时候这个线程并不一定已经被关闭了。如果 **接下来的代码是必须线程结束了才能执行的代码** ，那么使用 `TerminateThread` 就有可能会出现问题。

  如果需要用 `::TerminateThread` 达到同样的效果，那么需要在需要 **阻塞** 的地方加上这样一行代码 `::WaitForSingleObject(hThread,INFINITE);` 。这样只有操作系统关闭了需要关闭的线程之后 `::WaitForSingleObject` 才会放行让程序继续执行下一行代码。 

+ **进程就是4GB，线程就是EIP** --老唐

+ ```cpp
  DWORD WINAPI 线程A(PVOID pvParam) 		
  {
     while(g_nIndex < MAX_TIMES) 		
     {
        EnterCriticalSection(&cs);		
        //对全局遍历X的操作		
        LeaveCriticalSection(&cs);		
     }
     return(0);	
  }
  DWORD WINAPI 线程B(PVOID pvParam) 		
  {		
     		
     while(g_nIndex < MAX_TIMES) 		
     {		
        EnterCriticalSection(&cs);		
        //对全局遍历X的操作		
        LeaveCriticalSection(&cs);		
     }
     return(0);		
  }
  ```

  如果代码这样写的话那么要等一个线程的 `while` 循环执行完了之后才会归还令牌，第二个线程才有可能执行。所以这样写代码是不科学的。

+ 为了 **避免死锁** 

  + 最好让每个线程中获取令牌的 **顺序** 设计成一样的。
  + 最好不要嵌套，拿一个还一个，不要让一个线程同时拿到多个令牌

+ 如果想要避免发生 **内核对象泄露** ，则要在线程执行完毕之后把它 `CloseHandle` 掉。那么可以使用这样的代码

  ```cpp
  ::WaitForMultipleObjects(2, hHandleArr, TRUE, -1);
  ::CloseHandle(hHandleArr[0]);
  ::CloseHandle(hHandleArr[1])
  ```

  

  