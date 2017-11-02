import random
import os
start = 1
stop = 10000000
length = 1000000
list = []
def random_list(start,stop,length):
    for i in range(length):
        list.append(random.randint(start,stop))
    return list

print("list = ")
print(random_list(start,stop,length))
print("over list = ")

def sort(list,start,end):
    pivot = list[start]
    while start < end:
        while start < end and list[end] >= pivot:
            end -= 1
        while start < end and list[end] < pivot:
            list[start] = list[end]
            start += 1
            list[end] = list[start]
        list[start] =pivot
    return start

def quick_sort(list,start,end):
    if start < end:
        index = sort(list,start,end)
        quick_sort(list,start,index)
        quick_sort(list,index+1,end)
quick_sort(list,0,len(list)-1)
print(list)
with open('sort.text','w') as fd:
    for x in list:
        fd.write(str(x) + ',')

