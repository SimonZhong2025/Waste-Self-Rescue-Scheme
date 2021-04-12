#coding:utf-8
#w+ 只写模式下的可读可写
f = open('ff.txt','w+')
#w模式打开文件也就是删除原文件再创建新文件
print(f.read())
f.write('html+css')
#写完之后，光标在文件结尾
print(f.tell())
f.seek(0)
print(f.read())
f.close()
