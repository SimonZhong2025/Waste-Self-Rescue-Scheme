```cpp
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

#include <iostream>
using namespace std;
int main()
{
    char a[] = {0x66, 0x0A, 0x6B, 0X0C, 0X77, 0X26, 0X4F, 0X2E, 0X40,
                0X11, 0X78, 0X0D, 0X5A, 0X3B, 0X55, 0X11, 0X70, 0X19,
                0X46, 0X1F, 0X76, 0X22, 0X4D, 0X23, 0X44, 0X0E, 0X67,
                0X6,  0X68, 0X0F, 0X47, 0x32, 0x4f};

    char b[0x200];
    memset(b, 0, sizeof(b));

    b[0] = 'f';
    for (int i = 1; i < 33; i ++ )
    {
        b[i] = a[i] ^ a[i - 1];
    }
    cout << b;
}
```

