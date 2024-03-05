import unittest
from algorithms.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.number_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.string_array = ['Amanda', 'Bianca', 'Cristiane', 'Dennis',
                             'Felipe', 'Kennedy', 'Rafael', 'Zayn']

    def test_finding_amanda_in_string_array(self):
        result = binary_search(self.string_array, 'Amanda')
        self.assertEqual(result, self.string_array.index('Amanda'))

    def test_finding_cristiane_in_string_array(self):
        result = binary_search(self.string_array, 'Cristiane')
        self.assertEqual(result, self.string_array.index('Cristiane'))

    def test_finding_rafael_in_string_array(self):
        result = binary_search(self.string_array, 'Rafael')
        self.assertEqual(result, self.string_array.index('Rafael'))

    def test_finding_felipe_in_string_array(self):
        result = binary_search(self.string_array, 'Felipe')
        self.assertEqual(result, self.string_array.index('Felipe'))

    def test_finding_kennedy_in_string_array(self):
        result = binary_search(self.string_array, 'Kennedy')
        self.assertEqual(result, self.string_array.index('Kennedy'))

    def test_finding_non_existent_in_string_array(self):
        result = binary_search(self.string_array, 'José')
        self.assertEqual(result, None)

    def test_finding_seven_in_number_array(self):
        result = binary_search(self.number_array, 7)
        self.assertEqual(result, self.number_array.index(7))

    def test_finding_three_in_number_array(self):
        result = binary_search(self.number_array, 3)
        self.assertEqual(result, self.number_array.index(3))

    def test_finding_non_existent_number_in_number_array(self):
        result = binary_search(self.number_array, 42)
        self.assertEqual(result, None)
