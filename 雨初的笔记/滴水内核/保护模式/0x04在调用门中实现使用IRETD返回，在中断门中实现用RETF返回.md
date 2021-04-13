+ ![image-20201121192700640](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201121192700640.png)
+ ![image-20201126165632681](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201126165632681.png)





### 中断门使用 `RETF` 返回

+ 在中断门中用RETF返回，只需将[ESP+0x8]写到EFLAG，然后让ESP 和 SS向低地址移动4字节即可。主要代码如下

  ```cpp
  void __declspec(naked) interrupt_gate()
  {
  	__asm
  	{
  		// 这里往栈里面推了0x24个字节
  		pushad
  		pushfd
  	
  		add esp, 0x2c // 往下0x24 + 0x8的地方即为eflags
  
  		popfd // esp指向三环esp
  
  		// 将下面的三环esp和ss均往上移动一位
  		mov eax, [esp]
  		mov [esp - 0x4], eax
  		mov eax, [esp + 0x4]
  		mov [esp], eax
  		
          sub esp, 0x30 // 还原堆栈
              
  		popfd
  		popad
  
  		retf
  	}
  }
  ```

+ 编译一下然后 `F5` 找到中断门函数入口点为 `0x401040`

  ![image-20201126170545832](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201126170545832.png)

+ 构造一个中断门，下标为0x20，用 `int 0x20` 调用。这个中断门DPL为3，因为中断门中DPL要和CPL（应该是CPL吧）相等。

  ```cpp
  eq 8003f500 0040EE00`00081250
  ```

  





+ ![image-20201126170338074](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201126170338074.png)

```cpp
#include <windows.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// 调用门使用iret返回
void __declspec(naked) dym()
{
	__asm
	{
		iretd
	}
}

void __declspec(naked) interrupt_gate()
{
	__asm
	{
		// 这里往栈里面推了0x24个字节
		pushad
		pushfd
	
		add esp, 0x2c // 往下0x24 + 0x8的地方即为eflags

		popfd // esp指向三环esp

		// 将下面的三环esp和ss均往上移动一位
		mov eax, [esp]
		mov [esp - 0x4], eax
		mov eax, [esp + 0x4]
		mov [esp], eax
		
		sub esp, 0x30 // 还原堆栈

		popfd
		popad

		retf
	}
}



int main()
{
	char codebuff[6];
	*(PDWORD)&codebuff[0] = 0x12345678;
	*(PWORD)&codebuff[4] = 0x48; // 构造段选择子，index = 3，0环权限（提权）

	printf("0x%x\n", interrupt_gate);

	__asm
    {
		INT 0X20
        //pushfd //将标志位寄存器压入堆栈,作为调用门参数,而调用门参数刚刚好就从第3个位置分配,与中断门的EFLAGE寄存器位置相同
    }

	printf("finish");

	system("pause");

	return 0;
}
```



### 调用门使用 `IRETD` 返回

