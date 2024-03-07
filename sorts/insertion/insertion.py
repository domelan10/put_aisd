import random


def insertion_sort(unsorted_list: list) -> list:
    sorted_list = []
    sorted_list.append(unsorted_list[0])
    unsorted_list.pop(0)

    for e in unsorted_list:

        i = len(sorted_list) - 1

        while i >= 0 and sorted_list[i] >= e:
            i -= 1
        sorted_list.insert(i+1, e)
        print(sorted_list)

    return sorted_list


def main():
    np = sorted([random.randint(0, 100)*2 + 1 for _ in range(0, 10)])
    p = sorted([random.randint(0, 100)*2 for _ in range(0, 10)], reverse=True)
    unsorted_list = np + p
    print(insertion_sort(unsorted_list))


if __name__ == '__main__':
    main()
