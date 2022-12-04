class Node:
    __Slots__="element","next"
    def __init__(self,element,next):
        self.element=element
        self.next=next

class Stacklinked:
    def __init__(self):
        self.top=None
        self.size= 0

    def __len__(self):
        return self.size

    def isempty(self):
        return self.size==0

    def addfirst(self,e):
        newest = Node(e,None)
        if self.isempty():
            self.top=newest
        else:
            newest.next=self.top
            self.top=newest
        self.size+=1

    def removefirst(self):
        if self.isempty():
            print("stack is empty")
            return 
        else:
            e=self.top.element
            self.top=self.top.next
        if self.isempty():
            self.top=None
        self.size-=1
        return e
        

    def display(self):
        p=self.top
        while p:
            print(p.element,end="-->")
            p=p.next
        print()

    def peek(self):
        if self.isempty():
            print("stack is empty")
            return
        return self.top.element

s1=Stacklinked()
s1.addfirst(1)
s1.addfirst(2)
s1.addfirst(3)
s1.addfirst(4)
s1.display()
ele=s1.removefirst()
s1.display()
print(ele)
t=s1.peek()
print(t)
print(len(s1))



            

            