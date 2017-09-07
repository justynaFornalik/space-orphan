import random
import time

from constants import MONSTERS


def fight_monster(monster, health_points, experience_points):
    print('You encounter a ' + MONSTERS[monster][0] + '!')
    time.sleep(1)
    draw = random.randint(1, 3)
    if draw == 1:
        health_points -= MONSTERS[monster][1]
        print('The ' + MONSTERS[monster][0] + ' hits you.You lose ' + str(MONSTERS[monster][1]) + ' health points.')
        time.sleep(1)
    elif draw == 2:
        print('The ' + MONSTERS[monster][0] + ' strikes and misses you.')
        time.sleep(1)
    else:
        print('The ' + MONSTERS[monster][0] + ' tries to run away.')
        time.sleep(1)
    experience_points += MONSTERS[monster][1]
    print('You hit the ' + MONSTERS[monster][0] + '. You kill it and gain '
          + str(MONSTERS[monster][1]) + ' experience points.')
    time.sleep(1)
    input('Press enter to continue: ')

    return health_points, experience_points
