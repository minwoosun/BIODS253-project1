import turtle

BOUNDING_HEIGHT = 800
BOUNDING_WIDTH = 1200
HOUSE_HEIGHT = 500
HOUSE_WIDTH = 700


def draw_bounding_box(t):
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

def draw_house(t):
    t.penup()
    t.left(90)
    t.forward((BOUNDING_WIDTH - HOUSE_WIDTH)/2)
    t.pendown()
    t.left(90)
    t.forward(HOUSE_HEIGHT)
    t.right(90)
    t.forward(HOUSE_WIDTH)
    t.right(90)
    t.forward(HOUSE_HEIGHT)

def main():
    t = turtle.Turtle()
    draw_bounding_box(t)
    draw_house(t)
    turtle.done()

if __name__ == "__main__":
    main()

