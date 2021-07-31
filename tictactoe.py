# GLOBAL VARIABLES

# if game is still going on :
game_still_going = True

# who's the player?
current_player = "X"

# winner?
winner = None

# GAME BOARD
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


# DISPLAY THE BOARD
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# STARTING THE GAME
def play_game():
    # displays the board
    display_board()

    # if the game is still going on?
    while game_still_going:
        # handles a single turn of a player
        handle_turn(current_player)

        # checks is game is over
        check_if_game_over()

        # flips to another player
        flip_player()

    # after the game has ended :
    # check for winner or tie :
    if winner == "X" or winner == "O":
        print("Player " + winner + " won the game.")

    elif winner == None:
        print(" --- Game's a Tie. --- ")



# PLAYER's TURN
def handle_turn(player):
    print(player + "'s Turn.")
    position = input("Choose a position from 1-9 : ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9 : ")

        position = int(position) - 1      # --> converts your input into integer format and deducts 1 since your list's index starts from 0
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go Again.")

    board[position] = player

    display_board()


def check_if_game_over():
    check_game_winner()
    check_if_tie()


def check_game_winner():
    global winner  # --> set a global variable
    # check rows
    winner_rows = check_rows()
    # check column
    winner_cols = check_cols()
    # check diagonals
    winner_dia = check_dia()

    if winner_rows:
        winner = winner_rows
    elif winner_cols:
        winner = winner_cols
    elif winner_dia:
        winner = winner_dia
    else:
        winner = None

    return


def check_rows():
    # set up a global variable
    global game_still_going

    # check if any rows have same value and is not empty
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    # if any row does have a match, flag that there is a win
    if row1 or row2 or row3:
        game_still_going = False

    # return the winner X or O
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]

    return


def check_cols():
    # set up a global variable
    global game_still_going

    # check if any columns have same value and is not empty
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    # if any column does have a match, flag that there is a win
    if col1 or col2 or col3:
        game_still_going = False

    # return the winner X or O
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]

    return


def check_dia():
    # set up a global variable
    global game_still_going

    # check if any diagonals have same value and is not empty
    dia1 = board[0] == board[4] == board[8] != "-"
    dia2 = board[2] == board[4] == board[6] != "-"

    # if any diagonal does have a match, flag that there is a win
    if dia1 or dia2:
        game_still_going = False

    # return the winner X or O
    if dia1:
        return board[0]
    elif dia2:
        return board[2]

    return


def check_if_tie():
    global game_still_going

    if "-" not in board:
        game_still_going = False

    return


def flip_player():
    global current_player
    # if current player is X, change it to O
    if current_player == "X":
        current_player = "O"
        # if current player is O, change it to X
    elif current_player == "O":
        current_player = "X"
    return


play_game()




# create a board
# display the board
# play game
# handle turn
# check winner
# check row
# check column
# check diagonal
# check tie
# flip player
