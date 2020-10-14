#include <stdio.h>
#include <string.h>

int main()
{
   char a[110];
   scanf("%s", a);
   int len = strlen(a);

   printf("%d\n", len);
   for (int i = 0; i < len; i ++ )
      printf("%d\n", a[i] - 'a' + 1);
   
   return 0;
}



while练习1
http://oj.ncutea.com:2080/problem/lanqiao-1220
while练习2
http://oj.ncutea.com:2080/problem/lanqiao-1246

for练习1
http://oj.ncutea.com:2080/problem/994
for练习2
http://oj.ncutea.com:2080/problem/1000