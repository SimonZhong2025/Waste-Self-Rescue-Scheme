#coding:utf-8
#a+ 可读可写 ,追加写的光标位置在结尾，直接读，读不到内容，要改变光标位置
f = open('aaa.txt','a+')
f.seek(0)
print(f.read()) #读完之后光标在结尾
f.write('java')
f.seek(0)
print(f.read())
f.close()