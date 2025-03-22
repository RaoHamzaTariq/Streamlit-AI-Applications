import random

def display_board(board):
    print("-------")
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("-------")
    print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("-------")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")
    print("-------")

def get_player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                return move
            else:
                print("Inva lid move.")
        except ValueError:
            print("Invalid input.")
        return -1

def get_computer_move(board):
    empty_spaces = [i for i, space in enumerate(board) if space == " "]
    return random.choice(empty_spaces) if empty_spaces else -1

def check_win(board, player):
    win_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)             
    ]
    for line in win_lines:
        if board[line[0]] == board[line[1]] == board[line[2]] == player:
            return True
    return False

def check_tie(board):
    return " " not in board

def play_again():
    """Ask to play again."""
    while True:
        answer = input("Play again? (yes/no): ").lower()
        if answer in ("yes", "no"):
            return answer == "yes"
        else:
            print("Invalid input.")

def main():
    print("Welcome to Tic-Tac-Toe!")
    while True:
        board = [" "] * 9
        player = "X"
        game_over = False
        while not game_over:
            display_board(board)
            if player == "X":
                move = get_player_move(board, player)
                if move == -1:
                    continue
            else:
                move = get_computer_move(board)
                if move == -1:
                    print("Computer error")
                    game_over = True
                    break
            board[move] = player
            if check_win(board, player) or check_tie(board):
                display_board(board)
                print(f"Player {player} wins!" if check_win(board, player) else "It's a tie!")
                game_over = True
            player = "O" if player == "X" else "X"
        if not play_again():
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
