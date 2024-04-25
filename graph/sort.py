def topological_sort(array: list[list[int]], option: int) -> list[int]:
    l = list()

    match option:
        case 1:
            '''Adjacency Matrix'''
            
            for sub_array in array:
                if 1 not in sub_array:
                    found = array.index(sub_array)
                    l.append(found)
                    for i in array:
                        i[found] = 0

            return l



        case 2:
            '''Succesor List'''

        case 3:
            '''Edge Table'''



if __name__ == "__main__":
    pass
