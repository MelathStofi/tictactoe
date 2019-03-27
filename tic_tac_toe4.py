import os
import random


def boardOutput(game_board):
    os.system("clear")
    print('\n-------------------')
    print('|     |     |     |')
    print('|  ' + game_board[0] + '  |  ' + game_board[1] + '  |  ' + game_board[2] + '  |  ')
    print('|     |     |     |')
    print('|-----------------|')
    print('|     |     |     |')
    print('|  ' + game_board[3] + '  |  ' + game_board[4] + '  |  ' + game_board[5] + '  |  ')
    print('|     |     |     |')
    print('|-----------------|')
    print('|     |     |     |')
    print('|  ' + game_board[6] + '  |  ' + game_board[7] + '  |  ' + game_board[8] + '  |  ')
    print('|     |     |     |')
    print('-------------------\n')


def playAgain():
    if isThereAWinner or isTableFull is True:
        user_input = ""
        while user_input != "y" and user_input != "yes" and user_input != "n" and user_input != "no":
            user_input = input("Play again? (yes or no): ")
            if user_input == "yes":
                return True
            else:
                return False

def isSpaceEmpty(game_board, position):
    return (game_board[position] != "X") and (game_board[position] != "O")


def selectPlayerControl():
    symbol = ""
    while symbol != "X" and symbol != "O" and symbol != "x" and symbol != "o":
        player_input = input("\nEnter 'X' or 'O': ")
        if player_input == "x" or player_input == "X":
            symbol = "X"
        elif player_input == "o" or player_input == "O":
            symbol = "O"
    return symbol


def isTableFull(game_board):
    if game_board.count("X") + game_board.count("O") == 9:
        return True
    else:
        return False


def isThereAWinner(gameBoard):
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
        return True


def play_again(play):
    answer = input("Would you like to play an other one?(y/n):")
    if answer == "y" or answer == "Y":
        return True
    else:
        return False


def main():
    board = [" "] * 9
    work_time = True
    while work_time:

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

        boardOutput(board)

        player = 0
        while True:
            move = -1
            while (move < 0 or move > 8):
                move = int(input("\nPlayer" + str(player + 1) + "! Place \"" + player_control[player] + "\" to grid: ")) - 1


            if isSpaceEmpty(board, move):
                board[move] = player_control[player]
                boardOutput(board)
                if player == 0:
                    player = 1
                else:
                    player = 0

                    boardOutput(board)

            else:
                print("Space " + str(move + 1) + " is occupied!\n")

            if (isTableFull(board)) and (not(isThereAWinner(board))):
                print("It's a tie")
                break    

            if isThereAWinner(board):
                if player == 0:
                    player = 1
                else:
                    player = 0
                print("Winner is the player with symbol: " + str(player_control[player]) + ("\n" * 4))
                break

        if play_again(work_time) is True:
            board = [" "] * 9
            work_time = True
        else:
            work_time = False
            break


main()
