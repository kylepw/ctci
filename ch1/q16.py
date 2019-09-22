"""
    q16.py
    ~~~~~~

    String Compression: Implement a method to perform basic string compression
    using the counts of repeated characters. For example, the string
    aabcccccaaa would become a2b1c5a3. If the "compressed" string would not
    become smaller than the original string, your method should return the
    original string. You can assume the string has only uppercase and lowercase
    letters (a - z).
    Hints: #92, #110
"""
import unittest


def str_compress(s):
    counter = [{s[0]: 0}]
    only_ones = True
    for c in s:
        if c in counter[-1]:
            counter[-1][c] += 1
            if counter[-1][c] > 1:
                only_ones = False
        else:
            counter.append({c: 1})
    if only_ones:
        return s
    compressed = []
    for c in counter:
        for c, n in c.items():
            compressed.append(c + str(n))
    return ''.join(compressed)

def _count_compression(s):
    compressed = 0
    counter = 0
    for i in range(len(s)):
        counter += 1
        if i + 1 >= len(s) or s[i] != s[i + 1]:
            compressed += 1 + len(str(counter))
            counter = 0
    return compressed

def str_compress_solution(s):
    if _count_compression(s) >= len(s):
        return s
    compressed = []
    counter = 0
    for i in range(len(s)):
        counter += 1
        if i + 1 >= len(s) or s[i] != s[i + 1]:
            compressed.append(s[i])
            compressed.append(str(counter))
            counter = 0
    return ''.join(compressed)


class TestStrCompress(unittest.TestCase):
    def setUp(self):
        self.data = [
            ('aabcccccaaa', 'a2b1c5a3'),
            ('abcdef', 'abcdef')
        ]

    def test_str_compress(self):
        for s, expected in self.data:
            self.assertEqual(str_compress_solution(s), expected)

if __name__ == '__main__':
    unittest.main()