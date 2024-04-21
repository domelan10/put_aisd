from array_create import create_array
from avl_tree import create_avl_tree
from bst_tree import create_bst_tree
from show import in_order, pre_order
from search import search_max, search_min, search_key
from delete import delete_node, delete_tree
from balance import balance


def main() -> None:
    tree_choice = int(input(("Generate tree:\n1) BST\n2) AVL\n3) Exit program\n\n")))

    match tree_choice:
        case 1:
            array = create_array(int(input("\n\nGive length of an array: \n")))
            print("\nGenerated array: \n", array)
            root, height = create_bst_tree(array)
            print("\n\n\nTree created, with height ",height,", what do you want to do with it?\n")
        case 2:
            array = create_array(int(input("\n\nGive length of an array: \n")))
            print("\nGenerated array: \n", array)
            root, height = create_avl_tree(array)
            print("\n\n\nTree created, with height ",height,", what do you want to do with it?\n")
        case 3:
            exit()
        case _:
            print("Wrong choice!")
            main()

    while True:
        choice = int(input("\n\n1) Print tree in-order\n2) Print tree pre-order\n3) Delete nodes\n4) Delete whole tree\n5) Balance tree with rotation\n6) Print max element\n7) Print min elemenent\n8) Generate new tree\n9) Exit program\n\n"))
        print("\n\n\n")
        
        match choice:
            case 1:
                in_order(root)
            case 2:
                pre_order(root)
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
                balance(root)
            case 6:
                print("\nMax element: ",search_max(root),"\n")
            case 7:
                print("\nMin element: ",search_min(root),"\n")
            case 8:
                break
            case 9:
                exit()
            case _:
                print("Wrong choice!")
    
    main()

if __name__ == "__main__":
    main()
