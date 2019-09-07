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
ple, pale
    Hints: #23, #97, #130
"""
import unittest


def one_replace(orig, edit):
    edited = False
    for c1, c2 in zip(orig, edit):
        if c1 != c2:
            if edited:
                return False
            edited = True
    return True

def one_edit(smaller, larger):
    difference = False
    s_index = 0
    l_index = 0
    while s_index < len(smaller):
        if smaller[s_index] != larger[l_index]:
            if difference:
                return False
            s_index -= 1
            difference = True
        s_index += 1
        l_index += 1
    return True

def one_away(orig, edit):
    if orig == edit:
        return True
    if len(orig) == len(edit):
        return one_replace(orig, edit)
    if len(orig) == (len(edit) + 1):
        return one_edit(edit, orig)
    if len(orig) == (len(edit) - 1):
        return one_edit(orig, edit)
    return False





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