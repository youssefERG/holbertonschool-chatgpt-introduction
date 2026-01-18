#!/usr/bin/python3
"""
Tic Tac Toe Game
A two-player game where players alternate placing X and O on a 3x3 board.
First player to get three in a row wins.
"""

def print_board(board):
    """
    Display the current state of the board.

    Parameters:
        board (list): 3x3 grid representing the game board.

    Returns:
        None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """
    Check if there is a winner on the board.

    Checks rows, columns, and diagonals for three matching non-empty symbols.

    Parameters:
        board (list): 3x3 grid representing the game board.

    Returns:
        bool: True if there is a winner, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def is_board_full(board):
    """
    Check if the board is completely filled.

    Parameters:
        board (list): 3x3 grid representing the game board.

    Returns:
        bool: True if board is full, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True


def get_valid_move(board, player):
    """
    Prompt player for a valid move with input validation.

    Keeps asking until user enters valid coordinates (0-2)
    and the cell is not already occupied.

    Parameters:
        board (list): 3x3 grid representing the game board.
        player (str): Current player ("X" or "O").

    Returns:
        tuple: (row, col) of the valid move.
    """
    while True:
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            # Validate coordinates are in range
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Error: Row and column must be between 0 and 2. Try again.")
                continue

            # Check if cell is empty
            if board[row][col] == " ":
                return row, col
            else:
                print("That spot is already taken! Try again.")

        except ValueError:
            print("Error: Invalid input. Please enter numbers only (0, 1, or 2).")


def tic_tac_toe():
    """
    Main game loop for Tic Tac Toe.

    Alternates between two players until there is a winner or tie.

    Returns:
        None
    """
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    print("Welcome to Tic Tac Toe!")
    print("Players will alternate placing X and O.")
    print("First to get three in a row wins!\n")

    while True:
        print_board(board)

        # Get valid move from current player
        row, col = get_valid_move(board, player)
        board[row][col] = player

        # Check for winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check for tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()