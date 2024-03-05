import unittest
from algorithms.decimal_to_binary_converter import (
    convert_to_binary,
    _find_starting_multiplier
)


class TestDecimalToBinaryConverter(unittest.TestCase):

    def test_convert_42_to_binary(self):
        result = convert_to_binary(42)
        self.assertEqual(result, '101010')

    def test_convert_127_to_binary(self):
        result = convert_to_binary(127)
        self.assertEqual(result, '1111111')

    def test_convert_32423_to_binary(self):
        result = convert_to_binary(32423)
        self.assertEqual(result, '111111010100111')

    def test_convert_23123_to_binary(self):
        result = convert_to_binary(23123)
        self.assertEqual(result, '101101001010011')

    def test_convert_512_to_binary(self):
        result = convert_to_binary(512)
        self.assertEqual(result, '1000000000')

    def test_convert_25_to_binary(self):
        result = convert_to_binary(25)
        self.assertEqual(result, '11001')

    def test_convert_4_to_binary(self):
        result = convert_to_binary(4)
        self.assertEqual(result, '100')

    def test_find_starting_multiplier_for_42(self):
        multiplier = _find_starting_multiplier(42)
        self.assertEqual(multiplier, 32)

    def test_find_starting_multiplier_for_93(self):
        multiplier = _find_starting_multiplier(93)
        self.assertEqual(multiplier, 64)

    def test_find_starting_multiplier_for_2(self):
        multiplier = _find_starting_multiplier(2)
        self.assertEqual(multiplier, 2)
