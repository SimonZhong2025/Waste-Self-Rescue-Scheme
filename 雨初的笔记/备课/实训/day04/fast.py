#coding:utf-8
'''
快速排序
'''
def fastSort(a):
    if(len(a)>=2):
        #找基准数mid，不需要中间，随便哪里
        mid=a[len(a)//2]
        left,right=[],[]#定义两个列表，分别存放大于基准数的元素和小于基准数的元素
        #从原列表中删除基准数
        a.remove(mid)
        #大于基准数的元素放right,小于基准数的元素放left,此刻并未排好序，只是分好了类
        for i in a:
            if i<mid:
                left.append(i)
            else:
                right.append(i)
        return fastSort(left)+[mid]+fastSort(right)
    else:
        return a




                 