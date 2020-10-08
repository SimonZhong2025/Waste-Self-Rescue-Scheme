#coding:utf-8
'''
Python中的字符串用单引号或者双引号括起来，同时使用反斜杠\来转义某些特殊字符
'''
str='happy'
print(str)
print(type(str))
#str[index]  str[0]返回字符串的第一个字符
print(str[0])
#str[1]='b'   不可以
#str[0:3]  从下标0到下标3的字符，左闭右开
print(str[0:3])
#也支持索引反着来  正着来   0 1 2 3 4
#反着来   -5 -4 -3 -2 -1
print(str[0:-1])
#str[1:] 从下标为1开始，到最后
print(str[1:])
print(str[:3])
#str*2
print(str*2)
#字符串的加法就是做字符串的拼接
# \n是换行符
print('eve\ning')
# \\是\
print('eve\\ning')
#在字符串前加  r,能够得到本身表示的字符
print(r'eve\ning')
#\代表续行符,\后面不能有任何字符，连空格都不行
print('a'\
      'b'\
      'c')
