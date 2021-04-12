#coding:utf-8
#字符串常用方法
#字符串是通过单引号或双引号包裹的
# \ 可以转义   \n   \t    
strA ="I don\'t know" 
print(strA)
#字符串可以通过下标访问每个字符
strC ='Python是世界上最好的语言,\n大家一定要好好学。'
#len(str) 得到字符串的长度
print("字符串strC的长度是%d" % len(strC))
print("strC[10]=%s" % strC[10])
print("strC[-13]=%s" % strC[-13])
#可以截取字符串
print("strC[0:5]=%s" % strC[0:5])
print("strC[-2:]=%s" % strC[-2:])
print("strC[-23:]=%s" % strC[-23:])