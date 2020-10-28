+ JAVA**没有析构函数** ，类有构造方法，但没有析构方法。JAVA运行环境有垃圾回收机制，当一个类不再使用的时候JAVA会自动将其回收。

+ 提倡一个 **java原文件** 只写一个类。

+ JAVA不支持多重继承

+ Java使用`extends`关键字来实现继承：

+ 因此我们得出结论：如果父类没有默认的构造方法，子类就必须显式调用`super()`并给出参数以便让编译器定位到父类的一个合适的构造方法。

+ 从Java 15开始，允许使用`sealed`修饰class，并通过`permits`明确写出能够从该class继承的子类名称。

  例如，定义一个`Shape`类：

  ```
  public sealed class Shape permits Rect, Circle, Triangle {
      ...
  }
  ```

  上述`Shape`类就是一个`sealed`类，它只允许指定的3个类继承它

+ `instanceof`实际上判断一个变量所指向的实例是否是指定类型，或者这个类型的子类。如果一个引用变量为`null`，那么对任何`instanceof`的判断都为`false`。

+ ![image-20201028094659829](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed/image-20201028094659829.png).

+ 加上`@Override`可以让编译器帮助检查是否进行了正确的覆写。希望进行覆写，但是不小心写错了方法签名，编译器会报错。

+ 把一个方法声明为`abstract`，表示它是一个抽象方法，本身没有实现任何方法语句。因为这个抽象方法本身是无法执行的，所以，`Person`类也无法被实例化。编译器会告诉我们，无法编译`Person`类，因为它包含抽象方法。

+ 实际上，确切地说，`private`访问权限被限定在`class`的内部，而且与方法声明顺序*无关*。推荐把`private`方法放到后面，因为`public`方法定义了类对外提供的功能，阅读代码的时候，应该先关注`public`方法：