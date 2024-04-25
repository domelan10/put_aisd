def topological_sort(array: list[list[int]], option: int) -> list[int]:
    l = list()

    match option:
        case 1:
            '''Adjacency Matrix'''

            for sub_array in array:
                if 1 not in sub_array:
                    found = array.index(sub_array)
                    # print(found)
                    l.append(found)
                    for i in array:
                        i[found] = 0
            
            for sub_array in array:
                for element in sub_array:
                    print(element, end=' ')
                print('\n')

            return l



        case 2:
            '''Succesor List'''

        case 3:
            '''Edge Table'''



if __name__ == "__main__":
    pass
