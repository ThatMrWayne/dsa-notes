from typing import List
# 289


class Solution:
    def judge(self, row, col, board):
        row_limit = len(board)-1
        col_limit = len(board[0])-1
        next_state = None
        live_count = 0

        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if i == row and j == col:
                    continue
                elif not 0<=i<=row_limit or not 0<=j<=col_limit:
                    continue
                if isinstance(board[i][j], list):
                    # [0, 1] 第一個是原始的
                    origin_state = board[i][j][0]
                else:
                    origin_state = board[i][j]
                if origin_state == 1:
                    live_count+=1
        if board[row][col] == 1:
            if live_count < 2:
                next_state = 0
            elif live_count in (2,3):
                next_state = 1
            elif live_count > 3:
                next_state = 0
        else:
            if live_count == 3:
                next_state = 1
            else:
                next_state = 0
        board[row][col] = [board[row][col], next_state]

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.judge(row, col, board)

        for row in range(len(board)):
            for col in range(len(board[0])):
                board[row][col] = board[row][col][1]
