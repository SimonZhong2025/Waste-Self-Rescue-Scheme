+ 这道题考察伪随机数

  ```cpp
  #include <stdio.h>
  
  int main(){
          unsigned int random;
          random = rand();        // random value!
  
          unsigned int key=0;
          scanf("%d", &key);
  
          if( (key ^ random) == 0xdeadbeef ){
                  printf("Good!\n");
                  system("/bin/cat flag");
                  return 0;
          }
  
          printf("Wrong, maybe you should try 2^32 cases.\n");
          return 0;
  }
  ```

  因为每次 `rand()` 生成的都是一样的随机数，所以只要用 `gdb` 调一次就可以知道生成的随机数是多少

  ![image-20201024160803633](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201024160803633.png)

  ![image-20201024160812917](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201024160812917.png)

  ![image-20201024160828134](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201024160828134.png)

  ![image-20201024160843390](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201024160843390.png)

  ![image-20201024160949724](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201024160949724.png)