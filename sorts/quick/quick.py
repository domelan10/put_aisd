def partition(to_sort: list, left: int, right: int) -> int:
    pivot = to_sort[right]
    pointer = left - 1
    
    for id in range(left, right):
        if to_sort[id] <= pivot:
            pointer += 1
            to_sort[pointer], to_sort[id] = to_sort[id], to_sort[pointer]
    
    to_sort[right], to_sort[pointer + 1] = to_sort[pointer + 1], to_sort[right]
    return pointer + 1

def quick_sort(to_sort: list, left: int, right: int) -> None:
    if left < right:
        pivot = partition(to_sort, left, right)
        
        quick_sort(to_sort, left, pivot - 1)
        quick_sort(to_sort, pivot + 1, right)