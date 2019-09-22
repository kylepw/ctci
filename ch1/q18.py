"""
    q18.py
    ~~~~~~

    Zero Matrix: Write an algorithm such that if an element in an MxN matrix
    is 0, its entire row and column are set to 0.

    Hints: #17, 74, #102
"""
import unittest


def zero_matrix(matrix):
    M = len(matrix)
    N = len(matrix[0])

    columns = set()
    rows = set()
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                rows.add(i)
                columns.add(j)
                break
    zero_row(matrix, rows)
    zero_columns(matrix, columns)
    return matrix

def zero_row(matrix, rows):
    for row in rows:
        for j in range(len(matrix[0])):
            matrix[row][j] = 0

def zero_columns(matrix, columns):
    for column in columns:
        for i in range(len(matrix)):
            matrix[i][column] = 0

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()