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

+ 如果没有找到一个实例的属性，会自动调用 `__getattr__()` 方法，已有的属性不会在 `__getattr__()` 中查找。如下：

  ```python
  class Student(object):
  
      def __getattr__(self, attr):
  		if attr=='score':
  			return 99
          if attr=='age':
              return lambda: 25
          
  >>> s.score
  99
  >>> s.age()
  25
  ```

  如果想让class只响应特定的几个属性，我们要在没有找到相应属性的时候抛出 `AttributeError` 的错误。

  ```python
  class Student(object):
  
      def __getattr__(self, attr):
          if attr=='age':
              return lambda: 25
          raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
  ```

+ 定义一个 `__call__()` 方法，可以直接对实例进行调用。

  ```python
  class Student(object):
      def __init__(self, name):
          self.name = name
  
      def __call__(self):
          print('My name is %s.' % self.name)
          
  >>> s = Student('Michael')
  >>> s() # self参数不要传入
  My name is Michael.
  ```

  `__call__()` 中也可以传入参数，完全可以将其当作一个函数来进行调用。事实上在python中一个实例和一个函数也并没有什么本质上的区别。

+ 通过`callable()`函数，我们就可以判断一个对象是否是“可调用”对象。

+ `@unique`装饰器可以帮助我们检查保证没有重复值。(要 `from enum import Enum, unique` )

+ 要创建一个 `class` 对象， `type()` 函数依次传入3个参数

  ```python
  type(class的名称, 继承的父类集合, class的方法名称和函数绑定)
  ```

  实例如下

  ```python
  >>> def fn(self, name='world'): # 先定义函数
  ...     print('Hello, %s.' % name)
  ...
  >>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello 
  class
  >>> h = Hello()
  >>> h.hello()
  Hello, world.
  >>> print(type(Hello))
  <class 'type'>
  >>> print(type(h))
  <class '__main__.Hello'>
  ```

+ 如果要使用 `metaclass` ，要使用如下代码

  ```python
  # metaclass是类的模板，所以必须从`type`类型派生：
  class ListMetaclass(type):
      def __new__(cls, name, bases, attrs):
          attrs['add'] = lambda self, value: self.append(value)
          return type.__new__(cls, name, bases, attrs)
  ```

  其中 **metaclass** 必须从 `type` 类派生出来，且这个 **metaclass** 中必须有 `__new__()` 方法。

## 错误处理

+ 如果有一段代码可能会出错，可以用 `try` 去运行它。一旦这段代码执行出错，则后续代码不会继续执行，而是直接跳转到错误处理代码，即 `except` 代码块，如果执行完 `except` 之后后面还有 `finally` 语句块，则继续执行 `finally` 语句块。 **`finally` 代码块无论出现错误与否都会被执行。**

+ 如果可能产生的错误有不同种类，则可以通过不同 `except` 语句块处理，如下：

  ```python
  try:
      print('try...')
      r = 10 / int('a')
      print('result:', r)
  except ValueError as e:
      print('ValueError:', e)
  except ZeroDivisionError as e:
      print('ZeroDivisionError:', e)
  finally:
      print('finally...')
  print('END')
  ```

+ 使用`try...except`捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数`main()`调用`bar()`，`bar()`调用`foo()`，结果`foo()`出错了，这时，只要`main()`捕获到了，就可以处理：

  ```python
  def foo(s):
      return 10 / int(s)
  
  def bar(s):
      return foo(s) * 2
  
  def main():
      try:
          bar('0')
      except Exception as e:
          print('Error:', e)
      finally:
          print('finally...')
  ```

+ python内置的 `logging` 模块可以非常容易地记录错误信息，如 `logging.exception(e)`

  ```python
  # err_logging.py
  
  import logging
  
  def foo(s):
      return 10 / int(s)
  
  def bar(s):
      return foo(s) * 2
  
  def main():
      try:
          bar('0')
      except Exception as e:
          logging.exception(e)
  
  main()
  print('END')
  
  $ python3 err_logging.py
  ERROR:root:division by zero
  Traceback (most recent call last):
    File "err_logging.py", line 13, in main
      bar('0')
    File "err_logging.py", line 9, in bar
      return foo(s) * 2
    File "err_logging.py", line 6, in foo
      return 10 / int(s)
  ZeroDivisionError: division by zero
  END
  ```

