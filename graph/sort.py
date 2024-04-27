def topological_sort(array: list[list[int]], n: int, option: int = 1,  )-> list[int]:
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


if __name__ == "__main__":
    pass
