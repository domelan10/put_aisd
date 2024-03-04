import random


def insertion_sort(unsortedList: list) -> list:
    sortedList = []
    sortedList.append(unsortedList[0])
    unsortedList.pop(0)

    for e in unsortedList:

        i = len(sortedList) - 1

        while i >= 0 and sortedList[i] >= e:
            i -= 1
        sortedList.insert(i+1, e)
        print(sortedList)

    return sortedList


def main() -> None:
    np = sorted([random.randint(0, 100)*2 + 1 for _ in range(0, 10)])
    p = sorted([random.randint(0, 100)*2 for _ in range(0, 10)], reverse=True)
    unsortedList = np + p
    print(insertion_sort(unsortedList))


if __name__ == '__main__':
    main()
