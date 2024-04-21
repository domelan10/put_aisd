from array_create import create_array
from avl_tree import create_avl_tree
from bst_tree import create_bst_tree
from show import in_order, pre_order
from search import search_max, search_min, search_key
from delete import delete_node, delete_tree


def main() -> None:
    tree_choice = int(input(("Generate tree:\n1) BST\n2) AVL\n3) Exit program\n\n")))

    match tree_choice:
        case 1:
            root = create_bst_tree(int(input("Podaj długość tablicy: \n")))
        case 2:
            root = create_avl_tree(int(input("Podaj długość tablicy: \n")))
        case 3:
            exit()
        case _:
            print("Wrong choice!")
            main()

    print("Tree created, what do you want to do with it?\n\n")
    choice = int(input("1) Print tree in-order\n2) Print tree pre-order\n3) Delete nodes\n4) Delete whole tree\n5) Balance tree with rotation\n6) Exit program\n\n"))

    match choice:
        case 1:
            in_order(root)
        case 2:
            pre_order(root)
        case 3:
            delete_node(root)
        case 4:
            delete_tree(root)
        case 5:
            pass
        case 6:
            exit()
        case _:
            print("Wrong choice!")
            main()
    
    main()

if __name__ == "__main__":
    main()
