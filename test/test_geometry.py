import math
import unittest

from exception.exceptions import SamePointException
from model.geometry import Polar
from model.geometry import Rect, Cartesian


class CoordinatesTest(unittest.TestCase):

    def test_creation(self):
        polar = Polar(100, 90)
        self.assertEqual(polar.degrees, 90)
        self.assertEqual(polar.radians, math.pi / 2)

    def test_eq(self):
        polar = Polar(100, 0)
        other = Polar(100, 0)
        self.assertEqual(polar, other)

    def test_anti_clockwise_movement(self):
        polar = Polar(100, 0)

        polar.plus_angle(45)
        self.assertEqual(polar.degrees, 45)
        self.assertEqual(polar.radians, math.pi / 4)
        self.assertGreaterEqual(polar.to_cartesian().x, 70.71)
        self.assertGreaterEqual(polar.to_cartesian().y, 70.71)

        polar.plus_angle(45)
        self.assertEqual(polar.degrees, 90)
        self.assertEqual(polar.radians, math.pi / 2)
        self.assertEqual(polar.to_cartesian().x, 0)
        self.assertEqual(polar.to_cartesian().y, 100)

        polar.plus_angle(360)
        self.assertEqual(polar.degrees, 90)
        self.assertEqual(polar.radians, math.pi / 2)
        self.assertEqual(polar.to_cartesian().x, 0)
        self.assertEqual(polar.to_cartesian().y, 100)

    def test_clockwise_movement(self):
        polar = Polar(100, 0)

        polar.plus_angle(-90)
        self.assertEqual(polar.degrees, 270)
        self.assertEqual(polar.radians, math.pi * 3 / 2)
        self.assertEqual(polar.to_cartesian().x, 0)
        self.assertEqual(polar.to_cartesian().y, -100)

        polar.plus_angle(-90)
        self.assertEqual(polar.degrees, 180)
        self.assertEqual(polar.radians, math.pi)
        self.assertEqual(polar.to_cartesian().x, -100)
        self.assertEqual(polar.to_cartesian().y, 0)

        polar.plus_angle(-360)
        self.assertEqual(polar.degrees, 180)
        self.assertEqual(polar.radians, math.pi)
        self.assertEqual(polar.to_cartesian().x, -100)
        self.assertEqual(polar.to_cartesian().y, 0)

    def test_point_in_triangle(self):
        cart = Cartesian(0, 0)
        self.assertTrue(cart.is_in_triangle(Cartesian(-1, -1), Cartesian(0, 1), Cartesian(1, -1)))
        self.assertFalse(cart.is_in_triangle(Cartesian(-1, -1), Cartesian(0, -1), Cartesian(1, -1)))


class TestRect(unittest.TestCase):

    def test_creation(self):
        m_expected = 1
        b_expected = 0
        rect = Rect(Cartesian(1, 1), Cartesian(2, 2))
        self.assertEqual(m_expected, rect.m)
        self.assertEqual(b_expected, rect.b)

        m_expected = 1
        b_expected = -1
        rect = Rect(Cartesian(2, 1), Cartesian(3, 2))
        self.assertEqual(m_expected, rect.m)
        self.assertEqual(b_expected, rect.b)

        # same point is not going to define a rect
        with self.assertRaises(SamePointException):
            Rect(Cartesian(1, 1), Cartesian(1, 1))

    def test_contains(self):
        rect = Rect(Cartesian(2, 1), Cartesian(3, 2))
        self.assertTrue(rect.contain(Cartesian(4, 3)))
        self.assertTrue(rect.contain(Cartesian(0, -1)))
        self.assertFalse(rect.contain(Cartesian(0, 0)))
