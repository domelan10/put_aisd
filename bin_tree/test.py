from array_create import create_array, test_range, test_slope
from avl_tree import create_avl_tree
from bst_tree import create_bst_tree
from show import in_order, pre_order
from search import search_max, search_min, search_key
from delete import delete_node, delete_tree
from time import time
from balance import balance
import sys
import main as gen
import matplotlib.pyplot as plt

sys.setrecursionlimit(1000000000)

def test():
    trees = ["BST", "AVL"]
    # tests = ["find_max", "in_order", "balance_bst"]
    scale = [test_slope * i for i in range(1, test_range + 1)]
    # options = range(1, 5)
    options = [4] # change type of tests


    for option in options:
        match option:
            case 1:
                _, axes = plt.subplots()
                axes.set_xlabel("Test size")
                axes.set_ylabel("Time of execution")
                axes.set_title(f"Creating trees")

                for tree in trees:
                    print(f"Starting tree: {tree}")
                    times = {}
                    
                    times[tree] = [0]
                    for test_size in scale:
                        print(f"\tTest size: {test_size}")
                        match tree:
                            case "BST":
                                start = time()
                                create_bst_tree(create_array(test_size))
                                end = time()
                                times[tree].append(end - start)
                            case "AVL":
                                start = time()
                                create_avl_tree(create_array(test_size))
                                end = time()
                                times[tree].append(end - start)

                    axes.plot([0]+[element for element in scale], times[tree], label=tree)
                axes.legend()
            case 2:
                _, axes = plt.subplots()
                axes.set_xlabel("Test size")
                axes.set_ylabel("Time of execution")
                axes.set_title(f"Finding maximum element")

                for tree in trees:
                    print(f"Starting tree: {tree}")
                    times = {}
                    
                    times[tree] = [0]
                    for test_size in scale:
                        print(f"\tTest size: {test_size}")
                        match tree:
                            case "BST":
                                root, h = create_bst_tree(create_array(test_size))
                                start = time()
                                search_max(root)
                                end = time()
                                times[tree].append(end - start)
                            case "AVL":
                                root, h = create_avl_tree(create_array(test_size))
                                start = time()
                                search_max(root)
                                end = time()
                                times[tree].append(end - start)

                    axes.plot([0]+[element for element in scale], times[tree], label=tree)
                axes.legend()
            
            case 3:
                _, axes = plt.subplots()
                axes.set_xlabel("Test size")
                axes.set_ylabel("Time of execution")
                axes.set_title(f"Printing in-order")

                for tree in trees:
                    print(f"Starting tree: {tree}")
                    times = {}
                    
                    times[tree] = [0]
                    for test_size in scale:
                        print(f"\tTest size: {test_size}")
                        match tree:
                            case "BST":
                                root, h = create_bst_tree(create_array(test_size))
                                start = time()
                                in_order(root)
                                end = time()
                                times[tree].append(end - start)
                            case "AVL":
                                root, h = create_avl_tree(create_array(test_size))
                                start = time()
                                in_order(root)
                                end = time()
                                times[tree].append(end - start)

                    axes.plot([0]+[element for element in scale], times[tree], label=tree)
                axes.legend()

            case 4:
                _, axes = plt.subplots()
                axes.set_xlabel("Test size")
                axes.set_ylabel("Time of execution")
                axes.set_title(f"Balancing BST tree")

                tree = "BST"
                print(f"Starting tree: {tree}")
                times = {}
                    
                times[tree] = [0]
                for test_size in scale:
                    print(f"\tTest size: {test_size}")
                    match tree:
                        case "BST":
                            root, h = create_bst_tree(create_array(test_size))
                            start = time()
                            balance(root)
                            end = time()
                            times[tree].append(end - start)

                axes.plot([0]+[element for element in scale], times[tree], label=tree)
                axes.legend()

    print("\n")
    plt.show()

if __name__ == "__main__":
    test()
