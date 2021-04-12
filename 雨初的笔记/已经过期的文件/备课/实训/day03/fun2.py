#coding:utf-8
#普通参数
def add(a,b):
    return a+b
#print(add(1,2))#方法有几个参数就要放几个参数，多了少了都会报错 
#默认参数
def add2(a,b=4):  
    return a+b
#print(add2(3))  #只放一个参数，另一个参数用默认值
#print(add2(3,3)) #也可以放两个参数
#有默认值的形参要在没有默认值的形参后面
'''
def add3(a=3,b):
    return a+b
'''
#print(add3(2))  #2会给到形参a，所以形参b还是没有值
#还可以传入指定的形参的值
def minus(a,b): 
    return b-a
print(minus(b=5,a=1))  #传入了指定的形参的值
    