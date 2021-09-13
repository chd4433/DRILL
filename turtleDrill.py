import turtle

player = turtle.Turtle()
screen = player.getscreen()

def left() :
    player.seth(180)
    player.forward(50)
def right():
    player.seth(0)
    player.forward(50)
def up() :
    player.seth(90)
    player.forward(50)
def down():
    player.seth(270)
    player.forward(50)
def reset():
    player.reset()

screen.onkeypress(left, "a")
screen.onkeypress(right, "d")
screen.onkeypress(up, "w")
screen.onkeypress(down, "s")
screen.onkeypress(reset, "Escape")
screen.listen() 
screen.mainloop() 

input()