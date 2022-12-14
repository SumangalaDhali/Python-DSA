class Node:
    __Slots__='element','left','right'
    def __init__(self,element,left=None,right=None):
        self.element = element
        self.left=left
        self.right=left

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self,troot,e):
        temp = None
        while troot:
            temp = troot
            if e==troot.element:
                return
            elif e < troot.element:
                troot=troot.left
            elif e > troot.element:
                troot = troot.right
        n = Node(e)
        if self.root:
            if e < temp.element:
                temp.left=n
            else:
                temp.right=n
        else:
            self.root=n
    
    def inorder(self,troot):
        if troot:
            self.inorder(troot.left)
            print(troot.element,end=" ")
            self.inorder(troot.right)

B=BinarySearchTree()
B.insert(B.root,50)
B.insert(B.root,30)
B.insert(B.root,80)
B.insert(B.root,10)
B.insert(B.root,40)
B.insert(B.root,60)
B.inorder(B.root)






















    