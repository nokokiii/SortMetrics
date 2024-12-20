from time import time

from tabulate import tabulate

from algorithms import *
from generator import generate_data


ALGOS = {
    "Bubble sort": bubble_sort,
    "Insertion sort": insertion_sort,
    "Quick sort": quick_sort,
    "Merge sort": merge_sort,
    "Tim sort": tim_sort,
    "Intro sort": intro_sort,
    "Sort in python": sorted
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
    data_1k = generate_data(1000)
    data_10k = generate_data(10_000)
    data_100k = generate_data(100_000)

    sorting_algos = {
        "Bubble sort": bubble_sort,
        "Insertion sort": insertion_sort,
        "Quick sort": quick_sort,
        "Merge sort": merge_sort,
        "Tim sort": tim_sort,
        "Intro sort": intro_sort,
        "Sort in python": sorted
    }

    headers = ["Data size", *sorting_algos.keys()]

    time_data = [
        ["1k", *calculate_time(data_1k)],
        ["10k", *calculate_time(data_10k)],
        ["100k", *calculate_time(data_100k)]
    ]

    print(tabulate(time_data, headers=headers, tablefmt="pretty"))


if __name__ == "__main__":
    main()
