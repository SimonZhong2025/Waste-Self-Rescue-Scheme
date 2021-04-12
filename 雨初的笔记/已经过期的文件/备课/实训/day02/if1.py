#coding:utf-8
'''
#让用户输入4个数,输出最大值
a = int(input("请输入第一个数"))
b = int(input("请输入第二个数"))
c = int(input("请输入第三个数"))
d = int(input("请输入第四个数"))
max = a
if b>max:
    max = b
if c>max:
    max = c
if d>max:
    max = d
print("这四个数中的最大值为",max)
'''
#使用列表提供的方法去实现
li = [12,13,14,15,16]
print(max(li))
print(min(li))




