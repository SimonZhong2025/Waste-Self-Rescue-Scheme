+ ![image-20210430173824095](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20210430173824095.png)

  这里注释掉的两行代码是不需要的。因为在 `com.mysql.jdbc.Driver` 里面其已经帮我们注册了驱动。

  ![image-20210430174302608](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20210430174302608.png)

+ 为了让多条语句全部执行成功后再提交，可以设置 `setAutoCommit(false)` 。这样可以取消自动提交。

  ![image-20210601210135431](C:\Users\雨初\AppData\Roaming\Typora\typora-user-images\image-20210601210135431.png)