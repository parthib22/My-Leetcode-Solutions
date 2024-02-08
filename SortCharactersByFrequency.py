# https://leetcode.com/problems/sort-characters-by-frequency/

# Daily Challenge 07.02.24

# 451. Sort Characters By Frequency

# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

# Example 1:
# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.


# Example 2:
# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.

# Example 3:
# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.


class Solution:
    def frequencySort(self, s: str) -> str:
        sort = ""
        L = list()
        mx = 0
        for i in range(48, 123):
            c = chr(i)
            if c in s:
                t = s.count(c)
                L.append(c * t)
                if t > mx:
                    mx = t
                #     sort = c*t + sort
                # else:
                #     sort = sort + c*t
        for i in range(mx, 0, -1):
            for e in L:
                if i == len(e):
                    sort = sort + e
        return sort


if __name__ == "__main__":
    print(Solution().frequencySort(input()))
