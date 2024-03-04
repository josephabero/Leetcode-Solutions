"""
Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def get_palindrome(left, right):
            # Expand From Center
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Odd Palindromes
            odd = get_palindrome(i, i)

            # Even Palindromes
            even = get_palindrome(i, i + 1)

            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even

        return longest
