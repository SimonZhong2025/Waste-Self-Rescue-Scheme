Java Robot类使用指南
                                        ——Javee

Robot类用于为测试自动化、自运行演示程序和其他需要控制鼠标和键盘的应用程序生成本机系统输入事件。Robot 的主要目的是便于 Java 平台实现自动测试。

Java中使用Robot类时，需要导入java.awt包，如下：

```java
import java.awt.*;
```

Robot类和其他类实例化方法一样:

```java
//类名 对象名 = new 类名();
Robot robot = new Robot();
```

Robot类中常用的方法：

方法名

使用说明

使用实例

delay(n)

延迟电脑操作n毫秒，类似于Thread.sleep()

robot.delay(1000);

keyPress()

模拟手动按下电脑键盘上的某个键

robot.keyPress(KeyEvent.VK_SPACE); //按下空格键

keyRelease()

模拟手动松开电脑键盘上的某个键（与keyPress()对应，按下一个键必须松开这个键）

robot.keyRelease(KeyEvent.VK_SPACE);  //松开空格键

mouseMove(x,y)

将鼠标移动到指定的x,y位置

robot.mouseMove(300, 400);  //将鼠标移动到距离左边框300px，距离上边框400px的位置

mousePress()

按下鼠标上的某个键

robot.mousePress(InputEvent.BUTTON1_MASK); //按下左键

robot.mousePress(InputEvent.BUTTON2_MASK); //按下滚轴键robot.mousePress(InputEvent.BUTTON3_MASK); //按下右键

mouseRelease()

松开鼠标上的某个键

robot.mouseRelease(InputEvent.BUTTON1_MASK); //松开左键

robot.mouseRelease(InputEvent.BUTTON2_MASK); //松开滚轴键robot.mouseRelease(InputEvent.BUTTON3_MASK); //松开右键

注意事项：

在使用鼠标移动mouseMove()的时候，以为一些不可知因素，鼠标往往不能如我们所愿移动到指定的位置。所以在使用mouseMove()移动鼠标的时候，一般都和循环搭配使用，一般循环5~6次鼠标就可以移动到我们指定的位置，但以防万一可以稍微增加循环次数（10次左右），但不可循环次数太多，否则cpu运行效率会降低：

