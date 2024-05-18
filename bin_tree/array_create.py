import random

test_slope = 1000
test_range = 50

def create_array(n) -> list:
    # array = [n for n in range(1, n+1)]
    array = {random.randint(0, n*4) for n in range(1,n+1)}
    while len(array) < n:
        array.add(random.randint(0, n*4))
    array = list(array)
    return sorted(array)

if __name__ == '__main__':
    print(sorted(create_array(100)))