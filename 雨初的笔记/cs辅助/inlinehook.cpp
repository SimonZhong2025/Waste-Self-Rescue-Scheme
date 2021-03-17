作业答案:
1VirtualAlloc创建空间后，传入目标DLL的名称，调用远程线程启动LoadLibrary
加载目标DLL
2通过远程线程或DLL入口点



#include "stdafx.h"
#include "INLINE_HOOK.h"
#include <process.h>
#define PATCH_INLINE 5

CHAR szNewSize[]={"INLINE_HOOK成功"};
PCHAR dwHookAddre=0;
PCHAR dwRetAddre=0;


/************************************
**	用户函数
**
************************************/
DWORD MyMessageBox()
{
	MessageBoxW(0,L"INLINE成功",L"提示",0);

	return 0;
}
/************************************
**	中转函数
**
************************************/
DWORD _declspec(naked) NewFunction()
{
	_asm
	{
		pushad
		pushfd
		//LEA EAX,DWORD PTR DS:[szNewSize]
		//MOV DWORD PTR SS:[esp+0x24+8],EAX
		call MyMessageBox
		popfd
		popad
		
		MOV EDI,EDI
		PUSH EBP
		MOV EBP,ESP
		JMP dwRetAddre
		
		Retn
	}
}

/************************************
**	INLINE_HOOK功能函数
**
************************************/
DWORD _stdcall MyINLINEHookA(PCHAR pDllName,PCHAR pFunName)
{
	//页面属性备份
	DWORD state=0;
	//HOOK函数的地址
	dwHookAddre=(PCHAR)GetProcAddress(GetModuleHandleA(pDllName),pFunName);
	//HOOK结束返回的地址
	dwRetAddre=dwHookAddre+PATCH_INLINE;
	//备份的代码
	static BYTE byOldJmpCode[PATCH_INLINE]={0};
	//跳转代码
	BYTE byJmpCode[PATCH_INLINE]={0xe9};
	*(DWORD*)&byJmpCode[1]=(DWORD)NewFunction-(DWORD)dwHookAddre-5;
	//byJmpCode[PATCH_INLINE-1]=0xfe;

	//备份代码
	memcpy(byOldJmpCode,dwHookAddre,PATCH_INLINE);
	
	//开始HOOK
	VirtualProtect(dwHookAddre,PATCH_INLINE,PAGE_READWRITE,&state);
	memcpy(dwHookAddre,byJmpCode,PATCH_INLINE);
	VirtualProtect(dwHookAddre,PATCH_INLINE,state,&state);
	
	return 0;
}

/************************************
**	DLL服务函数
**
************************************/

BOOL APIENTRY DllMain( HANDLE hModule, 
                       DWORD  ul_reason_for_call, 
                       LPVOID lpReserved
					 )
{
    switch (ul_reason_for_call)
	{
		case DLL_PROCESS_ATTACH:
			MyINLINEHookA("user32.dll","MessageBoxA");
			break;
		case DLL_THREAD_ATTACH:
		case DLL_THREAD_DETACH:
		case DLL_PROCESS_DETACH:
			break;
    }
    return TRUE;
}



































#include "stdafx.h"



////////////////////////////////////////
//////          相关定义         ///////
////////////////////////////////////////

DWORD MyShellCodeA();
/***************************************
**   ShallCode引导代码段相关定义
***************************************/
typedef HMODULE (_stdcall *MyLoadLibraryA)(LPCSTR);
typedef FARPROC (_stdcall *MyGetProcAddressA)(HMODULE,LPCSTR);

typedef struct _UNICODE_STRING 
{
   USHORT    Length;
   USHORT    MaximumLength;
   PWSTR     Buffer;
 } UNICODE_STRING ,*PUNICODE_STRING;
