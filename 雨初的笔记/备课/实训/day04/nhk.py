#coding:utf-8
import random
'''
随机生成一个由26个小写英文字母组成100位的字符串，输出每个字母出现的次数，出现次数最多的那个字母是什么？
'''
str=''
for i in range(100):
    #random.randint()得到整数
    str+=chr(random.randint(97,122))
print(str)
#存放出现次数的列表
liCount=[]
for i in range(26):
    liCount.append(0)
a=0
for i in range(97,123):
      for j in str:  
        if(ord(j)==i):
            liCount[a]+=1
      a+=1
for i in range(26):
    print(chr(i+97),"出现了",liCount[i],"次")
print(chr(liCount.index(max(liCount))+97),"次数最多")
            
    