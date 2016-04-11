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
            None
        else:
            return self.items[len(self.items) - 1]

my_stack = stack()
max_area = 0
area = 0

print "Enter the number of buildings"
no_input = int(raw_input())

building_with_area = []

for i in xrange(no_input):
    ar = int(raw_input())
    building_with_area.append(ar)

print building_with_area


for i in xrange(len(building_with_area)):
    if my_stack.is_empty() or building_with_area[my_stack.peek()] <= building_with_area[i]:
        my_stack.push(i)
    else:
        top = my_stack.peek()
        if my_stack.is_empty():
            area = building_with_area[top] * i
        else:
            area = building_with_area[top] * (i - my_stack.peek() - 1)

        if area > max_area:
            max_area = area

while my_stack.is_empty() != True:
    top = my_stack.peek()

    if my_stack.is_empty():
            area = building_with_area[top] * i
    else:
        area = building_with_area[top] * (i - my_stack.peek() - 1)

    if area > max_area:
        max_area = area

print max_area