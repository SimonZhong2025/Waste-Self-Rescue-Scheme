#coding:utf-8
'''
字符串的格式化输出
'''
str = "hello"
#直接打印字符串
print("str=%s" % str)
#%3s 指的是字符串长度为3，原字符串超过3，按照原字符串输出
print("str=%3s" % str)
#%7s 不够位数补空格   %-7s在后面补空格
print("str=%7s" % str)
print("str=%-7s" % str)
#%7.2s  字符串长度为7，但是只取原字符串的两位，前面补空格
print("str=%7.2s" % str)
print("str=%*.*s" % (7,2,str))