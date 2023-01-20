import turtle

BOUNDING_HEIGHT = 800
BOUNDING_WIDTH = 1200
HOUSE_HEIGHT = 500
HOUSE_WIDTH = 700



t = turtle.Turtle()

t.penup()
t.setx(-1*BOUNDING_WIDTH/2)
t.pendown()
t.forward(BOUNDING_WIDTH)
t.left(90)
t.forward(BOUNDING_HEIGHT)
t.left(90)
t.forward(BOUNDING_WIDTH)
t.left(90)
t.forward(BOUNDING_HEIGHT)