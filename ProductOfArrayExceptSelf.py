# https://leetcode.com/problems/product-of-array-except-self/

# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # L = list()
        # prod = 1
        # _count = nums.count(0)
        # _len = len(nums)
        # if _count > 1:
        #     L = [0 for i in range(_len)]
        # else:
        #     for num in nums:
        #         if num != 0:
        #             prod = prod * num
        #     if _count == 0:
        #         for num in nums:
        #             L.append(prod // num)
        #     elif _count == 1:
        #         L = [0 for i in range(_len)]
        #         L[nums.index(0)] = prod
        # return L

        if 0 not in nums:
            mul = 1
            for num in nums:
                mul *= num
            return [mul // num for num in nums]
        else:
            zero = 0
            for num in nums:
                zero += 1 if num == 0 else 0
                if zero > 1:
                    break
            if zero > 1:
                return [0] * len(nums)
            mul = 1
            if zero == 1:
                for num in nums:
                    mul *= num if num != 0 else 1
                return [mul if num == 0 else 0 for num in nums]


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().productExceptSelf(nums))
