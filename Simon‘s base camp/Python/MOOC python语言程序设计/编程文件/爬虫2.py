# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 21:54:14 2021

@author: Zhong
"""

import requests

headers = {
    'referer': 'https://detail.tmall.com/item.htm?spm=a230r.1.14.1.4cc11f3ac1oeGY&id=638219285230&ns=1&abbucket=4',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68',
    'cookies' : 'dnk=tb744497849; tracknick=tb744497849; lid=tb744497849; lgc=tb744497849; cookie2=1860adea5dfbbf57293ca594c564c929; enc=39hKR5YwvdlVzzhdhxiHGbpy8PqdNnMtrrMrDo2xQZcnIb1jKTvyZkXMzxyWdB3cfxfFuuVyn4tZCAwYg0BPJJWsYopmtReQ5x8Sayeh%2BTM%3D; _tb_token_=3eebeeee11eef; cna=tu4/F7YVlG8CAXjm2hIMxmX/; tk_trace=1; t=8accf8858c1d1fc2ae40de75b7cb0f2b; tfstk=c67ABdtfc8204AARTiEof7b8dlfOZow9Fj9iWW-OT7Im7G0OiVbhJrazcCOTn7C..; x5sec=7b22726174656d616e616765723b32223a223938306263343633323265653438363531323666653533636264363639623937434b374177594d47454a66727863617072705878566967434d4f32352f397a2b2f2f2f2f2f77453d227d; uc1=cookie21=VT5L2FSpczFp&tag=8&cookie15=W5iHLLyFOGW7aA%3D%3D&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cart_m=0&existShop=false&cookie14=Uoe1hdjsq7JDeQ%3D%3D&lng=zh_CN&pas=0; uc3=nk2=F5RCYR%2Fwy5L1fbE%3D&lg2=URm48syIIVrSKA%3D%3D&vt3=F8dCuwucAzKTsgQ%2BYRw%3D&id2=UUphyd6ApN3wmGVgHw%3D%3D; _l_g_=Ug%3D%3D; uc4=id4=0%40U2grEhAnr8dtt%2Bp%2FrFt21lKQX5skdtCx&nk4=0%40FY4Jj1B6TG08spPEz05aqv4y%2BvDvdQ%3D%3D; unb=2203076610351; cookie1=WvKQwP1R7NhdB5OMAtdfRHjlHcdEnHzomR%2BTPc6MilQ%3D; login=true; cookie17=UUphyd6ApN3wmGVgHw%3D%3D; _nk_=tb744497849; sgcookie=E100V%2BXb%2FhdiHKy8EOL%2FWZ06UGZdYLkHzKVK%2FTugWSaVNS4YCKFBRq%2FBG06j8nHg7eEPMnm9ls7CLlkZ5z7bOURZjw%3D%3D; sg=915; csg=09699ae6; l=eBrKKldgQC1X2EKvBOfZnurza77TsIRAguPzaNbMiOCPOlfw7xHAW6axHILeCnGVh646J3lF3rp0BeYBqIq0x6aNa6Fy_Ckmn; isg=BLa21-jVynEcxoCkHgmBMHrzB-y41_oRP4dxtSCfqBklY1b9iWUsILUVez8PS_Ip'
}

url = "https://rate.tmall.com/list_detail_rate.htm?itemId=638219285230&spuId=1977793440&sellerId=2206485749255&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvWvvEvbQvUvCkvvvvvjiWPLSyzj1UPLSh1jYHPmP9sjEjRFcvtjlbPsLUQj3Ci9hvCvvv9UUgvpvhvvvvvvgCvvpvvPMMvvhvC9vhvvCvpv9CvhQvQlgvCsuxfaClHsyDZtcEsXZZDVQEfaClYb8rwm0guf0Dn1Bkp8oQD76Od56Q3aV3ff8ramDlIExreutiBXxrlj7JVVQHYWsUtE97kvhvC99vvOCgp49Cvv9vvUvGY9t64d9Cvm9vvvvvphvvvvvvvi3vpvQRvvm2phCvhRvvvUnvphvpgvvv96CvpC2939hvCvvhvvv%3D&needFold=0&_ksTS=1617977421844_408&callback=jsonp409"

data = requests.get(url,headers = headers).text

print(data)
