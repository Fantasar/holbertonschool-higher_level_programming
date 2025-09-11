#!/usr/bin/python3
"""Unittests for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Suite de tests pour la fonction max_integer"""

    def test_ordered_list(self):
        """Max d'une liste ordonnée"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max d'une liste non ordonnée"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Max au début de la liste"""
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        """Liste avec des nombres négatifs"""
        self.assertEqual(max_integer([-5, -9, -1, -7]), -1)

    def test_mixed_numbers(self):
        """Liste avec négatifs et positifs"""
        self.assertEqual(max_integer([-5, -1, 0, 3, 2]), 3)

    def test_one_element(self):
        """Liste avec un seul élément"""
        self.assertEqual(max_integer([42]), 42)

    def test_empty_list(self):
        """Liste vide"""
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        """Liste avec floats"""
        self.assertEqual(max_integer([1.5, 2.3, 0.7]), 2.3)

    def test_strings(self):
        """Max avec string => compare les caractères ASCII"""
        self.assertEqual(max_integer("abc"), "c")

    def test_string_list(self):
        """Max d'une liste de chaînes"""
        self.assertEqual(max_integer(["apple", "banana", "pear"]), "pear")


if __name__ == '__main__':
    unittest.main()
