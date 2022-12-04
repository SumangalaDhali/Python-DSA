class qarray:
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def isempty(self):
        return len(self.array)==0

    def enqueue(self,e):
        self.array.append(e)


    def dequeue(self):
        if self.isempty():
            print("queue is empty")
            return 0
        else:
            return self.array.pop(0)

    def front(self):
        return self.array[0]


a=qarray()
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
print(a.array)
ele=a.dequeue()
print(len(a.array))
print(ele)




