# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, p: str) -> int:
        st,str = "",""
        if len(p) == 1:
            return 1
        for i in range(len(p)):
            for j in range(i, len(p)):
                if p[j] not in st:
                    st = st + p[j]
                else:
                    if len(str) < len(st):
                        str = st
                    st = ""
                    break
        return len(str)
    
if __name__ == "__main__":
    ob = Solution()
    print(ob.lengthOfLongestSubstring(input()))