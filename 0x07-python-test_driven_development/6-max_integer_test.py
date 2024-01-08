#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Unittest for the function max_integer
    """
    def test_empty_list(self):
        """test empty list
        """
        list = []
        self.assertEqual(max_integer(list), None)

    def test_list(self):
        """test of int"""
        list = [2, 6, 24]
        self.assertEqual(max_integer(list), 24)

    def test_uniq(self):
        """test of one int"""
        list = [17]
        self.assertEqual(max_integer(list), 17)

    def test_string(self):
        """test of string"""
        list = ["Côme", "Le Sauter"]
        self.assertEqual(max_integer(list), "Le Sauter")
    
    def test_float(self):
        """test int and float"""
        list = [2, 6.66, 24.24]
        self.assertEqual(max_integer(list), 24.24)

    def test_neg(self):
        list = [2, 6.66, -24.24]
        self.assertEqual(max_integer(list), 6.66)
        
if __name__ == '__main__':
    unittest.main()
