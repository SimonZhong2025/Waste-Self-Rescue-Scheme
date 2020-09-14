+ ```python
  #coding:utf-8
  ```

  将编码设置为 **utf-8**

+ `penup` 可以将画笔抬起，然后将画笔移动到相应的位置

  `pendown` 可以将画笔落下，继续画图

+ `circle` 的第一个参数所要画的圆的半径，第二个参数是这个圆的圆周角，如果未指定第二个参数则默认360°，即将整个圆画出来。而如果指定了，比如 `circle(1, 180)` 这样会画出一个半圆

+ `fillcolor` 可以设定需要填充的颜色。如果没有传入参数 `fillcolor()` 则会返回描述颜色的字符串或者一个包含填充颜色 **RGB** 的tuple

+ `seth` 是 **to_angle** 的意思，用来设置海龟的朝向

  | 标准模式 | logo 模式 |
  | :------- | :-------- |
  | 0 - 东   | 0 - 北    |
  | 90 - 北  | 90 - 东   |
  | 180 - 西 | 180 - 南  |
  | 270 - 南 | 270 - 西  |

```py
>>> turtle.setheading(90)
>>> turtle.heading()
90.0
```

标准模式下 `seth(0)` 之后海龟的方向会指向右边，如图

![image-20200907112844563](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200907112844563.png)

+ `fd` 向海龟的朝向前进一个指定的距离
+ `lt` 左转 **angle** 个单位，单位默认是角度。（我觉得lt应该是left turn的意思）



## day2

+ 变量内存储的值改变了则其 `id()` 也改变，指向的地址不同。如果两个变量的值是一样的，则其 `id()` 获取的值也是一样的。
+ `python` 字符串可以进行乘法
+  `ecillpse` 有bug，输入中文要在后面点一下才能输入
+ `列表.index()` 方法返回这个元素在列表中的下标
+ `列表.count('元素')` 可以得到这个列表里面有多少个相同的元素
+ 创建一个空集合必须用 `set()` ，而不是 `{}` ，因为 `{}` 是用来创建空字典的。

## day3

+ 设置查找字典的默认值

  ![image-20200909143924376](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200909143924376.png)
  
+ `字典.get(键, 默认值)` 如果没有找到这个键，则返回默认值

## day4

![](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/20200910105155.png)

+ `math.pi` 是圆周率
+ `%f` 默认%后6位
+ ![image-20200910144957525](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200910144957525.png)

+ 判断字段是否为全英文 `字符串.isalpha()` ，转大写 `字符串.upper()`
+ `time.localtime()` 可以得到一个 `struct_time` 元组
+ `time.mktime(struct_time元组)` 可以得到一个时间戳 () 
+ `time.sleep()` 可以睡眠
+ 使用 `datetime.timedelta()` 用来前后移动时间
+ ![image-20200910161343727](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200910161343727.png)

## day5

+ 定向捕获异常之后还可以通过 `except:` 来捕获未知的错误。

+ 如果使用 `else` 必须放在所有 `except` 之后，如果没有错误发生那么 `else` 中的代码会被执行

+ ```python
  import traceback
  try:
      ...
  except () as e:
      traceback.print_exc()
      print(e)
  ```

+ 记录程序运行时间

  ```python
  print((time2 - time1).totalseconds())
  ```

+ ![image-20200911110437781](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200911110437781.png)

+ `r` 只读，只能打开已存在的文件，指针在开头

+ 使用 `fp.seek()` 的时候只有在打开模式中有 `b` 的时候才能将第二个参数设置为 `0` 之外的值。

+ `f.runcate(path, length)` 可以截断 `path` 对应的文件，使其最大为 `length` 字节。如果不指定 `length` 则从文件指针

+ ![image-20200912135700854](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200912135700854.png)

## day6

+ 可以通过 `._类名__私有变量名` 访问私有变量