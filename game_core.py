import os
from time import sleep

import random
from random import randint
from random import randrange



class colors:
    SILVER = '\033[90m'
    GOLD = '\033[93m'
    ELITE = '\033[91m'
    END = '\x1b[0m'


reserved_sign = ["#", '\033[92m' + '#' + '\33[37m', "@"]


'''
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
'''
def load_footballer(position, tier):
    """
    position: att, mid, deff, gk
    tier: SILVER, GOLD, ELITE
    """
    with open ('footballers.csv', 'r') as file:
        footballers_temp = file.readlines()

    footballers = []
    for line in footballers_temp:
        line = line.rstrip()
        line = line.split(',')
        footballers.append(line)

    footballers_to_pick = []
    for player in footballers:
        if player[1] == position and player[2] == tier:
            footballers_to_pick.append(player)
    loaded_footballer = random.choice(footballers_to_pick)

    if tier == 'SILVER':
        loaded_footballer.append(randint(55,70))
    elif tier == 'GOLD':
        loaded_footballer.append(randint(70,85))
    elif tier == 'ELITE':
        loaded_footballer.append(randint(85,99))

    return loaded_footballer

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


def create_first_board(width, height, sign):
    board = []
    for row in range(height):
        item_in_row = []

        for column in range(width-1):
            if row == 0 or row == (height - 1):
                item_in_row.append("#")
            else:
                if column == 0 or column == 150 or column == 178:
                    item_in_row.append("#")
                else:
                    item_in_row.append(sign)
        board.append(item_in_row)

    return board


def create_inventory_board(width, height):
    inventory_board = []

    for row in range(height):
        temporary_storage = []

        for column in range(width):
            temporary_storage.append(".")

        inventory_board.append(temporary_storage)

    return inventory_board

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
        random_pos_x = randint(0, 142 - building_range)
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
        sleep(0.2)
    print("Welcome to the Final Fantasy Football Game!")
    sleep(1)



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


def generate_footballers(xx, yy, board, positions_list, tiers_list):
    """
    inserts footballers in random position which is taken from xx and yy lists and their
    look depends on position and tier, imported from parameters
    """
    for i in range(len(xx)):
        insert_footballer(xx[i], yy[i], board, positions_list[i], tiers_list[i])
    return board



def load_data(filename):
    with open (filename, 'r') as file:
            content = file.readlines()
    return content


def ask_question(difficulty, position, easy_questions, medium_questions, hard_questions, easy_answers, medium_answers, hard_answers, reserve_players):

        """
        difficulty: easy, medium or hard
        """
        if difficulty == 'easy':
            random_digit = randint(0,len(easy_questions) - 1)
            print("If you answer this question, you get random SILVER player!" + "\n" + "If you fail, you will loose precious TIME!" + "\n")


            answer = input(easy_questions[random_digit])

            if answer == easy_answers[random_digit].lower().rstrip():
                dragon_loot.append("LAZAR")
                reserve_players.append(load_footballer(position, 'SILVER'))


        if difficulty == 'medium':
            random_digit = randint(0,len(medium_questions) - 1)
            print("If you answer this question, you get random GOLD player!" + "\n" + "If you fail, you will loose precious TIME!" + "\n")
            print(medium_answers[random_digit]) #CODE
            answer = input(medium_questions[random_digit])


            if answer == medium_answers[random_digit].lower().rstrip():
                reserve_players.append(load_footballer(position, 'GOLD'))


        if difficulty == 'hard':
            random_digit = randint(0,len(hard_questions) - 1)
            print("If you answer this question, you get random ELITE player!" + "\n" + "If you fail, you will loose precious TIME!" + "\n")
            print(hard_answers[random_digit]) #CODE
            answer = input(hard_questions[random_digit])


            if answer == hard_answers[random_digit].lower().rstrip():
                reserve_players.append(load_footballer(position, 'ELITE'))



