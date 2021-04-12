#coding:utf-8
from datetime import datetime
from datetime import timedelta
import time
import calendar
#获取当前时间(包含日期)
print(datetime.now())
#只要时间
print(datetime.now().time())
print(type(datetime.now()))
#获取当前日期
print(datetime.now().date())
#获取当前时间的元组
print(datetime.now().timetuple())
'''
使用datetime.timedelta() 用来前后移动时间
可以用的参数
weeks  days  hours minutes seconds microseconds
days=1 代表一天后  days=-1 代表前一天
'''
print(datetime.now()+timedelta(days=1))
#Calendar模块
print("2020年的年历是：")
print(calendar.prcal(2020))
#月历
cal = calendar.month(2020,9)
print("2020年9月份的月历是：")
print(cal)

