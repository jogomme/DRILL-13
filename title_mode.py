import game_framework
from pico2d import *


title_image = None


def init():
    global title_image
    title_image = load_image('title.png')


def finish():
    global title_image
    title_image = None


def update():
    pass


def render():
    clear_canvas()
    title_image.draw(400, 300)
    update_canvas()


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            import play_mode
            game_framework.change_mode(play_mode)
            break
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
