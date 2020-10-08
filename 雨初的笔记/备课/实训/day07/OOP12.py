#coding:utf-8
#Python中的内置类属性
from Student import *
print('Student.__doc__:%s' %Student.__doc__) #类的文档字符串
print('Student.__name__:%s' %Student.__name__) #类名
print('Student.__module__:%s' %Student.__module__) #类定义所在的模块名
print('Student.__bases__:',Student.__bases__) #类的所有父类组成的一个元组
print('Student.__dict__:',Student.__dict__) #类的属性组成的一个字典，由类的数据属性组成