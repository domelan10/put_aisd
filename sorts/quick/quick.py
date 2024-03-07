def partition(to_sort: list, left: int, right: int) -> int:
    print(to_sort)
    pivot = to_sort[right]
    pointer = left - 1
    
    for id in range(left, right):
        if to_sort[id] <= pivot:
            pointer += 1
            to_sort[pointer], to_sort[id] = to_sort[id], to_sort[pointer]
    
    to_sort[right], to_sort[pointer + 1] = to_sort[pointer + 1], to_sort[right]
    print(to_sort)
    return pointer + 1

def quick_sort(to_sort: list, left: int, right: int) -> None:
    if right < left:
        pivot = partition(to_sort, left, right)
        print(to_sort)
        
        quick_sort(to_sort, left, pivot - 1)
        quick_sort(to_sort, pivot + 1, right)
        print(to_sort)