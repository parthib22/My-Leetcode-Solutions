# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

# Example 1:
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2:
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

# Example 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # s=0
        # k=0
        # temp=text2
        # for i in text1:
        #     if i in temp:
        #         s += 1
        #         temp = temp[temp.index(i):]
        #         print(temp)
        # temp=text1
        # for i in text2:
        #     if i in temp:
        #         k += 1
        #         temp = temp[temp.index(i):]
        #         print(temp)
        # if s > k :
        #     return s
        # else:
        #     return k

        count = 0
        i = 0

        for num in text1:
            if num in text2 and text2.index(num) >= i:
                i = text2.index(num)
                count += 1
        return count


if __name__ == "__main__":
    text1, text2 = input().strip().split()
    ob = Solution()
    print(ob.longestCommonSubsequence(text1, text2))
