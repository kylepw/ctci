"""
    q42.py
    ~~~~~~
    Minimal Tree: Given a sorted (increasing order) array with unique integer
    elements, write an algorithm to create a binary search tree with minimal
    height.

    Hints: #19, #73, #116
"""
import unittest


def create_bst(array):
    """Create binary search tree from sorted `array`."""
    pass


class TestCreateBst(unittest.TestCase):
    def setUp(self):
        self.data = {
            '?': [3, 5, 6, 7, 8, 23, 34, 54, 61],
            '??': [0, 2, 5, 6, 11, 45, 101, 238],
        }

    def test_create_bst(self):
        for tree, array in self.data.items():
            self.assertEqual(create_bst(array), tree)


if __name__ == '__main__':
    unittest.main()