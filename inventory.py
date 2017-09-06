SPACE_WATER = 'W'
SPACE_BANANA = 'B'
SPACE_PIE = 'P'
URANIUM = 'U'

ITEMS = {SPACE_WATER: ['space water', 'food', 1],
         SPACE_BANANA: ['space banana', 'food', 1],
         SPACE_PIE: ['space pie', 'food', 1],
         URANIUM: ['uranium', 'material', 1]}
HEADLINE = ' '*10 + 'NAME' + ' ' * 15 + 'TYPE'+' ' * 10 + 'WEIGHT'+' '*10 + 'QUANTITY'


def add_to_inventory(inventory, item):
    if item in inventory.keys():
        inventory[item] = 1 + inventory[item]
    else:
        inventory[item] = 1
    return inventory


def display_inventory(inventory, ITEMS):
    table_bar = []
    table_bar.append("-"*70)
    print("Your space inventory:")
    print(HEADLINE)   
    print("".join(table_bar))

    for item in ITEMS:
        print((ITEMS[item][0]).rjust(15), (ITEMS[item][1]).rjust(15), str(ITEMS[item][2]).rjust(15), str(inventory[item]).rjust(15))
    print("".join(table_bar))
    return inventory


