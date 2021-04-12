#coding:utf-8
import random
'''
让用户输入一个数,例如 654321,打印123456,倒着打印出来
654321
1. 取到尾数1，把这个数改为65432，结果的数赋值为1
2. 取到尾数2，把这个数改为6543，结果的数赋值为12
n.  6  取到6 赋值 123456
。。。
   原来的数=？   结果的数=？

num1 = int(input('请输入一个整数'))
re = 0 #存放结果数
while num1>0:#原来的数会被越除越小
    #取出尾数
    la = num1%10
    #原来的数改变
    num1=num1//10
    #结果的数要赋值     1 2  12    12 3  123   123 4  1234
    re = re*10+la
print('倒转之后的数为',re)  
''' 

'''
有六个小正方体，分别印有1-6，随机扔，如果总和大于20，输出大，否则输出小
random.uniform(statr,end) 随机生成范围内的一个实数(包含小数) 左闭右开
'''
re = []#放六个正方体的列表
i = 0
while i<6:
    i+=1
    re.append(int(random.uniform(1,7)))
print(re)
su = 0
j = 0
while j<6:
    su += re[j]
    j+=1
if su>20:
    print('大')
else:
    print('小') 


