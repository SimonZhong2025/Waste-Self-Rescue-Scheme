+ 比较电路交换、报文交换和分组交换的主要优缺点

  >正确答案：
  >
  >电路交换优点：延时可控，对于时间敏感的应用来说比较合适。缺点：不灵活，独占信道，建立电路连接需要多花时间
  >报文交换：优点：灵活，节点存储转发优点：延时过长
  >分组交换：灵活，不独占信道，因此高效，延时比报文交换小缺点：延时不可控
  
+ TCP和UDP的区别

  >1.TCP面向连接的运输层协议，UDP无连接 
  >
  >  2.TCP是可靠交付，UDP是尽最大努力交付 
  >
  >  3.TCP面向字节流，UDP面向报文 
  >
  >  4.TCP是点对点连接的，UDP一对一，一对多，多对多都可以 
  >
  >  5.TCP适合用于网页，邮件等，UDP适合用于视频，语音广播等

+ 试在下列条件下比较电路交换和分组交换。要传送的报文共x（bit）。从源点到终点共经过k段链路，每段链路的传播时延为d（s），数据率为b(b/s)。在电路交换时电路的建立时间为s(s)。在分组交换时分组长度为p(bit)，且各结点的排队等待时间可忽略不计。问在怎样的条件下，分组交换的时延比电路交换的要小？（要求列出简要计算步骤）

  >我的答案：
  >
  >由题意可知电路交换的时延计算公式为：t1 = s + x / b + k * d而分组交换的时延计算步骤如下：先算出一共有多少个分组： n = floor(x / p)则分组交换总时延t2 = k * d + n * p / b + (k - 1) * (p / b)则t2 < t1的时候分组交换的时延比电路交换的要小当 x >> p时，floor(x / p) ≈ x / p，则分组交换比电路交换时延小的条件为：( k - 1) * (p / b) < s 
  >
  >正确答案：
  >
  >电路交换总时延为：x/b+kd+s;分组交换中总时延：（x/p）(p/b)+ (p/b)(k-1)+kd=x/b+kd+(p/b)*(k-1);当s>(k-1)*(p/b)时，电路交换的时延比分组交换的时延大，当x>>p,相反。

+ 网络协议的三要素是什么？各自有什么含义？

  >语法：数据与控制信息的结构或格式 
  >
  >语义：需要发出何种控制信息，完成何种动作以及做出何种响应
  >
  >同步：即时间实现顺序的详细说明

+ 协议与服务有何区别？有何关系？

  >协议是水平的，服务是垂直的。两种之间的关系：协议的实现保证了能够向上一层提供服务。

+ 写出五层网络模型的各层的主要功能

  >物理层：如何在传输介质上传输数据比特流
  >
  >数据链路层：封装成帧和数据差错检测，信道管理
  >
  >网络层：**路径的查找**
  >
  >传输层：实现**不同进程之间的通信**
  >
  >应用层：定义各种应用进程的协议规则

+ 数据链路（即逻辑链路）与链路（即物理链路）有何区别？

  “电路接通了“和“数据链路接通了”的区别何在？

  >链路（即物理链路）：指的是从一个结点到相邻结点的一段物理线路（有线或无线），中间没有任何其他的交换结点。**物理层的链路，实现物理层的四大功能即机械特性，功能特性，电气特性和过程特性**
  >
  >数据链路（即逻辑链路）：指的是为了实现传送数据，必须有一些必要的通信协议来控制这些数据的传输。所以是逻辑上的。
  >
  >
  >
  >“电路接通了“和“数据链路接通了”的区别何在？
  >
  >“电路接通了“：链路通了，电路没问题，物理层没问题
  >
  >数据链路接通了：第二层的协议没有问题，数据链路层没有问题了。
  >
  >因此数据链路接通的基础是要电路接通。

