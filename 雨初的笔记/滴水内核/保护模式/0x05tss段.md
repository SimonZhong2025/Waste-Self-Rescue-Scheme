参考 https://blog.csdn.net/Kwansy/article/details/108890586

+ ![image-20201128141100829](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201128141100829.png)
+ ![image-20201128141117844](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201128141117844.png)
+ ![image-20201127155603527](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201127155603527.png)
+ TSS是一块104个字节的内存， **其不在CPU里面，不是一个寄存器** 。
+ TSS存在的价值仅仅是允许我们一次性替换掉一堆寄存器
+ `bush flag`  如果是 `1` （B）说明这个段描述符已经被加载到 `tr` 寄存器里面。如果是 `0` （9）说明这个段描述符还没有被加载到 `tr` 寄存器里面。即如果加载到 `tr` 寄存器里面，则其会从 `9` 变成 `B` 。
+ `FS` 寄存器在三环是 `0x0000003b` ，在0环是 `0x00000030`

+ 最后一个结构 **Previous Task Link** 表示上一个进程的TSS段的段选择子

+ `0x68 == 104`

+ 可以通过 `dt nt!_KTSS` 来查看这个结构体

  ![image-20201127161322418](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201127161322418.png)



### 使用JMP FAR来使用TSS

+ ![image-20201128144750382](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201128144750382.png)

