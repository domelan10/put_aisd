import random

def partition(to_sort: list, left: int, right: int) -> int:
    pivot = to_sort[left]
    pointer_left = left
    pointer_right = right
    
    
    while True:
        while to_sort[pointer_left] < pivot:
            pointer_left += 1
        
        while to_sort[pointer_right] > pivot:
            pointer_right -= 1
        
        if pointer_left < pointer_right:
            to_sort[pointer_left], to_sort[pointer_right] = to_sort[pointer_right], to_sort[pointer_left]
            pointer_left += 1
            pointer_right -= 1
        else:
            return pointer_right

def quick_sort(to_sort: list, mode: int = 0, left: int = 0, right: int = -2) -> None:
    if right == -2:
        right = len(to_sort) - 1
    
    if left < right:
        if mode == 1:
            pivot_tmp = random.randint(left, right)
            to_sort[right], to_sort[pivot_tmp] = to_sort[pivot_tmp], to_sort[right]
        
        pivot = partition(to_sort, left, right)
        
        quick_sort(to_sort, mode, left, pivot)
        quick_sort(to_sort, mode, pivot + 1, right)
