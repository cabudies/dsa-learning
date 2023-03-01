class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

btn1=BinaryTreeNode(1)
btn2=BinaryTreeNode(4)
btn3=BinaryTreeNode(5)

btn1.left=btn2
btn1.right=btn3

# print("btn1======", btn1)
print("btn1.data======", btn1.data)
# print("btn1.left======", btn1.left)
# print("btn1.right======", btn1.right)
if btn1.left:
    print("btn1.left child data==========", btn1.left.data)

if btn1.right:
    print("btn1.right child data==========", btn1.right.data)

