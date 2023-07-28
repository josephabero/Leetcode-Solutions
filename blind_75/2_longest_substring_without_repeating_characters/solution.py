"""
Longest Substring Without Repeating Characters:
https://leetcode.com/problems/longest-substring-without-repeating-characters
"""

"""
Sliding Interval using substrings
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        longest = 0
        for i in range(0, len(s)):
            if s[i] not in substring:
                substring += s[i]
            else:
                substring = substring[substring.find(s[i]) + 1:] + s[i]
            longest = max(longest, len(substring))
        return longest


"""
Sliding Interval using lookup table
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        
        longest = 0
        start = 0
        for i in range(len(s)):
            if s[i] in chars:
                start = max(start, chars[s[i]] + 1)
            chars[s[i]] = i
            longest = max(longest, i - start + 1)
        return longest