import numpy as np

def swap(l1,l2):
    temp = l1
    l1 = l2
    l2 = temp
    return l1,l2


def partition(list,start,end):
    pivot = list[end]
    pIndex = start

    for i in range(start,end-1):
        if list[i] <= pivot:
            swap(list[i],list[pIndex])
            pIndex += 1
    swap(list[pIndex],list[end])
    return pIndex

def quickSort(list,start,end):
    if start >= end:
        return
    else:
        pIndex = partition(list,start,end)
        quickSort(list,start,pIndex-1)
        quickSort(list,pIndex+1,end)


print "Enter the length of list "
k = int(raw_input())

list = []

for i in xrange(k):
    value = np.random.randint(1,100)
    #value = int(raw_input())
    list.append(value)

print list
start = 0
end = len(list)

print end
response = quickSort(list,start,end)

print response