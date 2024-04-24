# https://leetcode.com/problems/n-th-tribonacci-number/

# Daily 24.04.24

# 1137. N-th Tribonacci Number

# The Tribonacci sequence Tn is defined as follows:

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.

# Example 1:
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

# Example 2:
# Input: n = 25
# Output: 1389537


class Solution:
    def tribonacci(self, n: int) -> int:

        x, y, z = 0, 1, 1

        for _ in range(n):
            c = x + y + z
            x = y
            y = z
            z = c

        return x

        # def helper(n):
        #     if n == 0:
        #         return 0
        #     if n == 1 or n == 2:
        #         return 1

        #     return helper(n - 1) + helper(n - 2) + helper(n - 3)

        # return helper(n)


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        print(Solution().tribonacci(i), end=" ")
