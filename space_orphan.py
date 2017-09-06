
import random
import time
import os


import printing
import boards
import inv
import move
import fight


from constants import *


def initialise_player():
    player_row = 1
    player_col = 1
    health_points = INITIAL_HEALTH_POINTS
    experience_points = INITIAL_EXPERIENCE_POINTS
    inventory = {}
    return player_row, player_col, health_points, experience_points, inventory


def play_level(board, player_row, player_col, health_points, experience_points, inventory):
    while health_points > 0:
        printing.print_board(board, player_row, player_col)
        key = move.getch()
        if key in MOVE_KEYS:
            player_row, player_col = move.move_player(board, player_row, player_col, key)
            printing.print_board(board, player_row, player_col)

            if board[player_row][player_col] in ITEMS:
                item = board[player_row][player_col]
                inv.add_to_inventory(inventory, item)
                inv.display_inventory(inventory)
                board[player_row][player_col] = EMPTY_SPACE

            elif board[player_row][player_col] in MONSTERS:
                monster = board[player_row][player_col]
                health_points, experience_points = fight.fight_monster(monster, health_points, experience_points)
                if health_points <= 0:
                    printing.print_screen(printing.lose_screen)
                    printing.print_info_about_authors()
                board[player_row][player_col] = EMPTY_SPACE

            elif board[player_row][player_col] == BOSS:
                result = fight.fight_with_boss(health_points, experience_points)

        elif key == ' ':
            inv.display_inventory(inventory)
    return health_points, experience_points, inventory


def main():
    printing.print_starting_screens()
    board = boards.initialise_board('board_level_1.txt')
    player_row, player_col, health_points, experience_points, inventory = initialise_player()
    play_level(board, player_row, player_col, health_points, experience_points, inventory)

main()
