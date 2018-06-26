import turtle
turtle.setup(800, 600)
turtle1 = turtle.Turtle()

hLine = 0
xStart = -100
xEnd = 50
y = 100

while hLine < 3:
    turtle1.penup()
    turtle1.setposition(xStart,y)
    turtle1.pendown()
    turtle1.setposition(xEnd,y)
    y -= 100
    hLine += 1

turtle1.penup()
turtle1.setposition(xStart,100)
turtle1.pendown()
turtle1.setposition(xStart, -100)

turtle.exitonclick()
