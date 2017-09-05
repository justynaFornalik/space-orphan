import os
import random
import sys
import tty
import termios

import game_inventory

PLAYER = '@'

WALL = '#'
RIVER = '~'
TREE = '^'
OBSTACLES = (WALL, RIVER, TREE)

EMPTY_SPACE = ' '

SPACE_SLOTH = 'L'
SPACE_SKUNK = 'S'
SPACE_RACOON = 'R'
SPACE_GIRAFFE = 'G'
SPACE_MONSTERS = (SPACE_SLOTH, SPACE_SKUNK, SPACE_RACOON, SPACE_GIRAFFE)
BOSS = '0'

SPACE_WATER = 'W'
SPACE_BANANA = 'B'
SPACE_PIE = 'P'
URANIUM = 'U'
ITEMS = (SPACE_WATER, SPACE_BANANA, SPACE_PIE, URANIUM)

UP = -1
DOWN = +1
LEFT = -1
RIGHT = +1
NO_CHANGE = 0

MOVE_KEYS = {'w': (UP, NO_CHANGE), 's': (DOWN, NO_CHANGE), 'a': (NO_CHANGE, LEFT), 'd': (NO_CHANGE, RIGHT)}


def print_introduction_screen():
    pass


def print_character_creation_screen():
    pass


def print_how_to_play_screen():
    pass


def make_board(file_name):
    board = []
    with open(file_name) as file:
        for line in file:
            line = line.strip()
            sublist = [item for item in line]
            board.append(sublist)
    return board


def find_empty_spaces(board):
    empty_spaces = []
    for i, sublist in enumerate(board):
        for n, char in enumerate(sublist):
            if board[i][n] == EMPTY_SPACE:
                empty_spaces.append((i, n))
    return empty_spaces


def put_on_board(what, board, row, col):
    board[row][col] = what


def print_board(board, player_row, player_col):
    os.system('clear')
    for i, sublist in enumerate(board):
        for n, char in enumerate(sublist):
            if player_row == i and player_col == n:
                print(PLAYER, end='')
            else:
                print(char, end='')
        print('\n', end='')


def is_obstacle(board, row, col):
    if board[row][col] in OBSTACLES:
        return True
    else:
        return False


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def move_player(board, player_row, player_col):
    key = getch()
    if key in MOVE_KEYS:
        new_player_row = player_row + MOVE_KEYS[key][0]
        new_player_col = player_col + MOVE_KEYS[key][1]

        if not is_obstacle(board, new_player_row, new_player_col):
            player_row, player_col = new_player_row, new_player_col

    return player_row, player_col


def pick_up_item(inventory):
    pass


def fight_monster(health_points, inventory):
    pass


def fight_with_boss(health_points, inventory):
    pass


def play_level(board, player_row, player_col, health_points):
    while health_points > 0:
        print_board(board, player_row, player_col)
        player_row, player_col = move_player(board, player_row, player_col)


        if board[player_row][player_col] in ITEMS:
            pick_up_item(inventory)

        elif board[player_row][player_col] in SPACE_MONSTERS:
            fight_monster(monster, health_points, inventory)

        elif board[player_row][player_col] == BOSS:
            fight_with_boss(health_points, inventory)


def print_win_screen():
    pass


def print_lose_screen():
    pass


def highscores():
    pass


def print_hall_of_fame_screen():
    pass


def main():
    print_introduction_screen()
    print_character_creation_screen()
    print_how_to_play_screen()




    board = make_board('board_level_1.txt')

    player_row = 1
    player_col = 1

    health_points = 15
    experience_points = 1
    inventory = {}

    play_level(board, player_row, player_col, health_points)




    print_win_screen()
    print_lose_screen()
    print_hall_of_fame_screen()


main()
