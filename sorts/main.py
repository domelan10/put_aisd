from insertion.insertion import insertion_sort 
from selection.selection import selection_sort
# from merge.merge import merge_sort
# from quick.quick import quick_sort

from py_tests.test_random import test_random
from py_tests.test_increase import test_increase
from py_tests.test_decrease import test_decrease
from py_tests.test_hill import test_hill


def main():
    print("Sort types: insertion, selection, merge, quick")
    print("Test types: random, increase, decrease, hill\n")
    sort = input("Select sort to test: ")
    test = input("Select test type: ")
    test_size = input("Select number of elements to test: ")
    
    match(test):
        case "random":
            test_random(sort)
        case "increase":
            test_increase(sort)
        case "decrease":
            test_decrease(sort)
        case "hill":
            test_hill(sort)


if __name__ == '__main__':
    main()