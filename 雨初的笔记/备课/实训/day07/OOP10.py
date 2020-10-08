#coding:utf-8
'''
import Student #Student是模块名(文件名)
#stu1 = Student()
#print(Student.aaa)
'''
from Student import *  #就像是把整个文件CTRL+C过来
print(Student.stuCount)
print(Student.stuType)
stu1 = Student('张三',1000)
#print(stu1.name)
#print(aaa)
#调用展示self的方法 
stu1.showSelf()
stu1.showCount()
'''
从执行结果可以看出，self__class__指向类
self代表的是类的一个实例，代表对象本身的地址
self不是Python关键字，也可以换其他的
'''
