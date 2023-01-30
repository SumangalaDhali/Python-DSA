'''
---syntax---
LinearSearch(array, key)
  for each item in the array
    if item == value
      return its index
'''
'''
def linearsearch(array,key):
    for i in range(0,len(array)):
        if array[i]==key:
            return i
    return -1
array=[2,4,7,9,0]
key=4
result=linearsearch(array,key)
if (result==-1):
    print("key not found")
else:
    print("found index at:",result)
'''
def linearsearch(array,key):
    index=0
    while index<len(array):
        if array[index]==key:
            return index
        index=index+1
    return -1

array=[1,3,2,7]
key=3
result=linearsearch(array,key)
if result==-1:
    print("key not found")
else:
    print("found index at:",result)

