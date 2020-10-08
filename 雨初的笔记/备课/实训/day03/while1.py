#coding:utf-8
#判断while后面的表达式是否为真,为真则执行循环体
'''
i = 1
while(i<10):
    print(i)
    i=i+1
'''
'''
j = 1
boo = True  #用来标识某件事是否发生的变量，一般加上is   isRain  isPass
while boo:
    print(j)
    j=j+1
    if(j>10):
        boo = False
'''
#while实现 1-100以内的偶数和
i = 0
su =0#和
while(i<101):
    su = su+i
    i+=2    #i=i+2
print('1-100以内偶数的和',su)





