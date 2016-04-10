class stack:
    def __init__(self):
        self.items = list()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            print None
        else:
            return self.items[len(self.items) - 1]


my_stack = stack()
max_stack = stack()

def push_element(x):
    my_stack.push(x)



def Del_Top_element():
    my_stack.pop()



def print_max_element():
    max = 0
    for i in xrange(my_stack.size()):
        if my_stack.peek() >= max:
            max = my_stack.pop()
    return max

print "Enter the number of inputs with query"
no_input = int(raw_input())

query_element_list = []

for i in xrange(no_input):
    query_element = raw_input()
    #print query_element
    query_element_list.append(query_element)

#print query_element_list

for i in xrange(len(query_element_list)):
    query_no = query_element_list[i].split(' ')
    #print 'length of query no ',len(query_no)
    if len(query_no) > 1:
        query = query_no[0]
        #print query
        element = query_no[1]
        if query == '1':
            push_element(element)
    else:
        query = query_no[0]
        if query == '2':
            Del_Top_element()
        elif query == '3':
           max_element = print_max_element()
           print max_element


