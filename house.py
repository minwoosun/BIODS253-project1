import turtle

BOUNDING_HEIGHT = 800
BOUNDING_WIDTH = 1200
HOUSE_HEIGHT = 500
HOUSE_WIDTH = 700



t = turtle.Turtle()

t.penup()
t.left(180)
t.forward(550)
t.left(90)
t.forward(400)
t.left(90)
t.pendown()
t.forward(BOUNDING_WIDTH)
t.left(90)
t.forward(BOUNDING_HEIGHT)
t.left(90)
t.forward(BOUNDING_WIDTH)
t.left(90)
t.forward(BOUNDING_HEIGHT)

turtle.done()
