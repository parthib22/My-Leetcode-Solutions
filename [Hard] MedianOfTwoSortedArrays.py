# https://leetcode.com/problems/median-of-two-sorted-arrays/

# 4. Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(list(nums1 + nums2))
        mid = len(merged) // 2

        if len(merged) % 2 != 0:
            return merged[mid]

        return (merged[mid - 1] + merged[mid]) / 2


if __name__ == "__main__":
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    ob = Solution()
    print(float(ob.findMedianSortedArrays(nums1, nums2)))
