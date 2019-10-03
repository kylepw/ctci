"""
    q42.py
    ~~~~~~
    Minimal Tree: Given a sorted (increasing order) array with unique integer
    elements, write an algorithm to create a binary search tree with minimal
    height.

    Hints: #19, #73, #116
"""
import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def create_bst(array):
    """Create binary search tree from sorted `array`."""
    if array != sorted(array):
        return False
    root = array[len(array) // 2]
    left = [val for val in array if val <= root]
    right = [val for val in array if val > root]
    print(array)
    print(root, left, right)



class TestCreateBst(unittest.TestCase):
    def setUp(self):
        self.data = {
            '?': [3, 5, 6, 9, 17, 23],
            #'??': [0, 2, 5, 6, 11, 45, 101],
        }

    def test_create_bst(self):
        for tree, array in self.data.items():
            self.assertEqual(create_bst(array), tree)


if __name__ == '__main__':
    unittest.main()