def generate_question(board,vertical_pos, horizontal_pos, reserve_players):

    easy_questions = load_data('easy_questions.csv')
    medium_questions = load_data('medium_questions.csv')
    hard_questions = load_data('hard_questions.csv')
    easy_answers = load_data('easy_answers.csv')
    medium_answers = load_data('medium_answers.csv')
    hard_answers = load_data('hard_answers.csv')


    current_pos = board[vertical_pos][horizontal_pos]
    if current_pos == (colors.SILVER + 'Ⓐ' + colors.END):
        ask_question('easy', 'att', easy_questions, medium_questions, hard_questions,
                        easy_answers, medium_answers, hard_answers, reserve_players)
        horizontal_pos += 1
    elif current_pos == (colors.SILVER + 'Ⓜ' + colors.END):
        ask_question('easy', 'mid', easy_questions, medium_questions, hard_questions,
                        easy_answers, medium_answers, hard_answers, reserve_players)
        horizontal_pos += 1
    elif current_pos == (colors.SILVER + 'Ⓓ' + colors.END):
        ask_question('easy', 'deff', easy_questions, medium_questions, hard_questions,
                        easy_answers, medium_answers, hard_answers, reserve_players)
        horizontal_pos += 1
    elif current_pos == (colors.SILVER + 'Ⓖ' + colors.END):
        ask_question('easy', 'gk', easy_questions, medium_questions, hard_questions,
                        easy_answers, medium_answers, hard_answers, reserve_players)
        horizontal_pos += 1
    elif current_pos == (colors.GOLD + 'Ⓐ' + colors.END):
        ask_question('medium', 'att', easy_questions, medium_questions, hard_questions,
                        easy_answers, medium_answers, hard_answers, reserve_players)
        horizontal_pos += 1
    elif current_pos == (colors.GOLD + 'Ⓜ' + colors.END):
        ask_question('medium', 'mid', easy_questions, medium_questions, hard_questions,
                        easy_answers, medium_answers, hard_answers, reserve_players)
        horizontal_pos += 1
    elif current_pos == (colors.GOLD + 'Ⓓ' + colors.END):
        ask_question('medium', 'deff', easy_questions, medium_questions, hard_questions,
                        easy_answers, medium_answers, hard_answers, reserve_players)
        horizontal_pos += 1
    elif current_pos == (colors.GOLD + 'Ⓖ' + colors.END):
        ask_question('medium', 'gk', easy_questions, medium_questions, hard_questions,
                        easy_answers, medium_answers, hard_answers, reserve_players)
        horizontal_pos += 1
    elif current_pos == (colors.ELITE + 'Ⓐ' + colors.END):
        ask_question('hard', 'att', easy_questions, medium_questions, hard_questions,
                        easy_answers, medium_answers, hard_answers, reserve_players)
        horizontal_pos += 1
    elif current_pos == (colors.ELITE + 'Ⓜ' + colors.END):
        ask_question('hard', 'mid', easy_questions, medium_questions, hard_questions,
                        easy_answers, medium_answers, hard_answers, reserve_players)
        horizontal_pos += 1
    elif current_pos == (colors.ELITE + 'Ⓓ' + colors.END):
        ask_question('hard', 'deff', easy_questions, medium_questions, hard_questions,
                        easy_answers, medium_answers, hard_answers, reserve_players)
        horizontal_pos += 1
    elif current_pos == (colors.ELITE + 'Ⓖ' + colors.END):
        ask_question('hard', 'gk', easy_questions, medium_questions, hard_questions,
                        easy_answers, medium_answers, hard_answers, reserve_players)

        horizontal_pos += 1

    return horizontal_pos


def main():

    width = 180
    height = 50


    dragon_loot = []
    horizontal_pos  = width//2
    vertical_pos = height//2


    board = create_first_board(width, height, ' ')
    board_with_buildings = create_random_amount_of_buildings(board) # added buildings to map
    board = board_with_buildings

    # creating lists of x,y coordinates for footballers generating
    xx = []
    yy = []

    footballers_amount = 0
    positions = ['att', 'mid', 'def', 'gk']
    tiers = [0, 1, 2]
    positions_list = []
    tiers_list = []

    #creating list of our collected players
    reserve_players = []


    while footballers_amount < 30:
        footballer_x = randint(2, 149)
        footballer_y = randint(2, height-2)

        if (board[footballer_y-1][footballer_x] == " " and
            board[footballer_y+1][footballer_x] == " " and
            board[footballer_y][footballer_x-1] == " " and
            board[footballer_y][footballer_x+1] == " "):

            xx.append(footballer_x)
            yy.append(footballer_y)
            positions_list.append(random.choice(positions))
            tiers_list.append(random.choice(tiers))

            footballers_amount += 1

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
        elif pressed_key == 'i':


            while True:
                print(dragon_loot)
                sleep(1)
                pressed_key = getch()
                os.system('clear')

                inventory_board = create_inventory_board(101, 101)
                inventory_board[5][5] = "x"
                print_board(inventory_board)


                if pressed_key == 'x':
                    exit()


        player = insert_player(board, horizontal_pos, vertical_pos, old_horizontal, old_vertical)



        generate_footballers(xx, yy, board, positions_list, tiers_list)

        horizontal_pos = generate_question(board,vertical_pos, horizontal_pos, reserve_players)



        print_board(board)
        print(reserve_players)


main()