+ 如果想要抛出错误，可以使用python内置的错误类型，也可以 **自定义错误类型**

  ```python
  class FooError(ValueError):
      pass
  
  def foo(s):
      n = int(s)
      if n==0:
          raise FooError('invalid value: %s' % s)
      return 10 / n
  
  foo('0')
  ```

  执行，可以最后跟踪到我们自己定义的错误：

  ```python
  $ python3 err_raise.py 
  Traceback (most recent call last):
    File "err_throw.py", line 11, in <module>
      foo('0')
    File "err_throw.py", line 8, in foo
      raise FooError('invalid value: %s' % s)
  __main__.FooError: invalid value: 0
  ```

  用 `try except` 语句捕捉到错误之后也可以使用 `raise` 来将这个错误重新抛出去

  ```python
  # err_reraise.py
  
  def foo(s):
      n = int(s)
      if n==0:
          raise ValueError('invalid value: %s' % s)
      return 10 / n
  
  def bar():
      try:
          foo('0')
      except ValueError as e:
          print('ValueError!')
          raise
  
  bar()
  ```

  这种使用方法非常常见，处理不了就将异常往上抛，抛到最顶层来对这个错误进行处理。

  +  `raise` 语句如果不带参数，则会把当前错误原样抛出，而如果想要定义错误的类型，也可以在 `raise` 语句之后自定义抛出的错误。如下

    ```python
    try:
        10 / 0
    except ZeroDivisionError:
        raise ValueError('input error!')
    ```

    但是绝对不能将一个错误转换为另一个毫不相关的错误。

+ python的 `assert` 的用法如下：`assert n != 0, 'n is zero!'`

  如果想要在运行的时候关掉 `assert` 断言，那么可以在运行 `python` 的时候加上 `-O` 参数（注意其中是大写的O）

+ `logging` 可以指定记录信息的级别，有`debug`，`info`，`warning`，`error`等几个级别，通过如下方法设置

  ```python
  import logging
  logging.basicConfig(level=logging.INFO)
  ```

  将 `level` 设置为 `logging.INFO` 之后则可以看到 `.info` 级别的输出，需要使用的时候代码如下

  ```python
  import logging
  
  s = '0'
  n = int(s)
  logging.info('n = %d' % n)
  print(10 / n)
  ```

  ## 单元测试

+ 需要编写单元测试时可以使用python自带的 `unittest` 模块

  ```python
  import unittest
  
  from mydict import Dict
  
  class TestDict(unittest.TestCase):
  
      def test_init(self):
          d = Dict(a=1, b='test')
          self.assertEqual(d.a, 1)
          self.assertEqual(d.b, 'test')
          self.assertTrue(isinstance(d, dict))
  
      def test_key(self):
          d = Dict()
          d['key'] = 'value'
          self.assertEqual(d.key, 'value')
  
      def test_attr(self):
          d = Dict()
          d.key = 'value'
          self.assertTrue('key' in d)
          self.assertEqual(d['key'], 'value')
  
      def test_keyerror(self):
          d = Dict()
          with self.assertRaises(KeyError):
              value = d['empty']
  
      def test_attrerror(self):
          d = Dict()
          with self.assertRaises(AttributeError):
              value = d.empty
  ```

  编写单元测试的时候，我们需要编写一个测试类，这个测试类继承于 `unittest.testCase` 。以 `test` 开头的方法就是测试方法，不以 `test` 开头的方法不被认为是测试方法，测试的时候不会执行。主要有如下的测试方法

  ```python
  self.assertRaises()
  self.assertEqual()
  self.assertTrue()
  self.assertFalse()
  ```

+ 写好单元测试之后需要开启测试只需要给main函数加上如下代码

  ```python
  if __name__ == '__main__':
      unittest.main()
  ```

  或者也可以在命令行通过参数 `-m unittest` 来直接运行单元测试，这是推荐的做法，因为这样可以一次运行多个单元测试，并且，有很多工具可以自动来运行这些单元测试。

+ 在测试中写的`setUp()`和`tearDown()`方法会分别在测试启动和测试结束的时候被调用。这样可以防止在每个测试函数中写出重复的代码，比如连接数据库和断开与数据库的连接。

+ 编写文档测试的时候中间多余的输出可以用 `...` 表示

  > 另外，当模块正常导入时，doctest不会被执行。只有在命令行直接运行时，才执行doctest。所以，不必担心doctest会在非测试环境下执行。

  ## IO

+ 同步IO和异步IO的区别是CPU等不等IO

+ 由于文件读写都有可能产生 `IOError` ，为了无论对错都能正确关闭文件，可以使用 `try ... finally` 实现。无论是否打开成功都使用 `f.close()` 关闭文件。

