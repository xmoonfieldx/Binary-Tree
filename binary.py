class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left==None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right==None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    
    def printtree(self):
        if root:
            if self.left:
                self.left.printtree()
            if self.right:
                self.right.printtree()
            print(self.data)
            
def printInorder(root):
  
    if root:
  
        # First recur on left child
        printInorder(root.left)
  
        # then print the data of node
        print(root.data),
  
        # now recur on right child
        printInorder(root.right)
  
  
# A function to do postorder tree traversal
def printPostorder(root):
  
    if root:
  
        # First recur on left child
        printPostorder(root.left)
  
        # the recur on right child
        printPostorder(root.right)
  
        # now print the data of node
        print(root.data),
  
  
# A function to do preorder tree traversal
def printPreorder(root):
  
    if root:
        
        # First print the data of node
        print(root.data),
  
        # Then recur on left child
        printPreorder(root.left)
  
        # Finally recur on right child
        printPreorder(root.right)
  
  
# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder traversal of binary tree is")
printPreorder(root)
  
print("\nInorder traversal of binary tree is")
printInorder(root)
  
print("\nPostorder traversal of binary tree is")
printPostorder(root)

                
