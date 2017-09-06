import sys
import tty
import termios

from constants import *


def is_obstacle(board, row, col):
    if board[row][col] in OBSTACLES:
        return True
    else:
        return False


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def move_player(board, player_row, player_col, key):
    new_player_row = player_row + MOVE_KEYS[key][0]
    new_player_col = player_col + MOVE_KEYS[key][1]

    if not is_obstacle(board, new_player_row, new_player_col):
        player_row, player_col = new_player_row, new_player_col

    return player_row, player_col