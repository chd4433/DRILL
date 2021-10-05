from pico2d import *
import random


KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def Rand_events():
    global x, y
    x = random.randrange(0, 1281 - 1)
    y = random.randrange(0, 1024 - 1)

def Go_Charater():
    global charaterX, charaterY
    global x, y
    global right
    global PlusX, PlusY
    if charaterX <= x:
        right = True
    else:
        right = False
    if charaterX == x or charaterY == y:
        Rand_events()
    PlusX = (x - charaterX)
    PlusY = y - charaterY

    if abs(PlusY) <= abs(PlusX):
        PlusX /= abs(PlusY)
        PlusY /= abs(PlusY)
    else:
        PlusX /= abs(PlusX)
        PlusY /= abs(PlusX)
    charaterX += PlusX
    charaterY += PlusY


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False



open_canvas(KPU_WIDTH,KPU_HEIGHT)


kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
handle = load_image('hand_arrow.png')

running = True
right = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
charaterX, charaterY = KPU_WIDTH // 2, KPU_HEIGHT // 2
PlusX, PlusY = 0, 0
frame = 0
hide_cursor()
Rand_events()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    Go_Charater()
    if right == True:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, charaterX, charaterY)
    else:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, charaterX, charaterY)

    handle.draw(x, y)
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()
    delay(0.01)


close_canvas()