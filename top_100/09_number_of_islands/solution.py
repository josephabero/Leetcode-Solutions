"""
Number of Islands
https://leetcode.com/problems/number-of-islands
"""
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(row, col):
            queue = deque()
            visited.add((row, col))
            queue.append((row, col))

            while queue:
                r, c = queue.popleft()

                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                for d_row, d_col in directions:
                    row, col = r + d_row, c + d_col

                    if row in range(len(grid))      and \
                       col in range(len(grid[0]))   and \
                       grid[row][col] == "1"        and \
                       (row, col) not in visited:
                        visited.add((row, col))
                        queue.append((row, col))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1

        return islands
