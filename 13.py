"""
    q13.py
    ~~~~~~
    Write a method to replace all spaces in a string with '%20'. You may
    assume that the string has sufficient space at the end to hold the
    additional characters, and that you are given the "true" length of the
    string.

    EXAMPLE
    Input: "Mr John Smith    ", 13
    Output: "Mr%20John%20Smith"
    Hints: #53, #118
"""
import unittest


def urlify(s, length):
    SPACE = '%20'

    chars = string.split()

    replaced = ['%20' if c == ' ' else c for c in chars]
    print(replaced)




class TestUrlify(unittest.TestCase):
    def setUp(self):
        params = [
            {('John Foody Weiner   ', 17): 'John%20Foody%20Weiner'},
            {('I  like   TKG  ', 13): 'I%20%20like%20%20%20TKG'},
            {('  What  is  100 cm? ', 19): '%20%20What%20%20is%20%20100%20cm?'},
            {('value="I   like turtles"', 23): 'value="I%20%20%20like%20turtles'},
            {('    ', 3): '%20%20%20'},
        ]

    def test_urlify(self):
        for p, expected in params.items():
            self.assertEqual(urlify(*p), expected)