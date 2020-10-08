#coding:utf-8
#finally语句中的代码最后都会执行
def mul(a,b):
    if a<b:
        raise BaseException('被减数不能小于减数') #有异常被抛出，但是我不处理，让别人处理
    else:
        return a-b
try:
    print(mul(0,3))
    print('try的结尾')
except:
    #pass #啥也不干
    raise  #把捕获的异常抛出(打印出来)
finally:
    print('finally')
print('------------')
sa = 'HELLO'
try:
    int(sa)
except IndexError as e:  #下标异常
    print('1',e)
except KeyError as e:  #字典不存在key值异常
    print('2',e)
except ValueError as e:
    print('3',e)
else:
    print('Success')
finally:
    print('finally')






