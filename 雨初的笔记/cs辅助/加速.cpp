BOOL WINAPI NewQueryPerformanceCounter(__out LARGE_INTEGER *lpPerformanceCount)
{
	BOOL ret = poldQueryPerformanceCounter(lpPerformanceCount);
	
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
		lpPerformanceCount->QuadPart = fake.QuadPart + Speed * (now.QuadPart - last_real.QuadPart);
		fake = *lpPerformanceCount;
		last_real = now;
	}
	return ret;
}