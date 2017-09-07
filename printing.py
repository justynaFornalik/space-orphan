import sys
import os


from constants import WALL, LAVA, TREE, MONSTERS, ITEMS


def read_screen(file_name):
    with open(file_name) as file:
        contents = file.read()
    return contents


def print_board(board, player, player_row, player_col, health_points, experience_points):
    os.system('clear')
    for i, sublist in enumerate(board):
        for n, char in enumerate(sublist):
            if player_row == i and player_col == n:
                print('\033[1;37;49m' + player, end='')
            else:
                if char == WALL:
                    print('\033[1;34;49m' + char, end='')
                elif char == LAVA:
                    print('\033[1;31;41m' + char, end='')
                elif char == TREE:
                    print('\033[1;32;49m' + char, end='')
                elif char in MONSTERS:
                    print('\033[1;33;49m' + char, end='')
                elif char in ITEMS:
                    print('\033[1;36;49m' + char, end='')
                else:
                    print('\033[1;35;49m' + char, end='')
        print('')
    print('\033[1;37;49m', end='')
    print('EXP:', experience_points, '     HP:', health_points)
    print('')


def print_screen(screen):
    os.system('clear')
    print(screen)
    input('Press enter to continue: ')


def print_starting_screens():
    print('\033[1;37;49m')
    introduction_screen = read_screen('intro.txt')
    how_to_play_screen = read_screen('how_to_play.txt')
    print_screen(introduction_screen)
    print_screen(how_to_play_screen)


def print_char_creation_screen():
    os.system('clear')
    character_creation_screen = read_screen('char_creation.txt')
    print(character_creation_screen)


def print_win_screen():
    win_screen = read_screen('win.txt')
    print_screen(win_screen)


def print_lose_screen():
    lose_screen = read_screen('lose.txt')
    print_screen(lose_screen)


def print_hall_of_fame_screen():
    os.system('clear')
    contents = []
    with open('highscores.txt') as file:
        for line in file:
            sublist = line.strip().split(',')
            contents.append(sublist)
    print('\n\n\n\n')
    print("HALL OF FAME\n\n")
    print('Name'.rjust(15), 'Time spent'.rjust(15), 'Monsters killed'.rjust(15))
    for sublist in contents:
        for item in sublist:
            print(item.rjust(15), end=' ')
        print('')
    print('\n')
    input('Press enter to continue: ')


def print_ending_screens():
    info_about_authors_screen = read_screen('authors_info.txt')
    print_hall_of_fame_screen()
    print_screen(info_about_authors_screen)
