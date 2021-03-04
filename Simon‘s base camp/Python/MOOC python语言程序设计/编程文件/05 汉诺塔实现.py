# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 17:28:08 2021

@author: Zhong
"""

count = 0
def hanoi(n, zero, goal, mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1, zero, goal))
        count += 1
    else :
        hanoi(n-1, zero, mid, goal)
        print("{}:{}->{}".format(n, zero, goal))
        count += 1
        hanoi(n-1, mid, goal, zero)

hanoi(3, 'A', 'C', 'B')
print(count)
