// dllmain.cpp : 定义 DLL 应用程序的入口点。
#include "pch.h"
#include <windows.h>
#include "head.h"
#include <Psapi.h>
#include <timeapi.h>
#pragma comment(lib,"Winmm.lib")
#pragma warning(disable:4996)

#define PATCH_INLINE 5
#undef _DEBUG

typedef BOOL(*zyc_QueryPerformanceCounter)(__out LARGE_INTEGER* lpPerformanceCount);
typedef DWORD(*zyc_2)(VOID);

zyc_2 old_timegettime;
zyc_2 old_gettickcount;
zyc_QueryPerformanceCounter old_QueryPerformanceCounter;
DWORD m_s_iSpeedTimes = 10;

DWORD WINAPI NewTimeGetTime(VOID)
{
	static DWORD fake = 0;
	static DWORD last_real = 0;
	DWORD now = old_timegettime();
	DWORD result;

	if (last_real == 0)
	{
		result = fake = last_real = now;
	}
	else
	{
		result = fake + m_s_iSpeedTimes * (now - last_real);
		fake = result;
		last_real = now;
	}

	return result;
}

DWORD WINAPI NewGetTickCount(void)
{
	static DWORD fake = 0;
	static DWORD last_real = 0;
	DWORD now = old_gettickcount();
	DWORD result;

	if (last_real == 0)
	{
		result = fake = last_real = now;
	}
	else
	{
		result = fake + m_s_iSpeedTimes * (now - last_real);
		fake = result;
		last_real = now;
	}

	return result;
}

BOOL WINAPI NewQueryPerformanceCounter(__out LARGE_INTEGER* lpPerformanceCount)
{
	BOOL ret = old_QueryPerformanceCounter(lpPerformanceCount);
	if (!ret) return ret;

	static LARGE_INTEGER fake = { 0 };
	static LARGE_INTEGER last_real = { 0 };
	LARGE_INTEGER now = *lpPerformanceCount;

	if (last_real.QuadPart == 0)
	{
		fake = last_real = now;
	}
	else
	{
		lpPerformanceCount->QuadPart = fake.QuadPart + m_s_iSpeedTimes * (now.QuadPart - last_real.QuadPart);
		fake = *lpPerformanceCount;
		last_real = now;
	}

	return ret;
}

