# https://leetcode.com/problems/find-the-pivot-integer/

# Daily 13.03.2024

# 2485. Find the Pivot Integer

# Given a positive integer n, find the pivot integer x such that:

# The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
# Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

# Example 1:
# Input: n = 8
# Output: 6
# Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

# Example 2:
# Input: n = 1
# Output: 1
# Explanation: 1 is the pivot integer since: 1 = 1.

# Example 3:
# Input: n = 4
# Output: -1
# Explanation: It can be proved that no such integer exist.


from math import sqrt


class Solution:
    def pivotInteger(self, n: int) -> int:
        # nums = [num for num in range(1, n + 1)]
        # for x in range(n // 2, n + 1):
        #     if sum(nums[: x + 1]) == sum(nums[x:]):
        #         return x + 1
        # return -1

        x = sqrt(n * (n + 1) / 2)
        return int(x) if x % 1 == 0 else -1


if __name__ == "__main__":
    print(Solution().pivotInteger(int(input())))
