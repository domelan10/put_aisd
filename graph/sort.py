def topological_sort(array: list[list[int]], option: int) -> list[int]:
    l = list()
    n = len(array)
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

            

        case 3:
            '''Edge Table'''



if __name__ == "__main__":
    pass
