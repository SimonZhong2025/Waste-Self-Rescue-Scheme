# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 16:18:04 2020

@author: Zhong
"""


import requests
url = "http://weekly.chinacdc.cn/news/TrackingtheEpidemic.htm"
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url, headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encodingg
    print(r.text[:1000]) # 有何分别？
except:
    print("失败")
    r.encoding = r.apparent_encoding
    print(r.text)