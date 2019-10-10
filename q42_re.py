"""
    q42_re.py
    ~~~~~~
    Minimal Tree: Given a sorted (increasing order) array with unique integer
    elements, write an algorithm to create a binary search tree with minimal
    height.

    Hints: #19, #73, #116
"""
import unittest


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        return f'({self.left}:L V: {self.value} R:{self.right})'


def array_to_binary(array, start=None, end=None):
    """Create binary search tree from `array` values via recursion."""
    start = 0 if start is None else start
    end = len(array) - 1 if end is None else end
    if start > end:
        return ''
    mid = (start + end) // 2
    node = Node(array[mid])
    node.left = array_to_binary(array, start, mid - 1)
    node.right = array_to_binary(array, mid + 1, end)

    return node


class TestArrayToBinary(unittest.TestCase):
    def setUp(self):
        self.arrays = (
            [3, 5, 6, 9, 17, 23],
            [0, 2, 5, 6, 11, 45, 101],
        )

    def test_create_bst(self):
        for array in self.arrays:
            print(array_to_binary(array))


if __name__ == "__main__":
    unittest.main()