print "This is singly - Linked List based implementation of Stack in Python"


class Node:
    def __init__(self,item,link):
        self.item = item
        self.next = link


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.size

    def pop(self):
        node = self.top
        self.top = self.top.next
        self.size -= 1
        return node.item

    def peek(self):
        if self.is_empty() is None:
            return None
        else:
            return self.top.item

    def push(self,item):
        self.top = Node(item,self.top)
        self.size += 1



print "enter the number of elements which you want to put in stack"

no_ele = int(raw_input())
my_stack = Stack()

for i in xrange(no_ele):
    value = int(raw_input())
    my_stack.push(value)


print my_stack.peek()

for i in xrange(no_ele):
    value = my_stack.pop()
    print value

print my_stack.is_empty()