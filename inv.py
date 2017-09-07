import time

from constants import ITEMS, URANIUM


def display_inventory(inventory):
    table_bar = []
    table_bar.append("-"*70)
    headline = ' '*10 + 'NAME' + ' ' * 15 + 'TYPE'+' ' * 10 + 'WEIGHT'+' '*10 + 'QUANTITY'

    if inventory:
        print("Your space inventory:")
        print(headline)
        print("".join(table_bar))
        for item in ITEMS:
            if item in inventory:
                print((ITEMS[item][0]).rjust(15), (ITEMS[item][1]).rjust(15),
                      str(ITEMS[item][2]).rjust(15), str(inventory[item]).rjust(15))
        print("".join(table_bar))
    else:
        print('Empty inventory')
    input("Press enter to continue: ")


def add_to_inventory(inventory, item, health_points):
    if item in inventory.keys():
        inventory[item] = 1 + inventory[item]
    else:
        inventory[item] = 1
    if item != URANIUM:
        health_points += 3
    print(ITEMS[item][0].capitalize(), 'was added to your inventory.')
    print('You gained 3 health points.')
    display_inventory(inventory)
    return health_points
