#coding:utf-8
#类的命名  class className(要继承的类名):
class Student:  #定义一个学生类
    '学生的基础类'   #类文档字符串，写一些关于类的简单描述
    #类变量，在所有的类的实例中共享
    stuCount = 0 #计算学生的总人数的变量  
    #类变量在类被加载时(只要提到了这个类)才会被创建
    #对象不被使用时，会被回收
    stuType = ['文科生','理科生','艺术生']  #提供给学生类的学生类型属性的选择
    '''
                构造方法（构造函数）:
                类在创建的时候一定会调用的方法
      self代表类的实例(对象)，在定义类的方法时是必须有的，但是不用主动传入参数
                  构造方法没有重载，？？？如何实现无参的构造方法？？？
    '''
    def __init__(self,name='无名',stuNo=9999):
        #实例变量要对象被创建才被创建
        self.name = name  #把参数中的name赋值给对象的name属性，self.name是实例变量
        self.stuNo = stuNo 
        Student.stuCount +=1  #每次实例化一个学生，都增加1
    #类的普通方法，与一般函数的区别，就是要把self作为第一个参数，表示某个类的实例
    
    #展示学生总数的方法
    def showCount(self):  
        print('总学生数为%d' % Student.stuCount)  #访问(调用类变量要通过类名.类变量)
    
    #展示学生的信息的方法
    def showStudentMes(self):
        #访问实例变量通过实例名.实例变量，在类定义的内部通过self表示当前的实例
        print('学生姓名:%s,学生学号:%d。' %(self.name,self.stuNo))
    #展示self的方法
    def showSelf(self):
        print(self) #展示对象的内存地址
        print(self.__class__) #展示对象的类名
#stu1 = Student()  #类的实例化 
#print(stu1.name)
    