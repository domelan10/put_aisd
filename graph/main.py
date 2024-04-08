from create import create_random
from show import DFS, BFS

def main():
    array = create_random(int(input()))
    for sub_array in array:
        print(sub_array)
    print("\n")
    DFS(array)
    BFS(array, 0)


if __name__ == '__main__':
    main()