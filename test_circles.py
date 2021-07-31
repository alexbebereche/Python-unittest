import unittest
from circles import circle_area
from math import pi


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # test areas when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi) # correct to 7 decimal places => assume they are equal
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)


    def test_values(self):
        # errors raised when necessary
        self.assertRaises(ValueError, circle_area, -2)  # what i expect, function, param of fct

    def test_types(self):
        # errors raised when necessary
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")