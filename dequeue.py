class DEQuearray:
    def __init__(self):
        self._data=[]

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data)==0

    def addfirst(self,e):
        self._data.insert(0,e)

    def addlast(self,e):
        self._data.append(e)

    def removefirst(self):
        if self.isempty():
            print("DEqueue is empty")
            return
        return self._data.pop(0)

    def removelast(self):
        if self.isempty():
            print("DEqueue is empty")
            return
        return self._data.pop()

    def front(self):
        if self.isempty():
            print("Dequeue is empty")
            return
        return self._data[0]

    def last(self):
        if self.isempty():
            print("Dequeue is empty")
            return
        return self._data[-1]


D=DEQuearray()
D.addfirst(4)
D.addlast(7)
print(D._data)
print(len(D))
print()



    

