#coding:utf-8
#同时使用多种格式化，并使用字典传参
print("My age is %(a)d,I like %(b)s,I have %(c).2f yuan." % {'a':20,'b':'python','c':99.2345})
'''
对于字符串，新增了str.format()函数，增强了字符串的格式化功能
'''
#不设置指定位置，按照默认顺序传参
print("{} {}".format("hello","world"))
#设置位置   后面参数看做列表，有下标
print("{0}{2}{1}{1}".format("hello","world","xiaoming"))
#设置参数
print("学校名为:{name},地址是:{add}".format(name="南大软",add="南京路"))
#通过字典传字符串
dic = {"name":"南大软","add":"南京路"}
print("学校名为:{name},地址是:{add}".format(**dic))
#还支持列表传参(支持对象传参)
myList = ["南大软","南京路"]
print("学校名为:{0[0]},地址是:{0[1]}".format(myList))




