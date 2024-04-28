from create import create_adjacency_matrix, create_edge_table, create_successor_list, create_edge_table_from_adj_matrix, create_successor_list_from_adj_matrix
from show import BFS, DFS
from sort import topological_sort_kahn, topological_sort_tarjan

def main() -> None:
    n = int(input("Give size of the matrix: "))
    adj_matrix = create_adjacency_matrix(n)
    edge_tab = create_edge_table_from_adj_matrix(adj_matrix)
    successor_list = create_successor_list_from_adj_matrix(adj_matrix)
    
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

    option1 = int(input("Select sort option:\n1 - Adjancency Matrix\n2 - Successor List\n3 - Edge Table\n"))

    match option1:
        case 1:
            l = topological_sort_kahn(adj_matrix,n,option1)

        case 2:
            l = topological_sort_kahn(successor_list,n,option1)

        case 3:
            l = topological_sort_kahn(edge_tab,n,option1)

    print(l)



if __name__ == '__main__':
    main()
