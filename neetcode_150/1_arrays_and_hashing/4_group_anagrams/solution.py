"""
Group Anagrams
https://leetcode.com/problems/group-anagrams
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        result = defaultdict(list) # Prevents needing to check if key exists

        for s in strs:
            count = [0] * 26

            for char in s:
                # Find index by subtracting ASCII values
                # Example: 'c'  - 'a'  = 99 - 97 = 2 (index)
                count[ord(char) - ord("a")] += 1

            # Need to cast to tuple as key must be immutable
            result[tuple(count)].append(s)

        return result.values() # Prevents needing to custom format output
