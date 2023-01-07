from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def removeDuplicates(head) :
    initial_head = head
    previous_head = initial_head

    while head is not None:
        if previous_head.data == head.data:
            previous_head.next = head.next
        else:
            previous_head = head
        head = head.next

    return initial_head

#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))
    # datas = [1, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 7, -1]
    # datas = [10, 20, 30, 40, 50, -1]
    # datas = [10, 10, 10, 10, -1]

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
# t = int(stdin.readline().strip())
t = 1

while t > 0 :
    head = takeInput()

    head = removeDuplicates(head)
    printLinkedList(head)

    t -= 1