#binary search algorithem iterative method
#in binary search array must be in sorted order

'''
#binary search iterative method
def binarysearch_iterative(A,key,L,R):
    while L<=R:
        mid=(L+R)//2
        if key==A[mid]:
            return mid
        elif key<=A[mid]:
            R=mid-1
        elif key>=A[mid]:
            L=mid+1
    return -1
A=[10,20,30,40,50]
result=binarysearch_iterative(A,20,0,len(A)-1)
if result==-1:
    print("key is not found at array")
else:
    print("key is found at index:",result)
'''

#Binarysearch recurssive method
def binarysearch_recurssive(A,key,L,R):
    if L>R:
        return False
    else:
        mid=(L+R)//2
        if key == A[mid]:
            return mid
        elif key >A[mid]:
            return binarysearch_recurssive(A,key,mid+1,R)
        else:
            return binarysearch_recurssive(A,key,L,mid-1)

A=[10,20,30,40,50]
result=binarysearch_recurssive(A,20,0,len(A)-1)
if result==-1:
    print("key not found at array")
else:
    print("key is found at index:",result)

