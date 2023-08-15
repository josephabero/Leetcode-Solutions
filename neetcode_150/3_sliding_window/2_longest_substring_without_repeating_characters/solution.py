"""
Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub = 0
        sub = set()
        left = 0

        for right in range(len(s)):
            while s[right] in sub:
                sub.remove(s[left])
                left += 1

            sub.add(s[right])

            if len(sub) > max_sub:
                max_sub = len(sub)
                
            right += 1

        return max_sub
