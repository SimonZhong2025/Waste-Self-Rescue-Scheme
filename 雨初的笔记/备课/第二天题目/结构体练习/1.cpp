#include <stdio.h>
#include <string.h>

struct People
{
	int grade;
	char name[30];
} peoples[30];

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i ++ )
    	scanf("%s%d", peoples[i].name, &peoples[i].grade);
   	char des[30];
	scanf("%s", des);
	for (int i = 0; i < n; i ++ )
		if (!strcmp(des, peoples[i].name))
			printf("%d\n", peoples[i].grade);
	return 0;
}