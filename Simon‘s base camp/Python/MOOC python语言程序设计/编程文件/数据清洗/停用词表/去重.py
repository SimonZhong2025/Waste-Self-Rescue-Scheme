# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 15:23:40 2021

@author: Zhong
"""

import pandas as pd
import os
import importlib
import sys
importlib.reload(sys)

inputfile = 'start.csv'
outputfile = 'quis_jd.txt'
data = pd.read_csv(inputfile,encoding='utf-8')
data.head()

sys.getdefaultencoding()

data.to_csv(outputfile, index = False, header = False, encoding = 'utf-8')
outdata_1 = pd.read_csv(outputfile, encoding = 'utf-8', header = None)
outdata_1.head()

outputfile = 'quis_jd2.txt'
l1 = len(outdata_1)
data_unique = pd.DataFrame(outdata_1[0].unique())
l2 = len(data_unique)
data.to_csv(outputfile, index = False, header = False, encoding = 'utf-8')
print(u'共%s条评论，删除了%s条评论。'%(l1, l1 - l2))
