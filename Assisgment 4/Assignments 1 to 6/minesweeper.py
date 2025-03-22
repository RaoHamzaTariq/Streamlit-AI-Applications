import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set()

    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row, col = divmod(loc, self.dim_size)
            if board[row][col] == '*':
                continue
            board[row][col] = '*'
            bombs_planted += 1
        return board

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        num_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) != (row, col) and self.board[r][c] == '*':
                    num_bombs += 1
        return num_bombs

    def dig(self, row, col):
        self.dug.add((row, col))
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) not in self.dug:
                    self.dig(r, c)
        return True

    def __str__(self):
        visible_board = [[' ' if (r, c) not in self.dug else str(self.board[r][c]) for c in range(self.dim_size)] for r in range(self.dim_size)]
        indices = '   ' + '  '.join(map(str, range(self.dim_size))) + '  \n'
        rows = [f'{i} |' + ' |'.join(row) + ' |' for i, row in enumerate(visible_board)]
        return indices + '-'*len(rows[0]) + '\n' + '\n'.join(rows) + '\n' + '-'*len(rows[0])


def play(dim_size=10, num_bombs=10):
    board = Board(dim_size, num_bombs)
    safe = True 
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\s)*', input("Where would you like to dig? Input as row,col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue
        safe = board.dig(row, col)
        if not safe:
            break
    if safe:
        print("CONGRATULATIONS!!!! YOU ARE VICTORIOUS!")
    else:
        print("SORRY GAME OVER :(")
        board.dug = {(r, c) for r in range(dim_size) for c in range(dim_size)}
        print(board)

if __name__ == '__main__':
    play()
