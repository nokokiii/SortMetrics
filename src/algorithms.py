from math import ceil, log2
from random import randrange
from typing import List, Optional


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Bubble sort algorithm

    :param arr: List of integers

    :return: Sorted list of integers
    """
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def insertion_sort(arr: List[int], start: Optional[int] = None, end: Optional[int] = None) -> List[int]:
    """
    Insertion sort algorithm

    :param arr: List of integers
    :param start: Starting index
    :param end: Ending index
    """
    start = start or 0
    end = end or len(arr)

    for i in range(start, end):
        j = arr[i]
        while i != start and j < arr[i - 1]:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = j

    return arr


def quick_sort(arr: List[int]) -> List[int]:
    """
    Quick sort algorithm

    :param arr: List of integers

    :return: Sorted list of integers
    """
    if len(arr) < 2:
        return arr

    pivot_index = randrange(len(arr))
    pivot = arr.pop(pivot_index)

    lesser = [item for item in arr if item <= pivot]
    greater = [item for item in arr if item > pivot]

    return [*quick_sort(lesser), pivot, *quick_sort(greater)]


def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge sort algorithm

    :param arr: List of integers

    :return: Sorted list of integers
    """
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

def heap_sort(arr: List[int]) -> List[int]:
    """
    Heap sort algorithm

    :param arr: List of integers

    :return: Sorted list of integers
    """
    def heapify(arr: List[int], heap_size: int, i: int):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < heap_size and arr[i] < arr[left]:
            largest = left

        if right < heap_size and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, heap_size, largest)

    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


def intro_sort(arr: List[int]) -> List[int]:
    """
    Intro sort algorithm

    :param arr: List of integers

    :return: Sorted list of integers
    """
    def median_of_three(arr: list, first: int, middle: int, last: int) -> int:
        if (arr[first] > arr[middle]) != (arr[first] > arr[last]):
            return arr[first]
        elif (arr[middle] > arr[first]) != (arr[middle] > arr[last]):
            return arr[middle]
        else:
            return arr[last]

    def partition(array: list, low: int, high: int, pivot: int) -> int:
        i = low
        j = high
        while True:
            while array[i] < pivot:
                i += 1
            j -= 1
            while pivot < array[j]:
                j -= 1
            if i >= j:
                return i
            array[i], array[j] = array[j], array[i]
            i += 1

    def intro_sort_helper(arr: List[int], start: int, end: int, size_threshold: int, max_depth: int) -> List[int]:
        while end - start > size_threshold:
            if max_depth == 0:
                return heap_sort(arr[start:end])
            max_depth -= 1
            pivot = median_of_three(arr, start, start + ((end - start) // 2) + 1, end - 1)
            p = partition(arr, start, end, pivot)
            arr = intro_sort_helper(arr, p, end, size_threshold, max_depth)
            end = p
        return insertion_sort(arr, start, end)

    if len(arr) <= 1:
        return arr

    max_depth = 2 * ceil(log2(len(arr)))
    return intro_sort_helper(arr, 0, len(arr), 16, max_depth)


def tim_sort(arr: List[int]) -> List[int]:
    """
    Tim sort algorithm

    :param arr: Unsorted list

    :return: Sorted list of integers
    """
    def binary_search(arr, item, start, end):
        if start == end:
            return start if arr[start] > item else start + 1
        if start > end:
            return start

        mid = (start + end) // 2
        if arr[mid] < item:
            return binary_search(arr, item, mid + 1, end)
        elif arr[mid] > item:
            return binary_search(arr, item, start, mid - 1)
        else:
            return mid

    def merge(left, right):
        if not left:
            return right
        if not right:
            return left

        if left[0] < right[0]:
            return [left[0], *merge(left[1:], right)]

        return [right[0], *merge(left, right[1:])]

    length = len(arr)
    runs, sorted_runs = [], []
    new_run = [arr[0]]
    sorted_array = []
    i = 1
    while i < length:
        if arr[i] < arr[i - 1]:
            runs.append(new_run)
            new_run = [arr[i]]
        else:
            new_run.append(arr[i])
        i += 1
    runs.append(new_run)

    for run in runs:
        sorted_runs.append(insertion_sort(run))
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)

    return sorted_array
