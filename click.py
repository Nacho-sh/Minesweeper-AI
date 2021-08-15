import pyautogui as gui


def click(position, board, length, button='left'):
    gui.click(board[0] + 10 + position % length * 20, board[1] + position // length * 20 + 10, button=button)
