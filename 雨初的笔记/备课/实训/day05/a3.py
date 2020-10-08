#coding:utf-8
f = open('aaa.txt','a+')
f.seek(0)
print(f.read())
#打印文件名  fileObj.name
print(f.name)
#清空文件
f.truncate(6)  
'''
truncate(position) 如果放参数是指从哪个位置开始清空
如果不放参数，是从当前光标位置开始清空
'''
f.seek(0)
print(f.read())
f.close()