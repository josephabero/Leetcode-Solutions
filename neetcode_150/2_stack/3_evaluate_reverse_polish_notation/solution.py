"""
Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in set("+-*/"):
                right = stack.pop()
                left = stack.pop()

                match(token):
                    case "+":
                        result = left + right
                    case "-":
                        result = left - right
                    case "*":
                        result = left * right
                    case "/":
                        result = left / right
                
                stack.append(int(result))

            else:
                stack.append(int(token))
        
        return stack.pop()
