import unittest

from src.algorithms import *

class TestAlgos(unittest.TestCase):
    def setUp(self):
        self.unsorted_arr = [500, 120, 2, 10, 4, 90, 290, 3, 890, 20, 32]
        self.sorted_arr = [2, 3, 4, 10, 20, 32, 90, 120, 290, 500, 890]

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort(self.unsorted_arr.copy()), self.sorted_arr)

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(self.unsorted_arr.copy()), self.sorted_arr)

    def test_quick_sort(self):
        self.assertEqual(quick_sort(self.unsorted_arr.copy()), self.sorted_arr)

    def test_merge_sort(self):
        self.assertEqual(merge_sort(self.unsorted_arr.copy()), self.sorted_arr)

    def test_heap_sort(self):
        self.assertEqual(heap_sort(self.unsorted_arr.copy()), self.sorted_arr)

    def test_intro_sort(self):
        self.assertEqual(intro_sort(self.unsorted_arr.copy()), self.sorted_arr)

    def test_time_sort(self):
        self.assertEqual(tim_sort(self.unsorted_arr.copy()), self.sorted_arr)
