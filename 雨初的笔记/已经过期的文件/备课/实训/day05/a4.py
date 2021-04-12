#coding:utf-8
#如果想在上一级打开或创建文件    /表示文件的层级关系
'''
f = open('../abc.txt','a')
f.write('121212')
f.close()
'''
for i in range(5):
    #重复5次，创建i.py文件
    f = open('D://app//'+str(i)+'.py','a')
    f.write('121212')
    f.close()