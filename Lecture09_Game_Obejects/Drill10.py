from pico2d import *
import random

# Game object class here

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x = random.randint(100, 700)
        self.y = 90
        self.frame = random.randint(0, 7)

    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.n = random.randint(0, 7)
        if self.n % 2 == 0:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')
        self.x = random.randint(100, 700)
        self.y = random.randint(100, 700)
        self.speed = random.randint(1, 7)
        self.frame = 0
        # self.frame = random.randint(0, 7)

    def update(self):
        if self.n % 2 == 0:
            if self.y - self.speed <= 62:
                self.y = 62
            else:
                self.y -= self.speed
        else:
            if self.y - self.speed <= 72:
                self.y = 72
            else:
                self.y -= self.speed

        # self.frame = (self.frame + 1) %

    def draw(self):
        if self.n % 2 == 0:
            self.image.clip_draw(self.frame, 0, 21, 21, self.x, self.y)
        else:
            self.image.clip_draw(self.frame, 0, 41, 41, self.x, self.y)





def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code

open_canvas()

grass = Grass()
# boy = Boy()

team = [ Boy() for i in range(11) ]

setBall = [ Ball() for i in range(20) ]

running = True
n = 0
# game main loop code

while running:
    handle_events()
    # for boy in team:
    #     boy.update()
    for ball in setBall:
        ball.update()
    clear_canvas()
    grass.draw()
    # for boy in team:
    #     boy.draw()
    for ball in setBall:
        ball.draw()
    update_canvas()

    delay(0.05)
# finalization code
