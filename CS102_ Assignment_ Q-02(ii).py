# CS102 Assignment-02, On tree traversal Postorder Traversal
# 19BCS091, RAVI SHANKAR SHARMA
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
 
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val)

root = Node(1) 
root.left=Node(2) 
root.right=Node(3) 
root.left.left=Node(4) 
root.left.right=Node(5) 
root.right.left=Node(6)
root.right.right=Node(7)

print ("\nPostorder traversal of binary tree is")
printPostorder(root) 


#OUTPUT:

#Postorder traversal of binary tree is
#4
#5
#2
#6
#7
#3
#1