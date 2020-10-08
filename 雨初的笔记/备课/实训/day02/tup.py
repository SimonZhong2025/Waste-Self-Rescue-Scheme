#coding:utf-8
'''
元组与列表类型，不同之处在于元组的元素不能被修改，元组是写在()里面的
'''
tup = ('java',3.14,'python',999,666)
atup = ('c#','html',333)
#tup[1] = 3.1415926  元组的元素不能被修改
print(tup)
print(tup[2])
print(tup[1:3])
print(tup[2:])
print(tup+atup)
#如果定义一个只有一个元素的元组，要加逗号以示区分
btup = ('hello',)
#String,list,tuple都是sequence(序列)
#定义一个空元组
ctup = ()
print(type(ctup))
