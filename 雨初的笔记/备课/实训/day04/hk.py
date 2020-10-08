#coding:utf-8
'''
求两个数的最大公约数和最小公倍数

(11,7)
没有倍数关系
两个数如果有倍数关系，最大公约数是小的数
'''
'''
def yue(a,b):    
    temp = a%b    
    while temp!=0:
        a=b       
        b=temp  
        temp=a%b
    return b
def bei(a,b):
    return (a*b)//yue(a,b)
'''
def yue(a,b):
    re = 0#用来存放最大公约数
    c = a #c表示小的那个数
    if c>b:
        c = b
    #从小的那个数递减，第一个能够被这两个数整除的就是最大公约数
    while c>0:
        if(a%c==0 and b%c==0):
            return re
        c-=1
def bei(a,b):
    c = a#用来保存大的那个数
    if b>a:
        c = b
    while c<=a*b:
        if(c%a==0 and c%b==0):
            return c
        c+=1
#写一个方法，将传入的列表(参数为列表),删除列表中重复的数据再输出新的列表
def delSame(a):
    c = [] #结果列表
    for i in a:#遍历a中的元素
        #如果这个i不在c中,才添加
        if not i in c:
            c.append(i)
    return c
'''
每个元素和每个元素去比较
list.sort()
[1,1,1,2,4,4,5,5,5,6,8,9]
'''












