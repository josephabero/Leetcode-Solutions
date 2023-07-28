"""
Contains Duplicate:
https://leetcode.com/problems/contains-duplicate
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        values = set()

        for num in nums:
        	# `in` lookup for sets is O(1)
            if num in values:
                return True
            values.add(num)
        return False
