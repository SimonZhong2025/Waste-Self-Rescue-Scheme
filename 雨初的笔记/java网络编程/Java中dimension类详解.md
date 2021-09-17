dimension - Java的一个类
        dimension是Java的一个类，封装了一个构件的高度和宽度，这个类与一个构件的许多属性具有相关性，因此在Component类中定义多个与之有关的方法，LayoutManager接口也与一个Dimension对象有关联。Dimension类的高度和宽度值是一个整数，表明有多少个像素点。

与Dimension类相关方法：getSize()和setSize(Dimension size)。分别用来获得和设置方格的大小。

       下面介绍类dimension的构造方法。

构造函数
Dimension()	
初始化的新实例Dimension类使用的默认值。

Dimension(String)	
初始化的新实例Dimension类使用的名称。

Dimension(String, String)	
初始化的新实例Dimension类使用的名称和标识符。

方法
（以下的方法常用的会用符号标识，注意侧重点）

AddToContainer(IContainer) AddToContainer(IContainer) AddToContainer(IContainer)	
将 ModelComponent 对象添加到指定的容器。 Adds a ModelComponent object to the specified container.

(Inherited from ModelComponent)
AfterInsert(Int32) AfterInsert(Int32) AfterInsert(Int32)	
在添加指定的索引后，显示 ModelComponent 对象。 Displays a ModelComponent object after added to the specified index.

(Inherited from ModelComponent)
AfterMove(Int32, Int32) AfterMove(Int32, Int32) AfterMove(Int32, Int32)	
在移动指定的索引后，显示 ModelComponent 对象。 Displays a ModelComponent object after moving to the specified index.

(Inherited from ModelComponent)
AfterRemove(ModelComponentCollection) AfterRemove(ModelComponentCollection) AfterRemove(ModelComponentCollection)	
删除 ModelComponentCollection 对象后，显示 ModelComponent。 Displays a ModelComponentCollection after a ModelComponent object is removed.

(Inherited from ModelComponent)
BeforeRemove(Boolean) BeforeRemove(Boolean) BeforeRemove(Boolean)	
清除前删除 ModelComponent对象。 Removes the ModelComponent object before the cleanup.

(Inherited from ModelComponent)
CanProcess(ProcessType) CanProcess(ProcessType) CanProcess(ProcessType)	
向服务器发送一个处理类型，并指示对于 Dimension 对象是否可执行该处理类型。 Sends a processing type to the server and indicates whether that process type can take place for the Dimension object.

Clone() Clone() Clone()	
创建 Dimension 对象的全新完整副本。 Creates a new, full copy of a Dimension object.

Clone(Boolean) Clone(Boolean) Clone(Boolean)	
创建 MajorObject 对象的新副本。 Creates a new copy of the MajorObject object.

(Inherited from MajorObject)
CopyTo(Dimension) CopyTo(Dimension) CopyTo(Dimension)	
副本Dimension到指定的对象的对象。 Copies a Dimension object to the specified object.

CopyTo(MajorObject, Boolean) CopyTo(MajorObject, Boolean) CopyTo(MajorObject, Boolean)	
将该对象复制到指定目标。 Copies the object to the specified destination.

(Inherited from ProcessableMajorObject)
CopyTo(ModelComponent) CopyTo(ModelComponent) CopyTo(ModelComponent)	
副本ModelComponent到指定的对象的对象。 Copies a ModelComponent object to the specified object.

(Inherited from ModelComponent)
CopyTo(NamedComponent) CopyTo(NamedComponent) CopyTo(NamedComponent)	
副本NamedComponent到指定的对象的对象。 Copies a NamedComponent object to the specified object.

(Inherited from NamedComponent)
Drop() Drop() Drop()	
删除当前对象并更新服务器。 Removes current object and updates server.

(Inherited from MajorObject)
Drop(DropOptions) Drop(DropOptions) Drop(DropOptions)	
使用指定选项删除当前对象并更新服务器。 Removes current object and updates server using specified options.

(Inherited from MajorObject)
Drop(DropOptions, XmlaWarningCollection) Drop(DropOptions, XmlaWarningCollection) Drop(DropOptions, XmlaWarningCollection)	
使用指定选项删除当前对象并更新服务器。 Removes current object and updates server using specified options. 对指定的 warnings 对象返回了由删除操作引发的警告。 Warnings resulting from drop operation are returned on the specified warnings object.

(Inherited from MajorObject)
Drop(DropOptions, XmlaWarningCollection, ImpactDetailCollection) Drop(DropOptions, XmlaWarningCollection, ImpactDetailCollection) Drop(DropOptions, XmlaWarningCollection, ImpactDetailCollection)	
使用指定选项删除当前对象并更新服务器。 Removes current object and updates server using specified options. 对指定的 warnings 变量返回了由删除操作引发的警告，并且对指定的 impactResult 变量返回了操作中受影响对象的结果。 Warnings resulting from drop operation are returned on the specified warnings variable and results for affected objects in operation are returned on specified impactResult variable.

