+ `yc_villagers` 表

  ```sql
  CREATE TABLE `yc_villagers` (
      `village` char(20) NOT NULL,
      -- 其属于哪个村庄
      `name` char(20) NOT NULL,
      `sex` char(3) NOT NULL CHECK(
          sex = '男'
          or sex = '女'
      ),
      `id` char(25) UNIQUE NOT NULL, -- 身份证号为主键且唯一
      `addr` char(100) NOT NULL,
      `phone_number` char(25) NOT NULL,
      PRIMARY KEY (`id`)
  ) ENGINE = InnoDB AUTO_INCREMENT = 10 DEFAULT CHARSET = utf8;
  ```

+ 插入数据 

  ```sql
  INSERT INTO `yc_villagers`
  VALUES (
          '村庄1',
          '钟雨初',
          '男',
          '8003119075',
          '南昌大学软件学院',
          '18070503122'
      ),
      (
          '村庄2',
          '张三',
          '女',
          '441231233123123131',
          '广东省阳江市江城区',
          '13474324857'
      );
  ```

+ `village_distance` 表

  ```sql
  CREATE TABLE `village_distances`(
      src CHAR(20) NOT NULL,
      dest CHAR(20) NOT NULL, 
      distance_kilo DOUBLE NOT NULL,
      FOREIGN KEY (src) REFERENCES yc_villagers(village) ON DELETE CASCADE ON UPDATE CASCADE, -- 级联删除
      FOREIGN KEY (dest) REFERENCES yc_villagers(village) ON DELETE CASCADE ON UPDATE CASCADE, -- 级联删除
      PRIMARY KEY (src, dest)
  );
  ```

+ `village_distance` 表中的数据

  ```sql
  INSERT INTO `village_distances`
  VALUES (
          '村庄1',
          '村庄3',
          12
      ),
      (
          '村庄3',
          '村庄1',
          12
      ),
      (
          '村庄3',
          '村庄2',
          32
      ),
      (
          '村庄2',
          '村庄3',
          32
      );
  ```


+ `village_pos` 表

  ```sql
  CREATE TABLE `village_pos`(
      x int NOT NULL, -- 村庄所在的x坐标
      y int NOT NULL, -- 村庄所在的y坐标
      village CHAR(20) NOT NULL, -- 村庄名
      -- 级联删除
      FOREIGN KEY (village) REFERENCES yc_villagers(village) ON DELETE CASCADE ON UPDATE CASCADE,
      -- 级联删除
      PRIMARY KEY (village)
  );
  ```

  数据

  ```sql
  INSERT INTO `village_pos`
  VALUES (
          2, 3, '村庄1'
      ),
      (
          6, 9, '村庄2'
      ),
      (
          15, 12, '村庄3'
      ),
      (
        31, 31, '村庄4'
      );
  ```
  
+ `villager_pos` 表

  ```sql
  CREATE TABLE `villager_pos`(
      x int NOT NULL, -- 村庄所在的x坐标
      y int NOT NULL, -- 村庄所在的y坐标
      name CHAR(20) NOT NULL, -- 村庄名
      -- 级联删除
      FOREIGN KEY (name) REFERENCES yc_villagers(nane) ON DELETE CASCADE ON UPDATE CASCADE,
      -- 级联删除
      PRIMARY KEY (name)
  );
  ```

  



### 笔记

+ ```java
  table.getRowCount();
  ```

  可以获取这个 `Jtable` 里面一共有多少行
  
+ 要往数据库里面插入数据的话可以使用这样的方法

  ```sql
  //3.create Statement
  String sql="insert into demo1student (name,age,score) values(?,?,?)";
          ps=connection.prepareStatement(sql);
          ps.setString(1,"Mary");
          ps.setInt(2,22);
          ps.setInt(3,99);
  
  //4.excuteUpdate
          int resultSet=ps.executeUpdate();
          if(resultSet>0){
          //如果插入成功，则打印success
          System.out.println("Sucess");
          }else{
  //如果插入失败，则打印Failure
          System.out.println("Failure");
          }
  ```

+ 弹出一个提示框

  ```java
  JOptionPane.showMessageDialog(null,
                          "您并未选中任何一行数据！", "错误", JOptionPane.INFORMATION_MESSAGE);
  ```

+ `java` 中 `trim` 方法可以去掉多余的符号，两端的空格和制表符、换行符等。

+ 对于选择的下拉列表

  ![image-20201212195214415](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201212195214415.png)

+ ![image-20201212201625396](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201212201625396.png)

+ ![image-20201213113609285](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201213113609285.png)

+ ![image-20201213161551577](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201213161551577.png)

