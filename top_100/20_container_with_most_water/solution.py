"""
Container With Most Water
https://leetcode.com/problems/container-with-most-water/
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        largest = 0

        while right > left:
            water = min(height[right], height[left]) * (right - left)

            if water > largest:
                largest = water

            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

        return largest
