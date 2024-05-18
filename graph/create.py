import random


test_slope = 100
test_range = 10


def create_adjacency_matrix(n: int) -> list[list[int]]:
    array = [[0 for _ in range(n)] for _ in range(n)]
    max_count = int(0.25*n*(n-1))
    
    # for i in range(1, n):
    #     array[i - 1][i] = 1
    #     max_count -= 1
    
    while max_count > 0:
        i, j = random.randint(0, n - 1), random.randint(0, n - 1)
        if i < j and array[i][j] != 1:
            array[i][j] = 1
            max_count -= 1
    
    return array


def create_successor_list_from_adj_matrix(array: list[list[int]]) -> list[list[int]]:
    table = list()
    
    for i in range(len(array)):
        table.append(list())
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i][j] == 1:
                table[i].append(j)

    return table


def create_successor_list(n) -> list[list[int]]:
    num_edges = n * (n - 1) // 4
    successors = [[] for _ in range(n)]
    edge_count = 0

    while edge_count < num_edges:
        source = random.randint(0, n - 2)
        target = random.randint(source + 1, n - 1)

        if target not in successors[source]:
            successors[source].append(target)
            edge_count += 1

    return successors



def create_edge_table_from_adj_matrix(array: list[list[int]]) -> list[list[int]]:
    table = list()
    
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i][j] == 1:
                if [i, j] not in table or table[j, i] not in table:
                    table.append([i, j])

    return table


def create_edge_table(n: int) -> list[list[int]]:
    num_edges = n * (n - 1) // 4

    edges = []
    for i in range(num_edges):
        while True:
            edge = [random.randint(0, n-1), random.randint(0, n-1)]
            if edge[0] < edge[1] and edge not in edges:
                edges.append(edge)
                break
            elif edge[0] > edge[1] and edge[::-1] not in edges:
                edges.append(edge[::-1])
                break

    return edges


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

if __name__ == '__main__':
    main()
