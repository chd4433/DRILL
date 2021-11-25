import random
from pico2d import *
import game_world
import game_framework


class Ball:
    MIN_FALL_SPEED = 50  # 50 pps = 1.5 meter per sec
    MAX_FALL_SPEED = 400 # 200 pps = 6 meter per sec
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), 600, random.randint(Ball.MIN_FALL_SPEED, Ball.MAX_FALL_SPEED)
        self.speed_x = 0
        self.collide_ball_size = 0
        self.collide_x, self.collide_y = 0, 0

    def get_bb(self):
        # fill here
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def get_bb2(self):
        return self.collide_x - self.collide_ball_size, self.collide_y - self.collide_ball_size, self.collide_x + self.collide_ball_size, self.collide_y + self.collide_ball_size

    def draw(self):
        self.image.draw(self.x, self.y)
        # fill here
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time
        self.x += game_framework.frame_time * self.speed_x
        # if self.x > 1600:
        #     self.x = 1600
        #     self.speed_x = -self.speed_x
        # if self.x < 0:
        #     self.x = 0
        #     self.speed_x = -self.speed_x

    def stop(self):
        self.fall_speed = 0

    def collide_brick(self, speed):
        self.fall_speed = 0
        self.speed_x = speed
        self.collide_ball_size = 10
        self.collide_x, self.collide_y = self.x, self.y


