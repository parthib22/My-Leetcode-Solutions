# https://leetcode.com/problems/factorial-trailing-zeroes/

# 172. Factorial Trailing Zeroes

# Given an integer n, return the number of trailing zeroes in n!.

# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

# Example 1:
# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.

# Example 2:
# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.

# Example 3:
# Input: n = 0
# Output: 0


class Solution:
    def trailingZeroes(self, n: int) -> int:
        # f = 1
        # for i in range(n):
        #     f = f * (i + 1)
        # count = 0
        # while f > 0:
        #     if f % 10 != 0:
        #         break
        #     count += 1
        #     f //= 10
        # return count

        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)

        # count = 0
        # while n > 0:
        #     n = n // 5
        #     count += n
        # return count


if __name__ == "__main__":
    print(Solution().trailingZeroes(int(input())))
