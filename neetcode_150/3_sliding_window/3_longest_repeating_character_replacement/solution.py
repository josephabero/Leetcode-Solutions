"""
Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_substring = 0
        left = 0

        chars = {}
        max_freq = 0

        for right in range(len(s)):
            # Add character to dict
            chars[s[right]] = 1 + chars.get(s[right], 0)

            # Update  max frequency as iterate through
            max_freq = max(max_freq, chars[s[right]])

            # Too many replacements, adjust sliding window
            while ((right - left + 1) - max_freq) > k:
                chars[s[left]] -= 1
                left += 1
        
            # Update max substring
            max_substring = max(right - left + 1, max_substring)
    
        return max_substring
