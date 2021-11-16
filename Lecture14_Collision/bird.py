import game_framework
from pico2d import *
import game_world
import random

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
BIRD_SPEED_KMPH = 0.3  # Km / Hour
BIRD_SPEED_MPM = (BIRD_SPEED_KMPH * 1000.0 / 60.0)
BIRD_SPEED_MPS = (BIRD_SPEED_MPM / 60.0)
BIRD_SPEED_PPS = (BIRD_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

SPACE = range(1)

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


class Fly:
    def enter(bird, event):
        pass

    def exit(bird, event):
        pass

    def do(bird):
        if bird.x >= 1600 and bird.dir == 1:
            bird.dir = 0
        elif bird.x <= 100 and bird.dir == 0:
            bird.dir = 1
        if bird.dir == 1:
            bird.velocity += BIRD_SPEED_PPS
        elif bird.dir == 0:
            bird.velocity -= BIRD_SPEED_PPS
        bird.x += bird.velocity * game_framework.frame_time
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14


    def draw(bird):
        if bird.dir == 1:
            bird.image.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y)
        else:
            bird.image.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y)

next_state_table = { Fly:{SPACE: Fly}}



class bird:

    def __init__(self):
        self.x, self.y = random.randint(100, 700), random.randint(100, 500)
        self.image = load_image('bird100x100x14.png')
        self.dir = 1
        self.frame = 0
        self.velocity = 0
        self.event_que = []
        self.cur_state = Fly
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
    def draw(self):
        self.cur_state.draw(self)