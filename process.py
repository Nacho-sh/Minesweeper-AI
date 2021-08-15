import pyautogui
from click import click


def check_adjacent(board_map, board, length):
    uleft = 0
    up = 0
    uright = 0
    dleft = 0
    down = 0
    dright = 0
    i = 0
    flagged = 0
    while i < len(board_map):
        if board_map[i] != 0 and board_map[i] != 9 and board_map[i] != 10:
            if i >= length:
                if board_map[i - length - 1] == 0:
                    uleft = 1
                elif board_map[i - length - 1] == 10:
                    flagged = flagged + 1
                    uleft = 0
                else:
                    uleft = 0
                if board_map[i - length] == 0:
                    up = 1
                elif board_map[i - length] == 10:
                    flagged = flagged + 1
                    up = 0
                else:
                    up = 0

                if board_map[i - length + 1] == 0 and (i + 1) % length != 0:
                    uright = 1
                elif board_map[i - length + 1] == 10 and (i + 1) % length != 0:
                    flagged = flagged + 1
                    uright = 0
                else:
                    uright = 0

            if board_map[i - 1] == 0 and i % length != 0:
                left = 1
            elif board_map[i - 1] == 10:
                flagged = flagged + 1
                left = 0
            else:
                left = 0

            if i + 1 < len(board_map) and board_map[i + 1] == 0 and (i + 1) % length != 0:
                right = 1
            elif i + 1 < len(board_map) and board_map[i + 1] == 10 and (i + 1) % length != 0:
                flagged = flagged + 1
                right = 0
            else:
                right = 0

            if i < len(board_map) - length:
                if board_map[i + length - 1] == 0:
                    dleft = 1
                elif board_map[i + length - 1] == 10:
                    flagged = flagged + 1
                    dleft = 0
                else:
                    dleft = 0

                if board_map[i + length] == 0:
                    down = 1
                elif board_map[i + length] == 10:
                    flagged = flagged + 1
                    down = 0
                else:
                    down = 0

                if i + length + 1 < len(board_map) and board_map[i + length + 1] == 0 and (i + 1) % length != 0:
                    dright = 1
                elif i + length + 1 < len(board_map) and board_map[i + length + 1] == 10 and (i + 1) % length != 0:
                    flagged = flagged + 1
                    dright = 0
                else:
                    dright = 0

            hidden_num = uleft + up + uright + left + right + dleft + down + dright + flagged
            if hidden_num == board_map[i]:
                if uleft == 1 and board_map[i - length - 1] != 10 and i > 11:
                    click(i - length - 1, board, length, 'right')
                    board_map[i - length - 1] = 10
                if up == 1 and board_map[i - length] != 10 and i > 10:
                    click(i - length, board, length, 'right')
                    board_map[i - length] = 10
                if uright == 1 and board_map[i - length + 1] != 10 and i > 9:
                    board_map[i - length + 1] = 10
                    click(i - length + 1, board, length, 'right')
                if left == 1 and board_map[i - 1] != 10 and i > 0:
                    board_map[i - 1] = 10
                    click(i - 1, board, length, 'right')
                if i + 1 < len(board_map) and right == 1 and board_map[i + 1] != 10:
                    board_map[i + 1] = 10
                    click(i + 1, board, length, 'right')
                if i + length - 1 < len(board_map) and dleft == 1 and board_map[i + length - 1] != 10:
                    board_map[i + length - 1] = 10
                    click(i + length - 1, board, length, 'right')
                if i + length < len(board_map) and down == 1 and board_map[i + length] != 10:
                    board_map[i + length] = 10
                    click(i + length, board, length, 'right')
                if i + length + 1 < len(board_map) and dright == 1 and board_map[i + length + 1] != 10:
                    board_map[i + length + 1] = 10
                    click(i + length + 1, board, length, 'right')
            elif flagged == board_map[i]:
                if uleft == 1 and i % length != 0:
                    click(i - length - 1, board, length)
                if up == 1 and i >= 10:
                    click(i - length, board, length)
                if uright == 1 and (i + 1) % length != 0:
                    click(i - length + 1, board, length)
                if left == 1 and i % length != 0:
                    click(i - 1, board, length)
                if right == 1 and (i + 1) % length != 0:
                    click(i + 1, board, length)
                if dleft == 1 and i % length != 0 and i + length < len(board_map):
                    click(i + length - 1, board, length)
                if down == 1 and i + length < len(board_map):
                    click(i + length, board, length)
                if dright == 1 and i + length + 1 < len(board_map):
                    click(i + length + 1, board, length)
        i = i + 1
        flagged = 0
    pyautogui.moveTo(10, 10)
    return board_map

