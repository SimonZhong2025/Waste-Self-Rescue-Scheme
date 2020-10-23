```cpp
#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    FILE* fp = NULL;
    char buf[1024] = {'\0'};
    fp = popen("cat /home/ctf/flag", "r");
    fgets(buf, 1024, fp);
    printf("buf: %s\n", buf);

    pclose(fp);

    return 0;
}
```

