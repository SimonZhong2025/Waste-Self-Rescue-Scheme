#coding:utf-8
'''
List(列表)是python使用比较频繁的一个数据类型
列表可以存放不同类型的数据，支持数字、字符串、甚至是另一个列表
列表是写在[]之间的，用逗号隔开元素的
和字符串一样，也可以通过索引得到元素
'''
list = ['java',3.14,'python',999,666]
alist = ['c#','html',333]
#列表的元素是可以被修改的
list[1] = 3.1415926
print(list)
#通过索引得到元素
print(list[0])
#得到某部分的元素
print(list[1:3])
print(list[2:])
print(list*2)
#列表可以实现拼接，组成一个新的列表
nlist = list + alist
print(nlist)
#截取列表的元素，还可以第三个参数，第三个参数表示每次截取的步长
print(nlist[1:6])
print(nlist[1:6:2])
#列表也支持反向输出  步长也要取负数
print(nlist[-1::-2])



