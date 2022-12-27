from sys import stdin

# Following is the Node class already written for the Linked List.
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def length(head):
    count = 0
    while head is not None:
        head = head.next
        count += 1
    return count


def deleteNode(head, pos) :
    if pos<0 or pos>=length(head):
        return head
    count = 0
    node_to_be_removed = None
    initial_head = head
    
    if pos == 0:
        initial_head = initial_head.next
    else:
        while head is not None:
            if pos-1 == count:
                node_to_be_removed = head
            elif (pos+1 == count) and (node_to_be_removed is not None):
                node_to_be_removed.next = head
            
            count += 1
            head = head.next

    return initial_head


# Taking Input Using Fast I/O.
def takeInput() :
    head = None
    tail = None

    # datas = list(map(int, stdin.readline().rstrip().split(" ")))
    datas = [3, 4, 5, 2, 6, 1, 9, -1]
    # datas = [10, 20, 30, 40, 50, 60, -1]

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



# To print the linked list.
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


# Main.
# t = int(stdin.readline().strip())
t = 1

while t > 0 :
    
    head = takeInput()
    # pos = int(stdin.readline().rstrip())
    # pos = 3
    # pos = 6
    pos = 0

    head = deleteNode(head, pos)
    printLinkedList(head)

    t -= 1
