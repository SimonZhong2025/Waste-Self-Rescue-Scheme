#coding:utf-8
'''
循环中的关键字
continue:结束本轮循环，继续下一轮
break:结束当前这个循环(整个for循环或while循环)
'''
m = 1
while(m<10):
    m=m+1
    if(m==5):
        continue#结束本轮循环，后面的代码不会执行,跳到下一次循环
    else:
        print(m)

n = 1
while(n<10):
    n=n+1
    if(n==5):
        break #结束整个循环(这里是这个while循环)
    else:
        print(n)
