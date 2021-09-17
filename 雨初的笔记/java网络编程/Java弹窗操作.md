Java弹窗操作
1、任务简介
本博客介绍两种Java弹窗操作的方法，第一个种是通过弹出对话框显示用户输入的信息，第二种是通过用户输入数字的不同打开不同的程序。

2、弹出对话框的操作
1）任务内容
编程实现一个命令窗程序，使得：
输入“A”则在屏上回显“Your input is A”
输入“我”则在屏上回显“Your input is 我”
等等。
输入ByeBye则退出程序.
特别提示：本系列任务共有三个，其余两个任务在《Java弹窗操作2》中。
2）任务代码
该程序使用JOptionPane类弹出对话框，具体代码如下：

```java
import java.util.Scanner;//导入java.util包下的Scanner类
import javax.swing.JOptionPane;//导入java.swing包下的JOptionPane类
public class Test1{//类名
    public static void main(String[] args){//程序主函数
        while(true){//定义死循环
            System.out.print("Please input:");//提示输入
            Scanner s=new Scanner(System.in);//创建scanner，控制台会一直等待输入，直到敲回车结束
            String str=s.nextLine();//将用户的输入转换为字符串形式
            if("ByeBye".equals(str)){//if语句的条件判断用户输入是否为ByeBye
                System.out.print("The process is over");//输出进程已结束
                System.exit(0);//关闭进程
            }else{
                //使用消息提示框输出信息
                JOptionPane.showMessageDialog(null, "You input is "+str, str, JOptionPane.PLAIN_MESSAGE);
            }   
        }
    }
}
```

3）运行结果
通过LICEcap截取的动态图如下：
![这里写图片描述](https://img-blog.csdn.net/20180523204517432?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xzeWxzeTcyNg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

3、通过命令打开程序的操作
1）任务内容
完成一个 java application应用程序，通过键盘输入1、2、3等值，输入1则调用运行windows记事本程序，输入2则调用运行windows画图程序……。
2）任务代码
我将该程序编为输入1则调用运行windows记事本程序，输入2则调用运行windows画图程序，输入3则调用啊哈C程序，输入4则调用QQ音乐程序（关于各个程序的具体路径需要自行设置，毕竟每台电脑中程序的路径大多不同），代码如下：

```java
import java.io.IOException;//导入java.io包下的OException类
import java.util.Scanner;//导入java.util包下的scanner类
public class Test2{//类名
    public static void main(String[] args) throws IOException {//程序主入口函数，抛出异常的声明
        while(true){
            System.out.print("Please input:");
            Scanner s=new Scanner(System.in);//创建scanner，控制台会一直等待输入，直到敲回车结束
            Runtime r=Runtime.getRuntime();//调用脚本命令，打开所需程序
            int i=s.nextInt();//用户可自行定义i的值
            switch(i){//指定switch语句表达式为变量i
            case 1:r.exec("notepad.exe");//当输入1时打开记事本
            break;//跳出该函数
            case 2:r.exec("mspaint.exe");//当输入2时打开画图
            break;//跳出该函数
            case 3:r.exec("C:\\啊哈C\\ahac.exe");//当输入3时打开啊哈c程序
            break;//跳出该函数
            case 4:r.exec("D:\\Program Files\\Tencent\\qqmusic\\QQMusic.exe");//当输入4时打开qq音乐程序
            break;//跳出该函数
            default:break;//若无常量满足表达式，则执行default后的语句
            }
        }
    }
}
```

3）运行结果
通过LICEcap截取的动态图如下：


4、总结
这些操作简单，但是对于初学者来说还是有一点难度的，我在刚接触这两个任务时也花了许多时间才完成程序，所以通过这篇博客给出代码并标明每一段代码的注释，希望能帮到更多的朋友，若有不足之处请大家指正。




