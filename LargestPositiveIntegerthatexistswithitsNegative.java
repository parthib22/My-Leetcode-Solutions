// https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

// Daily 02.05.2024

// 2441. Largest Positive Integer That Exists With Its Negative

// Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

// Return the positive integer k. If there is no such integer, return -1.

// Example 1:
// Input: nums = [-1,2,-3,3]
// Output: 3
// Explanation: 3 is the only valid k we can find in the array.

// Example 2:
// Input: nums = [-1,10,6,7,-7,1]
// Output: 7
// Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.

// Example 3:
// Input: nums = [-10,8,6,7,-2,-3]
// Output: -1
// Explanation: There is no a single valid k, we return -1.

import java.util.Arrays;
import java.util.Scanner;

public class LargestPositiveIntegerthatexistswithitsNegative {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Solution sol = new Solution();
        int[] nums = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        System.out.println(sol.findMaxK(nums));
        sc.close();
    }
}

class Solution {
    public int findMaxK(int[] nums) {
        int mx = -1;
        for (int num : nums) {
            if (num > mx) {
                for (int num2 : nums) {
                    if (num2 == num * -1) {
                        mx = num;
                        break;
                    }
                }
            }
        }
        return mx;
    }
}