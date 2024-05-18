def DFS_Euler(graph: list[list[int]], current: int = 0, stack = list()) -> list[int]:
    for id, value in enumerate(graph[current]):
        if value == 1:
            graph[current][id] = 0
            graph[id][current] = 0
            DFS_Euler(graph, id, stack)
    
    stack.append(current + 1)
    return stack

def is_valid_vertex(graph: list[list[int]], vertex: int, current: int, path: int):
    if graph[path[current-1]][vertex] == 0:
        return False
    if vertex in path:
        return False
    return True

def hamilton_cycle(graph: list[list[int]], path: list[int] = [], current: int = 1) -> list[int] | str:
    if path == []:
        path = [-1] * len(graph)
        path[0] = 0
        # print("init")
    
    if current == len(graph):
        # print("end")
        if graph[path[current-1]][path[0]] == 1:
            return path
        else:
            return "None found"
    
    for vertex in range(1, len(graph)):
        # print("\tvertex:", vertex)
        if is_valid_vertex(graph, vertex, current, path):
            # print("\t\tcorrect: Found")
            path[current] = vertex
            if hamilton_cycle(graph, path, current+1) != "None found":
                return path
            path[current] = -1
            # print("\t\tcorrect: False")
    
    return "None found"


if __name__ == '__main__':
    from generate import generate_30, generate_50, generate_70
    from show import print_graph
    import sys
    sys.setrecursionlimit(999999999)
    
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
    
    graph_size = int(input("Size of the graph: "))
    match int(input("Type of data (1-graph_30, 2-graph_50, 3-graph_70): ")):
        case 1:
            graph = generate_30(graph_size)
            print_graph(graph)
            match int(input("Type of algorithm (1-hamilton, 2-euler): ")):
                case 1:
                    print(hamilton_cycle(graph))
                case 2:
                    print(DFS_Euler(graph))
        case 2:
            graph = generate_50(graph_size)
            print_graph(graph)
            print(hamilton_cycle(graph))
        case 3:
            graph = generate_70(graph_size)
            print_graph(graph)
            match int(input("Type of algorithm (1-hamilton, 2-euler): ")):
                case 1:
                    print(hamilton_cycle(graph))
                case 2:
                    print(DFS_Euler(graph))