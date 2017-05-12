import os
from time import sleep
import random
from random import randint
from random import randrange
from functions import *


def main():

    width = 200
    height = 50

    reserve_players = []
    starting_11 = []
    reserved_sign = ["#", '\033[92m' + '#' + '\33[37m','\033[94m' + '#' + '\33[37m', '\033[93m' + '#' + '\33[37m',
    '\033[95m' + '#' + '\33[37m','\033[96m' + '#' + '\33[37m', "@"]

######################################## fasol
    level = 1
    boss_overall = 60
########################################
    intro(load_file_as_list('ascii_intro.txt', 'break'), 10)

    while level < 5:
        change_board = False
        horizontal_pos  = 2
        vertical_pos = height//2
        board = create_first_board(width, height, ' ')
        board_with_buildings = create_random_amount_of_buildings(board, reserved_sign, level) # added buildings to map
        board = board_with_buildings
        # creating lists of x,y coordinates for footballers generating
        xx, yy, positions_list, tiers_list = amount_of_footballers(board, height)
        last_level = level


        while not change_board:
            print()

            pressed_key = getch()

            os.system('clear')


            old_horizontal = horizontal_pos
            old_vertical = vertical_pos
            if pressed_key in ['w','a','s','d']:
                horizontal_pos, vertical_pos = hero_walking(pressed_key, board, horizontal_pos, vertical_pos, reserved_sign)
            elif pressed_key == 'x':
                exit()


    #-----------------------------------------------------------------------
            elif pressed_key == 'i':
                level, boss_overall = inventory_main_view(starting_11, reserve_players, pressed_key, level, boss_overall)
                clear_board_statistics(board)
    #---------------------------------------------------------------------------------------
            insert_player(board, horizontal_pos, vertical_pos, old_horizontal, old_vertical)

            generate_footballers(xx, yy, board, positions_list, tiers_list)
            horizontal_pos = generate_question(board,vertical_pos, horizontal_pos, reserve_players,starting_11)

            insert_reserve_players_amount(board,reserve_players)
            insert_squad_into_board(board,starting_11,'STARTING 11', 5)
            insert_string_into_board('LEVEL: ' + str(level), board, 45, 155)
            insert_string_into_board('BOSS OVERALL: ' + str(boss_overall), board, 46, 155)

            print_board(board)

            if last_level != level:
                change_board = True
                os.system("clear")
                for i in range(randint(3,5)):
                    starting_11.remove(random.choice(starting_11))
    print_you_won()
    # end game

main()
