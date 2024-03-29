import unittest
from algorithms.recursion import (
    sum_numbers,
    sum_numbers_alternative,
    sum_number_of_items,
    sum_number_of_items_alternative,
    find_highest_value,
    find_highest_value_alternative
)


class TestRecursion(unittest.TestCase):

    def setUp(self):
        self.array_1 = [2, 4, 6]
        self.array_2 = [1, 4, 24, 234, 1, 9, 12, 3]
        self.array_3 = [4, 6, 16, 48, 24]

    def test_sum_numbers_should_return_12(self):
        self.assertEqual(
            sum(self.array_1),
            sum_numbers(self.array_1)
        )

    def test_sum_numbers_should_return_288(self):
        self.assertEqual(
            sum(self.array_2),
            sum_numbers(self.array_2)
        )

    def test_sum_numbers_should_return_98(self):
        self.assertEqual(
            sum(self.array_3),
            sum_numbers(self.array_3)
        )

    def test_sum_number_alternatives_should_return_12(self):
        self.assertEqual(
            sum(self.array_1),
            sum_numbers_alternative(self.array_1)
        )

    def test_sum_numbers_alternative_should_return_288(self):
        self.assertEqual(
            sum(self.array_2),
            sum_numbers_alternative(self.array_2)
        )

    def test_sum_numbers_alternative_should_return_98(self):
        self.assertEqual(
            sum(self.array_3),
            sum_numbers_alternative(self.array_3)
        )

    def test_sum_number_of_items_array_1(self):
        self.assertEqual(
            len(self.array_1),
            sum_number_of_items(self.array_1)
        )

    def test_sum_number_of_items_array_2(self):
        self.assertEqual(
            len(self.array_2),
            sum_number_of_items(self.array_2)
        )

    def test_sum_number_of_items_array_3(self):
        self.assertEqual(
            len(self.array_3),
            sum_number_of_items(self.array_3)
        )

    def test_sum_number_of_items_alternative_array_1(self):
        self.assertEqual(
            len(self.array_1),
            sum_number_of_items_alternative(self.array_1)
        )

    def test_sum_number_of_items_alternative_array_2(self):
        self.assertEqual(
            len(self.array_2),
            sum_number_of_items_alternative(self.array_2)
        )

    def test_sum_number_of_items_alternative_array_3(self):
        self.assertEqual(
            len(self.array_3),
            sum_number_of_items_alternative(self.array_3)
        )

    def test_find_highest_value_array_1(self):
        self.assertEqual(
            6,
            find_highest_value(self.array_1)
        )

    def test_find_highest_value_array_2(self):
        self.assertEqual(
            234,
            find_highest_value(self.array_2)
        )

    def test_find_highest_value_array_3(self):
        self.assertEqual(
            48,
            find_highest_value(self.array_3)
        )

    def test_find_highest_value_alternative_array_1(self):
        self.assertEqual(
            6,
            find_highest_value_alternative(self.array_1)
        )

    def test_find_highest_value_alternative_array_2(self):
        self.assertEqual(
            234,
            find_highest_value_alternative(self.array_2)
        )

    def test_find_highest_value_alternative_array_3(self):
        self.assertEqual(
            48,
            find_highest_value_alternative(self.array_3)
        )
