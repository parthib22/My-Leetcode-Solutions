# https://leetcode.com/problems/power-of-two/

# 231. Power of Two

# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

# Example 1:
# Input: n = 1
# Output: true
# Explanation: 20 = 1

# Example 2:
# Input: n = 16
# Output: true
# Explanation: 24 = 16

# Example 3:
# Input: n = 3
# Output: false


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 2
        c = 0
        p = n
        while i <= n:
            if n % i == 0:
                c += 1
                n = n // i
                i = 1
            else:
                return False
            i += 1
        # print(c)
        return 2**c == p


if __name__ == "__main__":
    print(Solution().isPowerOfTwo(int(input())))
