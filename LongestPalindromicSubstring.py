# https://leetcode.com/problems/longest-palindromic-substring/

# 5. Longest Palindromic Substring

# Given a string s, return the longest
# palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        #         p = s[::-1]
        #         if s == p:
        #             return s
        #         max = 0
        #         temp = s[0]
        #         k = ""
        #         for i in range(len(s) - 1):
        #             for j in range(i + 1, len(s)):
        #                 k = s[i : j + 1]
        #                 if k in p and k == k[::-1] and max < len(k):
        #                     print(k)
        #                     max = len(k)
        #                     temp = k
        #         return temp

        # class Solution(object):
        #     def longestPalindrome(self, s):

        n = len(s)

        l = ""

        for i in range(n):
            for j in range(i, n):
                l1 = s[i : j + 1]
                if l1[::-1] == l1 and len(l1) > len(l):
                    l = l1

        return l


if __name__ == "__main__":
    ob = Solution()
    print(ob.longestPalindrome(input()))
