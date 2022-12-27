from sys import stdin, setrecursionlimit
setrecursionlimit(10)

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def findNode(head, n) :
    # Write your code here.
    found_element = False
    element_position = 0
    while head is not None:
        if head.data == n:
            found_element = True
            break
        head = head.next
        element_position += 1
    if found_element:
        return element_position
    return -1

def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))
    # datas = [3,4,5,2,6,1,9,-1]
    
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


t = int(stdin.readline().rstrip()) # number of inputs

while t > 0 :

    head = takeInput()
    element_to_find = int(input())

    result = findNode(head, element_to_find)
    print(result)

