"""
Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(nums, target):
            """Helper function to perform binary search
            """
            left = 0
            right = len(nums) - 1

            while left <= right:
                middle = left + ((right - left) // 2)

                if nums[middle] < target:
                    left = middle + 1
                elif nums[middle] > target:
                    right = middle - 1
                else:
                    return True
            return False
        
        # Use binary search to find row with valid range of target values
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            row = top + ((bottom - top) // 2)
            
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bottom = row - 1
            else:
                break
        
        # While loop broke without finding valid range
        if not (top <= bottom):
            return False
        
        # Row with valid range was found, perform binary search on the row
        row = top + ((bottom - top) // 2)
        return binary_search(matrix[row], target)