```java
//robot鼠标事件一个小栗子：
 
//
package auto_control;
 
import java.awt.*;
import java.awt.event.InputEvent;
 
/**
 * @Author Javee
 * @Date 2019/8/9 14:43
 * @Description 写一个脚本，打开电脑画板后，自动在画板上画一个奥运五环
 */
public class AutoPaint {
    public static void main(String[] args) throws AWTException {
        Robot robot = new Robot();
        robot.delay(3000); //运行代码后，暂停三秒，留够时间去打开电脑自带的画板，并点击形状里面的椭圆形
 
        //1111111111111111111111
        int i = 10;
        while (i-- > 0) {
            robot.mouseMove(400, 300);
        }
        robot.mousePress(InputEvent.BUTTON1_MASK);
        robot.delay(100);       //这里延迟0.1s，可以看到动态画的过程
        i = 10;
        while (i-- > 0) {
            robot.mouseMove(650, 550);
        }
        robot.mouseRelease(InputEvent.BUTTON1_MASK);
        robot.delay(1000);       //画完一个圆停止0.2s，否则因为计算机执行速度太快，看不到动态作图的过程
 
        //222222222222222222222
        i = 10;
        while (i-- > 0) {
            robot.mouseMove(0, 300);
        }
        robot.mousePress(InputEvent.BUTTON1_MASK);
        robot.mouseRelease(InputEvent.BUTTON1_MASK); //画完一个圆后在圆外面点一下鼠标，否则回拖动画的圆到下一个位置
        i = 10;
        while (i-- > 0) {
            robot.mouseMove(600, 300);
        }
        robot.mousePress(InputEvent.BUTTON1_MASK);
        robot.delay(100);       //这里延迟0.1s，可以看到动态画的过程
        i = 10;
        while (i-- > 0) {
            robot.mouseMove(850, 550);
        }
        robot.mouseRelease(InputEvent.BUTTON1_MASK);
        robot.delay(1000);       //画完一个圆停止0.2s，否则因为计算机执行速度太快，看不到动态作图的过程
 
        //3333333333333333333333333
        i = 10;
        while (i-- > 0) {
            robot.mouseMove(0, 300);
        }
        robot.mousePress(InputEvent.BUTTON1_MASK);
        robot.mouseRelease(InputEvent.BUTTON1_MASK); //画完一个圆后在圆外面点一下鼠标，否则回拖动画的圆到下一个位置
        i = 10;
        while (i-- > 0) {
            robot.mouseMove(800, 300);
        }
        robot.mousePress(InputEvent.BUTTON1_MASK);
        robot.delay(100);       //这里延迟0.2s，可以看到动态画的过程
        i = 10;
        while (i-- > 0) {
            robot.mouseMove(1050, 550);
        }
        robot.mouseRelease(InputEvent.BUTTON1_MASK);
        robot.delay(200);       //画完一个圆停止0.1s，否则因为计算机执行速度太快，看不到动态作图的过程
 
        //44444444444444444444444444
        i = 10;
        while (i-- > 0) {
            robot.mouseMove(0, 300);
        }
        robot.mousePress(InputEvent.BUTTON1_MASK);
        robot.mouseRelease(InputEvent.BUTTON1_MASK); //画完一个圆后在圆外面点一下鼠标，否则回拖动画的圆到下一个位置
        i = 10;
        while (i-- > 0) {
            robot.mouseMove(500, 425);
        }
        robot.mousePress(InputEvent.BUTTON1_MASK);
        robot.delay(100);       //这里延迟0.1s，可以看到动态画的过程
        i = 10;
        while (i-- > 0) {
            robot.mouseMove(750, 675);
        }
        robot.mouseRelease(InputEvent.BUTTON1_MASK);
        robot.delay(200);       //画完一个圆停止0.2s，否则因为计算机执行速度太快，看不到动态作图的过程
 
        //555555555555555555555555
        i = 10;
        while (i-- > 0) {
            robot.mouseMove(0, 300);
        }
        robot.mousePress(InputEvent.BUTTON1_MASK);
        robot.mouseRelease(InputEvent.BUTTON1_MASK); //画完一个圆后在圆外面点一下鼠标，否则回拖动画的圆到下一个位置
        i = 10;
        while (i-- > 0) {
            robot.mouseMove(700, 425);
        }
        robot.mousePress(InputEvent.BUTTON1_MASK);
        robot.delay(100);       //这里延迟0.1s，可以看到动态画的过程
        i = 10;
        while (i-- > 0) {
            robot.mouseMove(950, 675);
        }
        robot.mouseRelease(InputEvent.BUTTON1_MASK);
        robot.delay(200);       //画完一个圆停止0.2s，否则因为计算机执行速度太快，看不到动态作图的过程
 
 
    }
}
 
//当然，此代码还可以优化，有兴趣的朋友可以自己尝试优化一下代码，以减少代码量
```

下面再列举一两个robot键盘事件的小栗子:

