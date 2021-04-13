![image-20201206142643766](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201206142643766.png)





```cpp
#include <ntddk.h>
#include <ntdef.h>

#define DEVICE_NAME L"\\Device\\HbgDev"
#define SYMBOLICLINK_NAME L"\\??\\HbgDevLnk"

#define OPER1 CTL_CODE(FILE_DEVICE_UNKNOWN,0x800,METHOD_BUFFERED,FILE_ANY_ACCESS)
#define OPER2 CTL_CODE(FILE_DEVICE_UNKNOWN,0x900,METHOD_BUFFERED,FILE_ANY_ACCESS)

typedef struct _LDR_DATA_TABLE_ENTRY
{
	LIST_ENTRY InLoadOrderLinks;
	LIST_ENTRY InMemoryOrderLinks;
	LIST_ENTRY InInitializationOrderLinks;
	PVOID DllBase;
	PVOID EntryPoint;
	UINT32 SizeOfImage;
	UNICODE_STRING FullDllName;
	UNICODE_STRING BaseDllName;
	UINT32 Flags;
	UINT16 LoadCount;
	UINT16 TlsIndex;
	LIST_ENTRY HashLinks;
	PVOID SectionPointer;
	UINT32 CheckSum;
	UINT32 TimeDateStamp;
	PVOID LoadedImports;
	PVOID EntryPointActivationContext;
	PVOID PatchInformation;
} LDR_DATA_TABLE_ENTRY, * PLDR_DATA_TABLE_ENTRY;

VOID DriverUnload(PDRIVER_OBJECT driver);
NTSTATUS DriverEntry(PDRIVER_OBJECT driver, PUNICODE_STRING reg_path);
BOOLEAN KillProcessByPid(PDRIVER_OBJECT driver, UINT32 pid);
BOOLEAN GetKernelBase(IN PDRIVER_OBJECT driver, OUT PVOID* pkrnlbase, OUT PUINT32 pkrnlsize);
PVOID MemorySearch(IN PVOID bytecode, IN PVOID beginAddr, IN UINT32 length, IN PVOID endAddr);
NTSTATUS IrpDeviceControlProc(PDEVICE_OBJECT pDevObj, PIRP pIrp);

// PspTerminateProcess函数指针
typedef NTSTATUS(*_PspTerminateProcess)(PEPROCESS pEprocess,
	NTSTATUS ExitCode);
_PspTerminateProcess PspTerminateProcess;

// 全局变量
PDRIVER_OBJECT g_driver;

/*
NTSTATUS DriverEntry(PDRIVER_OBJECT driver, PUNICODE_STRING reg_path)
{
	g_driver = driver;
	driver->DriverUnload = DriverUnload;
	NTSTATUS status;

	PDEVICE_OBJECT pDeviceObj = NULL; // 设备对象指针
	UNICODE_STRING DeviceName; // 设备名，0环用
	UNICODE_STRING SymbolicLinkName; // 符号链接名，3环用

	//和三环通信
	RtlInitUnicodeString(&DeviceName, DEVICE_NAME);
	// 创建设备
	status = IoCreateDevice(driver, 0, &DeviceName,
		FILE_DEVICE_UNKNOWN, FILE_DEVICE_SECURE_OPEN, FALSE, &pDeviceObj);
	if (status != STATUS_SUCCESS)
	{
		IoDeleteDevice(pDeviceObj);
		DbgPrint("创建设备失败.\n");
		return status;
	}
	else
		DbgPrint("创建设备成功.\n");

	// 设置数据交互的方式
	pDeviceObj->Flags |= DO_BUFFERED_IO;

	// 创建符号链接
	RtlInitUnicodeString(&SymbolicLinkName, SYMBOLICLINK_NAME);
	IoCreateSymbolicLink(&SymbolicLinkName, &DeviceName);

	// 设置分发函数
	driver->MajorFunction[IRP_MJ_DIRECTORY_CONTROL] = IrpDeviceControlProc;



	return STATUS_SUCCESS;
}
*/
NTSTATUS DriverEntry(PDRIVER_OBJECT pDriver, PUNICODE_STRING RegPath)
{
	NTSTATUS status;
	ULONG uIndex = 0;
	PDEVICE_OBJECT pDeviceObj = NULL; // 设备对象指针
	UNICODE_STRING DeviceName; // 设备名，0环用
	UNICODE_STRING SymbolicLinkName; // 符号链接名，3环用

	// 创建设备名称
	RtlInitUnicodeString(&DeviceName, DEVICE_NAME);
	// 创建设备
	status = IoCreateDevice(pDriver, 0, &DeviceName, FILE_DEVICE_UNKNOWN, FILE_DEVICE_SECURE_OPEN, FALSE, &pDeviceObj);
	if (status != STATUS_SUCCESS)
	{
		IoDeleteDevice(pDeviceObj);
		DbgPrint("创建设备失败.\n");
		return status;
	}
	DbgPrint("创建设备成功.\n");
	// 设置交互数据的方式
	pDeviceObj->Flags |= DO_BUFFERED_IO;
	// 创建符号链接
	RtlInitUnicodeString(&SymbolicLinkName, SYMBOLICLINK_NAME);
	IoCreateSymbolicLink(&SymbolicLinkName, &DeviceName);
	// 设置分发函数
	pDriver->MajorFunction[IRP_MJ_DEVICE_CONTROL] = IrpDeviceControlProc;
	// 设置卸载函数
	pDriver->DriverUnload = DriverUnload;
	return STATUS_SUCCESS;
}

/*
// IRP_MJ_DEVICE_CONTROL 处理函数
NTSTATUS IrpDeviceControlProc(PDEVICE_OBJECT pDevObj, PIRP pIrp)
{
	// DbgPrint("IrpDeviceControlProc.\n");
	NTSTATUS status = STATUS_INVALID_DEVICE_REQUEST;
	PIO_STACK_LOCATION pIrpStack;
	ULONG uIoControlCode;
	PVOID pIoBuffer;
	// unsigned long是4个字节
	ULONG uInLength;
	ULONG uOutLength;
	ULONG uRead;
	ULONG uWrite;

	// 设置临时变量的值
	uRead = 0;
	uWrite = 0x12345678;
	// 获取IRP数据
	pIrpStack = IoGetCurrentIrpStackLocation(pIrp);
	// 获取控制码
	uIoControlCode = pIrpStack->Parameters.DeviceIoControl.IoControlCode;
	// 获取缓冲区地址（输入输出是同一个）
	pIoBuffer = pIrp->AssociatedIrp.SystemBuffer;
	// Ring3 发送数据的长度
	uInLength = pIrpStack->Parameters.DeviceIoControl.InputBufferLength;
	// Ring0 发送数据的长度
	uOutLength = pIrpStack->Parameters.DeviceIoControl.OutputBufferLength;

	switch (uIoControlCode)
	{
	case OPER1:
	{
		DbgPrint("执行了OPER1\n");
		pIrp->IoStatus.Information = 0;
		status = STATUS_SUCCESS;
		break;
	}
	case OPER2:
	{
		DbgPrint("IrpDeviceControlProc -> OPER2 输入字节数: %d\n", uInLength);
		DbgPrint("IrpDeviceControlProc -> OPER2 输出字节数: %d\n", uOutLength);
		// 读取缓冲区
		memcpy(&uRead, pIoBuffer, 4);
		DbgPrint("IrpDeviceControlProc -> OPER2 uRead: %x\n", uRead);
		// 写入缓冲区
		memcpy(pIoBuffer, &uWrite, 4);

		KillProcessByPid(g_driver, uRead);

		// 设置状态
		pIrp->IoStatus.Information = 2; // 返回两字节
		status = STATUS_SUCCESS;
		break;
	}
	}

	// 返回状态如果不设置，Ring3返回值是失败
	pIrp->IoStatus.Status = status;
	IoCompleteRequest(pIrp, IO_NO_INCREMENT);
	return STATUS_SUCCESS;
}*/

// IRP_MJ_DEVICE_CONTROL 处理函数
NTSTATUS IrpDeviceControlProc(PDEVICE_OBJECT pDevObj, PIRP pIrp)
{
	// DbgPrint("IrpDeviceControlProc.\n");
	NTSTATUS status = STATUS_INVALID_DEVICE_REQUEST;
	PIO_STACK_LOCATION pIrpStack;
	ULONG uIoControlCode;
	PVOID pIoBuffer;
	ULONG uInLength;
	ULONG uOutLength;
	ULONG uRead;
	ULONG uWrite;

	// 设置临时变量的值
	uRead = 0;
	uWrite = 0x12345678;
	// 获取IRP数据
	pIrpStack = IoGetCurrentIrpStackLocation(pIrp);
	// 获取控制码
	uIoControlCode = pIrpStack->Parameters.DeviceIoControl.IoControlCode;
	// 获取缓冲区地址（输入输出是同一个）
	pIoBuffer = pIrp->AssociatedIrp.SystemBuffer;
	// Ring3 发送数据的长度
	uInLength = pIrpStack->Parameters.DeviceIoControl.InputBufferLength;
	// Ring0 发送数据的长度
	uOutLength = pIrpStack->Parameters.DeviceIoControl.OutputBufferLength;

	switch (uIoControlCode)
	{
	case OPER1:
	{
		DbgPrint("IrpDeviceControlProc -> OPER1...\n");
		pIrp->IoStatus.Information = 0;
		status = STATUS_SUCCESS;
		break;
	}
	case OPER2:
	{
		DbgPrint("IrpDeviceControlProc -> OPER2 输入字节数: %d\n", uInLength);
		DbgPrint("IrpDeviceControlProc -> OPER2 输出字节数: %d\n", uOutLength);
		// 读取缓冲区
		memcpy(&uRead, pIoBuffer, 4);
		DbgPrint("IrpDeviceControlProc -> OPER2 uRead: %x\n", uRead);
		// 写入缓冲区
		memcpy(pIoBuffer, &uWrite, 4);
		// 设置状态
		pIrp->IoStatus.Information = 2; // 返回两字节
		status = STATUS_SUCCESS;
		break;
	}
	}

	// 返回状态如果不设置，Ring3返回值是失败
	pIrp->IoStatus.Status = status;
	IoCompleteRequest(pIrp, IO_NO_INCREMENT);
	return STATUS_SUCCESS;
}

// 封装杀进程API
BOOLEAN KillProcessByPid(PDRIVER_OBJECT driver, UINT32 pid)
{
	// 内存特征码
	UINT32 bytecode[] = {
		0x8b55ff8b,
		0xa16456ec,
		0x00000124,
		0x3b08758b
	};
	PVOID pKrnlBase;        // 内核基址
	UINT32 uKrnlImageSize;  // 内核大小
	PEPROCESS pEprocess;    // 要关闭的进程的EPROCESS

	// 获取内核模块基址和大小
	if (GetKernelBase(driver, &pKrnlBase, &uKrnlImageSize) == FALSE)
	{
		DbgPrint("获取内核模块基址和大小失败\r\n");
		return FALSE;
	}
	else
		DbgPrint("内核基址: %p，大小: %X\n", pKrnlBase, uKrnlImageSize);

	PspTerminateProcess =
		MemorySearch(bytecode, pKrnlBase, sizeof(bytecode),
			(PVOID)((PCHAR)pKrnlBase + uKrnlImageSize));

	if (PspTerminateProcess != NULL)
	{
		DbgPrint("找到特征码，函数开头：%p, 开头4字节：0x%x\r\n",
			PspTerminateProcess, *((PUINT32)PspTerminateProcess - 6));
	}

	else
	{
		DbgPrint("没有找到特征码！");
		return FALSE;
	}

	PsLookupProcessByProcessId((HANDLE)pid, &pEprocess); // 记事本PID是1796
	// 调用 PspTerminateProcess 关闭进程
	PspTerminateProcess(pEprocess, 0);
	DbgPrint("0x%x进程被 PspTerminateProcess 函数关闭了.\n", pid);

	return TRUE;
}

BOOLEAN GetKernelBase(IN PDRIVER_OBJECT driver, OUT PVOID* pkrnlbase, OUT PUINT32 pkrnlsize)
{
	// 设定头和遍历指针
	PLDR_DATA_TABLE_ENTRY pldrHead = (PLDR_DATA_TABLE_ENTRY)(driver->DriverSection);
	PLDR_DATA_TABLE_ENTRY pldrcur = pldrHead;
	UNICODE_STRING usKrnlBaseDllName;  // 内核模块名

	RtlInitUnicodeString(&usKrnlBaseDllName, L"ntoskrnl.exe");

	do
	{
		// 如果找到了
		if (RtlCompareUnicodeString(&usKrnlBaseDllName, &pldrcur->BaseDllName, TRUE) == 0)
		{
			*pkrnlbase = pldrcur->DllBase;
			*pkrnlsize = pldrcur->SizeOfImage;
			return TRUE;
		}
		// 指向下一个节点
		pldrcur = (PLDR_DATA_TABLE_ENTRY)pldrcur->InLoadOrderLinks.Flink;

	} while (pldrcur != pldrHead);

	return FALSE;
}

// 用来查找特征码的起始位置
PVOID MemorySearch(IN PVOID bytecode, IN PVOID beginAddr, IN UINT32 length, IN PVOID endAddr)
{
	DbgPrint("inside MemorySearch, length = %d\r\n", length);
	PVOID pcur = beginAddr;

	while (pcur != endAddr)
	{
		UINT32 tlen = RtlCompareMemory(pcur, bytecode, length);
		//if (RtlCompareMemory(pcur, bytecode, length) == length)

		if (tlen == length)
		{
			DbgPrint("找到特征码，内存地址%p\r\n", pcur);
			return pcur;
		}
		((UINT32)pcur)++;
	}

	// 没有找到则返回空指针
	DbgPrint("memorysearch失败\r\n");
	return NULL;
}

// 卸载驱动
VOID DriverUnload(PDRIVER_OBJECT driver)
{
	UNICODE_STRING SymbolicLinkName;
	// 删除符号链接，删除设备
	RtlInitUnicodeString(&SymbolicLinkName, SYMBOLICLINK_NAME);
	IoDeleteSymbolicLink(&SymbolicLinkName);
	IoDeleteDevice(g_driver->DeviceObject);

	DbgPrint("驱动卸载成功\n");
}

```





