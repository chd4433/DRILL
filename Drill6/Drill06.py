from pico2d import *

import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


x = 400
y = 90
end = True;
sequence = 0
angle=270
while (end == True):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    if(x<779 and sequence==0):
        x+=2
    if(x>=779 and sequence==0):
        sequence+=1
    if(y<555 and sequence==1):
        y+=2
    if(y>=555 and sequence==1):
        sequence+=1
    if(x>21 and sequence==2):
        x-=2
    if(x<=21 and sequence==2):
        sequence+=1
    if(y>90 and sequence==3):
        y-=2
    if(y<=90 and sequence==3):
        sequence=4
    if(x<400 and sequence==4):
        x+=2
    if(x>=400 and sequence==4):
        sequence+=1
    if(sequence==5):
        x=225*math.cos(angle/360*2*math.pi)+400
        y=225*math.sin(angle/360*2*math.pi)+300
        angle+=2
        if(angle==360):
            angle=0
        if(angle==270):
            sequence=0
    delay(0.01)




#close_canvas()
