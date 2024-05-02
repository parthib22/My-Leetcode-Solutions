# https://leetcode.com/problems/first-missing-positive/

# 41. First Missing Positive

# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

# Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.

# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.

# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.


from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums = list(set(nums))
        nums.sort()

        i = 0
        while nums and nums[i] < 0:
            nums.remove(nums[i])

        if not nums or nums[0] > 1:
            return 1

        m = len(nums) - 1
        for i in range(m):
            if nums[i + 1] != nums[i] + 1:
                m = i
                break

        return nums[m] + 1


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().firstMissingPositive(nums))