### shellcode

```cpp
// IRPTest_R3.cpp : 定义控制台应用程序的入口点。
//
#include "stdafx.h"
#include <Windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <winioctl.h>
#include <iostream>

using namespace std;

// 不能用库函数
#define TOUPPER(x) ((((x) >= 'a') && ((x) <= 'z')) ? ((x)-32) : (x))
#define TOLOWER(x) ((((x) >= 'A') && ((x) <= 'Z')) ? ((x) + 32) : (x))
#define EXIT_ERROR(x)                                 \
    do                                                \
    {                                                 \
	cout << "error in line " << __LINE__ << endl; \
	cout << x;                                    \
	getchar();                                    \
	exit(EXIT_FAILURE);                           \
    } while (0)
#define MY_ASSERT(x)                         \
    do                                       \
{                                        \
	if (!x)                              \
	EXIT_ERROR("ASSERTION failed!"); \
    } while (0)

typedef struct _UNICODE_STRING
{
    USHORT Length;
    USHORT MaximumLength;
    PWSTR Buffer;
} UNICODE_STRING, *PUNICODE_STRING;

typedef struct _PEB_LDR_DATA
{
    DWORD Length;
    bool Initialized;
    PVOID SsHandle;
    LIST_ENTRY InLoadOrderModuleList;
    LIST_ENTRY InMemoryOrderModuleList;
    LIST_ENTRY InInitializationOrderModuleList;
} PEB_LDR_DATA, *PPEB_LDR_DATA;

typedef struct _LDR_DATA_TABLE_ENTRY
{
    LIST_ENTRY InLoadOrderLinks;
    LIST_ENTRY InMemoryOrderLinks;
    LIST_ENTRY InInitializationOrderLinks;
    PVOID DllBase;
    PVOID EntryPoint;
    UINT32 SizeOfImage;
    UNICODE_STRING FullDllName;
    UNICODE_STRING BaseDllName;
    UINT32 Flags;
    USHORT LoadCount;
    USHORT TlsIndex;
    LIST_ENTRY HashLinks;
    PVOID SectionPointer;
    UINT32 CheckSum;
    UINT32 TimeDateStamp;
    PVOID LoadedImports;
    PVOID EntryPointActivationContext;
    PVOID PatchInformation;
} LDR_DATA_TABLE_ENTRY, *PLDR_DATA_TABLE_ENTRY;

// DWORD RVA_TO_FOA(LPVOID hKernel32, PIMAGE_DOS_HEADER pDosHeader,
//                  PIMAGE_NT_HEADERS32 pNTHeader,
//                  PIMAGE_SECTION_HEADER pSectionHeader, IN DWORD RVA);

void init()
{
//	freopen("c:\\123.txt", "w", stdout);
}

int main()
{
	init();
	PPEB_LDR_DATA pLDR = NULL;
	HMODULE hKernel32 = NULL;
    HMODULE hUser32 = NULL;

	char szKernel32[] = {
        'k', 0, 'e', 0, 'r', 0, 'n', 0, 'e', 0, 'l', 0, '3', 0,
			'2', 0, '.', 0, 'd', 0, 'l', 0, 'l', 0, 0,   0};  // Unicode
		char szUser32[] = {'u', 's', 'e', 'r', '3', '2', '.', 'd', 'l', 'l', 0};
		char szGetProcAddress[] = {'G', 'e', 't', 'P', 'r', 'o', 'c', 'A',
			'd', 'd', 'r', 'e', 's', 's', 0};
		char szLoadLibrary[] = {'L', 'o', 'a', 'd', 'L', 'i', 'b',
			'r', 'a', 'r', 'y', 'A', 0};
		char szMessageBoxA[] = {'M', 'e', 's', 's', 'a', 'g',
			'e', 'B', 'o', 'x', 'A', 0};
		char szHelloShellCode[] = {'H', 'e', 'l', 'l', 'o', 'S', 'h', 'e',
                               'l', 'l', 'C', 'o', 'd', 'e', 0};

	PPEB_LDR_DATA pltr = NULL;

	__asm {
		mov eax,fs:[0x30]  // PEB
		mov eax,[eax+0x0C]  // PEB->LDR
		mov pLDR,eax
    }
	
	// 这里不是一个指针，要&
	PLDR_DATA_TABLE_ENTRY pldrHead = (PLDR_DATA_TABLE_ENTRY)(&(pLDR->InLoadOrderModuleList));
	PLDR_DATA_TABLE_ENTRY pldrcur = (PLDR_DATA_TABLE_ENTRY)(pldrHead->InLoadOrderLinks.Flink);

	

	while (pldrcur != pldrHead)
	{
		PCHAR pchar1 = szKernel32;
		printf("%ws\n", pldrcur->BaseDllName.Buffer);
		PCHAR pchar2 = (PCHAR)(pldrcur->BaseDllName.Buffer);
		
		BOOL equalFlag = FALSE;

		while (1)
		{
			if ((*((PWORD)pchar1) == 0) && (*((PWORD)pchar2) == 0))
			{
				equalFlag = TRUE;
				break;
			}

			if (TOUPPER(*pchar1) != TOUPPER(*pchar2))
            {
                break;
            }
            pchar1 += 2;
            pchar2 += 2;
		}

		if (equalFlag)
		{
			hKernel32 = (HMODULE)(pldrcur->DllBase);
		}
		
		// 往前指
		pldrcur = (PLDR_DATA_TABLE_ENTRY)(pldrcur->InLoadOrderLinks.Flink);
	}

	if (hKernel32 == NULL)
	{
		printf("搜索kernel32失败！");
		getchar();
		exit(EXIT_FAILURE);
	}
	
	PIMAGE_DOS_HEADER pDosHeader = NULL;
	PIMAGE_NT_HEADERS32 pNTHeader = NULL;
	PIMAGE_SECTION_HEADER pSectionHeader = NULL;

	pDosHeader = (PIMAGE_DOS_HEADER)(hKernel32);
    MY_ASSERT(pDosHeader);
    MY_ASSERT((pDosHeader->e_magic == IMAGE_DOS_SIGNATURE));
	
	pNTHeader =
        (PIMAGE_NT_HEADERS32)((PBYTE)hKernel32 + pDosHeader->e_lfanew);
	MY_ASSERT(pNTHeader);
    if (pNTHeader->FileHeader.SizeOfOptionalHeader != 0xe0)
        EXIT_ERROR("this is not a 32-bit executable file.");

	pSectionHeader = (PIMAGE_SECTION_HEADER)(
        (PBYTE)pNTHeader + sizeof(IMAGE_NT_SIGNATURE) +
        sizeof(IMAGE_FILE_HEADER) + pNTHeader->FileHeader.SizeOfOptionalHeader);
	MY_ASSERT(pSectionHeader);

	// 导入表
	PIMAGE_IMPORT_DESCRIPTOR pImportDescriptor = (PIMAGE_IMPORT_DESCRIPTOR)(
        (PBYTE)hKernel32 + pNTHeader->OptionalHeader.DataDirectory[1].VirtualAddress);
	MY_ASSERT(pImportDescriptor);

	// 遍历导入表
	while (pImportDescriptor->Name != 0 || pImportDescriptor->FirstThunk != 0)
	{
		printf("0x%x\n", (PBYTE)hKernel32 + pImportDescriptor->Name);

		printf("DLL name: %s\n",
			(PCHAR)(PBYTE)hKernel32 + pImportDescriptor->Name);

		PDWORD pThunkData_INT = (PDWORD)((PBYTE)hKernel32 + pImportDescriptor->OriginalFirstThunk);
		PDWORD pThunkData_IAT = (PDWORD)((PBYTE)hKernel32 + pImportDescriptor->FirstThunk);

		PIMAGE_IMPORT_BY_NAME pImportByName = NULL;
		
		while (*pThunkData_INT)
		{
			if ((*pThunkData_INT) & 0x80000000)
			{
				printf("按序号导出：0x%x\n", (*pThunkData_INT) & 0x7fffffff);
			}
			else
			{
				pImportByName = (PIMAGE_IMPORT_BY_NAME)(
					(PBYTE)hKernel32 + (((DWORD)(*pThunkData_INT)) & 0x7fffffff));
				MY_ASSERT(pImportByName);
				printf("按名字导出：%s\n", pImportByName->Name);


				PCHAR pchar1 = szGetProcAddress;
				PCHAR pchar2 = (PCHAR)pImportByName->Name;

				BOOL flag = FALSE;

				while (1)
				{
					if (*pchar1 == 0 && *pchar2 == 0)
					{
						flag = TRUE;
						break;
					}

					if (*pchar1 != *pchar2) break;

					pchar1 ++ , pchar2 ++ ;
				}

				if (flag == TRUE)
				{
					printf("找到了!");
					getchar();
				}

// 这里不能用strcmp
// 				if (strcmp((PCHAR)(pImportByName->Name), szGetProcAddress) == 0)
// 				{
// 					printf("找到了!");
// 					getchar();
// 				}
			}

			pThunkData_INT ++ , pThunkData_IAT ++ ;
		}

		pImportDescriptor ++ ;
	}


	printf("无事发生");
	getchar();

	return 0;
}

// DWORD RVA_TO_FOA(LPVOID hKernel32, PIMAGE_DOS_HEADER pDosHeader,
//                  PIMAGE_NT_HEADERS32 pNTHeader,
//                  PIMAGE_SECTION_HEADER pSectionHeader, IN DWORD RVA)
// {
//     if (RVA < pNTHeader->OptionalHeader.SizeOfHeaders)
//         return RVA;
// 	
//     for (int i = 0; i < pNTHeader->FileHeader.NumberOfSections; i++)
//     {
//         if (RVA >= pSectionHeader[i].VirtualAddress &&
//             RVA < pSectionHeader[i].VirtualAddress +
// 			pSectionHeader[i].Misc.VirtualSize)
//         {
//             return (RVA - pSectionHeader[i].VirtualAddress +
// 				pSectionHeader[i].PointerToRawData);
//         }
//     }
// 	
//     EXIT_ERROR("rva to foa failure!");
// }
```





