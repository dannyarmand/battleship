from random import randint

board = []

for x in range(0,5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)

def random_row(board):
    return randint(0, len(board [0]) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

print(ship_row)
print(ship_col)

guesses = 0
while guesses <4:
        
    guess_row = int(input('Guess Row: '))
    guess_col = int(input('Guess Column: '))


    #This checks if you have guessed correctly
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break

    #This checks if you have guessed within the board
    if guess_row not in range(5) or guess_col not in range(5):
        print("Oops! That's not even in the ocean")

    #This checks if you have guessed already
    elif board[guess_row][guess_col] == 'X':
        print("You guessed that one already!")

    #This checks if you missed the ship and it marks it with an X
    else:
        print("You missed my battleship!")
        board[guess_row][guess_col] = 'X'
        print_board(board)
        guesses = guesses + 1
            if guesses == 4
                print("Game is over, you have run out of turns!")

   

