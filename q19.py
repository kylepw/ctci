"""
    q19.py
    ~~~~~~

    String Rotation: Assume you have a method isSubstring which checks if one
    word is a substring of another. Given two strings, s1 and s2, write code
    to check if s2 is a rotation of s1 using only one call to isSubstring
    (e.g., "waterbottle" is a rotation of "erbottlewat").

    Hints: #34, #88, #104
"""
import unittest


def string_rotation(s1, s2):
    """Return True if s2 is a rotation of s1"""
    return len(s1) == len(s2) and is_substring(s2, s1*2)

def is_substring(ss, s):
    return ss in s
class Test(unittest.TestCase):
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()