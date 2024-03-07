import random
import py_tests.test_size as test_size


def test_hill(size: int) -> list[int]:
    if size%2 == 0:
        size1, size2 = size//2, size//2
    else:
        size1, size2 = size//2, size//2 + 1
    
    increase = sorted([random.randint(0, test_size.max_test_number)*2 + 1 for _ in range(0, size1)])
    decrease = sorted([random.randint(0, test_size.max_test_number)*2 for _ in range(0, size2)], reverse=True)
    return increase + decrease