import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball, BigBall
from bird import bird

name = "MainState"

boy = None
grass = None
# bird1 = None
# bird2 = None
# bird3 = None
# bird4 = None
# bird5 = None

balls = []
big_balls = []



def collide(a, b):
    left_a , bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True




def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    # global bird1
    # bird1 = bird()
    # game_world.add_object(bird1, 2)

    global balls
    balls = [Ball() for i in range(10)] + [BigBall() for i in range(10)]
    game_world.add_objects(balls, 1)

    # global bird2
    # bird2 = bird()
    # game_world.add_object(bird2, 3)
    #
    # global bird3
    # bird3 = bird()
    # game_world.add_object(bird3, 4)
    #
    # global bird4
    # bird4 = bird()
    # game_world.add_object(bird4, 5)
    #
    # global bird5
    # bird5 = bird()
    # game_world.add_object(bird5, 6)

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
    for ball in balls:
        if collide(boy, ball):
            balls.remove(ball)
            game_world.remove_object(ball)
            # print("COLLISON")



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






