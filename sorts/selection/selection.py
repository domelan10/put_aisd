import random


def selection_sort(to_sort: list) -> list:
    for start_id in range(len(to_sort)):
        min_id = start_id
        
        for id in range(start_id + 1, len(to_sort)):
            if to_sort[id] < to_sort[min_id]:
                min_id = id

        to_sort[start_id], to_sort[min_id] = to_sort[min_id], to_sort[start_id]

    return to_sort


def main():
    tests = 2
    for i in range(0, tests + 1):
        print(f"\n{i})")
        data = [random.randint(0, 256) for _ in range(0, 10)]
        print(f"raw:    {data}")
        print(f"sorted: {selection_sort(data)}")


if __name__ == "__main__":
    main()