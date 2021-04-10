# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 16:31:58 2021

@author: Zhong
"""

import pandas as pd
import importlib
import sys
importlib.reload(sys)

inputfile = 'start.csv'
outputfile = 'end.csv' #csv文件转化为txt文件

csv = pd.read_csv(inputfile, encoding='utf-8') #读取csv中的数据

csv.head()

sys.getdefaultencoding()

df = pd.DataFrame(csv)

print(df.shape)#打印行数
f=df.drop_duplicates()#去重
print(f.shape)#打印去重后的行数
f.to_csv(outputfile, index = False, header = False, encoding = 'utf-8')

