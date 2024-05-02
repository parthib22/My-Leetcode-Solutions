# https://leetcode.com/problems/shortest-palindrome/

# 214. Shortest Palindrome

# You are given a string s. You can convert s to a
# palindrome
#  by adding characters in front of it.

# Return the shortest palindrome you can find by performing this transformation.

# Example 1:
# Input: s = "aacecaaa"
# Output: "aaacecaaa"

# Example 2:
# Input: s = "abcd"
# Output: "dcbabcd"


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # if s == s[::-1]:
        #     return s

        # n = len(s)

        # for i in range(1, n):
        #     st = s[-1:-i-1:-1] + s
        #     if st == st[::-1]:
        #         break
        # return st

        reverse = s[::-1]
        n = len(s)
        for i in range(len(s)):
            if s[: n - i] == reverse[i:]:
                return reverse[:i] + s
        return ""


if __name__ == "__main__":
    s = input()
    print(Solution().shortestPalindrome(s))
