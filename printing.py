import sys
import os

introduction_screen = 'intro screen'
character_creation_screen = 'character_creation_screen'
how_to_play_screen = 'how_to_play_screen'
lose_screen = 'lose screen'
win_screen = 'win_screen'


def print_screen(screen):
    os.system('clear')
    print(screen)
    input('Press enter to continue: ')


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
