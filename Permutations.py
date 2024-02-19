# https://leetcode.com/problems/permutations/

# 46. Permutations

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:
# Input: nums = [1]
# Output: [[1]]


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        L = []

        def per(s, i, length):
            if i == length:
                L.append(list(s))
            else:
                for j in range(i, length):
                    s[i], s[j] = s[j], s[i]
                    per(s, i + 1, length)
                    s[i], s[j] = s[j], s[i]

        per(nums, 0, len(nums))
        return L


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().permute(nums))
