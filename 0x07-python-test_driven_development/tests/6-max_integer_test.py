#!/usr/bin/python3
"""Unit test."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test the function max_integer(list=[])."""

    def test_empty_list(self):
        """Test empty list."""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_different_cases(self):
        """Test negative numbers, and other edge cases."""
        self.assertEqual(max_integer([9, 8, 7, 6, 5, 0, 1]), 9)
        self.assertEqual(max_integer([-9, 8, -7, 6, 5, 0, -1]), 8)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([6]), 6)
        self.assertEqual(max_integer([-1, -5, -9]), -1)
        self.assertEqual(max_integer([9, -9]), 9)
        self.assertEqual(max_integer([6, 6]), 6)

    def test_throw_error(self):
        """Test for TypeError conditions."""
        # self.assertRaises(TypeError, max_integer, "hi")
        self.assertRaises(TypeError, max_integer, 45)
        self.assertRaises(TypeError, max_integer, True)
        # self.assertRaises(TypeError, max_integer, {})
        # self.assertRaises(TypeError, max_integer, [1,2,True,3,4,0])
        self.assertRaises(TypeError, max_integer, [65, 8, 6, "4", 4, 325, 0])
        self.assertRaises(TypeError, max_integer, [1, [5, 56, 3, 6, 3], 6])
