from pico2d import *

WIDTH, HEIGHT = 1280, 1024


class Mario:
    def __init__(self):
        self.image = load_image('idle\idle.png')
        self.x = 100
        self.y = 200
        self.frame = 0
        self.dir = 0
    def update(self):
        # global n
        # if n<2:
        #     n += 1
        #     self.image = load_image('walk2.png')
        # elif n>= 2:
        #     n = 1
        #     self.image = load_image('walk1.png')
        # self.x += 5
        global direction
        if self.dir == 1 or self.dir == -1:
            global n
            if n < 2:
                n += 1
                self.image = load_image('walk\walk2.png')
            elif n >= 2:
                n = 1
                self.image = load_image('walk\walk1.png')
            self.x += 5 * self.dir
        elif self.dir == 0:
            self.image = load_image('idle\idle.png')
        if direction == 1:
            global m
            global jumpCount
            jumpSize = 10
            if m < 2:
                self.image = load_image('jump\jump1.png')
                jumpCount += 1
                self.y += jumpSize
                if jumpCount >= 15:
                    m += 1
            elif m >= 2:
                self.image = load_image('jump\jump2.png')
                jumpCount -= 1
                self.y -= jumpSize
                if jumpCount == 0:
                    m = 1
                    direction = 0

    def draw(self):
        self.image.clip_draw(self.frame, 0, 32, 32, self.x, self.y,120,120)
        # self.image.draw

class Map:
    def __init__(self):
        self.image = load_image('map\mapsize.png')

    def update(self):






def handle_events():
    global running
    global player
    global direction
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                player.dir += 1
            elif event.key == SDLK_LEFT:
                player.dir -= 1
            elif event.key == SDLK_UP:
                direction = 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                player.dir -= 1
            elif event.key == SDLK_LEFT:
                player.dir += 1



k = 'walk'
n = 1
m = 1
direction = 0
jumpCount = 0;

open_canvas(WIDTH, HEIGHT)

background = load_image('map\mapsize.png')

running = True
player = Mario()

while running:
    handle_events()
    player.update()
    clear_canvas()
    background.draw(13721 // 2, HEIGHT // 2)
    player.draw()
    update_canvas()

    delay(0.05)