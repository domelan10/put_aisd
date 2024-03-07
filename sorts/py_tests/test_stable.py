import random


def test_stable(size: int) -> list[int]:
    return [random.randint(0, 100)*2 + 1] * size