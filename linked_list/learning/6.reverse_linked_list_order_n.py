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
    inputList=[int (ele) for ele in input().split()]
    head=None
    tail=None
    for currData in inputList:
        if currData==-1:
            break
        newNode=Node(currData)
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
    return head
def reverse1(head):
    if head is None or head.next is None:
        return head
    smallHead=reverse1(head.next)
    curr=smallHead
    while curr.next is not None:
        curr=curr.next
    curr.next=head
    head.next=None
    return smallHead

def reverse2(head):
    if head is None or head.next is None:
        return head,head
    smallHead,smallTail=reverse2(head.next)
    smallTail.next=head
    head.next=None
    return smallHead,head
    

head=takeInput()
printLL(head)
head,tail=reverse2(head)
printLL(head)