"""
    q43.py
    ~~~~~~
    List of Depths: Given a binary tree, design an algorithm which creates
    a linked list of all the nodes at each depth (e.g. if you have a tree
    with depth D, you'll have D linked lists).

    Hints: #107, #123, #135
"""
from math import log
import unittest


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __repr__(self):
        return f'Node ({self.value})'


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        if self.next is None:
            return f'Node ({self.value})'
        return f'Node ({self.value}) -> {self.next}'


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


def list_of_depths(node, depth_nodes=None, depth=None):
    """Return list of nodes at each depth."""
    if not node:
        return
    if depth_nodes is None:
        depth_nodes = []
    if depth is None:
        depth = 0

    if len(depth_nodes) - 1 < depth:
        depth_nodes.append(LinkedListNode(node.value))
    else:
        depth_nodes[depth].next = LinkedListNode(node.value)
    list_of_depths(node.left, depth_nodes, depth + 1)
    list_of_depths(node.right, depth_nodes, depth + 1)

    return node


class TestListOfDepths(unittest.TestCase):
    def setUp(self):
        self.heads = [
            array_to_binary([3, 5, 6, 9, 17, 23]),
            array_to_binary([0, 2, 5, 6, 11, 45, 101]),
        ]

    def test_list_of_depths(self):
        for head in self.heads:
            depth_nodes = []
            list_of_depths(head, depth_nodes)
            for depth, nodes in enumerate(depth_nodes):
                print(depth, nodes)


if __name__ == "__main__":
    unittest.main()