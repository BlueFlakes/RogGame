import os
from time import sleep
from random import randint
from random import randrange

reserved_sign = ["#", '\033[92m' + '#' + '\33[37m', "@"]

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


def create_first_board(width, height, sign):
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

def create_building(box_range, board, pos_x=0, pos_y=0):

    for x in range(0, box_range):
        for y in range(0, box_range):
            if x == 0 or x == (box_range - 1):    # because func range count from 0 not from 1
                board[x + pos_x][y + pos_y] = reserved_sign[1]
            else:
                if y == 0 or y == box_range - 1:
                    board[x + pos_x][y + pos_y] = reserved_sign[1]
                else:
                    board[x + pos_x][y + pos_y] = '\033[30m' + '.' + '\33[37m'
    return board


def create_random_amount_of_buildings(board):
    for buildings in range(501):
        safe = True
        building_range = randrange(5, 12, 2)
        counter_errors = 0
        random_pos_x = randint(0, 122 - building_range)
        random_pos_y = randint(0, 42 - building_range)

        for x in range(building_range+2):

            if board[x+int(building_range/2)+random_pos_y][int(building_range/2)+random_pos_x] in reserved_sign:
                counter_errors += 1
            if board[int(building_range/2)+random_pos_y][x+int(building_range/2)+random_pos_x] in reserved_sign:
                counter_errors += 1
            if board[-x+int(building_range/2)+random_pos_y][int(building_range/2)+random_pos_x] in reserved_sign:
                counter_errors += 1
            if board[int(building_range/2)+random_pos_y][-x+int(building_range/2)+random_pos_x] in reserved_sign:
                counter_errors += 1
            if board[x+int(building_range/2)+random_pos_y][x+int(building_range/2)+random_pos_x] in reserved_sign:
                counter_errors += 1
            if board[-x+int(building_range/2)+random_pos_y][x+int(building_range/2)+random_pos_x] in reserved_sign:
                counter_errors += 1
            if board[-x+int(building_range/2)+random_pos_y][-x+int(building_range/2)+random_pos_x] in reserved_sign:
                counter_errors += 1
            if board[x+int(building_range/2)+random_pos_y][-x+int(building_range/2)+random_pos_x] in reserved_sign:
                counter_errors += 1

            if x == (building_range +1):

                for y in range(1, int((building_range+1)/2)+1):
                    if board[x+int(building_range/2)+random_pos_y][y+int(building_range/2)+random_pos_x] in reserved_sign:
                        counter_errors += 1
                    if board[x+int(building_range/2)+random_pos_y][-y+int(building_range/2)+random_pos_x] in reserved_sign:
                        counter_errors += 1
                    if board[-x+int(building_range/2)+random_pos_y][y+int(building_range/2)+random_pos_x] in reserved_sign:
                        counter_errors += 1
                    if board[-x+int(building_range/2)+random_pos_y][-y+int(building_range/2)+random_pos_x] in reserved_sign:
                        counter_errors += 1
                    if board[-y+int(building_range/2)+random_pos_y][x+int(building_range/2)+random_pos_x] in reserved_sign:
                        counter_errors += 1
                    if board[y+int(building_range/2)+random_pos_y][x+int(building_range/2)+random_pos_x] in reserved_sign:
                        counter_errors += 1
                    if board[-y+int(building_range/2)+random_pos_y][-x+int(building_range/2)+random_pos_x] in reserved_sign:
                        counter_errors += 1
                    if board[y+int(building_range/2)+random_pos_y][-x+int(building_range/2)+random_pos_x] in reserved_sign:
                        counter_errors += 1

        if counter_errors != 0:
            safe = False
        else:
            safe = True

        if safe == True:
            board = create_building(building_range, board, random_pos_y, random_pos_x)

    return board



def print_board(board):
    for row in board:
        for column in row:
            print(column, end = '')
        print()

def insert_player(board, pos_x, pos_y, old_h, old_v ):
    board[old_v][old_h] = " "
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

    if pressed_key == 'd' and board[v_position][h_position +1] not in reserved_sign:
        h_position += 1
    elif pressed_key == 'a' and board[v_position][h_position -1] not in reserved_sign:
        h_position -= 1
    elif pressed_key == 's' and board[v_position +1][h_position] not in reserved_sign:
        v_position += 1
    elif pressed_key == 'w' and board[v_position -1][h_position] not in reserved_sign:
        v_position -= 1

    return h_position, v_position


def main():
#    show_welcome()
    width = 130
    height = 50



    horizontal_pos  = width//2
    vertical_pos = height//2

    board = create_first_board(width, height, ' ')
    board_with_buildings = create_random_amount_of_buildings(board) # added buildings to map


    while True:
        print()

        pressed_key = getch()

        os.system('clear')

        board = board_with_buildings

        old_horizontal = horizontal_pos
        old_vertical = vertical_pos
        if pressed_key in ['w','a','s','d']:
            horizontal_pos, vertical_pos = hero_walking(pressed_key, board, horizontal_pos, vertical_pos)
        elif pressed_key == 'x':
            exit()

        player = insert_player(board, horizontal_pos, vertical_pos, old_horizontal, old_vertical)








        print_board(board)

main()
