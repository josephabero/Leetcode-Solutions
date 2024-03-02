"""
Decode String
https://leetcode.com/problems/decode-string/
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                # Gather letters
                letters = ""
                while stack[-1] != "[":
                    letters = stack.pop() + letters
                stack.pop() # Remove [

                # Gather numbers
                numbers = ""
                while stack and stack[-1].isnumeric():
                    numbers = stack.pop() + numbers

                # Calculate substring
                stack.append(int(numbers) * letters)

        result = ""
        while stack:
            result = stack.pop() + result
        return result
