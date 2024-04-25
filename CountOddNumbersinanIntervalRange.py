# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

# 1523. Count Odd Numbers in an Interval Range

# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

# Example 1:
# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].

# Example 2:
# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].


class Solution:
    def countOdds(self, low: int, high: int) -> int:

        num_in_between = high - low + 1

        if num_in_between % 2 == 1:
            if low % 2 == 1:
                return (num_in_between + 1) // 2

        return num_in_between // 2

        if high % 2 == 0 and low % 2 == 0:
            return (high - low) // 2
        elif not (high % 2 == 0 or low % 2 == 0):
            return (high - low) // 2 + 1
        else:
            return (high - low + 1) // 2


if __name__ == "__main__":
    low = int(input())
    high = int(input())
    print(Solution().countOdds(low, high))
