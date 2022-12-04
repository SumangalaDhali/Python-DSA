class Node:
    __Slots__='element','left','right'
    
    def __init__(self,element,left=None,right=None):
        self.element=element
        self.left=left
        self.right=right

class Binarysearch:
    def __init__(self):
        self.root=None
    
    def rinsert(self,troot,e):
        if troot:
            if e < troot.element:
                troot.left = self.rinsert(troot.left,e)
            elif e > troot.element:
                troot.right = self.rinsert(troot.right,e)
        else:
            n = Node(e)
            troot=n
        return troot


    def inorder(self,troot):
        if troot:
            self.inorder(troot.left)
            print(troot.element,end=" ")
            self.inorder(troot.right)

B = Binarysearch()
B.root=B.rinsert(B.root,50)
B.rinsert(B.root,50)
B.rinsert(B.root,30)
B.rinsert(B.root,80)
B.rinsert(B.root,10)
B.rinsert(B.root,40)
B.rinsert(B.root,60)
B.inorder(B.root)







    