+ 静态路由和动态路由有什么区别

  >正确答案
  >
  >静态路由是由管理员手工配置的，适合比较简单的网络或需要做路由特殊控制。而动态路由则是由动态路由协议自动维护的，不需人工干预，适合比较复杂大型的网络。
  >路由器能够自动地建立自己的路由表，并且能够根据实际实际情况的变化适时地进行调整。动态路由机制的运作依赖路由器的两个基本功能：对路由表的维护；路由器之间适时的路由信息交换。
  >
  >我的答案：
  >
  >动态路由的可拓展性要大大优于静态路由。在网络结构发生变化的时候动态路由可以自适应，但静态路由需要重新手动配置路由表。静态路由由管理员手工配置，适合简单的网络或者需要做路由特殊控制的网络。动态路由由动态路由协议自动维护，不需人工干预，适合比较复杂大型的网络。

+ 列出拥塞控制的四种方法：慢开始、__**拥塞避免**___、__**快重传**____、____**快恢复**__

+ 2、物理层的四大特性： __**过程特性**____、__**功能特性**____、**机械特性**_____、__**电气特性**____、

+ ![image-20210109230433705](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109230433705.png)

+ ![image-20210109170136356](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109170136356.png)

+ ![image-20210109170253338](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109170253338.png)

+ ![image-20210109171607554](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109171607554.png)

+ ![image-20210109172239710](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109172239710.png)

+ ![image-20210109172310917](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109172310917.png)

+ ![image-20210109183058315](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109183058315.png)

+ ![image-20210109183538764](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109183538764.png)

+ ![image-20210109183747702](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109183747702.png)

+ ![image-20210109183917780](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109183917780.png)

+ ![image-20210109190856509](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109190856509.png)

  这个子网地址可能是指子网号？

+ ![](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109191347339.png)

+ ![image-20210109191907948](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109191907948.png)

+ ![image-20210109192019339](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109192019339.png)

+ ![image-20210109192234774](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109192234774.png)

+ ![image-20210109192436312](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109192436312.png)

  王P186三种路由协议的比较

  >| RIP                  | OSPF               | BGP                  |
  >| -------------------- | ------------------ | -------------------- |
  >| 距离-向量            | 链路状态           | 路径-向量            |
  >| UDP                  | IP                 | TCP                  |
  >| 跳数最少             | 代价最低           | 较好、非最佳         |
  >| 和本节点相邻的路由器 | 网络中的所有路由器 | 和本节点相邻的路由器 |

+ ![image-20210109192900447](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109192900447.png)

+ ![image-20210109193128384](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109193128384.png)

+ ![image-20210109193542685](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109193542685.png)

+ ![image-20210109193900790](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109193900790.png)

+ ![image-20210109194107065](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109194107065.png)

+ ![image-20210109194129890](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109194129890.png)

+ ![image-20210109194915714](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109194915714.png)

+ ![image-20210109195350258](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109195350258.png)

+ ![image-20210109195614364](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109195614364.png)

+ ![image-20210109200805327](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109200805327.png)

+ ![image-20210109201004639](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109201004639.png)

+ ![image-20210109201022728](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109201022728.png)

+ **基带系统使用数字信号进行传输**

  ![image-20210109201129794](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109201129794.png)

+ 调制是数字信号转模拟信号，解调反之

+ ![image-20210109201255692](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109201255692.png)

+ ![image-20210109201455525](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109201455525.png)

+ ![image-20210109202400479](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109202400479.png)

+ ![image-20210109202449430](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109202449430.png)

+ ![image-20210109202611264](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109202611264.png)

  最后两个是 **白蓝、绿色**

+ ![image-20210109202716946](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109202716946.png)

+ ![image-20210109203015375](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109203015375.png)

+ ![image-20210109203054439](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109203054439.png)

+ ![image-20210109203953294](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109203953294.png)

+ ![image-20210109204204768](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109204204768.png)

+ ![image-20210109204225982](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109204225982.png)

+ ![image-20210109204517667](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109204517667.png)

+ ![image-20210109204703679](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109204703679.png)

+ ARPANET是1969

  ![image-20210109204913028](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109204913028.png)

+ ![image-20210109211229930](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109211229930.png)

+ ![image-20210109211333739](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109211333739.png)

+ ![image-20210109211320512](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109211320512.png)

+ ![image-20210109211522852](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109211522852.png)

+ 以传输层为界，**下三层为通信子网，传输层上为资源子网。**

+ ![image-20210109212310832](https://raw.githubusercontent.com/smallzhong/picgo-pic-bed/master/image-20210109212310832.png)

+ 