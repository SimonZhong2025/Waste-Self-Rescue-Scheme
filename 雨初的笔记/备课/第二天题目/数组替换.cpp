#include <stdio.h>

int main()
{
   int a[10];
   for (int i = 0; i < 10; i ++ ) scanf("%d", &a[i]);
   for (int i = 0; i < 10; i ++ )
      if (a[i] <= 0)
         a[i] = 1;
   for (int i = 0; i < 10; i ++ )
   {
      printf("X[%d] = %d\n", i, a[i]);
   }
   return 0;
}