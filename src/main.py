from time import time

from tabulate import tabulate

from algorithms import *
from generator import generate_data


ALGOS = {
    "Bubble sort": bubble_sort,
    "Insertion sort": insertion_sort,
    "Quick sort": quick_sort,
    "Merge sort": merge_sort,
    "Intro sort": intro_sort,
    "Tim sort": tim_sort,
    "Python": sorted
}

def calculate_time(data: List[int]) -> List[float]:
    """
    It's sorting data and calculating time for each algorithm

    :param data: list of integers to sort

    :return: list of time for each algorithm
    """
    time_data = []

    for _, algo in ALGOS.items():
        start = time()
        algo(data)
        end = time()
        time_data.append(round(end - start, 3))

    return time_data


def main() -> None:
    headers = ["Data size", *ALGOS.keys()]

    time_data = [
        ["100", *calculate_time(generate_data(100))],
        ["1k", *calculate_time(generate_data(1_000))],
        ["10k", *calculate_time(generate_data(10_000))],
        ["100k", *calculate_time(generate_data(100_000))]
    ]

    print(tabulate(time_data, headers=headers, tablefmt="pretty"))


if __name__ == "__main__":
    main()
