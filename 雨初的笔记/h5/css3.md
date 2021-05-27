+ `transform` 不会影响其他盒子的位置

+ ![image-20210526202729970](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master//image-20210526202729970.png)

  ![image-20210526203115450](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master//image-20210526203115450.png)

+ ![image-20210526203916155](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20210526203916155.png)

+ ![image-20210526210410210](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20210526210410210.png)

+ ![image-20210526211940507](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master//image-20210526211940507.png)

+ ![image-20210526212055794](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20210526212055794.png)

+ ![image-20210526212321180](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master//image-20210526212321180.png)

+ ![image-20210526223256218](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master//image-20210526223256218.png)

+ ![image-20210526223546077](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master//image-20210526223546077.png)

+ ![image-20210526223805875](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master//image-20210526223805875.png)

+ ![image-20210526223959691](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master//image-20210526223959691.png)

+ `relative ` (相对定位) 对象不可层叠、不脱离文档流，参考自身静态位置通过 top,bottom,left,right 定位，并且可以通过 `z-index` 进行层次分级。

+ `absolute` (绝对定位) 脱离文档流，通过 top,bottom,left,right 定位。选取其 **最近一个最有定位设置的父级对象** 进行绝对定位，如果对象的父级没有设置定位属性，absolute元素将以body坐标原点进行定位，可以通过z-index进行层次分级。

+ ![image-20210526224925009](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20210526224925009.png)\

  属性选择器

+ ![image-20210526225103086](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20210526225103086.png)

+ 如果想让热点图圈的发散速度刚开始快后来变慢，可以设置一个 `0%` 和一个 `70%` ，这样热点图发散起来就有速度的差别。

+ ![image-20210526225624484](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20210526225624484.png)

  这样可以在 `70%` 到 `100%` 的时候有淡出的效果。 `opacity` 从 `1` 到 `0` 。

+ 在写热点图中发散的圈圈的时候，如果想让三个圈圈有延时，不同时出现，而三个圈圈的主题代码使用同一个 `keyframe` ，那么可以通过给每一个圈圈单独设置 `animation-delay` 属性来让其触发的时间出现区别。

+ ![image-20210526230237271](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20210526230237271.png)

  在 `animation` 中如果不填 `animation-delay` 字段的值的话其默认为0，这时候如果如图进行 `animation-delay` 的设置的话 `.pulse2` 的属性会被忽略。因为其权重仅为10。如果想要防止这种情况可以加 `!important` 。

+ ![image-20210526230522693](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master//image-20210526230522693.png)

+ ![image-20210526231019793](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master//image-20210526231019793.png)

+ 元素可以添加多个动画，中间要用逗号分割。像下图这样使用

  ![image-20210526232346713](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20210526232346713.png)

+ 如果想停留在结束的状态则要设置 `forwards` 属性。这样动画结束之后就不会回到初始的状态，而是会停留在动画结束的状态。

### 3D

+ ![image-20210526233027974](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20210526233027974.png)

+ ![image-20210526233545286](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20210526233545286.png)

+ ![image-20210526233814827](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20210526233814827.png)

+ ![image-20210526234417129](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20210526234417129.png)

+ ![image-20210526234617150](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20210526234617150.png)

  透视是写在被观察元素的父盒子上的。而 `translateZ` 是写在被透视元素上面的。 `perspective` 本质上是指定当前观察者所处的位置，而 `translateZ` 是指定被观察的元素的位置。

+ ![image-20210527094554379](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20210527094554379.png)
+ ![image-20210527094702890](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20210527094702890.png)
+ ![image-20210527095225427](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20210527095225427.png)
+ ![image-20210527102415955](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20210527102415955.png)
+ 