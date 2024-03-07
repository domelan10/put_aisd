import random


def insertion_sort(sList: list) -> list:
    n = len(sList)

    if n <= 1:
        return sList
    
    for i in range(1, n):
        k = sList[i]

        j = i-1

        while j >= 0 and k < sList[j]:
            sList[j+1] = sList[j]

            j -= 1
        sList[j+1] = k

    return sList

def main():
    np = sorted([random.randint(0, 100)*2 + 1 for _ in range(0, 10)])
    p = sorted([random.randint(0, 100)*2 for _ in range(0, 10)], reverse=True)
    unsorted_list = np + p
    print(insertion_sort(unsorted_list))


if __name__ == '__main__':
    main()
