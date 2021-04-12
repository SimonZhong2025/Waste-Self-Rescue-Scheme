### trie

+ 例题

  >维护一个字符串集合，支持两种操作：
  >
  >1. “I x”向集合中插入一个字符串x；
  >2. “Q x”询问一个字符串在集合中出现了多少次。
  >
  >共有N个操作，输入的字符串总长度不超过 ![image-20201227225932982](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201227225932982.png)，字符串仅包含小写英文字母。
  >
  >#### 输入格式
  >
  >第一行包含整数N，表示操作数。
  >
  >接下来N行，每行包含一个操作指令，指令为”I x”或”Q x”中的一种。
  >
  >#### 输出格式
  >
  >对于每个询问指令”Q x”，都要输出一个整数作为结果，表示x在集合中出现的次数。
  >
  >每个结果占一行。
  >
  >#### 数据范围
  >
  >![image-20201227225924075](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201227225924075.png)
  >
  >![image-20201227230033970](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201227230033970.png)

+ `trie` 树用来快速存储字符串集合
+ 高效查找某个字符串是否出现过以及出现多少次
+ 只有26个字母，每个点最多向外连26条边。
+ Trie这个术语来自于re**trie**val。根据[词源学](https://zh.wikipedia.org/wiki/词源学)，trie的发明者Edward Fredkin把它读作[/ˈtriː/](https://zh.wikipedia.org/wiki/Help:英語國際音標) "tree"。[[1\]](https://zh.wikipedia.org/wiki/Trie#cite_note-DADS-1)[[2\]](https://zh.wikipedia.org/wiki/Trie#cite_note-Liang1983-2)但是，其他作者把它读作[/ˈtraɪ/](https://zh.wikipedia.org/wiki/Help:英語國際音標) "try"。[[1\]](https://zh.wikipedia.org/wiki/Trie#cite_note-DADS-1)[[2\]](https://zh.wikipedia.org/wiki/Trie#cite_note-Liang1983-2)[[3\]](https://zh.wikipedia.org/wiki/Trie#cite_note-KnuthVol3-3)

+ `trie` 树的根节点是一个空结点，所以存储的时候要使用 `++ idx` 而不是 `idx ++ ` 

  ![image-20201111090407477](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201111090407477.png)

+ 因为一个字符串的末尾是 `\0` ，所以可以这样遍历字符串

  ```cpp
  for (int i = 0; str[i]; i ++ )
  ```

+ 代码如下

  ```cpp
  #include <iostream>
  #include <stdio.h>
  #include <string.h>
  #include <algorithm>
  
  using namespace std;
  
  const int N = 20010;
  
  char str[100010];
  
  // son[p][u]表示u这个点下一个字母是u + 'a'的子节点的下标
  int son[N][26 + 1], cnt[N], idx; // 下标是0的点既是根节点又是空结点
  
  void insert()
  {
      // p用来存下一个探索的节点的下标。
      int p = 0;
      for (int i = 0; str[i]; i ++ )
      {
          int u = str[i] - 'a';
          if (!son[p][u]) son[p][u] = ++ idx;
          p = son[p][u];
      }
      cnt[p] ++ ;
  }
  
  int query()
  {
      int p = 0;
      for (int i = 0; str[i]; i ++ )
      {
          int u = str[i] - 'a';
          if (!son[p][u]) return 0;
          p = son[p][u];
  }
      return cnt[p];
  }
  
  int main()
  {
      int T;
      cin >> T;
      while (T -- )
      {
          char op[2];
          cin >> op >> str;
          if (*op == 'I') insert();
          else cout << query() << endl;
      }
    
      return 0;
  }
  ```



### KMP字符串

+ 例题

  >给定一个模式串S，以及一个模板串P，所有字符串中只包含大小写英文字母以及阿拉伯数字。
  >
  >模板串P在模式串S中多次作为子串出现。
  >
  >求出模板串P在模式串S中所有出现的位置的起始下标。
  >
  >#### 输入格式
  >
  >第一行输入整数N，表示字符串P的长度。
  >
  >第二行输入字符串P。
  >
  >第三行输入整数M，表示字符串S的长度。
  >
  >第四行输入字符串S。
  >
  >#### 输出格式
  >
  >共一行，输出所有出现位置的起始下标（下标从0开始计数），整数之间用空格隔开。
  >
  >#### 数据范围
  >
  >![image-20201227230122398](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201227230122398.png)
  >
  >![image-20201227230129544](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201227230129544.png)

![image-20201227103915196](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201227103915196.png)

+ `next[i] = j` 的含义是模式字符串中 `p[1, j]` 和 `p[i - j + 1, i]` 是相等的。也就是 **第一个字符到第j的字符** 组成的字符串和 **第i - j + 1到第i的字符是相等的** 。

+ `next` 在某个头文件里面有，所以在写代码的时候起名为 `ne` 才能万无一失。

  ![image-20201029190320145](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201029190320145.png)

  ![image-20201227103703695](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201227103703695.png)

+ `while (j && s[i] != p[j + 1]) j = ne[j];` 直到匹配或者退无可退为止

+ 代码如下

  ```scpp
  #include <iostream>
  
  using namespace std;
  
  const int N = 100010, M = 1000010;
  
  char p[N], s[M];
  int n, m;
  int ne[N];
  
  int main()
  {
     cin >> n >> p + 1 >> m >> s + 1;
     
     for (int i = 2, j = 0; i <= n; i ++ )
     {
         while (j && p[j + 1] != p[i]) j = ne[j];
         if (p[j + 1] == p[i]) j ++ ;
         ne[i] = j;
     }
     
     for (int i = 1, j = 0; i <= m; i ++ )
     {
         while (j && p[j + 1] != s[i]) j = ne[j];
         if (p[j + 1] == s[i]) j ++ ;
         if (j == n)
         {
             // 匹配成功
             printf("%d ", i - n); // 减去模式字符串的长度等于起点
             j = ne[j];
         }
     }
     
     return 0;
  }
  ```



+ ![image-20201228080016598](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201228080016598.png)

  做的过程中要用到的工具、过程等

+ 译后编辑

  ![image-20201228080149025](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201228080149025.png)

  ```
  ①______________()
  ```

  一个合理的点2~3分

+ 英翻中

  ![image-20201228080511861](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201228080511861.png)

  考试结束前20分钟会收到机器翻译的译文。