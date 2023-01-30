def quicksort(A, low, high):
    if low < high:
        pi = partition(A, low, high)
        quicksort(A, low, pi - 1)
        quicksort(A, pi + 1, high)


def partition(A, low, high):
    i, j = low + 1, high  # low + 1 because we dont have do while loop
    pivot = A[low]

    while True:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] > pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            break

    A[low], A[j] = A[j], A[low]

    return j

if __name__ == '__main__':
    A = [9, 12, 3, 15, 6]
    print("Array before Sorting")
    print(A)
    quicksort(A, 0, len(A) - 1)
    print("Array after Sorting")
    print(A)