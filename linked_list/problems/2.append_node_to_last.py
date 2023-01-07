from sys import stdin, setrecursionlimit
setrecursionlimit(11000)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def appendLastNToFirst(head, n) :
    initial_head = head
    count = 1
    new_head = None
    new_head_starting_position = None
    previous_node = None

    while head is not None:
        if count == n:
            new_head = head
        elif count == n-1:
            previous_node = head
        head = head.next
        count += 1

    if new_head:
        new_head_starting_position = new_head

    while new_head:
        if new_head == previous_node:
            new_head.next = None
            break
        if new_head.next is None:
            new_head.next = initial_head
        new_head = new_head.next
    
    return new_head_starting_position


#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    # datas = list(map(int, stdin.readline().rstrip().split(" ")))
    # datas = [1, 2, 3, 4, 5, -1]
    datas = [10, 6, 77, 90, 61, 67, 100, -1]

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
# t = int(stdin.readline().rstrip())
t = 1

while t > 0 :

    head = takeInput()
    # n = int(stdin.readline().rstrip())
    # n = 3
    n = 4

    head = appendLastNToFirst(head, n)
    printLinkedList(head)

    t -= 1 