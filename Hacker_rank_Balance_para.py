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
        if s.is_empty():
            print s.is_empty()
        else:
            return self.items[len(self.items) - 1]

def pair(a,b):
    open_s = a
    close_s = b
    if open_s =='(' and close_s == ')':
        return True
    elif open_s =='[' and close_s == ']':
        return True
    elif open_s =='{' and close_s == '}':
        return True
    else:
        return False


#test cases"

s = stack()

no_test_case = int(raw_input())
expression_list = []

for i in xrange(no_test_case):
    expression = raw_input()
    expression_list.append(expression)

#print expression_list

for i in xrange(len(expression_list)):
    for j in xrange(len(expression_list[i])):
        if expression_list[i][j] == '{' or expression_list[i][j] == '[' or expression_list[i][j] == '(':
            s.push(expression_list[i][j])
        elif expression_list[i][j] == '}' or expression_list[i][j] == ']' or expression_list[i][j] == ')':
            if pair(s.peek(), expression_list[i][j]) == True:
                s.pop()
                flag = 'YES'
            else:
                flag = 'NO'
                break
        elif s.is_empty():
            flag = 'YES'
        else:
            flag = 'NO'

    print flag
