def DFS_Euler(graph: list[list[int]], vertex: int, stack = list()) -> list[int]:
    for id, value in enumerate(graph[vertex]):
        if value == 1:
            graph[vertex][id] = 0
            graph[id][vertex] = 0
            DFS_Euler(graph, id, stack)
    
    stack.append(vertex + 1)
    return stack

def Is_Valid_Vertex(vertex: int, current: int, path: list[int], graph: list[list[int]]):
    if graph[path[current - 1]][vertex] == 0:
        return False
    
    if vertex in path:
        return False
    
    return True

def Hamiltonian(graph: list[list[int]], path: list[int] = [], current: int = -1, height: int = -1) -> list[int] | None:
    if height == -1:
        height = len(graph)
        path = [-1] * height
        path[0] = 0
        current = 1
        
    if current == height:
        return path
    
    for vertex in range(height):
        if Is_Valid_Vertex(vertex, current, path, graph):
            path[current] = vertex
            if Hamiltonian(graph, path, current + 1, height):
                return path
            
            path[current] = -1
    
    return None

# def Hamiltonian(graph: list[list[int]], vertex: int, start: int = -1, count: int = 0, path: list[int] = []):
#     if start == -1:
#         start = vertex
#         path = [vertex]
    
#     visited = [False for _ in graph]
#     visited[vertex] = True
    
#     for id, value in enumerate(graph[vertex]):
#         if id == start and count == len(graph) - 1:
#             return True
        
#         if not visited[value]:
#             if Hamiltonian(graph, id, start, count, path):
#                 path.append(id)
#                 return True
    
#     visited[vertex] = False
#     count -= 1
#     return False

if __name__ == '__main__':
    from generate import generate_30, generate_50, generate_70
    from show import print_graph
    import sys
    sys.setrecursionlimit(999999999)
    # graph = generate_30(int(input("Size: ")))
    
    # HAMILTON TEST
    # graph = [
    # #    1  2  3  4  5  6
    #     [0, 1, 1, 0, 0, 1], # 1
    #     [1, 0, 1, 0, 1, 0], # 2
    #     [1, 1, 0, 1, 1, 0], # 3
    #     [0, 0, 1, 0, 1, 1], # 4
    #     [0, 1, 1, 1, 0, 0], # 5
    #     [1, 0, 0, 1, 0, 0], # 6
    # ]
    
    # EULER TEST
    # graph = [
    # #    1  2  3  4  5  6  7  8  9  10
    #     [0, 1, 0, 0, 0, 0, 0, 0, 0, 1], # 1
    #     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0], # 2
    #     [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], # 3
    #     [0, 0, 1, 0, 1, 1, 0, 1, 0, 0], # 4
    #     [0, 0, 1, 1, 0, 1, 1, 0, 0, 0], # 5
    #     [0, 0, 0, 1, 1, 0, 1, 1, 0, 0], # 6
    #     [0, 0, 0, 0, 1, 1, 0, 1, 0, 1], # 7
    #     [0, 0, 0, 1, 0, 1, 1, 0, 1, 0], # 8
    #     [0, 0, 0, 0, 0, 0, 0, 1, 0, 1], # 9
    #     [1, 0, 1, 0, 0, 0, 1, 0, 1, 0], # 10
    # ]
    print_graph(graph)
    # print(DFS_Euler(graph, 0))
    print(Hamiltonian(graph))