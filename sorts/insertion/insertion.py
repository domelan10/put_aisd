def insertion_sort(to_sort: list) -> list:
    n = len(to_sort)

    if n <= 1:
        return to_sort
    
    for i in range(1, n):
        k = to_sort[i]

        j = i-1

        while j >= 0 and k < to_sort[j]:
            to_sort[j+1] = to_sort[j]

            j -= 1
        to_sort[j+1] = k

    return to_sort
