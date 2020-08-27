+ `fseek(fp, 0, SEEK_END)` 然后 `ftell(fp)` 可以得出这个文件的大小

  ![无法加载请爬梯子](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/20200706102237.png)

  > 如果流以二进制模式（b）打开，则ftell获得的值是距文件起始的字节数
  >
  > 如果流以文本模式打开，则此函数的返回值是未指定的，而且仅若作为 std::fseek 的输入才有意义。

  

+ 先是转换为一个 `PWORD` （指向WORD的指针），然后再取其内容。这样做是为了取得这个指针指向的内容的头两个字节，用来判断是否为有效的MZ头。（ `pileBuffer` 是一个 `LPVOID` ）

  ![无法加载请爬梯子](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/20200706102948.png)

  > 这里要 `*((PWORD)pFileBuffer)` 的原因是取值运算符 `*` 和强制类型转换运算符 `(type)` 的运算符优先级是同级的，结合方向从右到左，所以要多加上一个括号

+ 用指针的时候要养成 **先转型** 的好习惯，因为有时候如果忘了这个指针是什么类型的，但是后面又加上一个数，很可能会无法达到预期的效果。（先转成一个普通的指针，后面加偏移就是往后偏移多少个字节）

  ![无法加载请爬梯子](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/20200706155849.png)

  

+ 利用 `sprintf` 可以格式化字符串，比如将10进制的数字转换为16进制。另外需要注意的是 `itoa` 并不是一个标准函数，在linux平台下好像就不能使用。尽量不要用这个函数。

+ 头文件不要定义任何变量，那是非常业余的行为。 [C语言多文件共用全局变量](https://www.cnblogs.com/invisible2/p/6905892.html) 。可以在头文件中用 `extern` 来声明变量。

+ `sprintf` 会自动在字符串后面加上 `\0` ，所以不用太担心。（但是我还是喜欢 `memset` 一下怎么破。。）

  ![image-20200805213801324](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20200805213801324.png)

+ 多文件编程的时候还是尽量不要在两个文件中使用同名的函数吧。。在导入表查看的 `cpp` 文件中使用一个和节表查看 `cpp` 文件中同名的函数，最后居然跳到了节表查看的那个 `cpp` 里面的函数。。说实话这波没怎么看懂，就算是重载也应该是在同一个文件里面找函数吧。。不过算了，反正记得不要在多个文件中使用同名函数就对了。

  >很明显，所有未加static修饰的函数和全局变量具有全局可见性，其他的源文件也能够访问。static修饰函数和变量这一特性可以在不同的文件中定义同名函数和同名变量，而不必担心命名冲突。如果要让这个函数只有局部可见性，就要给它加上 `static`
  >
  >[static](https://blog.csdn.net/FreeApe/article/details/50979425)

+ 出现编码问题的时候这样做

  ```cpp
  #ifdef _UNICODE
  #define _tprintf wprintf
  #else
  #define _tprintf printf
  #endif
  ```

+ `setlocale` 好像是用来解决编码问题的。

+ ```cpp
  #ifdef _UNICODE
  #define _tprintf wprintf
  #else
  #define _tprintf printf
  #endif
  
  _tprintf(TEXT(""),...);
  ```

  这样可以写出兼容的代码。

  在VC6中 `TEXT("")` == `("")`

  而在VS中  `TEXT("")` == `("")`

+ `typedef` 一种函数指针的方法 **typedef  返回类型(*新类型)(参数表)**