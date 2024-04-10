# https://leetcode.com/problems/isomorphic-strings/

# Daily 02.04.2024

# 205. Isomorphic Strings

# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

# Example 3:
# Input: s = "paper", t = "title"
# Output: true


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = {}
        d2 = {}
        for i in range(len(s)):
            if s[i] not in d1 and t[i] not in d2:
                d1[s[i]] = t[i]
                d2[t[i]] = s[i]
            elif s[i] in d1 and d1[s[i]] != t[i]:
                return False
            elif t[i] in d2 and d2[t[i]] != s[i]:
                return False
        return True


if __name__ == "__main__":
    s, t = list(map(str, input().split()))
    print(Solution().isIsomorphic(s, t))
