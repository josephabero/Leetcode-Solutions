"""
Sqrt(x)
https://leetcode.com/problems/sqrtx/
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        start = 0
        end = x
        result = 0

        while start <= end:
            mid = ((end - start) // 2) + start

            if mid * mid > x:
                end = mid - 1
            elif mid * mid < x:
                start = mid + 1
                result = mid
            else:
                return mid
        return math.floor(result)
