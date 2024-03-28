import random


def create_array(n) -> list:
    # array = [n for n in range(1, n+1)]
    array = [random.randint(0, 100) for n in range(1,n+1)]
    return array

if __name__ == '__main__':
    print(create_array(10))