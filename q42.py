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


    def __str__(self):
        return f'Node ({self.value})'

def _insert_vals(head, values):
    """Insert binary tree values in `values` from `head`"""
    stack = [head]

    while stack:
        current = stack.pop()
        while len(current.children) < 2 and values:
            current.children.append(Node(values.pop()))
        stack.extend(current.children)

    return head

def create_bst(array):
    """Create binary search tree from sorted `array`."""
    if array != sorted(array):
        return False
    root_val = array.pop(len(array) // 2)
    left = [val for val in array if val <= root_val]
    right = [val for val in array if val > root_val]

    root = Node(root_val)
    left_head = Node(left.pop())
    right_head = Node(right.pop())
    root.children.extend([left_head, right_head])

    _insert_vals(left_head, left)
    _insert_vals(right_head, right)

    return root



class TestCreateBst(unittest.TestCase):
    def setUp(self):
        self.arrays = (
            [3, 5, 6, 9, 17, 23],
            [0, 2, 5, 6, 11, 45, 101],
        )

    def test_create_bst(self):
        for array in self.arrays:
            root = create_bst(array)
            stack = [root]
            print(f'Min val: {root.value}')
            while stack:
                node = stack.pop()
                if node.value <= root.value:
                    print('left', node)
                else:
                    print('right', node)
                stack.extend(node.children)


if __name__ == '__main__':
    unittest.main()