#coding:utf-8
'''
ASCII码
'''
#用户输入一个字符
#c = input('请输入一个字符！')
#print(type(c))  所有输入的都是字符串类型
c =int(input('请输入一个ASCII码！'))
#用户输入的ASCII   chr()把ASCII转换为字符
print(c,"对应的字符为",chr(c))
d =input("请输入一个字符")
#ord()把字符转换为对应的ASCII
print(d,"对应的ASCII码为",ord(d))

