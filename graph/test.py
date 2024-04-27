from create import create_adjacency_matrix, create_edge_table, create_successor_list, test_range, test_slope
from show import BFS, DFS
from sort import topological_sort_kahn, topological_sort_tarjan
from time import time
import sys
import matplotlib.pyplot as plt


def test() -> None:
    representations = ["adj_matrix", "edge_table", "successor_list"]
    # tests = ["find_max", "in_order", "balance_bst"]
    scale = [test_slope * i for i in range(1, test_range + 1)]
    
    option = 2 # change type of tests

    _, axes = plt.subplots()
    axes.set_xlabel("Test size")
    axes.set_ylabel("Time of execution")

    match option:
        case 1:
            axes.set_title(f"Traversal functions: BFS")

            for representation in representations:
                print(f"Starting representation: {representation}")
                times = {}
                
                times[representation] = [0]
                for test_size in scale:
                    print(f"\tTest size: {test_size}")
                    
                    match representation:
                        case "adj_matrix":
                            g =create_adjacency_matrix(test_size)
                            start = time()
                            BFS(g,0,1,test_size)
                            end = time()
                        case "edge_table":
                            g = create_edge_table(test_size)
                            start = time()
                            BFS(g,0,3,test_size)
                            end = time()
                        case "successor_list":
                            g = create_adjacency_matrix(test_size)
                            g = create_successor_list(g)
                            start = time()
                            BFS(g,0,2,test_size)
                            end = time()
                    times[representation].append(end - start)

                axes.plot([0]+[element for element in scale], times[representation], label=representation)
                        
        case 2:
            axes.set_title(f"Traversal functions: DFS")
            for representation in representations:
                print(f"Starting representation: {representation}")
                times = {}
                
                times[representation] = [0]
                for test_size in scale:
                    print(f"\tTest size: {test_size}")
                    
                    match representation:
                        case "adj_matrix":
                            g =create_adjacency_matrix(test_size)
                            start = time()
                            DFS(g,1)
                            end = time()
                        case "edge_table":
                            g = create_edge_table(test_size)
                            start = time()
                            DFS(g,3)
                            end = time()
                        case "successor_list":
                            g = create_adjacency_matrix(test_size)
                            g = create_successor_list(g)
                            start = time()
                            DFS(g,2)
                            end = time()
                    times[representation].append(end - start)

                axes.plot([0]+[element for element in scale], times[representation], label=representation)

        case 3:
            axes.set_title(f"Topological sort: Kahn")
            for representation in representations:
                print(f"Starting representation: {representation}")
                times = {}
                
                times[representation] = [0]
                for test_size in scale:
                    print(f"\tTest size: {test_size}")
                    
                    match representation:
                        case "adj_matrix":
                            g =create_adjacency_matrix(test_size)
                            start = time()
                            topological_sort_kahn(g,test_size,1)
                            end = time()
                        case "edge_table":
                            g = create_edge_table(test_size)
                            start = time()
                            topological_sort_kahn(g,test_size,3)
                            end = time()
                        case "successor_list":
                            g = create_adjacency_matrix(test_size)
                            g = create_successor_list(g)
                            start = time()
                            topological_sort_kahn(g,test_size,2)
                            end = time()
                    times[representation].append(end - start)

                axes.plot([0]+[element for element in scale], times[representation], label=representation)

    axes.legend()
    print("\n")
    plt.show()

if __name__ == '__main__':
    test()
    