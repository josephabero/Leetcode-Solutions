"""
Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        longest = 0
        
        # Handle single character edge case
        if len(s) == 1:
            return s
        
        for i in range(len(s) - 1):
            # Even Length Palinedrome
            left = i
            right = i + 1

            while(left >= 0 and right < len(s) and s[left] == s[right]):
                if right - left + 1 > longest:
                    longest = right - left + 1
                    result = s[left:right + 1]
                left -= 1
                right += 1

            # Odd Length Palindrome
            left = right = i

            while(left >= 0 and right < len(s) and s[left] == s[right]):
                if right - left + 1 > longest:
                    longest = right - left + 1
                    result = s[left:right + 1]
                left -= 1
                right += 1
 
        return result