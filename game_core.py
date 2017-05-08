import os
from time import sleep
from random import randint


def getch():
    import sys, tty, termios
    from select import select
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        [i, o, e] = select([sys.stdin.fileno()], [], [], 0.35)
        if i: ch=sys.stdin.read(1)
        else: ch=''
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
    print("Welcome to the Final Fantasy Football Game!")
    sleep(3)


def hero_walking(pressed_key, board, h_position, v_position):

    if pressed_key == 'd' and board[v_position][h_position +1] != '#':
        h_position += 1
    elif pressed_key == 'a' and board[v_position][h_position -1] != '#':
        h_position -= 1
    elif pressed_key == 's' and board[v_position +1][h_position] != '#':
        v_position += 1
    elif pressed_key == 'w' and board[v_position -1][h_position] != '#':
        v_position -= 1

    return h_position, v_position

def insert_monster(board):

    x = randint(8, 10)
    y = randint(8, 10)


    board[y][x] = "/"
    board[y][x + 1] = "\\"
    board[y][x+3] = "/"
    board[y][x+4] = "\\"
    board[y-1][x+3] = "_"
    board[y-1][x+2] = "_"
    board[y-1][x+1] = "_"
    board[y-1][x] = "^"
    return board


def main():
    show_welcome()
    width = 130
    height = 40

    player_move_counter = 0

    horizontal_pos  = width//2
    vertical_pos = height//2

    board = create_board(width, height, ' ')
    insert_player(board, horizontal_pos, vertical_pos)

    while True:
        pressed_key = getch()
        board = create_board(width, height, ' ')
        os.system('clear')

        if pressed_key in ['w','a','s','d']:
            horizontal_pos, vertical_pos = hero_walking(pressed_key, board, horizontal_pos, vertical_pos)
        elif pressed_key == 'x':
            exit()
        player = insert_player(board, horizontal_pos, vertical_pos)


        monster = insert_monster(board)



        for game_element in [player, monster]:  # tutaj sumujesz do boarda dodatkowe elementy
            board = game_element                # aby razem zostały wyświetlone


        print_board(board)

main()
