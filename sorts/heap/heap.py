def heapify(to_sort: list, n: int, i: int) -> list:
    lg = i #largest
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and to_sort[left] > to_sort[lg]:
        lg = left

    if right < n and to_sort[right] > to_sort[lg]:
        lg = right

    if lg != i:
        to_sort[i], to_sort[lg] = to_sort[lg], to_sort[i]
        heapify(to_sort, n, lg)

def heap_sort(to_sort: list) -> list:
    n = len(to_sort)

    for i in range(n // 2 - 1, -1, -1):
        heapify(to_sort, n, i)

    for i in range(n - 1, 0, -1):
        to_sort[i], to_sort[0] = to_sort[0], to_sort[i]
        heapify(to_sort, i, 0)

    return to_sort
