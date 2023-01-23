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
    t.pendown()
    t.forward(HOUSE_HEIGHT)
    t.right(90)
    t.forward(HOUSE_WIDTH)
    t.right(90)
    t.forward(HOUSE_HEIGHT)


def draw_branches(t, tree_width):
    """Draw branches for the tree

    Params:
        t: the Turtle object.
        tree_width: width of the tree
    """

    t.fillcolor('green')
    t.begin_fill()
    t.forward(tree_width)
    t.left(135)
    t.forward(tree_width * 2 / math.sqrt(2))
    t.left(90)
    t.forward(tree_width * 2 / math.sqrt(2))
    t.left(135)
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
    t.fillcolor('brown')
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

    # move to right tree
    gap = (BOUNDING_WIDTH - HOUSE_WIDTH)/4 - TREE_WIDTH/2
    t.left(90)
    t.forward(gap)

    # draw right tree 
    draw_tree(t)

    # move to left tree 
    gap = (BOUNDING_WIDTH - HOUSE_WIDTH)/4 + HOUSE_WIDTH
    t.penup()
    t.goto(400.00, -400.00)
    t.pendown()
    t.right(180)
    t.forward(gap)
    t.right(180)

    # draw left tree 
    draw_tree(t)


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


def main():
    t = turtle.Turtle()
    draw_bounding_box(t)
    draw_house(t)
    draw_all_trees(t)
    draw_all_clouds(t)
    draw_all_garages(t, HOUSE_WIDTH/5, HOUSE_HEIGHT/4)
    turtle.done()

if __name__ == "__main__":
    main()

