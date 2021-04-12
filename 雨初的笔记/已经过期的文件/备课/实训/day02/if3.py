#coding:utf-8
'''
实现百分制分数转换为等级制分数
让用户输入一个分数 0-100
60分以下输出E
60分以上(包含)输出D
70分以上(包含)输出C
80分以上(包含)输出B
90分以上(包含)输出:成绩为A
'''
score = int(input('请输入你的分数:'))
if score>=90:
    print('成绩为A')
elif score>=80:
    print('成绩为B')
elif score>=70:
    print('成绩为C')
elif score>=60:
    print('成绩为D')
else:
    print('成绩为E')