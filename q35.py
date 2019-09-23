"""
    q34.py
    ~~~~~~
    Sort Stack: Sort a stack such that smallest items are on the top

"""
import random
import unittest


class Node(object):
    def __init__(self, value):
        self.value = value
        self.above = None
        self.below = None

class Stack(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.top = None
        self.bottom = None

    def _join(self, above, below):
        if below:
            below.above = above
        if above:
            above.below = below

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def push(self, v):
        if self.size >= self.capacity:
            return False
        self.size += 1
        n = Node(v)
        if self.size == 1:
            self.bottom = n
        self._join(n, self.top)
        self.top = n
        return True

    def pop(self):
        if not self.top:
            return None
        t = self.top
        self.top = self.top.below
        self.size -= 1
        return t.value

    def peek(self):
        if not self.top:
            return None
        return self.top.value

def sort_stack(stack):
    sorted_stack = Stack(stack.capacity)
    sorted_stack.push(stack.pop())

    while not stack.is_empty():
        tmp = stack.pop()
        while sorted_stack.peek() and tmp < sorted_stack.peek():
            stack.push(sorted_stack.pop())
        sorted_stack.push(tmp)

    while not sorted_stack.is_empty():
        stack.push(sorted_stack.pop())



def my_sort_stack(stack):
    if stack.size < 1:
        return
    size = stack.size
    temp = Stack(capacity=stack.capacity)
    result = Stack(capacity=stack.capacity)

    while result.size < size:
        max_val = None
        while not stack.is_empty():
            carry = stack.pop()
            if max_val is None or max_val < carry:
                max_val = carry
            temp.push(carry)
        while not temp.is_empty():
            carry = temp.pop()
            if carry == max_val:
                print(carry)
                result.push(carry)
            else:
                stack.push(carry)

    return result


class TestMySortStack(unittest.TestCase):
    def setUp(self):
        capacity = 20
        self.s = Stack(capacity)
        values = [random.randint(10, 100) for _ in range(self.s.capacity // 2)]
        for v in values:
            self.s.push(v)
        self.sorted_vals = sorted(values)

    def test_sort_stack(self):
        sort_stack(self.s)
        for v in self.sorted_vals:
            self.assertEqual(self.s.pop(), v)

    def test_my_sort_stack(self):
        sorted_stack = my_sort_stack(self.s)
        for v in self.sorted_vals:
            self.assertEqual(sorted_stack.pop(), v)


if __name__ == '__main__':
    unittest.main()