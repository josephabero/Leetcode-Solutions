"""
Two Sum II: Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            _sum = numbers[left] + numbers[right]

            if _sum == target:
                return [left + 1, right + 1]
            elif _sum > target:
                right -= 1
            elif _sum < target:
                left += 1