+ 日常使用中并不需要使用 `try ... finally` 来防止文件打开出错的问题。使用 `with open(filepath, 'r') as f:` 就可以保证无论是否成功打开文件都会调用 `f.close()` 方法来关闭文件IO流。如下

  ```python
  with open('/path/to/file', 'r') as f:
      print(f.read())
  ```

  `read(size)` 方法可以设定一次读取的字节的多少， `readline()` 可以每次读取一行的内容，使用 `readlines()` 可以一次读取所有内容并按行返回一个 `list` 。（如果是读取配置文件一般使用 `readlines()` 方法来读取）

+ 如果要读取非 `utf-8` 编码的文本文件，需要给 `open()` 函数传入 `encoding` 参数。例如如果需要读取GBK编码的文件

  ```python
  >>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
  >>> f.read()
  '测试'
  ```

  >遇到有些编码不规范的文件，你可能会遇到`UnicodeDecodeError`，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，`open()`函数还接收一个`errors`参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
  >
  >```python
  >>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
  >```

+ 在使用 `write` 来写文件的时候，务必要在结束的时候调用 `close()` 方法，只有调用了 `close()` 方法操作系统才会将等IO的时候缓存的数据全部写入磁盘中。因为 `write()` 方法写数据的时候总是要等到空闲的时候再慢慢写入，如果不在最后调用 `close()` 方法，甚至可能数据只写了一部分到硬盘中而剩下的丢失了。所以使用 `wirte()` 方法的时候也是使用 `with` 语句来打开比较保险。这样不会忘记使用 `close()` 而导致输出的数据不完整。

+ ```python
  from io import StringIO
  ```

  `StringIO` 可以将内存中的字符串像读文件一样读取。这个是不是和 `sscanf` `sprintf` 有点像？

+ ```python
  from io import BytesIO
  ```

  `StringIO` 操作的只能是 `str` ，如果要操作二进制数据，就需要使用 `BytesIO` 。

+ os中的 `uname()` 函数在 `windows` 上不提供。 `os` 模块的某些函数是跟操作系统相关的。

+ 合并路径的两部分时，要用其提供的 `os.path.join()` 函数，这样可以处理不同操作系统的路径分隔符，而 `os.path.split()` 也可以将路径拆分为最后级别的目录或文件名和前面的路径两部分。

  ```python
  >>> os.path.split('/Users/michael/testdir/file.txt')
  ('/Users/michael/testdir', 'file.txt')
  ```

  `os.path.splitext()`可以直接让你得到文件扩展名，很多时候非常方便：

  ```python
  >>> os.path.splitext('/path/to/file.txt')
  ('/path/to/file', '.txt')
  ```

  `os` 中没有提供用于复制文件的函数，但幸运的是`shutil`模块提供了`copyfile()`的函数，你还可以在`shutil`模块中找到很多实用函数，它们可以看做是`os`模块的补充。

  最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：

  ```python
  >>> [x for x in os.listdir('.') if os.path.isdir(x)]
  ['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Applications', 'Desktop', ...]
  ```

  要列出所有的`.py`文件，也只需一行代码：

  ```python
  >>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
  ['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']
  ```

+ `serialization，marshalling，flattening` 都是序列化操作，在Python中叫 `pickling`

+ python提供了 `pickle` 模块来实现序列化。

  ```python
  with open('dump.txt', 'wb') as f:
  	pickle.dump(d, f)
  ```

  `pickle.dumps(d)` 将对象封装后作为 `bytes` 类型直接返回，而不是将其写入到文件。

  `pickle.dump(d, f)` 将对象封装后写入已经打开的 `f` 对象中。

+ 要将python对象序列化为 `json` ，可以使用python内置的json库

  ```python
  import json
  ```

  如果想要把一个自定义的类序列化为json，需要在序列化的时候传入一个能够用来将该对象转换为能被序列化的对象的函数。如下：

  ```python
  def student2dict(std):
      return {
          'name': std.name,
          'age': std.age,
          'score': std.score
      }
  
  >>> print(json.dumps(s, default=student2dict))
  {"age": 20, "name": "Bob", "score": 88}
  ```

  一般没有定义 `__slots__` 的class都有一个 `__dict__` 属性（注意这是一个属性而不是一个方法），如果我们想要序列化一个没有 `__slots__` 属性的class，也可以偷点懒利用这个属性

  ```python
  print(json.dumps(s, default=lambda obj: obj.__dict__))
  ```

  这样就不用另外写一个用来将类转换为能够序列化的对象的函数了。

## 常用内建模块

### datetime

