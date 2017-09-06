import random
import os

import printing
import hot_game
from constants import *


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