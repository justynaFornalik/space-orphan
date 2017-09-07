import os
import sys
import time

import printing
import boards
import inv
import move
import fight
import cold_game
import scores

from constants import *


def initialise_player():
    player_row = 1
    player_col = 1
    health_points = INITIAL_HEALTH_POINTS
    experience_points = INITIAL_EXPERIENCE_POINTS
    inventory = {}
    return player_row, player_col, health_points, experience_points, inventory


def choose_player_character():
    players = ['!', '@', '&', ')', '{', ']']
    print('     '.join(players), '\n')
    player = None
    while player not in players:
        player = input()
    return player


def ask_name():
    name = None
    while not name:
        name = input("\nWhat is your name? \n")
    return name


def wait_for_enter():
    input("Press enter to continue: ")


def is_not_enough_uranium(inventory):
    return URANIUM not in inventory or inventory[URANIUM] < NUM_URANIUM_REQUIRED


def say_not_enough_uranium():
    print("You do not have enough uranium to go to the next level!")
    wait_for_enter()


def say_end_level_1():
    print("Fantastic! You gathered enough Uranium for your suit!")
    print("You are able to go to the your enemy's planet to avenge your parents!")
    wait_for_enter()


def is_enough_experience(experience_points):
    return experience_points >= EXPERIENCE_REQUIRED_TO_FIGHT_BOSS


def say_not_enough_experience():
    print("You do not have enough experience to fight The Great Space Hippopotamus!")
    print("Come back when you are worthy!")
    wait_for_enter()


def end_game():
    printing.print_ending_screens()
    os.system('clear')
    sys.exit()


def fight_with_boss(experience_points, name, start_time):
    if is_enough_experience(experience_points):
        os.system('clear')
        result = cold_game.game()
        if result:
            printing.print_win_screen()
            time_spent = round(time.time() - start_time)
            scores.high_scores(name, time_spent, 'highscores.txt')
        else:
            printing.print_lose_screen()
        end_game()
    else:
        say_not_enough_experience()


def play_level(board, player, player_row, player_col, health_points, experience_points, inventory, start_time, name):
    while True:
        printing.print_board(board, player, player_row, player_col, health_points, experience_points)
        key = move.getch().lower()

        if key == ' ':
            inv.display_inventory(inventory)

        elif key in MOVE_KEYS:
            player_row, player_col = move.move_player(board, player_row, player_col, key)
            printing.print_board(board, player, player_row, player_col, health_points, experience_points)
            symbol = board[player_row][player_col]

            if symbol in ITEMS:
                health_points = inv.add_to_inventory(inventory, symbol, health_points)
                board[player_row][player_col] = EMPTY_SPACE

            elif symbol in MONSTERS:
                health_points, experience_points = fight.fight_monster(symbol, health_points, experience_points)
                board[player_row][player_col] = EMPTY_SPACE
                if health_points <= 0:
                    printing.print_lose_screen()
                    end_game()

            elif symbol == WAY_TO_SECOND_LEVEL:
                if is_not_enough_uranium(inventory):
                    say_not_enough_uranium()
                else:
                    break

            elif symbol == BOSS:
                fight_with_boss(experience_points, name, start_time)

    return health_points, experience_points, inventory


def main():
    printing.print_starting_screens()
    printing.print_char_creation_screen()
    player = choose_player_character()
    name = ask_name()
    board = boards.initialise_board('board_level_1.txt')
    player_row, player_col, health_points, experience_points, inventory = initialise_player()
    start_time = time.time()
    health_points, experience_points, inventory = play_level(board, player, player_row, player_col,
                                                             health_points, experience_points, 
                                                             inventory, start_time, name)
    say_end_level_1()
    player_row, player_col = 1, 1
    board = boards.initialise_board('board_level_2.txt')
    play_level(board, player, player_row, player_col, health_points, experience_points, inventory, start_time, name)


if __name__ == '__main__':
    main()
