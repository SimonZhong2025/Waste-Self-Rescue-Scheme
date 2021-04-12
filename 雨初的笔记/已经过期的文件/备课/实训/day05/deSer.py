#coding:utf-8
import pickle
#反序列化
#首先打开之前序列化了的文件，以读二进制的形式 rb
f = open('ser.txt','rb')
for i in range(2):
    obj = pickle.load(f) 
    print(obj)
f.close()