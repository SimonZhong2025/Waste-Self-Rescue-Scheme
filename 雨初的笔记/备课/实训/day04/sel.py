#coding:utf-8
'''
选择排序

a.每一轮中，每个元素都和第一个元素比较，小的放最左边 ，一轮过后，最小的在最左边
b.执行X轮

每一轮都要有一个最小值的位置
3 2 7 1 8
'''
def selSort(a):
    for i in range(len(a)-1):
        min = i  #把每一轮的i作为当前这一轮最小值的下标
        for j in range(i+1,len(a)):
            if(a[j]<a[min]):
                min = j #此刻j代表的下标的元素更小，但不一定是最小，因为循环还没结束
        #第二层的循环执行结束，得到最小值的下标，进行互换
        t=a[i]
        a[i]=a[min]
        a[min]=t   
    return a
        
        
          