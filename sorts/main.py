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


def main():
    print("Sort types: insertion, selection, merge, quick, heap, bubble, shell, counting")
    print("Test types: random, increase, decrease, hill, stable\n")
    sort = input("Select sort to test: ")
    test = input("Select test type: ")
    test_size = int(input("Select number of elements to test: "))
    
    match(test):
        case "random" | 1:
            data = test_random(test_size)
        case "increase" | 2:
            data = test_increase(test_size)
        case "decrease" | 3:
            data = test_decrease(test_size)
        case "hill" | 4:
            data = test_hill(test_size)
        case "stable" | 5:
            data = test_stable(test_size)
        case default:
            print("Unknown test type.")
            main()
            return 0
    
    print("Unsorted array: ", data)
    
    match(sort):
        case "insertion" | 1:
            data = insertion_sort(data)
        case "selection" | 2:
            data = selection_sort(data)
        case "merge" | 3:
            data = merge_sort(data)
        case "quick" | 4:
            data = quick_sort(data)
        case "heap" | 5:
            data = heap_sort(data)
        case "bubble" | 6:
            data = bubble_sort(data)
        case "shell" | 7:
            data = shell_sort(data)
        case "counting" | 8:
            data = counting_sort(data)
        case default:
            print("Unknown sort type.")
            main()
            return 0
    
    print("Sorted array: ", data)


if __name__ == '__main__':
    main()