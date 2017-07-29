from helper import *

def test():
    assert line_intersection((1,5),(1,3)) == (1, 3)
    assert line_intersection((1,2),(3,4)) is None
    assert line_intersection((1,1),(3,4)) is None
    assert line_intersection((1,1),(3,3)) is None
    assert line_intersection((1,2),(3,3)) is None
    assert line_intersection((1,2),(2,3)) == (2, 2)
    assert line_intersection((1,3),(2,3)) == (2, 3)
    assert line_intersection((1,3),(2,4)) == (2, 3)
    assert line_intersection((1,2),(2,4)) == (2, 2)
    assert line_intersection((1,5),(2,4)) == (2, 4)
    assert line_intersection((1,5),(1,4)) == (1, 4)
    assert line_intersection((1,5),(1,5)) == (1, 5)
    assert line_intersection((1,1),(1,1)) == (1, 1)
    assert line_intersection((2,2),(1,1)) is None
    assert line_intersection((3,4),(1,2)) is None
    assert line_intersection((2,4),(1,2)) == (2, 2)
    assert line_intersection((2,4),(1,5)) == (2, 4)
    assert line_intersection((2,4),(1,4)) == (2, 4)
    assert line_intersection((2,4),(2,4)) == (2, 4)
    assert line_intersection((2,4),(2,5)) == (2, 4)
    assert line_intersection((2,4),(1,5)) == (2, 4)
    assert line_intersection((2,4),(1,3)) == (2, 3)
    assert line_intersection((2,4),(1,2)) == (2, 2)

    assert intersection(Rect(1, 1, 2, 4), Rect(3, 5, 3, 1)) == Rect(3, 5, 0, 0)
    assert intersection(Rect(1, 1, 2, 4), Rect(4, 4, 3, 1)) is None
    assert intersection(Rect(1, 1, 2, 4), Rect(3, 4, 3, 1)) == Rect(3, 4, 0, 1)
    assert intersection(Rect(1, 1, 3, 3), Rect(3, 2, 2, 3)) == Rect(3, 2, 1, 2)
    assert intersection(Rect(1, 2, 3, 3), Rect(3, 1, 2, 4)) == Rect(3, 2, 1, 3)

def line_intersection(a, b):
    if a[0] < b[0] or (a[0] == b[0] and a[0]-a[1] < b[0]-b[1]):
        b, a = (a, b)

    results = [(an, bn) for bn in b for an in a if an - bn <= 0]

    if not results: return None
    if len(results) >= 2: return a

    return results[0]

def intersection(r1, r2):
    def get_line(r, dim):
        a0, al = (r[0][dim], r[1][dim])
        return (a0, a0+al)
    def get_line_intersection(dim):
        lines = [get_line(r, dim) for r in [r1, r2]]
        return line_intersection(*lines)

    line_intersections = [get_line_intersection(dim) for dim in range(2)]

    if not all(line_intersections): return None

    (x1, x2), (y1, y2) = line_intersections
    return Rect(x1, y1, x2-x1, y2-y1)

class Rect(R):
    def __init__(self, x=0, y=0, w=0, h=0):
        super().__init__(x=x, y=y, w=w, h=h)

    def __len__(self): 2

    def __getitem__(self, index):
        if index == 0: return Point(self.x, self.y)
        if index == 1: return Point(self.w, self.h)
        else: raise IndexError

    def __setitem__(self, index, value):
        if index == 0:
            x, y = value
            self.x = x
            self.y = y
        if index == 1:
            w, h = value
            self.w = w
            self.h = h
        else:
            raise IndexError

class Point(R):
    def __init__(self, x=0, y=0):
        super().__init__(x=x, y=y)

    def __len__(self): 2

    def __getitem__(self, index):
        if index == 0: return self.x
        if index == 1: return self.y
        else: raise IndexError

    def __setitem__(self, index, value):
        if index == 0: self.x = value
        if index == 1: self.y = value
        else: raise IndexError
