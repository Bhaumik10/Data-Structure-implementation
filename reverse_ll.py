def ReversePrint(head):
    if head == None:
        print None


    else:
        a = []
        while head.next != None:
            head = head.next
        a.append(head)