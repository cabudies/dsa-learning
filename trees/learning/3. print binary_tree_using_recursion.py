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


btn1=BinaryTreeNode(1)
btn2=BinaryTreeNode(2)
btn3=BinaryTreeNode(3)
btn4=BinaryTreeNode(4)

btn1.left=btn2
btn1.right=btn3
btn2.left=btn4

# print_tree(root=btn1)
print_tree_detailed(root=btn1)
