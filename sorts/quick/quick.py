import random

def partition(to_sort: list, left: int, right: int, mode: int = 0) -> int:
    match mode:
        case 0:
            pivot = to_sort[left]
        case 1:
            pivot = random.randint(left, right)
            to_sort[left], to_sort[pivot] = to_sort[pivot], to_sort[left]
            pivot = to_sort[pivot]

    pointer = right
    
    for id in range(left, right):
        if to_sort[id] >= pivot:
            pointer -= 1
            to_sort[pointer], to_sort[id] = to_sort[id], to_sort[pointer]
    
    to_sort[right], to_sort[pointer + 1] = to_sort[pointer + 1], to_sort[right]
    return pointer + 1

def quick_sort(to_sort: list, mode: int = 0, left: int = 0, right: int = -1) -> None:
    if right == -1:
        right = len(to_sort) - 1
    
    if left < right:
        pivot = partition(to_sort, left, right, mode)
        
        quick_sort(to_sort, mode, left, pivot - 1)
        quick_sort(to_sort, mode, pivot + 1, right)