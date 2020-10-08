#coding:utf-8
import random
'''
3.制作一个猜拳游戏，让用户选择出拳类型(石头、剪刀、布)，然后电脑随机出拳，最后打印电脑出拳和玩家出拳，并提示输赢
  结束后询问用户是否继续玩
'''
#用来表示用户出什么拳的字典
choDic = {"1":"石头","2":"剪刀","3":"布"}
tDic = {"石头":2,"剪刀":1,"布":0} #用0,1,2来代替字符剪刀石头布
while True:
    #dic.get(key,default='不存在是key对应的value值')
    plCho = choDic.get(input('请输入你的选择:1.石头\t2.剪刀\t3.布'),'error')
    if plCho=='error':
        print('输入错误')
        continue
    comCho = choDic[str(int(random.uniform(1,4)))]
    print('你出的是:',plCho,',电脑出的是:',comCho)
    #re表示两者出拳的差值    差值为1、-2代表赢了  差值为0平局  其他为输
    re = tDic[plCho] - tDic[comCho]
    if re==1  or re==-2:
        print('恭喜你，赢了！')
    elif re==0:
        print('平局！')
    else:
        print('你输了！')
    choose = input('是否继续游戏?Y/N')
    if choose=='N':
        break
    else:
        continue
    
    