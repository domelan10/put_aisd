import random


def create_array(n) -> list:
    # array = [n for n in range(1, n+1)]
    array = {random.randint(1, 100) for n in range(1,n+1)}
    array = list(array)
    return sorted(array)

if __name__ == '__main__':
    print(sorted(create_array(100)))