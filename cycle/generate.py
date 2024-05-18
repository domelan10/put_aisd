import random

def generate_30(n: int) -> list[list[int]]:
    graph = [[0 for _ in range(n)] for _ in range(n)]
    desired = n*(n-1)/2*0.3
    count = 0

    for i in range(n - 1):
        graph[i][i + 1] = 1
        graph[i + 1][i] = 1
        count += 1

    while count < desired:
        while True:
            one, two, three = random.randint(0, n - 1), random.randint(0, n - 1), random.randint(0, n - 1)
            
            if one == two or two == three or three == one:
                break
            
            if graph[one][two] == 1 or graph[one][three] == 1:
                break
            
            if graph[two][one] == 1 or graph[two][three] == 1:
                break
            
            if graph[three][one] == 1 or graph[three][two] == 1:
                break
            
            graph[one][two] = 1
            graph[one][three] = 1
            graph[two][one] = 1
            graph[two][three] = 1
            graph[three][one] = 1
            graph[three][two] = 1
            count += 3
    
    # cleared = random.randint(0, n - 1)
    # for i in range(n):
    #     graph[i][cleared] = 0
    #     graph[cleared][i] = 0
    
    return graph

def generate_50(n: int) -> list[list[int]]:
    graph = [[0 for _ in range(n)] for _ in range(n)]
    desired = n*(n-1)/2*0.5
    count = 0

    for i in range(n - 1):
        graph[i][i + 1] = 1
        graph[i + 1][i] = 1
        count += 1

    while count < desired:
        while True:
            one, two, three = random.randint(0, n - 1), random.randint(0, n - 1), random.randint(0, n - 1)
            
            if one == two or two == three or three == one:
                break
            
            if graph[one][two] == 1 or graph[one][three] == 1:
                break
            
            if graph[two][one] == 1 or graph[two][three] == 1:
                break
            
            if graph[three][one] == 1 or graph[three][two] == 1:
                break
            
            graph[one][two] = 1
            graph[one][three] = 1
            graph[two][one] = 1
            graph[two][three] = 1
            graph[three][one] = 1
            graph[three][two] = 1
            count += 3
    
    cleared = random.randint(0, n - 1)
    for i in range(n):
        graph[i][cleared] = 0
        graph[cleared][i] = 0
    
    return graph

def generate_70(n: int) -> list[list[int]]:
    graph = [[0 for _ in range(n)] for _ in range(n)]
    desired = n*(n-1)/2*0.7
    count = 0

    for i in range(n - 1):
        graph[i][i + 1] = 1
        graph[i + 1][i] = 1
        count += 1

    while count < desired:
        while True:
            one, two, three = random.randint(0, n - 1), random.randint(0, n - 1), random.randint(0, n - 1)
            
            if one == two or two == three or three == one:
                break
            
            if graph[one][two] == 1 or graph[one][three] == 1:
                break
            
            if graph[two][one] == 1 or graph[two][three] == 1:
                break
            
            if graph[three][one] == 1 or graph[three][two] == 1:
                break
            
            graph[one][two] = 1
            graph[one][three] = 1
            graph[two][one] = 1
            graph[two][three] = 1
            graph[three][one] = 1
            graph[three][two] = 1
            count += 3
    
    # cleared = random.randint(0, n - 1)
    # for i in range(n):
    #     graph[i][cleared] = 0
    #     graph[cleared][i] = 0
    
    return graph

if __name__ == '__main__':
    graph = generate_non_hamilton(int(input("Size: ")))
    
    for id, sub_array in enumerate(graph):
        print(id, sub_array, sep=". ")