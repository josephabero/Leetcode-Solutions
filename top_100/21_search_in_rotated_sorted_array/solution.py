"""
Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = ((right - left) // 2) + left

            if nums[middle] == target:
                return middle

            # Valid Left Section
            if nums[left] <= nums[middle]:
                # Target is in valid range
                if nums[left] <= target <= nums[middle]:
                    right = middle - 1
                # Target not in range, check other side
                else:
                    left = middle + 1

            # Valid Right Section
            elif nums[middle] <= nums[right]:
                # Target is in valid range
                if nums[middle] <= target <= nums[right]:
                    left = middle + 1
                # Target not in range, check other side
                else:
                    right = middle - 1

        return -1
