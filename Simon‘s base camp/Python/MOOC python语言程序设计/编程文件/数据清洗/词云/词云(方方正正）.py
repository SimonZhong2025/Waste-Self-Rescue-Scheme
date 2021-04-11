# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 16:26:36 2021

@author: CeciliaYip
"""
import wordcloud
# 从外部.txt文件中读取大段文本，存入变量txt中
f = open('（问答）合.txt',encoding='utf-8')
txt = f.read()

# 构建词云对象w，设置词云图片宽、高、字体、背景颜色等参数
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc')

# 将txt变量传入w的generate()方法，给词云输入文字
w.generate(txt)

# 将词云图片导出到当前文件夹
w.to_file('问答1.png')