+ 当Java程序启动的时候，实际上是启动了一个JVM进程，然后，JVM启动主线程来执行`main()`方法。在`main()`方法中，我们又可以启动其他线程。

+ 直接调用`Thread`实例的`run()`方法是无效的，要使用 `t.start()` 才能开启线程。

+ 一个线程还可以等待另一个线程直到其运行结束。例如，`main`线程在启动`t`线程后，可以通过`t.join()`等待`t`线程结束后再继续运行：`join(long)`的重载方法也可以指定一个等待时间，超过等待时间后就不再继续等待。

+ `volatile` 使用

  ![image-20201215115655994](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201215115655994.png)

+ 如何创建守护线程呢？方法和普通线程一样，只是在调用`start()`方法前，调用`setDaemon(true)`把该线程标记为守护线程：

+ 成员内部类可以无条件访问外部类的所有成员属性和成员方法（包括private成员和静态成员）。

+ `@Override` 掉 `paint` 方法就可以画出不同的东西

+ 设置边框可以用

  ```java
  j.setBorder(BorderFactory.createLoweredBevelBorder());
  ```

  来达到目的。

+ `g.setColor(new Color(255, 0, 0))` 可以用来设置填充的颜色。然后调用 `g.fillRect(0, 0, width / 2, width / 2)` 就可以填充出一个红色的矩形

+ 绘制几何图形的时候 `drawXXX` 表示只画线条， `fillXXX` 表示只填充。在做大作业的时候可以通过 `draw` 来画出边框线然后通过 `fill` 填充内部的颜色。

+ `draw` 要如果想要填充整个区域要缩小一个像素

  ![image-20201216193245176](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201216193245176.png)

  要改为 `g.drawRect(0, 0, width - 1, height - 1)` 。

+ 自己设定墙壁吧，然后在数据库中设定村庄所在的点，然后 `bfs`。

  

## TODO

- [ ] 表格的行距要设置一下。
- [x] 右键可以删除记录，删除了之后可以存到数据库中
- [ ] 要将表格中的内容设置为不可编辑
- [x] 往右键菜单里面加入一个修改数据
- [x] 要可以选择查询某个村庄的信息（ `select * from yc_villagers where village = ""` ）
- [ ] 展示查询的信息的时候要 `DESC` 。
- [ ] 把 `AfPanel` 修改一下改成自己的。
- [x] 加一个 `JComboBox` ，能选择展示不同的村庄的信息
- [x] 更新信息的时候 `JComboBox` 里面的信息也要更新
- [ ] `getSelectedItem` 
- [ ] 设计一张表，里面存放各村庄之间的距离
- [ ] 表格的样式必须得调整了
- [ ] 刷新的时候不能切换到全部村庄界面，这个bug要补上
- [ ] 村庄间的路是无向边，两个都要加进去
- [ ] 数据库里面一条路有两条记录，可以推到一个 `set` 里面防止表格中展示数据的时候重复。
- [ ] 往扶贫信息管理系统方向走
- [ ] 租数据库
- [x] 用 `graphics` 画
- [x] 改改改改distance，，改，，，人没了 `sql.*distance.*`
- [ ] 加加加加，，加加加 `check`
- [x] 加上登录界面
- [ ] 如果没有成功连接到数据库要报错
- [ ] 可以尝试把账号密码放到数据库中
- [ ] `issolving` 好像没用了
- [x] 增加一个按钮，可以显示搜索到的区域
- [x] 重新选择之后要可以自动清空才行
- [ ] 检测身份证号的时候加上正则
- [ ] 三次输错锁定，在数据库中进行

### 文档TODO

- [ ] 要在需求分析里面加对于数据库中表结构的说明
- [ ] 在文档中添加代码解释
- [ ] af，，不该用的。
- [ ] MAP要详解



### 亮点

![image-20201212192609186](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201212192609186.png)

+ 用到了 `try-catch`

  ![image-20201216090819465](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201216090819465.png)
  
+ ```
  this.setLocationRelativeTo(null);
  ```

  设置居中显示



### 踩到的坑

![image-20201213101723683](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201213101723683.png)

+ 死循环了

+ 级联删除

+ ![image-20201213213100556](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201213213100556.png)

  `vector` 不能用下标访问 
  
+ `setkeylistener` 后还要给 `panel` 加上 `requestFocus`

+ ![image-20201217151820711](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201217151820711.png)

  https://stackoverflow.com/questions/58604291/java-awt-queue-cannot-be-accessed-from-outside-package



### 看源码问题

![image-20201216181616428](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20201216181616428.png)

+ 使用 `MouseMotionListener` 来达到拖动鼠标画一块区域的效果

  https://blog.csdn.net/qq_29134495/article/details/51465457





### 问题

+ 接口是 **完善** 吗？---应该是实现吧