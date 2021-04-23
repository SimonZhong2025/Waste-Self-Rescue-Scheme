+ 在写完 `servlet` 的类之后，tomcat并不知道要如何访问这个类，需要在 `web.xml` 里面进行配置。

+ 在 `servlet` 中使用全局变量有线程安全问题。而如果进行加锁的话对用户体验太差。因此一般不要在 `servlet` 中使用全局变量。

+ 如果只需要重写 `service` 方法的话可以让类 `extends`  `GenericServlet` 类。这个类把其他的方法都进行默认处理，只把 `service` 方法做了抽象。

+ 在 `doget` 里面

  ![image-20210421141248857](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master/image-20210421141248857.png)

+ ![image-20210421150928914](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master/image-20210421150928914.png)

+ `session` 和 `cookie` 使用

  ![image-20210422145437738](https://cdn.jsdelivr.net/gh/smallzhong/new-picgo-pic-bed@master/image-20210422145437738.png)

+ 直接用 `tomcat` 启动服务的话 `tomcat` 目录里面的 `work` 目录不会被删除。关闭服务后 `session` 会被序列化到 `.ser` 文件中，重新启动后会重新反序列化到内存中，保证 `session` 不会因为服务器的重启而丢失。