#coding:utf-8
'''
写一个函数，传入参数1-7，输出周一到周日，传入其他的显示输入有误    
'''
def dateFun(nu):
    dateDic = { 1:'周一',
                2:'周二',
                3:'周三',
                4:'周四',
                5:'周五',
                6:'周六',
                7:'周日',
               }
    print(dateDic.get(nu, '无对应的值'))
dateFun(2)