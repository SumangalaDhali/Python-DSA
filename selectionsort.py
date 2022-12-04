def selectionsort(List):
    n=len(List)
    for i in range(n-1):
        position = i
        for j in range(i+1,n):
            if List[j] < List[position]:
                position = j
        temp = List[i]
        List[i]=List[position]
        List[position] = temp

List=[50,80,90,60,40,70]
print("Original array\n",List)
print("sorted Array")
selectionsort(List)
print(List)

