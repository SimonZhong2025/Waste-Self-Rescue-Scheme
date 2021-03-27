### aheadlib

1. 首先去掉VS中要求的预编译头

   ![image-20210326203201446](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master/image-20210326203201446.png)

2. 然后要改成多字节字符集的

   ![image-20210326203240306](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master/image-20210326203240306.png)

3. 可以改动拓展名，如果要劫持 `winspool.drv`

   ![image-20210326203449140](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master/image-20210326203449140.png)

4. 在win10系统里面因为32位的dll在 `syswow64` 里面，而 `system32` 里面都是64位的dll，因此aheadlib使用的取系统dll目录的方法是错误的。如果想要在win10下用这个，需要手动进行修改。

   ![image-20210326203740536](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master/image-20210326203740536.png)

   可以改为这个

   ![image-20210326204235599](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master/image-20210326204235599.png)

   其中 `IsWow64Process` 函数的返回值只是指示这个函数是否执行成功，真正的返回值放在第二个参数那个变量的地址里面。

5. 调试dll的时候要把exe路径加上

   ![image-20210326203953398](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master/image-20210326203953398.png)



