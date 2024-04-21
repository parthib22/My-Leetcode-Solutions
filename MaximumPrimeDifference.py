# https://leetcode.com/problems/maximum-prime-difference/

# 3115. Maximum Prime Difference

# You are given an integer array nums.

# Return an integer that is the maximum distance between the indices of two (not necessarily different) prime numbers in nums.

# Example 1:

# Input: nums = [4,2,9,5,3]

# Output: 3

# Explanation: nums[1], nums[3], and nums[4] are prime. So the answer is |4 - 1| = 3.

# Example 2:

# Input: nums = [4,8,2,8]

# Output: 0

# Explanation: nums[2] is prime. Because there is just one prime number, the answer is |2 - 2| = 0.

import math
from typing import List


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:

        def primePosition(start: int, end: int, step: int) -> int:
            for index in range(start, end, step):
                i = 2
                while i <= int(math.sqrt(nums[index])):
                    if nums[index] % i == 0:
                        break
                    i += 1
                if nums[index] != 1 and i > int(math.sqrt(nums[index])):
                    return index
            return

        first = primePosition(0, len(nums), 1)
        last = primePosition(len(nums) - 1, -1, -1)

        return last - first


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().maximumPrimeDifference(nums))
