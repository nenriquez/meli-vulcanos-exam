import math

from exception.exceptions import SamePointException
from model.config import DECIMAL_PRECISION

RADIO = 360
HALF_RADIO = 180


class Cartesian:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_polar(self):
        radio = math.hypot(self.x, self.y)
        angle = math.degrees(math.atan2(self.y, self.x))
        return Polar(radio, angle)

    """
    Inspired on http://stackoverflow.com/a/34093754/3046101
    :return true if this this coor is inside the triangle defined by p0, p1 and p2
    """
    def is_in_triangle(self, p0, p1, p2):
        d_x = self.x - p2.x
        d_y = self.y - p2.y

        d_x21 = p2.x - p1.x
        d_y12 = p1.y - p2.y

        D = d_y12 * (p0.x - p2.x) + d_x21 * (p0.y - p2.y)
        s = d_y12 * d_x + d_x21 * d_y
        t = (p2.y - p0.y) * d_x + (p0.x - p2.x) * d_y

        if D < 0:
            return s <= 0 and t <= 0 and s + t >= D

        return s >= 0 and t >= 0 and s + t <= D

    def distance(self, p):
        d_x = p.x - self.x
        d_y = p.y - self.y
        return math.sqrt(d_x ** 2 + d_y ** 2)

class Polar:

    def __init__(self, radio, angle):
        """
        :param radio (int): radio
        :param angle (float): angle in degrees
        """
        self._radio = radio
        self._angle = angle

    @property
    def radians(self):
        return math.radians(self._angle)

    @property
    def degrees(self):
        return self._angle

    @property
    def radio(self):
        return self._radio

    def plus_angle(self, value):
        """
        Plus value to current angle.

        :param value: angle in degrees to rotate
        """
        self._angle += value

        if self._angle > RADIO:
            self._angle -= RADIO

        if self._angle < 0:
            self._angle += RADIO

    def set_radio(self, value):
        self._radio = value

    def to_cartesian(self):
        # precision problem, cos(pi/2) != 0
        x = self._radio * round(math.cos(self.radians), DECIMAL_PRECISION)
        y = self._radio * round(math.sin(self.radians), DECIMAL_PRECISION)
        return Cartesian(x, y)

    def __eq__(self, other):
        return self.radio == other.radio and self.degrees == other.degrees


class Rect:

    def __init__(self, p1, p2):
        """
        Define rect between p1 and p2.

        y = m.x + b
        a.x + b.y + c = 0

        =>

        y = (-a.x - c)/b  => y = -a/b.x -c/b

        =>

        m = -a/b
        b = -c/b

        :param p1: cartesian p1 coordinates
        :param p2: cartesian p2 coordinates
        """
        if p1.x == p2.x and p1.y == p2.y:
            raise SamePointException(p1)

        a = p1.y - p2.y
        b = p2.x - p1.x
        c = p1.x * p2.y - p2.x * p1.y

        if b == 0:
            self.m = 0
            self.b = 0
        else:
            self.m = (-1) * a / b
            self.b = (-1) * c / b

    def contain(self, p):
        # i will fix precision to 10 decimals
        return round(p.y, DECIMAL_PRECISION) == round(self.m * p.x + self.b, DECIMAL_PRECISION)

    def __eq__(self, other):
        return self.m == other.m and self.b == other.b