import random


def ss(toSort: list) -> list:
    for startId in range(len(toSort)):
        minId = startId
        
        for id in range(startId + 1, len(toSort)):
            if toSort[id] < toSort[minId]:
                minId = id

        toSort[startId], toSort[minId] = toSort[minId], toSort[startId]

    return toSort


def main() -> None:
    tests = 2
    #SelectionSort
    print("===============================================")
    print("===============  SelectionSort  ===============")
    print("===============================================\n")
    for i in range(0, tests + 1):
        print(f"\n{i})")
        data = [random.randint(0, 256) for _ in range(0, 10)]
        print(f"raw:    {data}")
        print(f"sorted: {ss(data)}")


if __name__ == "__main__":
    main()