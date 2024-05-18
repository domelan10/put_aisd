def selection_sort(to_sort: list) -> list:
    for start_id in range(len(to_sort)):
        min_id = start_id
        
        for id in range(start_id + 1, len(to_sort)):
            if to_sort[id] < to_sort[min_id]:
                min_id = id

        to_sort[start_id], to_sort[min_id] = to_sort[min_id], to_sort[start_id]

    return to_sort