VOID init()
{
	LPVOID pImageBuffer = NULL;
	PIMAGE_DOS_HEADER pImageDosHeader = NULL;
	PIMAGE_NT_HEADERS32 pImageNTHeader = NULL;
	PIMAGE_SECTION_HEADER pImageSectionHeader = NULL;

	// 获取进程信息
	MODULEINFO moduleInfo;
	MY_ASSERT(GetModuleInformation(GetCurrentProcess(),
		GetModuleHandle(TEXT("hl2.exe")), &moduleInfo, sizeof(moduleInfo)));
	pImageBuffer = malloc(moduleInfo.SizeOfImage);
	printf("moduleinfo.baseofdll = 0x%p\r\n", moduleInfo.lpBaseOfDll);

	// 读取SizeOfImage大小的内存，放到pImageBuffer里面
	DWORD dwSizeRead = 0;
	MY_ASSERT(ReadProcessMemory(GetCurrentProcess(), moduleInfo.lpBaseOfDll,
		pImageBuffer, moduleInfo.SizeOfImage, &dwSizeRead));
	MY_ASSERT(moduleInfo.SizeOfImage == dwSizeRead);

	// 设定各种指针
	pImageDosHeader = (PIMAGE_DOS_HEADER)pImageBuffer;
	MY_ASSERT(pImageDosHeader);
	MY_ASSERT((pImageDosHeader->e_magic == IMAGE_DOS_SIGNATURE));
	pImageNTHeader =
		(PIMAGE_NT_HEADERS32)((PBYTE)pImageBuffer + pImageDosHeader->e_lfanew);
	MY_ASSERT(pImageNTHeader->FileHeader.SizeOfOptionalHeader == 0xe0);

	// 读取IAT表
	PIMAGE_IMPORT_DESCRIPTOR pImportDescriptor = (PIMAGE_IMPORT_DESCRIPTOR)(
		(PBYTE)pImageBuffer +
		pImageNTHeader->OptionalHeader.DataDirectory[1].VirtualAddress);

	// 设定旧timegettime指针
	old_timegettime = (zyc_2)timeGetTime;
	printf("old_timegettime = 0x%p\r\n", (DWORD)old_timegettime);
	MY_ASSERT(old_timegettime);

	// 设定旧gettickcount
	old_gettickcount = (zyc_2)GetTickCount;
	printf("old_gettickcount = 0x%p\r\n", (DWORD)old_gettickcount);
	MY_ASSERT(old_gettickcount);

	// 设定QueryPerformanceCounter
	old_QueryPerformanceCounter = (zyc_QueryPerformanceCounter)QueryPerformanceCounter;
	printf("QueryPerformanceCounter = 0x%p\r\n", (DWORD)old_QueryPerformanceCounter);
	MY_ASSERT(old_QueryPerformanceCounter);

	while (pImportDescriptor->Name != 0 || pImportDescriptor->FirstThunk != 0)
	{
		printf("DLL name: %s\n",
			(PCHAR)((PBYTE)pImageBuffer + pImportDescriptor->Name));

		PDWORD pThunkData_IAT = NULL;

		pThunkData_IAT = (PDWORD)(
			(PBYTE)pImageBuffer + pImportDescriptor->FirstThunk);

		PIMAGE_IMPORT_BY_NAME pImportByName = NULL;

		puts("");
		printf("IAT表:\n");
		while (*pThunkData_IAT)
		{
			if ((DWORD)old_timegettime == *pThunkData_IAT)
			{
				printf("找到了timegettime!\r\n");

				// 设定新地址
				DWORD dwSizeWritten = 0;
				DWORD t_addr = (DWORD)NewTimeGetTime;

				// 获得需要修改的地址离基址的偏移
				DWORD offsetToFunAddr = (DWORD)pThunkData_IAT - (DWORD)pImageBuffer;

				DWORD state = 0;
				DWORD a = VirtualProtect((LPVOID)((DWORD)moduleInfo.lpBaseOfDll + offsetToFunAddr), 10, PAGE_EXECUTE_READWRITE, &state);
				if (a == 0)
				{
					printf("virtualprtect failure! %d\r\n",GetLastError());
				}
				printf("before written 0x%p\r\n", *((PDWORD)((DWORD)moduleInfo.lpBaseOfDll + offsetToFunAddr)));
				MY_ASSERT(WriteProcessMemory(GetCurrentProcess(), (LPVOID)((DWORD)moduleInfo.lpBaseOfDll + offsetToFunAddr),
					(LPVOID)(&t_addr), sizeof(DWORD), &dwSizeWritten));
				printf("after written 0x%p\r\n", *((PDWORD)((DWORD)moduleInfo.lpBaseOfDll + offsetToFunAddr)));
				MY_ASSERT(dwSizeWritten == sizeof(DWORD));
			}

			else if ((DWORD)old_QueryPerformanceCounter == *pThunkData_IAT)
			{
				printf("找到了QueryPerformanceCounter!\r\n");

				// 设定新地址
				DWORD dwSizeWritten = 0;
				DWORD t_addr = (DWORD)NewQueryPerformanceCounter;

				// 获得需要修改的地址离基址的偏移
				DWORD offsetToFunAddr = (DWORD)pThunkData_IAT - (DWORD)pImageBuffer;

				DWORD state = 0;
				DWORD a = VirtualProtect((LPVOID)((DWORD)moduleInfo.lpBaseOfDll + offsetToFunAddr), 10, PAGE_EXECUTE_READWRITE, &state);
				if (a == 0)
				{
					printf("virtualprtect failure! %d\r\n", GetLastError());
				}
				printf("before written 0x%p\r\n", *((PDWORD)((DWORD)moduleInfo.lpBaseOfDll + offsetToFunAddr)));
				MY_ASSERT(WriteProcessMemory(GetCurrentProcess(), (LPVOID)((DWORD)moduleInfo.lpBaseOfDll + offsetToFunAddr),
					(LPVOID)(&t_addr), sizeof(DWORD), &dwSizeWritten));
				printf("after written 0x%p\r\n", *((PDWORD)((DWORD)moduleInfo.lpBaseOfDll + offsetToFunAddr)));
				MY_ASSERT(dwSizeWritten == sizeof(DWORD));
			}

			else if ((DWORD)old_gettickcount == *pThunkData_IAT)
			{
				printf("找到了gettickcount!\r\n");

				// 设定新地址
				DWORD dwSizeWritten = 0;
				DWORD t_addr = (DWORD)NewGetTickCount;

				// 获得需要修改的地址离基址的偏移
				DWORD offsetToFunAddr = (DWORD)pThunkData_IAT - (DWORD)pImageBuffer;

				DWORD state = 0;
				DWORD a = VirtualProtect((LPVOID)((DWORD)moduleInfo.lpBaseOfDll + offsetToFunAddr), 10, PAGE_EXECUTE_READWRITE, &state);
				if (a == 0)
				{
					printf("virtualprtect failure! %d\r\n", GetLastError());
				}
				printf("before written 0x%p\r\n", *((PDWORD)((DWORD)moduleInfo.lpBaseOfDll + offsetToFunAddr)));
				MY_ASSERT(WriteProcessMemory(GetCurrentProcess(), (LPVOID)((DWORD)moduleInfo.lpBaseOfDll + offsetToFunAddr),
					(LPVOID)(&t_addr), sizeof(DWORD), &dwSizeWritten));
				printf("after written 0x%p\r\n", *((PDWORD)((DWORD)moduleInfo.lpBaseOfDll + offsetToFunAddr)));
				MY_ASSERT(dwSizeWritten == sizeof(DWORD));
			}

			pThunkData_IAT++;
		}

		puts("");
		pImportDescriptor++;  // 将pImportDescriptor向后移动
	}
	//MessageBoxA(0, 0, 0, 0);
	//__asm int 3
	MessageBoxA(0, "内容", "标题", 0);
	//system("pause");
}

