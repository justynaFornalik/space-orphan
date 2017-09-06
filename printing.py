import sys
import os


from constants import *


introduction_screen = 'intro screen'
character_creation_screen = 'character_creation_screen'
how_to_play_screen = 'how_to_play_screen'
lose_screen = 'lose screen'
win_screen = 'win_screen'


def print_board(board, player_row, player_col):
    os.system('clear')
    for i, sublist in enumerate(board):
        for n, char in enumerate(sublist):
            if player_row == i and player_col == n:
                print('\033[1;37;49m' + PLAYER, end='')
            else:
                if char == WALL:
                    print('\033[1;34;49m' + char, end='')
                elif char == LAVA:
                    print('\033[1;31;49m' + char, end='')
                elif char == TREE:
                    print('\033[1;32;49m' + char, end='')
                elif char in MONSTERS:
                    print('\033[1;33;49m' + char, end='')
                elif char in ITEMS:
                    print('\033[1;36;49m' + char, end='')
                else:
                    print('\033[1;35;49m' + char, end='')
        print('\033[1;37;49m')


def print_screen(screen):
    os.system('clear')
    print(screen)
    input('Press enter to continue: ')


def print_starting_screens():
    print('\033[1;37;49m')
    print_screen(introduction_screen)
    print_screen(character_creation_screen)
    print_screen(how_to_play_screen)


def highscores():
    pass


def print_hall_of_fame_screen():
    os.system('clear')
    print('hall_of_fame_screen')


def print_info_about_authors():
    os.system('clear')
    print('info about authors')
    input("Press enter to end game: ")
    os.system('clear')
    sys.exit()
