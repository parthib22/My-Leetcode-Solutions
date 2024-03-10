# https://leetcode.com/problems/intersection-of-two-arrays/

# Daily 10.03.2024

# 349. Intersection of Two Arrays

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # nums1 = list(set(nums1))
        # nums2 = list(set(nums2))
        # L=[]
        # for num in nums1:
        #     if num in nums2:
        #         L.append(num)
        # return L

        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1.intersection(set2))


if __name__ == "__main__":
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    print(Solution().intersection(nums1, nums2))
