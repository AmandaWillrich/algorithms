import unittest
from algorithms.selection_sort import selection_sort


class TestSelectionSort(unittest.TestCase):

    def setUp(self):
        self.expected_number_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.expected_string_array = ['Amanda', 'Bianca', 'Cristiane',
                                      'Dennis', 'Felipe', 'Kennedy', 'Rafael',
                                      'Zayn']
        self.unordered_number_array = [4, 7, 3, 9, 1, 2, 5, 6, 8, 10]
        self.unordered_string_array = ['Zayn', 'Rafael', 'Bianca', 'Amanda',
                                       'Felipe', 'Kennedy', 'Dennis',
                                       'Cristiane']

    def test_selection_sort_on_unordered_number_array(self):
        result = selection_sort(self.unordered_number_array)
        self.assertEqual(result, self.expected_number_array)

    def test_selection_sort_on_unordered_string_array(self):
        result = selection_sort(self.unordered_string_array)
        self.assertEqual(result, self.expected_string_array)
