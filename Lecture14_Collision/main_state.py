import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball
from bird import bird

name = "MainState"

boy = None
grass = None
bird1 = None
bird2 = None
bird3 = None
bird4 = None
bird5 = None

balls = []
big_balls = []



def collide(a, b):
    # fill here
    return True




def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    global bird1
    bird1 = bird()
    game_world.add_object(bird1, 2)

    global bird2
    bird2 = bird()
    game_world.add_object(bird2, 3)

    global bird3
    bird3 = bird()
    game_world.add_object(bird3, 4)

    global bird4
    bird4 = bird()
    game_world.add_object(bird4, 5)

    global bird5
    bird5 = bird()
    game_world.add_object(bird5, 6)

    # fill here for balls





def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    # fill here for collision check



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