```java
//这里我使用的是idea，所以有些快捷键可能不适用于其他编译器
package auto_control;
 
import java.awt.*;
import java.awt.event.KeyEvent;
 
/**
 * @Author Javee
 * @Date 2019/8/9 11:19
 * @Description 使用代码在一个新建的Java文件中写一句代码
 * public static void main(String[] args) {
 *     System.out.println("Hello world!");
 * }
 * 并运行
 */
public class AutoControl {
    public static void main(String[] args) throws AWTException {
        Robot robot = new Robot();
        robot.delay(5000);
        //先模拟输入主方法
        robot.keyPress(KeyEvent.VK_P);
        robot.keyRelease(KeyEvent.VK_P);
        robot.delay(100);
        robot.keyPress(KeyEvent.VK_S);
        robot.keyRelease(KeyEvent.VK_S);
        robot.delay(100);
        robot.keyPress(KeyEvent.VK_V);
        robot.keyRelease(KeyEvent.VK_V);
        robot.delay(100);
        robot.keyPress(KeyEvent.VK_M);
        robot.keyRelease(KeyEvent.VK_M);
 
        robot.delay(500);
        robot.keyPress(KeyEvent.VK_ENTER);
        robot.keyRelease(KeyEvent.VK_ENTER);
        robot.delay(100);
 
        //先模拟电脑输入sout按下回车得到System.out.println();
 
        robot.keyPress(KeyEvent.VK_S);
        robot.keyRelease(KeyEvent.VK_S);
        robot.delay(100);
        robot.keyPress(KeyEvent.VK_O);
        robot.keyRelease(KeyEvent.VK_O);
        robot.delay(100);
        robot.keyPress(KeyEvent.VK_U);
        robot.keyRelease(KeyEvent.VK_U);
        robot.delay(100);
        robot.keyPress(KeyEvent.VK_T);
        robot.keyRelease(KeyEvent.VK_T);
 
        robot.delay(500);
        robot.keyPress(KeyEvent.VK_ENTER);
        robot.keyRelease(KeyEvent.VK_ENTER);
        robot.delay(100);
 
        //在括号里面输入"Hello world!"
        robot.keyPress(KeyEvent.VK_SHIFT);
        robot.keyPress(KeyEvent.VK_QUOTE);
 
        robot.keyRelease(KeyEvent.VK_SHIFT);
        robot.keyRelease(KeyEvent.VK_QUOTE);
        robot.delay(100);
 
        robot.keyPress(KeyEvent.VK_SHIFT);
        robot.keyPress(KeyEvent.VK_H);
        robot.keyRelease(KeyEvent.VK_SHIFT);
        robot.keyRelease(KeyEvent.VK_H);
        robot.delay(100);
        robot.keyPress(KeyEvent.VK_E);
        robot.keyRelease(KeyEvent.VK_E);
        robot.delay(100);
        robot.keyPress(KeyEvent.VK_L);
        robot.keyRelease(KeyEvent.VK_L);
        robot.delay(100);
        robot.keyPress(KeyEvent.VK_L);
        robot.keyRelease(KeyEvent.VK_L);
        robot.delay(100);
        robot.keyPress(KeyEvent.VK_O);
        robot.keyRelease(KeyEvent.VK_O);
        robot.delay(100);
 
        robot.keyPress(KeyEvent.VK_SPACE);
        robot.keyRelease(KeyEvent.VK_SPACE);
        robot.delay(100);
 
        robot.keyPress(KeyEvent.VK_W);
        robot.keyRelease(KeyEvent.VK_W);
        robot.delay(100);
        robot.keyPress(KeyEvent.VK_O);
        robot.keyRelease(KeyEvent.VK_O);
        robot.delay(100);
        robot.keyPress(KeyEvent.VK_R);
        robot.keyRelease(KeyEvent.VK_R);
        robot.delay(100);
        robot.keyPress(KeyEvent.VK_L);
        robot.keyRelease(KeyEvent.VK_L);
        robot.delay(100);
        robot.keyPress(KeyEvent.VK_D);
        robot.keyRelease(KeyEvent.VK_D);
        robot.delay(100);
        robot.keyPress(KeyEvent.VK_SHIFT);
        robot.keyPress(KeyEvent.VK_1);
        robot.keyRelease(KeyEvent.VK_SHIFT);
        robot.keyRelease(KeyEvent.VK_1);
 
        //模拟手动运行
        robot.delay(1000);
        robot.keyPress(KeyEvent.VK_CONTROL);
        robot.keyPress(KeyEvent.VK_SHIFT);
        robot.keyPress(KeyEvent.VK_F10);
        robot.keyRelease(KeyEvent.VK_CONTROL);
        robot.keyRelease(KeyEvent.VK_SHIFT);
        robot.keyRelease(KeyEvent.VK_F10);
    }
}
```

再来一个栗子（信息轰炸器，适用于电脑版的QQ和微信等）：

```java
package auto_control;
 
import java.awt.*;
import java.awt.event.KeyEvent;
 
/**
 * @Author Javee
 * @Date 2019/8/11 19:54
 * @Description  一个简单的QQ/微信轰炸器
 *                 用法：把需要发送的信息先复制到电脑的粘贴板（Ctrl + C）,
 *                 再运行此代码，然后打开需要轰炸的对象聊天窗口，点击一下
 *                 输入区即可自动轰炸
 * */
public class Boom {
    public static void main(String[] args) throws AWTException {
        Robot robot = new Robot();// 创建Robot对象
 
        int times = 50; //轰炸的次数，可以自己修改
        int time = 500; //两次轰炸之间相隔的时间，单位为毫秒
 
        robot.delay(3000);// 延迟三秒，主要是为了预留出打开窗口的时间，括号内的单位为毫秒
 
        for (int j = 0; j < times; j++) {//循环次数
            // 以下两行按下了ctrl+v，完成粘贴功能
            robot.keyPress(KeyEvent.VK_CONTROL);
            robot.keyPress(KeyEvent.VK_V);
            robot.keyRelease(KeyEvent.VK_CONTROL);// 释放ctrl按键，像ctrl，退格键，删除键这样的功能性按键，在按下后一定要释放，不然会出问题。crtl如果按住没有释放，在按其他字母按键是，敲出来的回事ctrl的快捷键。
            robot.delay(time);// 延迟发送，不然会一次性全发布出去，因为电脑的处理速度很快，每次粘贴发送的速度几乎是一瞬间，所以给人的感觉就是一次性发送了全部。这个时间可以自己改，想几秒发送一条都可以
            robot.keyPress(KeyEvent.VK_ENTER);// 回车
            robot.keyRelease(KeyEvent.VK_ENTER);
        }
    }
}
```