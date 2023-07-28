"""
Container With Most Water
https://leetcode.com/problems/container-with-most-water
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        largest_area = 0
        
        while(left < right):
            current_height = min(height[left], height[right])
            current_width = right - left
            area = current_height * current_width
            largest_area = area if area > largest_area else largest_area
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return largest_area
                
                