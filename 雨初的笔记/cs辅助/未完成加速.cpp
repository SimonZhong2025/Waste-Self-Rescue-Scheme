// dllmain.cpp : 定义 DLL 应用程序的入口点。
#include "pch.h"
#include <windows.h>
#include "head.h"
#include <Psapi.h>
#include <timeapi.h>
#pragma warning(disable:4996)

#define PATCH_INLINE 5
DWORD m_s_iSpeedTimes = 100; // 5倍加速
DWORD gettickcount_real_addr = 0x76F917F0;
DWORD QueryPerformanceCounter_real_addr = 0x76F9158C;

typedef BOOL(*zyc_QueryPerformanceCounter)(__out LARGE_INTEGER* lpPerformanceCount);
typedef DWORD(*zyc_2)(VOID);
zyc_2 g_oldGetTickCount;
zyc_2 g_oldTimeGetTime;
zyc_QueryPerformanceCounter g_oldQueryPerformanceCounter;

DWORD WINAPI NewTimeGetTime(VOID)
{
	static DWORD fake = 0;
	static DWORD last_real = 0;
	DWORD now = (*g_oldTimeGetTime)();
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

DWORD _declspec(naked) naked_GetTickCount()
{
	_asm
	{
		push ecx
		call[gettickcount_real_addr] // 76F331D1 FF 15 F0 17 F9 76    call        dword ptr [__imp__GetTickCount@0 (76F917F0h)]  
		pop ecx
	}
}

DWORD WINAPI NewGetTickCount(VOID)
{
	static DWORD fake = 0;
	static DWORD last_real = 0;
	DWORD now = naked_GetTickCount();
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

BOOL _declspec(naked) naked_NewQueryPerformanceCounter(__out LARGE_INTEGER* lpPerformanceCount)
{
	__asm
	{
		jmp[QueryPerformanceCounter]
	}
}

BOOL WINAPI NewQueryPerformanceCounter(__out LARGE_INTEGER* lpPerformanceCount)
{
	//BOOL ret = (*g_oldQueryPerformanceCounter)(lpPerformanceCount);
	BOOL ret = naked_NewQueryPerformanceCounter(lpPerformanceCount);
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

VOID hook_TimeGetTime()
{
	//页面属性备份
	DWORD state = 0;

	//HOOK函数的地址备份
	g_oldTimeGetTime = (zyc_2)(DWORD)GetProcAddress(GetModuleHandleA("Winmm.dll"), "timeGetTime");

	//跳转代码
	BYTE byJmpCode[PATCH_INLINE] = { 0xe9 };
	*(DWORD*)&byJmpCode[1] = (DWORD)NewTimeGetTime - (DWORD)g_oldTimeGetTime - 5;

	//开始HOOK
	VirtualProtect((PVOID)g_oldTimeGetTime, PATCH_INLINE, PAGE_READWRITE, &state);
	memcpy((PVOID)g_oldTimeGetTime, byJmpCode, PATCH_INLINE);

	// 保存原来的call位置，跳过stub
	g_oldTimeGetTime = (zyc_2)((DWORD)(*((PDWORD)(PCHAR(g_oldTimeGetTime) + 1))));
	//VirtualProtect((PVOID)g_oldTimeGetTime, PATCH_INLINE, state, &state);
}

VOID hook_GetTickCount()
{
	// 备份状态
	DWORD state = 0;

	//HOOK函数的地址备份
	g_oldGetTickCount = (zyc_2)(DWORD)GetProcAddress(GetModuleHandleA("Kernel32.dll"), "GetTickCount");

	//跳转代码
	BYTE byJmpCode[PATCH_INLINE] = { 0xe9 };
	*(DWORD*)&byJmpCode[1] = (DWORD)NewGetTickCount - (DWORD)g_oldGetTickCount - 5;

	//开始HOOK
	VirtualProtect((PVOID)g_oldGetTickCount, PATCH_INLINE, PAGE_READWRITE, &state);
	memcpy((PVOID)g_oldGetTickCount, byJmpCode, PATCH_INLINE);

	gettickcount_real_addr = (DWORD)(*(PDWORD)((PCHAR)g_oldGetTickCount + 2));
}

VOID hook_QueryPerformanceCounter()
{
	// 备份状态
	DWORD state = 0;

	//HOOK函数的地址备份
	g_oldQueryPerformanceCounter = (zyc_QueryPerformanceCounter)(DWORD)GetProcAddress(GetModuleHandleA("Kernel32.dll"), "QueryPerformanceCounter");

	//跳转代码
	BYTE byJmpCode[PATCH_INLINE] = { 0xe9 };
	*(DWORD*)&byJmpCode[1] = (DWORD)NewQueryPerformanceCounter - (DWORD)g_oldQueryPerformanceCounter - 5;

	//开始HOOK
	VirtualProtect((PVOID)g_oldQueryPerformanceCounter, PATCH_INLINE, PAGE_READWRITE, &state);
	memcpy((PVOID)g_oldQueryPerformanceCounter, byJmpCode, PATCH_INLINE);
	
	// 从代码中获取函数地址
	QueryPerformanceCounter_real_addr = (DWORD)(*(PDWORD)((PCHAR)g_oldQueryPerformanceCounter + 7));
}

VOID init()
{
	CHAR buffer[0x200];
	sprintf(buffer, "%x", gettickcount_real_addr);
	MessageBoxA(0, buffer, "GetTickCount", 0);

	sprintf(buffer, "%x", QueryPerformanceCounter_real_addr);
	MessageBoxA(0, buffer, "QueryPerformanceCounter", 0);


	hook_TimeGetTime();
	MessageBoxA(0, "hook_TimeGetTime", "hook_TimeGetTime", 0);
	Sleep(5000);

	//hook_GetTickCount();
	//MessageBoxA(0, "hook_GetTickCount", "hook_GetTickCount", 0);
	//Sleep(5000);
	//
	//hook_QueryPerformanceCounter();
	//MessageBoxA(0, "hook_GetTickCount", "hook_GetTickCount", 0);
	//Sleep(5000);

}


BOOL APIENTRY DllMain(HMODULE hModule,
	DWORD  ul_reason_for_call,
	LPVOID lpReserved
)
{
	switch (ul_reason_for_call)
	{
	case DLL_PROCESS_ATTACH:
		MessageBox(0, 0, TEXT("DLL注入成功！"), 0);
		init();
		MessageBox(0, TEXT("HOOK成功！"), TEXT("HOOK成功！"), 0);
		break;
	case DLL_THREAD_ATTACH:

	case DLL_THREAD_DETACH:

	case DLL_PROCESS_DETACH:

		break;
	}
	return TRUE;
}



//DWORD _stdcall MyINLINEHookA(PCHAR pDllName, PCHAR pFunName)
//{
//    //页面属性备份
//    DWORD state = 0;
//    //HOOK函数的地址
//    dwHookAddre = (PVOID)GetProcAddress(GetModuleHandleA(pDllName), pFunName);
//    //HOOK结束返回的地址
//    dwRetAddre = (PCHAR)dwHookAddre + PATCH_INLINE;
//    //备份的代码
//    static BYTE byOldJmpCode[PATCH_INLINE] = { 0 };
//    //跳转代码
//    BYTE byJmpCode[PATCH_INLINE] = { 0xe9 };
//    //*(DWORD*)&byJmpCode[1] = (DWORD)NewFunction - (DWORD)dwHookAddre - 5;
//    *(DWORD*)&byJmpCode[1] = (DWORD)NewQueryPerformanceCounter - (DWORD)dwHookAddre - 5;
//    //byJmpCode[PATCH_INLINE-1]=0xfe;
//
//    //备份代码
//    memcpy(byOldJmpCode, dwHookAddre, PATCH_INLINE);
//
//    //开始HOOK
//    VirtualProtect(dwHookAddre, PATCH_INLINE, PAGE_READWRITE, &state);
//    memcpy(dwHookAddre, byJmpCode, PATCH_INLINE);
//    VirtualProtect(dwHookAddre, PATCH_INLINE, state, &state);
//
//    return 0;
//}
//#pragma warning(disable:4996)
//CHAR Kernel32[] = "Kernel32.dll";
//CHAR funname[] = "QueryPerformanceCounter";
//DWORD out;
//PVOID dwHookAddre = 0;
//PCHAR dwRetAddre = 0;
//DWORD Speed = 100;
//#define PATCH_INLINE 5
//DWORD m_s_iSpeedTimes = 2;
//DWORD g_dwTimeGetTimeaddr;
//DWORD g_dwGetTickCountaddr;
//
//// 声明一个指向同样参数、返回值的函数指针类型
//typedef BOOL(*zyc_QueryPerformanceCounter)(__out LARGE_INTEGER* lpPerformanceCount);
//typedef DWORD(*zyc_2)(VOID);
//
//
//
//
//
//DWORD WINAPI NewTimeGetTime(void)
//{
//	static DWORD fake = 0;
//	static DWORD last_real = 0;
//	DWORD now = ((zyc_2)(g_dwTimeGetTimeaddr))();
//	DWORD result;
//
//	if (last_real == 0)
//	{
//		result = fake = last_real = now;
//	}
//	else
//	{
//		result = fake + m_s_iSpeedTimes * (now - last_real);
//		fake = result;
//		last_real = now;
//	}
//
//	return result;
//}
//
//DWORD WINAPI NewGetTickCount(void)
//{
//	static DWORD fake = 0;
//	static DWORD last_real = 0;
//	DWORD now = ((zyc_2)(g_dwGetTickCountaddr))();
//	DWORD result;
//
//	if (last_real == 0)
//	{
//		result = fake = last_real = now;
//	}
//	else
//	{
//		result = fake + m_s_iSpeedTimes * (now - last_real);
//		fake = result;
//		last_real = now;
//	}
//
//	return result;
//}
//
//BOOL WINAPI NewQueryPerformanceCounter(__out LARGE_INTEGER* lpPerformanceCount)
//{
//	BOOL ret = ((zyc_QueryPerformanceCounter)(dwHookAddre))(lpPerformanceCount);
//	if (!ret) return ret;
//
//	static LARGE_INTEGER fake = { 0 };
//	static LARGE_INTEGER last_real = { 0 };
//	LARGE_INTEGER now = *lpPerformanceCount;
//
//	if (last_real.QuadPart == 0)
//	{
//		fake = last_real = now;
//	}
//	else
//	{
//		lpPerformanceCount->QuadPart = fake.QuadPart + m_s_iSpeedTimes * (now.QuadPart - last_real.QuadPart);
//		fake = *lpPerformanceCount;
//		last_real = now;
//	}
//
//	return ret;
//}
//
//
//DWORD _declspec(naked) NewFunction_QueryPerformanceCounter()
//{
//	_asm
//	{
//		call NewQueryPerformanceCounter
//	}
//}
//
//// timegettime
//VOID hook2()
//{
//	//页面属性备份
//	DWORD state = 0;
//
//	//HOOK函数的地址
//	g_dwTimeGetTimeaddr = (DWORD)GetProcAddress(GetModuleHandleA("Winmm.dll"), "timeGetTime");
//
//	//跳转代码
//	BYTE byJmpCode[PATCH_INLINE] = { 0xe9 };
//	*(DWORD*)&byJmpCode[1] = (DWORD)NewTimeGetTime - (DWORD)g_dwTimeGetTimeaddr - 5;
//
//	//开始HOOK
//	VirtualProtect((PVOID)g_dwTimeGetTimeaddr, PATCH_INLINE, PAGE_READWRITE, &state);
//	memcpy((PVOID)g_dwTimeGetTimeaddr, byJmpCode, PATCH_INLINE);
//	VirtualProtect((PVOID)g_dwTimeGetTimeaddr, PATCH_INLINE, state, &state);
//}
//
//VOID hook3()
//{
//	//页面属性备份
//	DWORD state = 0;
//
//	//HOOK函数的地址
//	g_dwGetTickCountaddr = (DWORD)GetProcAddress(GetModuleHandleA("Kernel32.dll"), "GetTickCount");
//
//	//跳转代码
//	BYTE byJmpCode[PATCH_INLINE] = { 0xe9 };
//	*(DWORD*)&byJmpCode[1] = (DWORD)NewGetTickCount - (DWORD)g_dwGetTickCountaddr - 5;
//
//	//开始HOOK
//	VirtualProtect((PVOID)g_dwGetTickCountaddr, PATCH_INLINE, PAGE_READWRITE, &state);
//	memcpy((PVOID)g_dwGetTickCountaddr, byJmpCode, PATCH_INLINE);
//	VirtualProtect((PVOID)g_dwGetTickCountaddr, PATCH_INLINE, state, &state);
//}