#coding:utf-8
#写一个减法的方法
def mul(a,b):
    if a<b:
        raise BaseException("我只是个异常而已！")
        return 0
    else:
        return a-b
#print(mul(1,3))
try:
    raise NameError('Hi')
except NameError:
    print('你真的有问题！')
    #raise
    