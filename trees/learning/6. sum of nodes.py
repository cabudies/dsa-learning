class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def print_tree(root):
    if root == None:
        return
    print(root.data)
    print_tree(root.left)
    print_tree(root.right)


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


def tree_input():
    root = int(input("Enter node data: "))
    if root == -1:
        return None
    
    root = BinaryTreeNode(data=root)
    left_child = tree_input()
    right_child = tree_input()
    root.left = left_child
    root.right = right_child
    return root


def numNodes(root):
    if root==None:
        return 0
    leftCount=numNodes(root.left)
    rightCount=numNodes(root.right)
    return leftCount+rightCount+1


def sumNodes(root):
    if root==None:
        return 0
    leftCount=sumNodes(root.left)
    rightCount=sumNodes(root.right)
    return leftCount+rightCount+root.data

# root_node = tree_input()
btn1=BinaryTreeNode(1)
btn2=BinaryTreeNode(4)
btn3=BinaryTreeNode(5)

btn1.left=btn2
btn1.right=btn3

print_tree_detailed(root=btn1)
print("number of nodes=========", numNodes(btn1))
print("sum of nodes=========", sumNodes(btn1))

## 1
## 4
## -1
## -1
## 5
## -1
## -1
