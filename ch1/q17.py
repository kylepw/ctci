"""
    q17.py
    ~~~~~~

    Rotate Matrix: Given an image represented by an NxN matrix, where each
    pixel in the image is 4 bytes, write a method to rotate the image by
    90 degrees. Can you do this in place?

    Hints: #51, #100
"""
import unittest

def rotate_matrix(matrix):
    """Rotate in-place"""
    N = len(matrix)

    for layer in range(N // 2):
        first, last = layer, N - 1 - layer,
        for i in range(first, last):
            top = matrix[first][i]

            # left -> top
            matrix[first][i] = matrix[N-1-i][first]

            # bottom -> left
            matrix[N-1-i][first] = matrix[last][N-1-i]

            # right -> bottom
            matrix[last][N-1-i] = matrix[i][last]

            # top -> right
            matrix[i][last] = top
    return matrix

def rotate_matrix_copy(matrix):
    N = len(matrix)

    new_matrix = [row[ : ] for row in matrix]
    for i in range(N):
        for j in range(N):
            new_matrix[j][N - 1 - i] = matrix[i][j]
    return new_matrix

def rotate_matrix_solution(matrix):
    if len(matrix) <= 1 or len(matrix) != len(matrix[0]):
        return matrix
    N = len(matrix)

    for layer in range(N // 2):
        first, last = layer, N - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]

            # left -> top
            matrix[first][i] = matrix[last - offset][first]

            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top
    return matrix


class TestRotateMatrix(unittest.TestCase):
    def setUp(self):
        self.data = [
            ([
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25]
            ], [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5]
            ])
        ]

    @unittest.SkipTest
    def test_rotate_matrix(self):
        for before, after in self.data:
            self.assertEqual(rotate_matrix(before), after)

    @unittest.SkipTest
    def test_rotate_matrix_copy(self):
        for before, after in self.data:
            self.assertEqual(rotate_matrix_copy(before), after)
            self.assertEqual(rotate_matrix_copy(before), after)

    def test_rotate_matrix_solution(self):
        for before, after in self.data:
            self.assertEqual(rotate_matrix_solution(before), after)

if __name__ == '__main__':
    unittest.main()