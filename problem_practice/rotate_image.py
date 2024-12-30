#48
"""
1. flip vertically
2. do transpose
"""


class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # flip vertical
        top_row, bottom_row = 0, len(matrix)-1
        while top_row < bottom_row:
            for col in range(len(matrix)):
                temp = matrix[top_row][col]
                matrix[top_row][col] = matrix[bottom_row][col]
                matrix[bottom_row][col] = temp
            top_row+=1
            bottom_row-=1

        # transpose
        memo = set()
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                if row != col and (row,col) not in memo:
                    temp = matrix[row][col]
                    matrix[row][col] = matrix[col][row]
                    matrix[col][row] = temp
                    memo.add((row,col))
                    memo.add((col,row))
