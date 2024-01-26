"""
Reverse Integer
https://leetcode.com/problems/reverse-integer
"""

class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT = -2 ** 31    # -2^31
        MAX_INT = 2 ** 31 - 1 #  2^31 - 1
        reverse = 0

        while x != 0:
            if (reverse > (MAX_INT / 10)) or (reverse < (MIN_INT / 10)):
                return 0
            digit = x % 10 if x > 0 else x % -10
            reverse = (reverse * 10) + digit
            x = int(x / 10)
        return reverse
