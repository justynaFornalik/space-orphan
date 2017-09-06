import random

from constants import MONSTERS


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