# TODO
'''
def make_tree(board_map, i, uleft, up, uright, left, right, dleft, down, dright, length):
    map_list = []

    def check_flags():
        flagged = 0
        while i < len(board_map):
            if board_map[i] != 0 and board_map[i] != 9 and board_map[i] != 10:
                if i >= length:
                    if uleft == 10 and i % length != 0:
                        flagged = flagged + 1
                    if board_map[i - length] == 10:
                        flagged = flagged + 1
                    if board_map[i - length + 1] == 10 and (i + 1) % length != 0:
                        flagged = flagged + 1
                if board_map[i - 1] == 10 and i % length != 0:
                    flagged = flagged + 1
                if i + 1 < len(board_map) and board_map[i + 1] == 10 and (i + 1) % length != 0:
                    flagged = flagged + 1
                if i < len(board_map) - length:
                    if board_map[i + length - 1] == 10:
                        flagged = flagged + 1
                    if board_map[i + length] == 10:
                        flagged = flagged + 1
                    if i + length + 1 < len(board_map) and board_map[i + length + 1] == 10 and (i + 1) % length != 0:
                        flagged = flagged + 1
                if flagged <= board_map[i]:
                    make_tree(board_map, i, uleft, up, uright, left, right, dleft, down, dright, length)

    uleft = 0
    up = 0
    uright = 0
    dleft = 0
    down = 0
    dright = 0
    i = 0
    flagged = 0
    while i < len(board_map):
        if board_map[i] != 0 and board_map[i] != 9 and board_map[i] != 10:
            if i >= length:
                if board_map[i - length - 1] == 0:
                    uleft = 1
                elif board_map[i - length - 1] == 10:
                    flagged = flagged + 1
                    uleft = 0
                else:
                    uleft = 0
                if board_map[i - length] == 0:
                    up = 1
                elif board_map[i - length] == 10:
                    flagged = flagged + 1
                    up = 0
                else:
                    up = 0

                if board_map[i - length + 1] == 0 and (i + 1) % length != 0:
                    uright = 1
                elif board_map[i - length + 1] == 10 and (i + 1) % length != 0:
                    flagged = flagged + 1
                    uright = 0
                else:
                    uright = 0

            if board_map[i - 1] == 0 and i % length != 0:
                left = 1
            elif board_map[i - 1] == 10:
                flagged = flagged + 1
                left = 0
            else:
                left = 0

            if i + 1 < len(board_map) and board_map[i + 1] == 0 and (i + 1) % length != 0:
                right = 1
            elif i + 1 < len(board_map) and board_map[i + 1] == 10 and (i + 1) % length != 0:
                flagged = flagged + 1
                right = 0
            else:
                right = 0

            if i < len(board_map) - length:
                if board_map[i + length - 1] == 0:
                    dleft = 1
                elif board_map[i + length - 1] == 10:
                    flagged = flagged + 1
                    dleft = 0
                else:
                    dleft = 0

                if board_map[i + length] == 0:
                    down = 1
                elif board_map[i + length] == 10:
                    flagged = flagged + 1
                    down = 0
                else:
                    down = 0

                if i + length + 1 < len(board_map) and board_map[i + length + 1] == 0 and (i + 1) % length != 0:
                    dright = 1
                elif i + length + 1 < len(board_map) and board_map[i + length + 1] == 10 and (i + 1) % length != 0:
                    flagged = flagged + 1
                    dright = 0
                else:
                    dright = 0

            hidden_num = uleft + up + uright + left + right + dleft + down + dright + flagged
        i = i + 1
        flagged = 0'''
