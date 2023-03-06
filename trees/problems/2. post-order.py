from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following the structure used for Binary Tree
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postOrder(root):
	# Your code goes here
    if root == None:
        return None
    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end=" ")


def print_tree_detailed(root):
    if root == None:
        return
    print(root.data, end=": ")
    if root.left:
        print("L", root.left.data, end=", ")
    if root.right:
        print("R", root.right.data, end="")
    print()
    print_tree_detailed(root.left)
    print_tree_detailed(root.right)


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

postOrder(root)
## output
# 4 5 2 6 7 3 1 


# print_tree_detailed(root)
## output
# 5: L 6, R 10
# 6: L 2, R 3 
# 2:
# 3: R 9
# 9:
# 10:

