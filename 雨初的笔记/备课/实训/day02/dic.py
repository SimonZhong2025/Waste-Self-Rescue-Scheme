#coding:utf-8
'''
字典是Python中另一个非常有用的内置数据类型
列表是有序的对象集合，字典是无序的对象集合
两者的区别:列表是用过下标，字典是通过键值对
字典是一种映射类型，字典用{}标识，它是一个无序的键(key):值(value)的集合
键(key)必须使用不可变类型
在同一个字典中，键(key)的值必须是唯一的
'''
#定义一个空的字典
dic = {}
#dic[key]=value
dic['aaa'] = 'this is an apple'
dic[2] = 'this is a banana'
print(dic)
#得到某个key值对应的value值
print(dic['aaa'])
#给字典赋初始值
dicTyy = {'name':'tyy','age':'18','height':'181'}
print(dicTyy['height'])
#字典的value是可以修改的
dicTyy['age'] = '19'
print(dicTyy['age'])
#得到字典的全部key值或者value值
print(dicTyy.keys())
print(dicTyy.values())
#通过dict()方法来创建字典
dic3 = dict([('Baidu',1),('Google',2),('Taobao',3)])
print(dic3)
#len()得到字典的长度
print(len(dicTyy))

