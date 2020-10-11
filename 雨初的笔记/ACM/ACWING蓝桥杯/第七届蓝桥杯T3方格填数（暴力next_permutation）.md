+ 答案1580

  ```cpp
  #include<iostream>
  #include<cstdio>
  #include<cstdlib>
  #include<cstring>
  #include<cmath>
  #include <set>
  #include<algorithm>
  using namespace std;
  
  int a[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  
  bool check(int x, int y)
  {
  	if (abs(a[x] - a[y]) == 1) return true;
  	return false;
  }
  
  int main()
  {
  	freopen("f:\\out.txt", "w", stdout);
  	int res = 0;
  	do {
  		if (check(0, 1)) continue;
  		if (check(1, 2)) continue;
  		if (check(0, 3)) continue;
  		if (check(3, 4)) continue;
  		if (check(5, 6)) continue;
  		if (check(8, 9)) continue;
  		if (check(4, 5)) continue;
  		if (check(7, 8)) continue;
  		if (check(0, 4)) continue;
  		if (check(1, 5)) continue;
  		if (check(2, 6)) continue;
  		if (check(3, 7)) continue;
  		if (check(4, 8)) continue;
  		if (check(5, 9)) continue;
  		if (check(1, 4)) continue;
  		if (check(2, 5)) continue;
  		if (check(0, 5)) continue;
  		if (check(1, 4)) continue;
  		if (check(1, 6)) continue;
  		if (check(2, 5)) continue;
  		if (check(3, 8)) continue;
  		if (check(4, 7)) continue;
  		if (check(4, 9)) continue;
  		if (check(5, 8)) continue;
  		if (check(6, 9)) continue;
  		
  				
  		for (int i = 0; i < 9; i ++ ) printf("%d ", a[i]);
  		puts("");
  		res ++ ;
  			
  	} while (next_permutation(a, a + 10));
  	
  	cout << res << endl;
  }
  ```

  