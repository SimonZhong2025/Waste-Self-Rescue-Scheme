参考链接：https://www.acwing.com/solution/content/15937/

## 爆搜方法（无任何优化）（TLE）

```cpp
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <unordered_set>
#include <set>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
 
const int N = 100010;

int a[N], tmp[N];

int n, m;
int ans = 0;

void dfs(int x, int y)
{
	if (x % 2 == 0 && y % 2 == 0) return;
	if (x > n || y > m) return;
	if (x == n && y == m)
	{
		ans ++ ;
		return;
	}
	dfs(x + 1, y);
	dfs(x, y + 1);
}

int main()
{
	cin >> n >> m;
	dfs(1, 1);
	cout << ans << endl;
	return 0;
}
```

## 记忆化搜索

+ 对于DFS来说，单纯的爆搜会超时，那么我们在搜过一个点之后将其标记，这样就不会重复走过路线。如果重新搜到了这个点，而这个点已经在前面进行过搜索，已经得到了这个点到 `(n, m)` 共有多少条道路，那么就直接 `return f[x][y]` 就可以，这样就节省很多重复的搜索过程。

  

## 使用dp

+ 因为边上的路只能有一条，所以先把 `f[1][j]` 和 `f[i][1]` 全部设置为1，然后对于每一个格子，其状态转移方程都是 `f[i][j] = f[i - 1][j] + f[i][j - 1]` 。（当然对于两个都是偶数的格子要特判。）这样就可以递推到终点。最终得到的值就是 `f[n][m]` 的值。

  ```cpp
  #include <stdio.h>
  #include <iostream>
  
  using namespace std;
  typedef long long ll;
   
  const int N = 40;
  
  int a[N], tmp[N];
  
  int n, m;
  int ans = 0;
  
  int f[N][N];
  
  int main()
  {
  	cin >> n >> m;
  	if (n % 2 == 0 && m % 2 == 0)
  	{
  		cout << 0;
  		return 0;
  	}
  	for (int i = 1; i <= n; i ++ ) f[i][1] = 1;
  	for (int i = 1; i <= m; i ++ ) f[1][i] = 1;
  	for (int i = 2; i <= n; i ++ )
  		for (int j = 2; j <= m; j ++ )
  		{
  			if (i % 2 == 0 && j % 2 == 0) continue;
  			f[i][j] = f[i - 1][j] + f[i][j - 1];
  		}
  	cout << f[n][m];
  	return 0;
  }
  ```

  