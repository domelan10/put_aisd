from insertion.insertion import insertion_sort 
from selection.selection import selection_sort
from merge.merge import merge_sort
from quick.quick import quick_sort
from heap.heap import heap_sort
from bubble.bubble import bubble_sort
from shell.shell import shell_sort
from counting.counting import counting_sort

from py_tests.test_random import test_random
from py_tests.test_increase import test_increase
from py_tests.test_decrease import test_decrease
from py_tests.test_hill import test_hill
from py_tests.test_stable import test_stable

from time import time
import sys
sys.setrecursionlimit(1000000000)

def main(sort: str = "-1", test: str = "-1", test_size: int = 0) -> float:
    if sort == "-1":
        print("Sort types: insertion, selection, merge, quick_left, quick_random, heap, bubble, shell, counting") # remove: merge, bubble, counting
        sort = input("Select sort to test: ")
    if test == "-1":
        print("Test types: random, increase, decrease, hill, stable")
        test = input("Select test type: ")
    if test_size == 0:
        test_size = int(input("Select number of elements to test: "))
    
    if test_size <= 1:
            print("Number of elements to test must be greater than 1.")
            main()
            return 0
    
    match(test):
        case "random" | "1":
            data = test_random(test_size)
        case "increase" | "2":
            data = test_increase(test_size)
        case "decrease" | "3":
            data = test_decrease(test_size)
        case "hill" | "4":
            data = test_hill(test_size)
        case "stable" | "5":
            data = test_stable(test_size)
        case default:
            print("Unknown test type.")
            main()
            return 0
    
    # print("Unsorted array: ", data)
    
    match(sort):
        case "insertion" | "1":
            start = time()
            data = insertion_sort(data)
            end = time()
        case "selection" | "2":
            start = time()
            data = selection_sort(data)
            end = time()
        case "merge" | "3":
            start = time()
            data = merge_sort(data)
            end = time()
        case "quick_left" | "4":
            start = time()
            quick_sort(data, 0)
            end = time()
        case "quick_random" | "5":
            start = time()
            quick_sort(data, 1)
            end = time()
        case "heap" | "6":
            start = time()
            data = heap_sort(data)
            end = time()
        case "bubble" | "7":
            start = time()
            data = bubble_sort(data)
            end = time()
        case "shell" | "8":
            start = time()
            data = shell_sort(data)
            end = time()
        case "counting" | "9":
            start = time()
            data = counting_sort(data)
            end = time()
        case default:
            print("Unknown sort type.")
            main()
            return 0

    print("\tTime: ", end - start)
    print("\t\tdone")
    # print("Sorted array: ", data)
    
    return end - start


if __name__ == '__main__':
    main()
