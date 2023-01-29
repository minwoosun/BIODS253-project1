import turtle
import math

BOUNDING_HEIGHT = 800
BOUNDING_WIDTH = 1200
HOUSE_HEIGHT = 500
HOUSE_WIDTH = 700
TREE_HEIGHT = 250
TREE_WIDTH = 30
STARTING_X = -550
STARTING_Y = -400
WINDOW_SIZE = 80
FIRST_STORY = 250
SECOND_STORY = 150
N_WINDOWS = 8

TRUNCK_COLOR = 'brown'
BRANCH_COLOR = 'green'
BRANCH_ANGLE = 180-45

def draw_bounding_box(t):
    t.fillcolor('lightblue')
    t.penup()
    t.goto(STARTING_X, STARTING_Y)
    t.seth(0)
    t.pendown()
    t.begin_fill()
    t.forward(BOUNDING_WIDTH)
    t.left(90)
    t.forward(BOUNDING_HEIGHT)
    t.left(90)
    t.forward(BOUNDING_WIDTH)
    t.left(90)
    t.forward(BOUNDING_HEIGHT)
    t.end_fill()

def draw_house(t):
    t.penup()
    t.goto(STARTING_X + (BOUNDING_WIDTH - HOUSE_WIDTH)/2, STARTING_Y)
    t.seth(90)
    t.fillcolor("#f571cb")
    t.begin_fill()
    t.pendown()
    t.forward(HOUSE_HEIGHT)
    t.right(90)
    t.forward(HOUSE_WIDTH)
    t.right(90)
    t.forward(HOUSE_HEIGHT)
    t.end_fill()


def draw_branches(t, tree_width):
    """Draw branches for the tree

    Params:
        t: the Turtle object.
        tree_width: width of the tree
    """

    # isosceles right triangle length
    length = tree_width * math.sqrt(2)

    t.fillcolor(BRANCH_COLOR)
    t.begin_fill()
    t.forward(tree_width)
    t.left(BRANCH_ANGLE)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(BRANCH_ANGLE)
    t.forward(tree_width)
    t.end_fill()
    t.penup()
    t.left(90)
    t.forward(tree_width)
    t.right(90)
    t.pendown()

def draw_tree(t):
    """Draw a tree 

    Params:
        t: the Turtle object.
    """

    # tree trunk
    t.fillcolor(TRUNCK_COLOR)
    t.begin_fill()
    t.left(90)
    t.forward(TREE_HEIGHT)
    t.right(90)
    t.forward(TREE_WIDTH)
    t.right(90)
    t.forward(TREE_HEIGHT)
    t.right(90)
    t.forward(TREE_WIDTH / 2 )
    t.end_fill()

    # move to branch location
    t.penup()
    t.right(90)
    t.forward(TREE_HEIGHT)
    t.right(90)
    t.pendown()

    # draw branches
    draw_branches(t, TREE_WIDTH * 4) 
    draw_branches(t, TREE_WIDTH * 3) 
    draw_branches(t, TREE_WIDTH * 2) 


def draw_all_trees(t):
    """Draw two trees, one on each side of the house

    Params:
        t: the Turtle object.
    """

    # get width space for the two sides of the house
    side_widths = (BOUNDING_WIDTH - HOUSE_WIDTH)

    # get half the width space for one of the side 
    half_w = side_widths / 4

    # set starting point to half of side width - half tree width 
    gap =  half_w - TREE_WIDTH/2

    # move to starting point
    t.left(90)
    t.forward(gap)

    # draw right tree 
    draw_tree(t)

    # move to the other side (1/2 side width + house width)
    gap = half_w + HOUSE_WIDTH

    # move to left tree 
    t.penup()
    t.goto(400.00, -400.00)
    t.pendown()
    t.right(180)
    t.forward(gap)
    t.right(180)

    # draw left tree 
    draw_tree(t)


def draw_all_windows(t, windows_per_row):
    """Draw four windows on the house

    Params:
        t: the Turtle object.
    """
    start_loc = t.pos()
    margin = (HOUSE_WIDTH - (2 * windows_per_row - 1) * WINDOW_SIZE) / 2

    t.penup()
    t.seth(90)
    t.forward(FIRST_STORY)
    t.left(90)
    t.forward(margin)
    t.pendown()
    draw_window(t)
    for i in range(windows_per_row - 1):
        t.penup()
        t.forward(2*WINDOW_SIZE)
        t.pendown()
        draw_window(t)

    t.penup()
    t.seth(90)
    t.forward(SECOND_STORY)
    t.right(90)
    t.forward(2*(windows_per_row - 1) * WINDOW_SIZE)
    t.left(180)
    t.pendown()
    draw_window(t)
    for i in range(windows_per_row - 1):
        t.penup()
        t.seth(180)
        t.forward(2*WINDOW_SIZE)
        t.pendown()
        draw_window(t)

    t.penup()
    t.goto(start_loc)
    t.pendown()
    t.seth(270)


def draw_window(t):
    t.fillcolor("darkgray")
    t.begin_fill()
    for i in range(4):
        t.forward(WINDOW_SIZE)
        t.left(90)
    t.end_fill()


