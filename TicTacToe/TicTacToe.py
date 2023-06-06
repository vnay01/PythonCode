
""" Python code to learn about use of dictionaries"""

## This code 'models' a game of Tic-Tac-Toe
## Represents a clear board

Board= {'top-L':' ', 'top-M':' ', 'top-R': ' ',
        'mid-L':' ', 'mid-M':' ', 'mid-R': ' ',
        'low-L':' ', 'low-M':' ', 'low-R': ' '}

## define a function which prints a clear board

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    print('-+-+-')        




### To play the game, we need to prompt the users

turn = 'X'

for i in range(9):
    printBoard(Board)
    print('Turn for '+ turn + ' .Move on which space?')
    # capture the location on which to place the symbol
    move = input()
    Board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(Board)