"""
Container With Most Water
https://leetcode.com/problems/container-with-most-water
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        largest = 0

        left = 0
        right = len(height) - 1

        while left < right:
            product = min(height[left], height[right]) * (right - left)

            largest = max(product, largest)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return largest
