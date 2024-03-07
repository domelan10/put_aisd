import random


def test_decrease(size: int) -> list[int]:
    return sorted([random.randint(0, 100)*2 + 1 for _ in range(0, 10)], reverse=True)