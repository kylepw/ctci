"""
    q51.py
    ~~~~~~
    Insertion: Given two 32-bit numbers, M and N, and two bit positions,
    i and j, insert M into N between i and j positions, inclusive.

    Hints: #137, #169, #215
"""
import unittest


def bit_insert(N, M, i, j):
    # Clear bits i ~ j
    clear_mask = 0
    for c in range(32):
        if c < i or c > j:
            clear_mask += 1 << c
    # Insert
    insert_mask = M << i
    print(bin(N | insert_mask))
    return N | insert_mask


class TestBitInsert(unittest.TestCase):
    def test_bit_insert(self):
        data = {
            # (N=10000000000, M=10011, i=2, j=6): 10001001100
            (1024, 19, 2, 6): 1100,
        }
        for args, expected in data.items():
            self.assertEqual(bit_insert(*args), expected)

if __name__ == "__main__":
    unittest.main()