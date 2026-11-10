from pico2d import *
from sdl2 import SDLK_0, SDLK_1, SDLK_2, SDLK_ESCAPE, SDL_KEYDOWN, SDL_QUIT

import game_framework
import game_world
import item_state
from ball import Ball


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
        if event.type != SDL_KEYDOWN:
            continue
        if event.key == SDLK_ESCAPE:
            game_framework.pop_mode()
            return
        selections = {
            SDLK_0: 0,
            SDLK_1: 1,
            SDLK_2: 2,
        }
        if event.key in selections:
            selection = selections[event.key]
            item_state.select_ball(selection)
            if selection == 0:
                for layer in game_world.world:
                    for game_object in layer[:]:
                        if isinstance(game_object, Ball):
                            game_world.remove_object(game_object)
            game_framework.pop_mode()
            return


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    item_image.draw(get_canvas_width() // 2, get_canvas_height() // 2)
    update_canvas()
