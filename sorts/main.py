from insertion.insertion import insertion_sort 
from selection.selection import selection_sort
from merge.merge import merge_sort
from quick.quick import quick_sort
from heap.heap import heap_sort
from bubble.bubble import bubble_sort

from py_tests.test_random import test_random
from py_tests.test_increase import test_increase
from py_tests.test_decrease import test_decrease
from py_tests.test_hill import test_hill
from py_tests.test_stable import test_stable


def main():
    print("Sort types: insertion, selection, merge, quick, heap, bubble")
    print("Test types: random, increase, decrease, hill, stable\n")
    sort = input("Select sort to test: ")
    test = input("Select test type: ")
    test_size = int(input("Select number of elements to test: "))
    
    match(test):
        case "random":
            data = test_random(test_size)
        case "increase":
            data = test_increase(test_size)
        case "decrease":
            data = test_decrease(test_size)
        case "hill":
            data = test_hill(test_size)
        case "stable":
            data = test_stable(test_size)
    
    print("Unsorted array: ", data)
    
    match(sort):
        case "insertion":
            data = insertion_sort(data)
        case "selection":
            data = selection_sort(data)
        case "merge":
            data = merge_sort(data)
        case "quick":
            data = quick_sort(data)
        case "heap":
            data = heap_sort(data)
        case "bubble":
            data = bubble_sort(data)
    
    print("Sorted array: ", data)


if __name__ == '__main__':
    main()