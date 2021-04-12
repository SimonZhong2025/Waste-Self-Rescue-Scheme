#coding:utf-8
'''
假设用户名为'admin',密码为'psw123'
让用户从控制台输入账号密码，匹配则输入登录成功，失败则输出登录失败
'''
name = input('请输入用户名:')
psw = input('请输入密码')
if name == 'admin' and psw == 'psw123':
    print('登录成功')
else:
    print('登录失败')