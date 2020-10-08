#coding:utf-8
f = open('fa.txt','r+')
print(f.readline())
print(f.tell())
f.seek(4)
print(f.readline())
print(f.tell())
#只有二进制才可以设置1,2的值
#seek(a,b)   a是移动的长度(可正可负) b=0,1,2   0是文件开头 1是当前位置 2是文件结尾
print(f.seek(2,0))
print(f.tell())