print "This is Array based implementation of Stack in Python"

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)



print "enter the number of elements which you want to put in stack"

no_ele = int(raw_input())
my_stack = Stack()

for i in xrange(no_ele):
    value = int(raw_input())
    my_stack.push(value)





length_stack = my_stack.size()

print my_stack.peek()

for i in xrange(length_stack):
    value = my_stack.pop()
    print value


print my_stack.is_empty()
