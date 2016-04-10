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
            return None
        else:
            return self.items[len(self.items) - 1]


my_stack = stack()
s = ''
def str_append(str_x):
    if my_stack.is_empty():
        str_final = ''
        str_final = str_final + str_x
        s = str_final
        my_stack.push(s)
    else:
        str_final = my_stack.peek()
        str_final = str_final + str_x
        s = str_final
        my_stack.push(s)


def get(k):
    K = int(k) - 1
    if my_stack.size() > 0 :
        s = my_stack.peek()
        for i in xrange(len(s)):
            if i == K :
                char = s[i]
                return char
    else:
        return None

def earse_element(k):
    K = int(k)
    top_ele_size = my_stack.peek()
    if K > len(top_ele_size):
        return None
    elif len(top_ele_size) == K:
        #my_stack.pop()
        s = ''
        my_stack.push(s)
    else:
        s = my_stack.peek()
        my_stack.push(s[:len(s)-K])


print "Enter the number of inputs with query"
no_input = int(raw_input())

query_element_list = []

for i in xrange(no_input):
    query_element = raw_input()
    query_element_list.append(query_element)


for i in xrange(len(query_element_list)):
    query_no = query_element_list[i].split(' ')
    if len(query_no) > 1:
        query = query_no[0]
        #print query
        str_element = query_no[1]
        #print str_element
        if query == '1':
            s = str_append(str_element)
            #print s
        elif query == '2':
            new_s = earse_element(str_element)
            #
        elif query == '3':
            return_char = get(str_element)
            print return_char
    else:
        my_stack.pop()
        s = my_stack.peek()
        