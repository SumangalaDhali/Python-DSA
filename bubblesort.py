def bubblesort(A):
    n=len(A)
    for i in range(n-1):
        for j in range(n-1-i):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]

A=[8,9,3,4,1]
print("before sorting",A)
bubblesort(A)
print("After sorting",A)