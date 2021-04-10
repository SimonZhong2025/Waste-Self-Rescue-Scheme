# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 23:25:41 2021

@author: Zhong
"""

import requests
import re
import time
import pandas as pd

def main():
    url:'https://rate.tmall.com/list_detail_rate.htm?itemId=638219285230&spuId=1977793440&sellerId=2206485749255&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvgQvnvPpvUvCkvvvvvjiWPLSygjr2P2zy1jD2PmPZgjtPRLsOgjE8RsLpgjnjdvhvHhr8j3C2vhCLsOaYmLeQbyICaajEdvhvmZCmQ337vhCVyIOCvvBvppvvi9hvChCvCCpRvpvhvv2MMg9CvvXmp99hjEAIvpvUphvhgaKx9MugvpvIphvvvvvvphCvpvADvvC2QhCvjvUvvhBGphvwv9vvBj1vpCQmvvChNv9Cvh1CYkpvIqyDCcECTWeARFxjb9TxfXkXjovDN%2BLOd3OiHmx%2F1WAK5zHva6jUTEu4aDI0747BhC9YpV9w%2Bb0cVcpUwH5%2BkLeAUZiqVUcnvvhvCyCCvvvvv29CvvBvpvvvC9hvCYsw7DdNOPZgvpvhphvvvv%3D%3D&needFold=0&_ksTS=1617980806996_433&callback=jsonp434'
    headers = {
    'referer': 'https://detail.tmall.com/item.htm?spm=a230r.1.14.1.4cc11f3ac1oeGY&id=638219285230&ns=1&abbucket=4',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68',
    'cookies' : 'dnk=tb744497849; tracknick=tb744497849; lid=tb744497849; lgc=tb744497849; cookie2=1860adea5dfbbf57293ca594c564c929; enc=39hKR5YwvdlVzzhdhxiHGbpy8PqdNnMtrrMrDo2xQZcnIb1jKTvyZkXMzxyWdB3cfxfFuuVyn4tZCAwYg0BPJJWsYopmtReQ5x8Sayeh%2BTM%3D; _tb_token_=3eebeeee11eef; cna=tu4/F7YVlG8CAXjm2hIMxmX/; tk_trace=1; t=8accf8858c1d1fc2ae40de75b7cb0f2b; tfstk=c67ABdtfc8204AARTiEof7b8dlfOZow9Fj9iWW-OT7Im7G0OiVbhJrazcCOTn7C..; uc1=cart_m=0&cookie21=VFC%2FuZ9ainBZ&pas=0&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&existShop=false&lng=zh_CN&cookie14=Uoe1hdjsr87akQ%3D%3D&cookie15=UIHiLt3xD8xYTw%3D%3D&tag=8; uc3=lg2=UtASsssmOIJ0bQ%3D%3D&id2=UUphyd6ApN3wmGVgHw%3D%3D&nk2=F5RCYR%2Fwy5L1fbE%3D&vt3=F8dCuwucAz6v87N2igI%3D; uc4=id4=0%40U2grEhAnr8dtt%2Bp%2FrFt21lKQX5sg1%2BC3&nk4=0%40FY4Jj1B6TG08spPEz05aqv4y%2Fr57Qw%3D%3D; _l_g_=Ug%3D%3D; unb=2203076610351; cookie1=WvKQwP1R7NhdB5OMAtdfRHjlHcdEnHzomR%2BTPc6MilQ%3D; login=true; cookie17=UUphyd6ApN3wmGVgHw%3D%3D; _nk_=tb744497849; sgcookie=E100JxB3MlIkOT1fhTwiEJ1D%2B2XcRDHYoPvNYdfEmGPYFPtojkfwes9lk4%2Bk9pEhpCVerjVWXY%2BYCzCPfFYEYesVsQ%3D%3D; sg=915; csg=5559b682; l=eBrKKldgQC1X2pcAKO5ZPurza77tgIRb4sPzaNbMiInca6CO6FGRyNCQkmuJJdtjgt1FTetrTtzvnRLHR3x0ikfQ7_5LaCJqnxf..; isg=BO_vutPr0xafoembv6oot0ugfgP5lEO2rnQYagF8Hd5mUA9SCWWRBh0G0kDuKBsu',
    }
    startpage = 1
    endpage = 10
    for page in range(startpage,endpage+1):
        print('开始爬取第%s页' % page)
        url = url.format(str(page))
        r_toke = requests.get(url=url, headers= headers)
        r_toke.encoding='utf8'
        json_text=r_toke.text.strip('()')
        json_text=json_text.replace()
        
