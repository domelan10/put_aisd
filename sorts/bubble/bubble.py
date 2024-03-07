def bubble_sort(to_sort: list) -> list:
    n = len(to_sort)

    swap = False
    
    for i in range(n-1):
        for j in range(0,n-i-1):
            if to_sort[j] > to_sort[j+1]:
                swap = True
                to_sort[j], to_sort[j+1] = to_sort[j+1], to_sort[j]

        if not swap:
            return to_sort
        