import os
import random


def select_board_size():
    board_size = int(input("What is your requested board size?: "))
    return board_size


def initialise_board(board_size):
    board = []
    for i in range(board_size):
        board.append([" "] * board_size)
    return board


def board_output(game_board, size):
    os.system("clear")
    dash = '------'
    blank_bar = "     |"

    for row in game_board:
        print("-" + dash * size)
        print("|" + blank_bar * size)
        print("|  " + '  |  '.join(str(elem) for elem in row) + '  |')
        print("|" + blank_bar * size)
    print("-" + dash * size)


def request_player_input(plyr, plyr_ctrl):
    play_input = input("\nPlayer" + str(plyr + 1) + "! Place \"" + plyr_ctrl[plyr] + "\" to grid (x y): ")
    cords = list(play_input.split())
    return cords


def playAgain():
    if isThereAWinner or isTableFull is True:
        user_input = ""
        while user_input != "y" and user_input != "yes" and user_input != "n" and user_input != "no":
            user_input = input("Play again? (yes or no): ")
            if user_input == "yes":
                return True
            else:
                return False


def isSpaceEmpty(game_board, coordinates):
    return (game_board[int(coordinates[0]) - 1][int(coordinates[1]) - 1] != "X") and (game_board[int(coordinates[0]) - 1][int(coordinates[1]) - 1] != "O")


def selectPlayerControl():
    symbol = ""
    while symbol != "X" and symbol != "O" and symbol != "x" and symbol != "o":
        player_input = input("\nEnter 'X' or 'O': ")
        if player_input == "x" or player_input == "X":
            symbol = "X"
        elif player_input == "o" or player_input == "O":
            symbol = "O"
    return symbol


def isTableFull(game_board, size):
    if game_board.count("X") + game_board.count("O") == (size * size):
        return True
    else:
        return False



def is_there_a_winner_with_x(board):

    board_height = len(board)
    board_width = len(board[0])

    #check horizontal
    for y in range(board_height):
        for x in range(board_width - 4):
            if board[x][y] == "X" and board[x+1][y] == "X" and board[x+2][y] == "X" and board[x+3][y] == "X" and board[x+4][y] == "X":
                return True

    # check vertical spaces
    for x in range(board_width):
        for y in range(board_height - 4):
            if board[x][y] == "X" and board[x][y+1] == "X" and board[x][y+2] == "X" and board[x][y+3] == "X" and board[x][y+4] == "X":
                return True

    # check / diagonal spaces
    for x in range(board_width - 4):
        for y in range(4, board_height):
            if board[x][y] == "X" and board[x+1][y-1] == "X" and board[x+2][y-2] == "X" and board[x+3][y-3] == "X" and board[x+4][y-4] == "X":
                return True

    # check \ diagonal spaces
    for x in range(board_width - 4):
        for y in range(board_height - 4):
            if board[x][y] == "X" and board[x+1][y+1] == "X" and board[x+2][y+2] == "X" and board[x+3][y+3] == "X" and board[x+3][y+3] == "X":
                return True
    return False


def is_there_a_winner_with_o(board):

    board_height = len(board)
    board_width = len(board[0])
    #check horizontal
    for y in range(board_height):
        for x in range(board_width - 4):
            if board[x][y] == "O" and board[x+1][y] == "O" and board[x+2][y] == "O" and board[x+3][y] == "O" and board[x+4][y] == "O":
                return True

    # check vertical spaces
    for x in range(board_width):
        for y in range(board_height - 4):
            if board[x][y] == "O" and board[x][y+1] == "O" and board[x][y+2] == "O" and board[x][y+3] == "O" and board[x][y+4] == "O":
                return True

     # check / diagonal spaces
    for x in range(board_width - 4):
        for y in range(4, board_height):
            if board[x][y] == "O" and board[x+1][y-1] == "O" and board[x+2][y-2] == "O" and board[x+3][y-3] == "O" and board[x+4][y-4] == "O":
                return True

    # check \ diagonal spaces
    for x in range(board_width - 4):
        for y in range(board_height - 4):
            if board[x][y] == "O" and board[x+1][y+1] == "O" and board[x+2][y+2] == "O" and board[x+3][y+3] == "O" and board[x+3][y+3] == "O":
                return True
    return False

def play_again(play):
    answer = input("Would you like to play an other one?(y/n):")
    if answer == "y" or answer == "Y":
        return True
    else:
        return False


def main():
    work_time = True
    while work_time:

        board_size = select_board_size()
        current_board = initialise_board(board_size)

        player_control = ["", ""]
        player_control[random.randint(0, 1)] = selectPlayerControl()
        if player_control[0] == "X":
            player_control[1] = "O"
        elif player_control[1] == "X":
            player_control[0] = "O"
        elif player_control[1] == "O":
            player_control[0] = "X"
        elif player_control[1] == "O":
            player_control[0] = "X"
        print("\nPlayer1= " + player_control[0], "\nPlayer2= " + player_control[1])

        board_output(current_board, board_size)
        player = 0
        while True:
            move = request_player_input(player, player_control)

            if isSpaceEmpty(current_board, move):
                current_board[int(move[0]) - 1][int(move[1]) - 1] = player_control[player]
                board_output(current_board, board_size)
                if player == 0:
                    player = 1
                else:
                    player = 0

                    board_output(current_board, board_size)

            else:
                print("Space " + str(move) + " is occupied!\n")

            if (isTableFull(current_board, board_size)):
                '''and (not(isThereAWinner(current_board)))'''
                print("It's a tie")
                break    

            '''if isThereAWinner(current_board):
                if player == 0:
                    player = 1
                else:
                    player = 0
                print("Winner is the player with symbol: " + str(player_control[player]) + ("\n" * 4))
                break'''
            if is_there_a_winner_with_x(current_board) == True and is_there_a_winner_with_o(current_board) == False:
                print("The player with X is the Winner!")
                break

            if is_there_a_winner_with_x(current_board) == False and is_there_a_winner_with_o(current_board) == True:
                print("The player with O is the Winner!")
                break

        if play_again(work_time) is True:
            work_time = True
        else:
            work_time = False
            break


main()
