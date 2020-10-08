#coding:utf-8
#可以将字符串改为元组或者列表输出
la = 'python'
print(tuple(la))
print(list(la))
#得到字符对应的ASCII   ord(str)得到ASCII码    chr(ASCII)得到字符串   ？？如何随机的十位a-z的字符串？？
print(ord('中'))
print(ord('a'))
#得到ASCII代指的字符
print(chr(20013))
print(chr(65))
#得到字符中某个字符的下标
print(la.index('t'))
print('y' in la)
#.strip()去除字符串中首尾的空格
strA = '   aaBcdD   '
print(strA.strip())
#判断字段是否为全英文 isalpha()
print(strA.isalpha())
#转大写 upper()  转小写lower()
print(strA.upper())
print(strA.lower())
#可以通过某个字符将字符串分割为一个列表
strC = "tyy|abcd|qwer|df"
print(strC.split('|'))
print(strC.split('|')[2])
#判断字符串是否为全大写，全小写
print(strC.isupper())
print(strC.islower())


