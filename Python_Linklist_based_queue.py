class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        self.qhead = None
        self.qtail = None
        self.count = 0

    def is_empty(self):
        return self.qhead is None

    def size(self):
        return self.count

    def enqueue(self,item):
        node = Node(item)
        if self.qhead is None:
            self.qhead = node
        else:
            self.qtail.next = node
        self.qtail = node
        self.count += 1

    def dequeue(self):
        node = self.qhead
        if self.qhead is self.qtail:
            self.qtail = None
            self.qhead = self.qhead.next
            self.count -= 1
            return node.item

print "enter the no of elements"
n = int(raw_input())

q = Queue()


for i in xrange(n):
    element = int(raw_input())
    q.enqueue(element)

for i in xrange(n):
    value = q.dequeue()
    print value
