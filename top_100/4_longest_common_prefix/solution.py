"""
Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        if not strs:
            return prefix

        for left, first in enumerate(strs[0]):
            common = True
            for string in strs[1:]:
                if left >= len(string) or first != string[left]:
                    return prefix
            prefix += first
        return prefix
