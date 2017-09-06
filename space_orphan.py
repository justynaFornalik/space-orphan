import os
import sys

import printing
import boards
import inv
import move
import fight
import hot_game

from constants import *


def initialise_player():
    player_row = 1
    player_col = 1
    health_points = INITIAL_HEALTH_POINTS
    experience_points = INITIAL_EXPERIENCE_POINTS
    inventory = {}
    return player_row, player_col, health_points, experience_points, inventory


def is_not_enough_uranium(inventory):
    return URANIUM not in inventory or inventory[URANIUM] < NUM_URANIUM_REQUIRED


def say_not_enough_uranium():
    print("You do not have enough uranium to go to the next level!")
    input("Press enter to continue: ")


def is_enough_experience(experience_points):
    return experience_points > EXPERIENCE_REQUIRED_TO_FIGHT_BOSS


def say_not_enough_experience():
    print("You do not have enough experience to fight The Great Space Hippopotamus!")
    print("Come back when you are worthy!")
    input("Press enter to continue: ")


def fight_with_boss():
    if is_enough_experience(experience_points):
        os.system('clear')
        result = hot_game.game()
        if result:
            printing.print_screen(printing.win_screen)
        else:
            printing.print_screen(printing.lose_screen)
        end_game()
    else:
        say_not_enough_experience()


def end_game():
    printing.print_ending_screens()
    os.system('clear')
    sys.exit()


def play_level(board, player_row, player_col, health_points, experience_points, inventory):
    while True:
        printing.print_board(board, player_row, player_col)
        key = move.getch()

        if key == ' ':
            inv.display_inventory(inventory)

        elif key in MOVE_KEYS:
            player_row, player_col = move.move_player(board, player_row, player_col, key)
            printing.print_board(board, player_row, player_col)
            symbol = board[player_row][player_col]

            if symbol in ITEMS:
                inv.add_to_inventory(inventory, symbol)
                board[player_row][player_col] = EMPTY_SPACE

            elif symbol in MONSTERS:
                health_points, experience_points = fight.fight_monster(symbol, health_points, experience_points)
                board[player_row][player_col] = EMPTY_SPACE
                if health_points <= 0:
                    printing.print_screen(printing.lose_screen)
                    end_game()

            elif symbol == WAY_TO_SECOND_LEVEL:
                if is_not_enough_uranium(inventory):
                    say_not_enough_uranium()
                else:
                    break

            elif symbol == BOSS:
                fight_with_boss()

    return health_points, experience_points, inventory


def main():
    printing.print_starting_screens()
    board = boards.initialise_board('board_level_1.txt')
    player_row, player_col, health_points, experience_points, inventory = initialise_player()
    health_points, experience_points, inventory = play_level(board, player_row, player_col,
                                                             health_points, experience_points, inventory)

    player_row, player_col = 1, 1
    board = boards.initialise_board('board_level_2.txt')
    play_level(board, player_row, player_col, health_points, experience_points, inventory)


if __name__ == '__main__':
    main()
