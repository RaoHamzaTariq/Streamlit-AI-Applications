import random

def display_board(board):
    """Show the Tic-Tac-Toe board."""
    print("-------")
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("-------")
    print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("-------")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")
    print("-------")


def get_empty_spaces(board):
    """Get empty space indices."""
    return [i for i, space in enumerate(board) if space == " "]


def get_player_move(board):
    """Get player's move (1-9), return 0-8."""
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                return move
            else:
                print("Invalid move.")
        except ValueError:
            print("Invalid input.")



def check_win(board, player):
    """Check if player won."""
    win_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)  # Diagonals
    ]
    for line in win_lines:
        if board[line[0]] == board[line[1]] == board[line[2]] == player:
            return True
    return False


def check_tie(board):
    """Check if it's a tie."""
    return " " not in board



def minimax(board, depth, maximizing_player):
    """
    Minimax algorithm:  Find the best move for the AI.

    This version is simplified to be easier to understand.

    Args:
        board: Current board state.
        depth:  How many moves ahead we are looking.
        maximizing_player: True if it's the AI's turn, False if it's the player's turn.

    Returns:
        A dictionary with the score and the best move.
    """
    # Base cases:  Game over situations
    if check_win(board, "X"):  # Human wins
        return {"score": -10, "move": None}
    elif check_win(board, "O"):  # AI wins
        return {"score": 10, "move": None}
    elif check_tie(board):
        return {"score": 0, "move": None}

    # Recursive step:  Try all possible moves
    if maximizing_player:  # AI's turn
        best_score = -float("inf")  # Start with the worst possible score
        best_move = None
        for move in get_empty_spaces(board):
            new_board = list(board)  # Create a copy of the board
            new_board[move] = "O"  # Make the move
            result = minimax(new_board, depth + 1, False)  # Recursively call minimax
            score = result["score"]
            if score > best_score:  # Update if we found a better move
                best_score = score
                best_move = move
        return {"score": best_score, "move": best_move}
    else:  # Player's turn
        best_score = float("inf")  # Start with the worst possible score
        best_move = None
        for move in get_empty_spaces(board):
            new_board = list(board)
            new_board[move] = "X"  # Make the move
            result = minimax(new_board, depth + 1, True)  # Recursive call
            score = result["score"]
            if score < best_score:  # Update if it's a better move for the player
                best_score = score
                best_move = move
        return {"score": best_score, "move": best_move}



def get_ai_move(board):
    """Get the AI's move using minimax."""
    return minimax(board, 0, True)["move"]  # Get the move from the minimax result



def play_again():
    """Ask to play again."""
    while True:
        answer = input("Play again? (yes/no): ").lower()
        if answer in ("yes", "no"):
            return answer == "yes"
        else:
            print("Invalid input.")



def main():
    """Run the game."""
    print("Welcome to Tic-Tac-Toe!")
    while True:
        board = [" "] * 9
        player = "X"
        ai_player = "O"

        # Randomly choose who goes first
        if random.choice([0, 1]) == 0:
            print("You go first!")
        else:
            print("I go first!")
            player = "O"

        game_over = False
        while not game_over:
            display_board(board)
            if player == "X":
                move = get_player_move(board)
            else:
                move = get_ai_move(board)
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
