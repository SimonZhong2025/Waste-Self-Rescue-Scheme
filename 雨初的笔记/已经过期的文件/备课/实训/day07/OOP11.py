#coding:utf-8
from Student import *
#实例化类
stu1 = Student('Tom',1001)
stu2 = Student('Jerry',1002)
#stu1.showCount()
#Student.__doc__类文档属性
print(Student.__doc__)
#如何访问类的属性和方法
#通过小数点 . 来访问属性和方法
stu1.showStudentMes()
stu2.showStudentMes()
print('学生总人数为:%d人。' %Student.stuCount)
#添加、删除、修改类的属性
stu1.age = 7    #添加一个'age'属性
print('Tom的年龄是%d岁。' %stu1.age)
stu1.age = 8
print('一年后,Tom的年龄是%d岁。' %stu1.age)
#del stu1.age  #删除一个属性
#print('Tom的年龄是%d岁。' %stu1.age)
'''
还可以通过函数的方式来访问属性
hasattr(obj,attr)  检查对象是否包含某个属性
getattr(obj,attr)  返回对象的某个属性值
setattr(obj,attr,value)  设置对象的属性值
delattr(obj,attr) 删除对象的属性
'''
print(hasattr(stu1,'age')) #如果存在'age'属性则返回True
print(getattr(stu1,'age')) #返回对象的某个属性的值
setattr(stu1,'age',9)  #设置对象的某个属性的属性值
print('Tom的年龄是%d岁。' %stu1.age)
delattr(stu1,'age') #删除属性
print(hasattr(stu1,'age'))