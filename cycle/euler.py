def DFS_Euler(graph: list[list[int]], v: int, stack = list()) -> list[int]:
    for u in graph[v]:
        if u == 1:
            graph[v][u] = 0
            graph[u][v] = 0
            DFS_Euler(graph, u, stack)
    stack.append(v)

    return stack

if __name__ == '__main__':
    from generate import generate_30
    import sys
    sys.setrecursionlimit(999999999)
    graph = generate_30(int(input("Size: ")))
    
    print(DFS_Euler(graph, 0))