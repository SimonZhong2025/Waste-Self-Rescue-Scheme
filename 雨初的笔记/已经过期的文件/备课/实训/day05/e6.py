#coding:utf-8
'''
在有多个异常发生时，捕获会按照try的代码块顺序进行
'''
a = 9
b = 0
try:
    print('我还想再加一个异常：' % c)
    s = a/b
    print('%d与%d相除的数为%d' % (a,b,s))
except SyntaxError as msg:
    print('这里有一个异常')   #捕获异常后，可以给一些提示
    print(msg)
except ZeroDivisionError as msg:
    print('除数不能为零的错误')
    print(msg)
except NameError as msg:
    print('变量未命名的错误')
    print(msg)
else:
    print('%d与%d相除的数为%d,没有错误' % (a,b,s))
finally:
    print('finally总会执行')
