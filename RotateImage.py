# https://leetcode.com/problems/rotate-image/

# 48. Rotate Image

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:

# 1 2 3
# 4 5 6
# 7 8 9

# 7 4 1
# 8 5 2
# 9 6 3

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2:

# 5  1  9  11
# 2  4  8  10
# 13 3  6   7
# 15 14 12 16

# 15 13  2  5
# 14  3  4  1
# 12  6  8  9
# 16  7 10 11

# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)
        i, j = 0, n - 1

        while i < j:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i += 1
            j -= 1

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        return

    def printMatrix(self, matrix: List[List[int]]) -> None:
        for row in matrix:
            print(*row)
        print()

    def inputMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for _ in range(n):
            row = list(map(int, input().split()))
            matrix.append(row)
        return matrix


if __name__ == "__main__":

    n = int(input())
    matrix = Solution().inputMatrix(n)
    Solution().rotate(matrix)
    Solution().printMatrix(matrix)
