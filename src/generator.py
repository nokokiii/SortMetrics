from typing import List

from numpy import random


def generate_data(n: int, min_value: int = 0, max_value: int = 10000) -> List[int]:
    """
    Generates list of n numbers to sort

    :param n: amount of items that'll be generated
    :param min_value: minimum value that'll be generated (default = 0)
    :param max_value: maximum value that'll be generated (default = 10000)
    """
    return random.randint(min_value, max_value, size=n).tolist()
