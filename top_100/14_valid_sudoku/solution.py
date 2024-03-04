"""
Valid Sudoku
https://leetcode.com/problems/valid-sudoku/
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for row_i, row in enumerate(board):
            for col_i, value in enumerate(row):
                if value == ".":
                    continue

                if value in rows[row_i] or \
                    value in cols[col_i] or \
                    value in boxes[((row_i // 3) * 3) + (col_i // 3)]:
                    return False
                else:
                    rows[row_i].add(value)
                    cols[col_i].add(value)
                    boxes[((row_i // 3) * 3) + (col_i // 3)].add(value)
        return True
