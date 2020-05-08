# CS102 Assignment-02, On tree traversal Preorder Traversal
# 19CS091, RAVI SHANKAR SHARMA
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

def printPreorder(root):
    if root:
        print(root.val)
        printPreorder(root.left)
        printPreorder(root.right)

root = Node(1) 
root.left=Node(2) 
root.right=Node(3) 
root.left.left=Node(4) 
root.left.right=Node(5) 
root.right.left=Node(6)
root.right.right=Node(7)

print ("Preorder traversal of binary tree is")
printPreorder(root) 


#OUTPUT:

#Preorder traversal of binary tree is
#1
#2
#4
#5
#3
#6
#7