+ ```python
  from datetime import datetime
  ```

  `datetime` 是模块，这个模块还包含一个 `datetime` 类。如果仅导入 `import datetime` 则必须引用全名 `datetime.datetime` 。

+ `datetime.now()` 可以获取当前日期和时间

  ```python
  >>> from datetime import datetime
  >>> now = datetime.now() # 获取当前datetime
  >>> print(now)
  2015-05-18 16:28:07.198690
  >>> print(type(now))
  <class 'datetime.datetime'>
  ```

+ 1970年1月1日0：0：0之前的时间的UNIX时间是一个负数

+ 如果需要获取某个时间的UNIX时间戳，只需要对这个 `datetime` 对象调用 `.timestamp()` 方法。

  > 注意Python的timestamp是一个浮点数，整数位表示秒。
  >
  > 某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。

+ `//` 是向下取整的

+ 如果要将某一个  `timedate` 对象的时区转换为另一个时区，可以使用 `timedate对象.replace(tzone = 一个timezone对象)` 来达到目的。

### collections

+ `namedtuple`

  + `namedtuple`是一个函数，它用来创建一个自定义的`tuple`对象，并且规定了`tuple`元素的个数，并可以用属性而不是索引来引用`tuple`的某个元素。如下

    ```python
    >>> from collections import namedtuple
    >>> Point = namedtuple('Point', ['x', 'y'])
    >>> p = Point(1, 2)
    >>> p.x
    1
    >>> p.y
    2
    ```

    >`collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)`
    >
    >*field_names* 是一个像 `[‘x’, ‘y’]` 一样的字符串序列。另外 *field_names* 可以是一个纯字符串，用空白或逗号分隔开元素名，比如 `'x y'` 或者 `'x, y'` 。
    >
    >如果 *rename* 为真， 无效字段名会自动转换成位置名。比如 `['abc', 'def', 'ghi', 'abc']` 转换成 `['abc', '_1', 'ghi', '_3']` ， 消除关键词 `def` 和重复字段名 `abc` 。

### base64

+ 如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用`\x00`字节在末尾补足后，再在编码的末尾加上1个或2个`=`号，表示补了多少字节，解码的时候，会自动去掉。

### hashlib

+ 计算MD5的代码如下

  ```python
  import hashlib
  
  md5 = hashlib.md5()
  md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
  print(md5.hexdigest())
  # 结果如下d26a53750bc40b38b65a520292f69306
  ```

  如果数据量很大，可以分块多次调用 `update()` ，最后计算的结果是一样的

  ```python
  md5 = hashlib.md5()
  md5.update('how to use md5 in '.encode('utf-8'))
  md5.update('python hashlib?'.encode('utf-8'))
  print(md5.hexdigest())
  ```

  如果想要使用另外一种摘要算法 `sha1` ，只要变为 `sha1 = hashlib.sha1()` 即可

### hmac

+ 使用hmac的时候需要提供原始的消息、给消息加盐的随机 `key` 和需要使用的哈希算法。如果需要使用哈希算法，代码如下

  ```python
  >>> import hmac
  >>> message = b'Hello, world!'
  >>> key = b'secret'
  >>> h = hmac.new(key, message, digestmod='MD5')
  >>> # 如果消息很长，可以多次调用h.update(msg)
  >>> h.hexdigest()
  'fa4ee7d173f2d97ee79022d1a7355bcf'
  ```

### itertools

```python
 import itertools
```

