from pico2d import *
from sdl2 import SDL_QUIT

import game_framework


item_image = None


def init():
    global item_image
    item_image = load_image('item_select.png')


def finish():
    global item_image
    item_image = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return


def update():
    pass


def render():
    clear_canvas()
    item_image.draw(get_canvas_width() // 2, get_canvas_height() // 2)
    update_canvas()
