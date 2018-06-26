import turtle
turtle.setup(800, 600)

left = -300
right = 300
top = 200
bottom = -200

turtle1 = turtle.Turtle()
turtle1.hideturtle()

turtle1.penup()
turtle1.setposition(left, top)
turtle1.pendown()
turtle1.setposition(left, bottom)
turtle1.penup()
turtle1.setposition(right, top)
turtle1.pendown()
turtle1.setposition(right, bottom)

turtle2 = turtle.Turtle()
turtle2.shape("turtle")
turtle2.penup()

for i in range(2000):
    turtle2.forward(1)
    if turtle2.xcor() <= left or turtle2.xcor() >= right:
        turtle2.left(180)

turtle.exitonclick()
