"""
Happy Number
https://leetcode.com/problems/happy-number/
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        calculated = set()
        while n != 1 and n not in calculated:
            calculated.add(n)
            n = sum(int(i) ** 2 for i in str(n))
        return n == 1
