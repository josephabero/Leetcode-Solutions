"""
3Sum
https://leetcode.com/problems/3sum
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sorted_nums = sorted(nums)

        result = []

        for first in range(0, len(nums) - 1):
            left = first + 1
            right = len(nums) - 1

            if first > 0 and sorted_nums[first] == sorted_nums[first - 1]:
                continue

            while left < right:
                sum_ = sorted_nums[first] + sorted_nums[left] + sorted_nums[right]

                if sum_ > 0:
                    right -= 1

                elif sum_ < 0:
                    left += 1

                else:
                    result.append([sorted_nums[first], sorted_nums[left], sorted_nums[right]])
                    left += 1

                    while sorted_nums[left] == sorted_nums[left - 1] and left < right:
                        left += 1

        return result
