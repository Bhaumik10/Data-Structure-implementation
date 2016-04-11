print " This is the python list based implementation of Queue"

class Queue:
    def __init__(self):
        self.qList = list()

    def is_empty(self):
        return len(self) == 0

    def size(self):
        return len(self.qList)

    def enqueue(self,item):
        self.qList.append(item)

    def dequeue(self):
        return self.qList.pop(0)

print "enter the no of elements"
n = int(raw_input())

q = Queue()


for i in xrange(n):
    element = int(raw_input())
    q.enqueue(element)

for i in xrange(q.size()):
    value = q.dequeue()
    print value

