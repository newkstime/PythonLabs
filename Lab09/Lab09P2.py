import turtle
turtle.setup(800, 600)
turtle1 = turtle.Turtle()

def halfM(turn):
    turtle1.penup()
    turtle1.home()
    turtle1.pendown()
    turtle1.left(turn)
    turtle1.forward(50)
    turtle1.left(270-turn)
    turtle1.forward(100)

halfM(45)
halfM(135)

turtle.exitonclick()
