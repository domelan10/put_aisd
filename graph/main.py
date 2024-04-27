from create import create_adjacency_matrix
from show import DFS, BFS

def main() -> None:
    n = int(input())
    array = create_adjacency_matrix(n)
    for sub_array in array:
        print(sub_array)
    print("\n")
    DFS(array)
    print("\n")
    BFS(array, 0, 1, n)


if __name__ == '__main__':
    main()
