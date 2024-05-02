# https://leetcode.com/problems/reverse-string/

# 344. Reverse String

# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s = s.reverse()
        # for i in range(len(s) // 2):
        #     s[i], s[-i-1] = s[-i-1], s[i]


if __name__ == "__main__":
    s = list(map(str, input().split()))
    Solution().reverseString(s)
    print(*s)
