import turtle

wn = turtle.Screen()
tes = turtle.Turtle()
wn.bgcolor('green')
tes.shape('turtle')
tes.color('blue')

tes.up()
dis = 5
for i in range(40):
     tes.stamp()
     tes.forward(dis)
     tes.left(24)
     dis = dis + 2

wn.exitonclick()