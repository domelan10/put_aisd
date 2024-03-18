import random

def partition(to_sort: list, left: int, right: int) -> int:
    pivot = to_sort[left]    
    pointer_left = left + 1
    pointer_right = right
    
    while True:
        while pointer_left <= pointer_right and to_sort[pointer_left] <= pivot:
            pointer_left += 1
        
        while pointer_left <= pointer_right and to_sort[pointer_right] >= pivot:
            pointer_right -= 1
        
        if pointer_right < pointer_left:
            break
        else:
            to_sort[pointer_left], to_sort[pointer_right] = to_sort[pointer_right], to_sort[pointer_left]
    
    to_sort[left], to_sort[pointer_right] = to_sort[pointer_right], to_sort[left]
    return pointer_right

def quick_sort(to_sort: list, mode: int = 0, left: int = 0, right: int = -2) -> None:
    if right == -2:
        right = len(to_sort) - 1
    
    if left < right:
        if mode == 1:
            pivot = random.randint(left, right)
            to_sort[left], to_sort[pivot] = to_sort[pivot], to_sort[left]
        
        pivot = partition(to_sort, left, right)
        
        # print(left, pivot, right)
        
        quick_sort(to_sort, mode, left, pivot - 1)
        quick_sort(to_sort, mode, pivot + 1, right)