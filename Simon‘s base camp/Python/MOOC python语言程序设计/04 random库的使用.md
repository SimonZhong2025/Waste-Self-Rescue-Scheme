random库时使用随机数的Python标准库

random最基本的就是产生随机数random，random库包括两类函数，常用共8个

- 基本随机数函数：seed(), random()
- 扩展随机数函数：randint(), getrandbits(), uniform(), randrange(), choice(), shuffle()

### 需要掌握的能力
- 能够利用随机数种子产生的“确定”伪随机数
- 能够产生随机整数
- 能够对序列类型进行随机操作
主要要能主要掌握3~4个函数

### 基本随机数函数

|函数|描述|
|:---:|:---:|
|seed(a = None)|初始化给定的随机数种子，默认为当前系统时间</br>>>>random.seed(10) #产生种子10对应的序列|
|random()|生成一个[0.0, 1.0)之间的随机小数 </br>>>>random.random()</br>0.5714025946899135|

```
>>>import random
>>>random.seed(10)
>>>random.random()
0.5714025946899135
>>>random.random()
0.4288890546751146
```

我们使用种子，下次再用这个程序，可以再现和复现，看我们程序的需求。如果我只需要随机数，可以不需要设定种子数。

```
>>>import random
>>>random.seed(10)
>>>random.random()
0.5714025946899135
>>>random.seed(10)
>>>random.random()
0.5714025946899135
```

> 调用random函数的顺序只要相同，那么产生的随机数都是相同的。

|函数|描述|
|:---:|:---:|
|randint(a, b)|生成一个[a, b]之间的整数|
|randrange(m, n[,k])|生成一个[m, n)之间以k为步长的随机整数|
|getrandbits(k)||
|uniform(a, b)|生成一个[a, b]之间的随机小数|
