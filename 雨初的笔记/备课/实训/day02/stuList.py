#coding:utf-8
print('---欢迎来到XXX学生成绩录入系统---')
#\t空格
print('1.查看成绩 \t2.修改成绩\t3.添加成绩\t4.删除成绩')
#初始化两个列表，存放学生姓名+成绩
#驼峰式命名法
stuName = ['张三','李四']
stuScore = [70,80]
#用户输入的永远是字符串类型
choose = input('请输入你的操作')
if choose == '1':
    for i in stuName:
        #stuName.index(i) i在stuName中的下标值
        print(i,"的成绩为",stuScore[stuName.index(i)])
if choose == '2':
    name = input('请输入要修改的学生姓名')
    if name in stuName:
        score = input('请输入修改后的成绩')
        stuScore[stuName.index(name)] = score
        for i in stuName:
        #stuName.index(i) i在stuName中的下标值
            print(i,"的成绩为",stuScore[stuName.index(i)])
    else:
        print('学生不存在！')

        
        
        