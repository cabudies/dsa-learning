class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def print_tree(node):
    print(node.data, end=": ")
    if node.left:
        print(node.left.data, end=", ")
    if node.right:
        print(node.right.data, end=" ")
    print()

btn1=BinaryTreeNode(1)
btn2=BinaryTreeNode(2)
btn3=BinaryTreeNode(3)
btn4=BinaryTreeNode(4)

btn1.left=btn2
btn1.right=btn3
btn2.left=btn4

print_tree(node=btn1)
print_tree(node=btn2)
print_tree(node=btn3)
print_tree(node=btn4)
