class Node:
    def __init__(self,element,next):
        self.element=element
        self.next = next

class Queuelinked:
    def __init__(self):
        self.front=None
        self.rear = None
        self.size = 0

    def __len__(self):
        return self.size

    def isempty(self):
        return self.size==0

    def addlast(self,e):
        newest = Node(e,None)
        if self.isempty():
            self.rear=newest
            self.front=newest
        else:
            self.rear.next=newest
            self.rear = newest
        self.size +=1

    def removefront(self):
        if self.isempty():
            print("list is empty")
            return
        else:
            e = self.front.element
            self.front=self.front.next
        if self.isempty():
            self.rear=None
        self.size-=1
        return e

    def display(self):
        p = self.front
        while p:
            print(p.element,end="<--")
            p=p.next
        print()
    
    def disfirst(self):
        return self.front.element


q = Queuelinked()
q.addlast(10)
q.addlast(20)
q.addlast(30)
q.addlast(40)
q.display()
n=q.removefront()
n2=q.removefront()
print(len(q))
print(q.disfirst())
q.display()






        


    


