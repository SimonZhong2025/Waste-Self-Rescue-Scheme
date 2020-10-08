#coding:utf-8
#比较运算符
'''
<    a < b  判断a是否小于b  结果返回  True 或者  False
<=  
>  
>=  
!=
==  判断是否相等
'''
print(3<5)
print(4==4)
#逻辑运算符   与、或、非   and、or、not
print(3<5 and 3>5)
print(3<5 or 3>5)
print(not 3>5)
print("#########")
#短路
print(3 or a)  #or后面的代码不执行了
print(0 and a) #and后面的代码不执行了，虽然a未定义，但是不报错
print(0 or a)

