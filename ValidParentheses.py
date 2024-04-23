# https://leetcode.com/problems/valid-parentheses/

# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false


class Solution:
    def isValid(self, s: str) -> bool:

        # stack = []
        # open_, close = "[{(", "]})"

        # for c in s:
        #     if stack == [] or c in open_:
        #         stack.append(c)
        #     elif c in close:
        #         if stack[-1] in open_ and \
        #          open_.index(stack[-1]) == close.index(c):
        #             stack.pop()
        #         else:
        #             break
        #     else:
        #         stack.append(c)

        # return True if stack == [] else False

        if len(s) % 2 > 0:
            return False

        stack = []
        d = {"[": "]", "{": "}", "(": ")"}

        for c in s:

            if c in d:
                stack.append(c)

            elif not stack or d[stack.pop()] != c:
                return False

        return not stack


if __name__ == "__main__":
    s = input()
    print(Solution().isValid(s))
