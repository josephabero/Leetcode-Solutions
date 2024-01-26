"""
Search a 2D Matrix II
https://leetcode.com/problems/search-a-2d-matrix-ii
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        row, col = len(matrix) - 1, 0
        while row >= 0 and col < len(matrix[0]):
            if matrix[row][col] == target:
                return True
            elif col + 1 < len(matrix[0]) and matrix[row][col + 1] <= target:
                col += 1
            else:
                row -= 1
        return False
