+ 这道题和ACWING上BFS例题“八数码”很像，要用深搜

+ 答案是20

  ```cpp
  #include <iostream>
  #include <stdio.h>
  #include <string.h>
  #include <stdlib.h>
  #include <string>
  #include <vector>
  #include <algorithm>
  #include <queue>
  #include <map>
  #include <unordered_map>
  
  using namespace std;
  
  typedef pair<int, int> pii;
  typedef long long ll;
  #define xx first
  #define yy second
  const int N = 110;
  char a[N][N];
  
  int dx[] = {0, 0, 1, -1}, dy[] = {1, -1, 0, 0};
  int mov[] = {1, -1, 2, -2};
  
  string des = "87654321x";
  int maxdis = 0;
  
  int bfs(string origin)
  {
  	queue<string> q;
  	q.push(origin);
  	unordered_map<string, int> d;
  	while (q.size())
  	{
  		string t = q.front();
  		q.pop();
  		int distance = d[t];
  		if (t == des) 
  		{
  			freopen("CON", "w", stdout);
  			return distance;
  		}
  		int pos = t.find('x');
  		for (int i = 0; i < 4; i ++ )
  		{
  			int tpos = pos + mov[i];
  			if (tpos == -1) tpos = 8;
  			else if (tpos == -2) tpos = 7;
  			else if (tpos == 9) tpos = 0;
  			else if (tpos == 10) tpos = 1;
  			
  			swap(t[pos], t[tpos]);
  			
  			if (d.count(t) == 0)
  			{
  				cout << t << " " << distance + 1 << endl;
  				q.push(t);
  				d[t] = distance + 1;
  			}			
  
  			swap(t[pos], t[tpos]);
  		}
  	}
  }
  
  int main()
  {
  	freopen("f:\\out.txt", "w", stdout);
  	string origin = "12345678x";
  	cout << bfs(origin) << endl;
  	return 0;
  }
  ```

  