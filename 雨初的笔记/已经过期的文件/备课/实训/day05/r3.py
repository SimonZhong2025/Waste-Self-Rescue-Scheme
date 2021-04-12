#coding:utf-8
#r+ 可读可写打开，直接写入
f = open('fa.txt','r+')
#光标位置在最开始
f.write('I Like Java')
f.close()