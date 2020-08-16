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
  ::CloseHandle(hHandleArr[1]);
  ```

+ **互斥体** 与 **临界区** 的区别：

  1. 临界区只能用于单个进程间的线程控制。

  2. 互斥体可以设定等待超时，但临界区不能。

  3. 线程意外终结时，Mutex可以避免无限等待。

  4. Mutex效率没有临界区高。

+ **互斥体** 本质上是一个 **内核对象** 。所有的 **进程** 都可以看到。而 **临界区** 只能在 **本进程** 内使用。

+ 写三环程序的时候 `CreateMutex` 的第一个参数一般设置为 `NULL` 。

+ `CreateMutex` 的第二个参数指示这个线程是否保有这个互斥体的所有权。如果是 `FALSE` 的话意思应该就是创建的时候不加锁（吧（？））

+ `CreateMutex` 第二个参数如果是 `FALSE` 的话在其他地方 `WaitForSingleObject` 可以直接得到这个对象。如果是 `TRUE` 的话必须等到当前线程 `ReleaseMutex` 释放这个互斥体之后才能 `Wait` 到这个对象。 

+ `CloseHandle` 之后只是这个 **句柄** 被销毁了。如果在其他地方有对这个内核对象的引用，那么这个 **内核对象** 并不会被销毁。只有操作系统发现没有任何一个地方有指向这个内核对象的句柄了的时候操作系统才会自动销毁这个内核对象。比如说如果这个进程用 `CreateMutex` 创建了一个互斥体，但是另外一个进程也使用了这个互斥体，那么就算原来这个进程结束了，这个互斥体也不会被销毁。因为另外一个进程还需要使用这个互斥体。

+ 反复强调，不要在界面程序里面写业务。如果想做些什么事情的话要单独起一个线程最好。界面不会卡死。

+ 用 **全局变量** 来控制线程执行的方法是坏方法。因为在切换到这个线程发现 `flag` 不满足条件的时候操作系统并不会马上切换到另一个线程，而是会将 **20毫秒** 耗尽之后再切换到另一个线程。这样效率极低。

+ **线程同步** 就是一个线程可以控制下一个线程什么时候开始。

+ 对于一个事件（是一个内核对象），需要先 `CreateEvent` 生成这个事件，然后在其他的进程里面就可以通过 `OpenEvent` 获取这个事件的句柄（前提是这个事件不是匿名的）。

  内核对象在高2G的空间中。所有的进程都可以访问到非匿名的内核对象。

  ![image-20200814224233841](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200814224233841.png)

+ `CreateEvent` 的第二个参数 `bManualReset` 的意义是：

  + 如果设置为 `FALSE` ，那么只要有线程 `Wait` 到这个事件，就会立刻将其状态改变为阻塞。
  + 如果设置为 `TRUE` ，那么就算有线程 `Wait` 到这个事件，也不会改变其状态。而需要手动（ *Manual* ）通过 `SetEvent（设置为已通知状态）` 和 `ResetEvent（设置为未通知状态）（这个函数极少用到）` 来改变其状态。但是这种用法比较少见，因为容易产生线程安全问题。
  + 通常会把这个参数设置为 `FALSE` 。

+ `CreateEvent` 第三个参数 `bInitialState` 的意义是创建这个事件的时候将其设置为 **已通知状态（TRUE）** 还是 **未通知状态（FALSE）** 。如果是 **已通知状态** 的话说明其他线程可以直接 `Wait` 到这个对象。反之则需要等这个线程将这个事件设置为已通知状态之后才能 `Wait` 到这个对象。

+ 好像阻塞（正在 `Wait` 这个对象）的时候称这个内核对象为未通知状态，而已经 `Wait` 到这个对象之后称这个内核对象为已通知状态。

+ 如果一个线程要归还控制权，将一个事件设置为 **已通知状态** ，需要使用 `SetEvent` 函数达到目的。

+ 惨案。。![image-20200815002118623](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200815002118623.png)![image-20200814234047255](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20200814234047255.png)

  改这一个地方花了我20分钟。

+ 事件不仅可以用来做线程的 **互斥** ，还可以用来做线程的 **同步** 。而 **临界区和互斥体** 只能用来做线程的 **互斥** 。

+ 如果之后不需要用到这个线程的 **句柄** 了，那么大可将其 `CloseHandle` 掉。因为就算将其句柄删除，这个线程仍然会跑完。只是我们无法通过句柄来访问它了而已。

  ## 进程创建 / 加密壳基础

+ **程序** 只是一个存储在硬盘中的文件，不过这个文件遵守PE结构。 **镜像** 是 **程序** 拉伸后的结果。但是没有 `EIP` ，不能跑。而线程是可以运行的，有 `EIP` 。

+ 三环中能控制内核对象的 **句柄** 只是 **句柄表** 中的一个编号。句柄表中才真正存储了这个内核对象在 **高2G** 中的位置。需要访问这个内核对象的时候要用这个编号在句柄表中找到相应的位置，才能得到该内核对象真正的地址。

+ 每个 **进程** 都会有一个句柄表

+ `CreateProcess` 各参数

  ```cpp
  BOOL CreateProcess(
    LPCTSTR lpApplicationName,                 // name of executable module
    LPTSTR lpCommandLine,                      // command line string
    LPSECURITY_ATTRIBUTES lpProcessAttributes, // SD
    LPSECURITY_ATTRIBUTES lpThreadAttributes,  // SD
    BOOL bInheritHandles,                      // handle inheritance option
    DWORD dwCreationFlags,                     // creation flags
    LPVOID lpEnvironment,                      // new environment block
    LPCTSTR lpCurrentDirectory,                // current directory name
    LPSTARTUPINFO lpStartupInfo,               // startup information
    LPPROCESS_INFORMATION lpProcessInformation // process information);
  ```

  + 第一个参数 `lpApplicationName` 是一个 **常量字符串** ，指向需要运行的进程这个 `EXE` 所存放的地址。

  + 第二个参数 `lpCommandLine` 是一个 **字符串** ，（ **因为过程中可能要修改这个字符串的值所以不要传常量字符串进去** ），表示这个程序运行时候的命令行参数。

  + 第三个参数 `lpProcessAttributes` 传的是一个 `SECURITY_ATTRIBUTES` 结构体。如果其中 `bInheritHandle` 设置为 `TRUE` ，则表示 **创建出目标进程** 之后在 **原进程** 的句柄表中 **创建出来的进程的进程句柄是可以被继承的** 。

  + 第四个参数 `lpThreadAttributes` 和第三个参数类似，表示创建出来的进程的 **线程句柄** 是可以被继承的。

  + 第五个参数 `bInheritHandles` 表示创建这个子进程的时候 **允不允许这个子进程继承父进程的句柄** 。如果是 `TRUE` 则可以继承父进程的句柄。如果是 `FALSE` 则不能。

  + 倒数第二个参数 `lpStartupInfo` 表示我们 **需要这个进程以什么方式打开** 。应用程序有 **默认的打开方式** ，所以不用去改什么东西。这个结构体的结构如下

    ```cpp
    typedef struct _STARTUPINFO { 
        DWORD   cb; 
        LPTSTR  lpReserved; 
        LPTSTR  lpDesktop; 
        LPTSTR  lpTitle; 
        DWORD   dwX; 
        DWORD   dwY; 
        DWORD   dwXSize; 
        DWORD   dwYSize; 
        DWORD   dwXCountChars; 
        DWORD   dwYCountChars; 
        DWORD   dwFillAttribute; 
        DWORD   dwFlags; 
        WORD    wShowWindow; 
        WORD    cbReserved2; 
        LPBYTE  lpReserved2; 
        HANDLE  hStdInput; 
        HANDLE  hStdOutput; 
        HANDLE  hStdError; 
    } STARTUPINFO, *LPSTARTUPINFO; 
    ```

    我们只需要把 `DWORD cb` 的值赋为这个结构体的 **大小** ，然后把所有其他的成员设置为 **0** 即可。如下:

    ```cpp
    STARTUPINFO si = {0};   
    si.cb = sizeof(si);
    ```

    然后在调用函数的时候把 `&si` 作为倒数第二个参数传进去即可。

    > 之所以要设定这个结构的大小是因为这个结构的大小有可能会改变（可能会拓展）

  + 倒数第一个参数 `lpProcessInformation` 是一个 `OUT` 类型的参数。是用来返回值的参数。

    > `dwProcessId ` 是 **进程ID**
    >
    > `dwThreadId ` 是 **线程ID**
    >
    > `hProcess` 是 **进程句柄**
    >
    > `hThread` 是 **线程句柄**

+ `CreateEvent` 第一个参数（安全属性）如果填 `NULL` ，则默认不可以继承。

  > 继承的时候只复制 **句柄表** ，跟 **零环** 没有任何关系。

  `SECURITY_ATTRIBUTES` 共有三个成员，如果需要这个事件能被继承，所传的值如下：

  ```cpp
  sa.nLength = sizeof(sa); // 这个结构的大小	
  sa.lpSecurityDescriptor = NULL; // 安全描述符，仍然填NULL
  sa.bInheritHandle = TRUE; // 能否被继承。关键在此，要设置为TRUE（可以被继承）
  ```

  继承了之后直接通过命令行参数（ `argv[x]` ）将子进程需要用到的句柄传进子进程里面，然后在子进程里面直接把这个参数转为数字并通过 `(HANDLE)` 转换为一个句柄即可使用。因为子进程的句柄表继承了父进程的句柄。（ **如果这个句柄被设置为不能继承，则不能用这种方法得到。因为这种情况下子进程的句柄表中没有这个句柄，无法获取正确的句柄。** ）

+ 如果子进程继承了父进程的句柄，然后父进程中使用 `CloseHandle` 关闭了这个句柄，这个内核对象并不会消失。因为还有进程在使用这个内核对象。只是使用这个内核对象的进程数减一。只有 **使用这个内核对象的进程数为0** 时操作系统才会销毁这个内核对象。

+ 终止进程的三种方式：
  1. `VOID　ExitProcess(UINT  fuExitCode)` **===>进程自己调用**
  2. `TerminateProcess(HANDLE hProcess, UINT fuExitCode)` **===>终止其他进程**
  3. ·`ExitThread` **===>终止进程中的所有线程，进程也会终止**