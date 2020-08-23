# 八边形的绘制，注意range里面的数，我们只需要看需要走多少次即可，不需要看left多少次，只有fd才是有画上东西的。
import turtle as t
t.pensize(2)
for i in range(8):
    t.fd(100)
    t.left(45)
    
# 风车绘制，运用到goto函数
import turtle as t
t.pensize(2)
for i in range(4):
    t.fd(150)
    t.right(90)
    t.circle(-150, 45)
    t.goto(0,0)
    t.left(45)

#也可以这样
#WindWheel.py
import turtle as t
t.pensize(2)
for i in range(4):
    t.seth(90*i)
    t.fd(150)
    t.right(90)
    t.circle(-150, 45)
    t.goto(0,0)
