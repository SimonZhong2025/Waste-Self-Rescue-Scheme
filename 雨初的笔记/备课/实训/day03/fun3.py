#coding:utf-8
#动态参数
#a接收一个参数,剩下的参数形成一个元组tup,*接收一个元组
def add(a,*tup):
    c=0
    for i in tup:
        c=c+i
    return c+a
#print(add(10,1,2,5,6,7,8,9))  #10传给a，其他的形成元组tup
#还可以接收多个关键字，形成字典
def test1(name,age=18,**dic):
    print(name)
    print(age)
    print(dic)
#test1('tyy',20,sex='M',height='181cm',aaa=12)    
#test1('tyy',sex='M',height='181cm',aaa=12) 
#混搭使用  *tup前不能有默认参数，否则会把元组中的一个参数作为默认参数的值(默认参数就有值了) 
'''
def test2(a,b=10,*tup):
    print(b)
    c=0
    for i in tup:
        c=c+i
    return c-a-b
print(test2(1,2,10,11,12,13))  #希望b为默认值10 2,10,11,12,13形成元组
'''
def test2(a,*tup,b=10):
    print(b)
    c=0
    for i in tup:
        c=c+i
    return c-a-b
#print(test2(1,2,3,4,5))   #a的值为1   2,3,4,5形成元组  b为默认值10
#顺序：  位置参数，元组参数，默认参数，字典参数
def test3(name,age,*tup,sex='M',**dic):
    print(name)
    print(age)
    print(tup)
    print(sex)
    print(dic)
test3('tyy',20,'123','abcd','aaa',height='181cm',work='java')





    