import os
from time import sleep
from random import randint


def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def create_board(width, height, sign):
    board = []
    for row in range(height):
        item_in_row = []

        for column in range(width):
            if row == 0 or row == (height - 1):
                item_in_row.append("#")
            else:
                if column == 0 or column == (width - 1):
                    item_in_row.append("#")
                else:
                    item_in_row.append(sign)
        board.append(item_in_row)
    return board


def print_board(board):
    for row in board:
        for column in row:
            print(column, end = '')
        print()

def insert_player(board, pos_x, pos_y ):
    board[pos_y][pos_x] = '@'
    return board


def main():
    width = 130
    height = 40

    horizontal  = width//2
    vertical = height//2
    while True:
        pressed_key = getch()
        board = create_board(width, height, ' ')
        os.system('clear')
        if board[vertical][horizontal] != '#':
            old_vertical  = vertical
            old_horizontal = horizontal
            if pressed_key == 'd':
                horizontal += 1
                insert_player(board, horizontal, vertical)
                print_board(board)
            elif pressed_key == 'a':
                horizontal -= 1
                insert_player(board, horizontal, vertical)
                print_board(board)
            elif pressed_key == 's':
                vertical += 1
                insert_player(board, horizontal, vertical)
                print_board(board)
            elif pressed_key == 'w':
                vertical -= 1
                insert_player(board, horizontal, vertical)
                print_board(board)
            elif pressed_key == 'x':
                quit()
            elif pressed_key == 'i': #calling inventory
                pass
        else:
            horizontal  = old_horizontal
            vertical = old_vertical
            insert_player(board, horizontal, vertical)
            print_board(board)

main()

