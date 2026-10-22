import turtle

wn = turtle.Screen()

alex = turtle.Turtle()
distance = 50
angle = 90
for i in range(10):
  alex.forward(distance)
  alex.left(angle)
  distance = distance + 10
#   angle = angle - 3


wn.exitonclick()