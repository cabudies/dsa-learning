import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBST(lst):
    if len(lst) == 0:
        return None

    sorted_list = sorted(lst)
    middle_element = sorted_list[0]
    if len(sorted_list) % 2 == 1:
        middle_element = sorted_list[int(len(lst)/2)]

    root = BinaryTreeNode(data=middle_element)
    root.left = constructBST(lst=sorted_list[:int(len(lst)/2)])
    root.right = constructBST(lst=sorted_list[int(len(lst)/2)+1:])
    
    return root


def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
# n=int(input())
n=7
if(n>0):
    # lst=[int(i) for i in input().strip().split()]
    lst=[1, 2, 3, 4, 5, 6, 7]
    # lst=[1]
else:
    lst=[]
# root=constructBST(lst)
# preOrder(root)

root = constructBST(lst)
print("root===========", root)
# print("root.data===========", root.data)
preOrder(root)