+ ```cpp
  printf("请在windbg执行: eq 8003f048 %02x00e9%02x`%04x0068\n", ((DWORD)TSS>>24) & 0x000000FF,((DWORD)TSS>>16) & 0x000000FF, (WORD)TSS);
  ```

  + 首先要构造段描述符，仍然是在 `0x0048` 这个闲置的段描述符地方放入我们构造的段描述符。其 `limit = 0x0068 = 104` ，为TSS的大小，其 `BASE` 为我们放置构造的 `TSS` 的局部变量的地址，另注意这里 `G` 位要设置为0（**这里base的单位为字节，所以 `G` = 0**）因为这个段描述符还没有被放入到 `TR` 中去过，所以 `bush flag` 置为0，`DPL` 设置为3，为 `00e9` 

  + 构造的TSS如下

    ```cpp
    	TSS[0] = 0x00000000; // Previous Task Link CPU填充，表示上一个任务的选择子
    	TSS[1] = 0x00000000; // ESP0
    	TSS[2] = 0x00000000; // SS0
    	TSS[3] = 0x00000000; // ESP1
    	TSS[4] = 0x00000000; // SS1
    	TSS[5] = 0x00000000; // ESP2
    	TSS[6] = 0x00000000; // SS2
    	TSS[7] = dwCr3; // CR3 学到页就知道是啥了
    	TSS[8] = (DWORD)R3Func; // EIP
    	TSS[9] = 0x00000000; // EFLAGS
    	TSS[10] = 0x00000000; // EAX
    	TSS[11] = 0x00000000; // ECX
    	TSS[12] = 0x00000000; // EDX
    	TSS[13] = 0x00000000; // EBX
    	TSS[14] = (DWORD)esp+0x900; // ESP，解释：esp是一个0x1000的字节数组，作为裸函数的栈，这里传进去的应该是高地址，压栈才不会越界
    	TSS[15] = 0x00000000; // EBP
    	TSS[16] = 0x00000000; // ESI
    	TSS[17] = 0x00000000; // EDI
    	TSS[18] = 0x00000023; // ES
    	TSS[19] = 0x00000008; // CS 0x0000001B
    	TSS[20] = 0x00000010; // SS 0x00000023
    	TSS[21] = 0x00000023; // DS
    	TSS[22] = 0x00000030; // FS 0x0000003B
    	TSS[23] = 0x00000000; // GS
    	TSS[24] = 0x00000000; // LDT Segment Selector
    	TSS[25] = 0x20ac0000; // I/O Map Base Address
    ```

    + 这里的 `CR3` 寄存器要断下来之后在 `windbg` 里面通过 `!process 0 0` 来获取。

+ 代码如下

  ```cpp
  #include "stdafx.h"
  #include <Windows.h>
  #include <stdio.h>
  
  DWORD dwOk;
  DWORD dwESP;
  DWORD dwCS;
  
  BYTE PrevTr[6]; // 旧TR，供裸函数返回
  
  // 任务切换后的EIP
  void __declspec(naked) R3Func()
  {
  	__asm
  	{
  		pushad
  		pushfd
  
  		push fs
  		int 3 // int 3 会修改FS
  		pop fs
  
  		mov eax,1
  		mov dword ptr ds:[dwOk],eax
  		mov eax,esp
  		mov dword ptr ds:[dwESP],eax
  		mov ax,cs
  		mov word ptr ds:[dwCS],ax
  
  		popfd
  		popad
  		
  		jmp fword ptr ds:[PrevTr] // 重新通过保存的旧的TR跳回来
  	}
  }
  
  int main()
  {	
  	DWORD dwCr3; // windbg获取
  	char esp[0x1000]; // 任务切换后的栈，数组名就是ESP
  	
  	// 此数组的地址就是TSS描述符中的Base
  	DWORD *TSS = (DWORD*)VirtualAlloc(NULL, 0x68, MEM_COMMIT, PAGE_READWRITE);
  	if (TSS == NULL)
  	{
  		printf("VirtualAlloc 失败，%d\n", GetLastError());
  		getchar();
  		return -1;
  	}
  	printf("请在windbg执行: eq 8003f048 %02x00e9%02x`%04x0068\n", ((DWORD)TSS>>24) & 0x000000FF,((DWORD)TSS>>16) & 0x000000FF, (WORD)TSS);
  	printf("请在windbg中执行!process 0 0，复制TSS.exe进程DirBase的值，并输入.\nCR3: "); // 在windbg中执行 !process 0 0 获取，DirBase: 13600420  这个数要启动程序后现查
  	scanf("%x", &dwCr3); // 注意是%x
  	
  	TSS[0] = 0x00000000; // Previous Task Link CPU填充，表示上一个任务的选择子
  	TSS[1] = 0x00000000; // ESP0
  	TSS[2] = 0x00000000; // SS0
  	TSS[3] = 0x00000000; // ESP1
  	TSS[4] = 0x00000000; // SS1
  	TSS[5] = 0x00000000; // ESP2
  	TSS[6] = 0x00000000; // SS2
  	TSS[7] = dwCr3; // CR3 学到页就知道是啥了
  	TSS[8] = (DWORD)R3Func; // EIP
  	TSS[9] = 0x00000000; // EFLAGS
  	TSS[10] = 0x00000000; // EAX
  	TSS[11] = 0x00000000; // ECX
  	TSS[12] = 0x00000000; // EDX
  	TSS[13] = 0x00000000; // EBX
  	TSS[14] = (DWORD)esp+0x900; // ESP，解释：esp是一个0x1000的字节数组，作为裸函数的栈，这里传进去的应该是高地址，压栈才不会越界
  	TSS[15] = 0x00000000; // EBP
  	TSS[16] = 0x00000000; // ESI
  	TSS[17] = 0x00000000; // EDI
  	TSS[18] = 0x00000023; // ES
  	TSS[19] = 0x00000008; // CS 0x0000001B
  	TSS[20] = 0x00000010; // SS 0x00000023
  	TSS[21] = 0x00000023; // DS
  	TSS[22] = 0x00000030; // FS 0x0000003B
  	TSS[23] = 0x00000000; // GS
  	TSS[24] = 0x00000000; // LDT Segment Selector
  	TSS[25] = 0x20ac0000; // I/O Map Base Address
  
  	char buff[6] = {0,0,0,0,0x48,0};	
  	__asm
  	{
  		str ax // 将TR放到ax里面
  		lea edi,[PrevTr+4]
  		mov [edi],ax // 保存旧的TR
  		
  		jmp fword ptr[buff]
  	}
  	printf("ok: %d\nESP: %x\nCS: %x\n", dwOk, dwESP, dwCS);
  	
  	return 0;
  }
  
  
  ```

+ `int 3` 会修改 `fs` ，要事先将 `fs` 存下来
+ ![image-20201128150423705](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201128150423705.png)



### 使用CALL FAR来使用TSS

+ `CALL FAR` 的时候堆栈里面放的东西和中断门的时候放的一样，所以用 `iretd` 返回（在别人博客的代码里面看到是这样的，需要做个实验验证一下）

+ 在实验里面没有在堆栈中看到类似中断门的结构。。。。。。。那就留个坑算了。。

  ```cpp
  // TSS.cpp : Defines the entry point for the console application.
  //
  
  #include "stdafx.h"
  #include <Windows.h>
  #include <stdio.h>
  
  DWORD dwOk;
  DWORD dwESP;
  DWORD dwCS;
  
  
  // 任务切换后的EIP
  void __declspec(naked) R0Func()
  {
  	__asm
  	{
  		pushad
  		pushfd
  
  		push fs
  		int 3 // int 3 会修改FS
  		pop fs
  
  		mov eax,1
  		mov dword ptr ds:[dwOk],eax
  		mov eax,esp
  		mov dword ptr ds:[dwESP],eax
  		mov ax,cs
  		mov word ptr ds:[dwCS],ax
  
  		popfd
  		popad
  		iretd
  	}
  }
  
  int _tmain(int argc, _TCHAR* argv[])
  {	
  	DWORD dwCr3; // windbg获取
  	char esp[0x1000]; // 任务切换后的栈，数组名就是ESP
  	
  	// 此数组的地址就是TSS描述符中的Base
  	DWORD *TSS = (DWORD*)VirtualAlloc(NULL,104,MEM_COMMIT,PAGE_READWRITE);
  	if (TSS == NULL)
  	{
  		printf("VirtualAlloc 失败，%d\n", GetLastError());
  		getchar();
  		return -1;
  	}
  	printf("请在windbg执行: eq 8003f048 %02x00e9%02x`%04x0068\n", ((DWORD)TSS>>24) & 0x000000FF,((DWORD)TSS>>16) & 0x000000FF, (WORD)TSS);
  	printf("请在windbg中执行!process 0 0，复制TSS.exe进程DirBase的值，并输入.\nCR3: "); // 在windbg中执行 !process 0 0 获取，DirBase: 13600420  这个数要启动程序后现查
  	scanf("%x", &dwCr3); // 注意是%x
  	
  	TSS[0] = 0x00000000; // Previous Task Link CPU填充，表示上一个任务的选择子
  	TSS[1] = 0x00000000; // ESP0
  	TSS[2] = 0x00000000; // SS0
  	TSS[3] = 0x00000000; // ESP1
  	TSS[4] = 0x00000000; // SS1
  	TSS[5] = 0x00000000; // ESP2
  	TSS[6] = 0x00000000; // SS2
  	TSS[7] = dwCr3; // CR3 学到页就知道是啥了
  	TSS[8] = (DWORD)R0Func; // EIP
  	TSS[9] = 0x00000000; // EFLAGS
  	TSS[10] = 0x00000000; // EAX
  	TSS[11] = 0x00000000; // ECX
  	TSS[12] = 0x00000000; // EDX
  	TSS[13] = 0x00000000; // EBX
  	TSS[14] = (DWORD)esp+0x900; // ESP，解释：esp是一个0x1000的字节数组，作为裸函数的栈，这里传进去的应该是高地址，压栈才不会越界
  	TSS[15] = 0x00000000; // EBP
  	TSS[16] = 0x00000000; // ESI
  	TSS[17] = 0x00000000; // EDI
  	TSS[18] = 0x00000023; // ES
  	TSS[19] = 0x00000008; // CS 0x0000001B
  	TSS[20] = 0x00000010; // SS 0x00000023
  	TSS[21] = 0x00000023; // DS
  	TSS[22] = 0x00000030; // FS 0x0000003B
  	TSS[23] = 0x00000000; // GS
  	TSS[24] = 0x00000000; // LDT Segment Selector
  	TSS[25] = 0x20ac0000; // I/O Map Base Address
  
  	char buff[6] = {0,0,0,0,0x48,0};	
  	__asm
  	{
  		call fword ptr[buff]
  	}
  	printf("ok: %d\nESP: %x\nCS: %x\n", dwOk, dwESP, dwCS);
  
  	return 0;
  }
  
  
  ```

  















