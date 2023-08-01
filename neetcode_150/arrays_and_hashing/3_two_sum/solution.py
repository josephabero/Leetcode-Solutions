"""
Two Sum:
https://leetcode.com/problems/two-sum
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        values = {}

        for i, num in enumerate(nums):
            other = target - num

            if other in values:
                return [i, values[other]]

            values[num] = i
