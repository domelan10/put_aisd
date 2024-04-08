import random

def create_random(n: int) -> list[list[int]]:
    array = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(1, n):
        array[i - 1][i] = 1
    
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            if random.random() < 0.5:
                array[i - 1][j] = 1
    
    array[n - 2][n - 1] = 1
    return array

def main():
    array = create_random(int(input()))
    
    for sub_array in array:
        for element in sub_array:
            print(element, end=' ')
        print('\n')

if __name__ == '__main__':
    main()