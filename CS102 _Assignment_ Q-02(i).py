# CS102 Assignment-02, On tree traversal Inorder Traversal
# 19BCS091, RAVI SHANKAR SHARMA 
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

def printInorder(root):
    if root:
        printInorder(root.left)  
        print(root.val)
        printInorder(root.right) 

root = Node(1) 
root.left=Node(2) 
root.right=Node(3) 
root.left.left=Node(4) 
root.left.right=Node(5) 
root.right.left=Node(6)
root.right.right=Node(7)

print ("\nInorder traversal of binary tree is")
printInorder(root) 


#OUTPUT:

#Inorder traversal of binary tree is
#4
#2
#5
#1
#6
#3
#7