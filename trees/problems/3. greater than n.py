from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def countNodesGreaterThanX(root, x, count) :
    if root == None:
        return count
    if root.data>x:
        count = count + 1
    count = countNodesGreaterThanX(root.left, x, count)
    count = countNodesGreaterThanX(root.right, x, count)
    return count

#Taking level-order input using fast I/O method
def takeInput():
    # levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    levelOrder = "1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1"
    levelOrder = list(map(int, levelOrder.split(" ")))
    start = 0

    length = len(levelOrder)

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root

# Main
root = takeInput()
# x = int(stdin.readline().strip())
x = 2

count = countNodesGreaterThanX(root, x, 0)
print(count)