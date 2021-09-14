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
player.shape('turtle')
screen.onkey(left, "a")
screen.onkey(right, "d")
screen.onkey(up, "w")
screen.onkey(down, "s")
screen.onkey(reset, "Escape")
screen.listen() 
screen.mainloop() 

input()