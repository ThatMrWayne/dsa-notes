# 36


def check_center(row, col, board):
    memo = set()
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if board[i][j] == ".":
                continue
            if board[i][j] in memo:
                return False
            memo.add(board[i][j])
    return True

def isValidSudoku(board) -> bool:
    rows_set, cols_set = [], []
    for i in range(9):
        rows_set.append(set())
        cols_set.append(set())
    center_point_idx = {1,4,7}

    for row in range(9):
        for col in range(9):
            if row in center_point_idx and col in center_point_idx:
                if not self.check_center(row, col, board):
                    return False
            if board[row][col] == ".":
                continue
            if board[row][col] in rows_set[row] or board[row][col] in cols_set[col]:
                return False
            else:
                rows_set[row].add(board[row][col])
                cols_set[col].add(board[row][col])
    return True
