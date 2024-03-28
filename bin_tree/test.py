from array_create import create_array
from avl_tree import create_avl_tree
from bst_tree import create_bst_tree
from show import in_order
from search import search_max

def test():
    n = int(input("Podaj długość tablicy: \n"))

    array = create_array(n)
    print("Array: ", array, "\n")

    # root = create_avl_tree(array)

    root = create_bst_tree(array)

    print("Printing tree in order...\n")
    in_order(root)

    print("\n\n Max value in tree is: ", search_max(root))



if __name__ == "__main__":
    test()
