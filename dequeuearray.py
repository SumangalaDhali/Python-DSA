class dequeuarry:
    def __init__(self):
        self.data=[]


    def __len__(self):
        return len(self.data)

    def isempty(self):
        return len(self.data)==0

    def addfront(self,e):
        self.data.insert(0,e)

    def addrear(self,e):
        self.data.append(e)

    def removefront(self):
        return self.data.pop(0)

    def removerear(self):
        return self.data.pop()

    def display(self):
        if self.isempty():
            print("list is empty")
        else:
            for i in range(len(self.data)):
                print(self.data[i],end="-->")

    def disfirst(self):
        return self.data[0]

    def dislast(self):
        return self.data[-1]

q=dequeuarry()
q.addfront(1)
q.addfront(2)
q.addrear(3)
q.addrear(4)
q.display()
print()
print(q.disfirst())
print(q.dislast())
print(q.removefront())
print(q.removerear())
q.display()


