import random


def test_hill(size: int) -> list[int]:
    increase = sorted([random.randint(0, 100)*2 + 1 for _ in range(0, 10)])
    decrease = sorted([random.randint(0, 100)*2 for _ in range(0, 10)], reverse=True)
    return increase + decrease