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
    new_index = len(s)
    mutable = list(s)
    for i in reversed(range(length)):
        if mutable[i] == ' ':
            mutable[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            mutable[new_index - 1] = mutable[i]
            new_index -= 1
    return ''.join(mutable)


def urlify_simple(s, length):
    return s[:length].replace(' ', '%20')

class TestUrlify(unittest.TestCase):
    def setUp(self):
        self.args = {
            ('much ado about nothing      ', 22): 'much%20ado%20about%20nothing',
            ('Mr John Smith    ', 13): 'Mr%20John%20Smith',
        }

    def test_urlify(self):
        for arg, expected in self.args.items():
            self.assertEqual(urlify(*arg), expected)

class TestUrlifySimple(unittest.TestCase):
    def setUp(self):
        self.args = {
            #('John Foody Weiner   ', 17): 'John%20Foody%20Weiner',
            ('I  like   TKG  ', 13): 'I%20%20like%20%20%20TKG',
            ('  What  is  100 cm? ', 19): '%20%20What%20%20is%20%20100%20cm?',
            ('value="I   like turtles"', 23): 'value="I%20%20%20like%20turtles',
            ('    ', 3): '%20%20%20',
        }

    def test_urlify(self):
        for arg, expected in self.args.items():
            self.assertEqual(urlify_simple(*arg), expected)