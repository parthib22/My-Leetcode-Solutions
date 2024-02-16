# https://leetcode.com/problems/move-zeroes/description/

# 283. Move Zeroes

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# Follow up: Could you minimize the total number of operations done?


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        count = 0
        # count = nums.count(0)
        # length = len(nums)
        # if count == length:
        #     return
        # for _ in range(count):
        #     nums.remove(0)
        #     nums.append(0)
        temp = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[temp] = nums[i]
                temp += 1
            else:
                count += 1

        for i in range(len(nums) - count, len(nums)):
            nums[i] = 0


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    Solution().moveZeroes(nums)
    print(nums)
