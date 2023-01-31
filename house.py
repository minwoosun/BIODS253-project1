#!/usr/bin/env python3

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
CLOUD_X = [400, 450, 350, -400, -350]
CLOUD_HEIGHT = 250

TRUNCK_COLOR = "brown"
BRANCH_COLOR = "green"
BRANCH_ANGLE = 180 - 45
HOUSE_COLOR = "#f571cb"
SKY_COLOR = "lightblue"
PEN_COLOR = "black"
CLOUD_COLOR = "white"
WINDOW_COLOR = "darkgray"
DOOR_COLOR = "#03a9fc"
DOORKNOB_COLOR = "#f5d60f"
GARAGE_COLOR = "grey"
GARAGE_WINDOW_COLOR = "white"


def draw_circle(t, radius, color=CLOUD_COLOR):
    """Draw a circle.
    Params:
        t: the Turtle object
        radius: radius of the circle
        color: color of the circle
    """
    t.color(color, color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.pencolor(PEN_COLOR)


def draw_bounding_box(t):
    """Draw bounding box to put house in.
    Params:
        t: the Turtle object
    """
    t.fillcolor(SKY_COLOR)
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
    """Draw outline of house and make it pink.
    Params:
        t: the Turtle object
    """
    t.penup()
    t.goto(STARTING_X + (BOUNDING_WIDTH - HOUSE_WIDTH) / 2, STARTING_Y)
    t.seth(90)
    t.fillcolor(HOUSE_COLOR)
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
    t.forward(TREE_WIDTH / 2)
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
    side_widths = BOUNDING_WIDTH - HOUSE_WIDTH

    # get half the width space for one of the side
    half_w = side_widths / 4

    # set starting point to half of side width - half tree width
    gap = half_w - TREE_WIDTH / 2

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


def draw_window(t):
    """Draw a row of 4 windows

    Params:
        t: the Turtle object.
    """
    t.fillcolor(WINDOW_COLOR)
    t.begin_fill()
    for i in range(4):
        t.forward(WINDOW_SIZE)
        t.left(90)
    t.end_fill()


def draw_all_windows(t, windows_per_row):
    """Draw four windows on the house

    Params:
        t: the Turtle object.
        windows_per_row: number of windows per row
    """
    start_loc = t.pos()

    # distance between window and edge of house to be nicely spaced
    margin = (HOUSE_WIDTH - (2 * windows_per_row - 1) * WINDOW_SIZE) / 2

    t.penup()
    t.goto(STARTING_X + BOUNDING_WIDTH / 2 + HOUSE_WIDTH / 2, STARTING_Y)
    t.seth(90)
    t.forward(FIRST_STORY)
    t.left(90)
    t.forward(margin)
    t.pendown()
    draw_window(t)
    for i in range(windows_per_row - 1):
        t.penup()
        t.forward(2 * WINDOW_SIZE)
        t.pendown()
        draw_window(t)

    t.penup()
    t.seth(90)
    t.forward(SECOND_STORY)
    t.right(90)
    t.forward(2 * (windows_per_row - 1) * WINDOW_SIZE)
    t.left(180)
    t.pendown()
    draw_window(t)
    for i in range(windows_per_row - 1):
        t.penup()
        t.seth(180)
        t.forward(2 * WINDOW_SIZE)
        t.pendown()
        draw_window(t)

    t.penup()
    t.goto(start_loc)
    t.pendown()
    t.seth(270)


def draw_door(t, door_width, door_height):
    """Draw door of house, touching the bottom

    Params:
        t: the Turtle object.
        door_width: width of door
        door_height: height of door
    """

    doorknob = door_width / 15

    # save starting position for later
    start_loc = t.pos()

    # after drawing house, get to door starting point
    t.penup()
    t.goto(STARTING_X + BOUNDING_WIDTH / 2 - HOUSE_WIDTH / 4, STARTING_Y)
    t.seth(90)

    # draw door
    t.pendown()
    t.fillcolor(DOOR_COLOR)
    t.begin_fill()
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
    draw_circle(t, doorknob, DOORKNOB_COLOR)
    t.penup()
    t.left(180)
    t.forward(door_height / 2)
    t.pendown()
    t.left(90)
    t.forward(door_width * 0.2)
    t.penup()

    # go back to position before drawing door
    t.goto(start_loc)


def draw_rectangle(t, width, height, color):
    """Draw a rectangle starting at the bottom left corner

    Params:
        t: the Turtle object.
        width: the width of the rectangle
        height: the height of the rectangle
        color: the color of the rectangle
    """
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.seth(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
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
    window_x = garage_width / 2.2
    window_y = 3 * garage_height / 4

    # move to window 1 location
    t.penup()
    t.right(180)
    t.forward(window_x)
    t.right(90)
    t.forward(window_y)

    # draw window 1
    draw_rectangle(t, window_width, window_height, GARAGE_WINDOW_COLOR)

    # move to window 2 location
    t.forward(window_x)

    # draw window 2
    draw_rectangle(t, window_width, window_height, GARAGE_WINDOW_COLOR)


def draw_all_garages(t, garage_width, garage_height):
    """Draw two garages next to each other

    Params:
        t: the Turtle object.
        garage_width: the width of the garage
        garage_height: the height of the garage
    """
    window_width = garage_width / 3
    window_height = garage_height / 7
    t.penup()
    garage_x_start = STARTING_X + BOUNDING_WIDTH / 2
    garage_x_locations = [0, 6 * garage_width / 5]

    # draw garages at garage_x_locations
    for i in range(len(garage_x_locations)):
        t.goto(garage_x_start + garage_x_locations[i], STARTING_Y)
        draw_rectangle(t, garage_width, garage_height, GARAGE_COLOR)
        t.right(180)
        t.forward(garage_width)
        draw_garage_windows(t, window_width, window_height, garage_width, garage_height)


def draw_cloud(t, radius=30, color=CLOUD_COLOR, x_start=0, y_start=0):
    """Draw a cloud. 
    Params:
        t: the Turtle object
        radius: radius of the circle
        color: color of the circle
        x_start: x coordinate for starting pos
        y_start: y coordinate for starting pos
    """
    t.penup()
    t.goto(x_start, y_start)
    t.pendown()
    draw_circle(t, radius, color)
    t.right(90)
    draw_circle(t, radius, color)
    t.right(90)
    draw_circle(t, radius, color)
    t.right(90)
    draw_circle(t, radius, color)


def draw_all_clouds(t, cloud_x, cloud_height):
    """Draw two clouds.
    Params:
        t: the Turtle object.
        cloud_x: starting x positions
        cloud_height: starting cloud height
    """
    for position in cloud_x:
        draw_cloud(t, x_start=position, y_start=cloud_height)


def main(t):

    draw_bounding_box(t)
    draw_house(t)
    draw_door(t, HOUSE_WIDTH / 8, HOUSE_HEIGHT / 4)
    draw_all_windows(t, N_WINDOWS // 2)
    draw_all_trees(t)
    draw_all_clouds(t, CLOUD_X, CLOUD_HEIGHT)
    draw_all_garages(t, HOUSE_WIDTH / 5, HOUSE_HEIGHT / 4)


if __name__ == "__main__":
    t = turtle.Turtle()
    main(t)
    turtle.done()
