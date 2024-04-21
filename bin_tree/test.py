from array_create import create_array
from avl_tree import create_avl_tree
from bst_tree import create_bst_tree
from show import in_order, pre_order
from search import search_max, search_min, search_key
from delete import delete_node, delete_tree

def test():
    n = int(input("Podaj długość tablicy: \n"))

    array = create_array(n)
    array = sorted(array) # budowa avl tree zostaw, budowa bst tree zakomentuj dla testów :)
    print("Array: ", array, "\n")

    root, height = create_avl_tree(array)

    # root = create_bst_tree(array)

    print("Printing tree in order...\n")
    in_order(root)
    # pre_order(root)

    print("\n\n Max value in tree is: ", search_max(root))
    print("\n\n Min value in tree is: ", search_min(root))
    print("\n\n Height of a tree is: ", height)
    print(f"\n\n Path to {array[n - 1]} in tree is: ", search_key(root, array[n - 1]))
    d = input("Do you want to delete this tree? (y/n):")[0]

    match d:
        case "y":
            root = delete_tree(root)
            print("\n\nTree deleted!\n")
        case "n":
            print("\n\nTree not deleted!\n")


if __name__ == "__main__":
    test()
