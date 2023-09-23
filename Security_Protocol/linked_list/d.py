
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
    def __repr__(self):
        return f"{self.data}, ({self.next})"


def linked(a):

    print(type(a))
    llist = Node(a[0])
    head =  llist
    for i in range(1,len(a)):
        head.next = Node(a[i])
        head = head.next
    print(llist.next)
    print(type(llist))

