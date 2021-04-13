+ 迷宫图如下

  ```cpp
  __________ooooo_____o________o_
  ooooooooo__ooo__ooo_oooooooooo_
  oooooooooo__o__oooo_oooooooooo_
  _______oooo___ooooo_ooooooooooo
  oooooo_oooooooooooo_ooooooooooo
  oooooo_ooooo_oooooo_ooooooooooo
  oooooo_ooooo_oooooo_oooooooooos
  _______ooooo_oooooo__________Eo
  ```

  ```cpp
  #include <stdio.h>
  #include <stdlib.h>
  #include <string.h>
  
  int main()
  {
      char r[] = "DDDDDDDDDDSDSDSDDWDWDWDDDDSSSSSSSDDDDDDDDD";
      int len = strlen(r);
      printf("len = %d\n", len);
      for (int i = 0; i < len; i ++ )
      {
          printf("%c", r[i] - 'A' + 'a');
      }
  }
  ```

  ```cpp
  #include <stdio.h>
  #include <stdlib.h>
  #include <string.h>
  char maze[20][20];
  
  void print()
  {
      for (int i = 0; i < 8; i ++ )
      {
          for (int j = 0; j < 31; j ++ )
              printf("%c", maze[i][j]);
          puts("");
      }
      puts("\n");
  }
  
  int main(void)
  {
      strcpy(maze[0], "__________ooooo_____o________o_");
      strcpy(maze[1], "ooooooooo__ooo__ooo_oooooooooo_");
      strcpy(maze[2], "oooooooooo__o__oooo_oooooooooo_");
      strcpy(maze[3], "_______oooo___ooooo_ooooooooooo");
      strcpy(maze[4], "oooooo_oooooooooooo_ooooooooooo");
      strcpy(maze[5], "oooooo_ooooo_oooooo_ooooooooooo");
      strcpy(maze[6], "oooooo_ooooo_oooooo_oooooooooos");
      strcpy(maze[7], "_______ooooo_oooooo__________Eo");
  
      // char r[] = "DDDDDDDDDDSDSDSDDWDWDWDDDDSSSSSSSDDDDDDDDD";
      char r[] = "DDDDDDDDDSDSDSDDWDWDWDDDDSSSSSSSDDDDDDDDD";
      int posx = 0, posy = 0;
      int len = strlen(r);
      for (int i = 0; i < len; i++)
      {
          if (r[i] == 'D')
              posy++;
          if (r[i] == 'S')
              posx++;
          if (r[i] == 'A')
              posy--;
          if (r[i] == 'W')
              posx--;  
          if (maze[posx][posy] != '_')
          {
              print();
              printf("posx = %d, posy = %d\n", posx, posy);
              exit(0);
          }
          maze[posx][posy] = '+';
          print();
      }
      print();
  }
  ```

  ![image-20201022102517088](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201022102517088.png)

  做不出来，看汇编代码的能力还是要加强。