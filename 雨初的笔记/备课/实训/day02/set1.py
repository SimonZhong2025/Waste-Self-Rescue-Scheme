#coding:utf-8
'''
集合(set)是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象成为元素或者成员
基本功能是进行成员关系测试和删除重复的元素
可以用大括号{}或者set()函数创建集合
注意:创建一个空集合必须用set()，而不是{},因为{}是用来创造空字典的
'''
student = {'zhangsan','lisi','wanger','tyy','lisi'}
#1.集合输出有顺序么？  没有
#2.集合会自动去重
print(student)
#判断某个元素是否在集合中
if 'tyy' in student:
    print('tyy在集合中')
else:
    print('tyy不在集合中')
#定义一个空集合
seta = {}
setb = set()
print(type(seta),type(student),type(setb))
#集合可以用来做集合运算
a = set('abcdefg')
b = set('bcdegt')
#a-b 差集 只在a中的元素
print(a-b)
#a|b 并集 同时在a和b中
print(a|b)
#a&b 交集
print(a&b)
#a和b中不同时存在的元素
print(a^b)
