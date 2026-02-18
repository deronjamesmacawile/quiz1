# Console Tic-Tac-Toe (Row & Column Index 0-2)

board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

def print_board():
    print("\n  0   1   2")
    for i in range(3):
        print(i, " | ".join(board[i]))
        if i < 2:
            print("  ---------")
    print()

def check_winner():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def check_draw():
    for row in board:
        if " " in row:
            return False
    return True

while True:
    print_board()
    print(f"Player {current_player}'s turn")

    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    if board[row][col] == " ":
        board[row][col] = current_player
    else:
        print("Cell already taken! Try again.")
        continue

    if check_winner():
        print_board()
        print(f"🎉 Player {current_player} wins!")
        break

    if check_draw():
        print_board()
        print("It's a draw!")
        break

    current_player = "O" if current_player == "X" else "X"
