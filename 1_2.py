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
    """Runtime: O(n^2)?"""
    if not isinstance(str1, str) or not isinstance(str2, str):
        return False
    if len(str1) < 1 or len(str2) < 1:
        return False
    if len(str1) > len(str2):
        return False

    str1 = sort_str(str1)
    str2 = sort_str(str2)

    window_pos = 0
    found = False
    for c1 in str1:
        for i, c2 in enumerate(str2[window_pos:]):
            if c1 == c2:
                found = True
                window_pos += i + 1
                break
        if not found:
            return False
        else:
            found = False
    return True

def is_permutation_dict(str1, str2):
    """Runtime: O(N)"""
    if not isinstance(str1, str) or not isinstance(str2, str):
        return False
    if len(str1) < 1 or len(str2) < 1:
        return False
    if len(str1) > len(str2):
        return False

    count1 = {}
    count2 = {}
    for c in str1:
        if c in count1:
            count1[c] += 1
        else:
            count1[c] = 1
    for c in str2:
        if c in count2:
            count2[c] += 1
        else:
            count2[c] = 1
    for c in str1:
        if c not in count2 or count1[c] > count2[c]:
            return False
    return True


class TestPermutation(unittest.TestCase):
    def setUp(self):
        self.true_vals = [
            ('cba', 'blahcgah'),
            ('aaa', 'zaeopa4a'),
            ('4329', '5489203'),
            ('!!$$5jlp', '!5lk!jp4l$.$')
        ]
        self.false_vals = [
            ('hey', 'he'),
            (123, 'yo'),
            ('', ''),
            ('kul', 'kkkkkk'),
            ('uer', 'erqqqd'),
            ('oooops', 'psooohey')
        ]

    def test_permutation(self):
        for (str1, str2) in self.true_vals:
            self.assertTrue(is_permutation(str1, str2))
        for (str1, str2) in self.false_vals:
            self.assertFalse(is_permutation(str1, str2))

    def test_permutation_dict(self):
        for (str1, str2) in self.true_vals:
            self.assertTrue(is_permutation_dict(str1, str2))
        for (str1, str2) in self.false_vals:
            self.assertFalse(is_permutation_dict(str1, str2))