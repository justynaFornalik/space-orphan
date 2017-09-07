# Symbols on board
EMPTY_SPACE = ' '
BOSS = '('
WAY_TO_SECOND_LEVEL = '<'

# Obstacles
WALL = '#'
LAVA = '~'
TREE = '^'
OBSTACLES = (WALL, LAVA, TREE)

# Monsters
SPACE_SLOTH = 'L'
SPACE_SKUNK = 'S'
SPACE_RACOON = 'R'
SPACE_GIRAFFE = 'G'

# Dict of monster symbol to two_element list which constists of
# name of monster and health points it takes when it hits.
MONSTERS = {SPACE_SLOTH: ['space sloth', 2],
            SPACE_SKUNK: ['space skunk', 3],
            SPACE_RACOON: ['space racoon', 4],
            SPACE_GIRAFFE: ['space giraffe', 5]}

# Items
SPACE_WATER = '%'
SPACE_BANANA = 'C'
SPACE_PIE = '*'
URANIUM = 'U'

# Dict of item symbol to three-element list which constist of
# name of item, type of item and its weigth.
ITEMS = {SPACE_WATER: ['space water', 'food', 0.1],
         SPACE_BANANA: ['space banana', 'food', 0.2],
         SPACE_PIE: ['space pie', 'food', 0.5],
         URANIUM: ['uranium', 'material', 1.0]}

# Dict of monster symbol to initial number of this monster on the board
MONSTERS_TO_THEIR_INITIAL_NUM = {SPACE_SLOTH: 5, SPACE_SKUNK: 4, SPACE_RACOON: 3, SPACE_GIRAFFE: 2}
# Dict of item symbol to initial number of this item on the board
ITEMS_TO_THEIR_INITIAL_NUM = {SPACE_WATER: 10, SPACE_BANANA: 5, SPACE_PIE: 5, URANIUM: 10}

# Controls
UP = -1
DOWN = +1
LEFT = -1
RIGHT = +1
NO_CHANGE = 0

# Dict of key symbol to tuple of horizontal direction change and vertical diretion change
MOVE_KEYS = {'w': (UP, NO_CHANGE), 's': (DOWN, NO_CHANGE), 'a': (NO_CHANGE, LEFT), 'd': (NO_CHANGE, RIGHT)}

INITIAL_HEALTH_POINTS = 1
INITIAL_EXPERIENCE_POINTS = 1
EXPERIENCE_REQUIRED_TO_FIGHT_BOSS = 1  # change this to bigger number
NUM_URANIUM_REQUIRED = 1  # change this to bigger number
