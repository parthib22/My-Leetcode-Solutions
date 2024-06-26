// https://leetcode.com/problems/reverse-prefix-of-word/

// Daily 01.05.2024

// 2000. Reverse Prefix of Word

// Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

// For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
// Return the resulting string.

// Example 1:
// Input: word = "abcdefd", ch = "d"
// Output: "dcbaefd"
// Explanation: The first occurrence of "d" is at index 3.
// Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

// Example 2:
// Input: word = "xyxzxe", ch = "z"
// Output: "zxyxxe"
// Explanation: The first and only occurrence of "z" is at index 3.
// Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".

// Example 3:
// Input: word = "abcd", ch = "z"
// Output: "abcd"
// Explanation: "z" does not exist in word.
// You should not do any reverse operation, the resulting string is "abcd".

import java.util.Scanner;

public class ReversePrefixofWord {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Solution sol = new Solution();
        String word = sc.next();
        char ch = sc.next().charAt(0);
        System.out.println(sol.reversePrefix(word, ch));
        sc.close();
    }

}

class Solution {
    public String reversePrefix(String word, char ch) {

        int idx = word.indexOf(ch);

        if (idx == -1)
            return word;

        String st = "";

        for (int i = 0; i <= idx; i++) {
            st = word.charAt(i) + st;
        }
        return st + word.substring(idx + 1);
    }
}