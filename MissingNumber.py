# https://leetcode.com/problems/missing-number/

# Daily Question 20.02.24

# 268. Missing Number

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # _max = max(nums)
        # for i in range(_max + 1):
        #     if i not in nums:
        #         return i
        # return i + 1

        n = len(nums)
        _sum = (n * (n + 1)) // 2
        a_sum = sum(nums)
        return _sum - a_sum

        # nums.sort()

        # if nums[-1] == len(nums) - 1:
        #     return len(nums)

        # i = 0
        # while i < len(nums):
        #     if i != nums[i]:
        #         return i
        #     i += 1


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().missingNumber(nums))
