#!/usr/bin/env python3

from PIL import Image
import turtle
import matplotlib.testing.compare as mpcompare
import unittest
import tempfile
import os.path
import house


class TestShapes(unittest.TestCase):
    def _compare_canvas_to_expected(self, expected_filename):
        ''' compares the current canvas to an expected file.
        Returns None if and only if the files are identical'''

        TOLERANCE = 1.0 # somewhere between 0 and 255, higher is more lax.

        with tempfile.TemporaryDirectory() as tmp_dirname:
            actual_ps = os.path.join(tmp_dirname, 'canvas.ps')
            actual_png = os.path.join(tmp_dirname, 'canvas.png')
            canvas = turtle.getcanvas()
            
            # canvas generates a postscript file, but we have to convert it to a png in
            # order to compare it using matplotlib's library
            canvas.postscript(file=actual_ps)
            with Image.open(actual_ps) as im:
                im.save(actual_png)
            return mpcompare.compare_images(expected_filename, actual_png, TOLERANCE)


    def setUp(self):
        # this is run before every test
        turtle.reset()
        turtle.speed("fastest")
        turtle.tracer(0,0)
        turtle.setup(1200, 1200)
        turtle.screensize(canvwidth=1200, canvheight=1200, bg=None)

    def test_full_image(self):

        t = turtle.getturtle()
        house.main(t)
        turtle.hideturtle()

        # compare this 20,20,20 turtle against the well-known turtle png
        self.assertIsNone(self._compare_canvas_to_expected(expected_filename='testdata/house.png'))


if __name__ == '__main__':
    unittest.main()