//模块加载信息
typedef struct _PEB_LDR_DATA
{
	ULONG Length;
	BOOLEAN Initialized;
	PVOID SsHandle;
	_LIST_ENTRY InLoadOrderModuleList;           //模块加载顺序
	_LIST_ENTRY InMemoryOrderModuleList;         //模块在内存中的顺序
	_LIST_ENTRY InInitializationOrderModuleList; //模块初始化装载顺序
	PVOID EntryInProgress;
}PEB_LDR_DATA, *PPEB_LDR_DATA;
//链表单节点结构
typedef struct _LDR_DATA_TABLE_ENTRY 
 {      
    LIST_ENTRY InLoadOrderLinks;
    LIST_ENTRY InMemoryOrderLinks;
    LIST_ENTRY InInitializationOrderLinks;
    PVOID DllBase; 
    PVOID EntryPoint; 
    ULONG SizeOfImage;
    UNICODE_STRING FullDllName; 
    UNICODE_STRING BaseDllName; 
    ULONG Flags;
    USHORT LoadCount;
    USHORT TlsIndex;
    union 
    {   
        LIST_ENTRY HashLinks;
        struct 
        {
            PVOID SectionPointer; 
            ULONG CheckSum;
        }; 
    };
    ULONG TimeDateStamp;   
} LDR_DATA_TABLE_ENTRY, *PLDR_DATA_TABLE_ENTRY;
/***************************************
**   ShallCode用户段相关定义
***************************************/
typedef DWORD (_stdcall *MyMessageBoxA)(HWND,LPCTSTR ,LPCTSTR ,UINT);



/***************************************
**	ShellCode代码
**
***************************************/

