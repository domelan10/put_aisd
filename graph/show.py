def DFS(array: list[list[int]]) -> None:
    visited = set()
    visited.add(0)
    print(0)
    
    for sub_array in array:
        for id, element in enumerate(sub_array):
            if element == 1 and id not in visited:
                visited.add(id)
                print(id)


def BFS(graph: list[list[int]], s: int) -> None:
    h = len(graph)
    visited = set()
    in_degree = {}
    queue = [s]
    visited.add(s)

    for i in range(h):
        in_degree[i] = 0
    
    for sub_array in graph:
        for i in range(h):
            if sub_array[i] == 1:
                in_degree[i] += 1

    for i in range(h):
        if in_degree[i] == 0 and i not in visited:
            queue.append(i)
            visited.add(i)
    
    while queue:
        v = queue.pop(0)
        print(v, "\n")

        for neigh in range(h):
            if graph[v][neigh] == 1 and neigh not in visited:
                queue.insert(0, neigh)
                visited.add(neigh)
