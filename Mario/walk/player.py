from pico2d import *

class Mario:
    def __init__(self):
        self.image = load_image('walk1.png')
        self.x = 100
        self.y = 90
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
        if self.dir == 1 or self.dir == -1:
            global n
            if n < 2:
                n += 1
                self.image = load_image('walk2.png')
            elif n >= 2:
                n = 1
                self.image = load_image('walk1.png')
            self.x += 5 * self.dir

    # def walkRight(self):




    def draw(self):
        self.image.clip_draw(self.frame, 0, 32, 32, self.x, self.y)
        # self.image.draw

def handle_events():
    global running
    global player
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
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                player.dir -= 1
            elif event.key == SDLK_LEFT:
                player.dir += 1


k = 'walk'
n = 1


open_canvas()

running = True
player = Mario()

while running:
    handle_events()
    player.update()
    clear_canvas()
    player.draw()
    update_canvas()

    delay(0.05)