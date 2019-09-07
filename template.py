"""
    q??.py
    ~~~~~~

"""
import unittest


def method():
    pass

class TestMethod(unittest.TestCase):
    def setUp(self):
        self.data = ()

    def test_method(self):
        for d in self.data:
            pass

if __name__ == '__main__':
    unittest.main()