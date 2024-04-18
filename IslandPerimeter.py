# https://leetcode.com/problems/island-perimeter/?envType=daily-question&envId=2024-04-18

# Daily 18.04.2024

# 463. Island Perimeter

# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

# Example 1:
# https://assets.leetcode.com/uploads/2018/10/12/island.png
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.

# Example 2:
# Input: grid = [[1]]
# Output: 4

# Example 3:
# Input: grid = [[1,0]]
# Output: 4

# Constraints:
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        for row in grid:
            row.insert(0, 0)
            row.append(0)

        grid.insert(0, [0] * len(grid[0]))
        grid.append([0] * len(grid[0]))

        perimeter = 0

        for i in range(1, row_len + 1):
            for j in range(1, col_len + 1):
                if grid[i][j] == 1:
                    if grid[i - 1][j] == 0:
                        perimeter += 1
                    if grid[i + 1][j] == 0:
                        perimeter += 1
                    if grid[i][j - 1] == 0:
                        perimeter += 1
                    if grid[i][j + 1] == 0:
                        perimeter += 1

        return perimeter

    def islandPerimeter2(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        perimeter = 0

        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2

        return perimeter


if __name__ == "__main__":
    grid = [[int(x) for x in input().split()] for _ in range(int(input()))]
    print(Solution().islandPerimeter(grid))
    # print(Solution().islandPerimeter2(grid))
