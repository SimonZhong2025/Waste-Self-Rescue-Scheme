+ `str.rstrip` 删除右侧空格
+ `列表.append(元素)` 在list后面添加元素
+ `列表.insert(x, 元素)` 将元素插入到列表的x下标处
+ 所以`for x in ...`循环就是把每个元素代入变量`x`，然后执行缩进块的语句。
+ `range(x)` 可以生成一个整数序列，再通过 `list()` 可以转换为list
+ 判断一个dict里是否有某个key，可以 `'Thomas' in d` ，用in来判断，如果这个字典里面没有以 `Thomas` 为键的值则返回 `False`
+ set和dict一样都不可放 **不可变对象** 。所以不能将一个 `list` 放到一个 `set` 里面
+ 可以将一个 `tuple` 放到一个 `set` 里面，但是这个 `tuple` 里面不能有 `list` ，因为 `list` 是可变的对象
+ `set` 里面没有重复的元素

+ `max` 可以传进去元组或者列表，也可以传进去多个 `int`(浮点也行)

+ ```python
  isinstance(object, classinfo)
  ```

  class可以是直接或间接类名、基本类型或者由它们组成的元组。如 `isinstance(1, (int, float))`

  如果 `object` 的类型和 `classinfo` 的类型相同则返回 `True` ，否则返回 `False`

+ 判断变量类型可以用这个方法

  ```python
  if not isinstance(x, (int, float)):
      raise TypeError('bad operand type')
  ```

  raise一个错误

+ 一个函数可以返回多个返回值，但是事实上返回的是一个 `tuple` 元组。

  ```python
  def aaa:
      return 1, 2
  
  x, y = aaa()
  ```

  这样可以获得多个变量。但事实上返回的还是一个返回值，不过这个返回值是一个元组。	

+ **定义默认参数要牢记一点：默认参数必须指向不变对象！** 如果将默认参数设置为一个列表list，那么上一次调用函数结束时这个参数的值会保留到下一次函数调用的时候。如下

  ```python
  def add_end(L=[]):
      L.append('END')
      return L
  
  >>> add_end()
  ['END']
  >>> add_end()
  ['END', 'END']
  >>> add_end()
  ['END', 'END', 'END']
  ```

+ 在传入的参数前面加上一个 `*` 可以传入任意个参数（包括0个）。而在传入的参数前面加上 `**` 则可以传入字典。如 `city = 'Beijing'` 。

  ```python
  def calc(*numbers):
      sum = 0
      for n in numbers:
          sum = sum + n * n
      return sum
  
  >>> calc(1, 2)
  5
  >>> calc()
  0
  
  # 而如果想要直接传一个list或者tuple进去，则可以在这个list或者tuple前面加上*，如下
  >>> nums = [1, 2, 3]
  >>> calc(*nums)
  14
  ```

  而如果想要传一个字典到一个参数中有 `**dict` 的函数中去，也可以传字典，如下

  ```python
  def person(name, age, **kw):
      print('name:', name, 'age:', age, 'other:', kw)
  
  >>> extra = {'city': 'Beijing', 'job': 'Engineer'}
  >>> person('Jack', 24, **extra)
  name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
  ```

  > 注意这里传进去的 `kw` 是一份 `extra` 的拷贝，修改 `kw` 的内容并不会影响到原来的 `extra` 里面的内容

  ![image-20200907152145694](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200907152145694.png)

  命名关键字参数必须传入参数名，这和位置参数不同。 **如果没有传入参数名，调用将报错。**

+ **参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。**
+ `list` ，`tuple` ，`字符串` 都可以进行切片操作。切片操作第一个参数是起始位置，第二个参数是终止位置，第三个参数是隔多少个元素取一个。起始位置和结束位置都可以是负数（倒着数）