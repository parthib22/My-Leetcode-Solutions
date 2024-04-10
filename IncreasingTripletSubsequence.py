# https://leetcode.com/problems/increasing-triplet-subsequence/

# 334. Increasing Triplet Subsequence

# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

# Example 1:
# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.

# Example 2:
# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.

# Example 3:
# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

# Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # for i in range(len(nums) - 2):
        #     L = [nums[i]]
        #     for j in range(i,len(nums)):
        #         if nums[j] > L[-1]:
        #             L.append(nums[j])
        #         elif nums[j] > nums[i] and nums[j] < L[-1]:
        #             L.pop()
        #             L.append(nums[j])
        #         if len(L) == 3:
        #             return True
        # return False

        one = two = float("inf")
        for num in nums:
            if num <= one:
                one = num
            elif num <= two:
                two = num
            else:
                return True
        return False


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().increasingTriplet(nums))
