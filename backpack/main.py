from backpack import knapsack_bruteforce, knapsack_dynamic
from time import time

def main() -> None:
    file = open('input.txt', 'r')
    c = int(file.readline())
    n = int(file.readline())
    items = [[]]
    for line in file.readlines():
        value, weight = line.split(' ')
        items.append([int(value), int(weight)])
    
    print(f'C: {c}\nN: {n}\nItems: \tvalue\tweight', end='')
    for item in items[1:]:
        print(f'\n\t  {item[0]}\t   {item[1]}', end='')
    print('\n')
    
    dynamic_time = time()
    knapsack_dynamic(n, c, items)
    dynamic_time = time() - dynamic_time
    
    bruteforce_time = time()
    knapsack_bruteforce(n, c, items)
    bruteforce_time = time() - bruteforce_time
    
    print(f'\n\nDynamic time: {dynamic_time} seconds')
    print(f'Bruteforce time: {bruteforce_time} seconds')
    return

if __name__ == '__main__':
    main()