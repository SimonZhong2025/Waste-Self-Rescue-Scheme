#coding:utf-8
#w只写方式，如果文件不存在则创建文件，如果存在则覆盖
f = open('ff.txt','w')
#print(f.read())  没有读的权限
f.write('java\npython')
f.close()