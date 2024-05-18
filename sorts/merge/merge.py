def merge_sort(to_sort: list) -> list:
    if len(to_sort) > 1:
        center = len(to_sort) // 2
        
        left = merge_sort(to_sort[:center])
        right = merge_sort(to_sort[center:])
        
        left_id = right_id = main_id = 0
        
        while left_id < len(left) and right_id < len(right):
            if left[left_id] < right[right_id]:
                to_sort[main_id] = left[left_id]
                left_id += 1
            else:
                to_sort[main_id] = right[right_id]
                right_id += 1
            main_id += 1
        
        while left_id < len(left):
            to_sort[main_id] = left[left_id]
            left_id += 1
            main_id += 1
        
        while right_id < len(right):
            to_sort[main_id] = right[right_id]
            right_id += 1
            main_id += 1
    
    return to_sort