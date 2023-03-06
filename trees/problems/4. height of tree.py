from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following the structure used for Binary Tree
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def heightOfTree(root):
    if root is None:
        return 0
    left_depth = heightOfTree(root.left)
    right_depth = heightOfTree(root.right)
    final_depth = left_depth

    if left_depth < right_depth:
        final_depth = right_depth
    return final_depth + 1


#Taking level-order input using fast I/O method
def takeInput():
    # levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    levelOrder = "10 20 30 40 50 -1 -1 -1 -1 -1 -1"
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

height = heightOfTree(root)
print("height========", height)
## output
# 3
