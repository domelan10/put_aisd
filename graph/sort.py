def topological_sort_kahn(array: list[list[int]], n: int, option: int = 1)-> list[int]:
    l = list()
    visited = set()

    match option:
        case 1:
            '''Adjacency Matrix'''

            f = True
            while f:
                f = False
                for i in range(n):
                    for sub_array in array:
                        if sub_array[i] == 1 or i in visited:
                            break

                        f = True
                        visited.add(i)
                        l.append(i)
                        for j in range(n):
                            for sub_array in array:
                                sub_array[j] = 0

            return l

        case 2:
            '''Succesor List'''

            f = True
            while f:
                f = False
                for i in range(n):
                    for sub_array in array:
                        if i in sub_array or i in visited:
                            break
                        f = True

                        visited.add(i)
                        l.append(i)
                        array[i] = []
            
            return l

        case 3:
            '''Edge Table'''

            f = True
            while f:
                f = False
                for i in range(n):
                    for sub_array in array:
                        if sub_array[1] == i or i in visited:
                            break
                        f = True

                        visited.add(i)
                        l.append(i)
                        for j in array:
                            if j[0] == i:
                                j[1] = 0

            return l


def topological_sort_tarjan(array: list[list[int]], n: int, option: int)-> list[int]:
    l = list()
    queue = [0]
    current = 0
    colors = [0 for _ in range(n)] #0 - white, 1 - gray, 2 - black
    colors[0] = 1
    
    match option:
        case 1:
            '''Adjacency Matrix'''
            while queue:
                count = 0
                
                for id, val in enumerate(array[current][::-1]):
                    if colors[n - id - 1] == 0 and queue[-1] != n - id - 1 and val == 1:
                        queue.append(n - id - 1)
                        count += 1
                
                current = queue[-1]
                colors[current] = 1
                
                if current not in l and count == 0:
                    l.insert(0, current)
                    colors[current] = 2
                    queue = [value for value in queue if value != current]
                    if queue:
                        current = queue[-1]
            return l
        
        case 2:
            '''Succesor List'''
            while queue:
                count = 0
                
                for neigh in array[current][::-1]:
                    if colors[neigh] == 0 and queue[-1] != neigh:
                        queue.append(neigh)
                        count += 1
                
                current = queue[-1]
                colors[current] = 1
                
                if current not in l and count == 0:
                    l.insert(0, current)
                    colors[current] = 2
                    queue = [value for value in queue if value != current]
                    if queue:
                        current = queue[-1]
            return l
        
        case 3:
            '''Edge Table'''
            while queue:
                count = 0
                
                for _, [out, to] in enumerate(array):
                    if colors[to] == 0 and queue[-1] != to and out == current:
                        queue.append(to)
                        count += 1
                
                current = queue[-1]
                colors[current] = 1
                
                if current not in l and count == 0:
                    l.insert(0, current)
                    colors[current] = 2
                    queue = [value for value in queue if value != current]
                    if queue:
                        current = queue[-1]
            return l

if __name__ == "__main__":
    from create import create_adjacency_matrix, create_successor_list, create_edge_table
    # adj = create_adjacency_matrix(10)
    adj = [
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    # correct for tarjan: 0 1 3 2 5 7 8 4 6 9
    edge, succ = create_edge_table(adj), create_successor_list(adj)
    
    print("Adjacency Matrix")
    for line in adj:
        print(line)
    
    print("\n")
    print("Successor List")
    for i, sub_array in enumerate(succ):
        print("v"+str(i),sub_array)

    print("\n")
    print("Edge Table")
    print("out in")
    for i, sub_array in enumerate(edge):
        print("e"+str(i),sub_array)
    
    print("\n")
    print("Adjacency Matrix")
    result = topological_sort_tarjan(adj, len(adj), 1)
    print(result)

    print("\n")
    print("Successor List")
    print(topological_sort_tarjan(succ, len(adj), 2))


    print("\n")
    print("Edge Table")
    print(topological_sort_tarjan(edge, len(adj), 3))

