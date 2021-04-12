#coding:utf-8
#只读操作，文件必须存在
f = open('fa.txt','r',encoding='gbk')
'''
#readline() 读文件的第一行
print(f.readline())
#打印光标的位置tell()
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
'''
#f.read()读完后光标的位置位于文件的最尾端，要再读要改变光标的位置
print(f.read())
print(f.encoding)  #得到编码格式
print(f.tell())
#设置光标的位置  seek(index)
f.seek(0)
print(f.read())
#每次操作完都要关闭文件
f.close()
