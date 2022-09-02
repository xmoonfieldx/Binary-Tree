class Root:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insert(self,data):
        if self.data==None:
            self.data=data
        elif data<self.data:
            if self.left==None:
                self.left=Root(data)
            else:
                self.left.insert(data)
        elif data>self.data:
            if self.right==None:
                self.right=Root(data)
            else:
                self.right.insert(data)
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
        
def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)
        
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
        
class Solution:
    def invertTree(self, root):
       if root == None:
           return
       root.left, root.right=root.right,root.left
       self.invertTree(root.left)
       self.invertTree(root.right)       

if __name__ == "__main__":
    root = Root(5)
    for i in range(7):
        if i==5:
            continue
        else:
            root.insert(i)
    inorder(root)
    print('\n')
    preorder(root)
    print()
    postorder(root)
    print()
    Solution().invertTree(root)
    inorder(root)
    
