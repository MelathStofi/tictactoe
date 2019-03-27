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


'''def isThereAWinner(gameBoard):
    winner = False
    if gameBoard[0] == "X" and gameBoard[1] == "X" and gameBoard[2] == "X":
        return True
    if gameBoard[3] == "X" and gameBoard[4] == "X" and gameBoard[5] == "X":
        return True
    if gameBoard[6] == "X" and gameBoard[7] == "X" and gameBoard[8] == "X":
        return True
    if gameBoard[0] == "X" and gameBoard[3] == "X" and gameBoard[6] == "X":
        return True
    if gameBoard[1] == "X" and gameBoard[4] == "X" and gameBoard[7] == "X":
        return True
    if gameBoard[2] == "X" and gameBoard[5] == "X" and gameBoard[8] == "X":
        return True
    if gameBoard[0] == "X" and gameBoard[4] == "X" and gameBoard[8] == "X":
        return True
    if gameBoard[2] == "X" and gameBoard[4] == "X" and gameBoard[6] == "X":
        return True

    if gameBoard[0] == "O" and gameBoard[1] == "O" and gameBoard[2] == "O":
        return True
    if gameBoard[3] == "O" and gameBoard[4] == "O" and gameBoard[5] == "O":
        return True
    if gameBoard[6] == "O" and gameBoard[7] == "O" and gameBoard[8] == "O":
        return True
    if gameBoard[0] == "O" and gameBoard[3] == "O" and gameBoard[6] == "O":
        return True
    if gameBoard[1] == "O" and gameBoard[4] == "O" and gameBoard[7] == "O":
        return True
    if gameBoard[2] == "O" and gameBoard[5] == "O" and gameBoard[8] == "O":
        return True
    if gameBoard[0] == "O" and gameBoard[4] == "O" and gameBoard[8] == "O":
        return True
    if gameBoard[2] == "O" and gameBoard[4] == "O" and gameBoard[6] == "O":
        return True'''


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

        if play_again(work_time) is True:
            work_time = True
        else:
            work_time = False
            break


main()
