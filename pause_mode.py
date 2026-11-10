import os
from ctypes import byref, c_int

from pico2d import *
from sdl2 import SDLK_ESCAPE, SDLK_p
from sdl2.sdlttf import TTF_SizeUTF8

import game_framework
import game_world


pause_font = None
pause_text = 'PAUSED - Press P to resume'
pause_text_x = 0


def init():
    global pause_font, pause_text_x
    font_path = os.path.join(os.environ['WINDIR'], 'Fonts', 'arial.ttf')
    pause_font = load_font(font_path, 30)
    text_width = c_int()
    text_height = c_int()
    if TTF_SizeUTF8(
            pause_font.font, pause_text.encode('utf-8'),
            byref(text_width), byref(text_height)) != 0:
        raise RuntimeError('Could not measure the pause message')
    pause_text_x = (get_canvas_width() - text_width.value) / 2


def finish():
    global pause_font
    pause_font = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()
            return
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            import title_mode
            game_framework.pop_mode()
            game_framework.change_mode(title_mode)
            return


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    pause_font.draw(
        pause_text_x, get_canvas_height() / 2, pause_text, (0, 0, 0)
    )
    update_canvas()
