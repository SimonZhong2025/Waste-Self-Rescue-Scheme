# 八边形的绘制，注意range里面的数，我们只需要看需要走多少次即可，不需要看left多少次，只有fd才是有画上东西的。
import turtle as t
t.pensize(2)
for i in range(8):
    t.fd(100)
    t.left(45)
    
