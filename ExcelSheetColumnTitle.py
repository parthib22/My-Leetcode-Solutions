# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...

# Example 1:

# Input: columnNumber = 1
# Output: "A"
# Example 2:

# Input: columnNumber = 28
# Output: "AB"
# Example 3:

# Input: columnNumber = 701
# Output: "ZY"

n = int(input())
s = ""
# if n <= 26:
#     print(chr(n + 64))
# elif n % 26 == 0:
#     print(chr(n // 26 + 63) + chr(26 + 64))
# else:
while n > 0:
    n -= 1
    # L.append(n%26)
    # if m == 0:
    #     m = 26
    s = chr(65 + n % 26) + s
    n = n // 26

print(s)
