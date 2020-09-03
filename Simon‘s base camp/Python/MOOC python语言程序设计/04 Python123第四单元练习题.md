from time import perf_counter
start = perf_counter()
def is_prime(n):
    for i in range (2, n):
        if n%i == 0:
            return False
            break
    else: return True
sum = 2
for i in range (3, 100):
    if is_prime(i):
        sum += i
print(sum)
print(perf_counter()-start)
        
a = 2
for i in range(3,100):
    for b in range(2,i):
        if i%b == 0:
            break
    else:
        a += i
print(a)
    
#1060 0.0007600000000138607 1060 0.0005961999999612999 所以下面的方法更快，因为上面的方法多了循环


### 用户登录的三次机会
> 给用户三次输入用户名和密码的机会，要求如下：‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

- 如输入第一行输入用户名为‘Kate’,第二行输入密码为‘666666’，输出‘登录成功！’，退出程序；‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

- 当一共有3次输入用户名或密码不正确输出“3次用户名或者密码均有误！退出程序。”。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬

 
```
for i in range(0,6):
    a = input()
    if a == "Kate":
        b = input()
        if b == "666666":
            print("登陆成功！")
            break
        else :
            continue
else: print("3次用户名或者密码均有误！退出程序。")
```