"""
    q44.py
    ~~~~~~
    Check Balanced: Implement a function to check if a binary tree is balanced. For
    the purposes of this question, a balanced tree is defined to be a tree such that
    the heights of the two subtrees of any node never differ by more than one.

    Hints: #21, #33, #49, #105, #124
"""
import unittest


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __repr__(self):
        return f'Node ({self.value})'


def array_to_binary(array, start=None, end=None):
    """Create binary search tree from `array` values via recursion."""
    start = 0 if start is None else start
    end = len(array) - 1 if end is None else end
    if start > end:
        return None
    mid = (start + end) // 2
    node = Node(array[mid])
    node.left = array_to_binary(array, start, mid - 1)
    node.right = array_to_binary(array, mid + 1, end)

    return node


def balanced(node, height=None):
    """Return True if two trees are balanced, False if not"""
    if node is None:
        print(height)
        return height

    if height is None:
        height = 0
    return (balanced(node.left, height + 1) == balanced(node.right, height + 1)) or (balanced(node.left, height + 1) == balanced(node.right, height + 1) + 1) or (balanced(node.left, height + 1) == balanced(node.right, height + 1) - 1)


class TestBalanced(unittest.TestCase):
    def setUp(self):
        balanced_tree = array_to_binary([3, 5, 6, 9, 17, 23])
        unbalanced_tree = array_to_binary([0, 2, 5, 6, 9, 11, 45, 101])
        node = unbalanced_tree.right
        while node.left or node.right:
            print(node)
            if node.right:
                node = node.right
            elif node.left:
                node = node.left
        node.right = Node(6)
        node.right.right = Node(6)
        self.data = {
            #balanced_tree: True,
            unbalanced_tree: False,
        }

    def test_balanced(self):
        for tree, expected in self.data.items():
            self.assertEqual(balanced(tree), expected)


if __name__ == "__main__":
    unittest.main()