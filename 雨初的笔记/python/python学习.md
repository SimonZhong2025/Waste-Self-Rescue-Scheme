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

+ `dict` 迭代的是key。如果要迭代 `value` ，可以用`for value in d.values()`，如果要同时迭代 `key` 和 `value` ，可以用`for k, v in d.items()`。

+ 如果需要判断某个对象是否为可迭代的对象，可以通过collections模块的Iterable类型判断

  ```python
  >>> from collections.abc import Iterable
  >>> isinstance('abc', Iterable) # str是否可迭代
  True
  >>> isinstance([1,2,3], Iterable) # list是否可迭代
  True
  >>> isinstance(123, Iterable) # 整数是否可迭代
  False
  ```

+ 如果想通过下标循环一个列表，可以用内置的 `enumerate` 函数

  ```python
  >>> for i, value in enumerate(['A', 'B', 'C']):
  ...     print(i, value)
  ...
  0 A
  1 B
  2 C
  ```

+ 列表生成式后面的 `if` 是一个筛选条件，后面不能加上 `else` ，但是如果 `if` 放在 `for` 前面则必须加上 `else` 。因为此时是一个生成式。

+ 一个 **生成器** 和一个 **列表生成式** 的区别只是生成器是用 `()` 包起来的，而一个列表生成式是用 `[]` 包起来的。 一个生成器的值可以通过 `next(生成器)` 不断获得。

  ```python
  >>> g = (x * x for x in range(5))
  >>> g
  <generator object <genexpr> at 0x1022ef630>
  >>> next(g)
  0
  >>> next(g)
  1
  >>> next(g)
  4
  >>> next(g)
  9
  >>> next(g)
  16
  >>> next(g)
  25
  
  >>> next(g)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  StopIteration
  ```

+ ```python
  for i in range(5):
      print(i)
  #输出是0 1 2 3 4
  ```

+ 一个生成器在迭代到最后一个元素，没有更多的元素的时候会抛出 `StopIteration` 错误。

+ 一般使用生成器的时候也是用 `for` 循环来迭代里面的元素，因为 `generator` 也是可迭代对象。

+ 对于一个有 `yield` 的函数，它返回的是一个迭代器，并不是在 `return` 语句处返回，而是每次调用 `yeild` 的时候执行，遇到 `yeild` 返回，再次执行的时候从上次返回的 `yeild` 语句处继续执行。

  + 当然，对于一个可迭代的函数，我们也通常不会使用 `next` 来迭代这个函数，而是使用 `for` 来对这个生成器进行迭代。

+ 生成器都是`Iterator`对象，但`list`、`dict`、`str`虽然是`Iterable`，却不是`Iterator`。

  + 要能使用 `next` 获取下一对象的对象才能称为 `Iterator` 对象。
  + 如果需要将列表、元组、字典变为可迭代的对象，可以使用内置的 `iter` 方法。

+ ```python
  for x in [1, 2, 3, 4, 5]:
      pass
  
  #完全等价于
  
  it = iter([1, 2, 3, 4, 5]) # 首先获得Iterator对象:
  while True: # 循环:
      try:
          # 获得下一个值:
          x = next(it)
      except StopIteration:
          # 遇到StopIteration就退出循环
          break
  ```

+ python可以写出函数式的代码

  ```python
  def add(x, y, f):
      return f(x) + f(y)
  
  print(add(-5, 6, abs))
  # 结果为11
  ```

+ 要使用 `reduce` 需要在开头加上 `from functools import reduce`

  ```python
  >>> from functools import reduce
  >>> def add(x, y):
  ...     return x + y
  ...
  >>> reduce(add, [1, 3, 5, 7, 9])
  25
  ```

  `reduce` 中，函数接受两个参数， `reduce` 将结果继续和序列的下一个元素进行累积运算。

+ 使用 `type` 可以获得某个目标变量的类型

+ `del` 可以删除一个变量

+ `filter` 返回的值是一个 `Iterator` ，如果想强迫其计算完所有结果需要用 `list` 取得其所有结果

+ `sorted(列表, key = 处理函数)` 将这个列表中的每个元素通过处理函数处理，然后将其进行排序。返回的列表中的所有元素是处理函数处理之前的元素。

  + 如果要实现反向排列，可以传入第三个参数 `reverse = True`

+ **返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。**

+ 如果在生成闭包的时候想要使用外面的变量，要声明这个变量不是局部变量，用 `nonlocal 变量` 来声明

+ `lambda` 匿名函数 `arg1, arg2, ... argn : 表达式` 返回值是表达式的值

+ 函数对象有一个 `__name__` 属性，可以拿到函数的名字



