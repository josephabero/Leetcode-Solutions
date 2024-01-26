"""
Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
"""
class Solution:
    def isValid(self, s: str) -> bool:
        closed_brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        for char in s:
            if char in closed_brackets:
                if not stack or closed_brackets[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
