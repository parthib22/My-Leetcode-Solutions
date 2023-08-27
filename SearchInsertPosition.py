# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

nums = [int(x) for x in input().strip().split()]
target = int(input())
c = 0
beg = 0
end = len(nums)-1
mid = (beg + end) // 2
while beg <= end:
    if target < nums[mid]:
        end = mid - 1
    if target > nums[mid]:
        beg = mid + 1
    if target == nums[mid]:
        print(mid)
        c = 1
        break
    mid = (beg + end) // 2
if c == 0:
    print(mid+1)