- ```python
  itertools.count(start=0, step=1)
  ```

  `count()` 会创建一个迭代器，从 **start** 值开始，返回均匀间隔的值

  > 常用于 [`map()`](https://docs.python.org/zh-cn/3/library/functions.html#map) 中的实参来生成连续的数据点。此外，还用于 [`zip()`](https://docs.python.org/zh-cn/3/library/functions.html#zip) 来添加序列号

  ```python
  >>> import itertools
  >>> natuals = itertools.count(1)
  >>> for n in natuals:
  ...     print(n)
  ...
  1
  2
  3
  ...
  ```

- `cycle()` 会把传入的一个序列无限重复下去

  ```python
  >>> import itertools
  >>> cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
  >>> for c in cs:
  ...     print(c)
  ...
  'A'
  'B'
  'C'
  'A'
  'B'
  'C'
  ...
  ```

- `repeat()` 同样可以让一个元素无限重复下去，但是和 `cycle()` 不同的是如果提供第二个参数就可以限定重复的次数。

  ```python
  >>> ns = itertools.repeat('A', 3)
  >>> for n in ns:
  ...     print(n)
  ...
  A
  A
  A
  ```

- 无限序列虽然可以无限迭代下去，但是通常我们会通过`takewhile()`等函数根据条件判断来截取出一个有限的序列：

  ```python
  >>> natuals = itertools.count(1)
  >>> ns = itertools.takewhile(lambda x: x <= 10, natuals)
  >>> list(ns)
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  ```

- `chain()` 可以把一组迭代对象串联起来，并形成一个更大的迭代器

  ```python
  >>> for c in itertools.chain('ABC', 'XYZ'):
  ...     print(c)
  # 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'
  ```

- `groupby()`把迭代器中相邻的重复元素挑出来放在一起：

  ```python
  >>> for key, group in itertools.groupby('AAABBBCCAAA'):
  ...     print(key, list(group))
  ...
  A ['A', 'A', 'A']
  B ['B', 'B', 'B']
  C ['C', 'C']
  A ['A', 'A', 'A']
  ```

  我们还可以设定挑选的规则，比如可以设定大小写不敏感，大小写字母都分在同一个组里面

  ```python
  >>> for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
  ...     print(key, list(group))
  ...
  A ['A', 'a', 'a']
  B ['B', 'B', 'b']
  C ['c', 'C']
  A ['A', 'A', 'a']
  ```

  

### contextlib

+ 并不是只有文件操作的时候才能用 `with .. as ..` ，事实上对于任何对象，只要正确实现了上下文管理，都可以使用 `with` 。

  + 上下文管理是通过`__enter__`和`__exit__`这两个方法实现的

    ```python
    class Query(object):
    
        def __init__(self, name):
            self.name = name
    
        def __enter__(self):
            print('Begin')
            return self
        
        def __exit__(self, exc_type, exc_value, traceback):
            if exc_type:
                print('Error')
            else:
                print('End')
        
        def query(self):
            print('Query info about %s...' % self.name)
    ```

+ `__enter__()` 和 `__exit__()` 仍然很繁琐，因此可以使用 `@contextmanager` 这个装饰器来简化代码。

+ `@contextmanager`这个decorator接受一个generator，用`yield`语句把`with ... as var`把变量输出出去，然后，`with`语句就可以正常地工作了：

  ```python
  from contextlib import contextmanager
  
  class Query(object):
  
      def __init__(self, name):
          self.name = name
  
      def query(self):
          print('Query info about %s...' % self.name)
  
  @contextmanager
  def create_query(name):
      print('Begin')
      q = Query(name)
      yield q
      print('End')
  ```

  ```python
  with create_query('Bob') as q:
      q.query()
  ```

  如果我们想在某段代码执行前后自动执行特定代码，也可以用 `@contextmanager` 这个装饰器实现。如下

  ```python
  @contextmanager
  def tag(name):
      print("<%s>" % name)
      yield
      print("</%s>" % name)
  
  with tag("h1"):
      print("hello")
      print("world")
  
      
  # 输出如下
  <h1>
  hello
  world
  </h1>
  ```

  代码的执行顺序是：

  1. `with`语句首先执行`yield`之前的语句，因此打印出`<h1>`；
  2. `yield`调用会执行`with`语句内部的所有语句，因此打印出`hello`和`world`；
  3. 最后执行`yield`之后的语句，打印出`</h1>`。

  因此，`@contextmanager`让我们通过编写generator来简化上下文管理。



## 第三方库

### chardet

+ ```python
  >>> data = '离离原上草，一岁一枯荣'.encode('gbk')
  >>> chardet.detect(data)
  {'encoding': 'GB2312', 'confidence': 0.7407407407407407, 'language': 'Chinese'}
  ```

  `chardet.detect(data)` 可以获取 `data` 的字符编码、检测正确概率和判断其语言。不过 `language` 字段对应的可能是空。

  > `gbk` 字符集是 `gb2312` 字符集的超集，两者是同一种编码

### psutil

+ `psutil.test()` 可以模拟出 `ps` 命令的效果

  





## 其他

+ `try ... except ... else`

+ `python -m json.tool demo.json`
+ ![image-20200911082142534](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200911082142534.png)

+ 如果需要禁止函数修改列表，可以通过 `function_name[list_name[:]]` 来达到目的，这样函数所做的任何修改都只影响副本而不会影响原件。

+ 要删除一个列表中特定下标的元素可以使用 `del a[下标]`

+ 空字符串是 `True`

+ `random.choice()` 从一个list中随机挑选元素

+ 将 logging 的 error 方法的 `exc_info` 参数设置为 `True` 可以打印出 Traceback 错误堆栈信息。

  ```python
  logging.error('error occurred while scraping %s', url, exc_info=True)
  ```

  