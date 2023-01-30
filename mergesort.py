def mergesort(A, left, right):
    if left < right:
        mid = (left + right) // 2

        mergesort(A, left, mid)
        mergesort(A, mid + 1, right)

        merge(A, left, mid, right)


def merge(A, left, mid, right):
    i, j = left, mid + 1
    L = []

    while i <= mid and j <= right:
        if A[i] < A[j]:
            L.append(A[i])
            i += 1
        else:
            L.append(A[j])
            j += 1

    if i <= mid:
        L.extend(A[i:mid + 1])

    if j <= right:
        L.extend(A[j:right + 1])

    for x, v in enumerate(L):
        A[left + x] = v


if __name__ == '__main__':
    A = [ 5, 2, 9, 8, 1]
    print(A)
    mergesort(A, 0, len(A) - 1)
    print(A)