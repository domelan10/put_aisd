import random


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

def main():
    np = sorted([random.randint(0, 100)*2 + 1 for _ in range(0, 10)])
    p = sorted([random.randint(0, 100)*2 for _ in range(0, 10)], reverse=True)
    unsorted_list = np + p
    print(insertion_sort(unsorted_list))


if __name__ == '__main__':
    main()
