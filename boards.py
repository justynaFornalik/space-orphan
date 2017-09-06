import random

from constants import EMPTY_SPACE, MONSTERS_TO_THEIR_INITIAL_NUM, ITEMS_TO_THEIR_INITIAL_NUM


def make_board(file_name):
    board = []
    with open(file_name) as file:
        for line in file:
            line = line.strip()
            sublist = [item for item in line]
            board.append(sublist)
    return board


def find_empty_spaces(board):
    empty_spaces = []
    for i, sublist in enumerate(board):
        for n, char in enumerate(sublist):
            if board[i][n] == EMPTY_SPACE:
                empty_spaces.append((i, n))
    return empty_spaces


def put_on_board(board, what):
    empty_spaces = find_empty_spaces(board)
    for item in what:
        for i in range(what[item]):
            row, col = random.choice(empty_spaces)
            board[row][col] = item
            empty_spaces.remove((row, col))


def initialise_board(file_name):
    board = make_board(file_name)
    put_on_board(board, MONSTERS_TO_THEIR_INITIAL_NUM)
    put_on_board(board, ITEMS_TO_THEIR_INITIAL_NUM)
    return board
