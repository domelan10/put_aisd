def knapsack_bruteforce(n: int, c: int, items: dict[list[int]]) -> dict[list[int]]:
    decision_matrix = [[] for _ in range(1 << n+1)]
    max_value = 0
    
    for i in range(1 << n+1):
        total_weight = 0
        total_value = 0
        for j in range(1, n+1):
            if i & (1 << j):
                total_value += items[j][0]
                total_weight += items[j][1]
                decision_matrix[i].append(j)
        
        if total_weight <= c and total_value > max_value:
            max_value = total_value
            result_items = decision_matrix[i]
    
    return result_items

def knapsack_dynamic(n: int, c: int, items: dict[list[int]]) -> list[int]:
    decision_matrix = [[0 for _ in range(0, c+1)] for _ in range(0, n+1)]
    
    for i in range(1, n+1):
        for j in range(1, c+1):
            if items[i][1] > j:
                decision_matrix[i][j] = decision_matrix[i-1][j]
            else:
                decision_matrix[i][j] = max(decision_matrix[i-1][j], decision_matrix[i-1][j-items[i][1]] + items[i][0])
    
    for sub_array in decision_matrix:
        print(sub_array)
    
    result_items = list()
    while n > 0:
        if decision_matrix[n][c] > decision_matrix[n-1][c]:
            result_items.append(n)
            c -= items[n][1]
        n -= 1
    
    return result_items

def main() -> None:
    # index 0 - value of item, index 1 - weight of item
    items = {
        1: [2, 1],
        2: [1, 1],
        3: [3, 2],
        4: [7, 3],
        5: [6, 3]
    }

    n = len(items)
    c = 7
    print(n)
    match int(input('Type (1 - dynamic, 2 - bruteforce): ')):
        case 1:
            print("Picked items: ", knapsack_dynamic(n, c, items))
        case 2:
            print("Picked items: ", knapsack_bruteforce(n, c, items))


if __name__ == '__main__':
    main()