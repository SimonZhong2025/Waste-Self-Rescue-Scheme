#coding:utf-8
#a方式打开文件，如果文件不存在，则新建一个文件，如果存在则追加写
f = open('aaa.txt','a')
f.write('\\npython')  #也可以写换行符
#print(f.read())  没有读的方法
f.close()