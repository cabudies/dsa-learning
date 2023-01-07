class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printLL(head):
    while head is not None:
        print(str(head.data)+"->",end='')
        head=head.next
    print("None")
    return

def length(head):
    count=0
    while head is not None:
        count=count+1
        head=head.next
    return count

def insertAtIR(head,i,data):
    if i<0:
        return head
    if i==0:
        newNode=Node(data)
        newNode.next=head
        return newNode
    if head is None:
        return None
    smallHead=insertAtIR(head.next,i-1,data)
    head.next=smallHead
    return head

def insertAtI(head,i,data):
    if i<0 or i>length(head):
        return head
    count=0
    prev=None
    curr=head
    while count<i:
        
        
        prev=curr
        curr=curr.next
        count=count+1
    newNode=Node(data)
    if prev is not None:
        prev.next=newNode
    else:
        head=newNode
    
    newNode.next=curr
    return head

def takeInput():
    # inputList=[int (ele) for ele in input().split()]
    inputList=[1,2,3,4,5]
    head=None
    tail=None
    for currData in inputList: # currData = 1, 2
        if currData==-1:
            break
        newNode=Node(currData) # newNode = Node(data=1), Node(data=2)
        if head is None:
            head=newNode # current node same # head = Node(data=1)
            tail=newNode # previous node same # tail = Node(data=1)
        else:
            tail.next=newNode # tail.next (Node(data=1)) = Node(data=1), 
            # tail.next (Node(data=1, next=Node(1))) = Node(data=2) -> tail (Node(data=1, next=Node(2)))
            tail=newNode # tail = Node(data=1), tail = Node(data=2)
    return head

def reverse1(head): 
    # Node(data=1, next=Node(data=2, next=Node(data=3, next=None)))
    # head = Node(1)
    # head.next = Node(2)
    if head is None or head.next is None:
        return head
    smallHead=reverse1(head.next) # smallHead = Node(3)
    curr=smallHead # curr = Node(3)
    while curr.next is not None: # curr (Node(data=3,next=None))
        curr=curr.next
    curr.next=head
    head.next=None
    return smallHead

head=takeInput()
printLL(head)
# head=reverse1(head)
# printLL(head)