#!/usr/bin/python3
"""Unittest for max_integer([..]).
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def text_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]), None)

    def test_one_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_max_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 1.2, 7.4]), 7.4)

    def test_max_negative_integer(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_negative_and_positive(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
    
    def test_string_list(self):
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')
    
    def test_one_string(self):
        self.assertEqual(max_integer(['school']), 'school')
    
    def test_one_float(self):
        self.assertEqual(max_integer([10.5]), 10.5)


        

if __name__ == "__main__":
    unittest.main()
