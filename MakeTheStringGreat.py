# https://leetcode.com/problems/make-the-string-great/

# 1544. Make The String Great

# Given a string s of lower and upper case English letters.

# A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

# 0 <= i <= s.length - 2
# s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
# To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

# Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

# Notice that an empty string is also good.

# Example 1:
# Input: s = "leEeetcode"
# Output: "leetcode"
# Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

# Example 2:
# Input: s = "abBAcC"
# Output: ""
# Explanation: We have many possible scenarios, and all lead to the same answer. For example:
# "abBAcC" --> "aAcC" --> "cC" --> ""
# "abBAcC" --> "abBA" --> "aA" --> ""
# Example 3:

# Input: s = "s"
# Output: "s"

# import math


class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while i < len(s) - 1:
            if (s[i].islower() and s[i + 1].isupper() and s[i + 1] == s[i].upper()) or (
                s[i + 1].islower() and s[i].isupper() and s[i + 1] == s[i].lower()
            ):
                s = s[:i] + s[i + 2 :]
                i = 0
                continue
            i += 1
        return s

        # l = list(s)
        # while len(l)>0:
        #     f=0
        #     for i in range(0, len(l)-1):
        #         if l[i].upper()==l[i+1].upper() \
        #          and math.fabs(ord(l[i])-ord(l[i+1]))==32:
        #             l[i:i+2]=[]
        #             f=1
        #             break
        #     if f==0:
        #         break
        # st = ''.join(l)
        # return st


if __name__ == "__main__":
    s = input()
    print(Solution().makeGood(s))
