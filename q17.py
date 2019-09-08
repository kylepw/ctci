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
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[N-1-i][layer]

            # bottom -> left
            matrix[N-1-i][layer] = matrix[N-1-layer][N-1-i]

            # right -> bottom
            matrix[N-1-layer][N-1-i] = matrix[i][N-1-layer]

            # top -> right
            matrix[i][N-1-layer] = top
    return matrix

def rotate_matrix_copy(matrix):
    N = len(matrix)

    new_matrix = [row[ : ] for row in matrix]
    for i in range(N):
        for j in range(N):
            new_matrix[j][N - 1 - i] = matrix[i][j]
    return new_matrix


class TestRotateMatrix(unittest.TestCase):
    def setUp(self):
        self.data = ([
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

    def test_rotate_matrix(self):
        self.assertEqual(rotate_matrix(self.data[0]), self.data[1])

    @unittest.SkipTest
    def test_rotate_matrix_copy(self):
            self.assertEqual(rotate_matrix_copy(self.data[0]), self.data[1])

if __name__ == '__main__':
    unittest.main()