import random
import py_tests.test_size as test_size


def test_increase(size: int) -> list[int]:
    return sorted([random.randint(0, test_size.max_test_number) for _ in range(0, size)])