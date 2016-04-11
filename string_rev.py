s = "i love u...i fuck u"

print s[::-1]


def insert_l(list,x ):
    a = list
    a.insert(x[0],x[1])
    #remove_item = a[4]
    #print a.remove('d')
    print a
    return a

list = ['a','b','c','d']
x = (0,list[3])


p = insert_l(list,x)
print type(p)
del p[3+1]
print p