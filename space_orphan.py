
import random
import sys
import tty
import termios
import time
import os

import inventory
import hot_game
import printing
import boards

from constants import *


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


def move_player(board, player_row, player_col, key):
    new_player_row = player_row + MOVE_KEYS[key][0]
    new_player_col = player_col + MOVE_KEYS[key][1]

    if not is_obstacle(board, new_player_row, new_player_col):
        player_row, player_col = new_player_row, new_player_col

    return player_row, player_col


def fight_monster(monster, health_points, experience_points):
    print('You encounter a ' + MONSTERS[monster][0] + '!')
    draw = random.randint(1, 2)
    if draw == 1:
        health_points -= MONSTERS[monster][1]
        print('The ' + MONSTERS[monster][0] + ' hits you. You lose ' + str(MONSTERS[monster][1]) + ' health points.')
    else:
        experience_points -= MONSTERS[monster][1]
        print('You hit the ' + MONSTERS[monster][0] + '. You kill it and gain ' + str(MONSTERS[monster][1]) + ' experience points.')
    input('Press enter to continue: ')

    return health_points, experience_points


def fight_with_boss(health_points, experience_points):
    if experience_points > EXPERIENCE_REQUIRED_TO_FIGHT_BOSS:
        os.system('clear')
        result = hot_game.game()
        if result:
            printing.print_screen(printing.win_screen)
            printing.print_hall_of_fame_screen()
        else:
            printing.print_screen(printing.lose_screen)
        printing.print_info_about_authors()
    else:
        print("You don't have enough experience. Come back when you are worthy!")
        time.sleep(3)


def play_level(board, player_row, player_col, health_points, experience_points, inventory):
    while health_points > 0:
        print_board(board, player_row, player_col)
        key = getch()
        if key in MOVE_KEYS:
            player_row, player_col = move_player(board, player_row, player_col, key)
            print_board(board, player_row, player_col)

            if board[player_row][player_col] in ITEMS:
                item = board[player_row][player_col]
                inventory.add_to_inventory(inventory, item)
                inventory.display_inventory(inventory)
                board[player_row][player_col] = EMPTY_SPACE

            elif board[player_row][player_col] in MONSTERS:
                monster = board[player_row][player_col]
                health_points, experience_points = fight_monster(monster, health_points, experience_points)
                if health_points <= 0:
                    printing.print_screen(printing.lose_screen)
                    printing.print_info_about_authors()
                board[player_row][player_col] = EMPTY_SPACE

            elif board[player_row][player_col] == BOSS:
                result = fight_with_boss(health_points, experience_points)

        elif key == ' ':
            display_inventory(inventory)
    return health_points, experience_points, inventory


def initialise_player():
    player_row = 1
    player_col = 1
    health_points = INITIAL_HEALTH_POINTS
    experience_points = INITIAL_EXPERIENCE_POINTS
    inventory = {}
    return player_row, player_col, health_points, experience_points, inventory


def main():
    printing.print_starting_screens()
    board = boards.initialise_board('board_level_1.txt')
    player_row, player_col, health_points, experience_points, inventory = initialise_player()
    play_level(board, player_row, player_col, health_points, experience_points, inventory)

main()
