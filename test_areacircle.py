from areacircle import area_of_circle
from math import pi
import unittest

class Test_Area_of_Circle_input(unittest.TestCase):
    def test_area(self):

        # Test radius > =0
        self.assertAlmostEqual(area_of_circle(1), pi)
        self.assertAlmostEqual(area_of_circle(0), 0)
        self.assertAlmostEqual(area_of_circle(3.5), pi*3.5**2)

    def test_value(self):
        self.assertRaises(ValueError, area_of_circle, -1)