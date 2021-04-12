#coding:utf-8
#对列表的增删改查
name1 = ['zhangsan','lisi','list','tyy','list']
print(name1)
#遍历:一个一个的看
#for循环，i是变量，随便取的，表示每次循环使用它作为变量
for i in name1:
    print(i)
#增加
name2 = ['timo','yasuo']
#extend()将一个列表添加至另一个列表的结尾
name1.extend(name2)
print(name1)
#append()  在列表结尾追加一个元素
name1.append('yongen')
print(name1)
#insert 插入元素  insert(index,object)
name1.insert(2, 'mangseng')
print(name1)
#删除
#remove(value)  删除第一个匹配的元素，如果不存在这个值，会报错   
#name1.remove('aaa')   因为'aaa'不在列表中，所以会报错
name1.remove('list')  #删除第一个'list'
print(name1)
#pop(index)  以元素的下标去删除元素，默认删最后一个(如果不放参数)
#name1.pop(20)   没有对应下标的元素(长度不够)会报错
name1.pop(4)
print(name1)
#查
#index() 查询是否有指定元素，如果有，返回下标
print(name1.index('yasuo'))  #如果不存在就报错
#name1[index]
print(name1[name1.index('yasuo')])
#查询列表中有几个相同元素
#count()
name1.append('lisi')
print(name1.count('lisi'))
#排序
#按照字母的升序排序
name1.sort()
print(name1)
#按照字母的降序排序
name1.reverse()
print(name1)

