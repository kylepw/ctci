"""
    q11.py
    ~~~~~~

    Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures?
"""
import unittest


def is_unique(s):
    if not isinstance(s, str):
        return False
    if len(s) <= 1:
        return True

    exists = {}
    for c in s:
        if exists.get(c):
            return False
        else:
            exists[c] = True
    return True


class TestIsUnique(unittest.TestCase):
    def setUp(self):
        self.entries = [
            (123, False),
            ('a', True),
            ('abcd', True),
            ('zzzz', False),
            ('aryz', True),
            ('AaBb', True),
            ('lryl', False),
            ('3bk3l', False),
            ('3er4b', True)
        ]
    def test_values(self):
        for value, result in self.entries:
            self.assertEqual(is_unique(value), result)