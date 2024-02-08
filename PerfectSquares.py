# https://leetcode.com/problems/perfect-squares/

# Daily Challenge 08.02.24

# 279. Perfect Squares

# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

# Example 1:
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.

# Example 2:
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

n = int(input())
dp = [0] + [float("inf")] * n
for i in range(1, int(n**0.5) + 1):
    for j in range(i * i, n + 1):
        dp[j] = min(dp[j], dp[j - i * i] + 1)
print(dp[-1])
