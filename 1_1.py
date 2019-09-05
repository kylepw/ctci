"""
    1_1.py
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

    window_pos = 0
    while (window_pos < len(s)):
        for i, c in enumerate(s):
            print(i, c)
            if i == window_pos:
                continue
            if c == s[window_pos]:
                return False
        window_pos += 1
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