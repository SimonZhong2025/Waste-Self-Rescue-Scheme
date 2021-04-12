#include <stdio.h>

#include <iostream>

using namespace std;

int main()
{
    int ct = 0;
    for (int i = 0; i <= 20; i++)
        for (int j = 0; j <= 33; j++)
            for (int k = 0; k <= 300; k += 3)
                if (i * 5 + j * 3 + k / 3 == 100)
                {
                    printf("%d %d %d\n", i, j, k);
                    ct ++ ;
                }
    cout << ct << endl;
}