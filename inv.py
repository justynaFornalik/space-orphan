import time

from constants import *


def add_to_inventory(inventory, item):
    if item in inventory.keys():
        inventory[item] = 1 + inventory[item]
    else:
        inventory[item] = 1
    return inventory


def display_inventory(inventory):
    table_bar = []
    table_bar.append("-"*70)
    print("Your space inventory:")
    headline = ' '*10 + 'NAME' + ' ' * 15 + 'TYPE'+' ' * 10 + 'WEIGHT'+' '*10 + 'QUANTITY'
    print(headline)
    print("".join(table_bar))

    if inventory:
        for item in ITEMS:
            if item in inventory:
                print((ITEMS[item][0]).rjust(15), (ITEMS[item][1]).rjust(15),
                      str(ITEMS[item][2]).rjust(15), str(inventory[item]).rjust(15))
        print("".join(table_bar))
    else:
        print('Empty inventory')
    input("Press enter to continue: ")
    
