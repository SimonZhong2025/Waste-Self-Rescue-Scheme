#TemperConver.py

TemperStr = input("输入带有符号的温度值：")
if TemperStr[-1] in ['F','f']:
    C = (eval(TemperStr[0:-1]) - 32)/1.8
    print("转换后的温度值是{:.2f}C".format(C))
elif TemperStr[-1] in ['C','c']:
    F = (eval(TemperStr[0:-1]))*1.8 + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("格式错误")

#举一反三的改变
#标识放在温度数值前面
#标识字符改变为多个字符：82Ce等等
#货币转换、长度转换、重量转换、面积转换......
