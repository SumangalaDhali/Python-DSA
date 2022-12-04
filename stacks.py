class Stacksarray:
    def __init__(self):
        self.data=[]

    def __len__(self):
        return len(self.data)

    def isempty(self):
        return len(self.data)==0

    def push(self,e):
        self.data.append(e)

    def pop(self):
        if self.isempty():
            print("list is empty")
            return
        else:
            e = self.data.pop()
            return e

    def top(self):
        if self.isempty():
            print("list is empty")
            return
        else:
            e = self.data[-1]
            return e
    

s = Stacksarray()
s.push(1)
s.push(2)
s.push(3)
print(s.data)
i=s.pop()
print(i)
l=len(s)
print(l)
print(s.data)

