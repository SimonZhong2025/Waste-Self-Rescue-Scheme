#coding:utf-8
#通过二进制读写操作复制文件
f = open('鸣人.jpg','rb')
f2 = open('D://鸣人影分身.jpg','wb')
f2.write(f.read())
f.close()
f2.close()