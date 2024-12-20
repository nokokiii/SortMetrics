from typing import List


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


def insertion_sort(arr: List[int]) -> List[int]:
    """
    Insertion sort algorithm

    :param arr: List of integers

    :return: Sorted list of integers
    """
    for i in range(1, len(arr)):
        a = arr[i]
        j = i - 1

        while j >= 0 and a < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = a
    return arr


def quick_sort(arr: List[int]) -> List[int]:
    """
    Quick sort algorithm

    :param arr: List of integers

    :return: Sorted list of integers
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge sort algorithm

    :param arr: List of integers

    :return: Sorted list of integers
    """
    if len(arr) <= 1:
        return arr

    def merge(left: List[int], right: List[int]) -> List[int]:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def tim_sort(arr: List[int]) -> List[int]:
    """
    Tim sort algorithm

    :param arr: List of integers

    :return: Sorted list of integers
    """
    def merge(left: List[int], right: List[int]) -> List[int]:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min(i + min_run - 1, n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size
            end = min(start + size * 2 - 1, n - 1)

            merged_array = merge(arr[start:midpoint], arr[midpoint:end + 1])

            arr[start:start + len(merged_array)] = merged_array

        size *= 2

    return arr


def intro_sort(arr: List[int]) -> List[int]:
    """
    Intro sort algorithm: Combines QuickSort, HeapSort, and InsertionSort
    """
    import math
    from heapq import heapify, heappop

    def heapsort(arr):
        heapify(arr)
        return [heappop(arr) for _ in range(len(arr))]

    def intro_sort_helper(arr, depth_limit):
        if len(arr) <= 16:
            return insertion_sort(arr)
        elif depth_limit == 0:
            return heapsort(arr)
        else:
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return intro_sort_helper(left, depth_limit - 1) + middle + intro_sort_helper(right, depth_limit - 1)

    max_depth = int(math.log2(len(arr))) * 2
    return intro_sort_helper(arr, max_depth)
