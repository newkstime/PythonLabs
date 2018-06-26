import turtle
turtle.setup(800, 600)
turtle1 = turtle.Turtle()

def main():
    ecks(-200,50,315)
    ecks(-200,50,135)
    why(0,50,45)
    zee(200,85,180)

def wedge(forward=50, turn=90):
    turtle1.pendown()
    turtle1.forward(forward)
    turtle1.backward(forward)
    turtle1.left(turn)
    turtle1.forward(forward)

def ecks(x,y,z):
    turtle1.penup()
    turtle1.setposition(x,y)
    turtle1.left(z)
    wedge()
    turtle1.penup()
    turtle1.home()

def why(x,y,z):
    turtle1.penup()
    turtle1.setposition(x,y)
    turtle1.left(z)
    wedge()
    turtle1.penup()
    turtle1.home()
    turtle1.setposition(x,y)
    turtle1.pendown()
    turtle1.right(90)
    turtle1.forward(40)
    turtle1.penup()
    turtle1.home()

def zee(x,y,z):
    turtle1.setposition(x,y)
    turtle1.left(z)
    wedge(75,45)
    turtle1.forward(30)
    turtle1.right(225)
    turtle1.forward(80)

main()


turtle.exitonclick()
