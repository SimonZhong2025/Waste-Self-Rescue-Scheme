
/************************************************************************
** 功  能:绘制任务图形
** 参  数:
**		stMe			自身信息
**		stTarget		目标信息
**		hDc				窗口设备句柄
**		dwWindwMetricsX	窗口分辨率X
**		dwWindwMetricsY	窗口分辨率Y
** 返回值:VOID
************************************************************************/
VOID ShowPaint(stPlayerInfo stMe, stPlayerInfo stTarget, HDC hDc, DWORD dwWindwMetricsX, DWORD dwWindwMetricsY)
{
	FLOAT dx = 0;
	FLOAT dy = 0;
	FLOAT dz = 0;
	//水平夹角
	FLOAT levelAngle = 0;
	//俯仰角
	FLOAT elevation = 0;
	//角色夹角
	FLOAT fPlayerAngle_xy = 0;
	FLOAT fPlayerAngle_z = 0;
	//屏幕夹角
	FLOAT fPaintAngle_xy = 0;
	FLOAT fPaintAngle_z = 0;

	//计算我和目标的相对偏移
	dx = stTarget.x - stMe.x;
	dy = stTarget.y - stMe.y;
	dz = stTarget.z - 50 - stMe.z;

	FLOAT fDistance = sqrt(dx * dx + dy * dy);

	levelAngle = stMe.zy;
	elevation = stMe.sx;
	//角度补偿  -180 180 =》0 360
	if (levelAngle < 0)
	{
		levelAngle = levelAngle + 360;
	}
	elevation = -elevation;

	//计算角色夹角
	if (dx > 0)
	{
		if (dy == 0)
		{
			fPlayerAngle_xy = 0.0;
		}
		else if (dy > 0)
		{
			fPlayerAngle_xy = asin(dy / fDistance) * 180 / 3.1416;
		}
		else if (dy < 0)
		{
			fPlayerAngle_xy = 360.0 + (asin(dy / fDistance) * 180 / 3.1416);
		}
	}
	//判断特殊角度
	else if (dx == 0)
	{
		if (dy > 0)
		{
			fPlayerAngle_xy = 90.0;
		}
		else if (dy < 0)
		{
			fPlayerAngle_xy = 270.0;
		}
	}
	else if (dx < 0)
	{
		if (dy == 0)
		{
			fPlayerAngle_xy = 180.0;
		}
		else if (dy > 0)
		{
			fPlayerAngle_xy = 180.0 - asin(dy / (fDistance)) * 180 / 3.1416;
		}
		else if (dy < 0)
		{
			fPlayerAngle_xy = 180.0 - asin(dy / (fDistance)) * 180 / 3.1416;
		}
	}

	//视角水平夹角
	fPaintAngle_xy = levelAngle - fPlayerAngle_xy;
	if (fPaintAngle_xy == 180.0 || fPaintAngle_xy == -180.0)
	{
		fPaintAngle_xy = 180.0;
	}
	else if (fPaintAngle_xy > 180.0)
	{
		fPaintAngle_xy = fPaintAngle_xy - 360.0;
	}
	else if (fPaintAngle_xy < -180.0)
	{
		fPaintAngle_xy = fPaintAngle_xy + 360.0;
	}

	//视角俯仰夹角
	fPlayerAngle_z = asin(dz / (sqrt(dx * dx + dy * dy + dz * dz))) * 180 / 3.1416;
	fPaintAngle_z = elevation - fPlayerAngle_z;

	if (fPaintAngle_xy > -45 && fPaintAngle_xy < 45 && fPaintAngle_z > -45 && fPaintAngle_z < 45)
	{
		DWORD dwLift_x;
		DWORD dwLeft_y;
		DWORD dwRight_x;
		DWORD dwRight_y;
		//屏幕坐标转换
		//FLOAT fPaintPoint = 640 * (sin(fPaintAngle_xy)*fDistance / cos(fPaintAngle_xy)*fDistance);
		FLOAT fPaintPoint = dwWindwMetricsX * (tan(fPaintAngle_xy * 3.14 / 180) + 1) / 2;
		DWORD dwWight = 100 * 100 / (100 + fDistance) + 10;

		dwLift_x = fPaintPoint - dwWight / 2;
		dwRight_x = fPaintPoint + dwWight / 2;

		//俯仰
		FLOAT fPaintSx = dwWindwMetricsY * (tan(53.0 * 3.14 / 180) * tan(fPaintAngle_z * 3.14 / 180) * 10 / 11 + 1) / 2;

		//DWORD dwHight = 100 * 512 / (100 + fDistance);
		DWORD dwHight = 100 * 300 / (fDistance);

		dwLeft_y = fPaintSx + dwHight * ((fPaintAngle_z) / 100);
		dwRight_y = fPaintSx - dwHight * (1 - (fPaintAngle_z) / 100);

		WCHAR wBuffer[20] = {0};
		memset(wBuffer, 0, 40);
		swprintf_s(wBuffer, L"HP:%03d", stTarget.dwHp);
		//显示血量
		HPEN hPen;
		HBRUSH hBrush;
		//显示阵营
		if (stTarget.dwCT == 3)
		{
			hPen = CreatePen(PS_SOLID, 1, RGB(0, 245, 255));
		}
		else if (stTarget.dwCT == 2)
		{
			hPen = CreatePen(PS_SOLID, 1, RGB(255, 255, 0));
		}
		//显示方框
		SelectObject(hDc, hPen);
		Rectangle(hDc, dwLift_x, dwLeft_y, dwRight_x, dwRight_y);
		DeleteObject(hPen);

		// //显示血条-血条颜色设置
		// if (stTarget.dwState == 50)
		// {
		// 	SetTextColor(hDc, RGB(105, 105, 105));
		// 	hPen = CreatePen(PS_SOLID, 1, RGB(105, 105, 105));
		// 	hBrush = (HBRUSH)CreateSolidBrush(RGB(105, 105, 105));
		// }
		// else if (stTarget.dwHp >= 80)
		// {
		// 	SetTextColor(hDc, RGB(0, 255, 0));
		// 	hPen = CreatePen(PS_SOLID, 1, RGB(0, 255, 0));
		// 	hBrush = (HBRUSH)CreateSolidBrush(RGB(0, 255, 0));
		// }
		// else if (stTarget.dwHp >= 60)
		// {
		// 	SetTextColor(hDc, RGB(255, 255, 0));
		// 	hPen = CreatePen(PS_SOLID, 1, RGB(255, 255, 0));
		// 	hBrush = (HBRUSH)CreateSolidBrush(RGB(255, 255, 0));
		// }
		// else if (stTarget.dwHp >= 40)
		// {
		// 	SetTextColor(hDc, RGB(255, 97, 0));
		// 	hPen = CreatePen(PS_SOLID, 1, RGB(255, 97, 0));
		// 	hBrush = (HBRUSH)CreateSolidBrush(RGB(255, 97, 0));
		// }
		// else
		// {
		// 	SetTextColor(hDc, RGB(255, 0, 0));
		// 	hPen = CreatePen(PS_SOLID, 1, RGB(255, 0, 0));
		// 	hBrush = (HBRUSH)CreateSolidBrush(RGB(255, 0, 0));
		// }
		// TextOutW(hDc, dwRight_x, dwRight_y, wBuffer, 6);

		// SelectObject(hDc, hPen);
		// Rectangle(hDc, dwLift_x, dwRight_y + 6, dwRight_x, dwRight_y);
		// DeleteObject(hPen);

		// HBRUSH hOldBrush = (HBRUSH)SelectObject(hDc, hBrush);

		// Rectangle(hDc, dwLift_x, dwRight_y + 6, dwLift_x + (dwRight_x - dwLift_x) * stTarget.dwHp / 100, dwRight_y);
		// SelectObject(hDc, hOldBrush);
		// DeleteObject(hOldBrush);
		// DeleteObject(hBrush);
		// //Rectangle(hDc, 0, 0, dwWindwMetricsX, dwWindwMetricsY);
	}
}
