from sys import stdin , setrecursionlimit
setrecursionlimit(10**6)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))
    # datas = [3, 4, 5, 2, 6, 1, 9, -1]

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


# To print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


def length_count(head, count):
    if head is None:
        return count
    return length_count(head.next, count+1)


def lengthRecursive(head):
    # A linked list, find and return the length of input LL recursively.
    # Write your code here
    return length_count(head, 0)
    
    

# Main
# t = int(stdin.readline().rstrip())
t = 1

while t > 0 :
    head = takeInput()
    ans=lengthRecursive(head)
    print(ans)
    t -= 1 