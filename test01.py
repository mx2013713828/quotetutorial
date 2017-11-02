'''test github '''
import os
import random
def partition(li,start,end):
    li_len = end - start + 1
    if li_len < 2:
        raise ValueError("list which lenght is less than 2 ")
    key = li[end]
    middle_index = start
    for x in range(start,end):
        if li[x] < key:
            li[middle_index],li[x],li[middle_index]
            middle_index += 1
    li[end],li[middle_index] = li[middle_index],li[end]
    return middle_index
def sort(li,start,end):
    li_len = end - start + 1
    if li_len < 2:
        return li
    middle_index = partition(li,start,end)
    sort(li,start,middle_index - 1)
    sort(li,middle_index + 1,end)
    return li

def main():
    l = [1,11,4,6,9,24]

    li = sort(l, 0, len(l)-1)
    print(li)

if __name__ =='__main__':
    main()