DWORD MyShellCodeA()
{	
	CHAR k32NameA[]={'k','e','r','n','e','l','3','2','.','d','l','l',0};
	CHAR k32NameW[]={'k',0,'e',0,'r',0,'n',0,'e',0,'l',0,'3',0,'2',0,'.',0,'d',0,'l',0,'l',0,0,0};

	CHAR LoadLibraryAName[]={'L','o','a','d','L','i','b','r','a','r','y','A',0};
	CHAR GetProcAddressName[]={'G','e','t','P','r','o','c','A','d','d','r','e','s','s',0};
	
	PEB_LDR_DATA* pPebLdrData=NULL;
	PCHAR k32DllBase=0;
	PCHAR ptr1=NULL;
	PCHAR ptr2=NULL;
	PWCHAR ptr3=NULL;
	PWCHAR ptr4=NULL;
	DWORD flage=0;
	PIMAGE_DOS_HEADER pDos=NULL;
	PIMAGE_NT_HEADERS32 pNT=NULL;
	PIMAGE_EXPORT_DIRECTORY pExport=NULL;
	PDWORD pAddressOfName=NULL;
	PDWORD pAddressOfFunction=NULL;
	PSHORT pAddressOfNameOrdinals=NULL;
	PCHAR pfunction=NULL;

	MyLoadLibraryA pMyLoadLibraryA=NULL;
	MyGetProcAddressA pMyGetProcAddressA=NULL;
	//找到k32.dll
	_asm
	{
		mov eax,fs:[0x30]
		mov ecx,[eax+0x0c]
		mov pPebLdrData,ecx
	}
	_LDR_DATA_TABLE_ENTRY* lpInLoadOrderLinks=(_LDR_DATA_TABLE_ENTRY*)pPebLdrData->InLoadOrderModuleList.Flink;
	DWORD firstLink=(DWORD)lpInLoadOrderLinks;
	do 
	{
		flage=0;
		ptr3=lpInLoadOrderLinks->BaseDllName.Buffer;
		ptr4=(PWCHAR)&k32NameW[0];
		while (*ptr3==*ptr4)
		{
			if(*ptr3==0&&*ptr4==0)
			{
				flage=1;
				break;
			}
			ptr3++;
			ptr4++;
		}
		if(flage==1)
		{
			k32DllBase=(PCHAR)lpInLoadOrderLinks->DllBase;
			break;
		}
		lpInLoadOrderLinks=(_LDR_DATA_TABLE_ENTRY*)lpInLoadOrderLinks->InLoadOrderLinks.Flink;
	} while((DWORD)lpInLoadOrderLinks->InLoadOrderLinks.Flink!=firstLink);
	//未找到kernel32.dll
	if(k32DllBase==0)
	{
		return 0;
	}
	
	//找到kernel32导出表
	pDos=(PIMAGE_DOS_HEADER)k32DllBase;
	pNT=(PIMAGE_NT_HEADERS32)((PCHAR)pDos+pDos->e_lfanew);
	pExport=(PIMAGE_EXPORT_DIRECTORY)(k32DllBase+(DWORD)pNT->OptionalHeader.DataDirectory[0].VirtualAddress);
	//根据函数名找到目标函数
	pAddressOfNameOrdinals=(PSHORT)(k32DllBase+(DWORD)pExport->AddressOfNameOrdinals);
	pAddressOfName=(PDWORD)(k32DllBase+(DWORD)pExport->AddressOfNames);
	pAddressOfFunction=(PDWORD)(k32DllBase+(DWORD)pExport->AddressOfFunctions);
	
	for(DWORD i=0;i<=pExport->NumberOfNames;i++)
	{
		//找到函数名LoadLibraryA
		flage=0;
		ptr1=(PCHAR)(k32DllBase+(DWORD)pAddressOfName[i]);
		ptr2=LoadLibraryAName;
		while (*ptr1==*ptr2)
		{
			if(*ptr1==0&&*ptr2==0)
			{
				flage=1;
				break;
			}
			ptr1++;
			ptr2++;
		}
		if(flage==1)
		{
			//找到到处序号-nBase
			pMyLoadLibraryA=(MyLoadLibraryA)(k32DllBase+(DWORD)pAddressOfFunction[pAddressOfNameOrdinals[i]]);
		}

		//找到函数名GetProcAddress
		flage=0;
		ptr1=(PCHAR)(k32DllBase+(DWORD)pAddressOfName[i]);
		ptr2=GetProcAddressName;
		while (*ptr1==*ptr2)
		{
			if(*ptr1==0&&*ptr2==0)
			{
				flage=1;
				break;
			}
			ptr1++;
			ptr2++;
		}
		if(flage==1)
		{
			//找到到处序号-nBase
			pMyGetProcAddressA=(MyGetProcAddressA)(k32DllBase+(DWORD)pAddressOfFunction[pAddressOfNameOrdinals[i]]);
		}
	}
	//用户函数区==========================
	CHAR User32NameA[]={'U','s','e','r','3','2','.','d','l','l',0};
	CHAR MessageBoxANameA[]={'M','e','s','s','a','g','e','B','o','x','A',0};
	CHAR Text[]={-41,-94,-56,-21,-77,-55,-71,-90,0};
	MyMessageBoxA pMyMessageBoxA=NULL;

	HMODULE hMod=pMyLoadLibraryA(User32NameA);
	pMyMessageBoxA=(MyMessageBoxA)pMyGetProcAddressA(hMod,MessageBoxANameA);
	
	pMyMessageBoxA(0,Text,0,0);

	//====================================





	
	return 0;
}

/***************************************
**	注入器
**
***************************************/
void InjectCode(DWORD PID)
{
	HANDLE hProcess= OpenProcess(PROCESS_ALL_ACCESS,NULL,PID);
	if(hProcess==0)
	{
		MessageBox(0,TEXT("打开失败"),0,0);
	}
	//创建代码空间
	LPVOID pcdVAdd=VirtualAllocEx(hProcess,NULL,0x1000,MEM_COMMIT,PAGE_EXECUTE_READWRITE);
	//注入代码部分
	WriteProcessMemory(hProcess,pcdVAdd,&MyShellCodeA,0x1000,NULL);
	//启动线程、
	CreateRemoteThread(hProcess,NULL,0,(unsigned long (_stdcall *)(void*))pcdVAdd,NULL,0,NULL);
}



/***************************************
**	主进程代码
**
***************************************/
int main(int argc, char* argv[])
{
	DWORD PID=0;
	printf("Hello World!\n");
	printf("输入进程ID!\n");
	scanf("%d",&PID);
	//注入ShallCode
	InjectCode(PID);
	while(1);
	return 0;
}







