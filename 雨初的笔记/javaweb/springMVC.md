+ `springMVC` 能够创建对象，放入到容器中（springMVC容器），springMVC中放的是控制器对象。

+ ![image-20210531192215000](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master//image-20210531192215000.png)

+ ![image-20210531193303813](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master//image-20210531193303813.png)

+ ![image-20210531193525564](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master//image-20210531193525564.png)

+ ![image-20210531195558430](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master//image-20210531195558430.png)

+ ![image-20210531200503014](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master//image-20210531200503014.png)

+ ![image-20210531210912343](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master//image-20210531210912343.png)

+ 

+ 当配置了视图解析器后，可以使用逻辑名称（文件名），指定视图。框架会使用视图解析器的 `前缀 + 逻辑名称 + 后缀` 组成完整路径。这里就是字符串连接操作。

  ![image-20210531233909133](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master//image-20210531233909133.png)

+ ![image-20210531235355239](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master//image-20210531235355239.png)

  这样可以设置多个界面
  
+ 处理器方法的形参名和请求中的参数名必须一致，同名的请求参数赋值给同名的形参。

+ 如果不确定某个 `int` 类型的参数有没有，可以将其换成包装类型 `Integer` 。其也可以接受空值，也就不会产生400错误。

+ 为了不要每一个方法都加上 `setCharacterEncoding` ，可以在过滤器中设置字符编码。

+ ![image-20210601103703482](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master//image-20210601103703482.png)

+ 对于字符编码设置的过滤器

  ![image-20210601104108272](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20210601104108272.png)

+ `@RequestParam` 这个注解可以解决请求中参数名和形参参数名不一致的问题。 `value` 表示请求中的参数名称，位置在处理器方法的形参定义的前面。 `require` 可以确定这个参数是否存在。如果是 `false` 的话这个参数可以有也可以没有，为 `true` 的话这个参数必须存在。

  ![image-20210601111031604](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master//image-20210601111031604.png)

  这样使用