import numpy as np


def MergeorderedList(list1,list2):
    newlist = []
    a = 0
    b = 0
    while a < len(list1) and b < len(list2):
        if list1[a] < list2[b]:
            newlist.append(list1[a])
            a += 1
        else:
            newlist.append(list2[b])
            b += 1

    while a < len(list1):
        newlist.append(list1[a])
        a += 1

    while b < len(list2):
        newlist.append(list2[b])
        b += 1

    return newlist


def MergeSort(list):
    if len(list) <= 1:
        return list
    else:
        mid = len(list)/2

        lefthalf = MergeSort(list[:mid])
        righthalf = MergeSort(list[mid:])

        newList = MergeorderedList(lefthalf,righthalf)
        return newList



print "Enter the length of list "
k = int(raw_input())

list = []

for i in xrange(k):
    value = np.random.randint(1,100)
    #value = int(raw_input())
    list.append(value)

response = MergeSort(list)

print response