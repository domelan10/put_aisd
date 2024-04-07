from array_create import create_array
from avl_tree import create_avl_tree
from bst_tree import create_bst_tree
from show import in_order, pre_order
from search import search_max, search_min, search_key

def test():
    n = int(input("Podaj długość tablicy: \n"))

    array = create_array(n)
    print("Array: ", array, "\n")

    # root = create_avl_tree(array)

    root = create_bst_tree(array)

    print("Printing tree in order...\n")
    pre_order(root)

    print("\n\n Max value in tree is: ", search_max(root))
    print("\n\n Min value in tree is: ", search_min(root))
    print(f"\n\n Path to {array[n - 1]} in tree is: ", search_key(root, array[n - 1]))



if __name__ == "__main__":
    test()
