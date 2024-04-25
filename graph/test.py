from create import create_adjacency_matrix, create_edge_table, create_successor_list
from show import BFS, DFS
from sort import topological_sort

def main() -> None:
    matrix = create_adjacency_matrix(int(input()))
    table = create_edge_table(matrix)
    successor_list = create_successor_list(matrix)
    
    print("Adjacency Matrix")
    for sub_array in matrix:
        for element in sub_array:
            print(element, end=' ')
        print('\n')
    print("\n")

    print("Successor List")
    for i, sub_array in enumerate(successor_list):
        print("v"+str(i),sub_array, end=' ')
        print('\n')

    print("\n")
    print("Edge Table")
    print("out in")
    for i, sub_array in enumerate(table):
        print("e"+str(i),sub_array, end=' ')
        print('\n')

    l = topological_sort(matrix,option=1)
    print(l)


if __name__ == '__main__':
    main()
    