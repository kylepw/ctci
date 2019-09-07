"""
    q15.py
    ~~~~~~

    One Away: There are three types of edits that can be performed on strings:
    insert a character, remove a character, or replace a character. Given two
    strings, write a function to check if they are one edit (or zero edits)
    away.

    EXAMPLE
    pale, ple   -> true
    pales, pale -> true
    pale, bale  -> true
    pale, bake  -> false

    Hints: #23, #97, #130
"""
import unittest


def one_away(orig, edit):
    return True

class TestOneAway(unittest.TestCase):
    def setUp(self):
        self.data = [
            ('pale', 'ple', True),
            ('pales', 'pale', True),
            ('pale', 'bale', True),
            ('paleabc', 'pleabc', True),
            ('pale', 'ble', False),
            ('a', 'b', True),
            ('', 'd', True),
            ('d', 'de', True),
            ('pale', 'pale', True),
            ('pale', 'ple', True),
            ('ple', 'pale', True),
            ('pale', 'bale', True),
            ('pale', 'bake', False),
            ('pale', 'pse', False),
            ('ples', 'pales', True),
            ('pale', 'pas', False),
            ('pas', 'pale', False),
            ('pale', 'pkle', True),
            ('pkle', 'pable', False),
            ('pal', 'palks', False),
            ('palks', 'pal', False)
        ]

    def test_one_away(self):
        for orig, edit, result in self.data:
            self.assertEqual(one_away(orig, edit), result)

if __name__ == "__main__":
    unittest.main()