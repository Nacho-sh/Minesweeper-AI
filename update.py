import random

import pyautogui as gui
from process import check_adjacent
from click import click


# Finds and allocates in its respective position every number visible in the board.
def map_nums(board_map, board, length=0):
    i = 0

    for pos in gui.locateAllOnScreen('images/1.png', region=board, confidence=0.9):
        board_map[((pos[1] - board[1]) // 20) * length + ((pos[0] - board[0]) // 20) % length] = 1
        i = i + 1

    i = 0
    for pos in gui.locateAllOnScreen('images/2.png', region=board, confidence=0.9):
        board_map[((pos[1] - board[1]) // 20) * length + ((pos[0] - board[0]) // 20) % length] = 2
        i = i + 1

    i = 0
    for pos in gui.locateAllOnScreen('images/3.png', region=board, confidence=0.9):
        board_map[((pos[1] - board[1]) // 20) * length + ((pos[0] - board[0]) // 20) % length] = 3
        i = i + 1

    i = 0
    for pos in gui.locateAllOnScreen('images/4.png', region=board, confidence=0.9):
        board_map[((pos[1] - board[1]) // 20) * length + ((pos[0] - board[0]) // 20) % length] = 4
        i = i + 1

    i = 0
    for pos in gui.locateAllOnScreen('images/5.png', region=board, confidence=0.9):
        board_map[((pos[1] - board[1]) // 20) * length + ((pos[0] - board[0]) // 20) % length] = 5
        i = i + 1

    i = 0
    for pos in gui.locateAllOnScreen('images/6.png', region=board, confidence=0.9):
        board_map[((pos[1] - board[1]) // 20) * length + ((pos[0] - board[0]) // 20) % length] = 6
        i = i + 1

    i = 0
    for pos in gui.locateAllOnScreen('images/7.png', region=board, confidence=0.9):
        board_map[((pos[1] - board[1]) // 20) * length + ((pos[0] - board[0]) // 20) % length] = 7
        i = i + 1

    i = 0
    for pos in gui.locateAllOnScreen('images/8.png', region=board, confidence=0.9):
        board_map[((pos[1] - board[1]) // 20) * length + ((pos[0] - board[0]) // 20) % length] = 8
        i = i + 1

    i = 0
    for pos in gui.locateAllOnScreen('images/empty.png', region=board, confidence=0.9):
        board_map[((pos[1] - board[1]) // 20) * length + ((pos[0] - board[0]) // 20) % length] = 9
        i = i + 1
    i = 0

    for pos in gui.locateAllOnScreen('images/flag.png', region=board, confidence=0.95):
        board_map[((pos[1] - board[1]) // 20) * length + ((pos[0] - board[0]) // 20) % length] = 10
        i = i + 1
    if not (1 in board_map and 2 in board_map and 9 in board_map):
        click(random.randint(0, len(board_map)), board, length)
    board_map = check_adjacent(board_map, board, length)
    map_nums(board_map, board, length)


