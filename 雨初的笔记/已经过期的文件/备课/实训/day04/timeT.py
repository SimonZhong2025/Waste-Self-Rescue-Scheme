#coding:utf-8
import time
'''
时间戳方式:表示的是从1970年1月1日00:00:00到现在的秒数(偏移量)
struct_time 方式(元组): 9个元素
'''
#time()
#time.time()得到从1970年1月1日00:00:00到现在的秒数
print("当前的时间数值为%f" % time.time())
'''
locatime()得到本地时间，转换为计算机能够识别的时间格式，以元组形式保存
tm_year=2020, 年
tm_mon=9,     月
tm_mday=10,   日
tm_hour=15,   时
tm_min=50,    分
tm_sec=57,    秒
tm_wday=3,    星期几  （0-6）  0是周一
tm_yday=254, 一年中的第几天
tm_isdst=0   是否为夏令时节(中国不存在)   -1不详        0否      1是
'''
#time.localtime() 将一个时间戳转换为一个struct_time
print(time.localtime())
#time.gmtime()  UTC时区  伦敦时间
print(time.gmtime())
#time.mktime()  参数为struct_time
#写一个struct_time的元组
t=(2020,9,11,8,0,0,4,255,0)  #t是struct_time
print(time.mktime(t))
print(time.mktime(time.localtime()))
print('--------')
#把struct_time转换为固定的时间格式输出
print(time.asctime(time.localtime()))
#也可以传时间戳作为参数得到固定格式  ctime(秒数)
print(time.ctime())
'''
time.sleep() 参数为秒

def sleepTime():
    print(time.ctime())
    time.sleep(5)
    print(time.ctime())
sleepTime()
'''
#按照我们的格式去输出时间
t = time.mktime(t)
#strftime()
print(time.strftime("%B %d %Y %H:%M:%S",time.localtime(t)))
print(time.strftime("%B %d %Y %H:%M:%S"))




