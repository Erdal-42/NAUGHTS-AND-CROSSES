"""
Author: Erdal Koçak
Date: 18.10.2024
Project: NAUGHTS AND CROSSES GAME
Description: This program is a simple implementation of a 3x3 Naughts and Crosses game 
             where two players ('X' and 'O') can take turns to make moves. 
             It checks for horizontal, vertical, and diagonal wins, and validates 
             user input.

Version: 1.0
"""


BOARD_SIZE = 3

def validateInput(input_str):
    """
    Validates the player's input for the game.

    Args:
    input_str (str): The input provided by the player in the form "(row,col)".

    Returns:
    bool: True if the input is valid (within the board dimensions and correctly formatted),
          False otherwise.
    """
    input_str = input_str.strip("()")

    try:
        r, c = map(int, input_str.split(","))
    except ValueError:
        print("Input must be two numbers in format row,col e.g.  1,2")
        return False
    if r < 1 or r > BOARD_SIZE or c < 1 or c > BOARD_SIZE:
        print("Input is a number between 1 and 3 (inclusive)")
    return 0 < r < BOARD_SIZE + 1 and 0 < c < BOARD_SIZE + 1


def disect(move):
    """
    Parses the player's input move and returns the row and column.

    Args:
    move (str): The player's move input in the format "(row,col)".

    Returns:
    tuple: A tuple containing the row and column as integers.
    """
    move = move.strip("()")
    return map(int, move.split(","))
    

def playerValue(player):
    """
    Maps the player ('X' or 'O') to an integer value.

    Args:
    player (str): The player's symbol, either 'X' or 'O'.

    Returns:
    int: 1 for player 'X', 2 for player 'O'.
    """
    if player == 'X':
        return 1
    else:
        return 2


def valuePlayer(value):
    """
    Maps the integer value back to the player symbol.

    Args:
    value (int): The integer representing a player (1 for 'X', 2 for 'O').

    Returns:
    str: The player symbol ('X' or 'O') or an empty space (' ') if value is 0.
    """
    return {1: 'X', 2: 'O'}.get(value, ' ')


def drawBoard(board):
    """
    Draws the current state of the board.

    Args:
    board (list of lists): A 2D list representing the board's current state.
    """
    horizontal_line = " ---" * len(board[0])
    vertical_line = "|"
    for j in range(len(board)):
        print(horizontal_line)
        print(vertical_line, end='')
        for i in range(len(board[0])):
            print(' ' + valuePlayer(board[j][i]) + ' ' + vertical_line, end='')
        print()
    print(horizontal_line)


def lineCheck(list_, r, c):
    """
    Checks for a winning line (horizontal or vertical) based on the last move.

    Args:
    list_ (list of lists): The current state of the game board.
    r (int): The row of the last move.
    c (int): The column of the last move.

    Returns:
    int: The value of the winning player (1 for 'X', 2 for 'O'), or 0 if no winner.
    """
    # Horizontal Check.
    if len(set(list_[r-1])) == 1:
        return  list_[r-1][0]
    # Vertical Check.
    if (list_[0][c-1] and list_[0][c-1] == list_[1][c-1] == list_[2][c-1]):
        return  list_[0][c-1]
    return 0


def diagonalCheck(list_, r, c):
    """
    Checks for a winning diagonal based on the last move.

    Args:
    list_ (list of lists): The current state of the game board.
    r (int): The row of the last move.
    c (int): The column of the last move.

    Returns:
    int: The value of the winning player (1 for 'X', 2 for 'O'), or 0 if no winner.
    """
    if (r == c) or (r - c == 2) or (c-r == 2): 
        if (list_[0][0] == list_[1][1] == list_[2][2]) and list_[1][1]:
            return  list_[1][1]
        if (list_[2][0] == list_[1][1] == list_[0][2]) and list_[1][1]:
            return  list_[1][1]
    return 0


def checkForWinner(board, r, c):
    """
    Checks if there is a winner on the board after the last move.

    Args:
    board (list of lists): The current state of the game board.
    r (int): The row of the last move.
    c (int): The column of the last move.

    Returns:
    int: The value of the winning player (1 for 'X', 2 for 'O'), or 0 if no winner.
    """
    result = lineCheck(board, r, c) or diagonalCheck(board, r, c)
    if result:
        drawBoard(board)
        print("The winner is: ", valuePlayer(result))
    return result


def main():
    """
    The main function to start and run the game.
    Handles game flow, player moves, and board display.
    """
    player = ''
    while True:
        end = "draw"
        print("\nNAUGHTS AND CROSSES")
        print("\nNEW GAME")
        board = [[0,0,0],[0,0,0],[0,0,0]]
        drawBoard(board)
        no_of_cells = len(board) * len(board[0])
        for i in range(no_of_cells):
            player = '0' if i%2 else 'X'
            while True:
                move = input("Player " + player + " make a valid move(row,column): ")
                if validateInput(move) == False:
                    continue
                r, c = disect(move)
                if board[r-1][c-1] == 0:
                    board[r-1][c-1] = playerValue(player)
                    drawBoard(board)
                    break
                print("That cell is occupied.")
            if i > 3:
                if checkForWinner(board, r, c):
                    end = "win"
                    break
        if end == "draw":
            print("No winner.")
        while True:
            input_ = input("Would you like to play again (y/n)?").lower()
            if input_ == "n":
                print("Thanks for playing. Bye.")
                return
            if input_ in ["y"]:
                break


if  __name__=="__main__":
    main()
