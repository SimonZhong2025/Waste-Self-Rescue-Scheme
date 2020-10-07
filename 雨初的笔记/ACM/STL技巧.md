+ 判断一个 `map` 里面是否有某个元素

  ![image-20201003113234799](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20201003113234799.png)

+ 遍历 `map` 的时候可以用 `it->first` 和 `it->second` 分别取得键和值

  ![image-20201003120339377](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20201003120339377.png)

+ `find` 可以判断一个 `vector` 的某个区间里面有没有某个元素。

  ![image-20201006142135139](https://cdn.jsdelivr.net/gh/smallzhong/picgo-pic-bed@master/image-20201006142135139.png)

  如果 `find` 没有找到要找的元素则返回 `last`

+ `set` 去重并升序排列的， `multiset` 升序但不去重。

+ 要想知道一个 `set` 里面是否有某个元素，可以用 `s.count()` 也可以用 `s.find() != s.end()` 来判断