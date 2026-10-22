import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')
tess = turtle.Turtle()
alex = turtle.Turtle()

tess.pensize(5)
alex.color('hotpink')

tess.forward(120)
tess.left(120)
tess.forward(120)
tess.left(120)
tess.forward(120)
tess.left(120)

tess.right(180)
tess.forward(120)

alex.forward(75)
alex.left(90)
alex.forward(75)
alex.left(90)
alex.forward(75)
alex.left(90)
alex.forward(75)
alex.left(90)

wn.exitonclick()