# THis is the array based implementation of heap in Python
from array import Array

class MaxHeap:
    def __init__(self,maxsize):
        self.elements = Array(maxsize)
        self.count = 0

    # return the number of items in the heap
    def size(self):
        return self.count

    # return the maximum capacity of heap
    def capacity(self):
        return len(self.elements)

    # Add the value into the heap
    def add(self,item):
        if self.count < self.capacity():
            self.elements[self.count] = item
            self.count += 1
            self.siftip(self.count - 1)

    # Extract the maximum value form the heap
    def extract(self):
        if self.count > 0:
            value = self.elements[0]
            self.count -= 1
            self.elements = self.elements[self.count]
            self.siftdown(0)

    def siftup(self,index):
        if index > 0:
            parent = index
            if self.elemets[index] > self.elements[parent]:
                temp = self.elements[index]
                self.elements[index] = self.elements[parent]
                self.elements[parent] = temp
                self.siftup(parent)

    def siftdown(self,index):
        left = 2*index + 1
        right = 2*index + 2
        largest = index
        if left < self.count and self.elements[left] >= self.elements[largest]:
            largest = left
        elif right < self.count and self.elements[right] >= self.elements[largest]:
            largest = right
        if largest != index:
            swap(self.elements[index],self.elements[largest])
            self.siftdown(largest)



