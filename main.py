# Tic-Tac-Toe Game in Python

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)


# Function to check if any player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


# Function to check if the board is full (draw)
def is_board_full(board):
    return all([cell != " " for row in board for cell in row])


# Function to play the game
def play_game():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # X goes first

    while True:
        print_board(board)

        # Get the player's move
        try:
            row = int(input(f"Player {current_player}, enter the row (1-3): ")) - 1
            col = int(input(f"Player {current_player}, enter the column (1-3): ")) - 1
        except ValueError:
            print("Please enter a valid number!")
            continue

        # Check if the move is valid
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Invalid move. Try again.")
            continue

        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check if it's a draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()
