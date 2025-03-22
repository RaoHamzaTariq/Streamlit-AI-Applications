from pprint import pprint

def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == -1:
                return row, col
    return None, None  

def is_valid(board, num, row, col):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(9)]:
        return False

    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False

    return True

def solve_sudoku(board):
    row, col = find_empty_cell(board)
    if row is None:
        return True

    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = -1  

    return False  

if __name__ == "__main__":
    sudoku_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

    if solve_sudoku(sudoku_board):
        print("Sudoku Solved:")
        pprint(sudoku_board)
    else:
        print("No solution exists.")
