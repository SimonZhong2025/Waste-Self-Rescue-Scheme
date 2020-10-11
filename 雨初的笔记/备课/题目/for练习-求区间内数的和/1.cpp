#include <stdio.h>

int main()
{
    int a, b;
    scanf("%d%d", &a, &b);
    int res = 0;
    for (int i = a; i <= b; i ++ )
    {
        res += i;
    }
    printf("%d", res);
}