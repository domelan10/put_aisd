def shell_sort(to_sort: list) -> list:
    n = len(to_sort)

    gap = n // 2

    while gap > 0:
        j = gap

        while j < n:
            i = j - gap
            
            while i >= 0:

                if to_sort[i+gap] > to_sort[i]:
                    break

                else:
                    to_sort[i+gap], to_sort[i] = to_sort[i], to_sort[i+gap]
                
                i -= gap

            j += 1

        gap = gap // 2
        
    return to_sort 