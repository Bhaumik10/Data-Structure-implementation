class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def get_data(self):
        return self.data

    def set_next(self,new_next):
        self.next_node= new_next


class LinkedList(object):
    def insert(self):
        self.data
        return "successfully inserted"


if(head == NULL) {
    temp->next = NULL;
} else {
    temp->next = head;
}
head = temp;
return head;