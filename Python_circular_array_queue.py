print "circular array based - queue implementation"

from array import Array

class Queue:
    def __init__(self,maxsize):
        self.count = 0
        self.front = 0
        self.back = maxsize - 1
        self.qArray = Array(maxsize)

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == len(self.qArray)

    def enqueue(self,item):
        maxsize = len(self.qArray)
        self.back = (self.back + 1) %  maxsize
        self.qArray[self.back] = item
        self.count += 1

    def dequeue(self):
        item = self.qArray[self.front]
        maxsize = len(self.qArray)
        self.front = (self.front + 1) % maxsize
        self.count -= 1
        return item


print "enter the no of elements"
n = int(raw_input())

q = Queue()


for i in xrange(n):
    element = int(raw_input())
    q.enqueue(element)

for i in xrange(q.size()):
    value = q.dequeue()
    print value
