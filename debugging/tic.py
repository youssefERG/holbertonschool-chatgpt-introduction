def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (len(row) * 4 - 1))  # Adjust horizontal line to board width

def check_winner(board):
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

def is_draw(board):
    # Returns True if all cells are filled and there is no winner
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Invalid input! Row and column must be 0, 1, or 2.")
                continue
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            # Switch player
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

tic_tac_toe()
