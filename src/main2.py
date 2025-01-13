from time import time

import numpy as np
from tabulate import tabulate

from algorithms import *
from generator import generate_data


ALGOS = {
    "Multithreaded Merge Sort": thread_quick_sort,
    "Python": sorted
}


def calculate_time(data: List[int]) -> List[float]:
    """
    It's sorting data and calculating time for each algorithm

    :param data: list of integers to sort

    :return: list of time for each algorithm
    """
    time_data = []

    for algo_name, algo in ALGOS.items():
        start = time()
        algo(data)
        end = time()
        time_data.append(round(end - start, 3))

    return time_data


def main() -> None:
    headers = ["Data size", *ALGOS.keys()]

    time_data = [
        ["100k", *calculate_time(generate_data(100_000))],
        ["1M", *calculate_time(generate_data(1_000_000))],
        ["10M", *calculate_time(generate_data(10_000_000))],
    ]

    print(tabulate(time_data, headers=headers, tablefmt="pretty"))


if __name__ == "__main__":
    main()
