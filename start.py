import pyautogui as gui
from time import sleep
from update import map_nums
global size, location, board
length = 94
high = 44


def init_map():
    global size, length, high
    # length = int(input("Long"))
    # high = int(input("High"))
    return [0] * high * length


def locate_board():
    sleep(5)
    global location, size, board
    location = gui.locateOnScreen('images/hidden.png', confidence=0.9)
    board = (location[0], location[1], length * 20, high * 20)


def start():
    global length, high
    init_map()
    locate_board()
    gui.click(location[0] + length * 10 + 10, location[1] + high * 10 + 10)
    gui.moveTo(10, 10)
    map_nums(init_map(), board, length)


start()
