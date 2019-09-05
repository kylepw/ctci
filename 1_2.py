"""
    1_2.py
    ~~~~~~

    Given two strings, write a method to decide if one is a permutation of the other.
    Hint #1, #84, #122, #131
"""
import unittest

def sort_str(s):
    return ''.join(sorted(s))

def is_permutation(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        return False
    if len(str1) < 1 or len(str2) < 1:
        return False
    if len(str1) > len(str2):
        return False

    str1 = sort_str(str1)
    str2 = sort_str(str2)
    print(str1, str2)

    window_pos = 0
    found = False
    for c1 in str1:
        print('Window position: ', window_pos)
        print(c1)
        for i, c2 in enumerate(str2[window_pos:]):
            print(i, c2)
            if c1 == c2:
                found = True
                window_pos += i + 1
                break
        if not found:
            return False
        else:
            found = False
    return True

def is_permutation_pythonic(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        return False
    if len(str1) < 1 or len(str2) < 1:
        return False
    if len(str1) > len(str2):
        return False

    str1 = sort_str(str1)
    str2 = sort_str(str2)

    window_pos = 0
    for c1 in str1:
        for i, _ in enumerate(str2[window_pos:]):
            if c1 in str2[window_pos:]:
                window_pos += i
                break
            else:
                return False
    return True



class TestPermutation(unittest.TestCase):
    def setUp(self):
        self.str1 = 'cba'
        self.str2 = 'blahcgah'

        self.str3 = 'aaa'
        self.str4 = 'zeopa'

    def test_permutation(self):
        self.assertTrue(is_permutation(self.str1, self.str2))
        self.assertFalse(is_permutation(self.str3, self.str4))

    @unittest.SkipTest
    def test_permutation_pythonic(self):
        self.assertTrue(is_permutation_pythonic(self.str1, self.str2))
        #self.assertFalse(is_permutation_pythonic(self.str3, self.str4))




