+ `memset` 会将一个字节的元素设置为目标值，如果 `ch = 1` ，那么每一个字节都被设置为 `01` ，那为什么对一个 `bool` 数组用 `memset` 设置为1的时候所有元素都被设置为1呢

  ```cpp
  int main()
  {
      bool a[10][10];
      memset(a, 1, sizeof(a));
      for (int i = 0; i < 10; i++)
      {
          for (int j = 0; j < 10; j++)
              printf("%d ", a[i][j]);
          puts("");
      }
  }
  ```

  + 因为一个 `bool` 的大小是一个 `BYTE` 。

+ 为什么给一个 `bool` 赋其他值最后这个数组里面的值仍然是 `00000001` ？