(Inherited from MajorObject)
Drop(DropOptions, XmlaWarningCollection, ImpactDetailCollection, Boolean) Drop(DropOptions, XmlaWarningCollection, ImpactDetailCollection, Boolean) Drop(DropOptions, XmlaWarningCollection, ImpactDetailCollection, Boolean)	
使用指定选项删除当前对象并更新服务器。 Removes current object and updates server using specified options. 对指定的 warnings 变量返回了由删除操作引发的警告，并且对指定的 impactResult 变量返回了操作中受影响对象的结果。 Warnings resulting from drop operation are returned on the specified warnings variable and results for affected objects in operation are returned on specified impactResult variable.

(Inherited from MajorObject)
GetCreateReferences(Hashtable, Boolean, Boolean) GetCreateReferences(Hashtable, Boolean, Boolean) GetCreateReferences(Hashtable, Boolean, Boolean)	
获取 Hashtable 以创建引用。 Gets a Hashtable to create references.

(Inherited from MajorObject)
GetDependents(Hashtable) GetDependents(Hashtable) GetDependents(Hashtable)	
将挖掘结构和后续依赖项添加到指定Hashtable。 Adds the mining structures and subsequent dependents to the specified Hashtable.

GetDropDependents(Hashtable, Hashtable) GetDropDependents(Hashtable, Hashtable) GetDropDependents(Hashtable, Hashtable)	
获取删除依赖关系。 Gets the drop dependents.

(Inherited from MajorObject)
GetReferences(Hashtable, Boolean) GetReferences(Hashtable, Boolean) GetReferences(Hashtable, Boolean)	
获取该维度引用的对象。 Gets the objects that the dimension references.

GetUpdateOverwrites(Boolean) GetUpdateOverwrites(Boolean) GetUpdateOverwrites(Boolean)	
获取覆盖更新的 Hashtable 的 MajorObject 对象。 Gets the Hashtable object that overwrites the updated MajorObject.

(Inherited from MajorObject)
Process() Process() Process()	
进程ProcessableMajorObject。 Processes the ProcessableMajorObject.

(Inherited from ProcessableMajorObject)
其实上面的方法大部分都用不到，需要的时候可以查阅

下面以一个例子来简单使用一下介绍一下dimension的使用

（使用一个远程控制的人工智能程序来描述（仅部分代码，加粗倾斜部分代码为使用实例））

package zzh;

import java.awt.AWTException;
import java.awt.Dimension;
import java.awt.Rectangle;
import java.awt.Robot;
import java.awt.Toolkit;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;

public class LocationScreen {
    public static void main(String[] args) {
        System.out.println("这是一个请求远程控制桌面的人工智能程序");
        //询问框
        int choic = JOptionPane.showConfirmDialog(null,"请求控制对方电脑?","私人专属定制",JOptionPane.YES_NO_OPTION);
        //返回值为什么是int，
        if(choic == JOptionPane.NO_OPTION){
            return;
        }
        //输入IP地址和端口号，IP就是找到是那台电脑，而端口号是确定那一台电脑
        JOptionPane.showInputDialog("请输入IP地址和端口号","127.0.0.1:20000");
        //初始化窗口
        JFrame jFrame = new JFrame("远程监控");
        jFrame.setSize(500,600);
        jFrame.setVisible(true);
        jFrame.setAlwaysOnTop(true);
        jFrame.setLocationRelativeTo(null);
        jFrame.setDefaultCloseOperation(jFrame.EXIT_ON_CLOSE);
        //定义一个方法获取本机的操作系统
        Toolkit kt = Toolkit.getDefaultToolkit();
        //目的是获取屏幕的尺寸，毕竟电脑型号不一样
        Dimension dm = kt.getScreenSize();
        
       //这行代码和下面的代码实现效果是一样的      
    
        System.out.println(dm.getwidth(),dm.getheight());
       //不过是一个调用了具体的方法       
    
        System.out.println(dm);
        //设置一个显示的内容
        JLabel jLabel = new JLabel();
        jFrame.add(jLabel);
        
        //创建一个机器人
        try {
            Robot robot = new Robot();
            
            //指定坐标，目的是获取整个电脑界面的图片（视频就是一帧帧的图片）
            new Rectangle(jFrame.getWidth(), 0, (int)dm.getWidth()-jFrame.getWidth(), (int)jFrame.getHeight());
        } catch (Exception e) {
            e.printStackTrace();
        }
        
    }
}


具体方法

​               

​              

关于具体实现可以参照API文档，这里不再赘述。
