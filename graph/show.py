def DFS(array: list[list[int]], option: int) -> None:
    visited = set()
    queue = []
    max_length = len(array)
    current = 0
    
    match(option):
        case 1:
            while len(visited) < max_length:
                if current not in visited:
                    visited.add(current)
                    queue.append(current)
                    print(current)
                    
                    tmp_array = list()
                    for id, element in enumerate(array[current]):
                        if element == 1:
                            tmp_array.append(id)
                    
                    for element in sorted(tmp_array, reverse = True):
                        queue.append(element)
                
                if len(queue) > 0:
                    current = queue.pop()
                else:
                    for id in range(max_length):
                        if id not in visited:
                            current = id
            return
        
        case 2:
            while len(visited) < max_length:
                if current not in visited:
                    visited.add(current)
                    queue.append(current)
                    print(current)
                    
                    for element in sorted(array[current], reverse = True):
                        queue.append(element)
                
                if len(queue) > 0:
                    current = queue.pop()
                else:
                    for id in range(max_length):
                        if id not in visited:
                            current = id
            return
        
        case 3:
            max_length = 0
            for element in array:
                if element[1] > max_length:
                    max_length = element[1]
            max_length += 1
            
            while len(visited) < max_length:
                if current not in visited:
                    visited.add(current)
                    queue.append(current)
                    print(current)
                    tmp_array = list()
                    
                    for element in array:
                        if element[0] == current:
                            tmp_array.append(element[1])
                    
                    for element in sorted(tmp_array, reverse = True):
                        queue.append(element)
                
                if len(queue) > 0:
                    current = queue.pop()
                else:
                    for id in range(max_length):
                        if id not in visited:
                            current = id
            return

def BFS(array: list[list[int]], current: int, option) -> None:
    visited = set()
    printed = set()
    queue = []
    max_length = len(array)
    printed.add(current)
    print(current)
    
    match(option):
        case 1:
            while len(visited) < max_length:
                if current not in visited:
                    visited.add(current)
                    queue.append(current)
                    tmp_array = list()
                    
                    for id, element in enumerate(array[current]):
                        if element == 1:
                            tmp_array.append(id)
                            if id not in printed:
                                printed.add(id)
                                print(id)
                    
                    for element in sorted(tmp_array, reverse = True):
                        queue.append(element)
                
                if len(queue) > 0:
                    current = queue.pop()
                else:
                    for id in range(max_length):
                        if id not in visited:
                            current = id
                            if current not in printed:
                                printed.add(current)
                                print(current)
            return
        
        case 2:
            while len(visited) < max_length:
                if current not in visited:
                    visited.add(current)
                    queue.append(current)
                    
                    for element in array[current]:
                        if element not in printed:
                            printed.add(element)
                            print(element)
                    
                    for element in sorted(array[current], reverse = True):
                        queue.append(element)
                
                if len(queue) > 0:
                    current = queue.pop()
                else:
                    for id in range(max_length):
                        if id not in visited:
                            current = id
                            if current not in printed:
                                printed.add(current)
                                print(current)
            return
        
        case 3:
            max_length = 0
            for element in array:
                if element[1] > max_length:
                    max_length = element[1]
            max_length += 1
            
            while len(visited) < max_length:
                if current not in visited:
                    visited.add(current)
                    queue.append(current)
                    tmp_array = list()
                    
                    for element in array:
                        if element[0] == current:
                            tmp_array.append(element[1])
                            if element[1] not in printed:
                                printed.add(element[1])
                                print(element[1])
                    
                    for element in sorted(tmp_array, reverse = True):
                        queue.append(element)
                
                if len(queue) > 0:
                    current = queue.pop()
                else:
                    for id in range(max_length):
                        if id not in visited:
                            current = id
                            if current not in printed:
                                printed.add(current)
                                print(current)
            return


def main():
    from create import create_adjacency_matrix, create_edge_table, create_successor_list
    adj = create_adjacency_matrix(10)
    # adj = [
    #     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    #     [0, 0, 1, 1, 0, 0, 1, 1, 1, 1],
    #     [0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
    #     [0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
    #     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # ]
    # correct answer for DFS: 0 1 2 4 6 9 5 7 8 3
    # correct answer for BFS: 0 1 2 4 3 6 7 8 9 5
    edge, succ = create_edge_table(adj), create_successor_list(adj)
    
    print("Adjacency Matrix")
    for line in adj:
        print(line)
    
    print("\n")
    print("Successor List")
    for i, sub_array in enumerate(succ):
        print("v"+str(i),sub_array, end='\n')

    print("\n")
    print("Edge Table")
    print("out in")
    for i, sub_array in enumerate(edge):
        print("e"+str(i),sub_array, end='\n')
    
    print("\n")
    print("Adjacency Matrix")
    DFS(adj, 1)
    print("\n")
    BFS(adj, 0, 1)
    
    print("\n")
    print("Successor List")
    DFS(succ, 2)
    print("\n")
    BFS(succ, 0, 2)
    
    print("\n")
    print("Edge Table")
    DFS(edge, 3)
    print("\n")
    BFS(edge, 0, 3)

if __name__ == "__main__":
    main()