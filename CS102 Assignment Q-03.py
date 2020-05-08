# CS102 Assignment-03,  Python Program for Post order and Depth first level search.
# 19BCS091, RAVI SHANKAR SHARMA

class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  
def printInorder(root): 
    if root: 
        printInorder(root.left)  
        print(root.val)
        printInorder(root.right) 
 
def printPostorder(root): 
    if root: 
        printPostorder(root.left) 
        printPostorder(root.right) 
        print(root.val)
  
def printPreorder(root): 
    if root: 
        print(root.val)
        printPreorder(root.left)  
        printPreorder(root.right) 

root=Node(1) 
root.left=Node(2) 
root.right=Node(3) 
root.left.left=Node(4) 
root.left.right=Node(5) 
root.right.left=Node(6)
root.right.right=Node(7)
print ("Preorder traversal of binary tree is")
printPreorder(root) 
print ("\nInorder traversal of binary tree is")
printInorder(root) 
print ("\nPostorder traversal of binary tree is")
printPostorder(root) 


#OUTPUT:

#Preorder traversal of binary tree is
#1
#2
#4
#5
#3
#6
#7
#
#Inorder traversal of binary tree is
#4
#2
#5
#1
#6
#3
#7
#
#Postorder traversal of binary tree is
#4
#5
#2
#6
#7
#3
#1