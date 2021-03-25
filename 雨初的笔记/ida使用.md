+ `shift + f12` 可以查看字符串

+ `enter` 跳进去， `esc` 跳出来

+ `N` 重命名变量

+ `R` 将16进制转换为字符串

+ 一般来说

+ 按下空格可以从![image-20200826164322606](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200826164322606.png)

  这种界面切换到

  ![image-20200826164341789](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200826164341789.png)

  这种界面。

+ ACDU
  + A-字符串显示
  + C-识别成代码
  + D-数据，默认db,再按dw，再按dd
  + U-未定义，IDA会直接放16进制数字，不转换为任何东西

+ ![image-20200826165312104](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200826165312104.png)

  设置硬编码长度，最长16（硬编码最长16）

+ `G` 指令可以跳转到某一个地方（ **go** ）

+ `alt + T` 搜索

+ 按 `n` 进行重命名

+ `alt + Q` 可以选择结构体类型

+ 注释三种类型

  + 按分号 `;` 注释，所有往这个地方跳的代码都会显示这个注释的副本

    ![image-20200826170100077](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200826170100077.png)

  + 按 `:` 注释，往这个地方跳的代码不会显示这个注释的副本（按住shift + ;）

  + 针对函数的注释，按下分号 `;` 

    ![image-20200826170250615](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200826170250615.png)

    可以在函数上方注释函数的特征

+ ![image-20200826170343212](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200826170343212.png)

  交叉引用，可以列出所有使用这个函数的地方。
  
+ 在IDA里面的函数列表按 `ctrl + f` 可以按照函数名找函数。

+ IDA中按 `G` 可以跳转到需要的地址。

+ 在IDA中按 `\` 可以将一些有强转的地方简洁表示。

+ `shift + e` 可以把数据下载

+ 在汇编代码里面按 `/` 可以将C语言代码拷贝到汇编中。

+ `alt + t` 全文搜索。

+ 按 `t` 选择结构体偏移。

+ 结构体试图， `edit` ，添加结构体，可以添加 `standard structure` 。

  ![image-20210204133525746](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20210204133525746.png)

+ `alt + b` 可以打开二进制搜索界面。

