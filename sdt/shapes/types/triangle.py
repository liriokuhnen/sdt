import copy

from sdt.shapes.shape import Shape


class Triangle(Shape):

    """ Implementation of triangle Shape. """

    def draw(self, a, b, c):
        self.params_validate(a, b, c)
        if a == b == c:
            self._type = "Equilateral Triangle"
        elif a != b != c:
            self._type = "Scalene Triangle"
        else:
            self._type = "Isosceles Triangle"
        return copy.copy(self)

    def params_validate(self, a, b, c):
        if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
           raise Exception('Invalid param, please inform just numbers')
