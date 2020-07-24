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
