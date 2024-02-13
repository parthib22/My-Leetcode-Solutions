# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

# Daily Question 13.02.24

# 2108. Find First Palindromic String in the Array

# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

# A string is palindromic if it reads the same forward and backward.

# Example 1:
# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.

# Example 2:
# Input: words = ["notapalindrome","racecar"]
# Output: "racecar"
# Explanation: The first and only string that is palindromic is "racecar".

# Example 3:
# Input: words = ["def","ghi"]
# Output: ""
# Explanation: There are no palindromic strings, so the empty string is returned.


class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            # length = len(word)
            # for i in range(length // 2 + 1):
            #     if word[i] != word[length - i - 1]:
            #         break
            # if i == length // 2:
            #     return word
            if word == word[::-1]:
                return word
        return ""


if __name__ == "__main__":
    words = list(map(str, input().split()))
    ob = Solution()
    print(ob.firstPalindrome(words))
