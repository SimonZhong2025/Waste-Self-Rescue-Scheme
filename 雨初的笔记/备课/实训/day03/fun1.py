#coding:utf-8
def add(a,b): #a,b为形参(形式参数)
    c = a+b   #方法体
    return c  #返回值  返回a+b  有返回值的方法  #传入两个参数，返回他们的和
c = add(1,2) #方法的调用  这里的1,2是实参，实际的参数
print(c)

def add2(a,b):
    c = a+b
    print(c) #传入两个参数，打印他们的和
add2(1,2)