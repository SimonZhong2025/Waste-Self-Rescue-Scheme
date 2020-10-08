#coding:utf-8
#r+ 可读可写          rb+二进制可读可写
f = open('fa.txt','r+')  #使用二进制打开文件，所有字符都会显示
print(f.read())
#以二进制的形式写文件
f.write('aaa')   #  write(b'aaa')二进制写
f.close()