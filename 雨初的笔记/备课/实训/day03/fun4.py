#coding:utf-8
#位置参数   默认参数  *args  **kwargs
#位置参数， 默认参数
def func(a,b,sex='男'):
    print(a)
    print(sex)
#func(1,2)

#位置参数 *args 默认参数
def func2(a,b,sex='男',*tup):
    print(a,b)  #100,200
    print(sex)  #1
    print(tup)  #1,2,3,4,5
#func2(100,200,1,2,3,4,5)

#位置参数   默认参数  *args  **kwargs
'''
def func3(a,b,*tup,**dic,sex='男'):
    print(a,b)  #100,200
    print(sex)  #没有值，报错
    print(tup)  #1,2,3,4
func3(100,200,1,2,3,4,sex='女')
'''
def func4(a,b,*tup,sex='男',**dic):
    print(a,b)  #100,200
    print(sex)  #女
    print(tup)  #1,2,3,4
    print(dic) 
func4(100,200,1,2,3,4,sex='女',height='181cm',hobby='篮球')


