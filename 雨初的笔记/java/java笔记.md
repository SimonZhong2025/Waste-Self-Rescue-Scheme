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

+ ![image-20201028094659829](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201028094659829.png).

+ 加上`@Override`可以让编译器帮助检查是否进行了正确的覆写。希望进行覆写，但是不小心写错了方法签名，编译器会报错。

+ 把一个方法声明为`abstract`，表示它是一个抽象方法，本身没有实现任何方法语句。因为这个抽象方法本身是无法执行的，所以，`Person`类也无法被实例化。编译器会告诉我们，无法编译`Person`类，因为它包含抽象方法。

+ 实际上，确切地说，`private`访问权限被限定在`class`的内部，而且与方法声明顺序*无关*。推荐把`private`方法放到后面，因为`public`方法定义了类对外提供的功能，阅读代码的时候，应该先关注`public`方法：



+ 一个文件里面只能有一个公共类

+ `JRE` 就是 `java runtime environment`
+ `byte` 是一个字节
+ `long` 是 **8个字节** 。
+ `for (int x : a)` 这样也可以修改变量，和 `c++11` 里面的不太一样。
+ `final int` 和 **C++** 里面的 `const int` 差不多。
+ 二维数组要用 `.deeptostring` 才能得到





### 字符串

![image-20201030152728286](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201030152728286.png)

+ `.substring` 方法左闭右开

+ ![image-20201030153049630](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201030153049630.png)

  比较值而不是比较这两个字符串指向是否是一个地址。

+ `StringBuilder` 是可以写的。但不支持多线程。 `StringBuffer` 则可以支持多线程。

+ ![image-20201030154543275](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201030154543275.png)

+ `StringBuffer` 只能用 `append` 往后加数据。



### 面向对象

![image-20201030192004773](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201030192004773.png)

+ 在类里面可以赋初始值

+ 不像C++，在java中每个数据成员前面都要加上其访问限制。

+ JAVA中也有类似C++析构函数的功能

  ![image-20201030193130768](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201030193130768.png)

+ ![image-20201030193111288](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20201030193111288.png)

+ 在java中生成对象必须是用 `new` 。

  ![image-20201030200604204](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20201030200604204.png)

  这样是不行的。
  
+ ![image-20201030201441666](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20201030201441666.png)

+ 内部类不能有静态成员。

+ 静态类只能访问外部类的静态成员。

+ 外部类可以访问内部类的私有成员。

+ 接口只包含**常量和抽象方法**

+ `abstract` 类中也可以有非 `abstract` 方法，接口不可以。

+ 接口中默认的访问控制符都是**public**

![image-20201030210459792](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20201030210459792.png)

