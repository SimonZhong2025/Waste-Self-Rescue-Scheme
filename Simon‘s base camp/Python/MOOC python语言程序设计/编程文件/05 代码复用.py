# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 16:48:57 2021

@author: Zhong
"""


rvs_data = input("输入数字哈")

def Fn(n):
    if n == 1:
        return n
    elif n == 2:
        return n
    else:
        return Fn(n-2) + Fn(n-1)

print(Fn(eval(rvs_data)))
