import turtle
count =5

turtle.penup()
turtle.goto(-250,250)
turtle.pendown()

while(count>=0):
    turtle.forward(500)
    turtle.right(180)
    turtle.forward(500)
    turtle.left(90)
    turtle.penup()
    turtle.forward(100)
    turtle.left(90)
    turtle.pendown()
    count -=1

turtle.penup()
turtle.goto(-250,250)
turtle.right(90)
turtle.pendown()

while(count<5):
    turtle.forward(500)
    turtle.right(180)
    turtle.forward(500)
    turtle.right(90)
    turtle.penup()
    turtle.forward(100)
    turtle.right(90)
    turtle.pendown()
    count +=1



turtle.exitonclick()
    
