"""
Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
"""
class Solution:
    def getLastBracket(self, stack):
    	"""
    	Return valid last bracket in case where stack is empty
    	"""
        return stack.pop(-1) if stack else ""
    
    def isValid(self, s: str) -> bool:
        brackets = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        # Break early if Odd
        if len(s) % 2 == 1:
            return False
        
        stack = []
        for char in s:
            if char in brackets: # Closed Bracket
            	# Check for matching Open Bracket
                if brackets[char] != self.getLastBracket(stack):
                    return False
            else:
            	# Add to top of stack if open bracket
                stack.append(char)
        
        # Check for leftover open brackets
        return len(stack) == 0
            