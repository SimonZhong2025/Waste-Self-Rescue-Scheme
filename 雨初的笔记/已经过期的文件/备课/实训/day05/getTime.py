#coding:utf-8
import time
def showDate(a):
    return {
            0:"星期一",
            1:"星期二",
            2:"星期三",
            3:"星期四",
            4:"星期五",
            5:"星期六",
            6:"星期天"
            }.get(a[6],"时间输入错误")
print("今天是%s" %showDate(time.localtime()))