
# Swap without extra variable
def swap(l1,l2):
    l1 = l1 + l2
    l2 = l1 - l2
    l1 = l1 - l2
    return l1,l2


#Swap with extra variable
def swap_extra_var(l1,l2):
    temp = l1
    l1 = l2
    l2 = temp
    return l1,l2


print "enter the value which you want to swap, vl1 & vl2"
l1 = int(raw_input())
l2 = int(raw_input())

response = swap(l1,l2)
response1  = swap_extra_var(l1,l2)


print response,response1