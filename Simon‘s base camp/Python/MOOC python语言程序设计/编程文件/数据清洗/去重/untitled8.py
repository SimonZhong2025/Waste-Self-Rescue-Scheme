# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 16:31:58 2021

@author: Zhong
"""

import pandas as pd
import os
import importlib
import sys
importlib.reload(sys)

data1 = pd.read_csv('start.csv')
data2 = data1.drop_duplicates(subset='评论')
sys.getdefaultencoding('gkd')
fsave = open('quis1.txt', mode='a')
fsave.write(str(data2)+'\n')
fsave.close()