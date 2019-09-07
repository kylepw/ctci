"""
    q14.py
    ~~~~~~

    Palindrome Permutation: Given a string, write a function to check if it is
    a permutation of a palindrome. A palindrome is a word or phrase that is
    the same forwards and backwards. A permutation is a rearrangement of
    letters. The palindrome does not need to be limited to just dictionary
    words.

    EXAMPLE
    Input: Tact Coa
    Output: True (permutations: "taco cat", "atco cta", etc.)
    Hints: #106, #121, #134, #136
"""
import unittest
from collections import Counter


def perm_of_pal(s):
    s = s.replace(' ', '').lower()
    counter = Counter()
    for c in s:
        counter[c] += 1
    if list(counter.values()).count(1) > 1:
        return False
    if all([(count % 2 == 0) or (count == 1) for count in counter.values()]):
        return True
    return False

def char_num(c):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    val = ord(c)

    if a <= val <= z:
        return val - a
    elif A <= val <= Z:
        return val - A
    else:
        return -1

def perm_of_pal_solution(phrase):
    """Given solution"""
    table = [0 for _ in range(ord('z') - ord('a') + 1)]

    odd_counter = 0
    for c in phrase:
        n = char_num(c)
        if n != -1:
            table[n] += 1
            if table[n] % 2:
                odd_counter += 1
            else:
                odd_counter -= 1
    return odd_counter <= 1


class TestPermOfPal(unittest.TestCase):
    def setUp(self):
        self.data = [
            #('Tact Coa', True),
            ('jhsabckuj ahjsbckj', True),
            ('Able was I ere I saw Elba', True),
            ('So patient a nurse to nurse a patient so', False),
            ('Random Words', False),
            ('Not a Palindrome', False),
            ('no x in nixon', True),
            ('azAZ', True)
        ]

    def test_perm_of_pal(self):
        for arg, result in self.data:
            self.assertEqual(perm_of_pal(arg), result)

    def test_perm_of_pal_solution(self):
        for arg, result in self.data:
            self.assertEqual(perm_of_pal_solution(arg), result)