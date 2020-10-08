+ 看到 **最短路径** 这类字眼要马上想到使用 `BFS` 。

+ 这道题的解法中有个巧妙的地方是一维数组中的下标到二维数组中的下标的转换。

  ```cpp
  int 一维数组下标 = 二维数组X坐标 * 二维数组列数 + 二维数组Y坐标
  ```

+ 用 `unordered_map` 来存储每一种情况需要的 `distance` 。如果这种情况已经计算过了 （ `d.count() != 0` ）那么跳过这种情况。

+ 第八届蓝桥杯省赛A组第二题 **跳蚱蜢** 和这题也很像，题目放在最后，也可以搭配来看看

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
  string des = "12345678x";
  
  int dx[] = {0, 0, 1, -1}, dy[] = {1, -1, 0, 0};
  
  int bfs(string origin)
  {
  	queue<string> q;
  	unordered_map<string, int> d;
  	q.push(origin);
  	while (q.size())
  	{
  		string t = q.front();
  		q.pop();
  		
  		int distance = d[t];
  		if (t == des) return distance; // 如果找到了则直接返回
  		
  		int pos = t.find('x'); // 得到下标
  		int x = pos / 3;
  		int y = pos % 3;
  		for (int i = 0; i < 4; i ++ )
  		{
  			int tx = x + dx[i];
  			int ty = y + dy[i];
  			if (ty >= 0 && tx >= 0 && tx < 3 && ty < 3)
  			{
  				int realpos = tx * 3 + ty;
  				swap(t[realpos], t[pos]);
  				
  				if (!d.count(t))
  				{
  					d[t] = distance + 1;
  					q.push(t);
  				}
  				
  				swap(t[realpos], t[pos]);
  			}
  		} 
  	}
  	return -1;
  }
  
  int main()
  {
  	string origin = "";
  	char t[2];
  	for (int i = 0; i < 9; i ++ )
  	{
  		cin >> t;
  		origin += t[0];
  	}
  	cout << bfs(origin) << endl;
  	return 0;
  }
  ```

+ 附《跳蚱蜢》原题

  >标题：跳蚱蜢
  >
  >如图 p1.png 所示： 
  >有9只盘子，排成1个圆圈。
  >其中8只盘子内装着8只蚱蜢，有一个是空盘。
  >我们把这些蚱蜢顺时针编号为 1~8
  >
  >每只蚱蜢都可以跳到相邻的空盘中，
  >也可以再用点力，越过一个相邻的蚱蜢跳到空盘中。
  >
  >请你计算一下，如果要使得蚱蜢们的队形改为按照逆时针排列，
  >并且保持空盘的位置不变（也就是1-8换位，2-7换位,...），至少要经过多少次跳跃？
  >
  >注意：要求提交的是一个整数，请不要填写任何多余内容或说明文字。

  ![image-20201008105832210](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20201008105832210.png)

  > 答案是20