#coding:utf-8
'''
while True:
    try:
        a = int(input("请输入一个整数："))  #这行代码有异常，后面的代码不会执行
        print("输入成功！")
        break;
    except ValueError: #可以指明捕获的异常，也可以不写，当做通配符
        print("不好意思，你输入的不是整数！")
'''
'''
try:
    f = open('母猪的产后护理.txt') #打开一个文件
    s = f.readline()       #读文件
    i =int(s.strip())      #去除读出数据的空格并强转为int
except OSError as err:  #捕获一个OSError取个名字叫err
    print(err)
# except ValueError:  #捕获一个值异常
#     print("转换不了！")
except:  #还可以捕获未知的异常
    print("未知的错误")
    raise   #可以通过raise主动抛出捕获的异常
'''
print('--------------')
sa = 'HELLO'
try:
    int(sa)
except Exception as e: #Exception代表了所有异常
    print(e)




