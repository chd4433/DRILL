from pico2d import *

class Mario:
    def __init__(self):
        self.image = load_image('walk1.png')
        self.x = 100
        self.y = 90
    def update(self):
        global  n
        if n<2:
            n += 1
            self.image = load_image('walk2.png')
        elif n>= 2:
            n = 1
            self.image = load_image('walk1.png')
        self.x += 5


    def draw(self):
        self.image.draw(0, 0, 32, 32)
        # self.image.draw

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


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