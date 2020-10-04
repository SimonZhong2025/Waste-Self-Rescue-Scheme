```cpp
#include <math.h>
#include <stdio.h>
#include <string.h>

#include <algorithm>
#include <climits>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

const int N = 10010;
typedef long long ll;
priority_queue<long long, vector<long long>, greater<long long>> q;

int main()
{
    int n;
    cin >> n;
    while (n--)
    {
        long long t;
        cin >> t;
        q.push(t);
    }
    ll res = 0;
    while (q.size() > 1)
    {
        ll t1, t2;
        t1 = q.top();
        q.pop();
        t2 = q.top();
        q.pop();
        res += t1 + t2;
        q.push(t1 + t2);
    }
    cout << res << endl;
    return 0;
}
```



