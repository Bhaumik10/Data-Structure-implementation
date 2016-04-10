class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.qlist = list()

    def is_empty(self):
        return len(self) == 0

    def size(self):
        return len(self.qlist)

    def enqueue(self,data):
        self.qlist.append(data)

    def dequeue(self):
        self.qlist.pop(0)


def BFStRaverse(binTree):
    q = Queue()
    q.enqueue(binTree)

    while q.is_empty() is not None:
        node = q.dequeue()
        print node.data

        if node.left is not None:
            q.enqueue(node.left)

        if node.right is not None:
            q.enqueue(node.right)