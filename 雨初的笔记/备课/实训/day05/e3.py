#coding:utf-8
try:
    a = 2
    b = 0
    print(a/b)
except:
    print('出错了！！！！')
print('--------')
c = 10
d = 1
try:
    e = c/d
    print(e)
except ZeroDivisionError as err:
    print(err)
else:
    print('No error')
