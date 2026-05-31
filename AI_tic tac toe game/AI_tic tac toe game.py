import random

board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False

for turn in range(9):

    print_board()

    if turn % 2 == 0:  # Human Player X
        move = int(input("Choose position (1-9): ")) - 1

        while move < 0 or move > 8 or board[move] != " ":
            move = int(input("Invalid position! Choose again: ")) - 1

    else:  # AI Player O
        print("AI is making a move...")
        empty = [i for i in range(9) if board[i] == " "]
        move = random.choice(empty)

    board[move] = "X" if turn % 2 == 0 else "O"

    if check_winner("X"):
        print_board()
        print("You win!")
        break

    if check_winner("O"):
        print_board()
        print("AI wins!")
        break

else:
    print_board()
    print("It's a draw!")

input("Press Enter to exit...")