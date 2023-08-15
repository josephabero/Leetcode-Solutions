"""
Valid Parentheses
https://leetcode.com/problems/valid-parentheses
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chars = []
        brackets = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if char in brackets:
                if len(chars) < 1:
                    return False

                if chars.pop() != brackets[char]:
                    return False

            else:
                chars.append(char)

        return True if not chars else False
