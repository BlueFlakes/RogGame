
import os
from time import sleep
from random import randint
import random


class colors:
    SILVER = '\033[90m'
    GOLD = '\033[93m'
    ELITE = '\033[91m'
    END = '\x1b[0m'


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
        sleep(0.2)
    print("Welcome to the Final Fantasy Football Game!")
    sleep(1)


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


def insert_footballer(footballer_x, footballer_y, board, position, tier):
    """
    position = att, mid , deff or gk
    tier: silver = 0
          gold   = 1
          elite  = 2


    """
    #silver, gold, red, end
    colors = ['\033[90m', '\033[93m', '\033[91m', '\x1b[0m']
    x = footballer_x
    y = footballer_y 

    if position == 'att':
        board[y][x] = str(colors[tier]) + 'Ⓐ' + str(colors[3])
    elif position == 'mid':
        board[y][x] = str(colors[tier]) + 'Ⓜ' + str(colors[3])
    elif position == 'deff':
        board[y][x] = str(colors[tier]) + 'Ⓓ' + str(colors[3])
    elif position == 'gk':
        board[y][x] = str(colors[tier]) + 'Ⓖ' + str(colors[3])

    return colors


def generate_footballers(xx, yy, board, positions_list, tiers_list, total_number):
    """
    inserts footballers in random position which is taken from xx and yy lists and their 
    look depends on position and tier, imported from parameters
    """
    for i in range(1, total_number):
        insert_footballer(xx[i], yy[i], board, positions_list[i], tiers_list[i])
    return board


def ask_question(difficulty, easy_questions, medium_questions, hard_questions, easy_answers, medium_answers, hard_answers):
        """ 
        difficulty: easy, medium or hard
        """
        if difficulty == 'easy':
            random_digit = randint(0,len(easy_questions) - 1)
            answer = input(easy_questions[random_digit])
            if answer == easy_answers[random_digit]:
                sleep(2) # dodac warunek co w przypadku zwyciestwa

        if difficulty == 'medium':
            random_digit = randint(0,len(medium_questions) - 1)
            answer = input(medium_questions[random_digit])
            if answer == medium_answers[random_digit]:
                sleep(2) # dodac warunek co w przypadku zwyciestwa

        if difficulty == 'hard':
            random_digit = randint(0,len(hard_questions) - 1)
            answer = input(hard_questions[random_digit])
            if answer == hard_answers[random_digit]:
                sleep(2) # dodac warunek co w przypadku zwyciestwa


def generate_question(board,vertical_pos, horizontal_pos):
    """

    """
    easy_questions = ['easy question1', 'easy question2', 'easy question3']
    medium_questions = ['medium question1', 'medium question2', 'medium question3']
    hard_questions = ['hard question1', 'hard question2', 'hard question3']

    easy_answers = ['answer1', 'answer2', 'answer3']
    medium_answers = ['answer1', 'answer2', 'answer3']
    hard_answers = ['answer1', 'answer2', 'answer3']
    if (board[vertical_pos][horizontal_pos] == (colors.SILVER + 'Ⓐ' + colors.END) 
        or board[vertical_pos][horizontal_pos] == (colors.SILVER + 'Ⓜ' + colors.END) 
        or board[vertical_pos][horizontal_pos] == (colors.SILVER + 'Ⓓ' + colors.END) 
        or board[vertical_pos][horizontal_pos] == (colors.SILVER + 'Ⓖ' + colors.END)
        ):
        ask_question('easy', easy_questions, medium_questions, hard_questions, 
                        easy_answers, medium_answers, hard_answers)
        horizontal_pos += 1

    if (board[vertical_pos][horizontal_pos] == (colors.GOLD + 'Ⓐ' + colors.END) 
        or board[vertical_pos][horizontal_pos] == (colors.GOLD + 'Ⓜ' + colors.END) 
        or board[vertical_pos][horizontal_pos] == (colors.GOLD + 'Ⓓ' + colors.END) 
        or board[vertical_pos][horizontal_pos] == (colors.GOLD + 'Ⓖ' + colors.END)
        ):
        ask_question('medium', easy_questions, medium_questions, hard_questions, 
                        easy_answers, medium_answers, hard_answers)
        horizontal_pos += 1

    if (board[vertical_pos][horizontal_pos] == (colors.ELITE + 'Ⓐ' + colors.END) 
        or board[vertical_pos][horizontal_pos] == (colors.ELITE + 'Ⓜ' + colors.END) 
        or board[vertical_pos][horizontal_pos] == (colors.ELITE + 'Ⓓ' + colors.END) 
        or board[vertical_pos][horizontal_pos] == (colors.ELITE + 'Ⓖ' + colors.END)
        ):
        ask_question('hard', easy_questions, medium_questions, hard_questions, 
                        easy_answers, medium_answers, hard_answers)
        horizontal_pos += 1

    return horizontal_pos


def main():
 #   show_welcome()
    width = 130
    height = 40

    player_move_counter = 0

    horizontal_pos  = width//2
    vertical_pos = height//2

    board = create_board(width, height, ' ')

    # creating lists of x,y coordinates for footballers generating
    xx = []
    yy = []
    positions = ['att', 'mid', 'def', 'gk']
    tiers = [0, 1, 2]
    positions_list = []
    tiers_list = []

    for i in range(100):
        xx.append(randint(1, width-1))
        yy.append(randint(1, height-1))
        positions_list.append(random.choice(positions))
        tiers_list.append(random.choice(tiers))


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

        generate_footballers(xx, yy, board, positions_list, tiers_list, 35)
        horizontal_pos = generate_question(board,vertical_pos, horizontal_pos)

        print_board(board)
        print(vertical_pos, horizontal_pos)
        print(board[vertical_pos][horizontal_pos])
main()
