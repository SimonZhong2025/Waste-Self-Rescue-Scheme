#coding:utf-8
import traceback
try:
    print(5/0)
except (TypeError,ZeroDivisionError) as e:
    traceback.print_exc()  #错误的堆栈信息
    print(e)               #打印异常的实例
else:
    print("没错误！")
#类是脑海中的抽象概念  ，对象是类的一个实例化