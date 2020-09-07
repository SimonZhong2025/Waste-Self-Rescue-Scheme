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

+ **定义默认参数要牢记一点：默认参数必须指向不变对象！** 如果将默认参数设置为一个列表list，那么每次传入的参数都会被认为是下一次传入的默认参数。