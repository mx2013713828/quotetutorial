#coding=utf-8
import random
#定义三个常量用来表示下限、上限和数组长度
start = 1
stop = 1000
length = 100
#定义一个新数组存放随机数
list = []
def random_list(start, stop, length):
    for i in range(length):
        list.append(random.randint(start, stop))  #把生成的随机数插入到list
    return list

print("随机生成的数组为：")
print(random_list(start,stop,length))
print("排序后的数组为：")

#start   起始位置
#end     结束位置
#pivot   基准位
#index   空位

#将数组以基准元素分为左右两部分
def sort(list,start,end):
    pivot = list[start]        #选首个元素为基准数
    while start < end:         #判断数组中元素至少等于二
        while start < end and list[end] >= pivot:       #从左向右
            end -= 1
        while start < end and list[end] < pivot:        #从右向左
            list[start] = list[end]
            start += 1
            list[end] = list[start]                 #当起始位置==结束位置
        list[start] = pivot                         #将基准元素赋值到空位
    return start
#利用递归快速排序
def quick_sort(list, start, end):
    if start < end:
        index = sort(list,start,end)
        quick_sort(list,start,index)
        quick_sort(list,index+1,end)

quick_sort(list,0,len(list)-1)
print(list)




#时间复杂度：O(nlog n)
#空间复杂度：0(logn)
#要为递归提供所需的辅助空间