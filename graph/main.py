from create import create_adjacency_matrix
from show import DFS, BFS

def main() -> None:
    array = create_adjacency_matrix(int(input()))
    for sub_array in array:
        print(sub_array)
    print("\n")
    DFS(array)
    BFS(array, 0)


if __name__ == '__main__':
    main()
