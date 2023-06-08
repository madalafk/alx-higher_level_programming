#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Suite test for max_integer function
    """

    def test_max_integer(self):
        """
        Test max_integer function with a list of integers
        """
        self.assertEqual(max_integer([5, -2, 100, 3]), 100)

    def test_empty_list(self):
        """
        Test max_integer function with an empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_repeated_number(self):
        """
        Test max_integer function with a list containing repeated numbers
        """
        self.assertEqual(max_integer([1000, 1000, 1000]), 1000)

    def test_float_numbers(self):
        """
        Test max_integer function with a list of floating-point numbers
        """
        self.assertEqual(max_integer([50, 51, 50, 49]), 51)

    def test_max_operated_integer(self):
        """
        Test max_integer function with a list of numbers including a multiplication operation
        """
        self.assertEqual(max_integer([-3, -5 * -5, 12, -1]), 25)

    def test_neg_numbers(self):
        """
        Test max_integer function with a list of negative numbers
        """
        self.assertEqual(max_integer([-10, -5, -2, -1]), -1)

    def test_max_at_beginning(self):
        """
        Test max_integer function with the maximum number at the beginning of the list
        """
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_zero_number(self):
        """
        Test max_integer function with a list containing zero
        """
        self.assertEqual(max_integer([0, 0]), 0)

    def test_big_list(self):
        """
        Test max_integer function with a large list of numbers
        """
        self.assertEqual(max_integer([
            901, 902, 903, 904, 905, 906, 907, 908, 909, 910,
            911, 912, 913, 914, 915, 916, 917, 918, 919, 920,
            919, 918, 917, 1000, 915, 914, 913, 912, 911, 910,
            909, 908, 907, 906, 905, 904, 903, 902, 901]), 1000)

    def test_list_with_loop(self):
        """
        Test max_integer function with a list containing a loop
        """
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer([i * 5 for i in my_list]), 25)

    def test_one_number_in_a_list(self):
        """
        Test max_integer function with a list containing only one number
        """
        self.assertEqual(max_integer([1]), 1)

    def test_string_number_in_a_list(self):
        """
        Test max_integer function with a list containing a string
        """
        with self.assertRaises(TypeError):
            max_integer([0, '1'])

    def test_tuple_in_a_list(self):
        """
        Test max_integer function with a list containing a tuple
        """
        with self.assertRaises(TypeError):
            max_integer([10, (20, 30)])

    def test_dictionary(self):
        """
        Test max_integer function with a dictionary
        """
        with self.assertRaises(KeyError):
            max_integer({'key1': 1, 'key2': 2})

    def test_number(self):
        """
        Test max_integer function with a single number
        """
        with self.assertRaises(TypeError):
            max_integer(1)
