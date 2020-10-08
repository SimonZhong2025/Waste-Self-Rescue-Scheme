#coding:utf-8
'''
Python支持四种数字类型 int、float、boolean、complex(复数)
Python3中只有一种整数类型，int型
'''
a = 1
#通过id()方法，返回对象的唯一标识符(地址)
print(id(a))
#数字类型是不可变的
a = 2
print(id(a))
b = 3.14
#del 可以删除变量     del a,b,c
#del a,b    删除变量后，再调用会报错，变量未定义
print(b)
#boolean类型        Ture=1   False=0   是关键字，但是也可以运算
c = True
if(c):#    if(要判断的条件)
   print(a+c) 
#复数类型
d = 4+3j
#type() 得到的是变量的类型  有返回值的方法
print(type(d))
#思考:如果a=2  b=2  c=2  地址一样么？
e = 2
f = 2
#内存中没有变量指向数字2时，2不存在，一旦有变量值等于2，内存中开辟一块空间放2，后面再有变量等于2，是同一个
print(id(a),id(e),id(f))