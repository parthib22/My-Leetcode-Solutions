# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]

# Example 2:

# Input: rowIndex = 0
# Output: [1]

# Example 3:

# Input: rowIndex = 1
# Output: [1,1]

rowIndex = int(input())
L = []
M = [1]
for i in range(rowIndex):
    M = [1]
    for j in range(i):
        M.append(L[j] + L[j + 1])
    M.append(1)
    L = M
print(M)
