import random
import py_tests.test_size as test_size


def test_random(size: int) -> list[int]:
    return [random.randint(0, test_size.max_test_number) for _ in range(0, size)]