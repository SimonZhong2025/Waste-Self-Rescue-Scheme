# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 16:11:01 2021

@author: Zhong
"""

"""
去重并按原文件顺序排序
"""

from time import time

print('开始去重...')
start = time()
new_list = []

path = 'quis1.txt'
file=open(path).read().decode('gb18030','ignore')

for line in open(r'quis1.txt', 'r+'):
    new_list.append(line)

new_list2 = list(set(new_list))					#去重
new_list2.sort(key=new_list.index)				#以原list的索引为关键词进行排序
new_txt = ''.join(new_list2)					#将新list连接成一个字符串
with open(r'e:/Python/mypy/test_new.txt', 'w') as f:
	f.write(new_txt)
end = time()
shi = end - start
print('去重完毕！')
print('总耗时%s秒！' % shi)
