```
#PythonDraw.py 蟒蛇绘制图形是一切图形绘制的基础
import turtle
turtle.setup(650, 350, 200, 200)
turtle.penup() #别名turtle.pu()
turtle.fd(-250) #别名turtle.forward()
turtle.pendown() #别名turtle.pd()
turtle.pensize(25) #别名turtle.width()
turtle.pencolor("purple")
turtle.seth(-40) #向👉转
for i in range(4)
    turtle.circle(40, 80) #r是半径，angle是角度。半径为负数，则圆心在海🐢右侧的地方。若无angle，则时画一个圆
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done() #如果想自己关闭窗口则用这个函数，如果需要窗口自动关闭，则不需要这个语句
```
> 举一反三，七彩🐍，五角星等等东西

#### 标准库

python计算生态 = 标准库 + 第三方库

> 第三方库是需要经过安装才能使用的功能模块。我们经常用到库`Library`、包`Package`、模块`Module`，初学阶段统称为**模块**

![]()

#### turtle的绘图窗体

`turtle.setup(width, height, startx, starty)`

setup()设置窗体大小及位置，后两个参数可选。setup()并非必须的。如果没有设定位置，系统会默认窗体在屏幕的正中心。

#### turtle空间坐标体系

绝对坐标和屏幕空间坐标不同

###### 绝对坐标

中心为(0, 0)，可以用`turtle.goto(x, y)`来实现直线的一个绘制

###### 海🐢方向

右边为海右边为海🐢的前方
```
turtle.circle(r, anggle)
turtle.bk(d)
turtle.fd(d)
```

```
import turtle
turtle.left(45)
turtle.fd(150）
turtle.right(135)
turtle.fd(300)
turtle.left(135)
turtle.fd(150)
```

#### RGB色彩体系

由三种颜色形成的万物色，RGB每色取值范围0~255整数或者0~1小数

|英文名称|RGB|RGB|中文|
|:---:|:---:|:---:|:---:|
|white|255, 255, 255|1, 1, 1|白色|
|yellow|255, 255, 0|1, 1, 0|黄色|
|magenta|255, 0, 255|1, 0, 1|洋红|
|cyan|0, 255, 255|0, 1, 1|青色|
|blue|0, 0, 255|0, 0, 1|蓝色|
|black|0, 0, 0|0, 0, 0|黑色|
|gold|255, 215, 0|1, 0.84, 0|金色|
|purple|160, 32, 240|0.63, 0.13, 0.94|紫色|

###### turtle.colormode(mode)

1.0：RGB小数值模式

255：RGB整数值模式

共有三种使用的方式

```
t.pencolor("purple") #颜色字符串
t.pencolor(1, 1, 1) #RGB的小数值
t.pencolor((1, 1, 1) #RGB的元组值
```

### import更多用法

```
import turtle
turtle.setup(650, 350, 200, 200)
turtle.penup()
```

```
from turtle import*
setup(650, 350, 200, 200)
penup()
```

```最佳方法
import turtle as t
t.setup(650, 350, 200, 200)
t.penup()
```

> 第一种不会出现函数重名的问题，第二种可能会出现函数重名的问题。但也有解决办法，依据情况混合使用即可。二第三种即是最佳方法

### 方向控制函数

控制海🐢面对方向：绝对角度&海龟角度。只改变方向，不使之走动。

##### 绝对角度

`turtle.setheading(angle) #turtle.seth(angle)`

> 正负值和直角坐标系一致

##### 海🐢角度

```
t.left(angle)
t.right(angle)
```

### rangge() 函数

产生循环计数序列，记住这个是函数即可，复习上节课的[字符串和`range()`的结合](https://github.com/SimonZhong2025/Waste-Self-Rescue-Scheme/blob/master/Simon%E2%80%98s%20base%20camp/Python/MOOC%20python%E8%AF%AD%E8%A8%80%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1/01%20Python123%E7%AC%AC%E4%B8%80%E5%8D%95%E5%85%83%E7%BB%83%E4%B9%A0%E9%A2%98.md)


##### 学生作品
![](https://github.com/SimonZhong2025/Waste-Self-Rescue-Scheme/blob/master/Simon%E2%80%98s%20base%20camp/Python/MOOC%20python%E8%AF%AD%E8%A8%80%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1/Ps/turtle%E6%A1%88%E4%BE%8B.jpg)