BOOL APIENTRY DllMain(HMODULE hModule,
	DWORD  ul_reason_for_call,
	LPVOID lpReserved
)
{
	switch (ul_reason_for_call)
	{
	case DLL_PROCESS_ATTACH:
		MessageBoxA(0, 0, "DLL注入成功！", 0);
		AllocConsole();
		SetConsoleTitle(TEXT("Debug Output"));
		freopen("CONOUT$", "w", stdout);
		init();
		MessageBoxA(0, "HOOK成功！", "HOOK成功！", 0);
		break;
	case DLL_THREAD_ATTACH:

	case DLL_THREAD_DETACH:

	case DLL_PROCESS_DETACH:

		break;
	}
	return TRUE;
}

DWORD ReadPEFile(IN LPCSTR file_in, OUT LPVOID& pImageBuffer,
	PIMAGE_DOS_HEADER& pImageDosHeader, PIMAGE_NT_HEADERS32& pImageNTHeader,
	PIMAGE_SECTION_HEADER& pSectionHeader)
{
	FILE* fp;
	fp = fopen(file_in, "rb");
	if (!fp)
		EXIT_ERROR("fp == NULL!");
	DWORD file_size = 0;
	fseek(fp, 0, SEEK_END);
	file_size = ftell(fp);
	fseek(fp, 0, SEEK_SET);

	LPVOID t = malloc(file_size);
	if ((fread(t, file_size, 1, fp) != 1) || t == NULL)
		EXIT_ERROR("fread error or malloc error!");

	pImageBuffer = t;
	MY_ASSERT(pImageBuffer);

	pImageDosHeader = (PIMAGE_DOS_HEADER)(pImageBuffer);
	MY_ASSERT(pImageDosHeader);
	MY_ASSERT((pImageDosHeader->e_magic == IMAGE_DOS_SIGNATURE));

	pImageNTHeader =
		(PIMAGE_NT_HEADERS32)((PBYTE)pImageBuffer + pImageDosHeader->e_lfanew);
	if (pImageNTHeader->FileHeader.SizeOfOptionalHeader != 0xe0)
		EXIT_ERROR("this is not a 32-bit executable file.");

	pSectionHeader = (PIMAGE_SECTION_HEADER)(
		(PBYTE)pImageNTHeader + sizeof(IMAGE_NT_SIGNATURE) +
		sizeof(IMAGE_FILE_HEADER) + pImageNTHeader->FileHeader.SizeOfOptionalHeader);
	fclose(fp);
	return file_size;
}

DWORD RVA_TO_FOA(LPVOID pImageBuffer, PIMAGE_DOS_HEADER pImageDosHeader,
	PIMAGE_NT_HEADERS32 pImageNTHeader,
	PIMAGE_SECTION_HEADER pSectionHeader, IN DWORD RVA)
{
	if (RVA < pImageNTHeader->OptionalHeader.SizeOfHeaders)
		return RVA;

	for (int i = 0; i < pImageNTHeader->FileHeader.NumberOfSections; i++)
	{
		if (RVA >= pSectionHeader[i].VirtualAddress &&
			RVA < pSectionHeader[i].VirtualAddress +
			pSectionHeader[i].Misc.VirtualSize)
		{
			return (RVA - pSectionHeader[i].VirtualAddress +
				pSectionHeader[i].PointerToRawData);
		}
	}

	EXIT_ERROR("rva to foa failure!");
}

DWORD FOA_TO_RVA(LPVOID pImageBuffer, PIMAGE_DOS_HEADER pImageDosHeader,
	PIMAGE_NT_HEADERS32 pImageNTHeader,
	PIMAGE_SECTION_HEADER pSectionHeader, IN DWORD FOA)
{
	if (FOA < pImageNTHeader->OptionalHeader.SizeOfHeaders)
		return FOA;

	for (int i = 0; i < pImageNTHeader->FileHeader.NumberOfSections; i++)
	{
		if (FOA >= pSectionHeader[i].PointerToRawData &&
			FOA < pSectionHeader[i].PointerToRawData +
			pSectionHeader[i].Misc.VirtualSize)
		{
			return (FOA - pSectionHeader[i].PointerToRawData +
				pSectionHeader[i].VirtualAddress);
		}
	}

	EXIT_ERROR("foa to rva error!");
}