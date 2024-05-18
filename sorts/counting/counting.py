def counting_sort(data: list[int]) -> list[int]:
    max_data = max(data)
    counts = [0] * (max_data + 1)
    result = [0] * len(data)
    
    for num in data:
        counts[num] += 1
    
    for id in range(1, max_data + 1):
        counts[id] += counts[id - 1]
    
    for id in range(len(data) - 1, -1, -1):
        result[counts[data[id]] - 1] = data[id]
        counts[data[id]] -= 1
    
    return result