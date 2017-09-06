PLAYER = '@'
EMPTY_SPACE = ' '
BOSS = '0'
EXPERIENCE_REQUIRED_TO_FIGHT_BOSS = 0

INITIAL_HEALTH_POINTS = 1
INITIAL_EXPERIENCE_POINTS = 1

UP = -1
DOWN = +1
LEFT = -1
RIGHT = +1
NO_CHANGE = 0

MOVE_KEYS = {'w': (UP, NO_CHANGE), 's': (DOWN, NO_CHANGE), 'a': (NO_CHANGE, LEFT), 'd': (NO_CHANGE, RIGHT)}

WALL = '#'
LAVA = '~'
TREE = '^'
OBSTACLES = (WALL, LAVA, TREE)

SPACE_SLOTH = 'L'
SPACE_SKUNK = 'S'
SPACE_RACOON = 'R'
SPACE_GIRAFFE = 'G'
MONSTERS = {SPACE_SLOTH: ['space sloth', 2],
            SPACE_SKUNK: ['space_skunk', 3],
            SPACE_RACOON: ['space_racoon', 4],
            SPACE_GIRAFFE: ['space giraffe', 5]}
MONSTERS_TO_THEIR_INITIAL_NUM = {SPACE_SLOTH: 5, SPACE_SKUNK: 5, SPACE_RACOON: 5, SPACE_GIRAFFE: 5}


SPACE_WATER = '%'
SPACE_BANANA = '('
SPACE_PIE = '*'
URANIUM = 'U'
ITEMS = {SPACE_WATER: ['space water', 'food', 1],
         SPACE_BANANA: ['space banana', 'food', 1],
         SPACE_PIE: ['space pie', 'food', 1],
         URANIUM: ['uranium', 'material', 1]}
ITEMS_TO_THEIR_INITIAL_NUM = {SPACE_WATER: 5, SPACE_BANANA: 5, SPACE_PIE: 5, URANIUM: 5}