+ 装饰器

  把`@log`放到`now()`函数的定义处，相当于执行了语句：

  ```python
  now = log(now)
  ```

  把 `@log('execute')` 放到函数的定义处，相当于执行了语句

  ```python
  now = log('execute')(now)
  ```

  这行代码的实际意义是先调用 `log('execute')` 返回一个函数（一个装饰器），然后将 `now` 作为参数传入这个函数中，将最终调用的值赋给 `now`

  + 但通过装饰器返回的函数的 `__name__` 属性是装饰器的函数名，如果需要将返回的函数的名称设置为其原来的名称，不需要写 `wrapper.__name__ = func.__name__` 这种代码，只需要使用python内置的 `functools.wraps` 。像这样在 `wrapper` 前面加上一行 `@functools.wraps(func)`

    ```python
    import functools
    
    def log(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('call %s():' % func.__name__)
            return func(*args, **kw)
        return wrapper
    ```

    或者针对带参数的decorator：

    ```python
    import functools
    
    def log(text):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator
    ```

+ `functools.partial` 是用来给我们创建一个偏函数的，不用我们再像这样

  ```python
  def int2(x, base=2):
      return int(x, base)
  ```

  写一个偏函数，而是可以直接使用 `functools.partial` 来自动生成一个偏函数

  ```python
  >>> import functools
  >>> int2 = functools.partial(int, base=2)
  >>> int2('1000000')
  64
  >>> int2('1010101')
  85
  ```

  + 而如果像这样 `max2 = functools.partial(max, 10)` 使用偏函数，则在调用 `max2` 这个函数的时候会将 `10` 自动添加到调用 `max` 函数的最左边的参数，如下

    ```python
    max2 = functools.partial(max, 10)
    max2(5, 6, 7)
    # 等价于
    args = (10, 5, 6, 7)
    max(*args)
    ```

+ 任何模块代码的第一个字符串都被视为模块的文档注释。

  ```python
  #!/usr/bin/env python3
  # -*- coding: utf-8 -*-
  
  ' a test module '
  
  __author__ = 'Michael Liao'
  
  import sys
  
  def test():
      args = sys.argv
      if len(args)==1:
          print('Hello, world!')
      elif len(args)==2:
          print('Hello, %s!' % args[1])
      else:
          print('Too many arguments!')
  
  if __name__=='__main__':
      test()
  ```

  这段代码中的 `'a test module'` 便可被视为这个模块的文档注释



## OOP

+ 可以自由地给一个实例变量绑定属性，比如，给实例`bart`绑定一个`name`属性：

  ```python
  >>> bart.name = 'Bart Simpson'
  >>> bart.name
  'Bart Simpson'
  ```

+ `__init__` 方法的第一个参数永远是 `self` ，表示创建的示例本身。在 `__init__` 中将各种属性绑定到 `self` 可以给创建的示例本身绑定属性。

+ 如果有了 `__init__` 方法，在创建示例的时候就不能传入空的参数了，必须传入和 `__init__` 方法匹配的参数（但是 `self` 不需要传）

+ `python` 的类里面的私有变量要在变量名前面加上两个下划线。如 `__name` ，这样就无法在类外面访问这个变量。

+ `isinstance` 判断的时候，一个对象既是它的父类，也是它所属的类的对象。

+ 对于C和JAVA这种静态语言，传进去的类型必须是 `Animal` 类型或者它的子类，不过像python这种动态语言，我们只要保证传入的对象有一个 `run()` 方法就可以了。

  >这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
  
+ 如果要获得一个对象的所有属性和方法，可以使用 `dir()` 函数，它返回一个包含字符串的list，比如，获得一个 `str` 对象的所有属性和方法：

+ `len()` 其实底层也是调用 `字符串.__len__()` 方法。

+ `setttr(object, name, value)` 可以给 `object` 这个对象添加一个 `name` 的属性，这个属性对应的值是 `value` 。

+ `hasattr` 可以用来防止错误，判断传进来的对象是否有这个属性

+ > 在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

+ 要想修改类里面的属性要用 `类名.属性` 来修改。如果想在 `__init__()` 里面对其进行修改，不要用 `self.属性` ，而是要用 `类名.属性` 来修改。

+ 要给一个实例绑定一个方法：

  ```python
  from types import MethodType
  s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
  s.set_age(25) # 调用实例方法
  >>> s.age # 测试结果
  >>> 25
  ```

  但是这种方法只能给一个示例绑定一个方法，这个类的其他示例是不起作用的。如果想要给所有实例都绑定方法，可以给 `class` 绑定方法。

  ```python
  >>> def set_score(self, score):
  ...     self.score = score
  ...
  >>> Student.set_score = set_score
  ```

  这样绑定方法之后所有实例都可调用。

+ 如果想要限制某个class的实例能添加的属性，可以设置其中的 `__slots__` 属性，如下

  ```python
  class Student(object):
      __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
  ```

  这样Student的实例就只能绑定 `score` 和 `age` 这两个属性，如果试图绑定其他属性则会抛出 `AttributeError` 错误。

  + 另外使用 `__slots__` 的时候要注意其定义的属性只对当前类实例起作用，对继承的子类是不起作用的：

    ```python
    >>> class GraduateStudent(Student):
    ...     pass
    ...
    >>> g = GraduateStudent()
    >>> g.score = 9999
    ```

    除非在子类中也定义 `__slots__` ，这样子类实例允许定义的属性就是 **自身的`__slots__`加上父类的`__slots__`。** 。

