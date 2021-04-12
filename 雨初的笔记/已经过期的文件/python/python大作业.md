+ 要判断某个文件是否存在可以使用 `os.path.exists()`

  ```python
  import os
  os.path.exists(test_file.txt)
  #True
  
  os.path.exists(no_exist_file.txt)
  #False
  ```

+ 创建一个set要用 `set()` ，创建一个dict用 `{}`

+ 想判断字典中有没有某个key，可以使用字典的 `has_key()` 方法。

+ 如果 *ensure_ascii* 是 true （即默认值），输出保证将所有输入的非 ASCII 字符转义。如果 *ensure_ascii* 是 false，这些字符会原样输出。

+ python要删除一个文件可以用 `os` 里面的 `os.remove("aa.txt")`

+ 使用 `logging` 记录错误

+ `os.getcwd` 返回当前工作目录的字符串

+ 如果想要在局部定义一个全局变量，可以使用 `global` 关键字

  ```python
  x = 6
  def func():
      global x #定义外部的x
      x = 1
   
  func()
  print (x)
  #输出1
  ```

+ `@property` 装饰器下面的方法是外面访问里面的接口，实际存储数据的变量是加上一个下划线 `_` 的变量。











