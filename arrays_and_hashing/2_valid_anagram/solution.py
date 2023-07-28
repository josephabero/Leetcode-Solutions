"""
Valid Anagram:
https://leetcode.com/problems/valid-anagram
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        values = {
            "s": {},
            "t": {}
        }

        a = b = 0
        for a, b in zip(s, t):
            if not values["s"].has_key(a):
                values["s"][a] = 0
            if not values["t"].has_key(b):
                values["t"][b] = 0

            values["s"][a] += 1
            values["t"][b] += 1

        return values["s"] == values["t"]
