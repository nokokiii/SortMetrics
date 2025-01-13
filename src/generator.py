from typing import List

from numpy import random


def generate_data(n: int) -> List[int]:
    """
    Generates list of n numbers to sort

    :param n: amount of items that'll be generated
    """
    return [random.randint(0, n) for _ in range(n)]
