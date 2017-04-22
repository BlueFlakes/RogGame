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

def show_welcome():

    welcome = [


"""                    __
                 .-'||'-.
               .'   ||   '.             HOCKEY: SUCKS
              /   __||__   \
\\
              | /`-    -`\ |            OCCER: SUCKS
              | | 6    6 | |
              \/\____7___/\/            BASEBALL: SUCKS""",


"""      .--------:\:I:II:I:/;--------.
     /          \`:I::I:`/          \   BASKETBALL: SUCKS
    |            `------'            |
    |             \____/             |  CRICKET: SUCKS""",

"""    |      ,    __     ___    ,      |
    |======|   /  |   / _ \   |======|  RUGBY: SUCKS
    |======|   ^| |  | | | |  |======|
    |~~~~~|     | |  | |_| |   |~~~~~|  CURLING: SUCKS
    |     |\   [___]  \___/   /|     |""",

"""     \    \|                  |/    /
     `\    \  _ _.-=""=-._ _  /    /'
       `\   '`_)\\-++++-//(_`'   /'
         ;   (__||      ||__)   ;       FOOTBALL: DOESN'T SUCK
          ;   ___\      /___   ;
           '. ---/-=..=-\--- .'         ANY QUESTIONS
             `""`        `""`
    """]


    for item in welcome:
        print(item)
        sleep(1)
    print("Welcome in Final Fantasy Football Game!")
    sleep(3)











def main():
    show_welcome()
    width = 130
    height = 40

    h_position  = width//2
    v_position = height//2
    while True:
        pressed_key = getch()
        board = create_board(width, height, ' ')
        os.system('clear')
        old_v_position  = v_position
        old_h_position = h_position
        if pressed_key == 'd' and board[v_position][h_position +1] != '#':
            h_position += 1
            insert_player(board, h_position, v_position)
            print_board(board)
        elif pressed_key == 'a' and board[v_position][h_position -1] != '#':
            h_position -= 1
            insert_player(board, h_position, v_position)
            print_board(board)
        elif pressed_key == 's' and board[v_position +1][h_position] != '#':
            v_position += 1
            insert_player(board, h_position, v_position)
            print_board(board)
        elif pressed_key == 'w' and board[v_position -1][h_position] != '#':
            v_position -= 1
            insert_player(board, h_position, v_position)
            print_board(board)
        elif pressed_key == 'x':
            quit()
        elif pressed_key == 'i': #calling inventory
            pass
        else:
            h_position  = old_h_position
            v_position = old_v_position
            insert_player(board, h_position, v_position)
            print_board(board)


main()
