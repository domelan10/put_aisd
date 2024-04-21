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
            array = create_array(int(input("\n\nGive length of an array: \n")))
            print("\nGenerated array: \n", array)
            root, height = create_bst_tree(array)
        case 2:
            array = create_array(int(input("\n\nGive length of an array: \n")))
            print("\nGenerated array: \n", array)
            root, height = create_avl_tree(array)
        case 3:
            exit()
        case _:
            print("Wrong choice!")
            main()
    while True:
        print("\n\n\nTree created, what do you want to do with it?\n")
        choice = int(input("1) Print tree in-order and max height\n2) Print tree pre-order and max height\n3) Delete nodes\n4) Delete whole tree\n5) Balance tree with rotation\n6) Print max element\n7) Print min elemenent\n8) Generate new tree\n9) Exit program\n\n"))
        print("\n\n\n")
        
        match choice:
            case 1:
                in_order(root)
                print("\nHeight of tree: ", height, "\n\n")
            case 2:
                pre_order(root)
                print("\nHeight of tree: ", height, "\n\n")
            case 3:
                print("How many nodes do you want to delete?\n")
                n = int(input("Enter number of nodes to delete: \n"))
                print("Which nodes do you want to delete?")
                values = list()
                for i in range(n):
                    values.append(int(input()))
                for val in values:
                    root = delete_node(root, val)
            case 4:
                delete_tree(root)
            case 5:
                pass
            case 6:
                search_max(root)
            case 7:
                search_min(root)
            case 8:
                break
            case 9:
                exit()
            case _:
                print("Wrong choice!")
    
    main()

if __name__ == "__main__":
    main()
