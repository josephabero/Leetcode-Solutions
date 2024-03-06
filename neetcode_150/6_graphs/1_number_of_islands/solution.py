"""
Number of Islands
https://leetcode.com/problems/number-of-islands
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        num_of_islands = 0

        def visit_island(x, y):
            if grid[x][y] == "1" and (x, y) not in visited:
                visited.add((x, y))
            else:
                return

            directions = [
                (-1, 0),    # Up
                (1, 0),     # Down
                (0, -1),    # Left
                (0, 1),     # Right
            ]

            for dx, dy in directions:
                if 0 <= (x + dx) < len(grid) and \
                    0 <= (y + dy) < len(grid[0]):
                    visit_island((x + dx), (y + dy))


        for x, row in enumerate(grid):
            for y, col in enumerate(grid[x]):
                if grid[x][y] == "1" and (x, y) not in visited:
                    num_of_islands += 1
                    visit_island(x, y)

        return num_of_islands
