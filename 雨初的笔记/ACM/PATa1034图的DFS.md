```cpp
#include <math.h>
#include <stdio.h>
#include <string.h>

#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <vector>
using namespace std;

const int N = 10010;
typedef long long ll;

int n, k;
int numPerson = 0;  // 用来记录总人数
map<string, int> m;
int G[N][N];
bool vis[N] = {false};
map<string, int> stringToInt;
map<int, string> intToString;
map<string, int> Gang;  // 用来存储结果，老大->总值
int weight[N];

int change(string str)
{
    // 如果有这个数
    if (stringToInt.find(str) != stringToInt.end())
        return stringToInt[str];
    else
    {
        stringToInt[str] = numPerson;
        intToString[numPerson] = str;
        return numPerson++;
    }
}

void DFS(int nowVisit, int& total, int& boss, int& personct)
{
    vis[nowVisit] = true;
    personct++;
    if (weight[nowVisit] > weight[boss])
        boss = nowVisit;
    for (int i = 0; i < numPerson; i++)
        if (G[nowVisit][i] != 0)
        {
            total += G[nowVisit][i];
            G[nowVisit][i] = G[i][nowVisit] = 0;
            if (!vis[i])
                DFS(i, total, boss, personct);
        }
}

void DFSTrave()
{
    for (int i = 0; i < numPerson; i++)
        if (!vis[i])
        {
            int boss = i;      // boss
            int total = 0;     // 边权总和
            int personct = 0;  // 这个帮派有多少人
            DFS(i, total, boss, personct);
            if (personct > 2 && total > k)
                Gang[intToString[boss]] = personct;
        }
}

int main()
{
    cin >> n >> k;
    // printf("k = %d\n", k);
    for (int i = 0; i < n; i++)
    {
        string s1, s2;
        int time;
        cin >> s1 >> s2 >> time;
        int id1 = change(s1);
        int id2 = change(s2);
        G[id1][id2] += time;
        G[id2][id1] += time;
        weight[id1] += time;
        weight[id2] += time;
    }
    DFSTrave();
    cout << Gang.size() << endl;
    map<string, int>::iterator it = Gang.begin();
    for (; it != Gang.end(); it++)
        cout << it->first << " " << it->second << endl;
    return 0;
}
```

