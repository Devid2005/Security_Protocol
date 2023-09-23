class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"{self.data}, {self.next}"
   
def rotate(list1, k):
    length = 0
    current = list1
    #print(current)
    while current != None:
        length += 1
        current = current.next

    k = k % length

    fast, slow = list1, list1

    for _ in range(k):
        fast = fast.next

    while fast.next != None:
        fast = fast.next
        slow = slow.next
    fast.next = list1
    head = slow.next
    slow.next = None
    return head



def linked(a,b):

    #print(type(a))
    llist = Node(a[0])
    head =  llist
    for i in range(1,len(a)):
        head.next = Node(a[i])
        head = head.next
    return rotate(llist, b)
    
def rotate_list_inv(llist1,k):
    length = 0
    current = llist1
    while current != None:
        length += 1
        current = current.next
    k = length - k
    return rotate(llist1, k)

