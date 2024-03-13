import random

def partition(to_sort: list, left: int, right: int) -> int:
    pivot = to_sort[left]
    pointer = left
    
    for id in range(left + 1, right + 1):
        if to_sort[id] <= pivot:
            to_sort[pointer + 1], to_sort[id] = to_sort[id], to_sort[pointer + 1]
            pointer += 1
    
    to_sort[left], to_sort[pointer] = to_sort[pointer], to_sort[left]
    return pointer

def quick_sort(to_sort: list, mode: int = 0, left: int = 0, right: int = -1) -> None:
    if right == -1:
        right = len(to_sort) - 1
    
    if left < right:
        if mode == 1:
            pivot = random.randint(left, right)
            to_sort[left], to_sort[pivot] = to_sort[pivot], to_sort[left]
        
        pivot = partition(to_sort, left, right)
        
        while to_sort[pivot] == to_sort[left]:
            pivot += 1
            
            if pivot >= right:
                return
        
        quick_sort(to_sort, mode, left, pivot - 1)
        quick_sort(to_sort, mode, pivot + 1, right)