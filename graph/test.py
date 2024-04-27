from create import create_adjacency_matrix, create_edge_table, create_successor_list
from show import BFS, DFS
from sort import topological_sort

def main() -> None:
    n = int(input("Give size of the matrix: "))
    adj_matrix = create_adjacency_matrix(n)
    edge_tab = create_edge_table(adj_matrix)
    successor_list = create_successor_list(adj_matrix)
    
    print("Adjacency Matrix")
    for sub_array in adj_matrix:
        for element in sub_array:
            print(element)
    
    print("\n")
    print("Successor List")
    for i, sub_array in enumerate(successor_list):
        print("v"+str(i),sub_array)

    print("\n")
    print("Edge Table")
    print("out in")
    for i, sub_array in enumerate(edge_tab):
        print("e"+str(i),sub_array)

    option = int(input("Select sort option:\n1 - Adjancency Matrix\n2 - Successor List\n3 - Edge Table\n"))

    match option:
        case 1:
            l = topological_sort(adj_matrix,n,option)

        case 2:
            l = topological_sort(successor_list,n,option)

        case 3:
            l = topological_sort(edge_tab,n,option)

    print(l)


if __name__ == '__main__':
    main()
    