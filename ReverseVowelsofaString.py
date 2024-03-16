# https://leetcode.com/problems/reverse-vowels-of-a-string/

# 345. Reverse Vowels of a String

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "hello"
# Output: "holle"

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"


class Solution:
    def reverseVowels(self, s: str) -> str:
        start, end = 0, len(s) - 1
        vowel = "aAeEiIoOuU"
        s = list(s)
        while start < end:
            if s[start] in vowel and s[end] in vowel:
                if s[start] != s[end]:
                    s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            else:
                if s[start] not in vowel:
                    start += 1
                if s[end] not in vowel:
                    end -= 1
        return "".join(s)


if __name__ == "__main__":
    print(Solution().reverseVowels(input()))
