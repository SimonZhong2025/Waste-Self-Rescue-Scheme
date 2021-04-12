#coding:utf-8
#整数的格式化输出
num = 1424
print("num=%d" % num)
'''
%d  %i  %u 都可以表示整数
%o 八进制      %x十六进制
'''
print("%d,%i,%u" % (num,num,num))
print("%o,%x" % (num,num))
#整数的位数为1,但是原数据超过1位,按原数据输出,如果占的位数多于原数据，不足补空格
print("num=%1d" % num)
print("num=%10d" % num)
#不足的在后面补空格
print("num=%-10d%d" % (num,num))
#也可以补0
print("num=%010d" % num)
# %5.3 是上面两种补齐方式的结合，当整数部分不够5位时，优先补0，但还是不够7位，再补空格
print("num=%7.5d" %num)
print("num=%07.5d" %num)
print("num=%*.*d" %(7,5,num))