def draw_door(t, door_width, door_height):
    """Draw door of house in the middle and touching the bottom

    Params:
        t: the Turtle object.
    """

    doorknob = door_width / 15

    # save starting position for later
    start_loc = t.pos()

    # after drawing house, get to door starting point
    t.right(90)
    t.forward(HOUSE_WIDTH * 0.75)

    # draw door
    t.fillcolor('#03a9fc')
    t.begin_fill()
    t.right(90)
    t.forward(door_height)
    t.left(90)
    t.forward(door_width)
    t.left(90)
    t.forward(door_height)
    t.end_fill()

    # draw doorknob
    t.left(90)
    t.forward(door_width * 0.8)
    t.left(90)
    t.penup()
    t.forward(door_height / 2)
    t.pendown()
    draw_circle(t, doorknob, '#f5d60f')
    t.penup()
    t.left(180)
    t.forward(door_height / 2)

    # go back to position before drawing door
    t.goto(start_loc)

    # go back to orientation before drawing door
    #t.right(90)


def draw_garage(t, garage_width, garage_height):
    """Draw outline of a garage

    Params:
        t: the Turtle object.
        garage_width: the width of the garage
        garage_height: the height of the garage
    """

    t.pendown()
    t.fillcolor('grey')
    t.begin_fill()
    t.seth(90)
    t.forward(garage_height)
    t.right(90)
    t.forward(garage_width)
    t.right(90)
    t.forward(garage_height)
    t.end_fill()


def draw_garage_window(t, window_width, window_height):
    """Draw one garage window

    Params:
        t: the Turtle object.
        window_width: the width of the window
        window_height: the height of the window
    """

    t.pendown()
    t.fillcolor('white')
    t.begin_fill()
    t.forward(window_height)
    t.right(90)
    t.forward(window_width)
    t.right(90)
    t.forward(window_height)
    t.right(90)
    t.forward(window_width)
    t.penup()
    t.end_fill()


def draw_garage_windows(t, window_width, window_height, garage_width, garage_height):
    """Draw two garage windows 

    Params:
        t: the Turtle object.
        window_width: the width of each window
        window_height: the height of each window
        garage_width: the width of the garage
        garage_height: the height of the garage
    """
    # set starting location for window 1
    window_x = garage_width/2.2
    window_y = 3 * garage_height/4

    # move to window 1 location
    t.penup()
    t.right(90)
    t.forward(window_x)
    t.right(90)
    t.forward(window_y)

    # draw window 1
    draw_garage_window(t, window_width, window_height)

    # move to window 2 location
    t.forward(window_x)
    t.right(90)

    # draw window 2
    draw_garage_window(t, window_width, window_height)


def draw_all_garages(t, garage_width, garage_height):
    """Draw two garages next to each other

    Params:
        t: the Turtle object.
        garage_width: the width of the garage
        garage_height: the height of the garage
    """
    window_width = garage_width/3
    window_height = garage_height/7
    t.penup()

    # draw garage 1 
    t.goto(STARTING_X + BOUNDING_WIDTH/2, STARTING_Y)
    draw_garage(t, garage_width, garage_height)
    draw_garage_windows(t, window_width, window_height, garage_width, garage_height)

    # draw garage 2
    t.goto(STARTING_X + BOUNDING_WIDTH/2 + 6 * garage_width/5, STARTING_Y)
    draw_garage(t, garage_width, garage_height)
    draw_garage_windows(t, window_width, window_height, garage_width, garage_height)


def draw_circle(t, rad, col="white"):
    """Draw a circle.
    Params:
        t: the Tutle object
        rad: radius of the circle
        col: color of the circle
    """
    t.color(col,col)
    t.begin_fill()
    t.circle(rad)
    t.end_fill()
    t.pencolor("black")


def draw_cloud(t, rad=30, col="white", x_start=0, y_start=0):
    """Draw a cloud. 
    Params:
        t: the Tutle object
        rad: radius of the circle
        col: color of the circle
        x_start: x coordinate for starting pos
        y_start: y coordinate for starting pos
    """
    t.penup()
    t.goto(x_start, y_start)
    t.pendown()
    draw_circle(t, rad, col)
    t.right(90)
    draw_circle(t, rad, col)
    t.right(90)
    draw_circle(t, rad, col)
    t.right(90)
    draw_circle(t, rad, col)
    
  
def draw_all_clouds(t):
    """Draw two clouds.
    Params:
        t: the Tutle object.
    """
    draw_cloud(t, x_start=400, y_start=250)
    draw_cloud(t, x_start=450, y_start=250)
    draw_cloud(t, x_start=350, y_start=250)
    draw_cloud(t, x_start=-400, y_start=250)
    draw_cloud(t, x_start=-350, y_start=250)



def main(t):

    draw_bounding_box(t)
    draw_house(t)
    draw_door(t, HOUSE_WIDTH/8, HOUSE_HEIGHT/4)
    draw_all_windows(t, N_WINDOWS//2)
    draw_all_trees(t)
    draw_all_clouds(t)
    draw_all_garages(t, HOUSE_WIDTH/5, HOUSE_HEIGHT/4)


if __name__ == "__main__":
    t = turtle.Turtle()
    main(t)
    turtle.done()

