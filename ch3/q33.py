"""
    q33.py
    ~~~~~~
    Stack of Plates
"""
import random
import unittest


class StackOfPlates:
    def __init__(self, size=None):
        self.size = size if size else 3
        self.stacks = [[]]
        self.current = 0

    def push(self, value):
        if len(self.stacks[self.current]) >= self.size:
            self.stacks.append([value])
            self.current += 1
        else:
            self.stacks[self.current].append(value)

    def pop(self):
        if not self.stacks[self.current]:
            return None
        value = self.stacks[self.current].pop()
        if self.current > 0 and not self.stacks[self.current]:
            del self.stacks[self.current]
            self.current -= 1
        return value

    def peek(self):
        return self.stacks[self.current][-1] if self.stacks[self.current] else None

    def pop_at(self, index):
        if index == -1 or index == len(self.stacks) - 1:
            value = self.stacks[index].pop()
            self.stacks.pop()
            return value
        value = self.stacks[index].pop()
        self.stacks[index].append(self.stacks[index + 1][0])
        for i in range(index + 1, len(self.stacks)):
            if len(self.stacks[i]) > 1:
                for j in range(len(self.stacks[i]) - 1):
                    self.stacks[i][j] = self.stacks[i][j + 1]
                if i < len(self.stacks) - 1:
                    self.stacks[i].pop()
                    self.stacks[i].append(self.stacks[i + 1][0])
        self.stacks[-1].pop()
        if len(self.stacks[-1]) < 1:
            self.stacks.pop()
        return value



class TestStackOfPlates(unittest.TestCase):
    def setUp(self):
        self.size = 5
        self.s = StackOfPlates(size=self.size)

    def test_push(self):
        for _ in range(self.size * self.size):
            val = random.randint(10, 100)
            self.s.push(val)
            self.assertEqual(self.s.peek(), val)

    def test_pop(self):
        for _ in range(self.size * self.size):
                self.s.push(random.randint(10, 100))

        for _ in range(self.size * self.size):
            top = self.s.peek()
            self.assertEqual(self.s.pop(), top)
            self.assertNotEqual(self.s.peek(), top)

        self.assertIsNone(self.s.pop())

    def test_pop_at(self):
        for _ in range(self.size * self.size):
                self.s.push(random.randint(10, 100))

        for i in range(self.size-1):
            self.s.pop_at(i)

        self.s.pop_at(-1)
        self.assertEqual(len(self.s.stacks), self.size-1)
