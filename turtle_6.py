import turtle
wn = turtle.Screen()
wn.bgcolor('green')
jose = turtle.Turtle()
jose.shape('turtle')
jose.color('blue')
jose.up()


for i in range(10):
    jose.forward(50)
    jose.stamp()
   
    jose.forward(-50)
    jose.right(36)
   

wn.exitonclick()