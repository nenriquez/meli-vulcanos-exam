
class VirtualMethodException(Exception):
    def __init__(self, method_name):
        Exception.__init__(self, "Virtual Method: {} needs to be implemented.".format(method_name))


class SamePointException(Exception):
    def __init__(self, point):
        Exception.__init__(self, "Rect needs to be created with two diferents points ({}, {}).".format(point.x, point.y))
