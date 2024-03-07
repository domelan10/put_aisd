import random


def test_random(size: int) -> list[int]:
    return [random.randint(0, 100)*2 + 1 for _ in range(0, 10)]