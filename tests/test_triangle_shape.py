from nose.tools import raises
from sdt.shapes.shape_factory import ShapeFactory

ShapeFactory.initialize()


def test_equilateral():
    triangle = ShapeFactory.drawTriangle(1, 1, 1).getType()
    assert triangle == 'Equilateral Triangle'


def test_isosceles():
    triangle1 = ShapeFactory.drawTriangle(1, 1, 2).getType()
    triangle2 = ShapeFactory.drawTriangle(2, 1, 1).getType()
    assert triangle1 == 'Isosceles Triangle'
    assert triangle2 == 'Isosceles Triangle'


def test_scalene():
    triangle = ShapeFactory.drawTriangle(1, 2, 1).getType()
    assert triangle == 'Scalene Triangle'


@raises(Exception)
def test_draw_triangle_without_params():
    triangle = ShapeFactory.drawTriangle()


@raises(Exception)
def test_draw_triangle_with_invalid_value():
    triangle = ShapeFactory.drawTriangle(0, 0, 0)


@raises(Exception)
def test_draw_triangle_with_invalid_value():
    triangle = ShapeFactory.drawTriangle('a', 'b', 'c')