+ `@property` 这个装饰器用来给类的属性来定义参数检查， **负责把一个方法变成属性调用** ，在 `def 属性(self)` 前面加上 `@property` 这个装饰器表示给这个属性设定一个 **getter** ，获取这个类的属性的时候自动调用这个函数。而设定了 **getter** 之后在后面 `def 属性(self, value)` 的前面加上 `@score.setter` 则说明这是一个对应的 `setter` ，当设定这个属性的值的时候即调用这个函数。如下

  ```python
  class Student(object):
  
      @property
      def score(self):
          return self._score
  
      @score.setter
      def score(self, value):
          if not isinstance(value, int):
              raise ValueError('score must be an integer!')
          if value < 0 or value > 100:
              raise ValueError('score must between 0 ~ 100!')
          self._score = value
  ```

  ```python
  >>> s = Student()
  >>> s.score = 60 # OK，实际转化为s.set_score(60)
  >>> s.score # OK，实际转化为s.get_score()
  60
  >>> s.score = 9999
  Traceback (most recent call last):
    ...
  ValueError: score must between 0 ~ 100!
  ```

  如果只定义 `getter` 方法而不定义 `setter` 方法说明这个属性是一个只读属性。

  + 使用 **getter** 和 **setter** 的时候要注意

    ```python
    @property
    def width(self):
        return self._width
    ```

    要写 `self._属性` ，在属性前面要加上一个下划线，不然会报错。

+ 多重继承直接在类的定义中写上多个父类就行了

  > 如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让`Ostrich`除了继承自`Bird`外，再同时继承`Runnable`。这种设计通常称之为MixIn。
  >
  > 为了更好地看出继承关系，我们把`Runnable`和`Flyable`改为`RunnableMixIn`和`FlyableMixIn`。类似的，你还可以定义出肉食动物`CarnivorousMixIn`和植食动物`HerbivoresMixIn`，让某个动物同时拥有好几个MixIn：
  >
  > ```python
  > class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
  >     pass
  > ```

+ `__str__()` 方法和 `__repr__()` 方法的区别是 `__str__()` 返回的是用户看到的字符串，而 `__repr__()` 返回程序开发者看到的字符串，换句话说 `__repr__()` 是为 **调试** 服务的。

  一般要定义一个 `__str__()` 和一个 `__repr__()` ，但是一般这两个魔术方法的代码是一样的，所以有一种偷懒的方法

  ```python
  class Student(object):
      def __init__(self, name):
          self.name = name
      def __str__(self):
          return 'Student object (name=%s)' % self.name
      __repr__ = __str__
  ```

+ 如果一个类想被用于`for ... in`循环，类似list或tuple那样，就必须实现一个`__iter__()`方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的`__next__()`方法拿到循环的下一个值，直到遇到`StopIteration`错误时退出循环。

  如果想要写一个可以迭代的，用于产生斐波那契数列的类，代码如下

  ```python
  class Fib(object):
      def __init__(self):
          self.a, self.b = 0, 1 # 初始化两个计数器a，b
  
      def __iter__(self):
          return self # 实例本身就是迭代对象，故返回自己
  
      def __next__(self):
          self.a, self.b = self.b, self.a + self.b # 计算下一个值
          if self.a > 100000: # 退出循环的条件
              raise StopIteration()
          return self.a # 返回下一个值
  ```

  将这个实例用于 `for` 循环，结果如下

  ```python
  >>> for n in Fib():
  ...     print(n)
  ...
  1
  1
  2
  3
  5
  ...
  46368
  75025
  ```

+ 如果想要让一个通过 `__iter__()` 和 `__next__()` 达到能迭代的对象的实例能够像list那样可以 **通过下标来取得某一特定元素** ，可以设定其 `__getitem__()` 属性。如下：

  ```python
  class Fib(object):
      def __getitem__(self, n):
          a, b = 1, 1
          for x in range(n):
              a, b = b, a + b
          return a
  ```

  而如果还想让这个函数支持像list一样的切片方法，则还要判断传入的类型。因为切片的时候传入的是一个 `slice` 对象而不像通过下标取元素一样是一个 `int` 对象。

  ```python
  class Fib(object):
      def __getitem__(self, n):
          if isinstance(n, int): # n是索引
              a, b = 1, 1
              for x in range(n):
                  a, b = b, a + b
              return a
          if isinstance(n, slice): # n是切片
              start = n.start
              stop = n.stop
              if start is None:
                  start = 0
              a, b = 1, 1
              L = []
              for x in range(stop):
                  if x >= start:
                      L.append(a)
                  a, b = b, a + b
              return L
  ```

  一个 `slice` 有 `start` 、`stop` 、`step` 属性，分别代表切片的开始、结尾、步长。



