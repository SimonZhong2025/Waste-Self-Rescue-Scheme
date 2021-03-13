/************************************************************************
** 功  能:创建覆盖窗口
** 参  数:
**
** 返回值:出错返回0
************************************************************************/
RECT g_stRect;
RECT g_stKhRect;
HWND g_hWnd;
WindowsInfo g_stWindowsInfo = { 0 };
extern DWORD g_dwPid;
VOID CreateCoverWindow()
{
	//创建窗口
	WNDCLASSEX WINCLASS = { sizeof WNDCLASSEX };

	WINCLASS.cbSize = sizeof(WNDCLASSEX);
	WINCLASS.style = CS_HREDRAW | CS_VREDRAW;//改变则重绘 
	WINCLASS.lpfnWndProc = MyWindowProc;
	WINCLASS.hInstance = GetModuleHandle(0);
	WINCLASS.hCursor = LoadCursor(NULL, IDC_ARROW);
	WINCLASS.hbrBackground = (HBRUSH)RGB(0, 0, 0);
	WINCLASS.lpszClassName = L"CS-Cover";
	RegisterClassEx(&WINCLASS);

	//获取目标窗口
	HWND hCsWnd = YWHFindWindowsW(L"Counter-Strike Source");
	
	//获得窗口大小位置及(分辨率)
	GetWindowRect(hCsWnd, &g_stRect);
	GetClientRect(hCsWnd, &g_stKhRect);
	g_stKhRect.left = g_stRect.left;
	g_stKhRect.right = g_stRect.right;
	g_stKhRect.top = g_stRect.bottom - g_stKhRect.bottom;
	g_stKhRect.bottom = g_stRect.bottom;
	//获取窗口进程信息
	InitWindowsCS();
	//创建窗口 （分层窗口不绘制）
	g_hWnd = CreateWindowEx(WS_EX_LAYERED | WS_EX_TRANSPARENT, WINCLASS.lpszClassName, L"CS-Cover",
							WS_POPUP, g_stKhRect.left, g_stKhRect.top, g_stKhRect.right - g_stKhRect.left,
							g_stKhRect.bottom - g_stKhRect.top,NULL, NULL,WINCLASS.hInstance, NULL);


	//分层窗口透明度和颜色	筛选
	// SetLayeredWindowAttributes(g_hWnd, RGB(255,255,255), 0, LWA_COLORKEY);
	SetLayeredWindowAttributes(g_hWnd, 0, 255, LWA_ALPHA);

	ShowWindow(g_hWnd, SW_SHOW);

	//完全置顶
	SetWindowPos(g_hWnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE);

	CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)MainLoopThread, (PDWORD)&g_hWnd, 0, NULL);
	//消息循环
	MSG msg = { 0 };
	while (GetMessage(&msg, 0, 0, 0))
	{
		DispatchMessage(&msg);
	}
	CloseHandle(g_stWindowsInfo.hProcess);
	return ;
}


/************************************************************************
** 功  能:窗口回调函数
** 参  数:
**		
** 返回值:
************************************************************************/

LRESULT CALLBACK MyWindowProc(_In_ HWND hwnd, _In_ UINT uMsg, _In_ WPARAM wParam, _In_ LPARAM lParam)
{
	switch (uMsg)
	{
		case WM_PAINT:
		{
			//绘制目标人物
			HDC hDc = GetDC(g_hWnd);
			ShowPlayer(hDc, g_stWindowsInfo.hProcess, g_stWindowsInfo.dwBaseAddress,g_pPlayerBuffer, g_stKhRect.right- g_stKhRect.left, g_stKhRect.bottom- g_stKhRect.top);
			ReleaseDC(g_hWnd, hDc);
			break;
		}
		case WM_CREATE:
		{
			//区域拓展  
			MARGINS margin = { g_stKhRect.left, g_stKhRect.top, g_stKhRect.right, g_stKhRect.bottom };
			DwmExtendFrameIntoClientArea(hwnd, &margin);
			break;
		}
		case WM_CLOSE:
		{
			PostQuitMessage(0);
			break;
		}
			
	}
	return DefWindowProc(hwnd, uMsg, wParam, lParam);
}


/************************************************************************
** 功  能:重绘窗口
** 参  数:
**
** 返回值:
************************************************************************/
void MainLoopThread()
{
	while (TRUE)
	{
		//获取DC上下文
		HDC hDc = GetDC(g_hWnd);						

		//创建画刷并关联至上下文
		HBRUSH HbRUSH = CreateSolidBrush(RGB(255, 255, 255));
		HBRUSH hOldBrush = (HBRUSH)SelectObject(hDc, HbRUSH);
		//根据窗口重新绘制矩形
		Rectangle(hDc, 0, 0, g_stKhRect.right - g_stKhRect.left, g_stKhRect.bottom - g_stKhRect.top);

		HANDLE hMutex = CreateMutex(NULL, FALSE, TEXT("数据轮询"));
		SendMessage(g_hWnd, WM_PAINT, NULL, NULL);
		ReleaseMutex(hMutex);
		Sleep(50);
		SelectObject(hDc, hOldBrush);
		//清理句柄
		DeleteObject(HbRUSH);
		DeleteObject(hOldBrush);
		ReleaseDC(g_hWnd, hDc);
	}
}


/************************************************************************
** 功  能:初始化窗口信息
** 参  数:
**		
** 返回值:VOID
************************************************************************/
VOID InitWindowsCS()
{
	//模块基址获取  打开目标进程
	DWORD dwPid = YWHFindProcessW(L"hl2.exe");
	g_stWindowsInfo.hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, dwPid);
	if (g_stWindowsInfo.hProcess == NULL)
	{
		MessageBoxW(NULL,L"请以管理员身份重新运行程序!",NULL,NULL);
	}
	//遍历查找连接模块
	MODULEENTRY32 ModuInfo = { 0 };
	ModuInfo.dwSize = sizeof MODULEENTRY32;
	if (YWHGetModuleW(dwPid, L"client.dll", &ModuInfo) == 0)
	{
		CloseHandle(g_stWindowsInfo.hProcess);
		return;
	}
	g_stWindowsInfo.dwBaseAddress = (DWORD)ModuInfo.modBaseAddr;

	//找到游戏窗口并获取窗口
	g_stWindowsInfo.hCsWnd = YWHFindWindowsW(L"Counter-Strike Source");

	//获得窗口客户区大小位置及(分辨率)
	GetClientRect(g_stWindowsInfo.hCsWnd, &g_stWindowsInfo.stRect);
}

