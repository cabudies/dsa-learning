
from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def length(head) :
    linked_list_length = 0
    while head is not None:
        linked_list_length += 1
        head = head.next
    return linked_list_length


#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    # datas = list(map(int, stdin.readline().rstrip().split(" ")))
    datas = [3,4,5,2,6,1,9,-1]
    print("datas======", datas)

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head



#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()



#main
# t = int(stdin.readline().rstrip()) # number of inputs
t = 1

while t > 0 :

    head = takeInput()
    print(length(head))

    t -= 1

