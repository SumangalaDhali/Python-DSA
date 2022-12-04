from re import I


def insertionsort(List):
    n=len(List)
    for i in range(1,n):
        cvalue=List[i]
        position = i
        while position>0 and List[position-1]>cvalue:
            List[position] = List[position-1]
            position = position-1

    List[position] = cvalue
    return List

print(insertionsort([3,5,5,8,9,7]))

