+ `LOBYTE` 和 `HIBYTE` 是两个宏，分别用来取一个32bit的数据的低16bit和高16bit

+ 父类子类

  + 父类指针可以用来指向子类对象，因为其指针指向的都是该对象首地址的位置。

  ![无法加载请爬梯子](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/20200717195728.png)

  + 但是如果是子类特有的成员就不能用父类指针来使用了，因为编译器只知道这是个父类的指针，父类里面没有子类特有的成员。

    ![无法加载请爬梯子](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/20200717200325.png)

  + 最好永远不要像这样试图将一个父类类型的指针强转为子类指针。因为编译器不知道这个东西是一个父类对象，它会认为是一个子类对象。而这会导致如果试图访问这个指针里面的子类成员并不会报错，但是这个父类对象里面并没有子类成员，于是越界了，出现不可预知的错误。

    ![无法加载请爬梯子](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/20200717200626.png)



