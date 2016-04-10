import numpy as np

def BinSearch(list,target):
    len_of_list = len(list)

    if len_of_list == 0:
        return False
    elif len_of_list == 1 and list[0] == target:
        return True
    elif len_of_list >= 2:
        low = 0
        high = len_of_list - 1

        while low <= high:
            mid = (low+high)/2

            if list[mid] == target:
                return True
            elif target < list[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return False
    else:
        return False


print "Please enter the length of list"
k = int(raw_input())

list = []

for i in xrange(k):
    value = np.random.randint(1,100)
    #value = int(raw_input())
    list.append(value)

list.sort()

print "Enter the value which you want to check"
target = int(raw_input())

response = BinSearch(list,target)

print "Result of search activity is : " , response