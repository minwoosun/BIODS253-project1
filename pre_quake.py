"""Draw a neighborhood before the earthquake.
"""

import turtle
from house import *


def single_house_scene(t, tilt= 0, scale=1, right_offset=0, crack=False):
    """Draw a single house scene.

    Parameters
    ----------
    t : turtle.Turtle
        The turtle to draw with.
    scale : float
        The scale of the house, by default 1
    right_offset : float
        rightward offset from the center of the bounding box
        (negative values denote leftward offset), default is 0
    """

    # Draw Frame
    draw_house(t, scale=scale, right_offset=right_offset, tilt= tilt)
    # Draw front door
    draw_door(
        t, DOOR_WIDTH, DOOR_HEIGHT, scale=scale, right_offset=right_offset, tilt=tilt)
    # Draw windows
    if crack:
        pass
    else:
        draw_all_windows(
            t, windows_per_row=4, scale=scale, right_offset=right_offset, tilt= tilt
        )


    # Draw Garage Doors
    draw_all_garages(
        t, GARAGE_DOOR_WIDTH, GARAGE_DOOR_HEIGHT, scale=scale,
        right_offset=right_offset, tilt=tilt
    )
    # Draw one tree
    t.setheading(0+tilt)
    t.goto(
        STARTING_X + right_offset +
        (BOUNDING_WIDTH - HOUSE_WIDTH * scale) / 2 -
        FULL_TREE_WIDTH * scale, STARTING_Y
    )
    draw_tree(t, scale=scale)


if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(0)
    draw_bounding_box(t)
    nominal_scale_factor = 0.3
    reduced_scale_factor = 0.9
    nominal_offset = 400
    single_house_scene(
        t, tilt=0, scale=nominal_scale_factor,right_offset=nominal_offset
    )

    single_house_scene(
        t, tilt=0, scale=nominal_scale_factor * reduced_scale_factor, right_offset=0
    )

    single_house_scene(
        t, tilt=0, scale=nominal_scale_factor, right_offset=-nominal_offset
    )
    draw_all_clouds(t, CLOUD_X, CLOUD_HEIGHT)
    turtle.done()
